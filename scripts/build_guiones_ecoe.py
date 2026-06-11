#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Guiones ECOE — decks cortos por ESCENARIO, una tarjeta por componente de la rúbrica.
Casos: (1) Lactancia materna con mal agarre y baja ingesta · (2) Asma exacerbación moderada (adulto).
Cifras verificadas: RCP/BLS AHA oct-2025 · Asma GINA 2025 (prednisona 40-50 mg, nunca SABA solo).
Verbalización ECOE va SIEMPRE en el campo Extra con prefijo 🗣️ (CLAUDE.md).
"""
import os
import genanki

MODEL_ID = 1607392319  # cloze_estandar (reusable, no cambiar)
DECK_LACTANCIA = 1990012001
DECK_ASMA = 1990012002
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


def note(text, extra="", tags=None):
    return genanki.Note(model=model, fields=[text.strip(), extra.strip()], tags=tags or [])


# ============================ CASO 1: LACTANCIA ============================
TAGS_L = ["ecoe", "guion", "ginecoobstetricia", "lactancia"]
lactancia = genanki.Deck(DECK_LACTANCIA, "Guiones ECOE::Lactancia - Agarre y baja ingesta")

lactancia.add_note(note(
    "🍼 [B1] Obtención de información — pregunta del <b>bebé</b> "
    "{{c1::pañales mojados y evacuaciones al día}}, "
    "{{c2::somnolencia/rechazo, ictericia, fiebre, vómito verde y dificultad respiratoria}}, "
    "{{c3::peso al nacer vs actual y si fue término o prematuro}}; y de la <b>madre</b> "
    "{{c4::dolor, grietas, congestión, pezón plano/invertido y si le explicaron técnica}}.",
    "🗣️ ECOE: «Primero quiero descartar deshidratación e ictericia importante, y después observar la técnica, "
    "porque el dolor y las grietas suelen indicar que el agarre está superficial.»",
    TAGS_L,
))
lactancia.add_note(note(
    "🍼 [B2] Exploración (en orden) — "
    "{{c1::estado general y signos vitales del bebé}}, "
    "{{c2::peso actual y % de pérdida ponderal}}, "
    "{{c3::hidratación (mucosas, fontanela, llenado capilar, pañales) e ictericia}}, "
    "{{c4::boca: frenillo lingual, paladar, succión}}; en la madre "
    "{{c5::pezón/mama (grietas, congestión, pezón invertido, mastitis)}} y "
    "{{c6::OBSERVAR una toma}}.",
    "🗣️ ECOE: «Veo que toma solo la punta del pezón, los labios no están evertidos y se escuchan chasquidos: "
    "eso explica el dolor y que saque poca leche.»",
    TAGS_L,
))
lactancia.add_note(note(
    "🍼 [B3] Reconocimiento — diagnóstico: "
    "{{c1::problema de lactancia por agarre superficial con transferencia inefectiva}}, que explica "
    "{{c2::el dolor y las grietas maternas + la baja ingesta del bebé}}. El bebé está "
    "{{c3::estable pero con baja ingesta y deshidratación leve (pérdida ~8%, Na y BUN elevados)}} y "
    "{{c4::ictericia indirecta probablemente por baja ingesta}}.",
    "🗣️ ECOE (frase que da el punto): «No diría que el bebé está sano; está ESTABLE, pero con datos de "
    "baja ingesta que requieren intervención HOY.»",
    TAGS_L,
))
lactancia.add_note(note(
    "🍼 [B4] Diferenciales jerarquizados — 1) {{c1::mal agarre/técnica inadecuada}}, "
    "2) {{c2::baja ingesta con deshidratación leve}}, "
    "3) {{c3::ictericia por lactancia insuficiente o fisiológica}}, "
    "4) {{c4::problema anatómico del bebé (frenillo, paladar, succión débil)}}, "
    "5) {{c5::problema materno de mama/pezón (plano/invertido, ingurgitación, mastitis)}}, "
    "6) {{c6::infección neonatal u otra enfermedad — siempre descartarla}}.",
    "",
    TAGS_L,
))
lactancia.add_note(note(
    "🍼 [B5] Estudios dirigidos (no de rutina) — "
    "{{c1::peso y % de pérdida ponderal}}, "
    "{{c2::bilirrubina total/directa/indirecta interpretada con curva por horas de vida}}, "
    "{{c3::glucosa capilar si somnolencia o mala ingesta}}, "
    "{{c4::electrolitos, BUN/urea y creatinina si hay deshidratación}}; "
    "si fiebre/letargo/mala perfusión → {{c5::estudio de sepsis y referir a urgencias}}.",
    "Umbrales: pérdida ponderal anormal &gt;7–10% · Na &gt;145 apoya deshidratación · "
    "la fototerapia se decide por bilirrubina SEGÚN horas de vida y factores de riesgo.",
    TAGS_L,
))
lactancia.add_note(note(
    "🍼 [B6] Plan — "
    "{{c1::corregir técnica de agarre: boca bien abierta, mentón pega al pecho, areola en la boca, labios evertidos}}, "
    "{{c2::asegurar alimentación HOY con leche materna extraída (vasito/cucharita/jeringa)}}, "
    "{{c3::tratar grietas (corregir agarre + unas gotas de leche al aire)}}, "
    "{{c4::valoración pediátrica el mismo día}} y "
    "{{c5::seguimiento en 24 h: peso, pañales, hidratación, ictericia}}.",
    "Pezón plano/invertido: estimular o extraer unas gotas antes de la toma, posición de balón; "
    "pezonera temporal con apoyo si no logra prenderse. El bebé agarra AREOLA, no solo pezón.",
    TAGS_L,
))
lactancia.add_note(note(
    "🍼 [B7] Comunicación — "
    "{{c1::validar la angustia y normalizar (no está fallando, le pasa a muchas mamás)}}, "
    "{{c2::explicar en palabras simples que el agarre superficial causa dolor y poca leche}}, "
    "{{c3::dejar clara la prioridad: que el bebé coma hoy y poder lactar sin dolor}}, "
    "{{c4::ofrecer repetir y resolver dudas}}.",
    "",
    TAGS_L,
))
lactancia.add_note(note(
    "🍼 [EC] Errores críticos / alarma — NO cometas: "
    "{{c1::dejarla con un «siga intentando» habiendo ya baja ingesta}}, "
    "{{c2::recomendar destete por mastitis (es falso, se sigue amamantando)}}, "
    "{{c3::no valorar deshidratación/ictericia ni referir a pediatría el mismo día}}. "
    "Datos de alarma → urgencias: {{c4::fiebre/hipotermia, no moja pañales, fontanela hundida, "
    "ictericia que llega a piernas o palmas/plantas, cianosis, vómito verde, rechazo total, convulsiones}}.",
    "",
    TAGS_L,
))

# ============================ CASO 2: ASMA ============================
TAGS_A = ["ecoe", "guion", "urgencias", "neumologia", "asma", "gina2025"]
asma = genanki.Deck(DECK_ASMA, "Guiones ECOE::Asma - Exacerbacion moderada (adulto)")

asma.add_note(note(
    "🫁 [B1] Obtención de información — PRIMERO gravedad: "
    "{{c1::¿habla frases completas?, cianosis, confusión/somnolencia, cuántas veces usó salbutamol y si ayudó}}; "
    "luego {{c2::inicio, tos/fiebre, desencadenantes (polvo, frío, animales, infección)}}, "
    "{{c3::antecedente de asma, hospitalización/intubación previa y uso del controlador}}, "
    "y descartar {{c4::IAM, TEP, neumotórax y anafilaxia}}.",
    "🗣️ ECOE: «Sospecho crisis asmática, pero la reviso para clasificar la gravedad y descartar neumonía, "
    "neumotórax, tromboembolia, anafilaxia o problema cardiaco.»",
    TAGS_A,
))
asma.add_note(note(
    "🫁 [B2] Exploración — "
    "{{c1::estado general: ¿habla en frases?, alerta, cianosis, diaforesis}} + "
    "{{c2::signos vitales con SpO₂}}; tórax: "
    "{{c3::tiraje/músculos accesorios, espiración prolongada, sibilancias espiratorias difusas bilaterales}}; "
    "y descartar {{c4::tórax silencioso, matidez o hipersonoridad focal, y TVP en piernas}}.",
    "Caso típico moderada: FC 108, FR 26, SpO₂ 93%, sibilancias difusas, PEF 62%. "
    "Pide PEF si está disponible SIN retrasar el tratamiento.",
    TAGS_A,
))
asma.add_note(note(
    "🫁 [B3] Reconocimiento — {{c1::exacerbación asmática moderada}}. "
    "Es MODERADA porque {{c2::habla en frases, está alerta, SpO₂ 90–95%, PEF &gt;50% y sibilancias difusas}}; "
    "NO es severa/amenaza vital porque {{c3::no habla solo en palabras, SpO₂ no &lt;90%, sin cianosis, "
    "sin tórax silencioso, sin confusión ni agotamiento}}.",
    "",
    TAGS_A,
))
asma.add_note(note(
    "🫁 [B4] Diferenciales — 1) {{c1::exacerbación asmática (antecedente, desencadenante, sibilancias, mejora con salbutamol)}}, "
    "2) {{c2::neumonía (descartada: sin fiebre ni estertores focales)}}, "
    "3) {{c3::neumotórax (sin dolor súbito unilateral ni hipersonoridad)}}, "
    "4) {{c4::TEP (sin dolor pleurítico, hemoptisis ni edema unilateral)}}, "
    "5) {{c5::SCA (sin dolor irradiado ni diaforesis; si fuera típico → ECG y troponinas)}}.",
    "",
    TAGS_A,
))
asma.add_note(note(
    "🫁 [B5] Estudios — {{c1::NO retrasar el tratamiento esperando estudios}}. "
    "Útiles ahora: {{c2::oximetría y PEF antes/después del broncodilatador}}. "
    "Al estabilizar: {{c3::espirometría con reversibilidad = ↑FEV1 ≥12% y ≥200 mL post-broncodilatador}}. "
    "Solo si atípico: {{c4::Rx (neumonía/neumotórax), gasometría (grave/tórax silencioso), ECG/troponinas (dolor isquémico)}}.",
    "",
    TAGS_A,
))
asma.add_note(note(
    "🫁 [B6] Plan — "
    "{{c1::salbutamol con aerocámara 4–10 disparos cada 20 min × 3 ciclos}}, "
    "{{c2::oxígeno para SpO₂ 93–95%}}, "
    "{{c3::prednisona 40–50 mg VO cada 24 h × 5 días}}, "
    "{{c4::revalorar en 1 hora}}; egreso si {{c5::SpO₂ &gt;94%, mejora la disnea y PEF &gt;60–80%}}, "
    "con {{c6::controlador budesonida/formoterol, técnica inhalatoria y cita en 2–7 días}}.",
    "GINA 2025: NUNCA SABA solo como mantenimiento; alta con plan de acción escrito. "
    "Enjuagar boca tras el inhalador con esteroide.",
    TAGS_A,
))
asma.add_note(note(
    "🫁 [B7] Comunicación — "
    "{{c1::tranquilizar: no hay amenaza vital y ya está respondiendo}}, "
    "{{c2::explicar que los bronquios se inflaman y contraen; el salbutamol los abre, pero el controlador baja la inflamación}}, "
    "{{c3::tratar la crisis de hoy Y dejar plan para prevenir recaídas}}, "
    "{{c4::pedir que muestre su técnica inhalatoria y resolver dudas}}.",
    "",
    TAGS_A,
))
asma.add_note(note(
    "🫁 [EC] Errores críticos / alarma — NO: "
    "{{c1::dar SABA solo sin corticoide sistémico en crisis moderada}}, "
    "{{c2::subestimar la gravedad}}, "
    "{{c3::indicar un betabloqueador}}. "
    "Datos de alarma → urgencias: {{c4::disnea que empeora, no habla en frases, labios morados, "
    "somnolencia/confusión, SpO₂ &lt;90–92%, necesita el inhalador cada &lt;3–4 h, "
    "o el tórax que «ya no silba pero tampoco entra aire» (tórax silencioso)}}.",
    "",
    TAGS_A,
))

# ============================ BUILD ============================
os.makedirs(OUT, exist_ok=True)
pkg = genanki.Package([lactancia, asma])
out_path = os.path.join(OUT, "Guiones_ECOE_Lactancia_Asma.apkg")
pkg.write_to_file(out_path)
print(f"OK -> {out_path}")
print(f"  Lactancia: {len(lactancia.notes)} notas (deck {DECK_LACTANCIA})")
print(f"  Asma:      {len(asma.notes)} notas (deck {DECK_ASMA})")
