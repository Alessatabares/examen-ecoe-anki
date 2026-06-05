# No hay tiempo — Medicina Interna

Decks de **rescate** para la ECOE, misma arquitectura de los **3 pilares** que gine/obstetricia/cirugia:

```
PREGUNTO  → tronco + llave            (Pilar 1: Interrogatorio)
EXPLORO/PIDO → herramienta + panel    (Pilar 3: Exploración + Estudios)
MANEJO    → eje + bifurcación         (Pilar 2: Manejo)
```

> En medicina interna los ejes que más bifurcan: **ABC + glucosa + ECG primero**,
> **¿qué descompensó al crónico hoy?**, y en las crisis metabólicas/endocrinas
> **líquidos + corregir el déficit + tratar el gatillo**.

## Pilar 2 — Manejo (50)

| Subdeck | Cartas | Tag |
|---|---|---|
| 1 - Ejes / patrones madre | 8 | `tag:eje` |
| 2 - Manejos comunes (core) | 18 | `tag:core` |
| 3 - Menos comunes | 24 | `tag:menos_comun` |

## Pilar 1 — Interrogatorio: tronco + llave (45)

| Subdeck | Cartas | Tag |
|---|---|---|
| 1 - Troncos (ejes) | 7 | `tag:tronco` |
| 2 - Llaves comunes (core) | 18 | `tag:core` |
| 3 - Llaves menos comunes | 20 | `tag:menos_comun` |

## Pilar 3 — Exploración + Estudios (34)

**A) Discriminador** (por herramienta: ECG, troponina, BNP, dímero D, gasometría, EGO, índices urinarios, índices de anemia) y
**B) Panel** (por entidad: SCA, IC, CAD/EHH, AKI, hiponatremia, crónico complejo/riesgo CV, cirrosis, patrón de transaminasas).

| Subdeck | Cartas | Tag |
|---|---|---|
| 1 - Discriminadores (herramienta) | 8 | `tag:discriminador` |
| 2 - Paneles (por entidad) | 8 | `tag:panel` |
| 3 - Signos y scores | 18 | `tag:signo_score` |

## Cobertura (temas pedidos)

- **Crónico complejo / metabólico:** riesgo CV global, síndrome metabólico, prediabetes, diabetes, HTA, patrón de transaminasas, enfoque de anemia.
- **Cardio:** IC FEr/FEp, IAMCEST, IAMSEST, FA, crisis hipertensiva, estenosis aórtica, insuficiencia mitral, pericarditis.
- **Endocrino:** CAD, EHH, tormenta tiroidea, coma mixedematoso, crisis suprarrenal, trastornos del K (hiper/hipo), Graves/hipertiroidismo.
- **Renal:** AKI prerrenal, NTA, postrenal, síndromes glomerulares (nefrótico/nefrítico), trastornos hidroelectrolíticos.
- **Hepático:** cirrosis descompensada, encefalopatía, hepatitis alcohólica, MASLD/MASH.
- **Hemato:** anemia ferropénica, de enfermedad crónica, macrocítica (B12/folato).
- **Reumato:** gota, AR, LES, PMR.
- **Pulmonar:** EPOC, asma, TEP, NAC.
- **Infecto:** endocarditis, pielonefritis / ITU complicada, sepsis.
- **Especiales:** hiponatremia.

## Regenerar

```bash
pip install genanki   # o usar la .venv del repo
python build_manejo_mi.py
python build_interrogatorio_mi.py
python build_estudios_mi.py
```

> Verifica dosis, metas y umbrales **sede-dependientes** (metas de TA, esquemas
> antibióticos locales, dosis de insulina) y la versión vigente de cada guía
> (ESC, ADA, KDIGO, GOLD, GINA, AHA/ACC, EASL) antes del examen.
