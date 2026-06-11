#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Guiones ECOE (versión mínima) — Lactancia y Asma, 4 tarjetas por caso.
Cada tarjeta combina varios bloques de rúbrica, sin repetir contenido.
Cifras: RCP AHA oct-2025 · Asma GINA 2025. Verbalización/umbrales en Extra.
"""
import os
import genanki

MODEL_ID = 1607392319  # cloze_estandar
DECK_LACTANCIA = 1990012001
DECK_ASMA = 1990012002
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


# ==================== LACTANCIA (4 tarjetas) ====================
TL = ["ecoe", "guion", "ginecoobstetricia", "lactancia"]
lac = genanki.Deck(DECK_LACTANCIA, "Guiones ECOE::Lactancia - Agarre y baja ingesta")

note(lac,
    "🍼 [Interrogatorio + exploración] Bebé: {{c1::pañales/evacuaciones, somnolencia/rechazo, ictericia, "
    "peso al nacer vs actual (% pérdida)}}. Madre: {{c2::dolor/grietas, congestión, pezón plano/invertido}}. "
    "Clave: {{c3::OBSERVAR una toma}} + {{c4::vitales e hidratación del bebé (mucosas, fontanela, llenado capilar)}}.",
    "Mal agarre = toma solo la punta del pezón, labios no evertidos, chasquidos, duele.", TL)

note(lac,
    "🍼 [Dx + diferenciales] {{c1::problema de lactancia por agarre superficial con transferencia inefectiva}} + "
    "{{c2::deshidratación leve e ictericia indirecta por baja ingesta (bebé estable, NO sano)}}. "
    "Ddx: {{c3::frenillo lingual/paladar hendido, pezón invertido/mastitis, infección neonatal (siempre descartar)}}.",
    "🗣️ Frase clave: «Está estable PERO con baja ingesta que requiere intervención HOY.»", TL)

note(lac,
    "🍼 [Estudios + manejo] Dirigidos: {{c1::peso/% de pérdida, bilirrubina por horas de vida, "
    "electrolitos/BUN si deshidratación}}. Manejo: "
    "{{c2::corregir agarre (boca abierta, mentón pega, areola en boca, labios evertidos)}}, "
    "{{c3::asegurar alimentación HOY con leche materna extraída}}, "
    "{{c4::valoración pediátrica el mismo día + seguimiento en 24 h}}.",
    "Pérdida ponderal anormal &gt;7–10%. La mastitis NO obliga a destetar.", TL)

note(lac,
    "🍼 [Comunicación + alarma] {{c1::validar/normalizar, explicar simple, prioridad: que coma hoy y lactar sin dolor}}. "
    "Datos de alarma → urgencias: {{c2::no moja pañales, fontanela hundida, ictericia que llega a piernas/palmas, "
    "cianosis, vómito verde, rechazo total, fiebre o hipotermia}}.",
    "Error crítico: dejarla con un «siga intentando» habiendo ya baja ingesta.", TL)


# ==================== ASMA (4 tarjetas) ====================
TA = ["ecoe", "guion", "urgencias", "asma", "gina2025"]
asm = genanki.Deck(DECK_ASMA, "Guiones ECOE::Asma - Exacerbacion moderada (adulto)")

note(asm,
    "🫁 [Interrogatorio + exploración] PRIMERO gravedad: {{c1::¿habla en frases?, cianosis, confusión, "
    "cuántas veces usó salbutamol}}. Luego {{c2::desencadenante, antecedente de asma/hospitalización, uso del controlador}}. "
    "Exploración: {{c3::SpO₂, espiración prolongada, sibilancias difusas, tiraje}} y descartar {{c4::tórax silencioso}}.",
    "Caso moderada: FC 108, FR 26, SpO₂ 93%, PEF 62%.", TA)

note(asm,
    "🫁 [Dx + diferenciales] {{c1::exacerbación asmática moderada}} (habla en frases, SpO₂ 90–95%, PEF &gt;50%; "
    "NO severa = sin cianosis, tórax silencioso ni confusión). "
    "Ddx: {{c2::neumonía (sin fiebre/estertores focales), neumotórax, TEP, SCA}}.",
    "🗣️ «No espero estudios; clasifico gravedad, broncodilatador, O₂, corticoide si moderada, revaloro en 1 h.»", TA)

note(asm,
    "🫁 [Estudios + manejo] Estudios: {{c1::NO retrasar el tx; oximetría y PEF; espirometría al estabilizar "
    "(reversibilidad ↑FEV1 ≥12% y ≥200 mL)}}. Manejo: "
    "{{c2::salbutamol con aerocámara 4–10 disparos cada 20 min × 3}}, "
    "{{c3::O₂ para SpO₂ 93–95% + prednisona 40–50 mg × 5 días}}, "
    "{{c4::revalorar en 1 h; controlador budesonida/formoterol}}.",
    "GINA 2025: nunca SABA solo. Egreso si SpO₂ &gt;94% y PEF &gt;60–80%.", TA)

note(asm,
    "🫁 [Comunicación + alarma] {{c1::tranquilizar, explicar bronquios inflamados; tratar la crisis Y prevenir recaída; "
    "revisar técnica inhalatoria}}. Alarma → urgencias: {{c2::disnea que empeora, no habla en frases, labios morados, "
    "somnolencia, SpO₂ &lt;90–92%, necesita inhalador cada &lt;3–4 h, tórax silencioso}}.",
    "Error crítico: dar SABA solo sin corticoide; usar betabloqueador.", TA)


# ==================== BUILD ====================
os.makedirs(OUT, exist_ok=True)
out_path = os.path.join(OUT, "Guiones_ECOE_Lactancia_Asma.apkg")
genanki.Package([lac, asm]).write_to_file(out_path)
print(f"OK -> {out_path}")
print(f"  Lactancia: {len(lac.notes)} notas (deck {DECK_LACTANCIA})")
print(f"  Asma:      {len(asm.notes)} notas (deck {DECK_ASMA})")
