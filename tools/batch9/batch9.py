"""Batch 9 of Uruguayan acts: writes scripts/uruguay-law/corpus.d/98-batch9.json (gitlaw_common/SCHEMA.md).

    python -X utf8 scripts/uruguay-law/batch9/batch9.py [slugs] [--dry]
    python -X utf8 scripts/uruguay-law/batch9/batch9.py --vigencia <slug>...
    python -X utf8 scripts/uruguay-law/batch9/batch9.py --count [slugs]

batch8 is imported (batches 2 to 8's readings, law days and article days), batch 3's readings are re-installed with
batch 4 to 9's original-text prefixes, batch 7's "Incorpórese ... los siguientes artículos" reading is put back on top,
and batch5's part writer runs with this batch's table, part file and decisions.
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
UY = HERE.parent
for _d in ('batch8', 'batch7', 'batch6', 'batch5', 'batch4'):
    sys.path.insert(0, str(UY / _d))
import batch8 as b8  # noqa: E402

b7 = b8.b7
b6 = b7.b6
b5 = b7.b5
ih, batch2, batch3, batch4 = b5.ih, b5.batch2, b5.batch3, b5.batch4
_law = b5._law

# Left out, as IMPO gives (nearly) every article as a bare "(*)" pointer with no text in force: Leyes 18.567
# (28 of 28), 19.973 (46 of 53), 18.620 (7 of 7) and 19.196 (2 of 3).
ACTS: dict[str, dict] = dict([
    _law('ley-16713', 'Ley 16.713', 'Ley de Seguridad Social (Ley Nº 16.713)', 'leyes/16713-1995'),
    _law('ley-18446', 'Ley 18.446', 'Ley de la Institución Nacional de Derechos Humanos y Defensoría del Pueblo '
                                    '(Ley Nº 18.446)', 'leyes/18446-2008'),
    _law('ley-18795', 'Ley 18.795', 'Ley de Acceso a la Vivienda de Interés Social (Ley Nº 18.795)', 'leyes/18795-2011'),
    _law('ley-17957', 'Ley 17.957', 'Ley del Registro Nacional de Deudores Alimentarios (Ley Nº 17.957)',
         'leyes/17957-2006'),
    _law('ley-18076', 'Ley 18.076', 'Ley sobre el Derecho al Refugio y a los Refugiados (Ley Nº 18.076)',
         'leyes/18076-2006'),
    _law('ley-19167', 'Ley 19.167', 'Ley de Técnicas de Reproducción Humana Asistida (Ley Nº 19.167)',
         'leyes/19167-2013'),
    _law('ley-18473', 'Ley 18.473', 'Ley de Voluntad Anticipada (Ley Nº 18.473)', 'leyes/18473-2009'),
    _law('ley-16832', 'Ley 16.832', 'Ley de Actualización del Sistema Eléctrico Nacional (Ley Nº 16.832)',
         'leyes/16832-1997'),
    _law('ley-9515', 'Ley 9.515', 'Ley Orgánica Municipal (Ley Nº 9.515)', 'leyes/9515-1935'),
    _law('ley-17163', 'Ley 17.163', 'Ley de Fundaciones (Ley Nº 17.163)', 'leyes/17163-1999'),
    _law('ley-18256', 'Ley 18.256', 'Ley de Control del Tabaquismo (Ley Nº 18.256)', 'leyes/18256-2008'),
])

VIGENCIA: dict[str, str] = {}
for _cfg in ACTS.values():
    _cfg['vigencia'] = {**batch3.VIGENCIA, **batch4.VIGENCIA, **b5.VIGENCIA, **VIGENCIA, **_cfg['vigencia']}


def _reinstall() -> None:
    for n, f in batch4._ORIG.items():
        setattr(ih, n, f)
    ih._batch3 = False
    added = {**batch4.ACTS, **b5.ACTS_OWN, **b6.ACTS, **b7.ACTS, **b8.ACTS, **ACTS}
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

# Amending laws whose general day an IMPO "Ver vigencia" pointer to one of their articles hid (read by hand from the
# law's own text, cached), and Ley 18.246's deferred social-security articles.
LAW_DAY: dict[str, tuple[str, str]] = {
    '16736': ('1996-01-01', 'its art. 2: "regirá a partir del 1º de enero de 1996" (as batch 3 dates it)'),
    '17556': ('2003-01-01', 'its art. 2: "La presente ley regirá a partir del 1º de enero de 2003, excepto en aquellas '
                            'disposiciones en que, en forma expresa, se establezca otra fecha de vigencia"'),
    '19723': ('2019-12-21', 'its art. 3: "Las modificaciones establecidas en la presente ley entrarán en vigencia '
                            'transcurridos doce meses desde su promulgación" (promulgated 21/12/2018)'),
}
batch2.LAW_DAY.update(LAW_DAY)
b6.ARTICLE_DAY.update({
    ('18246', str(n)): ('2009-01-20', f'Ley Nº 18.246 art. 19: "Cumplido un año a partir de la entrada en vigencia de '
                                      f'esta ley, quedarán extendidos ... a que refieren los artículos 14 a 18 de esta '
                                      f'ley" (the law in force 20 January 2008; art. {n})')
    for n in range(14, 19)
})

b5.ACTS = ACTS
b5.RETRIEVED = batch2.RETRIEVED = '2026-10-31'
b5.PART = UY / 'corpus.d' / '98-batch9.json'
b5.VERIFICATION = HERE / 'verification.json'
b5.OTHER_PARTS = b5.OTHER_PARTS + [UY / 'corpus.d' / '97-batch8.json']
b5.DECISIONS_COMMON = [d.replace('Batch 8 acts', 'Batch 9 acts').replace('batches 2 to 7', 'batches 2 to 8')
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
