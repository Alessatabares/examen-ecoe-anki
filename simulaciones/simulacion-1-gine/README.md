# Simulación 1 — Ginecología (ITS / EIP)

Deck de Anki **`Simulaciones::Gine - Repaso 1`**. Repaso de la simulación de gineco-obstetricia
sobre infecciones de transmisión sexual y enfermedad inflamatoria pélvica, en formato ECOE.

## Estructura (36 tarjetas)

6 entidades × 6 tarjetas:

| # | Tarjeta | Para qué |
|---|---------|----------|
| 1 | Interrogatorio dirigido | qué preguntar y **qué orienta** cada respuesta |
| 2 | Exploración dirigida | **cómo hacerla y qué verbalizar** ante el examinador |
| 3 | Manejo | dx + tratamiento + consejería/parejas |
| 4–6 | Casos leve · moderado · difícil | la **misma enfermedad escalando**, para integrar |

Entidades: **Herpes genital · Sífilis primaria · Chancroide · VPH/condiloma · Molusco contagioso · EIP**
(con absceso tubo-ovárico y torsión ovárica como diferenciales en el caso difícil de EIP).

Los casos difíciles meten lo que cae de verdad en la ECOE: herpes primario en embarazo a término
(cesárea), sífilis en embarazada / alergia a penicilina, EIP → absceso vs torsión vs ectópico,
molusco extenso → sospecha de VIH.

## Importar a Anki

**Opción A — archivo listo (`.tsv`):** Anki → *Archivo → Importar* → elige `simulacion-1-gine.tsv`.
Separador: **Tabulador**. Campos: `Front`, `Back`, `Tags`. Marca **«Permitir HTML en los campos»**.

**Opción B — generar el `.apkg` (un clic):**

```bash
pip install genanki
python build_deck.py      # crea simulacion-1-gine.apkg y .tsv
```

Luego doble clic en `simulacion-1-gine.apkg`.

## Frase global ECOE

> «Paciente con lesión genital o dolor pélvico: evalúo estabilidad, embarazo y riesgo de ITS;
> hago exploración dirigida con inspección, especuloscopía o bimanual según el caso;
> tomo pruebas **sin retrasar el manejo empírico** cuando la sospecha clínica lo amerita;
> doy tratamiento, consejería sexual, manejo de parejas y seguimiento.»

---
Generado con Claude Code. Editar tarjetas en `build_deck.py` y reconstruir.
