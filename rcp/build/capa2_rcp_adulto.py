"""
RCP Adulto — Capa 2 (Componentes técnicos)
Guía: AHA 2025 (publicada 22-oct-2025)
Output: output/RCP_Adulto_Capa2.apkg
"""
import os
import json
import genanki

TEMA_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPO_ROOT = os.path.dirname(TEMA_ROOT)
OUTPUT = os.path.join(TEMA_ROOT, "output", "RCP_Adulto_Capa2.apkg")
IDS_PATH = os.path.join(REPO_ROOT, "ids.json")

DECK_ID = 1184050405
DECK_NAME = "RCP Adulto::Capa 2 - Componentes"

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

BASE_TAGS = ["capa2", "rcp_adulto", "aha2025"]

CARDS = [
    # Bloque A — AVDI técnica (2)
    {
        "text": "AVDI — estímulo verbal correcto: llamar al paciente {{c1::por su nombre}} y dar una orden simple (ej. 'abra los ojos'); registrar respuesta a la llamada y a la orden.",
        "extra": '🗣️ ECOE: "Señor García, ¿me escucha? Abra los ojos."',
        "tags": ["avdi", "ecoe"],
    },
    {
        "text": "AVDI — estímulo doloroso correcto: presión sobre {{c1::trapecio}}, {{c2::lecho ungueal}} o {{c3::reborde supraorbitario}}. Evitar el {{c4::frote esternal con nudillos}} por riesgo de lesión.",
        "extra": "Lo lesivo no es necesario: hay alternativas igual de efectivas y seguras.",
        "tags": ["avdi"],
    },

    # Bloque B — ABCDE componente por componente (10)
    {
        "text": "**A** sin trauma cervical: maniobra {{c1::frente-mentón}} (extensión cefálica + elevación del mentón).",
        "extra": '🗣️ ECOE: "Sin sospecha de trauma, realizo maniobra frente-mentón para abrir la vía aérea."',
        "tags": ["abcde", "via_aerea", "ecoe"],
    },
    {
        "text": "**A** con sospecha de trauma cervical: maniobra {{c1::tracción mandibular (jaw-thrust)}}; {{c2::no extender el cuello}}.",
        "extra": '🗣️ ECOE: "Sospecho lesión cervical: tracción mandibular sin movilizar el cuello, mantengo alineación."',
        "tags": ["abcde", "via_aerea", "trauma", "ecoe"],
    },
    {
        "text": "Signos de obstrucción de vía aérea: {{c1::estridor}}, {{c2::ronquido}}, {{c3::gorgoteo}}, {{c4::tiraje}} y, en obstrucción completa, {{c5::silencio total con esfuerzo respiratorio}}.",
        "extra": "Cada sonido orienta nivel: estridor → laríngeo; ronquido → caída de lengua; gorgoteo → secreciones/sangre.",
        "tags": ["abcde", "via_aerea"],
    },
    {
        "text": "**B** — parámetros normales adulto: FR {{c1::12–20/min}}; SatO2 objetivo {{c2::≥ 94%}} (en EPOC, {{c3::88–92%}}).",
        "extra": '🗣️ ECOE: "Frecuencia respiratoria 16, saturación 97% al aire ambiente."',
        "tags": ["abcde", "respiracion", "ecoe"],
    },
    {
        "text": "**B** — signos de gravedad respiratoria: taquipnea {{c1::> 30/min}}, bradipnea {{c2::< 8/min}}, uso de musculatura accesoria, asimetría torácica o silencio auscultatorio.",
        "extra": "Cualquiera de estos obliga a considerar soporte ventilatorio inmediato.",
        "tags": ["abcde", "respiracion"],
    },
    {
        "text": "**C** — umbrales de hipotensión adulto: TAS {{c1::< 90 mmHg}} o caída ≥ {{c2::40 mmHg}} respecto a la basal. FC normal {{c3::60–100/min}}.",
        "extra": '🗣️ ECOE: "TA 85/50, FC 118: paciente hipotenso y taquicárdico, sospecho shock."',
        "tags": ["abcde", "circulacion", "ecoe"],
    },
    {
        "text": "**C** — llenado capilar: normal {{c1::≤ 2 segundos}}; mayor de {{c2::3 segundos}} sugiere hipoperfusión periférica.",
        "extra": "Comprimir lecho ungueal 5 s y soltar; comparar con valor basal/temperatura.",
        "tags": ["abcde", "circulacion"],
    },
    {
        "text": "**D** — Glasgow se compone de Apertura ocular ({{c1::/4}}), Respuesta verbal ({{c2::/5}}) y Respuesta motora ({{c3::/6}}). Indicación de vía aérea avanzada con Glasgow {{c4::≤ 8}}.",
        "extra": '🗣️ ECOE: "Glasgow 7 (O2 V2 M3): indico aislamiento de vía aérea."',
        "tags": ["abcde", "neurologico", "ecoe"],
    },
    {
        "text": "**D** — siempre evaluar pupilas ({{c1::tamaño, simetría y reactividad}}) y {{c2::glucemia capilar}} ante alteración de consciencia.",
        "extra": '🗣️ ECOE: "Pupilas isocóricas reactivas, glucemia capilar 92 mg/dL."',
        "tags": ["abcde", "neurologico", "ecoe"],
    },
    {
        "text": "**E** — durante exposición: {{c1::controlar hemorragias externas}}, revisar el {{c2::dorso (rolo en bloque)}} y {{c3::prevenir hipotermia (manta térmica)}}.",
        "extra": '🗣️ ECOE: "Expongo, reviso dorso en bloque, controlo hemorragias y cubro al paciente con manta térmica."',
        "tags": ["abcde", "exposicion", "ecoe"],
    },

    # Bloque C — CAB detallado (1)
    {
        "text": "En paro adulto presenciado: iniciar **C** (compresiones) {{c1::antes}} de colocar vía aérea o ventilar; mantener ratio {{c2::30:2}} hasta colocar vía aérea avanzada.",
        "extra": "Sin vía aérea avanzada → ciclos 30:2. Con vía aérea avanzada → compresiones continuas + ventilaciones asincrónicas.",
        "tags": ["cab"],
    },

    # Bloque D — Compresiones (5)
    {
        "text": "Frecuencia de compresiones: {{c1::100–120 por minuto}}.",
        "extra": "Por debajo de 100 cae la perfusión; por encima de 120 cae la profundidad y el llenado diastólico.",
        "tags": ["compresiones"],
    },
    {
        "text": "Profundidad de compresiones adulto: {{c1::5–6 cm (2–2.4 in)}}; evitar {{c2::> 6 cm}} por riesgo de lesión torácica.",
        "extra": "Punto medio del rango es lo óptimo: ni superficial ni excesivo.",
        "tags": ["compresiones"],
    },
    {
        "text": "Tras cada compresión debe permitirse el {{c1::retroceso completo del tórax (recoil)}}; no apoyarse sobre el pecho entre compresiones.",
        "extra": "El recoil incompleto reduce el retorno venoso y la perfusión coronaria de la siguiente compresión.",
        "tags": ["compresiones"],
    },
    {
        "text": "Fracción de compresión torácica (CCF): objetivo {{c1::> 60%}}, idealmente {{c2::≥ 80%}}; minimizar las pausas (análisis DEA, ventilación, cambio de compresor).",
        "extra": "Cada segundo sin compresiones cae la presión de perfusión coronaria.",
        "tags": ["compresiones", "rcp_calidad"],
    },
    {
        "text": "Punto y técnica de compresión: {{c1::mitad inferior del esternón}}; {{c2::talón de una mano}} con la otra encima entrelazada; {{c3::brazos rectos}}, hombros sobre el paciente.",
        "extra": '🗣️ ECOE: "Talón de la mano sobre la mitad inferior del esternón, brazos rectos, comprimo perpendicular."',
        "tags": ["compresiones", "ecoe"],
    },

    # Bloque E — Ventilación (5)
    {
        "text": "Bolsa-válvula-mascarilla (BVM): usar desde el inicio si hay {{c1::personal entrenado}} y dispositivo disponible; si rescatador único o no entrenado, {{c2::compresiones-only}} es aceptable y eficaz.",
        "extra": "AHA 2025: ventilaciones recomendadas siempre que el rescatador esté dispuesto y capacitado.",
        "tags": ["ventilacion", "bvm"],
    },
    {
        "text": "Sello de mascarilla con un solo rescatador: técnica {{c1::E-C}} (pulgar e índice formando 'C' sobre la máscara, los otros tres dedos en 'E' sobre la mandíbula). Mejor con dos rescatadores: uno sella, otro ventila.",
        "extra": "Las fugas son la causa más frecuente de ventilación inefectiva con BVM.",
        "tags": ["ventilacion", "bvm"],
    },
    {
        "text": "Ratio compresión:ventilación **sin** vía aérea avanzada: {{c1::30:2}}.",
        "extra": "Mantener este ratio durante ciclos de 2 minutos hasta vía aérea avanzada o RCE.",
        "tags": ["ventilacion", "ratio"],
    },
    {
        "text": "Con vía aérea avanzada: compresiones {{c1::continuas (sin pausa para ventilar)}} + {{c2::1 ventilación cada 6 segundos}} (≈ {{c3::10/min}}). Volumen suficiente para {{c4::ver elevación torácica}}; evitar hiperventilación.",
        "extra": "La hiperventilación aumenta presión intratorácica, reduce retorno venoso y empeora gasto cardíaco.",
        "tags": ["ventilacion", "via_aerea_avanzada"],
    },
    {
        "text": "Ciclos: cambiar de compresor cada {{c1::2 minutos}} (≈ 5 ciclos de 30:2) para evitar fatiga; aprovechar el cambio para {{c2::chequear el ritmo}} con el monitor/DEA.",
        "extra": "Cambio rápido (< 5 s) para no caer la fracción de compresión.",
        "tags": ["compresiones", "ciclo"],
    },

    # Bloque F — DEA (3)
    {
        "text": "Pasos del DEA: {{c1::encender}} → {{c2::colocar parches (infraclavicular derecho + apical/línea axilar media izquierda)}} → 'no toquen' durante el {{c3::análisis}} → {{c4::descarga si está indicada}} → reanudar RCP **inmediatamente** durante {{c5::2 minutos}} antes del siguiente análisis.",
        "extra": '🗣️ ECOE: "Enciendo el DEA, coloco parches, me aparto para análisis, descarga si indica, retomo RCP de inmediato durante 2 minutos."',
        "tags": ["dea", "ecoe"],
    },
    {
        "text": "DEA en niños: usar parches pediátricos si {{c1::< 8 años o < 25 kg}}, si están disponibles. Si no hay parches pediátricos, usar {{c2::parches de adulto en posición anteroposterior}}.",
        "extra": "Nota: el deck es adulto, pero esta diferenciación cae a menudo en ECOE.",
        "tags": ["dea"],
    },
    {
        "text": "Situaciones particulares con DEA: marcapasos/DAI → parche a {{c1::≥ 2.5 cm}} del dispositivo; {{c2::parche transdérmico}} → retirar y limpiar la piel; tórax {{c3::mojado}} → secar; tórax con vello abundante → {{c4::afeitar o usar segundo juego de parches por adherencia inversa}}.",
        "extra": '🗣️ ECOE: "Detecto parche transdérmico: lo retiro, limpio la zona y coloco el parche del DEA."',
        "tags": ["dea", "ecoe"],
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
