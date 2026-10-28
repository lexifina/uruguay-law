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
