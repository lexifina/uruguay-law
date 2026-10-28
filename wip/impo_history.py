"""Rebuilds the history of a law or code from IMPO's consolidated text and IMPO's own notes.

IMPO (www.impo.com.uy/bases) gives, for each norm, the text in force today and, per article, notes such as

    Inciso 2º) redacción dada por: Ley Nº 18.719 de 27/12/2010 artículo 152.
    Literal Ñ) agregado/s por: Ley Nº 19.924 de 18/12/2020 artículo 86.
    Derogado/s por: Ley Nº 19.075 de 03/05/2013 artículo 26.
    TEXTO ORIGINAL: Ley Nº 18.331 de 11/08/2008 artículo 35.

with a link to the article as originally published (/bases/leyes-originales/...). Each article's history is the
original text, then one text per amending law in the order the laws took effect, ending with today's text.
Intermediate texts (an article amended by two or more laws on different days) are rebuilt only when IMPO's notes say
exactly what the later law did:

  * a later law *added* a lettered or numbered item: the earlier text is the later one without that item;
  * a later law gave a new wording to an item of an article an earlier law had rewritten whole, and IMPO links the
    earlier law's article as a TEXTO ORIGINAL: the earlier text is the one that law quotes.

Anything else is reported in the verification output and the article's intermediate text is not invented: the
article then changes once, on the last law's day, credited to all the laws IMPO names.
"""
from __future__ import annotations

import datetime as dt
import re
from dataclasses import dataclass, field

import fetch
from parse_text import impo_paragraphs, norm, strip_tags, wrap_width

KIND = {'redacción dada por': 'wording', 'redacción dada anteriormente por': 'wording-earlier',
        'agregado/s por': 'added', 'anteriormente agregado/s por': 'added-earlier',
        'derogado/s por': 'repealed', 'ver vigencia': 'vigencia'}
NOTE = re.compile(r'(?P<kind>redacción dada anteriormente por|redacción dada por|anteriormente agregado/s por|'
                  r'agregado/s por|derogado/s por|ver vigencia):\s*'
                  r'(?P<refs>(?:,?\s*(?:y\s+)?Ley Nº [\d.]+ de \d\d/\d\d/\d{4}\s+artículos?\s+[\d\s,y]+)+)', re.I)
REF = re.compile(r'Ley Nº (?P<n>[\d.]+) de (?P<d>\d\d)/(?P<m>\d\d)/(?P<y>\d{4})\s+artículos?\s+(?P<a>\d+)')


@dataclass
class Event:
    kind: str
    scope: str            # '' for the whole article, else e.g. 'Literal Ñ)', 'Inciso 2º)'
    law: str              # '18719'
    year: str
    art: str


@dataclass
class Article:
    key: str
    label: str
    current: list[str]
    events: list[Event] = field(default_factory=list)
    originals: list[tuple[str, str, str]] = field(default_factory=list)   # (law, year, art) under TEXTO ORIGINAL


def note_text(html: str) -> str:
    t = strip_tags(html.replace('<br>', '\n'))
    t = t.replace('\r\n', '\n')
    return re.sub(r'[ \t]+', ' ', t)


def parse_notes(html: str) -> tuple[list[Event], list[tuple[str, str, str]]]:
    t = note_text(html)
    events: list[Event] = []
    head, _, orig = t.partition('TEXTO ORIGINAL:')
    flat = re.sub(r'\s+', ' ', head)
    for m in NOTE.finditer(flat):
        before = flat[:m.start()]
        scope = re.split(r'(?<=\.)\s|\n', before)[-1].strip()
        scope = scope if re.match(r'(Inciso|Literal|Literales|Numeral|Numerales|Apartado|Párrafo)', scope) else ''
        for r in REF.finditer(m.group('refs')):
            events.append(Event(KIND[m.group('kind').lower()], scope, r.group('n').replace('.', ''), r.group('y'),
                                r.group('a')))
    originals = [(r.group('n').replace('.', ''), r.group('y'), r.group('a')) for r in REF.finditer(orig)]
    return events, originals


