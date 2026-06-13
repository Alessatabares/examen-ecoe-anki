NAME = "Corazon"

EJES = [
    ("Dolor tor&aacute;cico", [
        ("Opresivo retroesternal + irradiado a brazo izq/mand&iacute;bula + diafores&iacute;s + ST elevado en cara contigua", "<b>IAMCEST</b> (reperfusi&oacute;n &lt;90 min ICP o &lt;30 min fibrinol&iacute;sis)"),
        ("Opresivo en reposo o crescendo + ECG sin ST elevado + troponina elevada", "<b>IAMSEST</b> (SCA sin elevaci&oacute;n del ST; estratificar GRACE)"),
        ("Opresivo con esfuerzo + cede en &lt;10 min con reposo/nitrato + troponina normal", "Angina estable (isquemia demanda; prueba de esfuerzo)"),
        ("Desgarrante de inicio s&uacute;bito + irradia a espalda interescapular + asimetr&iacute;a de pulsos/TA entre brazos", "<b>Disecci&oacute;n a&oacute;rtica</b> (TC con contraste; control de FC y TA)"),
        ("Pleur&iacute;tico que mejora al sentarse e inclinarse hacia delante + frote + ST difuso c&oacute;ncavo + PR descendido", "Pericarditis aguda (AINE + colchicina)"),
        ("Tras herida punzante precordial + hipotensi&oacute;n + ruidos card&iacute;acos apagados + IY", "<b>Taponamiento por trauma penetrante</b> (pericardiocentesis/toracotom&iacute;a)"),
    ]),
    ("Palpitaciones", [
        ("Pulso irregularmente irregular + d&eacute;ficit de pulso + ECG sin onda P + R-R variable", "Fibrilaci&oacute;n auricular (control FC + anticoagular seg&uacute;n CHA2DS2-VASc)"),
        ("Palpitaciones r&aacute;pidas + s&iacute;ncope + QRS ancho regular + disociaci&oacute;n AV", "<b>Taquicardia ventricular</b> (cardioversi&oacute;n si inestable)"),
        ("Bradicardia + s&iacute;ncope + PR &gt; 200 ms fijo o disociaci&oacute;n AV completa", "Bloqueo AV (segundo/tercer grado; valorar marcapasos)"),
        ("Palpitaciones de inicio y fin s&uacute;bitos + QRS estrecho regular ~150-220 lpm", "Taquicardia supraventricular paroxistica (maniobras vagales/adenosina)"),
        ("Latidos aislados percibidos como vuelco + pausa compensadora + bigeminismo en ECG", "Extras&iacute;stoles ventriculares (benignas si coraz&oacute;n sano)"),
    ]),
    ("S&iacute;ncope", [
        ("S&iacute;ncope de esfuerzo + soplo sist&oacute;lico eyectivo en foco a&oacute;rtico irradiado a car&oacute;tidas + pulso parvus et tardus", "Estenosis a&oacute;rtica severa (recambio valvular si sintom&aacute;tica)"),
        ("S&iacute;ncope brusco sin pr&oacute;dromos + palpitaciones previas + QT largo o TV documentada", "<b>S&iacute;ncope arr&iacute;tmico</b> (monitorizar; riesgo de muerte s&uacute;bita)"),
        ("S&iacute;ncope precedido de n&aacute;useas/sudoraci&oacute;n/visi&oacute;n en t&uacute;nel + bipedestaci&oacute;n prolongada", "S&iacute;ncope vasovagal (medidas posturales; benigno)"),
        ("Mareo/s&iacute;ncope al incorporarse + ca&iacute;da de TA sist&oacute;lica &ge; 20 mmHg de pie", "S&iacute;ncope ortost&aacute;tico (revisar f&aacute;rmacos/volemia)"),
        ("S&iacute;ncope + dolor desgarrante + diferencia de TA &gt; 20 mmHg entre brazos", "<b>Disecci&oacute;n a&oacute;rtica</b> (emergencia; imagen urgente)"),
    ]),
    ("Disnea y edema (insuficiencia card&iacute;aca)", [
        ("Disnea de esfuerzo + ortopnea + DPN + crepitantes bibasales + S3 + FEVI &lt; 40%", "IC con FE reducida (FEr; IECA/ARNI + betabloqueante + ARM + iSGLT2)"),
        ("Disnea + HTA + crepitantes + FEVI &ge; 50% conservada + S4 + hipertrofia VI", "IC con FE preservada (FEp; control de TA y comorbilidades)"),
        ("Edemas en miembros inferiores + IY + hepatomegalia + reflujo hepatoyugular", "IC derecha/congesti&oacute;n sist&eacute;mica (diur&eacute;ticos de asa)"),
        ("Disnea s&uacute;bita + ortopnea extrema + crepitantes hasta &aacute;pices + esputo rosado", "<b>Edema agudo de pulm&oacute;n</b> (O2 + nitratos + diur&eacute;tico + VMNI)"),
        ("Fiebre + soplo nuevo + disnea + petequias/n&oacute;dulos de Osler + hemocultivos positivos", "<b>Endocarditis infecciosa</b> (Duke; antibi&oacute;tico precoz)"),
    ]),
    ("Soplo", [
        ("Soplo sist&oacute;lico eyectivo crescendo-decrescendo en foco a&oacute;rtico irradiado a car&oacute;tidas + clic ausente", "Estenosis a&oacute;rtica (gradiente medio &ge; 40 mmHg = severa)"),
        ("Soplo diast&oacute;lico decrescendo en borde paraesternal izq + pulso celer (salton) + presi&oacute;n de pulso amplia", "Insuficiencia a&oacute;rtica (valorar dilataci&oacute;n VI)"),
        ("Soplo holosist&oacute;lico en &aacute;pex irradiado a axila + S3 + soplo que no var&iacute;a con respiraci&oacute;n", "Insuficiencia mitral (cirug&iacute;a si sintom&aacute;tica/FEVI baja)"),
        ("Soplo diast&oacute;lico retumbante en &aacute;pex + chasquido de apertura + refuerzo presist&oacute;lico", "Estenosis mitral (frecuente FA; reumatica)"),
        ("Fiebre + soplo nuevo o cambiante + fen&oacute;menos emb&oacute;licos + vegetaci&oacute;n en eco", "<b>Endocarditis infecciosa</b> (hemocultivos + ecocardiograma)"),
    ]),
]

