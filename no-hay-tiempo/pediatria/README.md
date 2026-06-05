# No hay tiempo — Pediatría

Decks de **rescate** para la ECOE, misma arquitectura de los **3 pilares** que el resto de `no-hay-tiempo/`:

```
PREGUNTO  → tronco + llave            (Pilar 1: Interrogatorio)
EXPLORO/PIDO → herramienta + panel    (Pilar 3: Exploración + Estudios)
MANEJO    → eje + bifurcación         (Pilar 2: Manejo)
```

> Para estudiar **a fondo y por capas** existe el deck `pediatria/` (4 capas: Flujo macro · Componentes · Ejes · Manejo/DDx).
> Este es el de **rescate <3 días**. Los ejes madre de pediatría: **TEP** (¿se ve mal?),
> **fiebre por edad**, **todo por peso/kg**, **estridor = vía aérea alta**, **taquicardia antes que hipotensión**,
> y **el niño sano** (vacunas, desarrollo, maltrato).

## Pilar 2 — Manejo (47)

| Subdeck | Cartas | Tag |
|---|---|---|
| 1 - Ejes / patrones madre | 8 | `tag:eje` |
| 2 - Manejos comunes (core) | 18 | `tag:core` |
| 3 - Menos comunes | 21 | `tag:menos_comun` |

## Pilar 1 — Interrogatorio: tronco + llave (40)

| Subdeck | Cartas | Tag |
|---|---|---|
| 1 - Troncos (ejes) | 8 | `tag:tronco` |
| 2 - Llaves comunes (core) | 16 | `tag:core` |
| 3 - Llaves menos comunes | 16 | `tag:menos_comun` |

## Pilar 3 — Exploración + Estudios (34)

**A) Discriminador** (por herramienta: TEP, exantemas, estridor, lactante febril, deshidratación, bilirrubina, LCR, taquipnea) y
**B) Panel** (por entidad: fiebre sin foco, sepsis neonatal, ITU, Kawasaki, convulsión febril, respiratorio, maltrato, RN sano/tamizajes).

| Subdeck | Cartas | Tag |
|---|---|---|
| 1 - Discriminadores (herramienta) | 8 | `tag:discriminador` |
| 2 - Paneles (por entidad) | 8 | `tag:panel` |
| 3 - Signos y scores | 18 | `tag:signo_score` |

## Chuletas (una página para recitar)

- [Interrogatorio](CHULETA_INTERROGATORIO.md) — 8 troncos + llaves core/menos
- [Estudios / exploración](CHULETA_ESTUDIOS.md) — discriminadores + paneles + scores
- [Manejo](CHULETA_MANEJO.md) — 8 ejes + core + menos

## Cobertura (temas pedidos + añadidos indispensables)

- **Neonatología:** reanimación neonatal, ictericia/hiperbilirrubinemia, sepsis neonatal, meningitis neonatal, TORCH, conjuntivitis neonatal, VIH perinatal.
- **Infeccioso/fiebre:** fiebre sin foco <3 meses, ITU, meningitis, sepsis.
- **Respiratorio:** bronquiolitis (VRS), neumonía, crup, epiglotitis (Hib), tos ferina, asma.
- **ORL:** otitis media, faringoamigdalitis estreptocócica (McIsaac).
- **Digestivo/GU:** GEA y deshidratación (planes A/B/C), parasitosis.
- **Exantemas:** sarampión, rubéola, varicela, exantema súbito (roséola), eritema infeccioso, escarlatina, mano-pie-boca; impétigo/piel.
- **Sistémico/cardio:** Kawasaki, (soplo/cardiopatía → enlace Ruidos Cardíacos).
- **Neuro:** convulsión febril.
- **Reanimación:** PALS (paro pediátrico).
- **Preventivo:** desarrollo, crecimiento, vacunas, displasia de cadera, anemia ferropénica del lactante.
- **Añadidos indispensables:** **TEP** (eje madre), **maltrato infantil**, **atragantamiento/cuerpo extraño**.
- **Enlaces:** abdomen quirúrgico pediátrico (invaginación, estenosis pilórica) → deck de Cirugía; shock → Patrones Madre; soplos → Ruidos Cardíacos.

## Regenerar

```bash
pip install genanki   # o usar la .venv del repo
python build_manejo_ped.py
python build_interrogatorio_ped.py
python build_estudios_ped.py
```

> Audiencia **pediátrica** (separada del adulto). Verifica dosis por kg, esquemas
> antibióticos, umbrales de bilirrubina y calendarios de vacunación **sede-dependientes**
> (AAP/GPC/CENETEC, PALS, GINA) y la versión vigente de cada guía antes del examen.
