"""
Ruidos Cardiacos Pediátrico — Verbalización ECOE
Subdeck paralelo orientado a entrenar qué decir al sinodal en estación
de auscultación cardiovascular pediátrica.
Guías: AHA Jones 2015 (FR) + screening neonatal con pulsioximetría +
cardiopatías congénitas (AHA scientific statements).
Output: output/Ruidos_Cardiacos_Pediatrico_VerbalizacionECOE.apkg
"""
import os
import json
import genanki

TEMA_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPO_ROOT = os.path.dirname(TEMA_ROOT)
OUTPUT = os.path.join(TEMA_ROOT, "output", "Ruidos_Cardiacos_Pediatrico_VerbalizacionECOE.apkg")
IDS_PATH = os.path.join(REPO_ROOT, "ids.json")

DECK_ID = 1746203185
DECK_NAME = "Ruidos Cardiacos Pediátrico::Verbalización ECOE"

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

BASE_TAGS = ["verbalizacion", "ruidos_cardiacos_pediatrico", "aha", "ecoe"]

CARDS = [
    # ────────────────────────────────────
    # BLOQUE A — Apertura pediátrica (5)
    # ────────────────────────────────────
    {
        "text": 'Entras a la sala con padres y niño. Saludas a ambos: {{c1::"Buenos días, soy [tu nombre], médico/estudiante de medicina. ¿Son los padres del/de la [nombre del niño/a]?"}} Te diriges al niño a su altura: {{c2::"Hola [nombre], voy a escucharte el corazoncito, ¿está bien?"}}',
        "extra": "🎯 Doble comunicación: padres + niño en su nivel. Para niños mayores, hablar con ellos directamente sobre la maniobra. ❌ Error: ignorar al niño y hablar solo con los padres.",
        "tags": ["apertura"],
    },
    {
        "text": 'Anamnesis perinatal a los padres: {{c1::"¿Cómo fue el embarazo y el parto? ¿Cuánto pesó al nacer? ¿Tuvo problemas al nacer (necesitó oxígeno, UCIN, ictericia, hipoglucemia)? ¿Le hicieron el screening neonatal con pulsioximetría?"}}',
        "extra": "🎯 Antecedentes perinatales = clave en cardiopatías congénitas. El screening neonatal con oximetría es obligatorio en muchos países. ❌ Error: usar la anamnesis adulta genérica en lactante.",
        "tags": ["anamnesis"],
    },
    {
        "text": 'Anamnesis del lactante/niño dirigida a síntomas de ICC pediátrica: {{c1::"¿Se cansa al alimentarse o suda mucho mientras lo amamantan? ¿Tiene cianosis (se pone azul) cuando llora o se alimenta? ¿Tiene infecciones respiratorias frecuentes? ¿Cómo está su peso y talla respecto a las curvas de crecimiento?"}}',
        "extra": "🎯 Síntomas de ICC en lactante: cansancio con tomas + sudoración + IRA recurrentes + falla de medro. Diferentes del adulto. Cianosis con llanto = shunt. ❌ Error: usar criterios de adulto (disnea de esfuerzo) en lactante.",
        "tags": ["anamnesis", "icc_pediatrica"],
    },
    {
        "text": 'Antecedentes adicionales: {{c1::"¿Algún familiar con cardiopatía congénita, miocardiopatía, muerte súbita o síncope inexplicado? ¿Faringitis estreptocócicas recientes? ¿Está al día con las vacunas?"}}',
        "extra": "🎯 Faringitis estreptocócica reciente + clínica articular/cardíaca = fiebre reumática. Antecedente familiar de muerte súbita = considerar MHO o canalopatías. ❌ Error: omitir antecedente de faringitis (trampa Jones 2015).",
        "tags": ["antecedentes"],
    },
    {
        "text": 'Higiene + consentimiento + tranquilizar: {{c1::"Me lavo las manos y limpio el estetoscopio. (A los padres) Le voy a auscultar el corazón. Necesito que esté tranquilo para oír bien. (Al niño según edad) Mira, esto es un fonendoscopio, ¿quieres tocarlo? No duele, sólo es frío."}}',
        "extra": "🎯 Triple comunicación: higiene + permiso a padres + tranquilizar al niño. Niño llorando = auscultación inútil. ❌ Error: forzar al niño = exploración inválida.",
        "tags": ["higiene", "consentimiento"],
    },

    # ────────────────────────────────────
    # BLOQUE B — Inspección + palpación (4)
    # ────────────────────────────────────
    {
        "text": 'Inspección de facies y morfología — pista anchor: {{c1::"Inspecciono facies y rasgos buscando síndromes asociados a cardiopatía: rasgos de Down (CIV, canal AV), Williams (estenosis aórtica supravalvular), Marfan (dilatación aórtica), Turner (coartación), Noonan (estenosis pulmonar valvular)."}}',
        "extra": "🎯 Reconocer facies dismórficas = pista diagnóstica directa. ❌ Error: omitir la inspección morfológica = pierdes el síndrome que orienta al defecto.",
        "tags": ["inspeccion", "facies"],
    },
    {
        "text": 'Color, nutrición y acropaquia: {{c1::"Evalúo color (cianosis central peribucal o ungueal, palidez, ictericia), estado nutricional con percentiles de peso/talla (falla de medro como signo de ICC), dedos en palillo de tambor (acropaquia, marcador de hipoxemia crónica)."}}',
        "extra": "🎯 Cianosis central + acropaquia + falla de medro = sospecha cardiopatía cianótica. ❌ Error: no desvestir al niño completo o no buscar acropaquia.",
        "tags": ["inspeccion", "cianosis"],
    },
    {
        "text": 'Maniobra crítica en pediatría — palpación de pulsos en 4 extremidades: {{c1::"Palpo pulsos radial y femoral SIMULTÁNEAMENTE en ambos lados, comparándolos. Sin asimetría ni retraso radio-femoral."}} Si los pulsos femorales son débiles/ausentes o hay retraso → {{c2::sospecha de coartación de aorta hasta que se demuestre lo contrario}}.',
        "extra": "🎯 Pulsos en 4 extremidades = OBLIGATORIO en pediatría. Detecta coartación. ❌ Error: solo tomar pulso radial = pierdes la coartación.",
        "tags": ["palpacion", "pulsos", "coartacion"],
    },
    {
        "text": 'Palpación cardíaca + abdomen: {{c1::"Palpo el choque de la punta (en lactante es más alto, 4.º EIC LMC). Busco frémito en focos cardíacos. Palpo el abdomen — la hepatomegalia es signo PRECOZ de insuficiencia cardíaca pediátrica."}}',
        "extra": "🎯 Hepatomegalia en lactante con disnea/cansancio = ICC hasta descarte. Diferencia clave con adulto (ICC adulta se manifiesta más con edema pulmonar). ❌ Error: no palpar hígado.",
        "tags": ["palpacion", "hepatomegalia"],
    },

    # ────────────────────────────────────
    # BLOQUE C — Técnica de auscultación (3)
    # ────────────────────────────────────
    {
        "text": 'Para una auscultación válida en pediatría: {{c1::"Necesito al niño tranquilo. Si es lactante, puede estar en brazos del padre/madre durante la auscultación. Si llora o se mueve, la auscultación no es fiable — interrumpo y reintento cuando se calme, o uso distractores."}}',
        "extra": "🎯 Auscultar a niño llorando = inútil. La habilidad ECOE es reconocerlo y replantear. ❌ Error: intentar oír con niño llorando y dar diagnóstico.",
        "tags": ["tecnica"],
    },
    {
        "text": 'Ruidos fisiológicos del niño difieren del adulto: {{c1::"FC normal varía por edad: lactante 100-160, preescolar 80-120, escolar 70-110. Pueden tener arritmia sinusal respiratoria (FC aumenta con inspiración y disminuye con espiración) que es FISIOLÓGICA."}}',
        "extra": "🎯 Taquicardia 'fisiológica' en lactante es normal. Bradicardia <80 en lactante = anormal. Arritmia sinusal respiratoria = totalmente normal. ❌ Error: alarmarse por FC 140 en lactante sano.",
        "tags": ["tecnica", "ruidos_normales"],
    },
    {
        "text": 'Desdoblamiento de S2 — distinción crítica: {{c1::"Desdoblamiento fisiológico de S2: con la inspiración, el retorno venoso aumentado al VD retrasa el cierre pulmonar → S2 se desdobla. Con espiración se vuelve único."}} Si el desdoblamiento es {{c2::FIJO (no varía con respiración)}} → sospecho {{c3::CIA hasta que se demuestre lo contrario}}.',
        "extra": "🎯 S2 desdoblado FIJO = signo cardinal de CIA. Es la pista clínica directa que puede ser la única alteración detectable. ❌ Error: confundir desdoblamiento fisiológico (varía con respiración) con fijo.",
        "tags": ["s2", "cia"],
    },

    # ────────────────────────────────────
    # BLOQUE D — Soplo inocente vs patológico (5)
    # ────────────────────────────────────
    {
        "text": 'Los 7 criterios del soplo INOCENTE (regla de las 7 "S"): {{c1::"Sistólico (nunca diastólico ni continuo), Suave (≤2/6, sin frémito), Sin irradiación, Sin click ni galope asociado, Sin clínica cardiovascular, Sensitivo a posición (varía con maniobras), S2 normal con desdoblamiento fisiológico."}}',
        "extra": "🎯 Si cumple los 7 → inocente. Si falla 1 → derivar a cardiología pediátrica. ❌ Error: diagnosticar 'soplo inocente' sin demostrar los 7 criterios.",
        "tags": ["soplo_inocente"],
    },
    {
        "text": 'Soplo de Still (el más común en niños 3-7 años): {{c1::"Soplo musical, vibratorio (algunos lo describen como cuerda vibrando), en foco mesocárdico (entre paraesternal inferior y ápex), intensidad 1-2/6, varía con posición — disminuye en bipedestación, aumenta en supino."}} Es {{c2::completamente inocente, no requiere estudios cardiológicos}}.',
        "extra": "🎯 Nombrar el epónimo (Still) = nivel pulcro. Es el soplo benigno más frecuente del escolar. ❌ Error: derivar a cardiología por un Still típico.",
        "tags": ["soplo_inocente", "still"],
    },
    {
        "text": 'Otros soplos inocentes pediátricos a conocer: {{c1::"Soplo vibratorio musical (= Still). Soplo de eyección pulmonar fisiológico en 2.º EIC izquierdo, suave, sin irradiación, aumenta en supino o hiperdinamia (anemia, ejercicio, fiebre). Hum venoso (continuo, subclavicular, desaparece girando la cabeza o en supino)."}}',
        "extra": "🎯 Lista corta de soplos benignos. Conocerlos evita derivaciones innecesarias.",
        "tags": ["soplo_inocente"],
    },
    {
        "text": 'Criterios de soplo PATOLÓGICO (cualquiera = derivar): {{c1::"Diastólico o continuo (excepto hum venoso clásico), holosistólico, intensidad ≥3/6 o con frémito palpable, con irradiación, asociado a click eyectivo o galope, con clínica (cianosis, falla de medro, disnea), o con S2 anormal (desdoblamiento fijo, S2 único, P2 reforzado)."}}',
        "extra": "🎯 La 'imagen espejo' del soplo inocente. ❌ Error grave: oír un soplo y declarar 'inocente' sin chequear cada criterio — puede ocultar una cardiopatía congénita.",
        "tags": ["soplo_patologico"],
    },
    {
        "text": 'Indicaciones de ECOCARDIOGRAMA pediátrico: {{c1::"Soplo patológico (cualquier criterio anterior), cianosis, falla de medro, ICC clínica, síndrome conocido con riesgo cardíaco (Down, Marfan, Williams, Turner, Noonan), antecedente familiar de cardiopatía congénita o muerte súbita."}}',
        "extra": "🎯 Saber cuándo SÍ pedir eco = balance entre sobre-estudios y subdiagnóstico. ❌ Error: pedir eco a todo soplo (saturación de servicios) o a ninguno (subdiagnóstico).",
        "tags": ["estudios", "ecocardiograma"],
    },

    # ────────────────────────────────────
    # BLOQUE E — Cardiopatías congénitas (6)
    # ────────────────────────────────────
    {
        "text": 'Lactante con fatiga al comer, soplo holosistólico paraesternal izquierdo bajo con frémito, S2 normal. Verbalizas: "Soplo {{c1::holosistólico (plano) paraesternal izquierdo bajo (3.er-4.º EIC), intensidad 3-4/6 con frémito palpable}}, S2 normal. Compatible con {{c2::comunicación interventricular (CIV)}}. Solicito {{c3::ecocardiograma para tamaño y repercusión hemodinámica, plus radiografía de tórax y ECG}}."',
        "extra": "🎯 CIV es la cardiopatía congénita acianótica más común. Las pequeñas pueden cerrar solas; las grandes van a cirugía. ❌ Error: confundir con IM (esta tiene irradiación a axila).",
        "tags": ["civ"],
    },
    {
        "text": 'Niño en consulta rutinaria, asintomático, soplo sistólico de eyección pulmonar + S2 con DESDOBLAMIENTO FIJO. Verbalizas: "Soplo {{c1::sistólico de eyección, foco pulmonar (2.º EIC izq), intensidad 2-3/6, suave}}, con S2 desdoblado FIJO que no varía con la respiración. Compatible con {{c2::comunicación interauricular (CIA)}}. Solicito {{c3::ecocardiograma}}."',
        "extra": "🎯 S2 desdoblado FIJO es PATOGNOMÓNICO de CIA. Suele ser la única pista clínica (CIA es muchas veces asintomática hasta la adolescencia). ❌ Error: confundir el desdoblamiento fisiológico (varía con respiración) con el fijo.",
        "tags": ["cia"],
    },
    {
        "text": 'Lactante con soplo CONTINUO en región subclavicular izquierda, "en maquinaria", con falla de medro o cianosis. Verbalizas: "Soplo {{c1::CONTINUO en maquinaria, máximo en región subclavicular o infraclavicular izquierda}}, que abarca sístole y diástole sin interrupción. Compatible con {{c2::ductus arterioso persistente (DAP)}}. Solicito {{c3::ecocardiograma; en pretérmino → indometacina o ibuprofeno; en término sintomático → cierre percutáneo o quirúrgico}}."',
        "extra": "🎯 ÚNICO soplo CONTINUO patológico habitual en pediatría. ❌ Error: no identificar el patrón continuo y catalogarlo como hum venoso.",
        "tags": ["dap"],
    },
    {
        "text": 'Lactante con cianosis y crisis hipoxémicas (espasmos cianóticos), soplo sistólico de eyección en foco pulmonar. Verbalizas: "Cianosis central + soplo {{c1::sistólico de eyección, foco pulmonar (más fuerte cuanto más severa la EP infundibular)}}. Compatible con {{c2::tetralogía de Fallot (4 anomalías: estenosis pulmonar infundibular + CIV + cabalgamiento aórtico + hipertrofia VD)}}. Manejo de crisis hipoxémica: {{c3::posición genu-pectoral (knees-to-chest), oxígeno al 100%, morfina IM/IV, propranolol IV, expansión volémica}}."',
        "extra": "🎯 La posición de knees-to-chest aumenta RVS, disminuye shunt der-izq, mejora hipoxia. Recordar las 4 anomalías por nombre = nivel pulcro.",
        "tags": ["fallot"],
    },
    {
        "text": 'Niño con HTA en miembros superiores + pulsos femorales débiles + soplo sistólico en espalda. Verbalizas: "Hallazgo: {{c1::HTA en miembros superiores con TA en miembros inferiores menor, o pulsos femorales débiles con retraso radio-femoral}}. Soplo {{c2::sistólico de eyección audible en espalda, área interescapular izquierda}}. Compatible con {{c3::coartación de aorta}}. Solicito {{c4::ecocardiograma y eventualmente angio-TC o RM para anatomía}}."',
        "extra": "🎯 HTA en escolar/adolescente sin causa evidente = OBLIGA a descartar coartación. ❌ Error: olvidar palpar femorales en un control rutinario de TA.",
        "tags": ["coartacion"],
    },
    {
        "text": 'Niño asintomático o con disnea de esfuerzo. Soplo sistólico de eyección en foco pulmonar con CLICK eyectivo precoz, sin irradiación. Verbalizas: "Soplo {{c1::sistólico de eyección en foco pulmonar precedido de click eyectivo}}, S2 con P2 atenuado si la estenosis es severa. Compatible con {{c2::estenosis pulmonar valvular}}. Solicito {{c3::ecocardiograma para gradiente; si gradiente >50-60 mmHg → valvuloplastia con balón}}."',
        "extra": "🎯 El click eyectivo precoz lo separa de un soplo inocente. ❌ Error: ignorar el click y catalogar como inocente.",
        "tags": ["estenosis_pulmonar"],
    },

    # ────────────────────────────────────
    # BLOQUE F — Banderas rojas (4)
    # ────────────────────────────────────
    {
        "text": 'Niño con cianosis central crónica + acropaquia (dedos en palillo de tambor). Verbalizas: "{{c1::Cianosis central crónica con acropaquia (dedos en palillo)}} indica hipoxemia crónica de probable origen cardíaco. Sospecho {{c2::cardiopatía congénita cianótica (Fallot, transposición de grandes vasos, atresia tricuspídea, anomalía de Ebstein, síndrome de Eisenmenger)}}. {{c3::Derivación URGENTE a cardiología pediátrica}}."',
        "extra": "🎯 La acropaquia tarda meses en desarrollarse → indica hipoxemia crónica, no aguda. ❌ Error: no buscar acropaquia en niño con cianosis.",
        "tags": ["bandera_roja", "cianosis"],
    },
    {
        "text": 'Lactante con tetralogía de Fallot conocida o sospechada entra en crisis: cianosis súbita intensa, llanto inconsolable, irritabilidad. Verbalizas: "Crisis hipoxémica/espasmo cianótico. Manejo inmediato en orden: {{c1::posición genu-pectoral (rodillas al pecho), oxígeno al 100%, sedación con morfina IM/IV, propranolol IV, expansión volémica con cristaloides}}. Si refractario: {{c2::fenilefrina IV (aumenta RVS, disminuye shunt der-izq) o noradrenalina}}."',
        "extra": "🎯 Orden de manejo + razón fisiopatológica de cada paso (todos buscan aumentar RVS o disminuir contracción infundibular). ❌ Error: solo dar oxígeno sin las demás medidas.",
        "tags": ["bandera_roja", "crisis_hipoxemica"],
    },
    {
        "text": 'Niño con artritis migratoria + soplo cardíaco nuevo + corea o eritema marginado + faringitis estreptocócica reciente. Aplico criterios de {{c1::Jones 2015}}. Mayores (en población de alto riesgo): {{c2::carditis, artritis (mono o poliartritis), corea de Sydenham, eritema marginado, nódulos subcutáneos}}. Menores: {{c3::fiebre ≥38, artralgias, VSG/PCR elevadas, intervalo PR prolongado en ECG}}. Diagnóstico: 2 mayores, o 1 mayor + 2 menores + evidencia de infección estreptocócica reciente (ASLO, faringocultivo).',
        "extra": "🎯 Jones 2015 introdujo criterios distintos según nivel de riesgo poblacional (mayor sensibilidad en alto riesgo). Nombrar la guía con año = nivel pulcro. ❌ Error: olvidar el antecedente estreptocócico — sin él, no se hace diagnóstico.",
        "tags": ["bandera_roja", "fiebre_reumatica", "jones_2015"],
    },
    {
        "text": 'Recién nacido a las 24 horas de vida, saturación 92% en mano derecha y 88% en pie derecho. Verbalizas: "{{c1::Diferencia de saturación pre-ductal (mano derecha) y post-ductal (pie) mayor a 3%, O saturación absoluta menor a 95% en cualquiera}}. Screening neonatal POSITIVO. Indico {{c2::ecocardiograma URGENTE en las próximas 24 horas para descartar cardiopatía congénita ductus-dependiente (transposición de grandes vasos, atresia pulmonar, atresia tricuspídea, hipoplasia de cavidades izquierdas, coartación crítica)}}."',
        "extra": "🎯 Screening obligatorio en muchos países (incluido España). Detecta cardiopatías con saturación 'aceptable' a simple vista. ❌ Error grave: tranquilizarse con SatO2 92% en RN — para él es bajo.",
        "tags": ["bandera_roja", "screening_neonatal"],
    },

    # ────────────────────────────────────
    # BLOQUE G — Cierre ECOE (3)
    # ────────────────────────────────────
    {
        "text": 'Le explicas a los padres los estudios indicados con lenguaje accesible: {{c1::"Voy a solicitar electrocardiograma para ver el ritmo y la repolarización, radiografía de tórax para ver el tamaño del corazón y los pulmones, y ecocardiograma — una ecografía del corazón — para ver con detalle la estructura y función. Es indoloro."}}',
        "extra": "🎯 ECG + Rx + Eco es la tríada pediátrica de cribado. Lenguaje accesible para padres. ❌ Error: usar jerga ('cardiomegalia', 'shunt') sin traducir.",
        "tags": ["cierre", "estudios"],
    },
    {
        "text": 'Le explicas a los padres la derivación: {{c1::"Voy a derivarlo a cardiología pediátrica para que un especialista lo evalúe a fondo. La urgencia será [urgente si bandera roja / preferente si soplo patológico / ordinaria si dudoso]. Mientras tanto, [observe X síntoma específico / siga estas indicaciones nutricionales / mantenga el calendario vacunal]."}}',
        "extra": "🎯 Nivel de urgencia + indicaciones de control durante la espera + indicación de seguir lo habitual (vacunas). ❌ Error: cerrar sin instrucciones específicas a los padres.",
        "tags": ["cierre", "derivacion"],
    },
    {
        "text": 'Signos de alarma del lactante con sospecha de cardiopatía — específicos y diferentes del adulto: {{c1::"Si el niño rechaza el alimento o se cansa mucho mientras come, suda excesivamente con las tomas, respira muy rápido o con esfuerzo (tiraje), se pone azul (cianosis) en llanto o reposo, no gana peso adecuadamente, o tiene infecciones respiratorias repetidas — acudan a urgencias inmediatamente. Si todo va bien, control en [tiempo según urgencia]."}}',
        "extra": "🎯 Signos de ICC pediátrica específicos: la disnea de esfuerzo en lactante = cansancio al COMER (es su único 'ejercicio'). ❌ Error: usar criterios de adulto (disnea de esfuerzo, ortopnea) en lactante.",
        "tags": ["cierre", "signos_alarma"],
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
