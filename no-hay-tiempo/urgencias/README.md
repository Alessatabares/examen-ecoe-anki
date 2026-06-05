# No hay tiempo — Urgencias

Decks de **rescate** para la ECOE, misma arquitectura de los **3 pilares** que el resto de `no-hay-tiempo/`:

```
PREGUNTO  → tronco + llave            (Pilar 1: Interrogatorio)
EXPLORO/PIDO → herramienta + panel    (Pilar 3: Exploración + Estudios)
MANEJO    → eje + bifurcación         (Pilar 2: Manejo)
```

> Ejes madre de urgencias: **ABCDE** (primero lo que mata), **estable vs inestable** (resucitar en paralelo),
> **alteración del alerta → glucemia + cóctel + reversibles**, **dolor torácico/disnea: las que matan**,
> **clasificar el choque**, **toxicología: tratar al paciente, no al tóxico**, **sepsis 1 h**, y **tiempo es órgano**.

## Pilar 2 — Manejo (46)

| Subdeck | Cartas | Tag |
|---|---|---|
| 1 - Ejes / patrones madre | 8 | `tag:eje` |
| 2 - Manejos comunes (core) | 18 | `tag:core` |
| 3 - Menos comunes | 20 | `tag:menos_comun` |

## Pilar 1 — Interrogatorio: tronco + llave (40)

| Subdeck | Cartas | Tag |
|---|---|---|
| 1 - Troncos (ejes) | 8 | `tag:tronco` |
| 2 - Llaves comunes (core) | 16 | `tag:core` |
| 3 - Llaves menos comunes | 16 | `tag:menos_comun` |

## Pilar 3 — Exploración + Estudios (34)

**A) Discriminador** (por herramienta: ECG, gasometría+brecha aniónica, lactato, TAC de cráneo, toxidromes, glucemia, troponina, brecha osmolar) y
**B) Panel** (por entidad: SCA, sepsis, intoxicado, ACV, CAD/EHH, anafilaxia, shock indiferenciado, FUO).

| Subdeck | Cartas | Tag |
|---|---|---|
| 1 - Discriminadores (herramienta) | 8 | `tag:discriminador` |
| 2 - Paneles (por entidad) | 8 | `tag:panel` |
| 3 - Signos, scores y antídotos | 18 | `tag:signo_score` |

## Chuletas (una página para recitar)

- [Interrogatorio](CHULETA_INTERROGATORIO.md) — 8 troncos + llaves core/menos
- [Estudios / exploración](CHULETA_ESTUDIOS.md) — discriminadores + paneles + scores + antídotos
- [Manejo](CHULETA_MANEJO.md) — 8 ejes + core + menos

## Cobertura (temas pedidos + añadidos indispensables)

- **Cardiovascular:** SCA, choque, paro/RCP (ACLS), (disección aórtica).
- **Neurológico:** ACV/ictus, status epiléptico.
- **Infeccioso:** sepsis, FUO.
- **Alérgico:** anafilaxia.
- **Endocrino:** CAD, EHH, **hipoglucemia**.
- **Respiratorio:** crisis asmática, EPOC exacerbado, TEP.
- **Hipertensión:** emergencia hipertensiva.
- **Toxicología:** enfoque general + paracetamol, opioides, benzodiacepinas, organofosforados, monóxido de carbono, tricíclicos, alcoholes tóxicos (metanol/etilenglicol), salicilatos; **tabla de antídotos y toxidromes**.
- **Metabólico/ECG:** **hiperkalemia**, **alteración del estado de alerta/coma**.
- **Sangrado:** **hemorragia digestiva alta**, hemorragia/transfusión masiva (enlace Trauma).
- **Ambiental:** **golpe de calor**, **hipotermia**.
- **Vía aérea:** **atragantamiento/OVACE adulto**, neumotórax a tensión, taponamiento.
- **Extra pedido:** mordeduras (profilaxis antirrábica + antitetánica), vacunación del adulto, síncope.
- **Enlaces:** Trauma/Cirugía (quemaduras, transfusión masiva), RCP.

## Regenerar

```bash
pip install genanki   # o usar la .venv del repo
python build_manejo_urg.py
python build_interrogatorio_urg.py
python build_estudios_urg.py
```

> Verifica **dosis, energías de desfibrilación, dosis de antídotos y metas** sede-dependientes
> (AHA/ACLS, ESC, Surviving Sepsis, centro toxicológico) y la versión vigente de cada guía antes del examen.
