"""
Ruidos Cardiacos Adulto — Capa 3 (Ejes transversales)
Guías: AHA/ACC 2020 Valvular Heart Disease + AHA endocarditis
Output: output/Ruidos_Cardiacos_Adulto_Capa3.apkg
"""
import os
import json
import genanki

TEMA_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPO_ROOT = os.path.dirname(TEMA_ROOT)
OUTPUT = os.path.join(TEMA_ROOT, "output", "Ruidos_Cardiacos_Adulto_Capa3.apkg")
IDS_PATH = os.path.join(REPO_ROOT, "ids.json")

DECK_ID = 1179866901
DECK_NAME = "Ruidos Cardiacos Adulto::Capa 3 - Ejes"

with open(IDS_PATH) as f:
    MODEL_ID = json.load(f)["models"]["cloze_estandar"]

CSS = """
.card {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  font-size: 19px; text-align: left; color: #1a1a1a;
  background-color: #fafafa; padding: 20px; line-height: 1.5;
}
.cloze { font-weight: 600; color: #2563eb; }
#extra { margin-top: 16px; border: none; border-top: 1px solid #d4d4d4; }
"""

model = genanki.Model(
    MODEL_ID,
    "Estudio Médico Cloze",
    fields=[{"name": "Text"}, {"name": "Extra"}],
    templates=[{
        "name": "Cloze",
        "qfmt": "{{cloze:Text}}",
        "afmt": '{{cloze:Text}}<hr id="extra">{{Extra}}',
    }],
    css=CSS,
    model_type=genanki.Model.CLOZE,
)

BASE_TAGS = ["capa3", "ruidos_cardiacos_adulto", "aha", "ecoe"]

