#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exploración básica ECOE — interrogatorio + exploración física básica.
Decks SEPARADOS por audiencia (CLAUDE.md: no mezclar adulto y pediátrico).
Verbalización ECOE / umbrales van en el campo Extra.
"""
import os
import genanki

MODEL_ID = 1607392319  # cloze_estandar (reusable, no cambiar)
DECK_ADULTO = 1990012003
DECK_PEDIA = 1990012004
OUT = os.path.join(os.path.dirname(__file__), "output")

model = genanki.Model(
    MODEL_ID,
    "Estudio Médico Cloze",
    fields=[{"name": "Text"}, {"name": "Extra"}],
    templates=[{
        "name": "Cloze",
        "qfmt": "{{cloze:Text}}",
        "afmt": '{{cloze:Text}}<hr id="extra">{{Extra}}',
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


def note(deck, text, extra="", tags=None):
    deck.add_note(genanki.Note(model=model, fields=[text.strip(), extra.strip()], tags=tags or []))


# ============================ ADULTO ============================
TA = ["ecoe", "exploracion-basica", "adulto"]
adulto = genanki.Deck(DECK_ADULTO, "Exploracion Basica ECOE::Adulto - Interrogatorio y Exploracion")

note(adulto,
    "🧑 [Interrogatorio adulto — estructura] En orden: "
    "1) {{c1::ficha de identificación (nombre, edad, ocupación)}}, "
    "2) {{c2::motivo de consulta en palabras del paciente}}, "
    "3) {{c3::padecimiento actual con ALICIA}}, "
    "4) {{c4::antecedentes con SAMPLER}}, "
    "5) {{c5::interrogatorio por aparatos y sistemas}}.",
    "🗣️ Apertura (da el punto de comunicación): «Buenos días, soy [nombre], estudiante de medicina, "
    "¿me permite hacerle unas preguntas y explorarle?» — consentimiento + presentación.",
    TA)

note(adulto,
    "🧑 [ALICIA — caracterizar el síntoma] "
    "{{c1::A}}parición (¿desde cuándo?, súbito o gradual), "
    "{{c2::L}}ocalización, "
    "{{c3::I}}rradiación, "
    "{{c4::C}}aracterísticas (tipo e intensidad 0–10), "
    "{{c5::I}}ntensificantes/atenuantes, "
    "{{c6::A}}compañantes (síntomas asociados → aquí cazas banderas rojas).",
    "", TA)

note(adulto,
    "🧑 [SAMPLER — antecedentes (dilo completo = puntos)] "
    "{{c1::S}}íntomas asociados, "
    "{{c2::A}}lergias, "
    "{{c3::M}}edicamentos, "
    "{{c4::P}}atologías previas y cirugías, "
    "{{c5::L}}a última comida, "
    "{{c6::E}}ventos previos, "
    "{{c7::R}}iesgos (tabaco, alcohol, sexual, familiar, ocupacional).",
    "", TA)

note(adulto,
    "🧑 [Exploración adulto — arranque y técnica] "
    "{{c1::lavado de manos + consentimiento + privacidad}}; SIEMPRE empieza por "
    "{{c2::signos vitales y estado general}}; cada región en el orden "
    "{{c3::inspección → palpación → percusión → auscultación}} "
    "(excepción ABDOMEN: inspección → auscultación → percusión → palpación).",
    "Vitales normales: FC 60–100 · FR 12–20 · TA &lt;120/80 (HTA ≥140/90) · "
    "Temp 36–37.5 (fiebre ≥38) · SpO₂ ≥95% (hipoxemia &lt;90%).",
    TA)

note(adulto,
    "🧑 [Exploración adulto — orden céfalo-caudal] "
    "1) {{c1::cabeza y cuello (ojos, ORL, ganglios, tiroides, ingurgitación yugular)}}, "
    "2) {{c2::tórax: cardiaco y pulmonar}}, "
    "3) {{c3::abdomen}}, "
    "4) {{c4::extremidades (pulsos, edema, llenado capilar)}}, "
    "5) {{c5::neurológico básico (estado de alerta, fuerza, sensibilidad)}}.",
    "", TA)

note(adulto,
    "🧑 [Lo que sube de 3 a 4 en exploración] "
    "Verbaliza {{c1::hallazgos positivos Y negativos relevantes}} "
    "(ej.: «abdomen blando, SIN signos de irritación peritoneal») y explora "
    "{{c2::dirigido al motivo de consulta}}, no al azar.",
    "", TA)


# ============================ PEDIÁTRICO ============================
TP = ["ecoe", "exploracion-basica", "pediatria"]
pedia = genanki.Deck(DECK_PEDIA, "Exploracion Basica ECOE::Pediatrico - Interrogatorio y Exploracion")

note(pedia,
    "👶 [Interrogatorio pediátrico — qué AÑADE] Además del ALICIA del motivo, SIEMPRE: "
    "{{c1::edad exacta y peso}}, "
    "{{c2::perinatales (embarazo, parto, APGAR, complicaciones)}}, "
    "{{c3::alimentación y desarrollo psicomotor}}, "
    "{{c4::esquema de vacunación}}, "
    "{{c5::quién lo cuida y red de apoyo}}.",
    "El interrogatorio suele ser INDIRECTO (al cuidador); confirma quién da la información.",
    TP)

note(pedia,
    "👶 [Banderas rojas a interrogar] "
    "{{c1::fiebre — en menor de 3 meses ≥38 °C = urgencia}}, "
    "{{c2::rechazo al alimento}}, "
    "{{c3::irritabilidad o letargo}}, "
    "{{c4::dificultad respiratoria}}, "
    "{{c5::vómito verde, llanto inconsolable y datos de deshidratación}}.",
    "", TP)

note(pedia,
    "👶 [Exploración pediátrica — abordaje] "
    "{{c1::oportunista: aprovecha cuando esté tranquilo (ausculta primero si no llora)}}, "
    "{{c2::explora en brazos del cuidador si es pequeño}}, "
    "y deja para el FINAL lo molesto: {{c3::oídos (otoscopia) y garganta}}.",
    "", TP)

note(pedia,
    "👶 [Triángulo de Evaluación Pediátrica — impresión en segundos] Evalúa 3 lados: "
    "{{c1::Apariencia (tono, interacción, consolabilidad, mirada, llanto)}}, "
    "{{c2::trabajo Respiratorio (tiraje, aleteo, quejido, ruidos)}}, "
    "{{c3::Circulación cutánea (color: palidez, cianosis, moteado)}}.",
    "Si un lado está alterado = inestable → estabiliza antes de continuar la exploración.",
    TP)

note(pedia,
    "👶 [Exploración peds — base objetiva] Toma "
    "{{c1::signos vitales POR EDAD (FC y FR cambian con la edad)}}, "
    "{{c2::antropometría: peso, talla y perímetro cefálico}}, "
    "y en lactante {{c3::fontanela (normotensa, abombada o deprimida)}}.",
    "Taquipnea (OMS): &lt;2m ≥60 · 2–11m ≥50 · 1–5a ≥40 rpm. "
    "Llenado capilar normal &lt;2 s (&gt;3 s = alarma). Hipoxemia SpO₂ &lt;90–92%.",
    TP)

note(pedia,
    "👶 [Exploración peds — por sistemas] "
    "{{c1::estado general e hidratación (mucosas, llanto con lágrimas, signo del pliegue)}}, "
    "{{c2::tórax: esfuerzo respiratorio y auscultación}}, "
    "{{c3::abdomen}}, "
    "{{c4::piel (exantema, petequias)}}, "
    "{{c5::signos meníngeos}}; oídos y garganta al FINAL.",
    "", TP)


# ============================ BUILD ============================
os.makedirs(OUT, exist_ok=True)
out_path = os.path.join(OUT, "Exploracion_Basica_Adulto_Pediatrico.apkg")
genanki.Package([adulto, pedia]).write_to_file(out_path)
print(f"OK -> {out_path}")
print(f"  Adulto:     {len(adulto.notes)} notas (deck {DECK_ADULTO})")
print(f"  Pediátrico: {len(pedia.notes)} notas (deck {DECK_PEDIA})")
