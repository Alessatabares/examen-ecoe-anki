"""
RCP Adulto — Capa 1 (Flujo Macro)
Guía: AHA 2025 (publicada 22-oct-2025)
Output: output/RCP_Adulto_Capa1.apkg
"""
import os
import json
import genanki

TEMA_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPO_ROOT = os.path.dirname(TEMA_ROOT)
OUTPUT = os.path.join(TEMA_ROOT, "output", "RCP_Adulto_Capa1.apkg")
IDS_PATH = os.path.join(REPO_ROOT, "ids.json")

DECK_ID = 1379129479
DECK_NAME = "RCP Adulto::Capa 1 - Flujo Macro"

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

BASE_TAGS = ["capa1", "rcp_adulto", "aha2025"]

CARDS = [
    # Bloque A — Aproximación, consciencia, activación
    {
        "text": "Antes de aproximarte a un paciente colapsado, lo primero es {{c1::evaluar la seguridad de la escena}} para no convertirte en una segunda víctima.",
        "extra": '🗣️ ECOE: "La escena es segura, procedo a evaluar al paciente."',
        "tags": ["escena", "ecoe"],
    },
    {
        "text": "AVDI evalúa el nivel de consciencia inicial: {{c1::Alerta}} → {{c2::respuesta a Voz}} → {{c3::respuesta a Dolor}} → {{c4::Inconsciente}}.",
        "extra": "Mnemotecnia rápida para clasificar consciencia antes de pasar a Glasgow.",
        "tags": ["avdi"],
    },
    {
        "text": "Si un paciente no responde, antes de cualquier maniobra debes {{c1::pedir ayuda en voz alta}} y {{c2::activar el SEM}}.",
        "extra": '🗣️ ECOE: "¡Necesito ayuda aquí! Tú —señalando— llama al 911 y trae un DEA."',
        "tags": ["sem", "ecoe"],
    },
    {
        "text": "La activación del SEM se hace con {{c1::delegación dirigida}}: señalar a una persona concreta y darle una orden específica, nunca pedir ayuda al grupo en general.",
        "extra": '🗣️ ECOE: "Tú, el del suéter azul: llama al 911 y avisa que es un paro cardíaco. Tú, busca un DEA y tráelo."',
        "tags": ["sem", "ecoe"],
    },

    # Bloque B — Cadena de Supervivencia 2025
    {
        "text": "La Cadena de Supervivencia AHA 2025 es un {{c1::marco único y unificado}} que aplica a adultos y pediátricos, intra y extrahospitalarios.",
        "extra": "Cambio AHA 2025: antes existían 4 cadenas separadas (adulto/pediátrico × IHCA/OHCA); ahora una sola.",
        "tags": ["cadena_supervivencia"],
    },

    # Bloque C — Bifurcación pulso/respiración
    {
        "text": "La comprobación inicial de pulso {{c1::carotídeo}} y respiración se hace {{c2::simultáneamente}}, en {{c3::no más de 10 segundos}}.",
        "extra": '🗣️ ECOE: "Reviso pulso carotídeo y respiración simultáneamente, no más de 10 segundos."',
        "tags": ["bifurcacion", "ecoe"],
    },
    {
        "text": "Tras la valoración inicial hay tres escenarios: con pulso y respira → {{c1::ABCDE}}; con pulso pero no respira → {{c2::ventilaciones (paro respiratorio aislado)}}; sin pulso → {{c3::CAB / iniciar RCP}}.",
        "extra": "Esta bifurcación rectora ordena toda la conducta posterior.",
        "tags": ["bifurcacion"],
    },
    {
        "text": "En paro respiratorio aislado con sospecha de sobredosis por opioides, además de ventilar se debe administrar {{c1::naloxona}}.",
        "extra": '🗣️ ECOE: "Ventilaciones de rescate y, dado el contexto, administro naloxona IM/IN."\n\nNuevo en AHA 2025: naloxona incorporada al algoritmo BLS para legos.',
        "tags": ["naloxona", "ecoe"],
    },

    # Bloque D — ABCDE (paciente con pulso)
    {
        "text": "Para el paciente con pulso, la valoración primaria sigue {{c1::ABCDE}}: vía aérea, respiración, circulación, déficit neurológico, exposición.",
        "extra": '🗣️ ECOE: "Procedo a valoración primaria ABCDE."',
        "tags": ["abcde", "ecoe"],
    },
    {
        "text": "En ABCDE, la **A** corresponde a {{c1::vía aérea (Airway)}} y su permeabilidad.",
        "extra": '🗣️ ECOE: "A — vía aérea: permeable, sin cuerpos extraños ni signos de obstrucción."',
        "tags": ["abcde", "ecoe"],
    },
    {
        "text": "En ABCDE, la **B** corresponde a {{c1::respiración / ventilación (Breathing)}}: frecuencia respiratoria, simetría torácica, saturación, auscultación.",
        "extra": '🗣️ ECOE: "B — respiración: FR, expansión torácica simétrica, SatO2, auscultación bilateral."',
        "tags": ["abcde", "ecoe"],
    },
    {
        "text": "En ABCDE, la **C** corresponde a {{c1::circulación (Circulation)}}: pulso, TA, llenado capilar, color y temperatura de la piel.",
        "extra": '🗣️ ECOE: "C — circulación: FC, TA, llenado capilar, perfusión periférica."',
        "tags": ["abcde", "ecoe"],
    },
    {
        "text": "En ABCDE, la **D** corresponde a {{c1::déficit neurológico (Disability)}}: Glasgow, pupilas y glucemia capilar.",
        "extra": '🗣️ ECOE: "D — neurológico: Glasgow, pupilas isocóricas y reactivas, glucemia capilar."',
        "tags": ["abcde", "ecoe"],
    },
    {
        "text": "En ABCDE, la **E** corresponde a {{c1::exposición y entorno (Exposure)}}: desvestir para inspeccionar, revisar dorso, prevenir hipotermia.",
        "extra": '🗣️ ECOE: "E — exposición: desvisto al paciente buscando lesiones ocultas, reviso dorso, controlo temperatura, lo cubro."',
        "tags": ["abcde", "ecoe"],
    },

    # Bloque E — CAB (paro)
    {
        "text": "En el paciente sin pulso, la secuencia es {{c1::CAB}}: {{c2::Compresiones → vía Aérea → ventilación (Breathing)}}.",
        "extra": '🗣️ ECOE: "Paciente en paro: inicio CAB, comenzando con compresiones."',
        "tags": ["cab", "ecoe"],
    },
    {
        "text": "El motivo de iniciar por **C** (compresiones) en lugar de A en el paro adulto es {{c1::no retrasar la perfusión coronaria y cerebral}}; las compresiones son la única manera de generar flujo en ausencia de gasto cardíaco.",
        "extra": "Cambio histórico ABC → CAB precisamente para empezar a perfundir lo antes posible.",
        "tags": ["cab"],
    },
    {
        "text": "RCP de alta calidad descansa en cinco elementos: {{c1::profundidad adecuada}}, {{c2::frecuencia adecuada}}, {{c3::permitir el retroceso completo del tórax (recoil)}}, {{c4::minimizar interrupciones}} y {{c5::evitar hiperventilación}}.",
        "extra": "Capa 1: solo los conceptos. Los números van en Capa 2.",
        "tags": ["rcp_calidad"],
    },
    {
        "text": "El DEA debe colocarse y usarse {{c1::lo antes posible}}, intercalado con compresiones para minimizar las pausas.",
        "extra": '🗣️ ECOE: "En cuanto llegue el DEA lo aplico, sin detener las compresiones más allá de lo imprescindible."',
        "tags": ["dea", "ecoe"],
    },

    # Bloque F — Eje paralelo 5H/5T
    {
        "text": "Las causas reversibles **5H/5T** se buscan {{c1::como eje paralelo durante la RCP}}, sin detener las compresiones.",
        "extra": '🗣️ ECOE: "Mientras se mantiene RCP, repaso 5H y 5T buscando causa reversible."',
        "tags": ["5h_5t", "ecoe"],
    },
    {
        "text": "Las **5H** son: {{c1::Hipovolemia}}, {{c2::Hipoxia}}, {{c3::Hidrogeniones (acidosis)}}, {{c4::Hipo/Hiperpotasemia}} e {{c5::Hipotermia}}.",
        "extra": "",
        "tags": ["5h_5t"],
    },
    {
        "text": "Las **5T** son: {{c1::Tóxicos}}, {{c2::Taponamiento cardíaco}}, {{c3::neumotórax a Tensión}}, {{c4::Trombosis coronaria (IAM)}} y {{c5::Trombosis pulmonar (TEP)}}.",
        "extra": "",
        "tags": ["5h_5t"],
    },

    # Bloque G — Post-paro
    {
        "text": "Tras el retorno de la circulación espontánea (RCE), la conducta vuelve a la valoración {{c1::ABCDE}} para optimizar oxigenación, hemodinamia y manejo neurológico.",
        "extra": '🗣️ ECOE: "Confirmo RCE; paso a valoración ABCDE para fase post-paro."',
        "tags": ["post_paro", "abcde", "ecoe"],
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
