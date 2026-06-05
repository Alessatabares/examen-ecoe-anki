# No hay tiempo — Medicina Familiar

Decks de **rescate** para la ECOE, misma arquitectura de los **3 pilares** que gine/obstetricia/cirugía/medicina interna:

```
PREGUNTO  → tronco + llave            (Pilar 1: Interrogatorio)
EXPLORO/PIDO → herramienta + panel    (Pilar 3: Exploración + Estudios)
MANEJO    → eje + bifurcación         (Pilar 2: Manejo)
```

> En medicina familiar los ejes que más bifurcan: **descartar lo urgente antes de tratar como banal**,
> **¿ambulatorio vs referir/urgencias?**, **antibiótico solo cuando cambia el desenlace**, y
> **prevención en cada consulta** (tamizaje + vacunas + consejo).

## Pilar 2 — Manejo (69)

| Subdeck | Cartas | Tag |
|---|---|---|
| 1 - Ejes / patrones madre | 8 | `tag:eje` |
| 2 - Manejos comunes (core) | 24 | `tag:core` |
| 3 - Menos comunes | 37 | `tag:menos_comun` |

## Pilar 1 — Interrogatorio: tronco + llave (47)

| Subdeck | Cartas | Tag |
|---|---|---|
| 1 - Troncos (ejes) | 8 | `tag:tronco` |
| 2 - Llaves comunes (core) | 19 | `tag:core` |
| 3 - Llaves menos comunes | 20 | `tag:menos_comun` |

## Pilar 3 — Exploración + Estudios (34)

**A) Discriminador** (por herramienta: otoscopia, espirometría, ECG, tira de orina, glucemia/HbA1c, perfil tiroideo, índices de anemia, exploración del vértigo) y
**B) Panel** (por entidad: crónico DM/HTA, ITU, dolor torácico, respiratorio, anemia, próstata/LUTS, preventivo, cefalea).

| Subdeck | Cartas | Tag |
|---|---|---|
| 1 - Discriminadores (herramienta) | 8 | `tag:discriminador` |
| 2 - Paneles (por entidad) | 8 | `tag:panel` |
| 3 - Signos y scores | 18 | `tag:signo_score` |

## Chuletas (una página para recitar)

- [Interrogatorio](CHULETA_INTERROGATORIO.md) — 8 troncos + llaves core/menos
- [Estudios / exploración](CHULETA_ESTUDIOS.md) — discriminadores + paneles + scores
- [Manejo](CHULETA_MANEJO.md) — 8 ejes + core + menos

## Cobertura (temas pedidos)

- **Respiratorio:** neumonía, bronquitis, asma, EPOC, IVAS, influenza, derrame pleural, neumotórax.
- **ORL:** sinusitis, otitis media, otitis externa, faringitis, laringitis, rinitis, nódulo tiroideo.
- **Cardiovascular:** SCA, pericarditis, ICC, estenosis aórtica, TVP, síncope, dolor torácico.
- **Abdominal:** apendicitis, colecistitis, gastroenteritis, pancreatitis, diverticulitis, obstrucción.
- **Neuro:** EVC, migraña, cefalea tensional, cefalea red flag, vértigo (VPPB/central).
- **Musculoesquelético:** lumbalgia, cauda equina, ciática, cervicalgia.
- **Genitourinario:** cistitis, pielonefritis, cólico renal, ITU en embarazo, HPB, CA próstata.
- **Crónico/endocrino:** DM2, HTA, dislipidemia, hipo/hipertiroidismo, Cushing, pie diabético, anemia.
- **Urgencias:** sepsis, emergencia hipertensiva, CAD, hipoglucemia, tormenta tiroidea, crisis adrenal.
- **Preventivo:** vacunas, tabaquismo, VIH, tamizaje.

## Regenerar

```bash
pip install genanki   # o usar la .venv del repo
python build_manejo_mf.py
python build_interrogatorio_mf.py
python build_estudios_mf.py
```

> Verifica dosis, esquemas antibióticos y calendarios de vacunas/tamizaje **sede-dependientes**
> (GPC/CENETEC locales, USPSTF) y la versión vigente de cada guía antes del examen.
