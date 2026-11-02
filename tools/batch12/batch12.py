"""Batch 12 of Uruguayan acts: writes scripts/uruguay-law/corpus.d/99c-batch12.json (gitlaw_common/SCHEMA.md).

    python -X utf8 scripts/uruguay-law/batch12/batch12.py [slugs] [--dry]
    python -X utf8 scripts/uruguay-law/batch12/batch12.py --vigencia <slug>...
    python -X utf8 scripts/uruguay-law/batch12/batch12.py --count [slugs]

batch11 is imported (batches 2 to 11's readings, law days and article days), batch 3's readings are re-installed with
batch 4 to 12's original-text prefixes, batch 7's "Incorpórese ... los siguientes artículos" reading is put back on top,
and batch5's part writer runs with this batch's table, part file and decisions.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
UY = HERE.parent
for _d in ('batch11', 'batch10', 'batch9', 'batch8', 'batch7', 'batch6', 'batch5', 'batch4'):
    sys.path.insert(0, str(UY / _d))
import batch11 as b11  # noqa: E402

b10 = b11.b10
b9 = b10.b9
b8 = b9.b8
b7 = b8.b7
b6 = b7.b6
b5 = b7.b5
ih, batch2, batch3, batch4 = b5.ih, b5.batch2, b5.batch3, b5.batch4
_law = b5._law

ACTS: dict[str, dict] = dict([
    _law('ley-19043', 'Ley 19.043', 'Ley de Creación de la Universidad Tecnológica (Ley Nº 19.043)', 'leyes/19043-2012'),
    _law('ley-12549', 'Ley 12.549', 'Ley Orgánica de la Universidad de la República (Ley Nº 12.549)', 'leyes/12549-1958'),
    _law('ley-19122', 'Ley 19.122', 'Ley de Afrodescendientes: Normas para Favorecer su Participación (Ley Nº 19.122)',
         'leyes/19122-2013'),
    _law('ley-19846', 'Ley 19.846', 'Ley de Igualdad y No Discriminación entre Mujeres y Varones (Ley Nº 19.846)',
         'leyes/19846-2019'),
    _law('ley-17817', 'Ley 17.817', 'Ley de Lucha contra el Racismo, la Xenofobia y la Discriminación (Ley Nº 17.817)',
         'leyes/17817-2004'),
    _law('ley-19828', 'Ley 19.828', 'Ley de Fomento y Protección del Sistema Deportivo (Ley Nº 19.828)',
         'leyes/19828-2019'),
    _law('ley-15921', 'Ley 15.921', 'Ley de Zonas Francas (Ley Nº 15.921)', 'leyes/15921-1987'),
    _law('ley-16246', 'Ley 16.246', 'Ley de Puertos (Ley Nº 16.246)', 'leyes/16246-1992'),
    _law('ley-16466', 'Ley 16.466', 'Ley de Evaluación del Impacto Ambiental (Ley Nº 16.466)', 'leyes/16466-1994'),
    _law('ley-17849', 'Ley 17.849', 'Ley de Uso de Envases no Retornables (Ley Nº 17.849)', 'leyes/17849-2004'),
    _law('ley-19175', 'Ley 19.175', 'Ley de Pesca Responsable y Fomento de la Acuicultura (Ley Nº 19.175)',
         'leyes/19175-2013'),
    _law('ley-15939', 'Ley 15.939', 'Ley Forestal (Ley Nº 15.939)', 'leyes/15939-1987'),
    _law('ley-16858', 'Ley 16.858', 'Ley de Riego con Destino Agrario (Ley Nº 16.858)', 'leyes/16858-1997'),
    _law('ley-18161', 'Ley 18.161', 'Ley de Creación de la Administración de los Servicios de Salud del Estado '
                                    '(Ley Nº 18.161)', 'leyes/18161-2007'),
])


VIGENCIA: dict[str, str] = {}
for _cfg in ACTS.values():
    _cfg['vigencia'] = {**batch3.VIGENCIA, **batch4.VIGENCIA, **b5.VIGENCIA, **VIGENCIA, **_cfg['vigencia']}


def _reinstall() -> None:
    for n, f in batch4._ORIG.items():
        setattr(ih, n, f)
    ih._batch3 = False
    added = {**batch4.ACTS, **b5.ACTS_OWN, **b6.ACTS, **b7.ACTS, **b8.ACTS, **b9.ACTS, **b10.ACTS, **b11.ACTS, **ACTS}
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


LAW_DAY: dict[str, tuple[str, str]] = {
    '16320': ('1993-01-01', 'its art. 2: "La presente ley regirá a partir del 1° de enero de 1993, excepto en aquellas '
                            'disposiciones en que, en forma expresa, se establezca otra fecha de vigencia"'),
    '19566': ('2018-03-08', 'its art. 31: "La presente ley entrará en vigencia a los noventa días de su promulgación" '
                            '(promulgated 08/12/2017)'),
    '16002': ('1989-01-01', 'its art. 1: "La presente ley regirá a partir del 1º de enero de 1989, excepto en aquellas '
                            'disposiciones en que, en forma expresa, se establezca otra fecha de vigencia"'),
}
batch2.LAW_DAY.update(LAW_DAY)

b5.ACTS = ACTS
b5.RETRIEVED = batch2.RETRIEVED = '2026-10-31'
b5.PART = UY / 'corpus.d' / '99c-batch12.json'
b5.VERIFICATION = HERE / 'verification.json'
b5.OTHER_PARTS = b5.OTHER_PARTS + [UY / 'corpus.d' / '99b-batch11.json']
b5.DECISIONS_COMMON = [d.replace('Batch 11 acts', 'Batch 12 acts').replace('batches 2 to 10', 'batches 2 to 11')
                       for d in b5.DECISIONS_COMMON]
ACT_DECISIONS: dict[str, list[str]] = {
    'ley-15939': [
        "Ley 15.939, arts. 39 and 50: Ley 16.002 arts. 90 and 91 say their wording applies from Ley 15.939's own entry "
        "into force (1988); the history shows it from the day it entered the law, Ley 16.002's general day (1 January "
        "1989, its art. 1), and does not backdate it.",
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
