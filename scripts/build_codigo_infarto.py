#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Guion ECOE (mínimo) — Código Infarto / IAM con elevación del ST (STEMI inferior, 58 a).
4 tarjetas. Eje: ECG ≤10 min, NO esperar troponina, reperfusión; trampas (nitratos en IVD,
fibrinólisis en disección). Cifras ACC/AHA. Frases de oro y umbrales en Extra.
"""
import os
import genanki

MODEL_ID = 1607392319  # cloze_estandar
DECK_ID = 1990012016
OUT = os.path.join(os.path.dirname(__file__), "output")

model = genanki.Model(
    MODEL_ID, "Estudio Médico Cloze",
    fields=[{"name": "Text"}, {"name": "Extra"}],
    templates=[{"name": "Cloze", "qfmt": "{{cloze:Text}}",
                "afmt": '{{cloze:Text}}<hr id="extra">{{Extra}}'}],
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
TAGS = ["ecoe", "guion", "urgencias", "cardiologia", "iam", "stemi", "codigo-infarto"]
deck = genanki.Deck(DECK_ID, "Guiones ECOE::Codigo Infarto (IAM con elevacion del ST)")


def note(text, extra=""):
    deck.add_note(genanki.Note(model=model, fields=[text.strip(), extra.strip()], tags=TAGS))


note(
    "❤️ [Interrogatorio + exploración] Dolor torácico = posible urgencia cardiaca: "
    "{{c1::dolor opresivo retroesternal, irradiado a brazo izquierdo/mandíbula, &gt;20 min, "
    "diaforesis/náusea, factores de riesgo (HTA, DM, tabaco)}}. PREGUNTAR para decidir reperfusión: "
    "{{c2::sangrado, EVC, cirugía/trauma reciente, anticoagulantes, PDE5 (sildenafil/tadalafil), "
    "dolor desgarrante a la espalda o asimetría de pulsos (disección)}}. "
    "Exploración ABCDE + {{c3::ECG de 12 derivaciones en ≤10 min}}.",
    "Caso: 58 a, dolor 50 min, SpO₂ 94%, ansioso/diaforético/pálido.",
)
note(
    "❤️ [Dx por ECG + diferenciales] {{c1::elevación del ST en DII, DIII y aVF = STEMI inferior "
    "→ activar Código Infarto}}. Por ser inferior: {{c2::derivaciones derechas V3R-V4R (descartar infarto de "
    "ventrículo derecho); V7-V9 si sospecho posterior}}. "
    "Ddx: {{c3::NSTEMI/angina inestable, disección aórtica (¡NO fibrinolizar!), TEP, neumotórax, pericarditis}}.",
    "🗣️ «No espero la troponina para reperfundir si el ECG ya muestra STEMI.»",
)
note(
    "❤️ [Manejo inicial] {{c1::monitor + desfibrilador disponible, 2 vías IV, reposo/ayuno; "
    "O₂ SOLO si SpO₂ &lt;90% o dificultad respiratoria}}. Fármacos: "
    "{{c2::aspirina 160–325 mg masticada + 2º antiagregante (ticagrelor/prasugrel si ICP; clopidogrel si "
    "fibrinólisis) + anticoagulación (heparina/enoxaparina) + atorvastatina 80 mg}}. "
    "Cuidado: {{c3::nitratos NO si hipotensión, PDE5 reciente o infarto de VD; betabloqueador NO de rutina}}.",
    "Morfina IV titulada solo si el dolor persiste pese a nitrato. NO anticoagular/fibrinolizar si sospecha disección.",
)
note(
    "❤️ [Reperfusión + errores críticos] {{c1::angioplastia (ICP) primaria preferida → puerta-balón ≤90 min}}; "
    "si no disponible a tiempo y &lt;12 h de síntomas sin contraindicaciones → "
    "{{c2::fibrinólisis (puerta-aguja ≤30 min) + traslado farmacoinvasivo}}. "
    "NO fibrinólisis si {{c3::hemorragia intracraneal previa, EVC isquémico reciente, sangrado activo, "
    "disección aórtica, trauma/cirugía craneal, HTA severa no controlada}}. "
    "Errores: {{c4::mandar a casa con antiácido, esperar troponina, retrasar ECG/Código Infarto, "
    "olvidar aspirina o las derivaciones derechas}}.",
    "🗣️ Frase de oro: «dolor típico + elevación del ST = Código Infarto: ECG temprano, aspirina, monitor, "
    "anticoagulación, doble antiagregación y reperfusión; no espero troponina para abrir la arteria.»",
)

os.makedirs(OUT, exist_ok=True)
out_path = os.path.join(OUT, "Guiones_ECOE_Codigo_Infarto.apkg")
genanki.Package([deck]).write_to_file(out_path)
print(f"OK -> {out_path}")
print(f"  Código Infarto (STEMI): {len(deck.notes)} notas (deck {DECK_ID})")
