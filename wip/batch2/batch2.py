"""Batch 2 of the Uruguayan codes: writes scripts/uruguay-law/corpus.d/50-batch2.json (gitlaw_common/SCHEMA.md).

    python -X utf8 scripts/uruguay-law/batch2/batch2.py

Reads only the shared .cache (fetched by batch2/fetch2.py). Each code is rebuilt by the main agent's
impo_history.build_act (imported, not copied) from IMPO's consolidated text and IMPO's per-article notes, with each
in-force day taken from the amending law's own vigencia article. This module adds only:

  * two readings of IMPO's notes that impo_history does not know (NOTE_KINDS, scope words such as "Ordinal"),
  * a post-pass over the rebuilt versions: an article IMPO says was repealed and later given new wording is absent in
    between, and the anachronism rule (BRIEF.md, 2026-10-28) is applied to every unit,
  * the verification that today's text equals IMPO's consolidated text, unit for unit.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
UY = HERE.parent
sys.path.insert(0, str(UY))
import fetch  # noqa: E402
import impo_history as ih  # noqa: E402

# ---------------------------------------------------------------- readings of IMPO's notes

# Kinds of note impo_history does not parse; added to its tables so that the laws they name enter the history.
NOTE_KINDS = {'derogado anteriormente por': 'repealed-earlier', 'derogado/s anteriormente por': 'repealed-earlier',
              'redacción derogada por': 'wording-repealed'}


def _install_note_readings() -> None:
    if getattr(ih, '_batch2', False):
        return
    ih._batch2 = True
    ih.KIND.update(NOTE_KINDS)
    kinds = sorted(ih.KIND, key=len, reverse=True)
    ih.NOTE = re.compile('(?P<kind>' + '|'.join(re.escape(k) for k in kinds) + r'):\s*'
                         r'(?P<refs>(?:,?\s*(?:y\s+)?Ley Nº [\d.]+ de \d\d/\d\d/\d{4}\s+artículos?\s+[\d\s,y]+)+)',
                         re.I)
    orig_note_text = ih.note_text

    def note_text(html: str) -> str:
        # The CGP and the CPP number their paragraphs "ordinales" (547.1, 547.2); IMPO's notes scope changes to
        # them ("Ordinal 1º) inciso 2º) agregado/s por"). impo_history knows only Inciso/Literal/Numeral/Apartado
        # scopes and would read an unknown scope as the whole article, so "Ordinal" is read as an Apartado scope
        # that names no single item (no item marker is derived from it).
        return re.sub(r'\b[Oo]rdinal(es)?\b', lambda m: 'Apartado ordinal' + (m.group(1) or ''), orig_note_text(html))

    ih.note_text = note_text


_install_note_readings()

# ---------------------------------------------------------------- the acts

# slug -> IMPO path, the code's own law, vigencia articles of amending laws read by hand (law -> article), whether the
# base law enacted the text, and the code's own in-force day (IMPO path of the article that gives it, day, the words
# that must be in that article).
ACTS: dict[str, dict] = {
    'codigo-general-proceso': {
        'short': 'CGP', 'title': 'Código General del Proceso (Ley Nº 15.982)',
        'path': 'codigo-general-proceso/15982-1988', 'base': '15982', 'enacted': True,
        'vigencia': {},
        'base_in_force': ('codigo-general-proceso/15982-1988/547', '1989-11-20', 'el 20 de noviembre de 1989'),
    },
    'codigo-comercio': {
        'short': 'Código de Comercio', 'title': 'Código de Comercio',
        'path': 'codigo-comercio/817-1865', 'base': '817', 'enacted': False,
        'vigencia': {},
        'base_in_force': None,
    },
    'codigo-proceso-penal': {
        'short': 'CPP', 'title': 'Código del Proceso Penal (Ley Nº 19.293)',
        'path': 'codigo-proceso-penal-2017/19293-2014', 'base': '19293', 'enacted': True,
        'vigencia': {},
        'base_in_force': None,
    },
}

PART = UY / 'corpus.d' / '50-batch2.json'
VERIFICATION = HERE / 'verification.json'
RETRIEVED = '2026-10-28'
PLACEHOLDER = '[La fuente no da el texto vigente en esta fecha.]'
WORDING_NOW = ('wording', 'added')        # IMPO notes whose words are in today's text


def base_in_force(cfg: dict, main: dict) -> tuple[str, str] | None:
    """The code's own in-force day, from the article that gives it (asserted to contain the words in ACTS)."""
    if not cfg.get('base_in_force'):
        return None
    vpath, day, words = cfg['base_in_force']
    nro = vpath.rsplit('/', 1)[1]
    if vpath.startswith(cfg['path'] + '/'):
        art = next(a for a in main['articulos'] if a['nroArticulo'] == nro and not a['secArticulo'].strip())
    else:
        art = ih.load(vpath)
    text = ' '.join(art['textoArticulo'].split())
    assert words in text, (vpath, text)
    return day, f'{vpath}: "{text}"'


