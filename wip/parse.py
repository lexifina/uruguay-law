"""Turns the cache of scripts/uruguay-law/fetch.py into scripts/uruguay-law/corpus.json (gitlaw_common/SCHEMA.md).

    python -X utf8 scripts/uruguay-law/parse.py

Reads only .cache/ (no network). Deterministic: the same cache gives the same bytes.
"""
from __future__ import annotations

import hashlib
import html
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import fetch  # noqa: E402

RETRIEVED = '2026-10-28'
IMPO = fetch.IMPO

# ---------------------------------------------------------------- text helpers


def norm(s: str) -> str:
    """One typesetting for both publishers (IMPO and Parlamento)."""
    s = html.unescape(s)
    s = s.replace(' ', ' ').replace('\t', ' ')
    s = re.sub('[“”„«»]', '"', s)
    s = re.sub('[‘’´`]', "'", s)
    s = re.sub('[–—]', '-', s)
    s = s.replace('°', 'º').replace('ª', 'ª')
    s = re.sub(r'\bN\.\s?o\b\.?', 'Nº', s)
    s = re.sub(r'(\d)\.o\b', r'\1º', s)
    s = re.sub(r'\s*\(\*\)\s*$', '', s)      # IMPO's "amended" marker
    s = re.sub(r' {2,}', ' ', s)
    s = re.sub(r'\s+([,.;:])', r'\1', s)
    return s.strip()


def key_of(text: str) -> str:
    """Comparison key: the words alone, so typesetting differences do not count as changes."""
    t = text.lower()
    t = re.sub(r'^# [^\n]*\n', '', t)
    t = t.replace('º', '')
    return re.sub(r'[^0-9a-záéíóúüñ]+', '', t)


MARK = re.compile(r"^\s*(?:\d+[º]?|[A-Za-z]|[A-Z]'{1,2}|[IVXLC]+)\)\s")


def impo_paragraphs(raw: str) -> list[str]:
    """IMPO hard-wraps at ~72 columns. Rebuild paragraphs from indentation and item markers."""
    paras: list[str] = []
    cur: list[str] = []
    cont = 0

    def flush():
        if cur:
            paras.append(' '.join(x.strip() for x in cur))
            cur.clear()

    for line in raw.replace('\r\n', '\n').replace('\r', '\n').split('\n'):
        line = line.replace(' ', ' ').replace('\t', '    ').rstrip()
        if not line.strip():
            flush()
            continue
        ind = len(line) - len(line.lstrip(' '))
        m = MARK.match(line.replace('º', 'º'))
        if m:
            flush()
            cur.append(line)
            cont = len(m.group(0)) if m.group(0).endswith(' ') else ind
            # content column: after the marker and its spaces
            rest = line[len(m.group(0)):]
            cont = len(m.group(0)) + (len(rest) - len(rest.lstrip(' ')))
            continue
        if not cur:
            cur.append(line)
            cont = 0
            continue
        if abs(ind - cont) <= 1 or (cont == 0 and ind == 0):
            cur.append(line)
        else:
            flush()
            cur.append(line)
            cont = 0
    flush()
    return [p for p in (norm(x) for x in paras) if p]


def strip_tags(s: str) -> str:
    return re.sub(r'<[^>]+>', '', s)


def cell_paragraphs(cell: str) -> list[str]:
    parts = re.split(r'(?:<br\s*/?>\s*){2,}', cell, flags=re.I)
    return [p for p in (norm(strip_tags(re.sub(r'<br\s*/?>', ' ', x, flags=re.I))) for x in parts) if p]


# ---------------------------------------------------------------- the Constitution

def letter_key(letter: str) -> str:
    base = letter[0].lower()
    primes = letter.count("'")
    return f'disp-trans-{base}' + ('', '-prima', '-segunda')[primes]


def letter_label(letter: str) -> str:
    return f'Disposición transitoria y especial {letter})'


