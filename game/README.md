# ECOE Trainer · Videojuego de simulaciones clínicas

Entrena las decisiones y verbalizaciones que esperan los sinodales en simulaciones ECOE.

## Cómo jugar

**Online (recomendado)**: https://alessatabares.github.io/examen-ecoe-anki/game/

**Localmente**: navegadores bloquean `fetch()` desde `file://` por CORS. Hay que servir los archivos:

```bash
cd game/
python3 -m http.server 8000
# luego abre http://localhost:8000 en tu navegador
```

## Escenarios disponibles

| Tema | Escenario | Pasos | Dificultad |
|---|---|---|---|
| 🫀 RCP | Paro presenciado en vía pública | 18 | Básico-Intermedio |
| 🫀 RCP | Politraumatizado en shock hipovolémico | 11 | Intermedio |
| 🫀 RCP | Atragantamiento en restaurante (OVACE) | 12 | Básico-Intermedio |
| 🫀 RCP | Paro por acidosis severa en CAD | 11 | Intermedio-Avanzado |
| 🫀 RCP | Paro durante diálisis por hiperpotasemia | 11 | Intermedio-Avanzado |
| 🫀 RCP | Hipotermia severa tras inmersión | 12 | Avanzado |
| 🫀 RCP | Sobredosis de opioides con paro respiratorio | 11 | Básico-Intermedio |
| 🫀 RCP | Taponamiento por herida precordial | 11 | Avanzado |
| 🫀 RCP | Neumotórax a tensión en paciente ventilado | 11 | Intermedio-Avanzado |
| 🫀 RCP | TEP masivo postoperatorio | 11 | Avanzado |
| 🫀 RCP | Anafilaxia por picadura con paro inminente | 11 | Intermedio-Avanzado |
| 👂 Otoscopia | Otalgia con fiebre en niño de 3 años (OMA pediátrica) | 17 | Básico |
| 👂 Otoscopia | OMA perforada con otorrea purulenta súbita | 11 | Básico-Intermedio |
| 👂 Otoscopia | OMC simple con perforación central permanente | 11 | Intermedio |
| 👂 Otoscopia | Mastoiditis aguda como complicación de OMA | 11 | Intermedio-Avanzado |
| 👂 Otoscopia | OME (otitis serosa) en niño post-IRA | 11 | Intermedio |
| 👂 Otoscopia | Otolicuorrea (LCR) por fractura de peñasco | 11 | Avanzado |
| 👂 Otoscopia | Disfunción trompa Eustaquio post-vuelo | 11 | Básico-Intermedio |
| 👂 Otoscopia | Perforación timpánica traumática por bofetada | 11 | Intermedio |
| 👂 Otoscopia | Miringitis bullosa con otorrea serosanguinolenta | 11 | Intermedio |
| 👂 Otoscopia | Hemotímpano post-TCE (TM íntegra azul) | 11 | Avanzado |
| 👂 Otoscopia | Colesteatoma con otorrea fétida crónica | 11 | Avanzado |
| 👂 Otoscopia | Otomicosis con detritos algodonosos | 11 | Intermedio |
| 🎧 Ruidos cardíacos | Fiebre y soplo nuevo en usuario de drogas IV | 16 | Intermedio-Avanzado |

> **RCP (11 escenarios)** — 5H/5T canónicas (hipovolemia, hipoxia, hidrogeniones, hiperpotasemia, hipotermia, tóxicos, taponamiento, neumotórax a tensión, trombosis coronaria/IAM, TEP) + **anafilaxia** (AHA 2020).
>
> **Otoscopia (12 escenarios)** — patología de oído medio con foco en **caracterización del líquido por oído**:
> - 🟡 **Purulento** (OMA perforada, OMC simple, mastoiditis)
> - 💧 **Transparente/claro** (OME color miel, otolicuorrea por LCR con halo sign, disfunción trompa)
> - 🔴 **Hemorrágico** (perforación traumática, miringitis bullosa serosanguinolenta, hemotímpano azul-violáceo)
> - ⚪ **Blanquecino/fétido** (colesteatoma, otomicosis)

## Mecánicas

- **Vida del paciente** (100 → 0): baja con errores graves. Si llega a 0 → game over.
- **Streak** de aciertos consecutivos: bonus al puntaje (+2 por nivel, máx +10 por acierto).
- **Tiempo del sinodal**: 20 segundos por decisión. Aviso visual a 10s, alarma roja a 5s.

## Veredictos finales

| % aciertos | Veredicto |
|---|---|
| ≥85% | 🏆 Listo para sala de simulación ECOE |
| ≥70% | ✅ Aprobado, pulir detalles |
| ≥50% | ⚠️ En el límite, repasa |
| <50% | ❌ Repaso profundo desde Capa 1 |

## Estructura

```
game/
├── index.html              # UI single-page (menú + escenario + juego + final)
├── style.css               # tema oscuro clínico
├── game.js                 # motor (~280 líneas, vanilla JS)
└── scenarios/
    ├── manifest.json       # lista de escenarios disponibles
    ├── rcp/
    ├── otoscopia/
    └── ruidos_cardiacos/
```

## Añadir escenarios

1. Crea `scenarios/<tema>/<id>.json` siguiendo el formato del existente (campos: `id`, `titulo`, `tema`, `contexto`, `pasos[]`).
2. Cada paso tiene `situacion` y `opciones[]` con `texto`, `correcta` (bool), `puntos` (int), `feedback` (string).
3. Añade el escenario al `scenarios/manifest.json` (id, tema, icon, titulo, dificultad, pasos, url).
4. El motor lo carga automáticamente — no hay que tocar `game.js`.

## Stack

HTML5 + CSS3 + vanilla JavaScript. **Sin frameworks, sin servidor, sin LLM en runtime.** Token cost al jugar: **0**.
