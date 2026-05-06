"""
RCP Adulto — Capa 3 (Ejes fisiopatológicos 5H/5T)
Estructura por causa: fisiopatología → presentación → pista clínica → manejo.
Guía: AHA 2025 (publicada 22-oct-2025)
Output: output/RCP_Adulto_Capa3.apkg
"""
import os
import json
import genanki

TEMA_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPO_ROOT = os.path.dirname(TEMA_ROOT)
OUTPUT = os.path.join(TEMA_ROOT, "output", "RCP_Adulto_Capa3.apkg")
IDS_PATH = os.path.join(REPO_ROOT, "ids.json")

DECK_ID = 1824168378
DECK_NAME = "RCP Adulto::Capa 3 - Ejes"

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

BASE_TAGS = ["capa3", "rcp_adulto", "aha2025"]

CARDS = [
    # ────────────────────────────────────
    # 1. HIPOVOLEMIA (3)
    # ────────────────────────────────────
    {
        "text": "**Hipovolemia — fisiopatología:** pérdida de {{c1::volumen circulante efectivo}} → caída de {{c2::precarga}} → caída de gasto cardíaco → ritmo más frecuente {{c3::AESP}} (puede llegar a asistolia).",
        "extra": "Causa más prevenible y tratable de las 5H si se identifica precoz.",
        "tags": ["5h_5t", "hipovolemia"],
    },
    {
        "text": "**Hipovolemia — presentación y pista en valoración inicial:** en **C** del ABCDE → {{c1::taquicardia previa al paro}}, {{c2::hipotensión}}, llenado capilar > 3 s, {{c3::venas yugulares planas}}; contexto: hemorragia, vómitos/diarrea profusa, quemado, sepsis tardía.",
        "extra": '🗣️ ECOE: "Llenado capilar lento, yugulares planas y antecedente de sangrado: sospecho hipovolemia."',
        "tags": ["5h_5t", "hipovolemia", "ecoe"],
    },
    {
        "text": "**Hipovolemia — manejo específico:** {{c1::cristaloides en bolo 30 mL/kg}}, control del foco ({{c2::hemorragia → torniquete / hemoderivados; sepsis → antibiótico precoz}}) y {{c3::vasopresor}} si refractario tras volumen.",
        "extra": '🗣️ ECOE: "Bolo cristaloide 30 mL/kg, control del foco hemorrágico, vasopresor si persiste hipotenso."',
        "tags": ["5h_5t", "hipovolemia", "ecoe"],
    },

    # ────────────────────────────────────
    # 2. HIPOXIA (2)
    # ────────────────────────────────────
    {
        "text": "**Hipoxia — fisio + pista:** PaO2 baja → bradicardia → AESP/asistolia. Pista en **B**: {{c1::cianosis}}, {{c2::SatO2 baja previa al paro}}, broncoespasmo, obstrucción de vía aérea; ritmo típico {{c3::AESP}}.",
        "extra": '🗣️ ECOE: "Cianosis y desaturación previa al colapso: sospecho hipoxia como causa."',
        "tags": ["5h_5t", "hipoxia", "ecoe"],
    },
    {
        "text": "**Hipoxia — manejo:** oxigenación con {{c1::BVM + reservorio al 100%}}, asegurar vía aérea avanzada, descartar y resolver {{c2::obstrucción}} (cuerpo extraño, broncoespasmo, secreciones).",
        "extra": "Ventilar ANTES de buscar otras causas si la hipoxia es evidente.",
        "tags": ["5h_5t", "hipoxia"],
    },

    # ────────────────────────────────────
    # 3. HIDROGENIONES / ACIDOSIS (2)
    # ────────────────────────────────────
    {
        "text": "**Acidosis (H+) — fisio + pista:** pH bajo → {{c1::desensibilización a catecolaminas}} y arritmias. Pista: respiración de {{c2::Kussmaul}} previa, antecedente de {{c3::CAD, IRC o sepsis}}, gasometría con pH < 7.2.",
        "extra": "La gasometría arterial durante RCP no siempre es fiable; orientarse por el contexto.",
        "tags": ["5h_5t", "acidosis"],
    },
    {
        "text": "**Acidosis — manejo:** {{c1::ventilación efectiva}} corrige el componente respiratorio; el bicarbonato NO es rutinario, solo en {{c2::acidosis metabólica grave, hiperpotasemia o sobredosis de antidepresivos tricíclicos}}.",
        "extra": "Bicarbonato indiscriminado durante RCP empeora la acidosis intracelular.",
        "tags": ["5h_5t", "acidosis", "bicarbonato"],
    },

    # ────────────────────────────────────
    # 4. POTASIO (3) — hipo + hiper
    # ────────────────────────────────────
    {
        "text": "**Hipopotasemia — fisio + pista en ECG previo:** hiperexcitabilidad miocárdica → {{c1::ondas U prominentes}}, {{c2::QT largo}}, riesgo de {{c3::TV polimórfica / torsade de pointes}}. Contexto: diuréticos, vómitos/diarrea, alcoholismo.",
        "extra": "Casi siempre se acompaña de hipomagnesemia: corregir ambos.",
        "tags": ["5h_5t", "hipopotasemia"],
    },
    {
        "text": "**Hiperpotasemia — fisio + pista en ECG previo:** despolarización mantenida → secuencia {{c1::T picudas → PR largo → QRS ancho → onda sinusoidal → asistolia}}. Contexto: {{c2::IRC, rabdomiólisis, IECA/ARA-II/espironolactona, lisis tumoral}}.",
        "extra": '🗣️ ECOE: "T picudas y QRS ancho con antecedente de IRC: sospecho hiperpotasemia."',
        "tags": ["5h_5t", "hiperpotasemia", "ecoe"],
    },
    {
        "text": "**Manejo K:** Hipo → reposición de {{c1::K IV con Mg}}. Hiper → secuencia {{c2::gluconato cálcico (estabiliza membrana) → insulina + glucosa → β2-agonista → bicarbonato → diálisis}}.",
        "extra": '🗣️ ECOE: "Hiper K con cambios en ECG: gluconato cálcico inmediato, insulina con glucosa, salbutamol nebulizado y aviso a nefrología para diálisis."',
        "tags": ["5h_5t", "hiperpotasemia", "hipopotasemia", "ecoe"],
    },

    # ────────────────────────────────────
    # 5. HIPOTERMIA (3)
    # ────────────────────────────────────
    {
        "text": "**Hipotermia — fisio:** T < 30 °C → {{c1::bradicardia}} → {{c2::FV / asistolia}}; el miocardio frío es {{c3::refractario a fármacos y desfibrilación}}.",
        "extra": "Por debajo de 30 °C, fisiología cardíaca completamente alterada.",
        "tags": ["5h_5t", "hipotermia"],
    },
    {
        "text": "**Hipotermia — pista en E del ABCDE:** contexto de {{c1::ahogamiento, exposición a frío, anciano hallado en domicilio sin calefacción}}; **pupilas no son útiles** (pueden estar arreactivas reversibles).",
        "extra": "Aforismo: 'no se está muerto hasta que se está caliente y muerto'.",
        "tags": ["5h_5t", "hipotermia"],
    },
    {
        "text": "**Hipotermia — manejo:** {{c1::recalentamiento activo}} (extracorpóreo / ECMO si severa); si T < 30 °C limitar a {{c2::3 descargas}} hasta calentar; {{c3::espaciar fármacos}} (acumulación por metabolismo lento) y prolongar la RCP.",
        "extra": '🗣️ ECOE: "Hipotermia profunda: máximo 3 descargas, espacio adrenalina y mantengo RCP mientras inicio recalentamiento extracorpóreo."',
        "tags": ["5h_5t", "hipotermia", "ecoe"],
    },

    # ────────────────────────────────────
    # 6. TÓXICOS (3) — incluye opioides
    # ────────────────────────────────────
    {
        "text": "**Tóxicos — fisio:** mecanismo según agente. Opioides → {{c1::depresión respiratoria → hipoxia → paro}}; ATC → {{c2::bloqueo canales de sodio → QRS ancho → arritmia}}; BB/BCC → {{c3::bradicardia + hipotensión refractaria}}; CO → desplazamiento O2 de la Hb.",
        "extra": "La causa final del paro casi siempre es secundaria (hipoxia, arritmia, shock).",
        "tags": ["5h_5t", "toxicos"],
    },
    {
        "text": "**Tóxicos — pista en valoración inicial:** **D** → {{c1::pupilas puntiformes (opioides)}}, {{c2::midriasis (anticolinérgicos / simpaticomiméticos)}}; ECG → {{c3::QRS ancho (ATC, antiarrítmicos)}}; contexto (frasco, jeringa, antecedente psiquiátrico).",
        "extra": '🗣️ ECOE: "Pupilas puntiformes, depresión respiratoria y jeringa cercana: sospecho intoxicación por opioides."',
        "tags": ["5h_5t", "toxicos", "opioides", "ecoe"],
    },
    {
        "text": "**Tóxicos — manejo por agente:** Opioides → {{c1::naloxona 0.4–2 mg IM/IN/IV, repetir cada 2–3 min hasta 10 mg}}. ATC → {{c2::bicarbonato sódico}}. β-bloqueantes → {{c3::glucagón}}. BCC → {{c4::calcio + insulina a alta dosis (HIET)}}. CO → {{c5::O2 al 100% / cámara hiperbárica}}.",
        "extra": "AHA 2025: naloxona en algoritmo BLS de legos para sospecha de sobredosis.",
        "tags": ["5h_5t", "toxicos", "naloxona"],
    },

    # ────────────────────────────────────
    # 7. TAPONAMIENTO CARDÍACO (2)
    # ────────────────────────────────────
    {
        "text": "**Taponamiento cardíaco — fisio + presentación:** acúmulo pericárdico → caída de {{c1::llenado diastólico}} → caída del gasto → AESP. Tríada de Beck: {{c2::hipotensión, ingurgitación yugular, ruidos cardíacos apagados}}.",
        "extra": "Contexto: trauma torácico penetrante, pericarditis, post-IAM (rotura), urémico, neoplásico.",
        "tags": ["5h_5t", "taponamiento"],
    },
    {
        "text": "**Taponamiento — pista y manejo:** pista decisiva en C/eco bedside ({{c1::derrame pericárdico con colapso de cavidades derechas}}); manejo: {{c2::pericardiocentesis}} urgente (subxifoidea guiada por eco).",
        "extra": '🗣️ ECOE: "Tríada de Beck con eco que muestra derrame y colapso de VD: pericardiocentesis subxifoidea inmediata."',
        "tags": ["5h_5t", "taponamiento", "ecoe"],
    },

    # ────────────────────────────────────
    # 8. NEUMOTÓRAX A TENSIÓN (2)
    # ────────────────────────────────────
    {
        "text": "**Neumotórax a tensión — fisio + presentación:** aire en pleura con mecanismo valvular → colapso pulmonar + desplazamiento mediastínico → caída del retorno venoso. Pista en B/C: {{c1::hipoventilación + hiperresonancia unilateral}}, {{c2::desviación traqueal contralateral}}, ingurgitación yugular, {{c3::alta resistencia al ventilar con BVM}}.",
        "extra": "Contexto: trauma, ventilación mecánica, asma severo, EPOC con bullas.",
        "tags": ["5h_5t", "neumotorax"],
    },
    {
        "text": "**Neumotórax a tensión — manejo:** {{c1::descompresión con aguja inmediata}} (2.º EIC línea medioclavicular o {{c2::4.º–5.º EIC línea axilar anterior}}), seguida de {{c3::tubo torácico}} definitivo.",
        "extra": '🗣️ ECOE: "Sospecho neumotórax a tensión: descompresión con aguja en 4.º EIC línea axilar anterior y aviso para colocar tubo de tórax."',
        "tags": ["5h_5t", "neumotorax", "ecoe"],
    },

    # ────────────────────────────────────
    # 9. TROMBOSIS CORONARIA / IAM (3)
    # ────────────────────────────────────
    {
        "text": "**Trombosis coronaria (IAM) — fisio:** oclusión coronaria → isquemia transmural → inestabilidad eléctrica → {{c1::FV / TV sin pulso}} (ritmo desfibrilable más frecuente).",
        "extra": "Causa más común de paro extrahospitalario súbito en adulto.",
        "tags": ["5h_5t", "iam"],
    },
    {
        "text": "**IAM — pista en valoración inicial / contexto:** {{c1::dolor torácico opresivo previo}}, factores de riesgo cardiovascular, ECG previo con {{c2::SCACEST o cambios isquémicos}}; ritmo en paro {{c3::FV/TVsp}}.",
        "extra": '🗣️ ECOE: "Antecedente de dolor torácico y FV en monitor: sospecho IAM como causa del paro."',
        "tags": ["5h_5t", "iam", "ecoe"],
    },
    {
        "text": "**IAM — manejo:** intra-paro → {{c1::desfibrilación + RCP de calidad}}; tras RCE → {{c2::ICP urgente (puerta-balón ≤ 90 min)}}; si ICP no disponible → {{c3::trombólisis sistémica}} (siempre que no haya contraindicaciones tras RCE).",
        "extra": "Activación del laboratorio de hemodinamia debe arrancar mientras se trabaja la RCP.",
        "tags": ["5h_5t", "iam"],
    },

    # ────────────────────────────────────
    # 10. TROMBOSIS PULMONAR / TEP (3)
    # ────────────────────────────────────
    {
        "text": "**TEP masivo — fisio:** obstrucción del tracto de salida del VD → {{c1::sobrecarga aguda del ventrículo derecho}} → caída del gasto del VI → AESP/colapso. Hipoxia refractaria al oxígeno.",
        "extra": "Causa relativamente frecuente de AESP intrahospitalaria postoperatoria/inmovilización.",
        "tags": ["5h_5t", "tep"],
    },
    {
        "text": "**TEP — pista en valoración inicial:** {{c1::disnea súbita previa}}, factores Wells ({{c2::cirugía/inmovilización/cáncer/TVP previa}}), ritmo {{c3::AESP}}, hipoxia que no mejora; eco bedside con {{c4::dilatación de ventrículo derecho}}.",
        "extra": '🗣️ ECOE: "Postoperatorio reciente, disnea súbita y AESP con VD dilatado en eco: sospecho TEP."',
        "tags": ["5h_5t", "tep", "ecoe"],
    },
    {
        "text": "**TEP — manejo intra-paro:** {{c1::trombólisis sistémica empírica (alteplasa)}} ante alta sospecha; tras administrarla, prolongar la RCP {{c2::al menos 60–90 min}}; {{c3::ECMO o embolectomía quirúrgica}} si centro disponible.",
        "extra": '🗣️ ECOE: "Alta sospecha de TEP masivo: administro alteplasa y mantengo RCP al menos 60 minutos."',
        "tags": ["5h_5t", "tep", "ecoe"],
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
