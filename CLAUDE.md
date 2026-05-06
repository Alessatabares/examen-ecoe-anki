# Anki Deck Builder — Estudio Médico por Capas

Asistente para construir decks de Anki en `.apkg` usando `genanki`, optimizados para aprendizaje por **capas, ejes y sistemas** (estilo Müsel).

## Filosofía pedagógica

El usuario aprende construyendo desde el esqueleto hacia el detalle, conectando fisiología → presentación → manejo. Nunca empieces por minucias técnicas: primero el flujo macro, después los componentes, después los ejes transversales.

**Arquitectura por defecto (3 capas cloze + subdecks Q&A):**

| Capa | Tipo | Contenido | Deck path |
|---|---|---|---|
| 1 | Cloze | Flujo macro / algoritmo / esqueleto del tema | `Tema::Capa 1 - Flujo Macro` |
| 2 | Cloze | Profundización técnica por componente (números, técnica, ratios) | `Tema::Capa 2 - Componentes` |
| 3 | Cloze | Ejes transversales: fisiopatología → presentación → pista clínica → manejo | `Tema::Capa 3 - Ejes` |
| 4+ | Q&A clásico | Casos integradores, preguntas tipo examen, diagnóstico diferencial | `Tema::Avanzado::<subtema>` |

## Workflow obligatorio

Antes de generar nada:

1. **Pregunta y confirma:** tema, guías/fuentes y año (busca en web la versión más reciente si la guía cambia con frecuencia), audiencia (adulto/pediátrico/neonatal — decks separados), formato de examen (ECOE → verbalización al sinodal), capa que toca construir.
2. **Propón la arquitectura** y la lista completa de tarjetas de la capa solicitada en chat, antes de tocar código. Espera confirmación.
3. **Genera el `.apkg`** solo después del OK.
4. **Preserva IDs estables** entre capas y revisiones (ver sección IDs).

## Especificaciones técnicas del modelo

```python
import genanki

DECK_ID = <int de 10 dígitos, único por capa>
MODEL_ID = 1607392319  # Reusable para todas las capas cloze

model = genanki.Model(
    MODEL_ID,
    'Estudio Médico Cloze',
    fields=[{'name': 'Text'}, {'name': 'Extra'}],
    templates=[{
        'name': 'Cloze',
        'qfmt': '{{cloze:Text}}',
        'afmt': '{{cloze:Text}}<hr id="extra">{{Extra}}',
    }],
    css="""
    .card {
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      font-size: 19px; text-align: left; color: #1a1a1a;
      background-color: #fafafa; padding: 20px; line-height: 1.5;
    }
    .cloze { font-weight: 600; color: #2563eb; }
    #extra { margin-top: 16px; border: none; border-top: 1px solid #d4d4d4; }
    """,
    model_type=genanki.Model.CLOZE,
)
```

## Reglas de contenido por tarjeta

- **Capa 1:** una idea por tarjeta, sin números técnicos. Solo secuencia y bifurcaciones.
- **Capa 2:** números, técnica, ratios. Una tarjeta por componente.
- **Capa 3:** estructura cuádruple por causa/eje (fisiopatología → presentación → pista desde valoración inicial → manejo). Puede requerir 2–3 cards por causa.
- **Verbalización** (formato ECOE): siempre en el campo `Extra` con prefijo `🗣️ ECOE: "..."`. Nunca en el campo `Text`.
- **Tags consistentes:** `capa1` / `capa2` / `capa3` + tema + subsistema + `ecoe` si lleva verbalización + año de guía si es relevante.
- **Cada cloze cubre una unidad de información completa**, no fragmentos arbitrarios.

## Output

`<tema>/output/<Tema>_<Audiencia>_Capa<N>.apkg`

Cada tema vive en su propio subdirectorio en raíz, con su propio `build/` y `output/`.

## Búsqueda web obligatoria

Para guías que se actualizan (AHA, ESC, ATLS, GINA, GOLD, KDIGO, etc.), siempre verificar la versión más reciente con web search antes de incluir números técnicos.

## Registro de IDs (`ids.json`)

Antes de generar cualquier deck, lee `ids.json`. Después de generar, actualízalo añadiendo la nueva entrada.

Reglas:
- Si la combinación `tema + audiencia + capa` ya existe → **reusa ese `deck_id`**.
- Si no existe → genera uno nuevo con `random.randrange(1 << 30, 1 << 31)` y regístralo.
- Nunca dupliques `deck_id`s.

## Anti-patrones — NO hacer

- ❌ Generar `.apkg` sin haber mostrado y confirmado el contenido en chat primero
- ❌ Mezclar audiencias (adulto + pediátrico) en el mismo deck
- ❌ Cambiar `DECK_ID` o `MODEL_ID` entre revisiones de la misma capa
- ❌ Poner verbalización ECOE dentro del cloze (debe ir en `Extra`)
- ❌ Saltarse Capa 1 e ir directo a detalle técnico
- ❌ Q&A en capas 1–3 (esas son siempre cloze)

## Estructura del repo

```
.
├── CLAUDE.md
├── ids.json
├── requirements.txt
├── rcp/
│   ├── build/
│   └── output/
└── otoscopia/
    ├── build/
    └── output/
```

Cada nuevo tema se añade como subdirectorio `<tema>/` en raíz con su propio `build/` y `output/`. `ids.json` y `CLAUDE.md` permanecen únicos en raíz.
