# No hay tiempo — Ginecología

Decks de **rescate** para cuando queda poco para la ECOE. No estudies 25 manejos
sueltos: estudia primero los **ejes de decisión** (el árbol) y cuelga de ahí los
manejos, ya **verbalizados** como se hablan en la estación.

> La *key* que sacas en el interrogatorio dirigido **es** la bifurcación del manejo.
> Interrogatorio y tratamiento son el mismo árbol.

## Los 3 subdecks (42 cartas)

| Orden | Subdeck | Cartas | Para qué |
|---|---|---|---|
| 1 | **Ejes (madre)** | 7 | El andamiaje. La *pregunta* que decide el manejo. **Estúdialo primero.** |
| 2 | **Manejos trampa (core)** | 18 | El 80% de lo puntuable. Formato hablado. |
| 3 | **Menos preguntados** | 17 | Segunda pasada si sobra tiempo. |

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
