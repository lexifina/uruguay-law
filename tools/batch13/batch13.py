"""Batch 13 of Uruguayan acts: writes scripts/uruguay-law/corpus.d/99d-batch13.json (gitlaw_common/SCHEMA.md).

    python -X utf8 scripts/uruguay-law/batch13/batch13.py [slugs] [--dry]
    python -X utf8 scripts/uruguay-law/batch13/batch13.py --vigencia <slug>...
    python -X utf8 scripts/uruguay-law/batch13/batch13.py --count [slugs]

batch12 is imported (batches 2 to 12's readings, law days and article days), batch 3's readings are re-installed with
batch 4 to 13's original-text prefixes, batch 7's "Incorpórese ... los siguientes artículos" reading is put back on top,
and batch5's part writer runs with this batch's table, part file and decisions.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
UY = HERE.parent
for _d in ('batch12', 'batch11', 'batch10', 'batch9', 'batch8', 'batch7', 'batch6', 'batch5', 'batch4'):
    sys.path.insert(0, str(UY / _d))
import batch12 as b12  # noqa: E402

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
    # Left out: Ley 19.133 (all 33 articles "(*)") and Ley 19.484 (24 of 69 "(*)": mostly amendments of other laws).
    ('decreto-ley-15322', {'short': 'Decreto-Ley 15.322', 'title': 'Ley de Intermediación Financiera (Decreto-Ley Nº 15.322)',
                           'path': 'decretos-ley/15322-1982', 'base': '15322', 'enacted': True,
                           'original_prefix': 'decretos-leyes-originales/15322-1982', 'vigencia': {}}),
    ('decreto-ley-14219', {'short': 'Decreto-Ley 14.219', 'title': 'Ley de Arrendamientos Urbanos y Suburbanos '
                                                            '(Decreto-Ley Nº 14.219)',
                           'path': 'decretos-ley/14219-1974', 'base': '14219', 'enacted': True,
                           'original_prefix': 'decretos-leyes-originales/14219-1974', 'vigencia': {}}),
    _law('ley-19820', 'Ley 19.820', 'Ley de Fomento del Emprendedurismo (Ley Nº 19.820)', 'leyes/19820-2019'),
    _law('ley-18930', 'Ley 18.930', 'Ley sobre Información de Participaciones Patrimoniales al Portador (Ley Nº 18.930)',
         'leyes/18930-2012'),
    _law('ley-18786', 'Ley 18.786', 'Ley de Participación Público-Privada (Ley Nº 18.786)', 'leyes/18786-2011'),
    _law('ley-19253', 'Ley 19.253', 'Ley de Turismo (Ley Nº 19.253)', 'leyes/19253-2014'),
    _law('ley-19272', 'Ley 19.272', 'Ley de Descentralización y Participación Ciudadana (Ley Nº 19.272)',
         'leyes/19272-2014'),
    _law('ley-18597', 'Ley 18.597', 'Ley de Uso Eficiente de la Energía (Ley Nº 18.597)', 'leyes/18597-2009'),
])


VIGENCIA: dict[str, str] = {}
for _cfg in ACTS.values():
    _cfg['vigencia'] = {**batch3.VIGENCIA, **batch4.VIGENCIA, **b5.VIGENCIA, **VIGENCIA, **_cfg['vigencia']}


def _reinstall() -> None:
    for n, f in batch4._ORIG.items():
        setattr(ih, n, f)
    ih._batch3 = False
    added = {**batch4.ACTS, **b5.ACTS_OWN, **b6.ACTS, **b7.ACTS, **b8.ACTS, **b9.ACTS, **b10.ACTS, **b11.ACTS, **b12.ACTS, **ACTS}
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

b5.ACTS = ACTS
b5.RETRIEVED = batch2.RETRIEVED = '2026-10-31'
b5.PART = UY / 'corpus.d' / '99d-batch13.json'
b5.VERIFICATION = HERE / 'verification.json'
b5.OTHER_PARTS = b5.OTHER_PARTS + [UY / 'corpus.d' / '99c-batch12.json']
b5.DECISIONS_COMMON = [d.replace('Batch 12 acts', 'Batch 13 acts').replace('batches 2 to 11', 'batches 2 to 12')
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
    else:
        b5.main(sys.argv[1:])