def parlamento_constitution(raw: bytes) -> dict[str, list[str]]:
    """Units (key -> paragraphs) of a Parlamento HTML text of the Constitution."""
    h = raw.decode('utf-8')
    h = h[h.index('<!--ARTICULADO'):]
    end = h.find('<!--webbot bot="Include" U-Include="pieley')
    h = h[:end] if end > 0 else h
    units: dict[str, list[str]] = {}
    cur: list[str] | None = None
    in_trans = False
    for m in re.finditer(r'<table\b.*?</table>|<h4\b[^>]*>.*?</h4>|<p\b[^>]*>.*?</p>', h, re.S | re.I):
        block = m.group(0)
        if block[:3].lower() == '<h4':
            if 'DISPOSICIONES TRANSITORIAS' in strip_tags(block).upper():
                in_trans = True
            continue
        if block[:6].lower() == '<table':
            for row in re.findall(r'<tr\b[^>]*>(.*?)</tr>', block, re.S | re.I):
                cells = re.findall(r'<td\b[^>]*>(.*?)</td>', row, re.S | re.I)
                if not cells:
                    continue
                lead = norm(strip_tags(cells[0]))
                body: list[str] = []
                for c in cells[1:]:
                    body += cell_paragraphs(c)
                if in_trans and re.fullmatch(r"[A-Z]'{0,2}\)", lead):
                    cur = units.setdefault(letter_key(lead[:-1]), [])
                    lead_txt = lead
                    if body:
                        body[0] = f'{lead_txt} {body[0]}'
                    else:
                        body = [lead_txt]
                    cur += body
                    continue
                if cur is None:
                    continue
                if lead and body:
                    body[0] = f'{lead} {body[0]}'
                elif lead:
                    body = [lead]
                cur += body
            continue
        art = re.search(r'<a name="art(\d+)">', block)
        if art:
            in_trans = False
            cur = units.setdefault(f'art-{int(art.group(1)):03d}', [])
            text = re.sub(r'^.*?</u>\s*\.?-?\s*', '', block, count=1, flags=re.S)
            cur += cell_paragraphs(text)
            continue
        if cur is not None:
            cur += cell_paragraphs(block)
    # The transitional heading row "W)" etc. may carry an anchor; letters were read from the first cell.
    return units


def impo_constitution(main: dict, trans: dict) -> dict[str, list[str]]:
    units: dict[str, list[str]] = {}
    for a in main['articulos']:
        n = int(a['nroArticulo'])
        key = f'art-{n:03d}' + (f'-{a["secArticulo"].strip().lower()}' if a['secArticulo'].strip() else '')
        units[key] = impo_paragraphs(a['textoArticulo'])
    tx = trans['articulos'][0]['textoArticulo']
    paras = impo_paragraphs(tx)
    cur = None
    for p in paras:
        m = re.match(r"([A-Z])('{0,2}|\"|´{1,2})\)\s", p)
        if m:
            letter = m.group(1) + ("''" if m.group(2) in ('"', "''") else m.group(2).replace('´', "'"))
            cur = units.setdefault(letter_key(letter), [])
            p = f'{letter}) ' + p[m.end():]
        if cur is not None:
            cur.append(p)
    return units


def render(key: str, paras: list[str]) -> str:
    return f'# {label_of(key)}\n' + ''.join(p + '\n' for p in paras)


def label_of(key: str) -> str:
    if key.startswith('art-'):
        rest = key[4:]
        n, _, sec = rest.partition('-')
        return f'Artículo {int(n)}' + (f' {sec.upper()}' if sec else '')
    if key.startswith('disp-trans-'):
        rest = key[len('disp-trans-'):]
        letter = rest[0].upper() + {'': '', '-prima': "'", '-segunda': "''"}[rest[1:]]
        return letter_label(letter)
    return key


def unit_kind(key: str) -> str:
    return 'transitional' if key.startswith('disp-trans-') else 'art'


def sha(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def main() -> None:
    c_url, t_url = fetch.ACTS['constitucion'][:2]
    impo_main = fetch.fetch(c_url, True)
    impo_trans = fetch.fetch(t_url, True)
    current = impo_constitution(json.loads(impo_main.decode('latin-1')), json.loads(impo_trans.decode('latin-1')))
    p67 = parlamento_constitution(fetch.fetch(fetch.CONST_PARLAMENTO['1967'], True))
    p97 = parlamento_constitution(fetch.fetch(fetch.CONST_PARLAMENTO['1997'], True))
    if '--diff' in sys.argv:
        for name, a, b in (('1967->1997', p67, p97), ('1997->IMPO', p97, current)):
            print('==', name)
            for k in sorted(set(a) | set(b)):
                ka, kb = key_of('\n'.join(a.get(k, []))), key_of('\n'.join(b.get(k, [])))
                if ka != kb:
                    print(' ', k, 'added' if k not in a else 'removed' if k not in b else 'changed')
                elif len(a[k]) != len(b[k]):
                    print(' ', k, f'same words, paragraphs {len(a[k])} vs {len(b[k])}')
        return


if __name__ == '__main__':
    main()


def _debug_word_diff(a: str, b: str) -> list[str]:
    import difflib
    wa, wb = a.split(), b.split()
    out = []
    for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, wa, wb, autojunk=False).get_opcodes():
        if op != 'equal':
            out.append(f'{op}: {" ".join(wa[i1:i2])!r} -> {" ".join(wb[j1:j2])!r}')
    return out
