#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ECOE/ACLS — Causas reversibles de paro (5H/5T): interrogatorio → ABCDE → manejo inicial.
1 tarjeta-marco (barrido ABCDE + verbalización) + 1 por causa (10). Cifras ACLS/AHA estables.
Cada cause-card: pregunta que orienta {{c1}} · dónde en ABCDE {{c2}} · manejo inicial {{c3}}.
"""
import os
import genanki

MODEL_ID = 1607392319  # cloze_estandar
DECK_ID = 1990012015
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
TAGS = ["ecoe", "acls", "rcp", "causas-reversibles", "5h5t"]
deck = genanki.Deck(DECK_ID, "Guiones ECOE::Causas reversibles de paro (5H 5T)")


def note(text, extra=""):
    deck.add_note(genanki.Note(model=model, fields=[text.strip(), extra.strip()], tags=TAGS))


# ---------- Tarjeta marco: barrido ABCDE + verbalización ----------
note(
    "🔁 [Marco — barrido ABCDE para causas reversibles] Mientras siguen compresiones + DEA, busco 5H/5T: "
    "en A {{c1::obstrucción, vómito, cuerpo extraño, edema (anafilaxia)}}; "
    "B {{c2::hipoxia, neumotórax a tensión, TEP}}; "
    "C {{c3::hemorragia/hipovolemia, IAM, taponamiento, arritmia por potasio}}; "
    "D {{c4::toxinas, hipoglucemia, acidosis, potasio}}; "
    "E {{c5::hipotermia, trauma, embarazo, tóxicos/parches}}.",
    "5H: Hipoxia, Hipovolemia, Hidrogeniones (acidosis), Hipo/hiperK, Hipotermia. "
    "5T: neumotórax a Tensión, Taponamiento, Tóxicos, Trombosis pulmonar (TEP), Trombosis coronaria (IAM). "
    "🗣️ Pregunto al testigo qué pasó ANTES de caer: dolor torácico, disnea, atragantamiento, trauma, sangrado, "
    "fármacos/drogas, diálisis, diabetes, infección, cirugía reciente, inmovilización, frío/tóxicos.",
)

# ---------- 5H ----------
note(
    "🫁 [Hipoxia] Pregunta: {{c1::¿se atragantó/estaba comiendo/ahogo? asma, EPOC, neumonía, opioides, humo, ahogamiento}}. "
    "ABCDE: {{c2::A/B — vía aérea obstruida, no eleva tórax, cianosis, sibilancias/estertores, SpO₂ baja}}. "
    "Manejo: {{c3::abrir vía aérea, retirar cuerpo extraño visible, aspirar, ventilar con bolsa-válvula-mascarilla + O₂, "
    "RCP si paro; adrenalina IM si anafilaxia peri-paro}}.",
)
note(
    "🩸 [Hipovolemia] Pregunta: {{c1::¿sangró/trauma/vómito-diarrea severos/quemaduras/embarazo o dolor pélvico/"
    "hemorragia digestiva?}}. ABCDE: {{c2::C/E — palidez, piel fría, pulsos débiles, llenado lento, hipotensión, "
    "sangrado visible}}. Manejo: {{c3::control de hemorragia (presión directa/torniquete), supino, 2 vías IV + "
    "cristaloides/hemocomponentes, cirugía si sangrado interno}}.",
)
note(
    "⚗️ [Hidrogeniones / acidosis] Pregunta: {{c1::¿sepsis/fiebre/infección? diabetes descontrolada (Kussmaul), "
    "insuficiencia renal, paro prolongado, tóxicos}}. ABCDE: {{c2::B/C/D — Kussmaul previo, shock, alteración neuro, "
    "datos de sepsis/DKA}}. Manejo: {{c3::RCP efectiva, ventilación/O₂, tratar causa (líquidos+antibiótico si sepsis; "
    "insulina+líquidos si DKA); bicarbonato solo en casos seleccionados por ACLS}}.",
)
note(
    "🧂 [Hipo/hiperkalemia] Pregunta: {{c1::¿enfermedad renal/diálisis? ¿faltó a diálisis? potasio, espironolactona, "
    "IECA/ARA-II; debilidad súbita; DKA}}. ABCDE: {{c2::C/D — arritmias; en monitor QRS ancho y T picudas; "
    "fístula de diálisis visible en E}}. Manejo: {{c3::BLS: RCP+DEA+avisar; avanzado: calcio IV si hiperK, "
    "insulina+glucosa, salbutamol, bicarbonato, diálisis si renal}}.",
)
note(
    "🥶 [Hipotermia] Pregunta: {{c1::¿estuvo en frío/agua fría/intemperie/intoxicado/inmersión?}}. "
    "ABCDE: {{c2::E/C/D — piel muy fría, temperatura baja, rigidez, bradicardia, pupilas lentas, bajo nivel de conciencia}}. "
    "Manejo: {{c3::retirar ropa húmeda, cubrir/ambiente cálido, manejo suave, continuar RCP, recalentar; "
    "NO declarar muerte hasta recalentar}}.",
)

# ---------- 5T ----------
note(
    "🎈 [Neumotórax a Tensión] Pregunta: {{c1::¿trauma de tórax/herida penetrante/ventilación mecánica/"
    "dolor súbito + falta de aire?}}. ABCDE: {{c2::B/C — tórax asimétrico, ausencia unilateral de murmullo, "
    "hipersonoridad, ingurgitación yugular, hipotensión, desviación traqueal (tardía), PEA}}. "
    "Manejo: {{c3::O₂, RCP; descompresión con aguja/toracostomía → tubo torácico; sello oclusivo si herida abierta}}.",
)
note(
    "💧 [Taponamiento cardiaco] Pregunta: {{c1::¿herida penetrante en pecho/trauma/cáncer/pericarditis/diálisis/"
    "procedimiento cardiaco reciente?}}. ABCDE: {{c2::C/B — hipotensión, ingurgitación yugular, ruidos apagados, "
    "pulso paradójico, PEA con pulmones relativamente limpios}}. Manejo: {{c3::RCP, líquidos IV como puente, "
    "aviso inmediato a cirugía; definitivo: pericardiocentesis o toracotomía}}.",
)
note(
    "💊 [Toxinas / tabletas] Pregunta: {{c1::¿medicamentos/drogas/alcohol/opioides? frascos, parches, pesticidas, "
    "monóxido de carbono, intento suicida}}. ABCDE: {{c2::D/A/B/E — pupilas puntiformes + respiración lenta (opioides), "
    "secreciones (organofosforados), frascos/parches, hipoventilación}}. Manejo: {{c3::RCP/ventilación, retirar "
    "exposición/parches, naloxona si opioide (sin retrasar RCP), centro toxicológico/antídotos específicos}}.",
)
note(
    "🫀 [Trombosis pulmonar / TEP masivo] Pregunta: {{c1::¿disnea súbita/dolor pleurítico/hemoptisis? cirugía reciente, "
    "inmovilización, viaje largo, cáncer, embarazo/puerperio, anticonceptivos; pierna hinchada}}. "
    "ABCDE: {{c2::B/C — hipoxia, taquicardia, hipotensión, ingurgitación yugular, pulmones a veces limpios, PEA; "
    "signos de TVP}}. Manejo: {{c3::RCP + O₂, activar traslado/ALS; trombólisis o embolectomía en TEP masivo}}.",
)
note(
    "❤️ [Trombosis coronaria / IAM] Pregunta: {{c1::¿dolor opresivo irradiado a brazo/mandíbula/espalda? sudor frío, "
    "náusea, antecedente de infarto, HTA, diabetes, tabaquismo}}. ABCDE: {{c2::C — paro súbito, FV/TV desfibrilable, "
    "piel fría/diaforesis; post-ROSC ECG con elevación ST o isquemia}}. Manejo: {{c3::RCP + DEA/desfibrilación si ritmo "
    "desfibrilable; post-ROSC: ECG, antiagregación si indicado, reperfusión/cateterismo urgente}}.",
)

os.makedirs(OUT, exist_ok=True)
out_path = os.path.join(OUT, "Guiones_ECOE_Causas_Reversibles_5H5T.apkg")
genanki.Package([deck]).write_to_file(out_path)
print(f"OK -> {out_path}")
print(f"  Causas reversibles 5H/5T: {len(deck.notes)} notas (deck {DECK_ID})")
