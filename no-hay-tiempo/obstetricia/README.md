# No hay tiempo — Obstetricia

Decks de **rescate** para la ECOE, con la misma arquitectura de los **3 pilares**
de la estación que el paquete de ginecología:

```
PREGUNTO  → tronco + llave            (Pilar 1: Interrogatorio)
EXPLORO/PIDO → herramienta + panel    (Pilar 3: Exploración + Estudios)
MANEJO    → eje + bifurcación         (Pilar 2: Manejo)
```

> En obstetricia el eje transversal que más bifurca es **la edad gestacional**
> (corte en 34 y 37 sem) y la regla **"estabilizo a la madre antes de diagnosticar"**.

## Pilar 2 — Manejo (42 cartas)

| Subdeck | Cartas | Tag |
|---|---|---|
| 1 - Ejes (madre) | 7 | `tag:eje` |
| 2 - Manejos trampa (core) | 18 | `tag:core` |
| 3 - Menos preguntados | 17 | `tag:menos_preguntado` |

## Pilar 1 — Interrogatorio: tronco + llave (42 cartas)

| Subdeck | Cartas | Tag |
|---|---|---|
| 1 - Troncos (ejes) | 7 | `tag:tronco` |
| 2 - Llaves comunes (core) | 18 | `tag:core` |
| 3 - Llaves menos preguntadas | 17 | `tag:menos_preguntado` |

## Pilar 3 — Exploración + Estudios (33 cartas)

Dos formas: **A) Discriminador** (por herramienta: USG 1T/3T, RCTG, Doppler, especuloscopia, Leopold/tacto, TA) y
**B) Panel** (por enfermedad: control prenatal, preeclampsia, HELLP, DMG, sangrado 1T, TORCH, EGB, Rh).

| Subdeck | Cartas | Tag |
|---|---|---|
| 1 - Discriminadores (herramienta) | 8 | `tag:discriminador` |
| 2 - Paneles (por enfermedad) | 8 | `tag:panel` |
| 3 - Menos preguntados | 17 | `tag:menos_preguntado` |

## Cobertura (temas pedidos)

- **Sangrado 1T:** ectópico, mola, aborto.
- **Sangrado 3T:** placenta previa, DPPNI.
- **Hipertensivos:** HTA gestacional, preeclampsia (severa), eclampsia, HELLP, sulfato de Mg.
- **Control prenatal:** DMG, EGB, Rh, IVU, TORCH, inducción, anticoncepción.
- **Vigilancia fetal:** RCIU, sufrimiento/FCF, RCTG, Doppler.
- **Parto y pretérmino:** APP, RPM, corioamnionitis, postérmino, trabajo de parto verdadero.
- **Embarazo:** suplementos, vacunas, datos de alarma.

## Importar / regenerar

`.apkg` en `output/` (jerarquía `No hay tiempo::Obstetricia::…`). Para reconstruir:

```bash
pip install genanki
python build_manejo_obst.py
python build_interrogatorio_obst.py
python build_estudios_obst.py
```

> Verifica contra la guía de tu sede los umbrales que cambian entre versiones
> (CTOG 1 paso vs 2 pasos, EGB 35-37 vs 36-37, grosor, dosis). Para ECOE van finas.