ESTACIONES = [
    ("INSPECCION GENERAL Y SIGNOS VITALES", [
        ("Hipotensi&oacute;n + taquicardia + piel fr&iacute;a y sudorosa", "Mala perfusi&oacute;n perif&eacute;rica", "Relleno capilar &gt; 2 s", "<b>Shock cardiog&eacute;nico</b>", "TA baja con pulmones congestivos: pienso en fallo de bomba, pido eco urgente"),
        ("Herida penetrante en zona precordial", "Hipotensi&oacute;n + ruidos apagados", "Ingurgitaci&oacute;n yugular", "<b>Taponamiento por trauma penetrante</b>", "Herida en la caja de Beck: busco la tr&iacute;ada y preparo pericardiocentesis"),
        ("Cianosis + diafores&iacute;s + ansiedad", "Taquipnea + uso de musculatura accesoria", "Esputo asalmonado", "<b>Edema agudo de pulm&oacute;n</b>", "Paciente sentado y disn&eacute;ico: O2 y diur&eacute;tico mientras confirmo"),
        ("Fiebre + estigmas perif&eacute;ricos (Janeway/Osler)", "Petequias conjuntivales", "Hemorragias en astilla", "<b>Endocarditis infecciosa</b>", "Fiebre con soplo: saco tres hemocultivos antes del antibi&oacute;tico"),
    ]),
    ("PULSOS Y TENSION ARTERIAL", [
        ("Pulso irregularmente irregular", "D&eacute;ficit de pulso (FC central &gt; perif&eacute;rica)", "Sin onda P en ECG", "Fibrilaci&oacute;n auricular", "Tomo el pulso un minuto completo: irregular sin patr&oacute;n, sospecho FA"),
        ("Asimetr&iacute;a de pulsos entre ambos brazos", "Diferencia de TA &gt; 20 mmHg", "Pulso radial-femoral retardado", "<b>Disecci&oacute;n a&oacute;rtica</b>", "Mido TA en los dos brazos: si difieren mucho pienso en disecci&oacute;n"),
        ("Pulso parvus et tardus (peque&ntilde;o y retardado)", "Presi&oacute;n de pulso estrecha", "Soplo a&oacute;rtico asociado", "Estenosis a&oacute;rtica", "Pulso carot&iacute;deo lento y peque&ntilde;o: orienta a obstrucci&oacute;n a&oacute;rtica"),
        ("Pulso celer et magnus (salt&oacute;n/colapsante)", "Presi&oacute;n de pulso amplia", "Pulso de Corrigan", "Insuficiencia a&oacute;rtica", "Pulso que sube y baja r&aacute;pido: sugiere regurgitaci&oacute;n a&oacute;rtica"),
        ("Pulso paradojico (cae &gt; 10 mmHg en inspiraci&oacute;n)", "Hipotensi&oacute;n", "Taquicardia", "<b>Taponamiento card&iacute;aco</b>", "Si el pulso desaparece al inspirar mido el pulso paradojico"),
    ]),
    ("PALPACION PRECORDIAL", [
        ("Latido de la punta desplazado hacia abajo y afuera", "&Iacute;ctus amplio y sostenido", "Sobrecarga de volumen", "Cardiomegalia por IC con FEr", "Palpo el &iacute;ctus fuera de la l&iacute;nea medioclavicular: VI dilatado"),
        ("&Iacute;ctus sostenido y poco desplazado (sustained)", "Impulso apical en c&uacute;pula", "Hipertrofia VI", "Estenosis a&oacute;rtica / HTA cr&oacute;nica", "&Iacute;ctus potente pero localizado: hipertrofia por sobrecarga de presi&oacute;n"),
        ("Fr&eacute;mito sist&oacute;lico en foco a&oacute;rtico", "Thrill palpable", "Soplo &ge; grado IV", "Estenosis a&oacute;rtica severa", "Si palpo el thrill el soplo es al menos grado cuatro"),
        ("Frote pericardico palpable + dolor que mejora sentado", "Roce sist&oacute;lico-diast&oacute;lico", "Sin desplazamiento del &iacute;ctus", "Pericarditis aguda", "Palpo y ausculto el roce que cambia con la postura"),
    ]),
    ("AUSCULTACION POR FOCOS", [
        ("Soplo eyectivo en foco a&oacute;rtico (2&ordm; EID) irradiado a car&oacute;tidas", "Disminuci&oacute;n del 2&ordm; ruido", "Pulso parvus et tardus", "Estenosis a&oacute;rtica", "Ausculto en el 2&ordm; espacio derecho e irradia al cuello: estenosis a&oacute;rtica"),
        ("Soplo diast&oacute;lico decrescendo en foco a&oacute;rtico/Erb", "Mejor con paciente inclinado y en espiraci&oacute;n", "Presi&oacute;n de pulso amplia", "Insuficiencia a&oacute;rtica", "Lo oigo mejor con el paciente inclinado hacia delante en espiraci&oacute;n"),
        ("Soplo que aumenta en inspiraci&oacute;n en foco tric&uacute;spide (4&ordm; EID)", "Onda v yugular prominente", "Hepatomegalia pulsatil", "Insuficiencia tric&uacute;spide / fallo derecho", "El soplo que crece al inspirar es derecho: signo de Rivero-Carvallo"),
        ("Soplo holosist&oacute;lico en foco mitral (&aacute;pex) irradiado a axila", "S3 audible", "No var&iacute;a con respiraci&oacute;n", "Insuficiencia mitral", "Soplo en punta que va a la axila y no cambia con respirar: mitral"),
        ("Tercer ruido (S3) de galope protodiast&oacute;lico", "Ritmo de galope + crepitantes", "FEVI reducida", "IC con FE reducida", "El S3 en un adulto con disnea me dice sobrecarga de volumen"),
        ("Cuarto ruido (S4) presist&oacute;lico", "Ventr&iacute;culo r&iacute;gido", "FEVI preservada + HVI", "IC con FE preservada", "El S4 refleja un ventr&iacute;culo r&iacute;gido que cuesta llenar"),
        ("Frote pericardico de tres componentes", "Aumenta inclinado hacia delante", "ST difuso c&oacute;ncavo", "Pericarditis aguda", "El roce de cuero suena en s&iacute;stole y di&aacute;stole y cambia con la postura"),
    ]),
    ("INGURGITACION YUGULAR Y CONGESTION", [
        ("PVY elevada (&gt; 3 cm sobre &aacute;ngulo esternal) + reflujo hepatoyugular", "Edemas con f&oacute;vea", "Hepatomegalia congestiva", "IC derecha/congestiva", "Mido la presi&oacute;n venosa yugular a 45 grados: est&aacute; elevada"),
        ("IY que aumenta en inspiraci&oacute;n (signo de Kussmaul)", "Ruidos apagados", "Pulso paradojico", "<b>Taponamiento card&iacute;aco</b> (tr&iacute;ada de Beck)", "IY + hipotensi&oacute;n + ruidos apagados: tr&iacute;ada de Beck, taponamiento"),
        ("Onda a en ca&ntilde;&oacute;n en el pulso yugular", "Bradicardia + s&iacute;ncope", "Disociaci&oacute;n AV en ECG", "Bloqueo AV completo", "Las ondas a en ca&ntilde;&oacute;n me indican disociaci&oacute;n auriculoventricular"),
    ]),
]
