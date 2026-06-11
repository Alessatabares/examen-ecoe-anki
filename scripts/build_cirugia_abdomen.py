#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Guiones ECOE (mínimos) — Cirugía / abdomen agudo, 4 tarjetas por caso.
A: Apendicitis que se PERFORA a mitad de consulta (24 a) — incluye el giro clínico.
B: Colecistitis aguda calculosa (42 a) que requiere cirugía.
Cálculos/umbrales y frases de oro en Extra.
"""
import os
import genanki

MODEL_ID = 1607392319  # cloze_estandar
DECK_APENDI = 1990012012
DECK_COLECI = 1990012013
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


# ==================== A: APENDICITIS QUE SE PERFORA ====================
TA = ["ecoe", "guion", "cirugia", "apendicitis"]
ap = genanki.Deck(DECK_APENDI, "Guiones ECOE::Apendicitis (perforacion en consulta)")

note(ap,
    "🔪 [Interrogatorio + exploración] {{c1::dolor periumbilical que MIGRA a fosa iliaca derecha, anorexia, "
    "náusea, fiebre, empeora al caminar/toser}}; en mujer fértil descartar {{c2::embarazo (FUM, β-hCG) y causas "
    "ginecológicas}}. Exploración: vitales + abdomen {{c3::McBurney, Rovsing, psoas, obturador, defensa/rebote/rigidez}}.",
    "Caso: 24 a, 18 h, migración periumbilical→FID, McBurney y Rovsing +, T 38.1.", TA)

note(ap,
    "🔪 [Dx + diferenciales] Inicial: {{c1::apendicitis aguda (migración, anorexia, fiebre, McBurney +) → "
    "valoración quirúrgica urgente}}. Ddx en mujer fértil: {{c2::embarazo ectópico (β-hCG), torsión ovárica, "
    "EPI, ITU/cólico renal, gastroenteritis}}.",
    "Score de Alvarado. β-hCG SIEMPRE antes de operar.", TA)

note(ap,
    "🔪 [GIRO → perforación a mitad de consulta] Cambio: {{c1::dolor localizado → GENERALIZADO, defensa "
    "involuntaria, rebote, rigidez (abdomen en tabla), ruidos disminuidos}} + deterioro "
    "{{c2::hipotensión, taquicardia, fiebre alta}}. Integro {{c3::apendicitis complicada perforada con "
    "peritonitis generalizada → urgencia quirúrgica, paso a ABCDE}}.",
    "🗣️ Frase de oro: «dolor localizado→generalizado + abdomen rígido + rebote + deterioro = perforada hasta "
    "demostrar lo contrario: ABCDE, antibiótico IV y cirugía.»", TA)

note(ap,
    "🔪 [Manejo urgente + errores críticos] {{c1::ayuno, 2 vías IV, cristaloide (bolo 20 mL/kg si hipoperfusión), "
    "analgesia IV (NO negarla), antiemético}}, {{c2::antibiótico IV amplio: ceftriaxona + metronidazol "
    "(o piperacilina/tazobactam si sepsis)}}, {{c3::avisar a cirugía YA para control del foco}}. "
    "NO: {{c4::mandar a casa, dar laxante/antidiarreico, dar nada por VO, retrasar antibiótico/cirugía por "
    "estudios, olvidar la β-hCG}}.", "", TA)


# ==================== B: COLECISTITIS AGUDA ====================
TC = ["ecoe", "guion", "cirugia", "colecistitis"]
co = genanki.Deck(DECK_COLECI, "Guiones ECOE::Colecistitis aguda")

note(co,
    "🟢 [Interrogatorio + exploración] {{c1::dolor en hipocondrio derecho persistente &gt;6 h, irradiado a "
    "hombro/espalda, tras comida grasa, con cólicos previos que cedían}}; descartar {{c2::ictericia, coluria, "
    "acolia (vía biliar) y dolor en cinturón (pancreatitis)}}. Exploración: vitales + "
    "{{c3::signo de Murphy (pausa inspiratoria dolorosa); descartar defensa/rebote/peritonitis}}.",
    "Caso: 42 a, 18 h, irradia a hombro, tras tacos grasosos, T 38.4, Murphy +.", TC)

note(co,
    "🟢 [Dx + diferenciales] {{c1::colecistitis aguda calculosa (dolor persistente &gt;6 h + fiebre + Murphy +, "
    "ya NO es cólico biliar que cede)}}. Ddx: {{c2::cólico biliar, coledocolitiasis (ictericia/coluria/BD↑), "
    "colangitis (+ictericia+hipotensión+confusión = tríada de Charcot), pancreatitis (lipasa↑)}}.",
    "🗣️ Frase de oro: «cólico biliar dura horas y cede; colecistitis = dolor persistente &gt;6 h con "
    "fiebre/leucocitosis y Murphy +.»", TC)

note(co,
    "🟢 [Estudios + interpretación] {{c1::BH (leucocitosis/neutrofilia), perfil hepático (BT/BD, AST/ALT, FA, GGT) "
    "para diferenciar de obstrucción/colangitis, lipasa (descartar pancreatitis), β-hCG}}. "
    "Imagen inicial: {{c2::USG hepatobiliar = litos, pared engrosada &gt;4–5 mm, líquido perivesicular, "
    "Murphy sonográfico, ¿colédoco dilatado?}}.",
    "Caso: leucos 15,900/N 84%, BD normal, lipasa normal, colédoco no dilatado → colecistitis sin colangitis "
    "ni pancreatitis.", TC)

note(co,
    "🟢 [Manejo + errores críticos] {{c1::ayuno, líquidos IV, analgesia IV, antiemético}}, "
    "{{c2::antibiótico IV: ceftriaxona 1–2 g/día + metronidazol (o ampicilina/sulbactam; pip/tazo si sepsis)}}, "
    "{{c3::colecistectomía laparoscópica TEMPRANA en el mismo ingreso}}; si inestable/no candidata → "
    "{{c4::estabilizar + drenaje percutáneo (colecistostomía)}}. "
    "NO: mandar a casa con analgésico, llamarlo «gastritis», olvidar perfil hepático/lipasa/USG, retrasar cirugía.",
    "", TC)


# ==================== BUILD ====================
os.makedirs(OUT, exist_ok=True)
out_path = os.path.join(OUT, "Guiones_ECOE_Cirugia_Abdomen.apkg")
genanki.Package([ap, co]).write_to_file(out_path)
print(f"OK -> {out_path}")
print(f"  Apendicitis (perforación): {len(ap.notes)} notas (deck {DECK_APENDI})")
print(f"  Colecistitis aguda:        {len(co.notes)} notas (deck {DECK_COLECI})")
