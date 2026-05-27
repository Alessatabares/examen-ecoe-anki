# Patrones Madre — Formato Embudo Q&A

Decks transversales que entrenan el reconocimiento de un **síndrome madre** (shock, dolor torácico, abdomen agudo, alteración del estado mental, disnea aguda, etc.). Viven por encima de los temas: una vez identificado el patrón madre, te dispara la pregunta correcta sobre el sistema/tema específico.

No reemplazan los decks por tema (RCP, gineco, cirugía…). Los complementan.

## Filosofía

Para ECOE, el sinodal describe una escena. La estudiante debe:

1. Reconocer el **patrón madre** ("esto es shock").
2. Identificar la **subcausa** ("es hipovolémico por sangrado").
3. Traducir mentalmente cada signo a su **fisiopatología** ("la piel fría es vasoconstricción compensatoria").
4. Disparar el **manejo justificado** ("dos vías gruesas porque necesita reposición rápida").

El embudo va de lo general a lo concreto. Cada nivel se construye sobre el anterior.

## Estructura del deck — 4 niveles

Cada patrón madre se construye como un solo deck Q&A con 4 niveles secuenciales. La cantidad de subcausas (N) determina el total de cards: **1 + 3N** cards (N1: 1 card global, N2-N4: una card por subcausa por nivel).

Para shock hipovolémico N=4 → 1 + 12 = **13 cards**.

### Nivel 1 — Identificar el patrón madre (1 card)

Una sola card que define el patrón en términos de fisiología pura.

| Front | Back |
|---|---|
| Pregunta global sobre qué falla en el sistema | Nombre del patrón madre + metáfora unificadora |

**Ejemplo (shock hipovolémico):**
- Front: *Choque donde lo que falla es el líquido en el sistema circulatorio*
- Back: *Shock hipovolémico — tanque vacío*

### Nivel 2 — Imagen mental → nombre formal (N cards)

Una card por cada subcausa. El front es una **metáfora visual** (no clínica todavía); el back es el **nombre formal** de la subcausa.

| Front (imagen mental) | Back (nombre formal) |
|---|---|
| Metáfora corporal/mecánica que evoca el mecanismo | Nombre técnico + lista de escenarios donde aparece |

**Ejemplo:**
- Front: *Además del líquido pierdes glóbulos rojos y "camiones de oxígeno" (Hb)*
- Back: *Hipovolémico hemorrágico (HDA, trauma, ectópico roto, posparto)*

### Nivel 3 — Mecanismo fisiopatológico → signo clínico (N cards)

Una card por subcausa. Front y back son **listas numeradas correlacionadas**: el ítem 1 del front corresponde al ítem 1 del back, etc. Entrena el "por qué" detrás de cada signo.

| Front (mecanismos numerados) | Back (signos numerados) |
|---|---|
| Cabecera: subcausa identificada<br>1. Mecanismo fisiopatológico A<br>2. Mecanismo B<br>3. ... | 1. Signo/síntoma que produce A<br>2. Signo que produce B<br>3. ... |

**Ejemplo (hipovolémico por vómito/diarrea):**
- Front: *1. Pérdida de agua intravascular · 2. ↓ volumen circulante · 3. Vasoconstricción periférica · 4. ↓ retorno venoso al pararse · 5. Riñón retiene agua · 6. ↓ volumen intersticial*
- Back: *1. Mucosas secas, sed · 2. Taquicardia, hipotensión · 3. Piel fría, palidez, llenado capilar lento · 4. Hipotensión ortostática · 5. Oliguria · 6. Ojos hundidos*

### Nivel 4 — Escena clínica → acción de manejo (N cards)

Una card por subcausa. El front describe **la escena del paciente** + una lista numerada de **problemas/riesgos visualizados** (con tensión clínica, no descripciones técnicas planas). El back es la lista numerada de **acciones de manejo** correspondientes.

| Front (escena + problemas) | Back (acciones correspondientes) |
|---|---|
| Cabecera: escena clínica vívida del paciente<br>1. Problema/riesgo redactado como imagen<br>2. ... | 1. Acción concreta que lo resuelve<br>2. ... |

**Ejemplo (hipovolémico hemorrágico):**
- Front cabecera: *Paciente sangrante (HDA, trauma, ectópico, posparto) pálido, taquicárdico, hipotenso*
- Front items: *1. Sangrante e inestable — no es momento de estar solo · 2. Si el líquido entra lento, se va antes de llegar al sistema · 3. Va a necesitar sangre — pídela antes de necesitarla · 4. Aunque le entres litros, no llevan oxígeno como la sangre · 5. La hemorragia sigue corriendo hasta que cierres la llave*
- Back items: *1. ABCDE + pedir ayuda + monitorización · 2. Dos vías gruesas + cristaloide inicial · 3. BH, grupo y cruzadas, coagulación · 4. Protocolo de transfusión si inestable · 5. FAST / endoscopia / cirugía / USG según contexto*

## Reglas de redacción

- **N1**: una sola card, pregunta global, sin detalles clínicos.
- **N2**: la imagen mental del front NO debe contener el nombre técnico. Tiene que ser metáfora pura. El nombre vive solo en el back.
- **N3**: front y back son listas con la **misma cantidad de ítems**, numerados, correspondencia 1↔1. Sin acciones de manejo aquí — solo fisiopatología → semiología.
- **N4**: el front es **narrativo**, evoca tensión clínica ("la vía aérea se está cerrando por edema", no "vía aérea en riesgo"). El back es **accionable** ("ABCDE + evaluar inhalación", no "evaluar al paciente").
- Mantener entre 4-8 ítems por lista en N3 y N4. Si una subcausa necesita más, considerar partirla en dos cards.

## Especificaciones técnicas

- **Modelo Q&A**: reusar `MODEL_QA_ID = 1607392320` (ya existe en gineco-obstetricia capa 5).
- **DECK_ID**: nuevo por cada patrón madre. Generar con `random.randrange(1 << 30, 1 << 31)` y registrar en `ids.json`.
- **DECK_NAME**: `Patrones Madre::<Nombre del patrón>`. Ejemplo: `Patrones Madre::Shock Hipovolémico`.
- **Tags base**: `patrones_madre`, `ecoe`, slug del patrón (`shock_hipovolemico`), nivel (`n1`/`n2`/`n3`/`n4`), subcausa (`hemorragico`, `gi`, etc.).
- **Output**: `patrones_madre/output/Patrones_Madre_<Slug>.apkg`.
- **Build script**: `patrones_madre/build/<slug>.py`.

## Workflow para añadir un nuevo patrón madre

1. Definir el patrón madre y sus **N subcausas**.
2. Para cada subcausa, redactar 3 cards (N2, N3, N4) siguiendo las reglas de arriba.
3. Mostrar las cards en chat para aprobación antes de generar el `.apkg`.
4. Crear `patrones_madre/build/<slug>.py` reusando la estructura del `shock_hipovolemico.py`.
5. Ejecutar `python3 patrones_madre/build/<slug>.py`.
6. Actualizar `ids.json` con la nueva entrada.

## Patrones madre planeados

- ✅ Shock hipovolémico (4 subcausas: GI, hemorrágico, quemaduras, pediátrico)
- ⏳ Shock séptico / distributivo
- ⏳ Shock cardiogénico
- ⏳ Shock obstructivo
- ⏳ Dolor torácico
- ⏳ Abdomen agudo
- ⏳ Alteración del estado mental
- ⏳ Disnea aguda
