# No hay tiempo — Ginecología

Decks de **rescate** para cuando queda poco para la ECOE, organizados por los
**3 pilares de la estación**. El mismo recorrido, una sola arquitectura:

```
PREGUNTO  → tronco + llave            (Pilar 1: Interrogatorio)
EXPLORO/PIDO → herramienta + panel    (Pilar 3: Exploración + Estudios)
MANEJO    → eje + bifurcación         (Pilar 2: Manejo)
```

> La *key* que sacas en el interrogatorio **es** la bifurcación del manejo, y el
> hallazgo de la exploración **es** lo que cierra el dx. Los tres pilares son el mismo árbol.

## Pilar 2 — Manejo (42 cartas)

| Orden | Subdeck | Cartas | Para qué |
|---|---|---|---|
| 1 | **Ejes (madre)** | 7 | El andamiaje. La *pregunta* que decide el manejo. **Estúdialo primero.** |
| 2 | **Manejos trampa (core)** | 18 | El 80% de lo puntuable. Formato hablado. |
| 3 | **Menos preguntados** | 17 | Segunda pasada si sobra tiempo. |

## Pilar 1 — Interrogatorio: tronco + llave (43 cartas)

| Orden | Subdeck | Cartas | Para qué |
|---|---|---|---|
| 1 | **Troncos (ejes)** | 8 | El guión de apertura por motivo de consulta (reutilizable en todo el grupo). |
| 2 | **Llaves comunes (core)** | 18 | La pregunta-llave que fija el dx de lo más preguntado. |
| 3 | **Llaves menos preguntadas** | 17 | Segunda pasada. |

Build: `build_interrogatorio_gine.py` · chuleta imprimible: `CHULETA_INTERROGATORIO.md`.

## Pilar 3 — Exploración + Estudios (33 cartas)

Dos **formas** de estudio, no una:
- **A) Discriminador:** una herramienta separa un grupo por un hallazgo → organizas *por herramienta* (USG-TV, bimanual, especuloscopia…).
- **B) Panel / workup:** una enfermedad pide una batería con roles (confirma / descarta imitador / repercusión) → organizas *por enfermedad* (SOP, infertilidad, climaterio…).

| Orden | Subdeck | Cartas | Para qué |
|---|---|---|---|
| 1 | **Discriminadores (herramienta)** | 8 | Front = herramienta, back = tabla hallazgo → dx. |
| 2 | **Paneles (por enfermedad)** | 8 | La batería de labs/imagen y el rol de cada uno. |
| 3 | **Menos preguntados** | 17 | AMH, HSG, BI-RADS, POP-Q, DXA, 17-OHP… |

Build: `build_estudios_gine.py`.

## Formato de cada carta de manejo (dorso, 3 bloques)

- 🟦 **Verbalizo** (al sinodal, técnico): qué indico / solicito.
- 🟩 **Consejería** (a la paciente, lenguaje llano + empatía).
- 🟧 **Cierre** (seguridad): datos de alarma + seguimiento + pareja/lactancia.

Las cartas de **eje** llevan: *regla madre · bifurcación · trampa ECOE*.

## Ruta de estudio con poco tiempo

1. Memoriza los **7 títulos de eje** (7 imágenes). Con el eje, el manejo casi se deduce.
2. Pasa el subdeck **2 (core)**: son las trampas que distinguen aprobado de excelente.
3. Solo si sobra tiempo, el subdeck **3**.

## Importar a Anki

Doble clic en cualquier `.apkg` de `output/`, o el combinado
`No_Hay_Tiempo_Gineco_TODOS.apkg` (los 3 subdecks con jerarquía
`No hay tiempo::Ginecologia::…`).

Filtrar en Anki: `tag:core` (los 18 clave), `tag:eje` (los 7), `tag:menos_preguntado` (los 17).

## Regenerar

```bash
pip install genanki
python build_no_hay_tiempo_gine.py    # reconstruye los 4 .apkg en output/
```

## Cobertura (lo que pediste)

- **ITS:** sífilis (temprana/tardía), chancroide, VPH, herpes, EIP, cervicitis.
- **Vaginitis/cervicitis:** candidiasis, vaginosis, tricomoniasis.
- **Oncológico:** NIC 1/2-3, ca cérvix invasor, tamizaje + Papanicolaou anormal, ca endometrio, ca ovario, BI-RADS.
- **Mama benigna:** fibroadenoma, quiste, mastitis, absceso, Paget, telorrea.
- **Gine general:** SOP (desea/no desea), endometriosis, adenomiosis, miomatosis, climaterio, prolapso, Bartholino, liquen escleroso, patología vulvoperineal, infertilidad.
