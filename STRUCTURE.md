# Estructura / Structure

| Carpeta | Contenido |
| --- | --- |
| `constitucion/` | La Constitución de la República (1967, con las reformas de 1989, 1994, 1996 y 2004); `art-067.md` es el art. 67 |
| `codigos/<codigo>/` | Los códigos (`codigos/codigo-civil/art-1700.md` es el art. 1700 del Código Civil) |
| `leyes/<año>/<número>-<objeto>/` | Una ley, por año de promulgación y número, p. ej. `leyes/2008/18331-proteccion-de-datos-personales/` |
| `decretos-ley/<año>/<número>-<objeto>/` | Los decretos-ley de 1973-1985, igual |
| `decretos/<año>/<número>-<objeto>/` | Decretos del Poder Ejecutivo (número/año), igual |

Cada carpeta tiene un archivo por artículo (`art-001.md`, `art-003-bis.md`), `vistos.md` con los vistos y
considerandos de un decreto, y un `README.md` con el nombre, las fechas, la estructura (secciones y capítulos) y la
lista de disposiciones. Las notas de IMPO de cada artículo (redacción dada por, agregado por, derogado por ...)
van debajo de su texto. Ninguna carpeta tiene más de 1.000 entradas. `data/paths.json` relaciona el id de cada norma
(`ley-18331`) con su carpeta.

## Fechas

Cada versión es un commit, fechado a las 12:00 (America/Montevideo) del día en que entró en vigencia, que repite el
trailer `In-force:`; `In-force-basis:` dice de dónde sale ese día:

- `clausula-de-vigencia`: la cláusula de vigencia de la propia norma (un día, o su publicación);
- `codigo-civil-art-1`: sin cláusula, diez días después de su publicación en el Diario Oficial (Código Civil, art.
  1); también cuando la cláusula nombra un día anterior a la publicación (ninguna versión se fecha antes de que su
  ley se publicara);
- `vigencia-de-articulos`: algunos artículos tienen un día de vigencia propio, posterior; la versión se fecha cuando
  todos sus artículos están vigentes;
- `ultima-modificacion`: el texto actualizado de IMPO (sin las versiones anteriores), fechado cuando entró en
  vigencia la última ley que, según las notas de IMPO, lo modificó.

Antes de 1970 (git no guarda fechas anteriores) los commits se fechan el 1 de enero de 1970, con el día real en el
asunto y en `In-force:`. Una norma cuya vigencia queda librada a otro acto, o con un día todavía futuro, queda fuera.
Ninguna fecha de este repositorio es el día en que descargamos algo.
