#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Guion ECOE (mínimo) — Neumonía pediátrica GRAVE con hipoxemia (8 m, 8 kg, SpO₂ 89%).
4 tarjetas. Estación de urgencia: abordaje ABCDE; la hipoxemia define gravedad.
Cálculo de dosis incluido. Verbalización/umbrales en Extra.
"""
import os
import genanki

MODEL_ID = 1607392319  # cloze_estandar
DECK_ID = 1990012011
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
TAGS = ["ecoe", "guion", "pediatria", "urgencias", "neumonia", "hipoxemia"]
deck = genanki.Deck(DECK_ID, "Guiones ECOE::Neumonia pediatrica con hipoxemia")


def note(text, extra=""):
    deck.add_note(genanki.Note(model=model, fields=[text.strip(), extra.strip()], tags=TAGS))


note(
    "🫁👶 [Interrogatorio + ABCDE] Pregunta {{c1::inicio de tos/fiebre, dificultad respiratoria "
    "(tiraje, aleteo, quejido, cianosis, pausas), rechazo al alimento, diuresis, letargo, contacto infeccioso, "
    "atragantamiento y VACUNAS}}. Como hay hipoxemia, exploración = {{c2::ABCDE}}: vía aérea, "
    "{{c3::B: FR, SpO₂, tiraje subcostal/intercostal, aleteo, quejido, auscultación (estertores focales)}}, "
    "C perfusión, D alerta.",
    "Caso: 8 m, 8 kg, vacunación incompleta. T 38.9, FC 165, FR 62, SpO₂ 89%, tiraje, estertores en base derecha.",
)
note(
    "🫁👶 [Dx + diferenciales] {{c1::neumonía adquirida en la comunidad GRAVE con hipoxemia}} "
    "(fiebre, taquipnea para la edad, tiraje, aleteo, quejido, estertores focales, SpO₂ 89%). "
    "Vacunación incompleta → riesgo de {{c2::neumococo / H. influenzae b}}. "
    "Ddx: {{c3::bronquiolitis (más sibilancias difusas), sepsis de foco respiratorio, "
    "aspiración de cuerpo extraño (inicio súbito)}}.",
    "🗣️ «La SpO₂ de 89% lo cambia todo: ya NO es neumonía ambulatoria; es grave con hipoxemia "
    "→ oxígeno inmediato + hospitalización.»",
)
note(
    "🫁👶 [Estudios + manejo] {{c1::NO retrasar O₂ ni antibiótico por estudios}}; Rx tórax, BH/PCR, "
    "hemocultivo antes del antibiótico si no retrasa. Manejo URGENTE: "
    "{{c2::oxígeno YA, titular para SpO₂ &gt;92%}}, "
    "{{c3::ceftriaxona 50 mg/kg IV/IM cada 24 h → 8 kg = 400 mg}}, "
    "{{c4::paracetamol 10–15 mg/kg (80–120 mg); NO antitusígenos ni salbutamol de rutina; "
    "referir/hospitalizar con O₂ durante el traslado}}.",
    "Taquipnea OMS lactante 2–11 m ≥50 rpm. Alternativa: ampicilina 50 mg/kg c/6 h + gentamicina 6 mg/kg/día.",
)
note(
    "🫁👶 [Comunicación + alarma] {{c1::explicar: neumonía + oxígeno bajo (89%) = los pulmones no pasan "
    "suficiente O₂; no es seguro en casa, necesita hospital}}. "
    "Alarma: {{c2::respira más rápido, tiraje, quejido, labios morados, pausas, no come/bebe, letargo, "
    "convulsiones, manos frías, no orina, empeora pese al O₂}}. "
    "{{c3::completar vacunas (neumococo, Hib, influenza) al estabilizar}}.",
    "Error crítico: tratar como ambulatoria una neumonía con hipoxemia; no dar oxígeno.",
)

os.makedirs(OUT, exist_ok=True)
out_path = os.path.join(OUT, "Guiones_ECOE_Neumonia_Pediatrica.apkg")
genanki.Package([deck]).write_to_file(out_path)
print(f"OK -> {out_path}")
print(f"  Neumonía pediátrica: {len(deck.notes)} notas (deck {DECK_ID})")
