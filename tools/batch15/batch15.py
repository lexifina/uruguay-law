"""Batch 15 of Uruguayan acts: writes scripts/uruguay-law/corpus.d/99f-batch15<a,b,...>.json
(gitlaw_common/SCHEMA.md), small parts of 2 to 4 acts (PARTS).

    python -X utf8 scripts/uruguay-law/batch15/batch15.py [--dry]                 # every sub-part, in order
    python -X utf8 scripts/uruguay-law/batch15/batch15.py <letter> [slugs] [--dry]
    python -X utf8 scripts/uruguay-law/batch15/batch15.py --vigencia <slug>...
    python -X utf8 scripts/uruguay-law/batch15/batch15.py --count [slugs]

batch14 is imported (batches 2 to 14's readings, law days and article days), batch 3's readings are re-installed with
batch 4 to 15's original-text prefixes, batch 7's "Incorpórese ... los siguientes artículos" reading is put back on top,
and batch5's part writer runs with this batch's table, part file and decisions.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
UY = HERE.parent
for _d in ('batch14', 'batch13', 'batch12', 'batch11', 'batch10', 'batch9', 'batch8', 'batch7', 'batch6', 'batch5', 'batch4'):
    sys.path.insert(0, str(UY / _d))
import batch14 as b14  # noqa: E402

b13 = b14.b13
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
    # Probed and left out: Ley 17.835 (13 of 22 articles repealed), Ley 18.098 (4 articles), Leyes 18.590 and 19.075 (every article but one a bare "(*)" pointer into the CNA and the
    # Código Civil), Ley 19.120 (faltas; 12 of 25 articles bare "(*)"), Ley 17.726 (amends the old Código del
    # Proceso Penal), Leyes 16.737, 18.410 and 19.630 (one article each: a constitutional amendment approval, a school
    # name and a treaty approval).
    _law('ley-17228', 'Ley 17.228', 'Ley de Prenda sin Desplazamiento (Ley Nº 17.228)', 'leyes/17228-2000'),
    _law('ley-17684', 'Ley 17.684', 'Ley del Comisionado Parlamentario para el Sistema Carcelario (Ley Nº 17.684)',
         'leyes/17684-2003'),
    _law('ley-18125', 'Ley 18.125', 'Carta Orgánica del Banco Hipotecario del Uruguay (Ley Nº 18.125)', 'leyes/18125-2007'),
    _law('ley-18131', 'Ley 18.131', 'Ley de Creación del Fondo Nacional de Salud (Ley Nº 18.131)', 'leyes/18131-2007'),
    _law('ley-19286', 'Ley 19.286', 'Código de Ética Médica (Ley Nº 19.286)', 'leyes/19286-2014'),
    _law('ley-18426', 'Ley 18.426', 'Ley de Salud Sexual y Reproductiva (Ley Nº 18.426)', 'leyes/18426-2008'),
    _law('ley-19823', 'Ley 19.823', 'Código de Ética en la Función Pública (Ley Nº 19.823)', 'leyes/19823-2019'),
    _law('ley-17866', 'Ley 17.866', 'Ley de Creación del Ministerio de Desarrollo Social (Ley Nº 17.866)', 'leyes/17866-2005'),
    _law('ley-19869', 'Ley 19.869', 'Ley de Telemedicina (Ley Nº 19.869)', 'leyes/19869-2020'),
    _law('ley-15977', 'Ley 15.977', 'Ley de Creación del Instituto Nacional del Menor (Ley Nº 15.977)', 'leyes/15977-1988'),
    _law('ley-19530', 'Ley 19.530', 'Ley de Salas de Lactancia Materna (Ley Nº 19.530)', 'leyes/19530-2017'),
    _law('ley-18405', 'Ley 18.405', 'Ley del Servicio de Retiros y Pensiones Policiales (Ley Nº 18.405)', 'leyes/18405-2008'),
    _law('ley-18396', 'Ley 18.396', 'Ley Orgánica de la Caja de Jubilaciones y Pensiones Bancarias (Ley Nº 18.396)',
         'leyes/18396-2008'),
    _law('ley-17738', 'Ley 17.738', 'Ley Orgánica de la Caja de Jubilaciones y Pensiones de Profesionales Universitarios '
                                    '(Ley Nº 17.738)', 'leyes/17738-2004'),
])


VIGENCIA: dict[str, str] = {}
for _cfg in ACTS.values():
    _cfg['vigencia'] = {**batch3.VIGENCIA, **batch4.VIGENCIA, **b5.VIGENCIA, **VIGENCIA, **_cfg['vigencia']}


def _reinstall() -> None:
    for n, f in batch4._ORIG.items():
        setattr(ih, n, f)
    ih._batch3 = False
    added = {**batch4.ACTS, **b5.ACTS_OWN, **b6.ACTS, **b7.ACTS, **b8.ACTS, **b9.ACTS, **b10.ACTS, **b11.ACTS, **b12.ACTS, **b13.ACTS, **b14.ACTS, **ACTS}
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
    # Used only by part x (no other part has these laws).
    '18405': ('2009-01-01', 'its art. 63: "entrará en vigencia el primer día del segundo mes siguiente a su publicación '
                            'en el Diario Oficial" (published 17/11/2008)'),
    '18396': ('2009-01-01', 'its art. 95: "La presente ley entrará en vigencia el 1º de enero de 2009"'),
    # Art. 152 puts Título IV cap. I, Título VI cap. II and Títulos X and XI in force ten days after publication
    # (2004-02-06): the act is dated by its general rule, so those parts show from 2004-08-01 (never before their day).
    '17738': ('2004-08-01', 'its art. 152: "entrará en vigencia el primer día del séptimo mes siguiente al de su '
                            'promulgación por el Poder Ejecutivo" (promulgated 07/01/2004)'),
    '20208': ('2023-12-01', 'its art. 19: "entrará en vigencia el primer día del mes siguiente al de su publicación en '
                            'el Diario Oficial" (published 08/11/2023)'),
    '20410': ('2025-08-01', 'its art. 25: "entrará en vigencia el primer día del mes siguiente al de su publicación en '
                            'el Diario Oficial" (published 15/07/2025)'),
}
batch2.LAW_DAY.update(LAW_DAY)

# Small parts (coordinator, 2026-10-31): each sub-part holds 2 to 4 acts and gets its own PUBLISH as soon as it is
# verified. A sub-part's file name sorts after the ones before it; each later sub-part reads the earlier ones as
# published parts (shared law entries). `batch15.py` with no part letter regenerates every sub-part in order, each in
# its own process.
PARTS: dict[str, list[str]] = {
    'a': ['ley-17228', 'ley-17684', 'ley-18125'],
    'b': ['ley-18131', 'ley-19286', 'ley-18426'],
    'c': ['ley-19823', 'ley-17866'],
    'e': ['ley-19869', 'ley-15977', 'ley-19530'],
    'x': ['ley-18405', 'ley-18396', 'ley-17738'],
}
# Part x (letter x so it sorts after the parts published before it; give later parts letters < x) was held for the
# Ley 20.130 question until the coordinator's decision (2026-10-31): its survivor-pension repeals (20.130 art. 74) stay
# on 2023-08-01 by art. 53, its other 20.130 changes are Título XI (numeral 1). HELD parts are built only with --dry.
HELD: dict[str, list[str]] = {}
assert sorted(sum(PARTS.values(), []) + sum(HELD.values(), [])) == sorted(ACTS)


def part_file(letter: str) -> Path:
    return UY / 'corpus.d' / f'99f-batch15{letter}.json'


def use_part(letter: str) -> None:
    b5.ACTS = {s: ACTS[s] for s in {**PARTS, **HELD}[letter]}
    b5.PART = part_file(letter)
    b5.VERIFICATION = HERE / f'verification.{letter}.json'
    b5.OTHER_PARTS = BASE_OTHER_PARTS + [part_file(x) for x in PARTS if x < letter and part_file(x).exists()]


b5.ACTS = ACTS
b5.RETRIEVED = batch2.RETRIEVED = '2026-10-31'
b5.VERIFICATION = HERE / 'verification.json'
BASE_OTHER_PARTS = b14.BASE_OTHER_PARTS + [b14.part_file(x) for x in b14.PARTS]
b5.OTHER_PARTS = BASE_OTHER_PARTS
b5.DECISIONS_COMMON = [d.replace('Batch 14 acts', 'Batch 15 acts').replace('batches 2 to 13', 'batches 2 to 14')
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
    elif sys.argv[1:2] and sys.argv[1] in HELD:
        if '--dry' not in sys.argv:
            raise SystemExit(f'part {sys.argv[1]} is held: --dry only')
        use_part(sys.argv[1])
        b5.main(sys.argv[2:])
    elif sys.argv[1:2] and sys.argv[1] in PARTS:
        use_part(sys.argv[1])
        b5.main(sys.argv[2:])
    else:
        import subprocess
        for _letter in PARTS:
            r = subprocess.run([sys.executable, '-X', 'utf8', __file__, _letter, *sys.argv[1:]])
            if r.returncode:
                raise SystemExit(r.returncode)
