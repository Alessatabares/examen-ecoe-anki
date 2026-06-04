# No hay tiempo — Cirugía

Decks de **rescate** para la ECOE, misma arquitectura de los **3 pilares** que gine/obstetricia:

```
PREGUNTO  → tronco + llave            (Pilar 1: Interrogatorio)
EXPLORO/PIDO → herramienta + panel    (Pilar 3: Exploración + Estudios)
MANEJO    → eje + bifurcación         (Pilar 2: Manejo)
```

> En cirugía los dos ejes que más bifurcan: **ABCDE (primero lo que mata)** y
> **estable vs inestable → TAC vs quirófano**. Y el reloj: **tiempo = tejido**.

## Pilar 2 — Manejo (42)

| Subdeck | Cartas | Tag |
|---|---|---|
| 1 - Ejes / patrones madre | 7 | `tag:eje` |
| 2 - Manejos comunes (core) | 18 | `tag:core` |
| 3 - Menos comunes | 17 | `tag:menos_comun` |

## Pilar 1 — Interrogatorio: tronco + llave (42)

| Subdeck | Cartas | Tag |
|---|---|---|
| 1 - Troncos (ejes) | 7 | `tag:tronco` |
| 2 - Llaves comunes (core) | 18 | `tag:core` |
| 3 - Llaves menos comunes | 17 | `tag:menos_comun` |

## Pilar 3 — Exploración + Estudios (33)

**A) Discriminador** (por herramienta: eFAST, Rx tórax/abdomen, TAC, signos, lactato, SNG/tacto, Doppler) y
**B) Panel** (por entidad: trauma, pancreatitis, biliar, sepsis, transfusión masiva, abdomen agudo, vascular, obstrucción).

| Subdeck | Cartas | Tag |
|---|---|---|
| 1 - Discriminadores (herramienta) | 8 | `tag:discriminador` |
| 2 - Paneles (por entidad) | 8 | `tag:panel` |
| 3 - Signos y scores | 17 | `tag:signo_score` |

## Cobertura (temas pedidos)

- **Trauma:** penetrante (estable/inestable), cerrado, lesión esplénica (Kehr), neumotórax a tensión, taponamiento, hemotórax masivo, tórax inestable, fractura pélvica.
- **Hemorragia:** ectópico roto, HDA úlcera, HDA várices, HDB, AAA roto, Cullen/Grey-Turner, choque hipovolémico, reanimación.
- **Abdomen agudo:** apendicitis, perforación, colecistitis, colangitis, pancreatitis, diverticulitis, vólvulo, isquemia mesentérica.
- **Obstrucción:** SOI alta/baja, hernia, íleo, asa cerrada.
- **Infección:** peritonitis, absceso, fascitis necrotizante, gangrena, sepsis.
- **Especiales:** síndrome compartimental, disección aórtica, torsión testicular, torsión ovárica.

## Regenerar

```bash
pip install genanki
python build_manejo_cir.py
python build_interrogatorio_cir.py
python build_estudios_cir.py
```

> Nota: «SA» de tu lista lo interpreté como **síndrome compartimental agudo** (de extremidad).
> Si te referías a otra cosa (síndrome aórtico/compartimental abdominal), avísame y lo ajusto.
> Verifica dosis/umbrales sede-dependientes (sitio de descompresión de neumotórax, metas de TA, etc.).
