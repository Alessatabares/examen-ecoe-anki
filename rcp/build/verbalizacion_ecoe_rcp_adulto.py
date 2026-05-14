"""
RCP Adulto — Verbalización ECOE
Subdeck paralelo orientado a entrenar qué decir al sinodal en cada bifurcación.
Guía: AHA 2025 (publicada 22-oct-2025)
Output: output/RCP_Adulto_VerbalizacionECOE.apkg
"""
import os
import json
import genanki

TEMA_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPO_ROOT = os.path.dirname(TEMA_ROOT)
OUTPUT = os.path.join(TEMA_ROOT, "output", "RCP_Adulto_VerbalizacionECOE.apkg")
IDS_PATH = os.path.join(REPO_ROOT, "ids.json")

DECK_ID = 1502938476
DECK_NAME = "RCP Adulto::Verbalización ECOE"

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

BASE_TAGS = ["verbalizacion", "rcp_adulto", "aha2025", "ecoe"]

CARDS = [
    # ──────────────────────────────────
    # BLOQUE A — Llegada y activación SEM (4)
    # ──────────────────────────────────
    {
        "text": 'Llegas y encuentras a un hombre colapsado en la vía pública. Antes de tocarlo, lo primero que verbalizas es: {{c1::"La escena es segura, procedo a evaluar al paciente."}}',
        "extra": "🎯 El sinodal evalúa que VERBALICES la seguridad antes de aproximarte. ❌ Error común: ir directo a sacudir al paciente. Si la escena no fuera segura: 'La escena no es segura por X, espero/llamo/me protejo'.",
        "tags": ["llegada", "activacion_sem"],
    },
    {
        "text": 'Llegas al paciente colapsado. Te arrodillas, lo sacudes por los hombros y dices con voz fuerte: {{c1::"Señor, ¿me escucha? Abra los ojos."}} No responde. Comunicas el hallazgo: {{c2::"Paciente inconsciente."}}',
        "extra": "🎯 Estímulo verbal ANTES del doloroso, y anuncio del hallazgo en voz alta. ❌ Error: empezar por frote esternal o saltarse la verbalización del nivel de consciencia.",
        "tags": ["avdi"],
    },
    {
        "text": 'Paciente confirmado inconsciente. Antes de cualquier otra maniobra, señalas a personas concretas del grupo y dices: {{c1::"Tú, el del suéter azul: llama al 911 y avisa que es un paro cardíaco. Tú, el de la camisa blanca: busca un DEA y tráelo."}}',
        "extra": "🎯 DELEGACIÓN DIRIGIDA: persona específica + orden específica + información concreta ('paro cardíaco'). ❌ Error: 'que alguien llame al 911' — el sinodal lo cuenta como activación fallida (difusión de responsabilidad).",
        "tags": ["activacion_sem", "delegacion"],
    },
    {
        "text": 'Tras activar el SEM y antes de tocar al paciente, anuncias en voz alta: {{c1::"Reviso pulso carotídeo y respiración simultáneamente, no más de 10 segundos."}}',
        "extra": "🎯 Verbalizar el 'simultáneo' y el límite de '≤10 segundos' — criterios AHA explícitos. ❌ Error: revisar pulso y respiración por separado o no acotar el tiempo.",
        "tags": ["bifurcacion"],
    },

    # ──────────────────────────────────
    # BLOQUE B — Bifurcación inicial (3)
    # ──────────────────────────────────
    {
        "text": 'A los 8 segundos detectas pulso carotídeo y respiración espontánea. Anuncias el resultado y el siguiente paso: {{c1::"Paciente con pulso y respira; procedo a valoración primaria ABCDE."}}',
        "extra": "🎯 Anunciar el resultado del chequeo y la transición al siguiente esquema. ❌ Error: quedarse callado y pasar al ABCDE sin verbalizar el cambio de marco.",
        "tags": ["bifurcacion", "abcde"],
    },
    {
        "text": 'Detectas pulso carotídeo pero NO respiración espontánea. Anuncias: {{c1::"Paciente con pulso pero no respira: paro respiratorio aislado. Inicio ventilaciones de rescate, una cada 6 segundos."}} Si hay sospecha de opioides añades: {{c2::"además administro naloxona IM/IN."}}',
        "extra": "🎯 Diagnóstico explícito ('paro respiratorio aislado') + conducta correcta (NO compresiones) + frecuencia. AHA 2025 incluyó naloxona en algoritmo BLS de legos. ❌ Error grave: iniciar compresiones a un paciente con pulso.",
        "tags": ["bifurcacion", "paro_respiratorio", "naloxona"],
    },
    {
        "text": 'A los 9 segundos: no hay pulso ni respiración. Anuncias el diagnóstico y la conducta: {{c1::"Paciente en paro cardiorrespiratorio. Inicio RCP de alta calidad: secuencia CAB, comenzando con compresiones."}}',
        "extra": "🎯 Nombrar el diagnóstico ('paro cardiorrespiratorio') y la secuencia (CAB) en voz alta. ❌ Error: empezar a comprimir en silencio sin verbalizar.",
        "tags": ["bifurcacion", "cab"],
    },

    # ──────────────────────────────────
    # BLOQUE C — ABCDE narrado paso a paso (6)
    # ──────────────────────────────────
    {
        "text": 'Tras confirmar pulso y respiración, antes de explorar al paciente anuncias el marco: {{c1::"Procedo a valoración primaria ABCDE."}}',
        "extra": "🎯 Nombrar la metodología ANTES de ejecutarla — estructura la actuación para el sinodal. ❌ Error: empezar a explorar sin nombrar el esquema.",
        "tags": ["abcde"],
    },
    {
        "text": 'Paso A del ABCDE. Verbalizas: {{c1::"A — vía aérea: permeable, sin cuerpos extraños, sin estridor ni gorgoteo."}}',
        "extra": "🎯 Nombrar lo que VES y lo que NO ves (negativos pertinentes: obstrucción, sangre, vómito). Si hubiera sospecha de trauma cervical: añadir 'mantengo alineación cervical, realizo tracción mandibular'.",
        "tags": ["abcde", "via_aerea"],
    },
    {
        "text": 'Paso B del ABCDE. Verbalizas: {{c1::"B — respiración: FR 16 por minuto, expansión torácica simétrica, saturación 97% al aire ambiente, auscultación con murmullo vesicular bilateral sin agregados."}}',
        "extra": "🎯 Los cuatro datos: FR + simetría + SatO2 + auscultación. ❌ Error: solo decir 'respira bien' — falta de granularidad.",
        "tags": ["abcde", "respiracion"],
    },
    {
        "text": 'Paso C del ABCDE. Verbalizas: {{c1::"C — circulación: FC 88, TA 124/78, llenado capilar 2 segundos, piel tibia y bien perfundida, pulsos periféricos presentes y simétricos."}}',
        "extra": "🎯 FC + TA + llenado capilar + piel/perfusión + pulsos. ❌ Error: omitir el llenado capilar — es el dato que más diferencia una exploración pulcra de una mediocre.",
        "tags": ["abcde", "circulacion"],
    },
    {
        "text": 'Paso D del ABCDE. Verbalizas: {{c1::"D — neurológico: Glasgow 15, pupilas isocóricas y reactivas a la luz, sin focalidad. Glucemia capilar 92 miligramos por decilitro."}}',
        "extra": "🎯 Glasgow + pupilas + glucemia capilar SIEMPRE ante alteración de consciencia. ❌ Error: olvidar la glucemia capilar.",
        "tags": ["abcde", "neurologico"],
    },
    {
        "text": 'Paso E del ABCDE. Verbalizas: {{c1::"E — exposición: desvisto al paciente buscando lesiones ocultas, reviso dorso movilizándolo en bloque, controlo hemorragias externas, mantengo temperatura con manta térmica."}}',
        "extra": "🎯 Cuatro acciones: desvestir + dorso en bloque + hemorragias + prevención de hipotermia. ❌ Error: levantar al paciente sin 'en bloque' o no cubrirlo tras revisar.",
        "tags": ["abcde", "exposicion"],
    },

    # ──────────────────────────────────
    # BLOQUE D — Durante la RCP (5)
    # ──────────────────────────────────
    {
        "text": 'Diagnosticado el paro, te colocas a un lado del paciente. Verbalizas la técnica mientras te posicionas: {{c1::"Talón de la mano sobre la mitad inferior del esternón, brazos rectos, comprimo perpendicular: 100 a 120 por minuto, profundidad 5 a 6 centímetros, permitiendo retroceso completo del tórax."}}',
        "extra": "🎯 Posición + frecuencia + profundidad + recoil en una sola verbalización demuestra dominio de los cinco elementos de RCP de alta calidad. ❌ Error: empezar a comprimir sin nombrar los parámetros.",
        "tags": ["compresiones", "rcp_calidad"],
    },
    {
        "text": 'Llega el DEA. Verbalizas la secuencia mientras lo operas: {{c1::"Enciendo el DEA, coloco parches en posición infraclavicular derecha y axilar media izquierda. ¡No toquen al paciente, análisis en curso! Descarga indicada: me aparto, descarga aplicada. Retomo RCP inmediatamente durante 2 minutos."}}',
        "extra": "🎯 Cada subpaso anunciado en voz alta protege al equipo y demuestra dominio. ❌ Error: aplicar la descarga sin advertir o no retomar RCP 'inmediatamente'.",
        "tags": ["dea"],
    },
    {
        "text": 'Han pasado 2 minutos de compresiones. Anuncias el cambio a tu compañero: {{c1::"Cambio de compresor en 3, 2, 1. Aprovecho el cambio para chequear ritmo en el monitor."}}',
        "extra": "🎯 Cambio cada 2 min + cuenta atrás para coordinación + chequeo de ritmo en la transición (minimiza pausa). Cambio rápido (< 5 s) para no caer la fracción de compresión. ❌ Error: dejar al mismo compresor más allá de 2 min por fatiga acumulada.",
        "tags": ["compresiones", "ciclo"],
    },
    {
        "text": 'Durante el segundo ciclo de RCP, sin detener compresiones, verbalizas al equipo el repaso sistemático de causas reversibles: {{c1::"Mientras mantenemos RCP, repaso causas reversibles. 5H: hipovolemia, hipoxia, hidrogeniones, hipo/hiperpotasemia, hipotermia. 5T: tóxicos, taponamiento, neumotórax a tensión, trombosis coronaria, trombosis pulmonar."}}',
        "extra": "🎯 Verbalizar el repaso enumerado demuestra que NO solo estás comprimiendo: estás pensando en el diferencial. ❌ Error: decir 'buscar causas reversibles' sin enumerarlas.",
        "tags": ["5h_5t"],
    },
    {
        "text": 'Tras intubar al paciente, anuncias el cambio de patrón ventilatorio: {{c1::"Vía aérea avanzada colocada: compresiones continuas sin pausa para ventilar, y una ventilación cada 6 segundos."}}',
        "extra": "🎯 Anunciar el cambio de ratio (30:2 → continuas + asincrónicas) es un punto que muchos olvidan y el sinodal busca activamente. ❌ Error: seguir 30:2 después de intubar.",
        "tags": ["ventilacion", "via_aerea_avanzada"],
    },

    # ──────────────────────────────────
    # BLOQUE E — Verbalización por causa reversible (9)
    # ──────────────────────────────────
    {
        "text": 'Durante la RCP recuerdas que el paciente venía con vómitos y diarrea profusa de 3 días. Verbalizas: "Sospecho {{c1::hipovolemia}} por contexto de pérdidas digestivas y llenado capilar lento previo. Administro {{c2::cristaloide en bolo 30 mL/kg}} y busco foco hemorrágico activo."',
        "extra": "🎯 Estructura tipo: 'sospecho X por dato Y, administro/hago Z'. El sinodal busca que NOMBRES el dato que apoya tu sospecha, no solo la sospecha aislada.",
        "tags": ["5h_5t", "hipovolemia"],
    },
    {
        "text": 'Antes del paro el paciente estaba cianótico con SatO2 78%. Verbalizas: "Sospecho {{c1::hipoxia}} como causa del paro por cianosis y desaturación previa. Optimizo {{c2::ventilación con BVM más reservorio al 100%}} y descarto obstrucción de vía aérea."',
        "extra": "🎯 Hipoxia es la causa más frecuente de AESP por bradicardia previa al paro. Manejarla ANTES de buscar otras causas. La verbalización debe transmitir esa prioridad.",
        "tags": ["5h_5t", "hipoxia"],
    },
    {
        "text": 'Paciente con IRC en diálisis, en monitor ves T picudas y QRS ancho. Verbalizas: "Sospecho {{c1::hiperpotasemia}} por insuficiencia renal y cambios electrocardiográficos. Administro {{c2::gluconato cálcico para estabilizar membrana, insulina con glucosa, salbutamol nebulizado}} y solicito {{c3::diálisis urgente}}."',
        "extra": "🎯 Orden correcto: Ca (estabiliza membrana) → insulina+glucosa → β2-agonista → diálisis. Nombrar el porqué del calcio ('estabiliza membrana') es nivel pulcro. ❌ Error frecuente: empezar por bicarbonato.",
        "tags": ["5h_5t", "hiperpotasemia"],
    },
    {
        "text": 'Paciente rescatado de aguas frías, temperatura central 28 °C. Verbalizas: "Hipotermia profunda: {{c1::limito a un máximo de 3 descargas hasta calentar al paciente, espacio la adrenalina}} e inicio {{c2::recalentamiento extracorpóreo}}. Mantengo RCP prolongada — no se está muerto hasta que se está caliente y muerto."',
        "extra": "🎯 El aforismo final ('caliente y muerto') es clásico y el sinodal lo aprecia como señal de dominio. Por debajo de 30 °C el miocardio es refractario a fármacos y desfibrilación.",
        "tags": ["5h_5t", "hipotermia"],
    },
    {
        "text": 'Joven encontrado inconsciente, pupilas puntiformes, jeringa en el suelo, frecuencia respiratoria 4 por minuto. Verbalizas: "Sospecho {{c1::intoxicación por opioides}} por miosis, hipoventilación y contexto. Administro {{c2::naloxona 0.4 a 2 miligramos IM o intranasal, repito cada 2 a 3 minutos hasta un máximo de 10 miligramos}} mientras ventilo con BVM."',
        "extra": "🎯 AHA 2025: naloxona ya está en el algoritmo BLS de legos. Nombrar la dosis y la vía te diferencia del estudiante que solo dice 'naloxona'.",
        "tags": ["5h_5t", "toxicos", "opioides"],
    },
    {
        "text": 'Paciente post-IAM con hipotensión, ingurgitación yugular y ruidos cardíacos apagados. Verbalizas: "{{c1::Tríada de Beck}}: sospecho {{c2::taponamiento cardíaco}}. Solicito eco bedside y procedo a {{c3::pericardiocentesis subxifoidea guiada por eco}}."',
        "extra": "🎯 Nombrar la tríada por su epónimo ('Beck') + eco antes de pinchar. ❌ Error: pericardiocentesis a ciegas si hay eco disponible.",
        "tags": ["5h_5t", "taponamiento"],
    },
    {
        "text": 'Paciente con trauma torácico cerrado. En B detectas hipoventilación e hiperresonancia izquierda; en C ves desviación traqueal a la derecha e ingurgitación yugular. Verbalizas: "Sospecho {{c1::neumotórax a tensión izquierdo}}. Realizo {{c2::descompresión con aguja en 4.º o 5.º espacio intercostal línea axilar anterior}}, seguida de {{c3::tubo torácico}} definitivo."',
        "extra": "🎯 AHA/ATLS actual prefiere 4.º-5.º EIC línea axilar anterior sobre el clásico 2.º EIC medioclavicular (mayor tasa de éxito, menor riesgo de lesión vascular).",
        "tags": ["5h_5t", "neumotorax"],
    },
    {
        "text": 'FV en monitor. El paciente tenía dolor torácico opresivo previo al colapso y factores de riesgo cardiovascular. Verbalizas: "Sospecho {{c1::trombosis coronaria como causa del paro}}. Mantengo desfibrilación y RCP de alta calidad. Mientras tanto, activo {{c2::laboratorio de hemodinamia para ICP urgente con objetivo puerta-balón menor o igual a 90 minutos}}."',
        "extra": "🎯 Activar hemodinamia DURANTE la RCP, no esperar al RCE. La verbalización debe transmitir paralelismo de acciones. ❌ Error: esperar al traslado para activar hemodinamia.",
        "tags": ["5h_5t", "iam"],
    },
    {
        "text": 'Postoperatorio reciente de cirugía abdominal, disnea súbita previa al colapso, AESP en monitor, eco bedside muestra dilatación de ventrículo derecho. Verbalizas: "Sospecho {{c1::TEP masivo}} por contexto postoperatorio, AESP e imagen ecocardiográfica de sobrecarga derecha. Administro {{c2::trombólisis sistémica empírica con alteplasa}} y prolongo RCP {{c3::al menos 60 a 90 minutos}} tras la administración."',
        "extra": "🎯 La RCP PROLONGADA post-trombólisis es la diferencia clínica clave que el sinodal busca. ❌ Error frecuente: dar alteplasa y parar a los 20 minutos.",
        "tags": ["5h_5t", "tep"],
    },

    # ──────────────────────────────────
    # BLOQUE F — Transiciones y cierre (3)
    # ──────────────────────────────────
    {
        "text": 'Durante el chequeo de ritmo del cuarto ciclo, detectas pulso carotídeo y el ETCO2 sube súbitamente de 14 a 38 mmHg. Verbalizas: {{c1::"Confirmo retorno de circulación espontánea con pulso carotídeo presente y elevación súbita de ETCO2. Suspendo compresiones y paso a valoración ABCDE post-paro."}}',
        "extra": "🎯 Confirmar RCE con DOS datos (pulso + ETCO2, o pulso + TA). La elevación súbita de ETCO2 > 35-40 mmHg es el signo más precoz y específico. ❌ Error: parar al primer pulso percibido sin confirmar con un segundo dato.",
        "tags": ["post_paro", "rce"],
    },
    {
        "text": 'Llevan 30 minutos de RCP sin RCE, ritmo persistente en asistolia, ETCO2 sostenido < 10 mmHg, sin causa reversible identificada. Verbalizas al equipo: {{c1::"Repasamos criterios de terminación: asistolia persistente, ETCO2 menor a 10 sostenido, sin causa reversible identificada tras revisión sistemática de 5H y 5T. Propongo dar por terminada la reanimación. ¿Acuerdo del equipo?"}}',
        "extra": "🎯 Tres criterios juntos: ritmo no desfibrilable persistente + ETCO2 bajo sostenido + sin causa reversible. Decisión CONSENSUADA con el equipo, no unilateral. ❌ Error: detener RCP sin verbalizar criterios ni buscar consenso.",
        "tags": ["terminacion"],
    },
    {
        "text": 'Llega la ambulancia avanzada con el paciente recuperado tras RCE. Entregas usando la estructura {{c1::SBAR — Situación, Background, Assessment, Recomendación}}: "Varón 58 años, paro presenciado por FV hace 18 minutos, 2 descargas y 2 mg de adrenalina administrados, RCE hace 4 minutos. Glasgow 6, intubado y ventilado, TA 92/60, sospecha alta de IAM como causa. Recomendación: traslado directo a hemodinamia."',
        "extra": "🎯 NOMBRAR la estructura SBAR antes del relato la organiza para el equipo receptor y demuestra dominio. ❌ Error: relato cronológico desordenado sin marco.",
        "tags": ["handover", "post_paro"],
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
