# Simulación 3 — Trauma / Cirugía urgente

Deck de Anki **`Simulaciones::Trauma Cirugía - Repaso 3`**. Repaso de la simulación de
trauma/cirugía en formato ECOE, alineado con **ATLS 11ª edición (2024)**.

## Estructura (30 tarjetas)

10 entidades × 3 tarjetas:

| # | Tarjeta | Para qué |
|---|---------|----------|
| 1 | Abordaje | interrogatorio (qué pregunto y **qué orienta**) + exploración (**cómo y qué verbalizar**: xABCDE, eFAST, auscultación/percusión, compresión pélvica) |
| 2 | Manejo | dx + tratamiento (dosis) + **criterios de quirófano / referencia** + frase ECOE |
| 3 | Caso escalonado | una viñeta **estable → respondedor/transitorio → inestable-crítico** con la conducta de cada nivel (el crítico = amenaza vital → intervención salvadora) |

**Entidades:** Base (xABCDE / politraumatizado) · Objeto penetrante encajado · Trauma penetrante
inestable · Trauma cerrado/politrauma · Lesión esplénica (signo de Kehr) · Neumotórax a tensión ·
Taponamiento cardíaco · Hemotórax masivo · Tórax inestable/flail chest · Fractura pélvica inestable.

## Actualizaciones ATLS 11ª ed. incorporadas (verificadas)

- **xABCDE:** el control de **hemorragia exanguinante** se antepone a la vía aérea.
- **Reanimación de control de daños:** hipotensión permisiva, **cristaloide tibio solo como puente**,
  **hemoderivados precoces 1:1:1 (o sangre total O−)** y **ácido tranexámico (TXA)**.
- **Descompresión con aguja:** **5º EIC línea axilar anterior/media** (catéter ≥8 cm); 2º EIC LMC como
  alternativa y en pediatría. Tubo de tórax en el **triángulo de seguridad** (4º–5º EIC).
- **Taponamiento:** la **cirugía** es el tratamiento de elección; la **pericardiocentesis** es solo puente.
- **Penetrante:** la **inestabilidad por sí sola** ya indica quirófano; **FAST negativo no excluye** lesión.
- **Hemotórax masivo:** toracotomía si **>1500 mL** inmediatos o **>200 mL/h** sostenido.
- **Pelvis:** binder centrado en **trocánteres mayores** (no en la cintura).

## Importar a Anki

**Opción A — archivo listo (`.tsv`):** Anki → *Archivo → Importar* → `simulacion-3-trauma-cirugia.tsv`.
Separador: **Tabulador**. Campos: `Front`, `Back`, `Tags`. Marca **«Permitir HTML en los campos»**.

**Opción B — generar el `.apkg`** (con el venv aislado del repo):

```bash
../../.venv/bin/python build_deck.py
```

Luego doble clic en `simulacion-3-trauma-cirugia.apkg`.

## Frases ECOE de cierre (incluidas en las tarjetas de Manejo)

- **Base:** «Activo el protocolo de transfusión masiva 1:1:1 y uso el cristaloide solo como puente.»
- **Objeto encajado:** «Objeto impalado: lo estabilizo, no lo retiro, y traslado a quirófano para extracción controlada.»
- **Penetrante inestable:** «No pierdo tiempo en TAC; activo transfusión masiva y lo llevo a quirófano.»
- **Lesión esplénica:** «Si está estable, TAC y manejo no operatorio vigilado; si está inestable con FAST+, laparotomía.»
- **Neumotórax a tensión:** «Descomprimo de inmediato y luego coloco tubo de tórax; la radiografía es de control.»
- **Taponamiento:** «Estabilizo con volumen y activo cirugía; la pericardiocentesis es solo puente.»
- **Hemotórax masivo:** «Tubo de tórax y reanimo con sangre; si drena >1500 mL o sigue sangrando, toracotomía.»
- **Tórax inestable:** «Analgesia agresiva, fisioterapia y vigilancia de contusión pulmonar; intubo solo si falla la respiración.»
- **Fractura pélvica:** «Binder en trocánteres mayores, transfundo 1:1:1 y, si sigue sangrando, angioembolización o fijación externa.»

---
Generado con Claude Code. Editar tarjetas en `build_deck.py` y reconstruir.
