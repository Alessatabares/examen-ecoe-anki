"""
Ruidos Cardiacos Adulto — Verbalización ECOE
Subdeck paralelo orientado a entrenar qué decir al sinodal en la estación
de auscultación cardiovascular.
Guías: AHA/ACC 2020 Valvular Heart Disease + Duke modificados (endocarditis)
Output: output/Ruidos_Cardiacos_Adulto_VerbalizacionECOE.apkg
"""
import os
import json
import genanki

TEMA_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPO_ROOT = os.path.dirname(TEMA_ROOT)
OUTPUT = os.path.join(TEMA_ROOT, "output", "Ruidos_Cardiacos_Adulto_VerbalizacionECOE.apkg")
IDS_PATH = os.path.join(REPO_ROOT, "ids.json")

DECK_ID = 1623891054
DECK_NAME = "Ruidos Cardiacos Adulto::Verbalización ECOE"

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

BASE_TAGS = ["verbalizacion", "ruidos_cardiacos_adulto", "aha_acc_2020", "ecoe"]

CARDS = [
    # ────────────────────────────────────
    # BLOQUE A — Apertura ECOE (5)
    # ────────────────────────────────────
    {
        "text": 'Paciente entra a tu consulta. Antes de cualquier maniobra verbalizas: {{c1::"Buenos días, soy [tu nombre], médico/estudiante de medicina. ¿Es usted el señor/la señora [apellido]? Voy a hacerle una exploración cardiovascular por su consulta de [motivo]."}}',
        "extra": "🎯 4 elementos: saludo + presentación + identidad + anuncio de la maniobra. ❌ Error: ir directo al estetoscopio sin saludo ni anuncio.",
        "tags": ["apertura"],
    },
    {
        "text": 'Sentado el paciente, anamnesis dirigida al sistema cardiovascular: {{c1::"¿Tiene dolor torácico, disnea, palpitaciones, síncope o desmayos? ¿Fiebre reciente? ¿Edema en piernas o aumento de peso súbito?"}} Si hay dolor, caracterízalo con {{c2::OPQRST (Onset, Provocación/paliación, Calidad, Radiación, Severidad, Timing)}}.',
        "extra": "🎯 Los 5 síntomas centinela CV: dolor, disnea, palpitaciones, síncope, edema. OPQRST si dolor. ❌ Error: anamnesis genérica sin dirigir al sistema.",
        "tags": ["anamnesis"],
    },
    {
        "text": 'Antecedentes que CAMBIAN la conducta: {{c1::"¿Tuvo fiebre reumática o faringitis frecuentes en la infancia? ¿Le han dicho que tiene un soplo? ¿Ha tenido cirugía cardíaca o prótesis valvular? ¿Usa drogas inyectables? ¿Procedimientos dentales recientes con sangrado?"}}',
        "extra": "🎯 FR previa → valvulopatía reumática (EM). Prótesis + drogas IV + dental procedures → riesgo de endocarditis. ❌ Error: omitir antecedentes que reconfiguran el diagnóstico (trampa ECOE clásica).",
        "tags": ["anamnesis", "antecedentes"],
    },
    {
        "text": 'Antes de la auscultación, en voz alta: {{c1::"Procedo a lavarme las manos / aplicar gel hidroalcohólico, y limpio el estetoscopio (campana y membrana) con alcohol."}}',
        "extra": "🎯 La LIMPIEZA DEL ESTETOSCOPIO es específica de esta estación (diferente de otoscopia). ❌ Error: olvidar limpiar el estetoscopio.",
        "tags": ["higiene"],
    },
    {
        "text": 'Antes de auscultar, consentimiento + preparación: {{c1::"Le voy a auscultar el pecho. Le pediré que descubra el tórax (manteniendo su pudor con la bata), que respire normalmente, y por momentos que se incline o se acueste de lado. ¿Está de acuerdo?"}}',
        "extra": "🎯 Consentimiento + preparación + advertencia de cambios de posición + cuidar el pudor. ❌ Error: pedirle descubrirse sin avisar = falla ética.",
        "tags": ["consentimiento"],
    },

    # ────────────────────────────────────
    # BLOQUE B — Inspección + palpación (3)
    # ────────────────────────────────────
    {
        "text": 'Con el tórax descubierto, ANTES de tocar: {{c1::"Inspecciono el precordio: sin deformidades torácicas (pectus excavatum/carinatum), sin cicatrices de esternotomía o toracotomía, sin pulsaciones visibles anormales."}}',
        "extra": "🎯 Cicatriz de esternotomía = cirugía cardíaca previa = contexto crítico. Pectus puede asociar Marfan. ❌ Error: omitir la inspección visual.",
        "tags": ["inspeccion"],
    },
    {
        "text": 'Palpas el ápex con la palma o yemas: {{c1::"Palpo el choque de la punta en el 5.º espacio intercostal, línea medioclavicular izquierda, de menos de 2 cm de diámetro, no sostenido."}} Si está {{c2::desplazado lateralmente sospecho dilatación VI (IM crónica, miocardiopatía); si es sostenido sospecho hipertrofia VI (EA, HTA)}}.',
        "extra": "🎯 Ubicación + tamaño + duración. Cada alteración tiene significado etiológico. ❌ Error: saltar la palpación.",
        "tags": ["palpacion"],
    },
    {
        "text": 'Antes de auscultar, búsqueda de frémito: {{c1::"Palpo los focos cardíacos con la base de la palma buscando frémitos. Sin frémito palpable."}} Si lo hay → soplo de intensidad {{c2::≥4/6 en escala de Levine}}.',
        "extra": "🎯 Frémito = umbral de intensidad ≥4/6. Diferencia automática entre soplo leve y significativo. ❌ Error: solo auscultar sin palpar.",
        "tags": ["palpacion", "fremito"],
    },

    # ────────────────────────────────────
    # BLOQUE C — Técnica de auscultación (4)
    # ────────────────────────────────────
    {
        "text": 'Antes de colocar el estetoscopio, anuncias el orden: {{c1::"Auscultaré sistemáticamente 5 focos: aórtico (2.º EIC derecho), pulmonar (2.º EIC izquierdo), aórtico accesorio o de Erb (3.er EIC izquierdo), tricúspide (4.º-5.º EIC paraesternal izquierdo) y mitral o ápex (5.º EIC línea medioclavicular)."}}',
        "extra": "🎯 5 focos + ubicaciones anatómicas exactas + orden estandarizado. ❌ Error: auscultar al azar sin nombrar los focos.",
        "tags": ["tecnica", "focos"],
    },
    {
        "text": 'Uso ambos componentes del estetoscopio según la frecuencia: {{c1::"Membrana (diafragma) presionando firme para ALTAS frecuencias: S1, S2, soplos de insuficiencia aórtica e insuficiencia mitral. Campana sin presionar para BAJAS frecuencias: S3, S4 y retumbo diastólico de estenosis mitral."}}',
        "extra": "🎯 Saber qué cabeza usar para qué hallazgo. ❌ Error: solo usar membrana = pierdes EM (retumbo) y galopes (S3/S4).",
        "tags": ["tecnica"],
    },
    {
        "text": 'Maniobras dinámicas obligatorias: {{c1::Decúbito lateral izquierdo con CAMPANA en ápex → mejora el retumbo de estenosis mitral y el S3}}. {{c2::Sentado, inclinado hacia adelante, en espiración forzada, con MEMBRANA en foco aórtico → mejora el soplo diastólico de insuficiencia aórtica}}.',
        "extra": "🎯 Las dos maniobras clásicas. Verbalizarlas + hacerlas demuestra dominio técnico. ❌ Error: auscultar solo en decúbito supino = pierdes EM e IA.",
        "tags": ["tecnica", "maniobras"],
    },
    {
        "text": 'Maniobras que cambian la intensidad de los soplos: {{c1::Valsalva (fase de strain) → DISMINUYE casi todos los soplos EXCEPTO miocardiopatía hipertrófica obstructiva (MHO) y prolapso mitral (estos AUMENTAN)}}. {{c2::Cuclillas o handgrip → aumentan retorno venoso y RVS → AUMENTAN IM e IA; DISMINUYEN MHO}}.',
        "extra": "🎯 Saber qué soplos aumentan con qué maniobra = identifica MHO y prolapso. ❌ Error: no usar maniobras = no diferencia MHO de EA.",
        "tags": ["maniobras"],
    },

    # ────────────────────────────────────
    # BLOQUE D — Descripción del soplo (4)
    # ────────────────────────────────────
    {
        "text": 'Al describir un soplo, los 7 elementos en orden: {{c1::"Timing (sistólico/diastólico/continuo), forma (holosistólico/crescendo-decrescendo/decrescendo), intensidad (Levine I-VI), foco máximo, irradiación, calidad o timbre, cambios con maniobras dinámicas"}}.',
        "extra": "🎯 Checklist ECOE estándar. ❌ Error: decir 'soplo sistólico' sin desglosar — el sinodal espera el análisis completo.",
        "tags": ["descripcion_soplo"],
    },
    {
        "text": 'Intensidad por escala de Levine: {{c1::"I = muy débil, audible solo en silencio. II = débil pero audible inmediatamente. III = moderado, sin frémito. IV = fuerte con FRÉMITO palpable. V = muy fuerte, audible con el borde del estetoscopio apenas tocando. VI = audible sin estetoscopio."}}',
        "extra": "🎯 Frémito = umbral 4/6. ≥4/6 = casi siempre patológico. ❌ Error: no graduar la intensidad o usar otra escala (cuantitativa, sin Levine).",
        "tags": ["descripcion_soplo", "levine"],
    },
    {
        "text": 'Irradiaciones clásicas a verbalizar: {{c1::EA → carótidas}}; {{c2::IM → axila izquierda}}; {{c3::coartación o EA subvalvular → espalda interescapular}}; {{c4::CIV → cinturón paraesternal sin irradiación a axila}}.',
        "extra": "🎯 Irradiaciones son anchors diagnósticos clave. ❌ Error: no buscar irradiación = pierdes diferenciación EA/IM/CIV.",
        "tags": ["descripcion_soplo", "irradiacion"],
    },
    {
        "text": 'Maniobra de Carvallo (cambios con respiración): {{c1::los soplos del lado DERECHO (insuficiencia tricuspídea, estenosis pulmonar) AUMENTAN con la INSPIRACIÓN profunda (mayor retorno venoso al VD)}}. Los del lado izquierdo no cambian o disminuyen levemente.',
        "extra": "🎯 Signo de Carvallo POSITIVO = soplo aumenta con inspiración → origen DERECHO. Diferencia IT (paraesternal) vs IM. ❌ Error: no diferenciar IT de IM.",
        "tags": ["maniobras", "carvallo"],
    },

    # ────────────────────────────────────
    # BLOQUE E — Verbalización por patrón (8)
    # ────────────────────────────────────
    {
        "text": 'Anciano con angina, síncope y disnea. Soplo sistólico crescendo-decrescendo en foco aórtico, irradia a carótidas, S2 disminuido. Verbalizas: "Soplo {{c1::sistólico romboidal (crescendo-decrescendo), intensidad 3-4/6, foco aórtico con irradiación a carótidas, S2 apagado}}. Compatible con {{c2::estenosis aórtica}}. Solicito {{c3::ECG y ecocardiograma para gradiente y área valvular; si área <1 cm² y síntomas → derivación para reemplazo (TAVI o quirúrgico)}}."',
        "extra": "🎯 Tríada clásica de EA severa sintomática: angina + síncope + ICC = mortalidad ~50% a 2 años sin reemplazo. ❌ Error: subestimar los síntomas.",
        "tags": ["estenosis_aortica"],
    },
    {
        "text": 'Soplo diastólico decrescendo en foco aórtico que se ausculta mejor sentado inclinado adelante en espiración. Pulso saltón. Verbalizas: "Soplo {{c1::diastólico decrescendo en foco aórtico/Erb, audible mejor con el paciente sentado e inclinado hacia adelante}}. Pulso {{c2::de Corrigan/martillo de agua, TA divergente}}. Compatible con {{c3::insuficiencia aórtica}}. Solicito ecocardiograma para cuantificar regurgitación y diámetros del VI."',
        "extra": "🎯 Pulso de Corrigan y TA divergente = signos periféricos de IA = nivel pulcro. ❌ Error: solo describir el soplo sin signos periféricos.",
        "tags": ["insuficiencia_aortica"],
    },
    {
        "text": 'Soplo holosistólico en ápex que irradia a axila, AUMENTA con handgrip, disminuye con Valsalva. Verbalizas: "Soplo {{c1::holosistólico (plano) en foco mitral con irradiación a axila izquierda, AUMENTA con handgrip}}. Compatible con {{c2::insuficiencia mitral}}. Solicito {{c3::ecocardiograma para etiología (prolapso, isquémica, reumática, funcional) y cuantificación}}."',
        "extra": "🎯 Holosistólico + axila = IM clásica. Cambios con maniobras lo separan de MHO. ❌ Error: confundir con CIV (también holosistólico pero paraesternal y SIN axila).",
        "tags": ["insuficiencia_mitral"],
    },
    {
        "text": 'Soplo diastólico en retumbo en ápex (mejor con campana en decúbito lateral izq), S1 reforzado, chasquido de apertura, antecedente de fiebre reumática. Verbalizas: "Soplo {{c1::diastólico en retumbo, foco mitral, mejor audible con CAMPANA en decúbito lateral izquierdo}}, con S1 reforzado y chasquido de apertura. Compatible con {{c2::estenosis mitral (típicamente reumática)}}. Solicito {{c3::ecocardiograma para área valvular y morfología; ECG buscando FA}}."',
        "extra": "🎯 Tríada: retumbo + S1 reforzado + chasquido de apertura. FR es la causa #1 de EM. Asociar FA es frecuente. ❌ Error: olvidar usar la campana — el retumbo es de baja frecuencia.",
        "tags": ["estenosis_mitral"],
    },
    {
        "text": 'Joven con click meso-sistólico seguido de soplo en ápex que se desplaza con Valsalva. Verbalizas: "{{c1::Click meso-sistólico seguido de soplo telesistólico en foco mitral, que se hace más PRECOZ con Valsalva y bipedestación}}. Compatible con {{c2::prolapso de válvula mitral}}." Si fuera IT en cambio: "{{c3::Soplo holosistólico paraesternal izquierdo, AUMENTA con la inspiración (Carvallo POSITIVO)}}."',
        "extra": "🎯 Carvallo POSITIVO = signo cardinal de IT (diferencia de IM). Prolapso desplaza el click con Valsalva. ❌ Error: confundir prolapso con IM aislada.",
        "tags": ["prolapso_mitral", "insuficiencia_tricuspidea"],
    },
    {
        "text": 'Embarazada/febril/anémica con soplo sistólico suave ≤2/6 en foco pulmonar, sin irradiación, sin frémito, sin clínica cardiovascular. Verbalizas: "Soplo {{c1::sistólico de eyección, intensidad 2/6, foco pulmonar, sin irradiación, sin frémito, sin S3/S4}}. En contexto de {{c2::hiperdinamia (fiebre/embarazo/anemia)}}, compatible con {{c3::soplo funcional/inocente del adulto}}. Conducta: tratar la causa subyacente, sin estudios cardiológicos inmediatos."',
        "extra": "🎯 Soplo de hiperdinamia, no patológico. Resolver la causa primero. ❌ Error: pedir ecocardiograma a toda embarazada con soplo.",
        "tags": ["soplo_funcional"],
    },
    {
        "text": 'Paciente con fiebre persistente + soplo nuevo + factor de riesgo (prótesis, drogas IV, procedimiento dental). Verbalizas: "Sospecho endocarditis infecciosa. Aplico criterios de {{c1::Duke modificados: 2 mayores, 1 mayor + 3 menores, o 5 menores}}. Mayores: {{c2::hemocultivos positivos típicos + evidencia ecocardiográfica de afectación endocárdica (vegetación/absceso/dehiscencia)}}. Menores: {{c3::predisposición, fiebre >38, fenómenos vasculares (Janeway/embolismo), inmunológicos (Osler/Roth/glomerulonefritis), microbiológicos que no cumplen mayor}}."',
        "extra": "🎯 Nombrar Duke modificados explícitamente + saber los mayores/menores. ❌ Error: diagnosticar endocarditis 'clínicamente' sin enmarcar en Duke.",
        "tags": ["endocarditis", "duke"],
    },
    {
        "text": 'Paciente con prótesis valvular antes de procedimiento dental con manipulación gingival. Verbalizas: "Indico profilaxis antibiótica de endocarditis con {{c1::amoxicilina 2 g VO 30-60 minutos antes del procedimiento (clindamicina 600 mg si alergia a penicilina)}}. La profilaxis SOLO está indicada en pacientes con: {{c2::prótesis valvular, endocarditis previa, cardiopatía congénita cianótica no reparada, trasplante cardíaco con valvulopatía residual}}."',
        "extra": "🎯 Las indicaciones de profilaxis se ESTRECHARON mucho en guías AHA. Saberlas evita sobreprofilaxis. ❌ Error: indicarla a todo paciente con valvulopatía (ya no se hace).",
        "tags": ["profilaxis_endocarditis"],
    },

    # ────────────────────────────────────
    # BLOQUE F — Banderas rojas (3)
    # ────────────────────────────────────
    {
        "text": 'Paciente con EA + tríada clínica de síncope, angina y disnea/ICC. Verbalizas: "EA con {{c1::tríada de síncope + angina + insuficiencia cardíaca}} = EA crítica sintomática. Mortalidad sin tratamiento ~50% a 2 años. Plan: {{c2::derivación URGENTE a cardiología para reemplazo valvular (TAVI o quirúrgico) según riesgo y anatomía}}."',
        "extra": "🎯 La tríada cambia la urgencia inmediatamente. ❌ Error: tratar síntomas (diurético) sin derivar.",
        "tags": ["bandera_roja", "estenosis_aortica"],
    },
    {
        "text": 'IM aguda (ruptura de cuerda post-IAM o endocarditis) con edema pulmonar súbito. Verbalizas: "IM aguda con {{c1::edema pulmonar y deterioro hemodinámico súbito}}. Es una EMERGENCIA quirúrgica. Plan: {{c2::estabilización con ventilación mecánica, diurético, vasodilatador (nitroprusiato si TA permite), balón de contrapulsación intraaórtica, y cirugía URGENTE de reemplazo o reparación valvular}}."',
        "extra": "🎯 IM aguda ≠ IM crónica. La aguda es emergencia. ❌ Error: tratarla como crónica con IECA + diurético crónicos.",
        "tags": ["bandera_roja", "insuficiencia_mitral_aguda"],
    },
    {
        "text": 'Endocarditis confirmada + déficit neurológico súbito o lesiones cutáneas. Verbalizas: "Endocarditis con {{c1::evento embólico (cerebral, esplénico, renal) o lesiones de Janeway (no dolorosas en palmas/plantas) o nódulos de Osler (dolorosos en pulpejos)}}. Indica vegetación de alto riesgo embólico. Plan: {{c2::antibioterapia IV dirigida tras hemocultivos, ecocardiograma transesofágico urgente, valoración por cirugía cardíaca para considerar reemplazo valvular precoz}}."',
        "extra": "🎯 Diferencia Janeway (no dolorosas, palmas/plantas, vasculares) de Osler (dolorosas, pulpejos, inmunológicas) = nivel pulcro. ❌ Error: confundirlas.",
        "tags": ["bandera_roja", "endocarditis"],
    },

    # ────────────────────────────────────
    # BLOQUE G — Cierre ECOE (3)
    # ────────────────────────────────────
    {
        "text": 'Tras la auscultación, le explicas al paciente los estudios indicados con lenguaje accesible: {{c1::"Voy a solicitar un electrocardiograma para ver el ritmo del corazón, un ecocardiograma para ver con detalle las válvulas y la función del músculo cardíaco, y unos análisis de sangre (BNP/NT-proBNP si sospecho insuficiencia; hemocultivos si sospecho infección)."}}',
        "extra": "🎯 ECG + Eco + biomarcadores explicados en lenguaje claro. ❌ Error: pedir estudios sin explicar al paciente para qué.",
        "tags": ["cierre", "estudios"],
    },
    {
        "text": 'Plan terapéutico con escenarios: {{c1::"Si los estudios confirman valvulopatía moderada-severa o sintomática, lo derivaré a cardiología para evaluación más profunda y considerar tratamiento médico o intervencionista (TAVI, valvuloplastia con balón, cirugía de reemplazo o reparación). Mientras tanto, controle [síntoma específico] y siga [indicación específica]."}}',
        "extra": "🎯 Plan CONDICIONAL explícito + control de síntomas mientras tanto. ❌ Error: cerrar sin decir qué pasa según resultado.",
        "tags": ["cierre", "plan"],
    },
    {
        "text": 'Cierras SIEMPRE con signos de alarma específicos al sistema CV + tiempo de control: {{c1::"Si presenta dolor torácico que no cede, dificultad respiratoria que empeora estando acostado (ortopnea), desmayo, fiebre persistente sin causa clara, o palpitaciones intensas — acuda a urgencias inmediatamente. Si todo va bien, control en [tiempo: típicamente 2-4 semanas tras eco]."}}',
        "extra": "🎯 Signos de alarma específicos al CV + tiempo concreto de control. ❌ Error: cerrar genérico sin señales específicas.",
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