def unit_key(nro: str, sec: str) -> str:
    sec = sec.strip().lower()
    return f'art-{int(nro):04d}' + (f'-{sec}' if sec else '')


def unit_label(nro: str, sec: str) -> str:
    return f'Artículo {int(nro)}' + (f' {sec.strip().upper()}' if sec.strip() else '')


def load(path: str, offline: bool = True) -> dict:
    return fetch.impo_json(fetch.impo(path), offline)


def articles(main: dict) -> tuple[list[Article], int]:
    width = wrap_width([a['textoArticulo'] for a in main['articulos']])
    out = []
    for a in main['articulos']:
        ev, orig = parse_notes(a.get('notasArticulo') or '')
        out.append(Article(unit_key(a['nroArticulo'], a['secArticulo']), unit_label(a['nroArticulo'], a['secArticulo']),
                           impo_paragraphs(a['textoArticulo'], width), ev, orig))
    return out, width


# ---------------------------------------------------------------- dates

def ddmmyyyy(s: str) -> str:
    d, m, y = s.strip().split('/')
    return f'{y}-{m}-{d}'


def plus_days(day: str, n: int) -> str:
    return (dt.date.fromisoformat(day) + dt.timedelta(days=n)).isoformat()


VIGENCIA = re.compile(r'regir[áa] a partir del? (?:d[íi]a )?(\d+)[º°]? de (\w+) de (\d{4})', re.I)
MONTHS = {'enero': 1, 'febrero': 2, 'marzo': 3, 'abril': 4, 'mayo': 5, 'junio': 6, 'julio': 7, 'agosto': 8,
          'setiembre': 9, 'septiembre': 9, 'octubre': 10, 'noviembre': 11, 'diciembre': 12}


def in_force(header: dict, vigencia_text: str | None) -> tuple[str, str]:
    """(in-force day, how it was found) for a law, from its own vigencia article or the default rule."""
    if vigencia_text:
        m = VIGENCIA.search(re.sub(r'\s+', ' ', vigencia_text))
        if m:
            return (f'{m.group(3)}-{MONTHS[m.group(2).lower()]:02d}-{int(m.group(1)):02d}',
                    f'its vigencia article: "{m.group(0)}"')
    pub = ddmmyyyy(header['fechaPublicacion'])
    return plus_days(pub, 10), f'published {pub}; Código Civil art. 1: ten days after publication'


# ---------------------------------------------------------------- items

ITEM = re.compile(r"^(?:(\d+)\s?[º°o]?|([A-ZÑa-zñ]))\)")


def scope_marker(scope: str) -> str | None:
    """'Literal Ñ)' -> 'Ñ', 'Numeral 5)' -> '5'; None for incisos and compound scopes."""
    m = re.fullmatch(r'(?:Literal|Numeral|Apartado) ([0-9]+|[A-ZÑ])[º°]?\)', scope.strip())
    return m.group(1) if m else None


def item_index(paras: list[str], marker: str) -> int | None:
    hits = [i for i, p in enumerate(paras) if (m := ITEM.match(p)) and (m.group(1) or m.group(2)) == marker]
    return hits[0] if len(hits) == 1 else None


def quoted_article(law_text: str, art: str, width: int) -> list[str] | None:
    """The new wording an amending article gives to article `art`: the quoted block that opens with
    "ARTICULO <art>." (IMPO's original of the amending law)."""
    t = law_text.replace('\r\n', '\n')
    m = re.search(r'"\s*ART[IÍ]CULO\s+' + art + r'[º°]?\.?\s*-?\s*', t)
    if not m:
        return None
    rest = t[m.end():]
    end = re.search(r'"\s*(?:\.|\n\s*\n|$)', rest)
    body = rest[:end.start()] if end else rest
    if re.match(r'Inciso', body.strip()):
        return None                 # only one inciso is quoted
    return impo_paragraphs(body, width)
