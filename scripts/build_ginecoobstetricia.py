#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Guiones ECOE (mínimos) — Gineco-Obstetricia, 4 tarjetas por caso.
A: Control prenatal inicial (8 sem por FUM) — cálculo EG/FPP, labs, suplementos.
B: Consejería anticonceptiva (migraña con aura → sin estrógeno).
C: Especuloscopia + Papanicolaou (sangrado postcoital, Pap atrasado).
Estaciones de consejería/procedimiento: exploración = técnica, plan = consejería.
"""
import os
import genanki

MODEL_ID = 1607392319  # cloze_estandar
DECK_PRENATAL = 1990012008
DECK_ANTICONC = 1990012009
DECK_PAP = 1990012010
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


# ==================== A: CONTROL PRENATAL INICIAL ====================
TP = ["ecoe", "guion", "obstetricia", "control-prenatal"]
pre = genanki.Deck(DECK_PRENATAL, "Guiones ECOE::Control prenatal inicial")

note(pre,
    "🤰 [Interrogatorio + cálculo EG/FPP] Confirma {{c1::FUM, regularidad de ciclos, seguridad de la fecha, "
    "datos de alarma (sangrado, dolor unilateral, síncope)}}; además G-P-A-C, comorbilidades, fármacos, tóxicos, "
    "vacunas, alimentación, red de apoyo. EG por FUM: {{c2::días desde la FUM ÷ 7 (ej.: 56 días = 8 semanas)}}. "
    "FPP (Naegele): {{c3::FUM + 7 días − 3 meses + 1 año}}.",
    "Caso: FUM 15-abr-2026, hoy 10-jun → 8 sem. FPP = 22-ene-2027. "
    "Confirmar con USG de 1er trimestre (localización, vitalidad, EG).", TP)

note(pre,
    "🤰 [Exploración + dx] {{c1::signos vitales (TA basal = clave), peso/talla → IMC, palidez/tiroides/edema}}; "
    "a las 8 sem {{c2::el útero aún no rebasa la pelvis (no se mide fondo uterino)}}. "
    "Dx: {{c3::embarazo de ~8 sem por FUM, primigesta, sin datos de alarma, aparentemente bajo riesgo}}; "
    "descartar {{c4::ectópico, amenaza de aborto, ITU asintomática, anemia}}.",
    "El IMC orienta la ganancia de peso saludable del embarazo.", TP)

note(pre,
    "🤰 [Estudios iniciales + suplementos] Labs: {{c1::BH, grupo y Rh (+Coombs si Rh−), EGO/urocultivo, glucosa, "
    "VIH, VDRL/sífilis, HBsAg}} + {{c2::USG de 1er trimestre}}. Suplementos: "
    "{{c3::ácido fólico 0.4 mg/día (4–5 mg si antecedente de DTN, DM o anticonvulsivos)}}, "
    "{{c4::hierro elemental 30–60 mg/día; calcio 1–1.5 g si ingesta baja o riesgo de preeclampsia}}.",
    "Hierro separado de leche/café/té. NO vitamina A en dosis altas (teratógena).", TP)

note(pre,
    "🤰 [Vacunas + alarma + seguimiento] Vacunas: {{c1::influenza en cualquier trimestre; Tdap 27–36 sem; "
    "NO vacunas vivas (SRP/varicela)}}. Seguimiento: {{c2::cita en 4 sem; tamiz de diabetes gestacional 24–28 sem}}. "
    "Alarma → urgencias: {{c3::sangrado, dolor abdominal/unilateral, síncope, salida de líquido, "
    "cefalea intensa/visión borrosa/epigastralgia, hinchazón súbita, fiebre, vómito incoercible}}.",
    "Cefalea + fosfenos + epigastralgia más adelante = sospecha de preeclampsia.", TP)


# ==================== B: CONSEJERÍA ANTICONCEPTIVA ====================
TC = ["ecoe", "guion", "ginecologia", "anticoncepcion"]
ant = genanki.Deck(DECK_ANTICONC, "Guiones ECOE::Consejeria anticonceptiva")

note(ant,
    "💊 [Interrogatorio + razonamiento] 3 cosas ANTES de elegir método: "
    "{{c1::descartar embarazo (FUM, relaciones, ¿falla de condón?)}}, "
    "{{c2::buscar contraindicaciones a estrógeno (migraña con aura, fumadora >35, HTA, TEV, cáncer de mama, "
    "hepatopatía, lactancia <6 sem)}}, "
    "{{c3::valorar riesgo de ITS y la preferencia (diario / larga duración / reversible)}}.",
    "Caso: 26 años, migraña CON AURA → es la contraindicación clave.", TC)

note(ant,
    "💊 [Decisión clínica] Migraña con aura = {{c1::evitar combinados (pastilla combinada, parche, anillo) "
    "por riesgo vascular}}. Ofrecer SIN estrógeno: {{c2::implante, DIU de cobre, DIU hormonal, inyección o "
    "pastilla solo de progestina}}. Siempre {{c3::condón para ITS (ningún hormonal ni DIU protege contra ITS)}}.",
    "🗣️ «No toda paciente que pide pastillas debe recibir combinadas; primero descarto embarazo, ITS y "
    "contraindicación a estrógeno.»", TC)

note(ant,
    "💊 [Estudios + opciones] Estudios: {{c1::NO se necesitan labs/hormonas/USG de rutina; solo prueba de embarazo "
    "si hay duda; exploración pélvica solo si se elige DIU}}. Opciones por eficacia/seguridad aquí: "
    "{{c2::implante o DIU (larga duración, muy eficaces, sin estrógeno) = recomendación principal}}; alternativa "
    "{{c3::pastilla solo de progestina (desogestrel 75 µg/día, misma hora, sin descansos)}}.",
    "CDC 2024: remover barreras innecesarias, no retrasar el método sin causa. "
    "DIU de cobre = también anticoncepción de emergencia si se coloca &lt;5 días.", TC)

note(ant,
    "💊 [Inicio/respaldo + alarma + seguimiento] Respaldo con condón: "
    "{{c1::progestina si inicia después del día 5 (2 días); implante/DIU si fuera de los primeros días (7 días)}}. "
    "Alarma: {{c2::cefalea súbita, déficit neurológico, dolor torácico/disnea, pierna hinchada (TEV), "
    "pérdida de visión; con DIU: no palpa hilos, dolor o fiebre}}. "
    "Seguimiento: {{c3::pastilla 1–3 meses; implante/DIU 4–6 semanas}}.", "", TC)


# ==================== C: ESPECULOSCOPIA + PAPANICOLAOU ====================
TS = ["ecoe", "guion", "ginecologia", "especuloscopia", "papanicolaou"]
pap = genanki.Deck(DECK_PAP, "Guiones ECOE::Especuloscopia y Papanicolaou")

note(pap,
    "🔬 [Apertura + interrogatorio] SIEMPRE primero: "
    "{{c1::consentimiento, confidencialidad, acompañante/chaperón, «si duele, paramos»}}. "
    "Interrogatorio: {{c2::sangrado postcoital vs intermenstrual, FUM, ¿posible embarazo?, flujo/dolor/fiebre}}, "
    "{{c3::último Pap y si fue anormal, VPH/displasia, inicio de vida sexual, parejas/condón, ITS, tabaco, "
    "inmunosupresión, vacuna VPH}}.",
    "Caso: Laura 32 a, sangrado postcoital, último Pap hace 6 años.", TS)

note(pap,
    "🔬 [Técnica de especuloscopia] {{c1::vaciar vejiga, posición ginecológica, cubrir; inspeccionar genitales externos}}. "
    "Espéculo {{c2::lubricado con agua, introducir cerrado y oblicuo, rotar y abrir lento; «sentirá presión, no dolor»}}. "
    "Visualizar {{c3::paredes vaginales, flujo, y cérvix: color, ectropión, pólipos, friabilidad, sangrado al contacto, "
    "secreción mucopurulenta, lesión exofítica}}.",
    "Toma de Pap: espátula en ectocérvix (giro 360°) + cepillo endocervical; rotular; retirar el espéculo observando.", TS)

note(pap,
    "🔬 [Dx + diferenciales + REGLA DE ORO] Sangrado postcoital + Pap atrasado, sin lesión macroscópica sospechosa. "
    "Ddx: {{c1::ectropión cervical, cervicitis por ITS, pólipo cervical}}; "
    "descartar {{c2::lesión intraepitelial / cáncer cervicouterino}}. "
    "REGLA DE ORO: {{c3::si veo lesión sospechosa (friable, irregular, sangrante, exofítica) NO me quedo con el Pap "
    "→ refiero a colposcopia + biopsia}}.",
    "🗣️ Frase de oro: «Si veo lesión sospechosa, no me tranquilizo con el Pap: refiero a colposcopia/biopsia.»", TS)

note(pap,
    "🔬 [Plan + alarma + seguimiento] {{c1::tomar Pap (atrasado) ± prueba de VPH; pruebas Chlamydia/Gonorrhea si "
    "riesgo/cervicitis; prueba de embarazo si duda; NO antibiótico empírico sin secreción/fiebre/EPI}}. "
    "Si Pap alterado (ASC-US persistente, LSIL, HSIL, AGC) o lesión → {{c2::colposcopia}}. "
    "Alarma: {{c3::sangrado abundante, dolor pélvico intenso, fiebre, flujo fétido, sangrado posmenopáusico}}. "
    "Seguimiento: {{c4::2–4 semanas o al llegar el resultado}}.", "", TS)


# ==================== BUILD ====================
os.makedirs(OUT, exist_ok=True)
out_path = os.path.join(OUT, "Guiones_ECOE_GinecoObstetricia.apkg")
genanki.Package([pre, ant, pap]).write_to_file(out_path)
print(f"OK -> {out_path}")
print(f"  Control prenatal:  {len(pre.notes)} notas (deck {DECK_PRENATAL})")
print(f"  Anticoncepción:    {len(ant.notes)} notas (deck {DECK_ANTICONC})")
print(f"  Especulo + Pap:    {len(pap.notes)} notas (deck {DECK_PAP})")
