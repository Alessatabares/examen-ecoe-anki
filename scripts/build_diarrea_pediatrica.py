#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Guiones ECOE — Diarrea pediátrica (2 escenarios), una tarjeta por bloque de rúbrica.
Caso A: disentería bacteriana con sangre (Valeria 4 a, 16 kg) → Plan B + ciprofloxacino.
Caso B: GEA viral con deshidratación moderada (11 kg) → Plan B, SIN antibiótico.
Cálculos de dosis incluidos (alto rendimiento ECOE). Verbalización/umbrales en Extra.
"""
import os
import genanki

MODEL_ID = 1607392319  # cloze_estandar
DECK_DISENTERIA = 1990012006
DECK_DESHIDRA = 1990012007
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


def note(deck, text, extra="", tags=None):
    deck.add_note(genanki.Note(model=model, fields=[text.strip(), extra.strip()], tags=tags or []))


# ==================== CASO A: DISENTERÍA BACTERIANA ====================
TA = ["ecoe", "guion", "pediatria", "diarrea", "disenteria"]
disenteria = genanki.Deck(DECK_DISENTERIA, "Guiones ECOE::Diarrea pediatrica - Disenteria bacteriana")

note(disenteria,
    "💩 [B1] Interrogatorio (diarrea con sangre) — caracteriza evacuaciones: "
    "{{c1::n.º en 24 h, líquidas/sangre/moco/jalea de grosella, ¿sangre roja visible?}}, "
    "{{c2::tenesmo (puja y sale poco con moco/sangre)}}, "
    "{{c3::fiebre, vómito (¿retiene líquidos?), dolor cólico}}, "
    "{{c4::deshidratación: diuresis, lágrimas, boca seca, ojos hundidos}}, "
    "{{c5::contacto/comida sospechosa y antibiótico o antidiarreico previo}}.",
    "🗣️ ECOE: «Hago preguntas dirigidas y luego exploro para valorar hidratación y descartar gravedad.»", TA)

note(disenteria,
    "💩 [B2] Exploración — "
    "{{c1::estado general (¿tóxica?, alerta/letárgica) y signos vitales con peso}}, "
    "{{c2::hidratación: ojos, mucosa, lágrimas, pliegue, llenado capilar, pulsos, diuresis}}, "
    "{{c3::abdomen: distensión, ruidos, dolor, defensa/rebote/rigidez (descartar quirúrgico)}}, "
    "{{c4::revisar pañal/heces (sangre y moco)}}.",
    "Caso: 16 kg, irritable consolable NO tóxica, T 38.5, FC 118, llenado 2 s, ojos algo hundidos, "
    "mucosa seca, lágrimas disminuidas → deshidratación leve-moderada.", TA)

note(disenteria,
    "💩 [B3] Reconocimiento — Dx: "
    "{{c1::diarrea aguda inflamatoria/invasiva tipo disentería, probablemente bacteriana}}, con "
    "{{c2::deshidratación leve a moderada, SIN choque ni abdomen quirúrgico}}; lo sustento por "
    "{{c3::fiebre + sangre + moco + dolor cólico + tenesmo}}.",
    "🗣️ «NO es Plan C porque no está letárgica, sí bebe, pulsos presentes, llenado 2 s y TA conservada.»", TA)

note(disenteria,
    "💩 [B4] Diferenciales — 1) {{c1::Shigella u otra bacteria invasiva (fiebre, sangre, moco, tenesmo)}}, "
    "2) {{c2::Campylobacter/Salmonella (alimentos)}}, "
    "3) {{c3::E. coli enterohemorrágica — OJO: cuidado con antibiótico por riesgo de SHU}}, "
    "4) {{c4::GEA viral (menos probable: suele ser acuosa sin sangre)}}; "
    "descarto {{c5::invaginación (sin jalea de grosella/masa) y abdomen quirúrgico (sin defensa/rebote)}}.",
    "SHU = síndrome urémico hemolítico (típico de E. coli O157:H7).", TA)

note(disenteria,
    "💩 [B5] Estudios (en diarrea con sangre SÍ se piden) — "
    "{{c1::coprológico (leucocitos y eritrocitos fecales, moco, parásitos)}}, "
    "{{c2::coprocultivo con antibiograma (identifica germen y ajusta)}}, "
    "{{c3::BH (espero leucocitosis con neutrofilia) y PCR}}, "
    "{{c4::electrolitos/urea/creatinina si no tolera VO, orina poco o mal estado}}.",
    "Caso: leucos 15,800 / neutrófilos 82%, leucocitos y eritrocitos fecales abundantes → bacteriana. "
    "No esperar el coprocultivo para tratar si la clínica lo exige.", TA)

note(disenteria,
    "💩 [B6] Manejo (4 partes) — "
    "1) {{c1::Plan B: VSO 75 mL/kg en 4 h → 75×16 = 1200 mL en tomas pequeñas}}, "
    "2) {{c2::ciprofloxacino 15 mg/kg/dosis cada 12 h × 3 días → 240 mg = 5 mL de 250 mg/5 mL}}, "
    "3) {{c3::zinc 20 mg VO cada 24 h × 10–14 días}}, "
    "4) {{c4::NO loperamida/antidiarreicos, continuar alimentación, revalorar a las 4 h}}.",
    "Si vomita: esperar 5–10 min y reiniciar más lento. Reposición: 100–200 mL tras cada evacuación.", TA)

note(disenteria,
    "💩 [B7] Comunicación — "
    "{{c1::validar el susto de ver sangre}}, "
    "{{c2::explicar: una bacteria irrita el intestino → moco, sangre, fiebre y cólico}}, "
    "{{c3::tranquilizar: no hay choque ni abdomen quirúrgico}}, "
    "{{c4::antibiótico empírico + coprocultivo para confirmar y ajustar}}.", "", TA)

note(disenteria,
    "💩 [EC/alarma + seguimiento] Regresar a urgencias si: "
    "{{c1::somnolencia/no responde, no bebe, vomita todo, no orina, ojos muy hundidos, manos frías, "
    "llenado lento, sangre que aumenta, dolor intenso/abdomen duro, vómito verde, convulsiones}}. "
    "Vigilar SHU: {{c2::palidez, moretones, orina oscura o deja de orinar}}. "
    "Seguimiento: {{c3::revalorar a las 4 h y cita en 24–48 h; ajustar con coprocultivo}}.",
    "Error crítico: dar antidiarreico en diarrea con sangre (empeora); no buscar choque ni SHU.", TA)


# ==================== CASO B: GEA VIRAL, DESHIDRATACIÓN MODERADA ====================
TB = ["ecoe", "guion", "pediatria", "diarrea", "deshidratacion"]
deshidra = genanki.Deck(DECK_DESHIDRA, "Guiones ECOE::Diarrea pediatrica - Deshidratacion moderada (viral)")

note(deshidra,
    "💧 [B1] Interrogatorio — "
    "{{c1::n.º y características (aguadas/sangre/moco/negras), vómitos (¿retiene?), fiebre}}, "
    "{{c2::dolor abdominal (leve cólico vs intenso localizado) y distensión}}, "
    "{{c3::contacto/comida y tratamientos previos (antibiótico/antidiarreico)}}, "
    "{{c4::estado de alerta y convulsiones}}, "
    "{{c5::hidratación: ¿bebe normal/con sed/no puede?, pañales mojados, lágrimas, boca seca}}.",
    "🗣️ ECOE: «Pregunto y luego reviso para saber QUÉ GRADO de deshidratación tiene y elegir el manejo más seguro.»", TB)

note(deshidra,
    "💧 [B2] Exploración — "
    "{{c1::estado general (alerta / irritable consolable / letárgico) y signos vitales}}, "
    "{{c2::hidratación: ojos, mucosa/lengua, lágrimas, pliegue, llenado capilar, pulsos, pañales}}, "
    "{{c3::abdomen blando vs distendido / defensa / rebote}}, "
    "{{c4::revisar pañal (acuosa, sin sangre ni moco)}}.", "", TB)

note(deshidra,
    "💧 [B3] Reconocimiento — Dx: "
    "{{c1::gastroenteritis aguda probablemente viral con deshidratación MODERADA}}. Sustento: "
    "{{c2::diarrea acuosa, vómitos escasos, febrícula, contacto familiar, SIN sangre ni moco, abdomen blando}} + "
    "{{c3::ojos hundidos, mucosa seca, lágrimas disminuidas, sed ávida, pocos pañales}}.",
    "🗣️ «NO es grave (Plan C) porque está despierto, irritable pero consolable, sí bebe, pulsos presentes "
    "y llenado conservado → corresponde Plan B.»", TB)

note(deshidra,
    "💧 [B4] Diferenciales — 1) {{c1::GEA viral (acuosa, febrícula, contacto, sin sangre)}}, "
    "2) {{c2::GEA bacteriana/disentería (menos probable: sin sangre, moco ni fiebre alta)}}, "
    "3) {{c3::intoxicación alimentaria}}; "
    "descarto {{c4::abdomen agudo/invaginación (sin dolor episódico, vómito biliar, masa, jalea de grosella)}} "
    "y {{c5::sepsis (sin letargo, mala perfusión ni fiebre alta)}}.", "", TB)

note(deshidra,
    "💧 [B5] Estudios — "
    "{{c1::el dx y el grado de hidratación son CLÍNICOS; sin estudios de rutina si responde a Plan B}}. "
    "Lo clave: {{c2::peso (para calcular el suero), signos vitales seriados, revalorar a las 4 h}}. "
    "{{c3::glucosa capilar si somnoliento/convulsiones/mala ingesta}}; "
    "{{c4::electrolitos/urea/creatinina si grave o Plan C; coprocultivo solo si sangre/moco/fiebre alta/tóxico}}.", "", TB)

note(deshidra,
    "💧 [B6] Manejo — "
    "{{c1::Plan B: VSO 75 mL/kg en 4 h → 75×11 = 825 mL en tomas pequeñas}}; "
    "si mejora pasa a {{c2::Plan A: 50–100 mL tras cada evacuación (<2 años), continuar alimentación y lactancia}}; "
    "{{c3::zinc 20 mg VO cada 24 h × 10–14 días (>6 meses)}}; "
    "{{c4::NO antibiótico (sin sangre/moco/fiebre alta) ni antidiarreicos}}.",
    "Si vomita: esperar 5–10 min y reiniciar más lento. Revalorar a las 4 h.", TB)

note(deshidra,
    "💧 [B7] Comunicación — "
    "{{c1::tranquilizar: no hay choque ni abdomen grave y aún bebe}}, "
    "{{c2::lo importante NO es cortar la diarrea, sino evitar la deshidratación}}, "
    "{{c3::el suero repone agua y sales; el zinc acorta el episodio}}, "
    "{{c4::enseñar a preparar y dar el suero en casa}}.", "", TB)

note(deshidra,
    "💧 [EC/alarma] Regresar a urgencias si: "
    "{{c1::no bebe, vomita todo, muy dormido/no responde, no orina, sangre/moco en heces, fiebre alta, "
    "dolor intenso/abdomen distendido, vómito verde, convulsiones, ojos muy hundidos, manos frías, llenado lento}}. "
    "Si aparece {{c2::letargo, no puede beber, pulsos débiles o mala perfusión → ya NO es Plan B, es Plan C con líquidos IV}}.",
    "Error crítico: dar antidiarreicos (loperamida) a un niño; suspender la lactancia.", TB)


# ==================== BUILD ====================
os.makedirs(OUT, exist_ok=True)
out_path = os.path.join(OUT, "Guiones_ECOE_Diarrea_Pediatrica.apkg")
genanki.Package([disenteria, deshidra]).write_to_file(out_path)
print(f"OK -> {out_path}")
print(f"  Disentería:            {len(disenteria.notes)} notas (deck {DECK_DISENTERIA})")
print(f"  Deshidratación viral:  {len(deshidra.notes)} notas (deck {DECK_DESHIDRA})")
