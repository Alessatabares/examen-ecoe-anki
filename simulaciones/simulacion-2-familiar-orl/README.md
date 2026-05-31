# Simulación 2 — Medicina Familiar / ORL y cuello

Deck de Anki **`Simulaciones::Familiar ORL - Repaso 2`**. Repaso de la simulación de medicina
familiar (sección otorrinolaringología y patología tiroidea), en formato ECOE.

## Estructura (33 tarjetas) — versión condensada

11 entidades × 3 tarjetas:

| # | Tarjeta | Para qué |
|---|---------|----------|
| 1 | Abordaje | interrogatorio (qué pregunto y **qué orienta**) + exploración (**cómo y qué verbalizar**: otoscopia, rinoscopia, orofaringe, palpación de cuello/tiroides) |
| 2 | Manejo | dx + tratamiento (dosis) por gravedad + **cuándo referir** + frase ECOE |
| 3 | Caso escalonado | una viñeta **leve → moderado → difícil** con la conducta de cada nivel (el difícil = bandera roja → referencia) |

Entidades: **Sinusitis · Coinfección (sinusitis+otitis+neumonía) · Otitis media aguda ·
Otitis media serosa · Perforación timpánica · Otitis externa · Faringitis estreptocócica ·
Rinitis alérgica · Rinitis irritativa · Bocio · Nódulo tiroideo**.

Los casos difíciles meten las banderas rojas de la simulación: celulitis orbitaria, mastoiditis,
otitis externa maligna (diabético/inmunosuprimido), absceso periamigdalino, compresión traqueal,
nódulo con datos de alarma → BAAF.

## Importar a Anki

**Opción A — archivo listo (`.tsv`):** Anki → *Archivo → Importar* → `simulacion-2-familiar-orl.tsv`.
Separador: **Tabulador**. Campos: `Front`, `Back`, `Tags`. Marca **«Permitir HTML en los campos»**.

**Opción B — generar el `.apkg`** (con el venv aislado del repo):

```bash
../../.venv/bin/python build_deck.py
```

Luego doble clic en `simulacion-2-familiar-orl.apkg`.

## Frases ECOE de cierre (incluidas en las tarjetas de Manejo)

- **Sinusitis:** «Sinusitis bacteriana; inicio amoxicilina/clavulanato y medidas de soporte.»
- **Otitis media:** «Otitis media aguda; indico amoxicilina y analgesia.»
- **Otitis externa:** «Otitis externa; manejo con gotas óticas y mantener oído seco.»
- **Faringitis:** «Faringitis estreptocócica; amoxicilina 10 días para prevenir complicaciones.»
- **Rinitis:** «Rinitis alérgica; antihistamínico, corticoide nasal y control ambiental.»
- **Bocio:** «Solicito perfil tiroideo y ultrasonido para definir etiología.»
- **Nódulo tiroideo:** «Nódulo tiroideo; solicito TSH y ultrasonido, valorando BAAF si hay datos de alarma.»

---
Generado con Claude Code. Editar tarjetas en `build_deck.py` y reconstruir.
