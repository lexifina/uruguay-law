"""Batch 10 of Uruguayan acts: writes scripts/uruguay-law/corpus.d/99-batch10.json (gitlaw_common/SCHEMA.md).

    python -X utf8 scripts/uruguay-law/batch10/batch10.py [slugs] [--dry]
    python -X utf8 scripts/uruguay-law/batch10/batch10.py --vigencia <slug>...
    python -X utf8 scripts/uruguay-law/batch10/batch10.py --count [slugs]

batch9 is imported (batches 2 to 9's readings, law days and article days), batch 3's readings are re-installed with
batch 4 to 10's original-text prefixes, batch 7's "Incorpórese ... los siguientes artículos" reading is put back on top,
and batch5's part writer runs with this batch's table, part file and decisions.
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
UY = HERE.parent
for _d in ('batch9', 'batch8', 'batch7', 'batch6', 'batch5', 'batch4'):
    sys.path.insert(0, str(UY / _d))
import batch9 as b9  # noqa: E402

b8 = b9.b8
b7 = b8.b7
b6 = b7.b6
b5 = b7.b5
ih, batch2, batch3, batch4 = b5.ih, b5.batch2, b5.batch3, b5.batch4
_law = b5._law

ACTS: dict[str, dict] = dict([
    # Left out: Ley 5.350 (IMPO gives all 7 articles as "(*)"), Ley 18.395 (8 of 17 "(*)": an amending law) and Ley
    # 13.728 (65 of 217 "(*)").
    _law('ley-18091', 'Ley 18.091', 'Ley de Prescripción de Acciones y Créditos Laborales (Ley Nº 18.091)',
         'leyes/18091-2007'),
    _law('ley-18251', 'Ley 18.251', 'Ley de Tercerizaciones Laborales (Ley Nº 18.251)', 'leyes/18251-2008'),
    _law('ley-12590', 'Ley 12.590', 'Ley de Licencia Anual (Ley Nº 12.590)', 'leyes/12590-1958'),
    _law('ley-15996', 'Ley 15.996', 'Ley de Horas Extras (Ley Nº 15.996)', 'leyes/15996-1988'),
    _law('ley-18572', 'Ley 18.572', 'Ley de Abreviación de los Juicios Laborales (Ley Nº 18.572)', 'leyes/18572-2009'),
    _law('ley-19690', 'Ley 19.690', 'Ley del Fondo de Garantía de Créditos Laborales (Ley Nº 19.690)',
         'leyes/19690-2018'),
    _law('ley-18227', 'Ley 18.227', 'Ley de Asignaciones Familiares (Ley Nº 18.227)', 'leyes/18227-2007'),
    _law('ley-19313', 'Ley 19.313', 'Ley de Trabajo Nocturno (Ley Nº 19.313)', 'leyes/19313-2015'),
    _law('ley-17215', 'Ley 17.215', 'Ley de Trabajadoras en Estado de Gravidez o en Período de Lactancia '
                                    '(Ley Nº 17.215)', 'leyes/17215-1999'),
    _law('ley-16774', 'Ley 16.774', 'Ley de Fondos de Inversión (Ley Nº 16.774)', 'leyes/16774-1996'),
    _law('ley-17613', 'Ley 17.613', 'Ley de Bancos (Ley Nº 17.613)', 'leyes/17613-2002'),
    # Ley 16.696 (Carta Orgánica del BCU) left out for now: one TEXTO ORIGINAL link points at a chapter anchor of the
    # whole law (leyes-originales/16696-1995#CAPITULOVI), which IMPO serves no article JSON for.
])

# IMPO keeps Ley 12.590's original texts under a suffixed path (its own TEXTO ORIGINAL links say so).
ACTS['ley-12590']['original_prefix'] = 'leyes-originales/12590-1958_A'

VIGENCIA: dict[str, str] = {}
for _cfg in ACTS.values():
    _cfg['vigencia'] = {**batch3.VIGENCIA, **batch4.VIGENCIA, **b5.VIGENCIA, **VIGENCIA, **_cfg['vigencia']}


def _reinstall() -> None:
    for n, f in batch4._ORIG.items():
        setattr(ih, n, f)
    ih._batch3 = False
    added = {**batch4.ACTS, **b5.ACTS_OWN, **b6.ACTS, **b7.ACTS, **b8.ACTS, **b9.ACTS, **ACTS}
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
b5.PART = UY / 'corpus.d' / '99-batch10.json'
b5.VERIFICATION = HERE / 'verification.json'
b5.OTHER_PARTS = b5.OTHER_PARTS + [UY / 'corpus.d' / '98-batch9.json']
b5.DECISIONS_COMMON = [d.replace('Batch 9 acts', 'Batch 10 acts').replace('batches 2 to 8', 'batches 2 to 9')
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