CARDS = [
    # Bloque A — EA
    {
        "text": "**EA** — fisiopato: obstrucción al TSVI → {{c1::hipertrofia concéntrica del VI}} → ↑ presión telediastólica. Etiología por edad: {{c2::&lt;70 años: bicúspide; ≥70 años: degenerativa/calcificada}}.",
        "extra": "La válvula aórtica bicúspide es la cardiopatía congénita más frecuente (1-2% de la población). En jóvenes da EA precoz por calcificación acelerada del velo anómalo.",
        "tags": ["ea"],
    },
    {
        "text": "**EA** — presentación: tríada clásica de EA severa = {{c1::angina, síncope, disnea}}. Pulso {{c2::parvus et tardus}}, soplo crescendo-decrescendo aórtico irradiado a carótidas, S2 disminuido o ausente en severas.",
        "extra": '🗣️ ECOE: "Paciente con síncope durante esfuerzo + soplo aórtico crescendo-decrescendo irradiado a carótidas + pulso pequeño y lento — sospecho EA severa, solicito ecocardiograma urgente."',
        "tags": ["ea", "presentacion"],
    },
    {
        "text": "**EA** — manejo: severa sintomática → {{c1::TAVR (≥65 años o alto riesgo quirúrgico) o SAVR}}. Severa asintomática con FE &lt;50% o test de ejercicio positivo → también cirugía. Sin reemplazo en EA severa sintomática → supervivencia {{c2::&lt;50% a 2-3 años}}.",
        "extra": "TAVR (válvula percutánea transcatéter) ha desplazado a SAVR como primera línea en pacientes >75 años o riesgo quirúrgico intermedio-alto. En jóvenes bajos en riesgo, SAVR aún preferida por durabilidad.",
        "tags": ["ea", "manejo"],
    },

    # Bloque B — IM
    {
        "text": "**IM primaria (estructural)** — fisiopato: defecto valvular intrínseco ({{c1::prolapso, ruptura cordal, endocarditis, fiebre reumática}}). Presentación: aguda → {{c2::edema pulmonar súbito}}; crónica → años asintomática, luego disnea de esfuerzo + S3.",
        "extra": "IM aguda no permite adaptación: AI no dilatada → ↑ brusco de presión retrógrada → edema pulmonar fulminante. Sospechar ruptura cordal en paciente con disnea súbita + soplo nuevo en ápex.",
        "tags": ["im", "primaria"],
    },
    {
        "text": "**IM secundaria (funcional)** — fisiopato: válvula normal pero {{c1::dilatación o disfunción del VI}} (miocardiopatía isquémica o dilatada) → desplazamiento del aparato subvalvular → mala coaptación de velos.",
        "extra": "La IM funcional es 'consecuencia' del VI enfermo, no causa. Por eso el tratamiento primero es médico (de la causa de fondo) y la reparación valvular sola raramente cura el problema.",
        "tags": ["im", "secundaria"],
    },
    {
        "text": "**IM** — manejo: primaria severa sintomática, o asintomática con FE ≤60% o DTSVI ≥40 mm → {{c1::reparación valvular preferida sobre reemplazo}}. Secundaria → primero {{c2::tratamiento médico óptimo de IC (IECA, BB, MRA)}}; si persiste sintomática → MitraClip o cirugía.",
        "extra": '🗣️ ECOE: "Paciente con IM primaria severa por prolapso, FE 58% — propongo reparación valvular electiva por mejor pronóstico vs reemplazo y antes de que aparezca disfunción ventricular."',
        "tags": ["im", "manejo"],
    },

    # Bloque C — IAo
    {
        "text": "**IAo** — fisiopato y presentación: válvula incompetente → regurgitación diastólica → {{c1::sobrecarga de volumen del VI con hipertrofia excéntrica}}. Síntomas tardíos. Signos periféricos: {{c2::pulso saltón (Corrigan), Musset, Quincke, Traube, presión de pulso amplia}}.",
        "extra": "Todos los signos periféricos clásicos de IAo derivan del mismo mecanismo: presión de pulso amplia por sístole alta (volumen sistólico aumentado) + diástole baja (regurgitación). Si la PP es amplia, busca IAo.",
        "tags": ["iao"],
    },
    {
        "text": "**IAo** — manejo: severa sintomática, o asintomática con FE ≤55% o DTSVI &gt;50 mm → {{c1::reemplazo valvular aórtico}}. IAo aguda (endocarditis, disección aórtica) → {{c2::cirugía urgente}}.",
        "extra": '🗣️ ECOE: "Soplo decrescendo diastólico nuevo + dolor torácico irradiado a espalda + hipotensión — sospecho disección aórtica con IAo aguda, TAC angio urgente y cirugía cardiovascular."',
        "tags": ["iao", "manejo"],
    },

    # Bloque D — EM
    {
        "text": "**EM** — fisiopato y presentación: etiología #1 {{c1::fiebre reumática}}. Fusión de comisuras → estenosis → ↑ presión en AI → {{c2::fibrilación auricular + congestión pulmonar (disnea, hemoptisis)}}. Soplo: chasquido de apertura + retumbo diastólico en ápex con campana en decúbito lateral izquierdo.",
        "extra": "Cuanto más cerca esté el chasquido de S2, más severa la EM (mayor presión en AI). Refuerzo presistólico desaparece al entrar en FA (no hay contracción auricular efectiva).",
        "tags": ["em"],
    },
    {
        "text": "**EM** — manejo: severa sintomática (área ≤1.0 cm²) con anatomía favorable (Wilkins ≤8) → {{c1::comisurotomía percutánea con balón}}. Score alto, trombo en AI o IM moderada/severa → {{c2::reemplazo valvular quirúrgico}}. Anticoagulación si FA o trombo en AI.",
        "extra": "Wilkins evalúa 4 puntos (movilidad, engrosamiento, calcificación, aparato subvalvular). El umbral ≤8 es el clásico para preferir balón sobre cirugía.",
        "tags": ["em", "manejo"],
    },

    # Bloque E — PVM
    {
        "text": "**PVM** — fisiopato: degeneración mixomatosa de los velos mitrales → desplazamiento &gt;2 mm sobre el anillo. Presentación: frecuentemente asintomático; puede dar {{c1::palpitaciones, dolor torácico atípico, ansiedad}}. Auscultación: {{c2::click mesosistólico + soplo telesistólico en ápex}}.",
        "extra": "Con Valsalva el click se adelanta y el soplo se alarga: el VI más vacío permite que el velo prolapse antes en la sístole. Maniobra diagnóstica clave.",
        "tags": ["pvm"],
    },
    {
        "text": "**PVM** — manejo: asintomático sin IM significativa → {{c1::seguimiento clínico}}. Con IM severa → manejo de IM primaria (reparación valvular preferida). Profilaxis de endocarditis {{c2::NO indicada}} (cambio AHA 2007).",
        "extra": "Antes (pre-2007) se daba profilaxis antibiótica a todos los PVM. La revisión AHA limitó la indicación a alto riesgo real (prótesis, endocarditis previa, cardiopatía congénita cianótica residual, trasplante con valvulopatía).",
        "tags": ["pvm", "manejo"],
    },

    # Bloque F — MCH adulto
    {
        "text": "**MCH adulto** — fisiopato y presentación: hipertrofia ≥15 mm sin causa secundaria + obstrucción dinámica TSVI por SAM. Síntomas: {{c1::disnea, dolor torácico, síncope, palpitaciones, muerte súbita}}. Diferencial con corazón de atleta: {{c2::atleta regresa con desentrenamiento, MCH no}}.",
        "extra": "Otros datos que orientan a corazón de atleta vs MCH: dimensiones del VI normales-altas en atleta vs reducidas en MCH (cavidad pequeña); función diastólica normal en atleta vs alterada en MCH.",
        "tags": ["mch"],
    },
    {
        "text": "**MCH adulto** — manejo: {{c1::betabloqueador o verapamilo}} en obstructiva sintomática; si refractario → {{c2::miectomía septal quirúrgica o ablación septal con alcohol}}. DAI en alto riesgo (score HCM Risk-SCD ESC). Restricción de deportes competitivos.",
        "extra": "Contraindicados en MCH obstructiva: digoxina, nitratos, vasodilatadores, inotrópicos positivos — todos empeoran la obstrucción dinámica al reducir volumen ventricular o aumentar la contractilidad.",
        "tags": ["mch", "manejo"],
    },

    # Bloque G — Endocarditis en drogas IV
    {
        "text": "**Endocarditis en uso de drogas IV** — fisiopato: bacteriemia por inyección no estéril → afecta predominantemente {{c1::válvula tricúspide}} (primera válvula en encontrar). Microorganismo #1: {{c2::Staphylococcus aureus}}.",
        "extra": "En usuarios de drogas IV piensa siempre primero en S. aureus (incluyendo MRSA). Empírico inicial razonable: vancomicina + gentamicina, ajustar a hemocultivos.",
        "tags": ["endocarditis", "drogas_iv"],
    },
    {
        "text": "**Endocarditis tricuspídea** — presentación: {{c1::fiebre, soplo holosistólico en BEII que aumenta con inspiración (Rivero-Carvallo)}}, {{c2::embolia séptica pulmonar (nódulos cavitados en RX)}}. Estigmas periféricos (Janeway, Osler, Roth) menos frecuentes en lado derecho.",
        "extra": '🗣️ ECOE: "Paciente usuario de drogas IV con fiebre + soplo holosistólico en BEII que aumenta con inspiración + nódulos cavitados pulmonares — alta sospecha de endocarditis tricuspídea por S. aureus."',
        "tags": ["endocarditis", "presentacion"],
    },
    {
        "text": "**Endocarditis** — manejo: {{c1::hemocultivos x3 antes de antibiótico empírico}}, ecocardiograma (transtorácico primero, transesofágico si dudas o prótesis), antibioticoterapia 4-6 semanas. Cirugía urgente si: {{c2::insuficiencia cardiaca, infección no controlada, embolia recurrente, o vegetación grande (&gt;10 mm móvil)}}.",
        "extra": "Tres hemocultivos separados por al menos 1 hora antes del antibiótico, idealmente de sitios diferentes. No esperar a la fiebre — la bacteriemia en endocarditis suele ser persistente.",
        "tags": ["endocarditis", "manejo"],
    },

    # Bloque H — Anamnesis + maniobras + derivación urgente
    {
        "text": "**Anamnesis dirigida ECOE adulto** — preguntas obligadas: {{c1::síncope, angina, disnea (clase funcional NYHA), palpitaciones, edemas, fiebre persistente, uso de drogas IV, antecedente reumático en infancia, antecedente familiar de muerte súbita o cardiopatía estructural, embarazo}}.",
        "extra": '🗣️ ECOE: "Antes de auscultar, pregunto por síntomas funcionales (clase NYHA), antecedentes reumáticos en la infancia, fiebre persistente, uso de drogas IV, antecedente familiar de cardiopatía o muerte súbita, y si está embarazada."',
        "tags": ["anamnesis"],
    },
    {
        "text": "**Maniobras dinámicas — verbalización ECOE**: {{c1::Valsalva (↑ MCH/PVM, ↓ resto)}}, {{c2::handgrip (↑ IM/IAo/CIV)}}, {{c3::Rivero-Carvallo en inspiración (↑ IT/EP)}}, sentadilla→pie (↑ MCH/PVM). Anunciar la maniobra elegida y la respuesta esperada antes de ejecutarla.",
        "extra": '🗣️ ECOE: "Para confirmar mi sospecha de MCH, voy a pedirle al paciente que realice maniobra de Valsalva — espero que el soplo aumente claramente. Si así ocurre, refuerza el diagnóstico de obstrucción dinámica."',
        "tags": ["maniobras"],
    },
    {
        "text": "**Cuándo derivar urgente** — banderas rojas adulto: {{c1::síncope/angina/disnea con soplo aórtico (EA severa sintomática)}}, {{c2::soplo nuevo + fiebre persistente (endocarditis)}}, soplo + hemoptisis (EM con congestión pulmonar), {{c3::IAo aguda (endocarditis o disección aórtica)}}. Todos requieren ingreso o derivación inmediata a cardiología.",
        "extra": '🗣️ ECOE: "Este paciente cumple criterio de derivación urgente porque [síntoma específico] + [soplo específico] = [patología grave]. Ingreso a cardiología, no manejo ambulatorio."',
        "tags": ["banderas_rojas", "derivacion"],
    },
]

deck = genanki.Deck(DECK_ID, DECK_NAME)

for card in CARDS:
    note = genanki.Note(
        model=model,
        fields=[card["text"], card["extra"]],
        tags=BASE_TAGS + card["tags"],
    )
    deck.add_note(note)

os.makedirs(os.path.dirname(OUTPUT), exist_ok=True)
genanki.Package(deck).write_to_file(OUTPUT)

print(f"Notas: {len(CARDS)}")
print(f"DECK_ID: {DECK_ID}")
print(f"Output: {OUTPUT}")
