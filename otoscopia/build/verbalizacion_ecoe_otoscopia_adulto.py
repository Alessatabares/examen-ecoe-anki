"""
Otoscopia Adulto — Verbalización ECOE
Subdeck paralelo orientado a entrenar qué decir al sinodal en cada momento
de la estación de otoscopia.
Guías: AAO-HNS (otitis externa 2014, OME 2016) + AAP/AAO-HNS OMA 2013 (reaff.)
Output: output/Otoscopia_Adulto_VerbalizacionECOE.apkg
"""
import os
import json
import genanki

TEMA_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPO_ROOT = os.path.dirname(TEMA_ROOT)
OUTPUT = os.path.join(TEMA_ROOT, "output", "Otoscopia_Adulto_VerbalizacionECOE.apkg")
IDS_PATH = os.path.join(REPO_ROOT, "ids.json")

DECK_ID = 1389254671
DECK_NAME = "Otoscopia Adulto::Verbalización ECOE"

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

BASE_TAGS = ["verbalizacion", "otoscopia_adulto", "aao_hns", "ecoe"]

CARDS = [
    # ────────────────────────────────────
    # BLOQUE A — Apertura ECOE (5)
    # ────────────────────────────────────
    {
        "text": 'El paciente entra a tu consulta. Antes de cualquier maniobra verbalizas: {{c1::"Buenos días, soy [tu nombre], médico/estudiante de medicina. ¿Es usted el señor/la señora [apellido]? Voy a explorarle el oído por su consulta de [motivo]."}}',
        "extra": "🎯 4 elementos que evalúa el sinodal: saludo + presentación profesional + confirmación de identidad + anuncio de la maniobra. ❌ Error común: entrar directo al otoscopio sin saludo ni anuncio.",
        "tags": ["apertura", "saludo"],
    },
    {
        "text": 'Sentado el paciente, antes de tocarle el oído, le preguntas dirigido al síntoma: {{c1::"¿Desde cuándo le duele/oye mal/le supura el oído? ¿Es uno o ambos oídos? ¿Hubo fiebre, vértigo, antecedente de baño, trauma o cuerpo extraño?"}}',
        "extra": "🎯 Estructura: cronología + lateralidad + síntomas asociados (fiebre, vértigo) + factores precipitantes (baño, trauma, cuerpo extraño). ❌ Error: explorar sin anamnesis previa — pierdes contexto diagnóstico.",
        "tags": ["anamnesis"],
    },
    {
        "text": 'Cierras la anamnesis preguntando antecedentes que cambian la conducta: {{c1::"¿Ha tenido infecciones de oído previas? ¿Cirugía o tubos de ventilación? ¿Padece diabetes o inmunosupresión? ¿Usa audífono o se mete cotonetes/objetos al oído?"}}',
        "extra": "🎯 Antecedentes que cambian conducta: diabetes → riesgo de otitis externa maligna (Pseudomonas); cotonetes → factor predisponente de OE; cirugía previa → tímpano puede tener patrón post-quirúrgico no patológico. ❌ Error: omitir antecedentes y luego no entender por qué el cuadro es atípico.",
        "tags": ["anamnesis", "antecedentes"],
    },
    {
        "text": 'Antes de manipular el otoscopio, en voz alta y haciéndolo: {{c1::"Procedo a lavarme las manos / aplicar gel hidroalcohólico antes de la exploración."}}',
        "extra": "🎯 Acto observable + verbalizado. Aunque uses gel, dilo. ❌ Error: hacer la higiene en silencio o saltarla — falla automática en muchas estaciones ECOE.",
        "tags": ["higiene"],
    },
    {
        "text": 'Antes de acercar el otoscopio al oído, explicas y pides permiso: {{c1::"Le voy a explorar ambos oídos con un otoscopio. Es una maniobra rápida y normalmente no duele. Si en algún momento siente molestia, dígamelo. ¿Está de acuerdo?"}}',
        "extra": "🎯 Explicación de la maniobra + advertencia de posible molestia + permiso explícito. ❌ Error: meter el espéculo sin avisar — falla ética y técnica.",
        "tags": ["consentimiento"],
    },

    # ────────────────────────────────────
    # BLOQUE B — Inspección externa pre-otoscopio (3)
    # ────────────────────────────────────
    {
        "text": 'Antes del otoscopio, inspeccionas el oído externo y verbalizas: {{c1::"Inspecciono pabellón auricular y región retroauricular: sin asimetrías, sin eritema, sin edema, sin lesiones cutáneas, sin signos inflamatorios mastoideos."}}',
        "extra": "🎯 Lo que ves Y lo que NO ves (negativos pertinentes). El signo de Jacques (despegamiento del pabellón en mastoiditis aguda) se detecta justo en esta inspección. ❌ Error: ir directo al CAE sin inspección externa previa.",
        "tags": ["inspeccion_externa"],
    },
    {
        "text": 'Tras la inspección visual, palpas y verbalizas: {{c1::"Palpo trago, pabellón y mastoides: sin dolor referido, sin masas palpables, sin signos inflamatorios locales."}}',
        "extra": "🎯 Tres puntos a palpar: trago + pabellón + mastoides. La palpación mastoidea es crucial para descartar mastoiditis.",
        "tags": ["palpacion"],
    },
    {
        "text": 'Mientras palpas el trago aplicas presión moderada. Si el paciente refiere dolor exquisito, lo verbalizas como bifurcación rectora: {{c1::"Signo del trago POSITIVO — orienta a otitis externa antes incluso de visualizar la membrana timpánica."}}',
        "extra": "🎯 Bifurcación rectora: positivo = otitis externa; negativo con clínica auditiva = otitis media o patología timpánica. ❌ Error: olvidar este signo y confundir otitis externa con OMA porque ambas duelen al oído.",
        "tags": ["signo_trago", "bifurcacion"],
    },

    # ────────────────────────────────────
    # BLOQUE C — Técnica de otoscopia (4)
    # ────────────────────────────────────
    {
        "text": 'Listo para empezar con el otoscopio, anuncias: {{c1::"Empiezo por el oído asintomático para usarlo como referencia normal y no contaminar el espéculo."}}',
        "extra": "🎯 Reglas ECOE básicas: lado sano primero + razón verbalizada. ❌ Error: empezar por el lado que duele — contamina espéculo y al sinodal le indica falta de método.",
        "tags": ["tecnica"],
    },
    {
        "text": 'Tomas el otoscopio y verbalizas la técnica de sujeción: {{c1::"Sostengo el otoscopio como un lápiz y apoyo el meñique en la mejilla del paciente para amortiguar movimientos bruscos."}}',
        "extra": "🎯 Tipo lápiz + meñique de apoyo = previene laceración del CAE si el paciente se mueve. ❌ Error: sostenerlo en puño cerrado o sin punto de apoyo — riesgo de lesión.",
        "tags": ["tecnica"],
    },
    {
        "text": 'Para rectificar el CAE en el adulto, verbalizas mientras lo haces: {{c1::"Tracciono el pabellón auricular hacia arriba y hacia atrás para rectificar el conducto."}} (En niño <3 años cambiaría a: {{c2::abajo y atrás}} por la anatomía más horizontal).',
        "extra": "🎯 Adulto = arriba y atrás. Niño pequeño = abajo y atrás (CAE más horizontal y corto). Nombrar la diferencia anatómica te suma puntos. ❌ Error: traccionar al revés y no poder visualizar el tímpano.",
        "tags": ["tecnica", "traccion"],
    },
    {
        "text": 'Antes de introducir el otoscopio eliges el espéculo y lo verbalizas: {{c1::"Selecciono el espéculo más grande que entre cómodamente sin causar dolor — generalmente 4 mm en adulto, 2-3 mm en niño."}}',
        "extra": "🎯 El más grande POSIBLE da mejor visión y luz. Demasiado pequeño = visión túnel. Demasiado grande = dolor y lesión del CAE.",
        "tags": ["tecnica", "especulo"],
    },

    # ────────────────────────────────────
    # BLOQUE D — Descripción de hallazgos (4)
    # ────────────────────────────────────
    {
        "text": 'Una vez introducido el otoscopio, ANTES de describir el tímpano describes el conducto: {{c1::"Conducto auditivo externo: permeable, sin cerumen abundante, sin eritema, sin edema, sin exudado, sin lesiones ni cuerpos extraños."}}',
        "extra": "🎯 CAE PRIMERO, tímpano después. Es el orden anatómico y el sinodal lo espera. ❌ Error: brincar directo al tímpano sin describir el CAE — pierdes información (cerumen, otitis externa, cuerpo extraño).",
        "tags": ["descripcion_cae"],
    },
    {
        "text": 'Al describir un tímpano verbalizas los 4 elementos en orden: {{c1::"color, transparencia, posición del cono de luz, integridad y posición del mango del martillo y umbo."}}',
        "extra": "🎯 Los 4 elementos = checklist ECOE estándar para timpano. ❌ Error: decir solo 'tímpano normal' sin desglosar — el sinodal espera la descripción analítica.",
        "tags": ["descripcion_timpano"],
    },
    {
        "text": 'Frente a un tímpano normal verbalizas el anchor completo: {{c1::"Tímpano gris perlado, translúcido, con cono de luz íntegro en cuadrante anteroinferior, mango del martillo y umbo visibles en posición central. Sin abombamiento, sin retracción, sin perforación, sin nivel hidroaéreo."}}',
        "extra": "🎯 Es el 'anchor' verbal que el sinodal busca. Aprenderlo de memoria. ❌ Error: decir 'se ve bien' o 'normal' — el sinodal no puede evaluar lo que no especificas.",
        "tags": ["descripcion_timpano", "timpano_normal"],
    },
    {
        "text": 'Si el cerumen o detritus impide ver la membrana, NO la etiquetes como normal. Verbaliza honestamente: {{c1::"El cerumen abundante en el CAE impide la visualización completa de la membrana timpánica. Indico ablandadores y lavado/extracción, y reexploración tras la limpieza."}}',
        "extra": "🎯 La honestidad es nivel pulcro: no etiquetes lo que no ves. ❌ Error grave: decir 'tímpano normal' cuando estás viendo cerumen — falla de método y de ética profesional.",
        "tags": ["descripcion_timpano", "cerumen"],
    },

    # ────────────────────────────────────
    # BLOQUE E — Verbalización por patrón patológico (8)
    # ────────────────────────────────────
    {
        "text": 'Tímpano abombado, eritematoso, sin cono de luz, paciente con fiebre y otalgia aguda. Verbalizas: "Tímpano {{c1::abombado y eritematoso, con pérdida del cono de luz}}. Hallazgos compatibles con {{c2::otitis media aguda (OMA)}}. Plan: {{c3::analgesia y antibiótico empírico — amoxicilina 1 g cada 8 horas en adulto, 80-90 mg/kg/día dividido en niño, si cumple criterios de tratamiento}}."',
        "extra": "🎯 El ABOMBAMIENTO es el signo cardinal de OMA según AAP 2013, NO el eritema solo. ❌ Error común: diagnosticar OMA solo por eritema (un tímpano puede estar rojo por llanto o fiebre alta sin OMA).",
        "tags": ["oma", "patron"],
    },
    {
        "text": 'Tímpano retraído u opaco con nivel hidroaéreo o burbujas, sin fiebre, hipoacusia conductiva. Verbalizas: "Tímpano {{c1::opaco con nivel hidroaéreo, sin abombamiento ni eritema, sin signos inflamatorios}}. Compatible con {{c2::otitis media con efusión (OME)}}. Plan: {{c3::observación 3 meses (resolución espontánea frecuente); si persiste o hay retraso del lenguaje en niño, derivar a ORL para considerar tubos de ventilación}}."',
        "extra": "🎯 OME NO se trata con antibiótico. Es seroso, no infeccioso agudo. ❌ Error frecuente: prescribir amoxicilina ante OME — sobretratamiento sin beneficio clínico.",
        "tags": ["ome", "patron"],
    },
    {
        "text": 'Signo del trago positivo, CAE eritematoso, edematoso, con exudado o detritus. Verbalizas: "Conducto auditivo externo {{c1::eritematoso y edematoso, con detritus/exudado, doloroso a la tracción del trago}}. Compatible con {{c2::otitis externa aguda}}. Plan: {{c3::gotas tópicas (ciprofloxacino + dexametasona) 7-10 días, analgesia, evitar baño y entrada de agua}}."',
        "extra": "🎯 Manejo TÓPICO, NO sistémico (salvo extensión a partes blandas o paciente diabético/inmunosuprimido). ❌ Error: dar antibiótico oral para una otitis externa simple.",
        "tags": ["otitis_externa", "patron"],
    },
    {
        "text": 'Solución de continuidad visible en la membrana timpánica. Verbalizas: "Membrana timpánica con {{c1::perforación de bordes [netos = traumática reciente / irregulares = post-infecciosa] en el cuadrante [postero-inferior/central/marginal]}}. Plan: {{c2::evitar entrada de agua al oído, gotas antibióticas si hay otorrea, control en 4-6 semanas; si no cierra espontáneamente, derivar a ORL para miringoplastia}}."',
        "extra": "🎯 Describir BORDES (netos vs irregulares) y LOCALIZACIÓN (central vs marginal). Las marginales sugieren riesgo aumentado de colesteatoma — vale la pena derivar antes.",
        "tags": ["perforacion", "patron"],
    },
    {
        "text": 'Masa marrón/amarillenta/negruzca ocupando el CAE. Verbalizas: "{{c1::Tapón de cerumen impactado que ocupa el CAE e impide visualización}}. Plan: {{c2::ablandadores tópicos (peróxido o aceite) 3-5 días seguido de lavado con jeringa de agua tibia, o extracción manual con cureta bajo visión directa}}. {{c3::Reexplorar tímpano tras la extracción}}."',
        "extra": "🎯 NUNCA lavar si hay sospecha de perforación previa (preguntar en anamnesis). La REEXPLORACIÓN post-extracción es obligatoria — el tapón puede ocultar OMA u otra patología.",
        "tags": ["cerumen", "patron"],
    },
    {
        "text": 'Masa blanca-perlada-escamosa en pars flácida (cuadrante superior) + otorrea fétida crónica + hipoacusia conductiva progresiva. Verbalizas: "Masa {{c1::blanca, perlada, escamosa en pars flácida (ático)}} asociada a otorrea fétida e hipoacusia. Compatible con {{c2::colesteatoma}}. Plan: {{c3::derivación URGENTE a ORL para evaluación quirúrgica}} — es lesión destructiva."',
        "extra": "🎯 BANDERA ROJA: nunca manejar en primer nivel. ❌ Error grave: prescribir gotas y reevaluar — el colesteatoma erosiona huesecillos, mastoides, puede dar parálisis facial o complicación intracraneal.",
        "tags": ["colesteatoma", "patron", "bandera_roja"],
    },
    {
        "text": 'Vesículas o ampollas hemorrágicas sobre la membrana timpánica + dolor intenso desproporcionado. Verbalizas: "{{c1::Vesículas/ampollas hemorrágicas sobre la membrana timpánica}}. Compatible con {{c2::miringitis bullosa (variante viral de OMA, frecuentemente por Mycoplasma)}}. Plan: {{c3::analgesia con AINE como principal; antibiótico (macrólido) si hay datos de OMA bacteriana asociada o factores de riesgo}}."',
        "extra": "🎯 Analgesia es lo principal (el dolor es desproporcionado). Antibiótico no siempre — depende de presentación bacteriana asociada.",
        "tags": ["miringitis", "patron"],
    },
    {
        "text": 'Paciente refiere hipoacusia progresiva pero la otoscopia muestra tímpano completamente normal. Verbalizas: "Tímpano de aspecto {{c1::normal y simétrico en ambos oídos}}. Dado que persiste hipoacusia con otoscopia normal, sospecho {{c2::hipoacusia neurosensorial}} y solicito {{c3::audiometría tonal y logoaudiometría}} para confirmar y caracterizar."',
        "extra": "🎯 Tímpano normal NO descarta hipoacusia — el problema no se ve en otoscopia. El estudio es la audiometría. ❌ Error: cerrar el caso con 'exploración normal' sin solicitar audiometría.",
        "tags": ["hipoacusia_neurosensorial", "patron"],
    },

    # ────────────────────────────────────
    # BLOQUE F — Banderas rojas → derivación (3)
    # ────────────────────────────────────
    {
        "text": 'Paciente con otorrea + paresia del lado facial ipsilateral (asimetría facial, no cierra el ojo). Verbalizas: "Otitis activa con {{c1::parálisis facial periférica ipsilateral}} — BANDERA ROJA por sospecha de {{c2::mastoiditis aguda o colesteatoma complicado}}. Derivación URGENTE a ORL para imagen (TC de hueso temporal) y tratamiento intravenoso."',
        "extra": "🎯 NUNCA esperar respuesta a antibiótico oral con esta combinación. Imagen (TC) + ORL inmediato. La parálisis facial puede ser permanente si no se actúa rápido.",
        "tags": ["bandera_roja", "paralisis_facial"],
    },
    {
        "text": 'Otitis crónica + vértigo provocado al presionar el trago o aplicar presión positiva en el CAE. Verbalizas: "Sospecha de {{c1::fístula laberíntica}} por signo de fístula positivo, probable erosión del laberinto óseo por colesteatoma. Derivación URGENTE a ORL para imagen y manejo quirúrgico."',
        "extra": "🎯 Signo de la fístula POSITIVO = presión en CAE provoca vértigo/nistagmo. Es complicación grave del colesteatoma.",
        "tags": ["bandera_roja", "fistula_laberintica"],
    },
    {
        "text": 'Diabético/inmunosuprimido con otitis externa que no mejora con tópicos, dolor desproporcionado, tejido de granulación en CAE. Verbalizas: "Sospecho {{c1::otitis externa maligna/necrotizante}} por Pseudomonas en paciente diabético. Requiere {{c2::ingreso hospitalario, antibiótico IV (ciprofloxacino o piperacilina-tazobactam) y TC de hueso temporal}}. Derivación URGENTE a ORL."',
        "extra": "🎯 Mortalidad alta sin tratamiento adecuado (15-30%). ❌ Error grave: tratar como otitis externa simple en diabético — puede progresar a osteomielitis de base de cráneo.",
        "tags": ["bandera_roja", "otitis_externa_maligna"],
    },

    # ────────────────────────────────────
    # BLOQUE G — Cierre ECOE (3)
    # ────────────────────────────────────
    {
        "text": 'Tras la exploración, te diriges al paciente con lenguaje llano (no técnico): {{c1::"He explorado ambos oídos. Lo que encontré es [hallazgo en palabras simples — ej: \'inflamación en el conducto del oído\', no \'eritema y edema del CAE\']. Probablemente tiene [diagnóstico en términos comprensibles]. ¿Tiene alguna pregunta antes de pasar a hablar del tratamiento?"}}',
        "extra": "🎯 Lenguaje LLANO + invitación a preguntas. ❌ Error: hablar al sinodal solamente, ignorando al paciente simulado. La comunicación con paciente es parte de la calificación.",
        "tags": ["cierre", "comunicacion"],
    },
    {
        "text": 'Le explicas al paciente el plan terapéutico con los 4 elementos: {{c1::"Voy a indicarle [tratamiento específico] por [duración]. La forma de tomarlo/aplicarlo es [instrucción concreta]. Es importante que [evite agua/complete el tratamiento aunque mejore/no use cotonetes]."}}',
        "extra": "🎯 Tratamiento + duración + forma de uso + indicación negativa (qué evitar). ❌ Error: solo decir 'le doy estas gotas' — falta de instrucciones concretas penaliza.",
        "tags": ["cierre", "plan_terapeutico"],
    },
    {
        "text": 'Cierras SIEMPRE con signos de alarma específicos + tiempo de control: {{c1::"Si empeora el dolor, aparece fiebre alta, vértigo intenso, parálisis de la cara o supuración con mal olor, debe acudir a urgencias inmediatamente. Si todo va bien, vuelva a control en [1-2 semanas o lo que aplique] para reexplorar."}}',
        "extra": "🎯 Signos de alarma ESPECÍFICOS (no genéricos) + tiempo concreto de control. ❌ Error: cerrar sin advertir signos de alarma — falla común y muy penalizada por el sinodal.",
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
