"""Batch 14 of Uruguayan acts: writes scripts/uruguay-law/corpus.d/99e-batch14<a,b,...>.json
(gitlaw_common/SCHEMA.md), small parts of 2 to 4 acts (PARTS).

    python -X utf8 scripts/uruguay-law/batch14/batch14.py [--dry]                 # every sub-part, in order
    python -X utf8 scripts/uruguay-law/batch14/batch14.py <letter> [slugs] [--dry]
    python -X utf8 scripts/uruguay-law/batch14/batch14.py --vigencia <slug>...
    python -X utf8 scripts/uruguay-law/batch14/batch14.py --count [slugs]

batch13 is imported (batches 2 to 13's readings, law days and article days), batch 3's readings are re-installed with
batch 4 to 14's original-text prefixes, batch 7's "Incorpórese ... los siguientes artículos" reading is put back on top,
and batch5's part writer runs with this batch's table, part file and decisions.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
UY = HERE.parent
for _d in ('batch13', 'batch12', 'batch11', 'batch10', 'batch9', 'batch8', 'batch7', 'batch6', 'batch5', 'batch4'):
    sys.path.insert(0, str(UY / _d))
import batch13 as b13  # noqa: E402

b12 = b13.b12
b11 = b12.b11
b10 = b11.b10
b9 = b10.b9
b8 = b9.b8
b7 = b8.b7
b6 = b7.b6
b5 = b7.b5
ih, batch2, batch3, batch4 = b5.ih, b5.batch2, b5.batch3, b5.batch4
_law = b5._law

ACTS: dict[str, dict] = dict([
    # Left out: Decreto-Ley 15.524 (TCA: every article a bare "(*)"), Ley 19.588 (all "(*)", amends Ley 13.728) and
    # Decreto-Ley 14.294 (estupefacientes; fetched): arts. 81-83 carry "Redacción derogada por" (wording added in 2001,
    # repealed in 2004) and art. 67 "Reincorporado por", note kinds impo_history does not read, so today's text did
    # not equal IMPO's.
    ('decreto-ley-14701', {'short': 'Decreto-Ley 14.701', 'title': 'Ley de Títulos Valores (Decreto-Ley Nº 14.701)',
                           'path': 'decretos-ley/14701-1977', 'base': '14701', 'enacted': True,
                           'original_prefix': 'decretos-leyes-originales/14701-1977', 'vigencia': {}}),
    _law('ley-19678', 'Ley 19.678', 'Ley del Mercado de Seguros (Ley Nº 19.678)', 'leyes/19678-2018'),
    _law('ley-10751', 'Ley 10.751', 'Ley de Propiedad Horizontal (Ley Nº 10.751)', 'leyes/10751-1946'),
    _law('ley-10449', 'Ley 10.449', 'Ley de Consejos de Salarios (Ley Nº 10.449)', 'leyes/10449-1943'),
    _law('ley-18840', 'Ley 18.840', 'Ley de Conexión a las Redes Públicas de Saneamiento (Ley Nº 18.840)',
         'leyes/18840-2011'),
    _law('ley-18244', 'Ley 18.244', 'Ley de Deudores Alimentarios Morosos (Ley Nº 18.244)', 'leyes/18244-2007'),
    _law('ley-16021', 'Ley 16.021', 'Ley de Nacionalidad y Ciudadanía (Ley Nº 16.021)', 'leyes/16021-1989'),
    _law('ley-19140', 'Ley 19.140', 'Ley de Alimentación Saludable en los Centros de Enseñanza (Ley Nº 19.140)',
         'leyes/19140-2013'),
    _law('ley-19978', 'Ley 19.978', 'Ley de Teletrabajo (Ley Nº 19.978)', 'leyes/19978-2021'),
])


VIGENCIA: dict[str, str] = {}
for _cfg in ACTS.values():
    _cfg['vigencia'] = {**batch3.VIGENCIA, **batch4.VIGENCIA, **b5.VIGENCIA, **VIGENCIA, **_cfg['vigencia']}


def _reinstall() -> None:
    for n, f in batch4._ORIG.items():
        setattr(ih, n, f)
    ih._batch3 = False
    added = {**batch4.ACTS, **b5.ACTS_OWN, **b6.ACTS, **b7.ACTS, **b8.ACTS, **b9.ACTS, **b10.ACTS, **b11.ACTS, **b12.ACTS, **b13.ACTS, **ACTS}
    for slug in added:
        assert slug not in batch3.ACTS, slug
    batch3.ACTS.update(added)
    try:
        batch3._install()
    finally:
        for slug in added:
            del batch3.ACTS[slug]
    b7._articles = ih.articles          # batch 7's reading wraps the freshly installed one
    ih.articles = b7.articles


_reinstall()


LAW_DAY: dict[str, tuple[str, str]] = {}
batch2.LAW_DAY.update(LAW_DAY)

# Small parts (coordinator, 2026-10-31): each sub-part holds 2 to 4 acts and gets its own PUBLISH as soon as it is
# verified. A sub-part's file name sorts after the ones before it; each later sub-part reads the earlier ones as
# published parts (shared law entries). `batch14.py` with no part letter regenerates every sub-part in order, each in
# its own process.
PARTS: dict[str, list[str]] = {
    'a': ['decreto-ley-14701', 'ley-19678', 'ley-10751'],
    'b': ['ley-10449', 'ley-18840', 'ley-18244'],
    'c': ['ley-16021', 'ley-19140', 'ley-19978'],
}
assert sorted(sum(PARTS.values(), [])) == sorted(ACTS)


def part_file(letter: str) -> Path:
    return UY / 'corpus.d' / f'99e-batch14{letter}.json'


def use_part(letter: str) -> None:
    b5.ACTS = {s: ACTS[s] for s in PARTS[letter]}
    b5.PART = part_file(letter)
    b5.VERIFICATION = HERE / f'verification.{letter}.json'
    b5.OTHER_PARTS = BASE_OTHER_PARTS + [part_file(x) for x in PARTS if x < letter and part_file(x).exists()]


b5.ACTS = ACTS
b5.RETRIEVED = batch2.RETRIEVED = '2026-10-31'
b5.VERIFICATION = HERE / 'verification.json'
BASE_OTHER_PARTS = b5.OTHER_PARTS + [UY / 'corpus.d' / '99d-batch13.json']
b5.OTHER_PARTS = BASE_OTHER_PARTS
b5.DECISIONS_COMMON = [d.replace('Batch 13 acts', 'Batch 14 acts').replace('batches 2 to 12', 'batches 2 to 13')
                       for d in b5.DECISIONS_COMMON]
ACT_DECISIONS: dict[str, list[str]] = {}
b5.ACT_DECISIONS = ACT_DECISIONS

if __name__ == '__main__':
    if sys.argv[1:2] == ['--vigencia']:
        batch2.ACTS.update(ACTS)
        for s in sys.argv[2:]:
            batch2.vigencia_report(s)
    elif sys.argv[1:2] == ['--count']:
        b5.count(sys.argv[2:])
    elif sys.argv[1:2] and sys.argv[1] in PARTS:
        use_part(sys.argv[1])
        b5.main(sys.argv[2:])
    else:
        import subprocess
        for _letter in PARTS:
            r = subprocess.run([sys.executable, '-X', 'utf8', __file__, _letter, *sys.argv[1:]])
            if r.returncode:
                raise SystemExit(r.returncode)
