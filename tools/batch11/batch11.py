"""Batch 11 of Uruguayan acts: writes scripts/uruguay-law/corpus.d/99b-batch11.json (gitlaw_common/SCHEMA.md).

    python -X utf8 scripts/uruguay-law/batch11/batch11.py [slugs] [--dry]
    python -X utf8 scripts/uruguay-law/batch11/batch11.py --vigencia <slug>...
    python -X utf8 scripts/uruguay-law/batch11/batch11.py --count [slugs]

batch10 is imported (batches 2 to 10's readings, law days and article days), batch 3's readings are re-installed with
batch 4 to 11's original-text prefixes, batch 7's "Incorpórese ... los siguientes artículos" reading is put back on top,
and batch5's part writer runs with this batch's table, part file and decisions.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
UY = HERE.parent
for _d in ('batch10', 'batch9', 'batch8', 'batch7', 'batch6', 'batch5', 'batch4'):
    sys.path.insert(0, str(UY / _d))
import batch10 as b10  # noqa: E402

b9 = b10.b9
b8 = b9.b8
b7 = b8.b7
b6 = b7.b6
b5 = b7.b5
ih, batch2, batch3, batch4 = b5.ih, b5.batch2, b5.batch3, b5.batch4
_law = b5._law

ACTS: dict[str, dict] = dict([
    # Left out: Ley 18.214 (3 articles, an amending law, 2 of them "(*)"), Decreto-Ley 14.219 (IMPO has no such path),
    # Ley 16.696 (its TEXTO ORIGINAL links point at chapter anchors, e.g. leyes-originales/16696-1995#CAPITULOVI).
    ('codigo-aeronautico', {'short': 'Código Aeronáutico', 'title': 'Código Aeronáutico (Decreto-Ley Nº 14.305)',
                            'path': 'codigo-aeronautico/14305-1974', 'base': '14305', 'enacted': True,
                            'original_prefix': 'decretos-leyes-originales/14305-1974', 'vigencia': {}}),
    ('codigo-aguas', {'short': 'Código de Aguas', 'title': 'Código de Aguas (Decreto-Ley Nº 14.859)',
                      'path': 'codigo-aguas/14859-1978', 'base': '14859', 'enacted': True,
                      'original_prefix': 'textos-originales-decreto-ley/14859-1978', 'vigencia': {}}),
    _law('ley-19920', 'Ley 19.920', 'Ley General de Derecho Internacional Privado (Ley Nº 19.920)', 'leyes/19920-2020'),
    _law('ley-7812', 'Ley 7.812', 'Ley de Elecciones (Ley Nº 7.812)', 'leyes/7812-1925'),
    _law('ley-18485', 'Ley 18.485', 'Ley de Partidos Políticos (Ley Nº 18.485)', 'leyes/18485-2009'),
    _law('ley-15848', 'Ley 15.848', 'Ley de Caducidad de la Pretensión Punitiva del Estado (Ley Nº 15.848)',
         'leyes/15848-1986'),
    _law('ley-18831', 'Ley 18.831', 'Ley de Restablecimiento de la Pretensión Punitiva del Estado (Ley Nº 18.831)',
         'leyes/18831-2011'),
    _law('ley-16099', 'Ley 16.099', 'Ley de Prensa (Ley Nº 16.099)', 'leyes/16099-1989'),
    _law('ley-18232', 'Ley 18.232', 'Ley de Radiodifusión Comunitaria (Ley Nº 18.232)', 'leyes/18232-2007'),
])


VIGENCIA: dict[str, str] = {}
for _cfg in ACTS.values():
    _cfg['vigencia'] = {**batch3.VIGENCIA, **batch4.VIGENCIA, **b5.VIGENCIA, **VIGENCIA, **_cfg['vigencia']}


def _reinstall() -> None:
    for n, f in batch4._ORIG.items():
        setattr(ih, n, f)
    ih._batch3 = False
    added = {**batch4.ACTS, **b5.ACTS_OWN, **b6.ACTS, **b7.ACTS, **b8.ACTS, **b9.ACTS, **b10.ACTS, **ACTS}
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

# One more reading, in this process only: numbered items written "6º La construcción ..." (an ordinal with no closing
# parenthesis, as in the Código de Aguas) are items too, so a numeral a later law added ("Numeral 6º) agregado/s por")
# is removed from the earlier text as impo_history removes "6º)" items. Used only when the usual reading finds none.
ORDINAL_ITEM = re.compile(r'^(\d+)[º°]\s')
_item_index = ih.item_index


def item_index(paras: list[str], marker: str) -> int | None:
    i = _item_index(paras, marker)
    if i is not None:
        return i
    hits = [k for k, p in enumerate(paras) if (m := ORDINAL_ITEM.match(p)) and m.group(1) == marker]
    return hits[0] if len(hits) == 1 else None


ih.item_index = item_index

LAW_DAY: dict[str, tuple[str, str]] = {}
batch2.LAW_DAY.update(LAW_DAY)

b5.ACTS = ACTS
b5.RETRIEVED = batch2.RETRIEVED = '2026-10-31'
b5.PART = UY / 'corpus.d' / '99b-batch11.json'
b5.VERIFICATION = HERE / 'verification.json'
b5.OTHER_PARTS = b5.OTHER_PARTS + [UY / 'corpus.d' / '99-batch10.json']
b5.DECISIONS_COMMON = [d.replace('Batch 10 acts', 'Batch 11 acts').replace('batches 2 to 9', 'batches 2 to 10')
                       for d in b5.DECISIONS_COMMON]
ACT_DECISIONS: dict[str, list[str]] = {
    'codigo-aguas': [
        "Código de Aguas: IMPO serves original texts only for the articles it links as TEXTO ORIGINAL; for the fixed "
        "sample of unamended articles it serves none, so those articles read as IMPO's consolidated text from the "
        "first version without that cross-check. Art. 152: numeral 6º (written \"6º La construcción ...\", with no "
        "parenthesis) is absent before Ley 17.296, which added it.",
    ],
    'ley-7812': [
        "Ley 7.812, art. 49: IMPO's consolidated text lacks the words \"listas de candidatos que hubiesen sido\" that "
        "its original text has, and IMPO's notes name no law that removed them; the article reads as IMPO gives it "
        "today from the first version, so this one change is not dated or credited.",
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
