"""Batch 8 of Uruguayan acts: writes scripts/uruguay-law/corpus.d/97-batch8.json (gitlaw_common/SCHEMA.md).

    python -X utf8 scripts/uruguay-law/batch8/batch8.py [slugs] [--dry]
    python -X utf8 scripts/uruguay-law/batch8/batch8.py --vigencia <slug>...
    python -X utf8 scripts/uruguay-law/batch8/batch8.py --count [slugs]

batch7 is imported (batches 2 to 7's readings, law days and article days), batch 3's readings are re-installed with
batch 4 to 8's original-text prefixes, batch 7's "Incorpórese ... los siguientes artículos" reading is put back on top,
and batch5's part writer runs with this batch's table, part file and decisions.
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
UY = HERE.parent
for _d in ('batch7', 'batch6', 'batch5', 'batch4'):
    sys.path.insert(0, str(UY / _d))
import batch7 as b7  # noqa: E402

b6 = b7.b6
b5 = b7.b5
ih, batch2, batch3, batch4 = b5.ih, b5.batch2, b5.batch3, b5.batch4
_law = b5._law

ACTS: dict[str, dict] = dict([
    # Left out: Ley 18.083 (38 of its 113 articles are "(*)" pointers to the laws they amended, like the LUC) and
    # Ley 17.838 (every article is a bare "(*)": IMPO gives no text in force to check against).
    _law('ley-18508', 'Ley 18.508', 'Ley de Negociación Colectiva en el Marco de las Relaciones Laborales en el Sector '
                                    'Público (Ley Nº 18.508)', 'leyes/18508-2009'),
    _law('ley-18596', 'Ley 18.596', 'Ley de Reparación a las Víctimas de la Actuación Ilegítima del Estado '
                                    '(Ley Nº 18.596)', 'leyes/18596-2009'),
    _law('ley-18026', 'Ley 18.026', 'Ley de Cooperación con la Corte Penal Internacional (Ley Nº 18.026)',
         'leyes/18026-2006'),
    _law('ley-19643', 'Ley 19.643', 'Ley de Prevención y Combate de la Trata de Personas (Ley Nº 19.643)',
         'leyes/19643-2018'),
    _law('ley-17815', 'Ley 17.815', 'Ley de Violencia Sexual contra Niños, Adolescentes o Incapaces (Ley Nº 17.815)',
         'leyes/17815-2004'),
    _law('ley-18407', 'Ley 18.407', 'Ley General de Cooperativas (Ley Nº 18.407)', 'leyes/18407-2008'),
    _law('ley-19353', 'Ley 19.353', 'Ley del Sistema Nacional Integrado de Cuidados (Ley Nº 19.353)', 'leyes/19353-2015'),
    _law('ley-18471', 'Ley 18.471', 'Ley de Protección, Bienestar y Tenencia de Animales (Ley Nº 18.471)',
         'leyes/18471-2009'),
    _law('ley-16906', 'Ley 16.906', 'Ley de Promoción y Protección de Inversiones (Ley Nº 16.906)', 'leyes/16906-1998'),
    _law('ley-19529', 'Ley 19.529', 'Ley de Salud Mental (Ley Nº 19.529)', 'leyes/19529-2017'),
    _law('ley-18412', 'Ley 18.412', 'Ley del Seguro Obligatorio de Automotores (Ley Nº 18.412)', 'leyes/18412-2008'),
    _law('ley-18191', 'Ley 18.191', 'Ley de Tránsito y Seguridad Vial (Ley Nº 18.191)', 'leyes/18191-2007'),
    _law('ley-19691', 'Ley 19.691', 'Ley de Promoción del Trabajo para Personas con Discapacidad (Ley Nº 19.691)',
         'leyes/19691-2018'),
])

VIGENCIA: dict[str, str] = {}
for _cfg in ACTS.values():
    _cfg['vigencia'] = {**batch3.VIGENCIA, **batch4.VIGENCIA, **b5.VIGENCIA, **VIGENCIA, **_cfg['vigencia']}


def _reinstall() -> None:
    for n, f in batch4._ORIG.items():
        setattr(ih, n, f)
    ih._batch3 = False
    added = {**batch4.ACTS, **b5.ACTS_OWN, **b6.ACTS, **b7.ACTS, **ACTS}
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
b5.PART = UY / 'corpus.d' / '97-batch8.json'
b5.VERIFICATION = HERE / 'verification.json'
b5.OTHER_PARTS = b5.OTHER_PARTS + [UY / 'corpus.d' / '95-batch7.json']
b5.DECISIONS_COMMON = [d.replace('Batch 7 acts', 'Batch 8 acts').replace('batches 2 to 6', 'batches 2 to 7')
                       for d in b5.DECISIONS_COMMON]
ACT_DECISIONS: dict[str, list[str]] = {
    'ley-18407': [
        "Ley 18.407, art. 205 literal G) of numeral 9): Ley 19.164 art. 3 declares that the exemption it worded "
        "applies from Ley 18.407's own entry into force (2008); the history shows the words from the day they "
        "entered the law, ten days after Ley 19.164's publication (6 December 2013), and does not backdate them.",
    ],
}
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
