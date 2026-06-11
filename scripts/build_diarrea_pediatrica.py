#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Guiones ECOE (versión mínima) — Diarrea pediátrica.
Caso A: disentería bacteriana (16 kg) → 4 tarjetas.
Caso B: GEA viral con deshidratación moderada (11 kg) → 3 tarjetas (solo los
        discriminadores frente a la disentería, para no repetir contenido).
Cálculos de dosis incluidos. Verbalización/umbrales en Extra.
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


# ==================== CASO A: DISENTERÍA (4 tarjetas) ====================
TA = ["ecoe", "guion", "pediatria", "diarrea", "disenteria"]
dis = genanki.Deck(DECK_DISENTERIA, "Guiones ECOE::Diarrea pediatrica - Disenteria bacteriana")

note(dis,
    "💩 [Interrogatorio + exploración] {{c1::evacuaciones (sangre/moco/jalea de grosella), tenesmo, fiebre, "
    "vómito, dolor cólico}}; hidratación {{c2::diuresis, lágrimas, ojos, mucosa}}. "
    "Exploración: {{c3::estado general + vitales con peso y grado de deshidratación}}, "
    "{{c4::abdomen (descartar defensa/rebote/quirúrgico)}}.",
    "Caso 16 kg: irritable consolable, T 38.5, llenado 2 s → deshidratación leve-moderada (no Plan C).", TA)

note(dis,
    "💩 [Dx + diferenciales] {{c1::disentería probablemente bacteriana (sangre+moco+fiebre+tenesmo) con "
    "deshidratación leve-moderada, sin choque ni abdomen quirúrgico}}. "
    "Ddx: {{c2::Shigella, Campylobacter/Salmonella}}; OJO {{c3::E. coli enterohemorrágica → cuidado con "
    "antibiótico por riesgo de SHU}}; descartar invaginación.",
    "SHU = síndrome urémico hemolítico (E. coli O157:H7).", TA)

note(dis,
    "💩 [Estudios + manejo] Estudios (SÍ en diarrea con sangre): {{c1::coprológico, coprocultivo con antibiograma, "
    "BH con leucocitosis/neutrofilia}}. Manejo: {{c2::Plan B VSO 75 mL/kg → 75×16 = 1200 mL en 4 h}}, "
    "{{c3::ciprofloxacino 15 mg/kg/dosis cada 12 h × 3 d → 240 mg = 5 mL de 250 mg/5 mL}}, "
    "{{c4::zinc 20 mg/día × 10–14 d, NO antidiarreicos}}.",
    "No esperar el coprocultivo para tratar si la clínica lo exige.", TA)

note(dis,
    "💩 [Comunicación + alarma] {{c1::explicar: bacteria que irrita el intestino; antibiótico empírico + "
    "coprocultivo para ajustar}}. Alarma → urgencias: {{c2::no bebe, vomita todo, no orina, sangre que aumenta, "
    "abdomen duro, vómito verde, convulsiones}}; vigilar SHU {{c3::palidez, moretones, orina oscura}}.",
    "Error crítico: antidiarreico en diarrea con sangre (empeora).", TA)


# ==================== CASO B: GEA VIRAL — solo discriminadores (3 tarjetas) ====================
TB = ["ecoe", "guion", "pediatria", "diarrea", "deshidratacion"]
des = genanki.Deck(DECK_DESHIDRA, "Guiones ECOE::Diarrea pediatrica - Deshidratacion moderada (viral)")

note(des,
    "💧 [Dx — contraste con disentería] {{c1::GEA viral: acuosa, SIN sangre ni moco, febrícula, contacto familiar}} "
    "con {{c2::deshidratación MODERADA (irritable consolable, sí bebe, pulsos presentes → Plan B, no Plan C)}}. "
    "Descartar {{c3::bacteriana/disentería, abdomen agudo, sepsis}}.",
    "🗣️ «Lo importante no es cortar la diarrea, sino evitar la deshidratación.»", TB)

note(des,
    "💧 [Estudios + manejo] {{c1::dx y grado son CLÍNICOS, sin estudios de rutina si responde a Plan B}}. "
    "Manejo: {{c2::Plan B VSO 75 mL/kg → 75×11 = 825 mL en 4 h}}, luego "
    "{{c3::Plan A: 50–100 mL tras cada evacuación (&lt;2 años), continuar alimentación/lactancia}}, "
    "{{c4::zinc 20 mg/día × 10–14 d, NO antibiótico ni antidiarreicos}}.",
    "Antibiótico SOLO si sangre/moco/fiebre alta/aspecto tóxico.", TB)

note(des,
    "💧 [Alarma + escalada a Plan C] Regresar si {{c1::no bebe, vomita todo, muy dormido, no orina, sangre/moco, "
    "convulsiones, ojos muy hundidos, manos frías}}. "
    "Si {{c2::letargo, no puede beber, pulsos débiles o mala perfusión → ya NO es Plan B, es Plan C con líquidos IV}}.",
    "Error crítico: antidiarreicos (loperamida) en un niño; suspender la lactancia.", TB)


# ==================== BUILD ====================
os.makedirs(OUT, exist_ok=True)
out_path = os.path.join(OUT, "Guiones_ECOE_Diarrea_Pediatrica.apkg")
genanki.Package([dis, des]).write_to_file(out_path)
print(f"OK -> {out_path}")
print(f"  Disentería:            {len(dis.notes)} notas (deck {DECK_DISENTERIA})")
print(f"  Deshidratación viral:  {len(des.notes)} notas (deck {DECK_DESHIDRA})")
