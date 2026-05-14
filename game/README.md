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

## Mecánicas

- **Vida del paciente** (100 → 0): baja con errores graves. Si llega a 0 → game over con mensaje educativo.
- **Streak** de aciertos consecutivos: bonus al puntaje (+2 por nivel, máx +10 por acierto).
- **Tiempo del sinodal**: 20 segundos por decisión. Aviso visual a 10s, alarma roja a 5s. No responder = -10 vida.

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
├── index.html              # UI single-page
├── style.css               # tema oscuro clínico
├── game.js                 # motor (~200 líneas, vanilla JS)
└── scenarios/
    └── rcp/
        └── 001_paro_calle.json
```

## Añadir escenarios

1. Crea `scenarios/<tema>/<id>.json` siguiendo el formato del existente (campos: `id`, `titulo`, `contexto`, `pasos[]`).
2. Cada paso tiene `situacion` y `opciones[]` con `texto`, `correcta` (bool), `puntos` (int), `feedback` (string).
3. Cambia `SCENARIO_URL` en `game.js` o (futuro) usa el selector desde `manifest.json`.

## Stack

HTML5 + CSS3 + vanilla JavaScript. **Sin frameworks, sin servidor, sin LLM en runtime.** Token cost al jugar: **0**.