# ---------------------------------------------------------------- per-unit timelines

def timelines(act: dict) -> tuple[dict[str, list], dict[str, str]]:
    """key -> [(day, unit or None, credits)] at every change, from versions that all carry full `units`."""
    tl: dict[str, list] = {}
    prev: dict = {}
    for v in act['versions']:
        units = v['units']
        for k in sorted(set(units) | set(prev)):
            if units.get(k) != prev.get(k) or k not in tl:
                tl.setdefault(k, []).append([v['from'], units.get(k), list(v['credits'].get(k, []))])
        prev = units
    labels = {k: next(u['label'] for _, u, _ in c if u) for k, c in tl.items() if any(u for _, u, _ in c)}
    return tl, labels


def versions_from(tl: dict[str, list], template: list[dict]) -> list[dict]:
    days = sorted({d for c in tl.values() for d, _, _ in c})
    src, sha = template[0]['source_url'], template[0]['sha256']
    notes = {v['from']: v.get('note') for v in template}
    out, prev = [], {}
    for day in days:
        units, credits = {}, {}
        for k, chain in tl.items():
            cur = [c for c in chain if c[0] <= day]
            if not cur:
                continue
            d, u, ls = cur[-1]
            if u is not None:
                units[k] = u
            if d == day and ls and units.get(k) != prev.get(k):
                credits[k] = list(ls)
        out.append({'from': day, 'source_url': src, 'sha256': sha, 'units': dict(sorted(units.items())),
                    'credits': dict(sorted(credits.items())), 'note': notes.get(day)})
        prev = units
    out[0]['note'] = template[0].get('note')
    out[-1]['note'] = template[-1].get('note') if len(out) > 1 else out[-1]['note']
    return out


def unit(label: str, paras: list[str]) -> dict:
    return {'label': label, 'kind': 'art', 'text': ih.render(label, paras)}


def post_pass(act: dict, main: dict, base: str, ver: dict) -> dict:
    """Repealed-then-revived articles, and the anachronism rule. Returns what it changed, for decisions."""
    arts, _ = ih.articles(main)
    day_of = {label: d['day'] for label, d in ver['in_force'].items()}     # keyed by law label
    base_day = ver['base_in_force']['day']
    tl, labels = timelines(act)
    done = {'absent_between': [], 'placeholder': [], 'absent_before': []}

    def day(law: str) -> str | None:
        return day_of.get(ih.law_label(law))

    for a in arts:
        chain = tl.get(a.key)
        if chain is None:
            continue
        evs = [e for e in a.events if e.law != base and e.kind != 'vigencia' and day(e.law) and day(e.law) > base_day]
        # 1. "Derogado anteriormente por" a law R, and the article given new wording later: absent from R's day
        #    until the next law after R changes it.
        for e in evs:
            if e.kind != 'repealed-earlier' or e.scope:
                continue
            r, rk = day(e.law), ih.law_key(e.law)
            later = [c for c in chain if c[0] > r]
            if not later or later[0][1] is None:
                continue
            for c in later:
                if rk in c[2]:
                    c[2].remove(rk)
            chain[:] = [c for c in chain if c[0] < r] + [[r, None, [rk]]] + later
            done['absent_between'].append(f'{a.label}: absent from {r} ({ih.law_label(e.law)}, "derogado '
                                          f'anteriormente") until {later[0][0]}')
        # 2. The anachronism rule: today's wording must not appear before the last law that IMPO says gave it.
        now = [e for e in evs if e.kind in WORDING_NOW]
        if not now or not a.current:
            continue
        last = max(now, key=lambda e: day(e.law))
        d_last = day(last.law)
        today = unit(a.label, a.current)
        early = [c for c in chain if c[0] < d_last and c[1] == today]
        if not early:
            continue
        inserted = (last.kind == 'added' and not last.scope)
        first_early = early[0][0]
        # the change on first_early keeps its credit (that law did change the article; its words are unknown);
        # today's wording arrives on d_last, credited to every law after first_early up to d_last
        lks: list[str] = []
        for c in chain:
            if first_early < c[0] <= d_last:
                lks += [l for l in c[2] if l not in lks]
        for l in sorted({e.law for e in evs if first_early < day(e.law) <= d_last}, key=lambda l: (day(l), int(l))):
            if ih.law_key(l) not in lks:
                lks.append(ih.law_key(l))
        keep = [c for c in chain if c[0] < first_early]
        filler = None if inserted else unit(a.label, [PLACEHOLDER])
        mid = [[first_early, filler, list(early[0][2]) if keep else []]]
        rest = [c for c in chain if c[0] > d_last]
        chain[:] = keep + mid + [[d_last, today, lks or [ih.law_key(last.law)]]] + rest
        done['absent_before' if inserted else 'placeholder'].append(
            f'{a.label}: today\'s wording held back until {d_last} ({ih.law_label(last.law)})')
    act['versions'] = versions_from(tl, act['versions'])
    return done
