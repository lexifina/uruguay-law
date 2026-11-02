"""Recognize whole added articles whose own explicit commencement is still future."""
import datetime as dt
import re

MONTHS = {'enero': 1, 'febrero': 2, 'marzo': 3, 'abril': 4, 'mayo': 5, 'junio': 6,
          'julio': 7, 'agosto': 8, 'septiembre': 9, 'octubre': 10, 'noviembre': 11, 'diciembre': 12}
START = re.compile(r'\b(?:la presente disposici[óo]n|(?:el presente|este) art[íi]culo)\b'
                   r'[^.]{0,400}?\bentrar[áa] en (?:vigencia|vigor)\s+a partir del?\s+'
                   r'(\d+)[°º]?\s+de\s+(\w+)\s+de\s+(\d{4})', re.I)


def future_added_day(article: dict, docs_date: str) -> str | None:
    """Only whole additions, never future replacements of existing wording.

    An addition note and a single explicit date in the article are both required.
    Scoped additions, amendments and repeal notes cannot prove whole-article absence.
    """
    notes = article.get('notasArticulo') or ''
    labels = re.findall(r'<b>(?:<font[^>]*>)?([^<]+?)(?:</font>)?</b>', notes, re.I)
    labels = [re.sub(r'\s+', ' ', s).strip().rstrip(':').lower() for s in labels]
    if 'agregado/s por' not in labels:
        return None
    if any(re.search(r'redacci[óo]n|derogad|suprimid|inciso|literal|numeral', s) for s in labels):
        return None
    matches = START.findall(' '.join((article.get('textoArticulo') or '').split()))
    if len(matches) != 1:
        return None
    d, month, y = matches[0]
    if month.lower() not in MONTHS:
        return None
    day = dt.date(int(y), MONTHS[month.lower()], int(d)).isoformat()
    return day if day > docs_date else None
