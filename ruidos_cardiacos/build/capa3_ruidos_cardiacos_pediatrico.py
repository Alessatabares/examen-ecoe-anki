"""
Ruidos Cardiacos Pediátrico — Capa 3 (Ejes transversales)
Guías: AHA scientific statements (cardiopatías congénitas, Jones 2015)
Output: output/Ruidos_Cardiacos_Pediatrico_Capa3.apkg
"""
import os
import json
import genanki

TEMA_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPO_ROOT = os.path.dirname(TEMA_ROOT)
OUTPUT = os.path.join(TEMA_ROOT, "output", "Ruidos_Cardiacos_Pediatrico_Capa3.apkg")
IDS_PATH = os.path.join(REPO_ROOT, "ids.json")

DECK_ID = 1406304186
DECK_NAME = "Ruidos Cardiacos Pediátrico::Capa 3 - Ejes"

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

BASE_TAGS = ["capa3", "ruidos_cardiacos_pediatrico", "aha", "ecoe"]

CARDS = [
    # Bloque A — Soplo inocente
    {
        "text": "**Soplo inocente** — fisiopato: {{c1::turbulencia funcional en corazón sano}}. Presentación: sistólico ≤2/6, musical/vibratorio, asintomático. Pista clínica: cambia con la postura, S2 normal, sin frémito ni irradiación. Manejo: {{c2::tranquilización familiar, sin ecocardiograma ni restricción de actividad}}.",
        "extra": '🗣️ ECOE: "Soplo de baja intensidad, sin frémito, sin irradiación, que cambia con la postura, S2 normal, niño asintomático sin antecedentes — compatible con soplo inocente, no requiere estudios adicionales."',
        "tags": ["inocente"],
    },
    {
        "text": "**Soplo inocente** — anamnesis ECOE para descartar patología: confirmar {{c1::ausencia de fatiga al comer, falla para crecer, cianosis, antecedente familiar de cardiopatía o muerte súbita}}. Maniobra dinámica clave: {{c2::cambio del soplo con sedestación/decúbito}}.",
        "extra": '🗣️ ECOE: "Pregunto por fatiga al lactar, sudoración con la alimentación, cianosis y antecedentes familiares de cardiopatía. Después ausculto en decúbito y sentado — si el soplo se modifica, refuerza la hipótesis de inocente."',
        "tags": ["inocente", "anamnesis"],
    },

    # Bloque B — CIV
    {
        "text": "**CIV** — fisiopato: shunt {{c1::VI→VD}} por gradiente sistólico VI≫VD. Tamaño = hemodinámia: pequeña → asintomática; grande → {{c2::hiperflujo pulmonar + insuficiencia cardiaca + retraso pondoestatural}}.",
        "extra": "El gradiente VI-VD es constante toda la sístole, por eso el soplo es holosistólico plano. La presión del VI siempre supera la del VD mientras no haya hipertensión pulmonar avanzada.",
        "tags": ["civ"],
    },
    {
        "text": "**CIV** — presentación por edad: en neonato puede ser silente (resistencias pulmonares altas); aparece soplo hacia las {{c1::4-6 semanas}} cuando bajan las resistencias pulmonares. Pista clínica: {{c2::holosistólico en BEII + frémito + falla para crecer}}.",
        "extra": '🗣️ ECOE: "Niño de 6 semanas con falla para crecer, diaforesis al comer y soplo holosistólico con frémito en borde esternal inferior izquierdo — sospecho CIV mediana o grande, solicito ecocardiograma."',
        "tags": ["civ", "presentacion"],
    },
    {
        "text": "**CIV** — manejo: pequeña Qp/Qs &lt;1.5 → {{c1::observación, cierre espontáneo frecuente}}. Mediana-grande Qp/Qs ≥1.5 → {{c2::diuréticos + IECA + soporte nutricional + cierre quirúrgico o percutáneo}}. Sin cierre → riesgo de {{c3::síndrome de Eisenmenger}}.",
        "extra": "Eisenmenger = inversión del shunt (D→I) por hipertensión pulmonar irreversible. Contraindica el cierre quirúrgico. Por eso la oportunidad terapéutica está antes de que la HTP se haga irreversible.",
        "tags": ["civ", "manejo"],
    },

    # Bloque C — PCA
    {
        "text": "**PCA** — fisiopato: persistencia del conducto arterioso &gt;48-72h. Shunt I→D (aorta→pulmonar) en sístole y diástole → soplo {{c1::continuo en maquinaria}} + {{c2::pulsos saltones}} (presión de pulso amplia).",
        "extra": "Los pulsos saltones (Corrigan-like) se explican porque la diástole pierde volumen hacia la pulmonar → presión diastólica baja, sistólica conservada → presión de pulso amplia.",
        "tags": ["pca"],
    },
    {
        "text": "**PCA** — presentación: en prematuro → {{c1::dificultad respiratoria, dependencia ventilatoria}}; en niño/adulto → silente hasta dilatación de cavidades izquierdas o hipertensión pulmonar.",
        "extra": '🗣️ ECOE: "En prematuro de 28 semanas con dependencia ventilatoria y soplo continuo en infraclavicular izquierdo — sospecho PCA hemodinámicamente significativo."',
        "tags": ["pca", "presentacion"],
    },
    {
        "text": "**PCA** — manejo: prematuro → {{c1::indometacina o ibuprofeno (inhiben prostaglandinas que mantienen el ductus abierto)}}. Niño/adulto → {{c2::cierre percutáneo con dispositivo (Amplatzer)}}. Si Eisenmenger → cierre {{c3::contraindicado}}.",
        "extra": "Contraindicaciones a indometacina/ibuprofeno: enterocolitis necrotizante, hemorragia activa, insuficiencia renal, trombocitopenia. Paracetamol emerge como alternativa.",
        "tags": ["pca", "manejo"],
    },

    # Bloque D — Estenosis pulmonar
    {
        "text": "**Estenosis pulmonar** — fisiopato y presentación: obstrucción al tracto de salida del VD → {{c1::hipertrofia compensatoria del VD}}. Mayoría asintomática hasta gradiente moderado-severo, luego {{c2::disnea de esfuerzo, dolor torácico, síncope}}.",
        "extra": "Click eyectivo precede al soplo crescendo-decrescendo en foco pulmonar. Irradia a espalda. Cuanto más severa, más se separa el click de S1.",
        "tags": ["estenosis_pulmonar"],
    },
    {
        "text": "**EP** — manejo: {{c1::valvuloplastia con balón}} si gradiente pico &gt;40 mmHg en sintomático o &gt;60 mmHg en asintomático. Tasa de éxito &gt;90%.",
        "extra": '🗣️ ECOE: "Paciente con EP severa (gradiente pico 70 mmHg) sintomático con síncope de esfuerzo — propongo valvuloplastia pulmonar con balón como primera línea."',
        "tags": ["estenosis_pulmonar", "manejo"],
    },

    # Bloque E — Fiebre reumática
    {
        "text": "**Fiebre reumática** — fisiopato: respuesta autoinmune cruzada ({{c1::mimicry molecular}}) 2-3 semanas post-faringitis por {{c2::Streptococcus pyogenes (grupo A beta-hemolítico)}}. El daño valvular crónico define el pronóstico.",
        "extra": "La fiebre reumática es prevenible: tratar la faringitis estreptocócica con penicilina (10 días) reduce el riesgo a casi cero. Por eso el dato de faringitis no tratada es clave.",
        "tags": ["fiebre_reumatica"],
    },
    {
        "text": "**FR** — presentación: aplicación clínica de Jones 2015. La valvulopatía aguda más frecuente es {{c1::insuficiencia mitral}} (holosistólico ápex, irradia a axila); la {{c2::estenosis mitral}} aparece años después como secuela crónica.",
        "extra": '🗣️ ECOE: "Niño de 10 años con artritis migratoria, fiebre y soplo nuevo de insuficiencia mitral 3 semanas después de faringitis — sospecho fiebre reumática aguda, solicito ASLO, ECG, ecocardiograma."',
        "tags": ["fiebre_reumatica", "presentacion"],
    },
    {
        "text": "**FR** — profilaxis secundaria: {{c1::penicilina G benzatínica IM cada 21-28 días}}. Duración: 5 años o hasta los 21 (sin carditis), {{c2::10 años o hasta los 21 (con carditis sin secuela)}}, **de por vida** si {{c3::valvulopatía residual}}.",
        "extra": "Alternativa si alergia a penicilina: eritromicina o azitromicina oral diaria. La adherencia es el mayor reto — preferir benzatínica IM mensual cuando sea posible.",
        "tags": ["fiebre_reumatica", "profilaxis"],
    },

    # Bloque F — MCH pediátrica
    {
        "text": "**MCH** — fisiopato: hipertrofia ventricular sin causa secundaria + obstrucción dinámica del TSVI por {{c1::SAM (movimiento sistólico anterior de la mitral)}}. Origen: {{c2::genético autosómico dominante (mutaciones en sarcómeros)}}.",
        "extra": "Las mutaciones más comunes están en MYH7 (cadena pesada de la miosina) y MYBPC3 (proteína C ligadora de miosina). Penetrancia variable, por eso pueden saltarse generaciones.",
        "tags": ["mch"],
    },
    {
        "text": "**MCH** — presentación pediátrica: frecuentemente asintomática; pueden aparecer disnea, dolor torácico, síncope con esfuerzo, o {{c1::muerte súbita en deportista}}. Anamnesis crítica: {{c2::antecedente familiar de muerte súbita &lt;50 años}}.",
        "extra": '🗣️ ECOE: "Adolescente con síncope durante ejercicio + tío fallecido súbitamente a los 32 años + soplo sistólico en BEI que aumenta con Valsalva — sospecho MCH, restrinjo actividad y solicito ecocardiograma + ECG + estudio familiar."',
        "tags": ["mch", "presentacion", "banderas_rojas"],
    },
    {
        "text": "**MCH** — manejo: {{c1::betabloqueador o calcioantagonista no-DHP (verapamilo)}} para reducir contractilidad y gradiente. **Restricción de deportes competitivos**. DAI implantable si {{c2::alto riesgo: síncope inexplicado, antecedente familiar de muerte súbita, grosor septal masivo, TVNS}}.",
        "extra": "Contraindicaciones en MCH obstructiva: digoxina, nitratos, vasodilatadores e inotrópicos positivos — todos empeoran la obstrucción dinámica.",
        "tags": ["mch", "manejo"],
    },

    # Bloque G — Tetralogía de Fallot
    {
        "text": "**Fallot** — fisiopato: 4 defectos (CIV grande, cabalgamiento aórtico, obstrucción RVOT, hipertrofia VD). Cianosis depende del grado de obstrucción RVOT: más obstrucción → más shunt {{c1::D→I por la CIV}} → más cianosis.",
        "extra": "Por eso Fallot es 'cianótica con flujo pulmonar disminuido'. Otras cianóticas con flujo aumentado (TGA, drenaje venoso anómalo) tienen mecanismo distinto.",
        "tags": ["fallot"],
    },
    {
        "text": "**Fallot** — crisis hipoxémica (\"tet spell\"): cianosis aguda por aumento del shunt D→I ({{c1::espasmo infundibular o caída de las resistencias sistémicas}}). Pista clínica: {{c2::niño llorando o esforzándose que se torna intensamente cianótico, irritable, luego letárgico}}.",
        "extra": '🗣️ ECOE: "Lactante con cianosis aguda durante el llanto, irritable, después letárgico — alta sospecha de crisis hipoxémica de Fallot, manejo inmediato sin esperar estudios."',
        "tags": ["fallot", "crisis_hipoxemica"],
    },
    {
        "text": "**Fallot** — manejo agudo de crisis: {{c1::posición genupectoral (rodillas al pecho, ↑ resistencia sistémica)}}, oxígeno 100%, {{c2::morfina (relaja infundíbulo)}}, bolo de líquidos, betabloqueador, fenilefrina si refractario. Definitivo: {{c3::corrección quirúrgica entre 3-6 meses}}.",
        "extra": "Lo que NO se debe dar: inotrópicos positivos (empeoran el espasmo infundibular) ni vasodilatadores (caen las resistencias sistémicas y aumenta el shunt D→I).",
        "tags": ["fallot", "manejo"],
    },

    # Bloque H — CIA
    {
        "text": "**CIA** — fisiopato y presentación: shunt I→D (AI→AD) por gradiente bajo entre aurículas → sobrecarga de volumen del VD → {{c1::S2 desdoblado fijo}}. Presentación: {{c2::tardía (4-5 años o adulto joven)}}, frecuentemente asintomática hasta dilatación derecha o hipertensión pulmonar.",
        "extra": "El S2 desdoblado fijo es patognomónico porque el volumen del VD es similar en inspiración y espiración (el shunt I→D iguala el llenado).",
        "tags": ["cia"],
    },
    {
        "text": "**CIA** — manejo: cierre si Qp/Qs &gt;1.5 con dilatación derecha. Ostium secundum → {{c1::cierre percutáneo (Amplatzer)}}. Ostium primum y seno venoso → {{c2::cirugía}}. Sin cierre → riesgo de {{c3::fibrilación auricular y embolia paradójica}} en adulto.",
        "extra": '🗣️ ECOE: "Adulto joven con disnea de esfuerzo, S2 desdoblado fijo y dilatación de cavidades derechas en eco — propongo cierre percutáneo de CIA tipo ostium secundum."',
        "tags": ["cia", "manejo"],
    },

    # Bloque I — Anamnesis dirigida + maniobras
    {
        "text": "**Anamnesis dirigida ECOE pediátrica** — preguntas obligadas: {{c1::fatiga al comer/lactar, diaforesis con la alimentación, infecciones respiratorias recurrentes, falla para crecer, cianosis perioral o con esfuerzo, antecedente familiar de muerte súbita o cardiopatía congénita, prematuridad, síndromes genéticos (Down → canal AV, DiGeorge → Fallot, Turner → coartación)}}.",
        "extra": '🗣️ ECOE: "Antes de auscultar, pregunto cómo come el niño, si suda, si tiene infecciones respiratorias frecuentes, si crece bien, si se pone azul, y por antecedentes familiares de cardiopatía o muerte súbita."',
        "tags": ["anamnesis"],
    },
    {
        "text": "**Maniobras dinámicas — resumen aplicado**: Valsalva ↓ retorno → ↓ todos los soplos salvo {{c1::MCH y prolapso mitral (aumentan)}}. Sentadilla o handgrip ↑ retorno/postcarga → {{c2::↑ IM, IAo, CIV}}. Rivero-Carvallo (inspiración) → {{c3::↑ soplos derechos (IT, EP)}}.",
        "extra": '🗣️ ECOE: "Para confirmar la hipótesis pediré al paciente que haga la maniobra X — espero que el soplo se modifique de la manera Y. Si efectivamente cambia así, refuerza el diagnóstico."',
        "tags": ["maniobras"],
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
