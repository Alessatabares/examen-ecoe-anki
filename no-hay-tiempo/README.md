# No hay tiempo — decks de rescate ECOE (< 3 días)

Decks de **rescate** para cuando tienes que pasar una estación de la ECOE y te quedan
**menos de 3 días**. Todas las especialidades comparten la **misma arquitectura de 3 pilares**,
y cada pilar tiene **3 subdecks** (patrón madre/ejes → más probable/core → menos probable):

```
PREGUNTO      → tronco + llave            (Pilar 1: Interrogatorio)
EXPLORO/PIDO  → herramienta + panel       (Pilar 3: Exploración + Estudios)
MANEJO        → eje + bifurcación         (Pilar 2: Manejo)
```

- **Interrogatorio:** abres con el **tronco** (lo que preguntas igual en todo el grupo) y cierras con la **llave** (la pregunta que fija el dx).
- **Estudios:** **discriminador** (una herramienta separa por un hallazgo) + **panel** (qué pides por entidad) + **signos/scores**.
- **Manejo:** **eje/patrón madre** (la regla que decide la bifurcación) + conducta (verbalizo → consejería → red flag).

> Para estudiar **a fondo** existen aparte los decks por **4 capas** (Flujo macro · Componentes · Ejes · Manejo/DDx)
> en las carpetas raíz del repo. Estos son los de **rescate**: patrón y bifurcación, no minucia.

## Especialidades (923 cartas)

| Carpeta | Interrog. | Estudios | Manejo | Total | Chuletas |
|---|--:|--:|--:|--:|---|
| [Ginecología](ginecologia/) | 43 | 33 | 42 | **118** | [Interrog.](ginecologia/CHULETA_INTERROGATORIO.md) |
| [Obstetricia](obstetricia/) | 42 | 33 | 42 | **117** | — |
| [Cirugía](cirugia/) | 42 | 33 | 42 | **117** | — |
| [Medicina Interna](medicina_interna/) | 45 | 34 | 50 | **129** | [I](medicina_interna/CHULETA_INTERROGATORIO.md) · [E](medicina_interna/CHULETA_ESTUDIOS.md) · [M](medicina_interna/CHULETA_MANEJO.md) |
| [Medicina Familiar](medicina_familiar/) | 64 | 49 | 88 | **201** | [I](medicina_familiar/CHULETA_INTERROGATORIO.md) · [E](medicina_familiar/CHULETA_ESTUDIOS.md) · [M](medicina_familiar/CHULETA_MANEJO.md) |
| [Pediatría](pediatria/) | 40 | 34 | 47 | **121** | [I](pediatria/CHULETA_INTERROGATORIO.md) · [E](pediatria/CHULETA_ESTUDIOS.md) · [M](pediatria/CHULETA_MANEJO.md) |
| [Urgencias](urgencias/) | 40 | 34 | 46 | **120** | [I](urgencias/CHULETA_INTERROGATORIO.md) · [E](urgencias/CHULETA_ESTUDIOS.md) · [M](urgencias/CHULETA_MANEJO.md) |

## Cómo usarlo en < 3 días

1. **Día 1 — patrones madre.** Recita en voz alta los **ejes/troncos** de la especialidad (es el guion que abre cualquier estación) usando la **chuleta**.
2. **Día 2 — comunes (core).** Repasa las tablas de **llaves core** y **manejos core**; simula 4-6 casos completos: tronco → herramienta/panel → eje de manejo.
3. **Día 3 — menos comunes + trampas.** Las menos probables y las trampas de secuencia/red flags. Importa los `.apkg` a Anki para repaso espaciado.

> Las **chuletas** (1 página por pilar) son la herramienta real de < 3 días; los `.apkg` son el repaso espaciado.

## Importar a Anki

Cada carpeta tiene `output/` con:
- subdecks sueltos (`Manejo_02_Core.apkg`, etc.)
- un paquete por pilar (`No_Hay_Tiempo_<esp>_<pilar>_TODOS.apkg`)

Los `deck_id` y `model_id` son estables (registrados en `../ids.json`): reimportar **actualiza** las
cartas existentes sin duplicar.

## Regenerar

```bash
pip install genanki   # o usar la .venv del repo
# desde la carpeta de la especialidad:
python build_manejo_*.py && python build_interrogatorio_*.py && python build_estudios_*.py
```

## Estructura

```
no-hay-tiempo/
├── README.md                 (este índice)
├── <especialidad>/
│   ├── README.md
│   ├── CHULETA_*.md          (hojas de recitación de 1 página)
│   ├── build_manejo_*.py
│   ├── build_interrogatorio_*.py
│   ├── build_estudios_*.py
│   └── output/               (.apkg)
└── ...
```

> Contenido orientado a **patrón y bifurcación** con guías estándar (ESC, AHA, ADA, KDIGO, GOLD, GINA,
> ATLS, AAP, PALS, GPC MX, etc.). **No** sustituye la guía vigente: verifica dosis, metas y umbrales
> **sede-dependientes** antes del examen.
