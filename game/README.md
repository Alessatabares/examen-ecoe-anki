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
| 👂 Otoscopia | Otalgia con fiebre en niño de 3 años | 17 | Básico |
| 🎧 Ruidos cardíacos | Fiebre y soplo nuevo en usuario de drogas IV | 16 | Intermedio-Avanzado |

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
