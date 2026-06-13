# -*- coding: utf-8 -*-
NAME = "Inmune"

EJES = [
    ("Reacci&oacute;n al&eacute;rgica aguda / anafilaxia", [
        ("Urticaria + estridor + hipotensi&oacute;n tras alimento o picadura", "<b>Anafilaxia (adrenalina IM YA)</b>"),
        ("Habones generalizados + prurito SIN compromiso de v&iacute;a a&eacute;rea ni hipotensi&oacute;n", "Urticaria aguda al&eacute;rgica"),
        ("Edema de labios y lengua + estridor + sibilancias minutos tras f&aacute;rmaco", "<b>Anafilaxia con compromiso de v&iacute;a a&eacute;rea</b>"),
        ("Broncoespasmo + hipotensi&oacute;n + s&iacute;ntomas digestivos tras contraste yodado", "<b>Anafilaxia (reacci&oacute;n bif&aacute;sica posible)</b>"),
        ("S&iacute;ncope + taquicardia + urticaria tras segunda dosis de antibi&oacute;tico", "<b>Anafilaxia (shock distributivo)</b>"),
        ("Prurito palmoplantar + sensaci&oacute;n de muerte inminente como pr&oacute;dromo", "Pr&oacute;dromo de anafilaxia"),
    ]),
    ("Edema facial / labial s&uacute;bito (angioedema)", [
        ("Edema de labios y lengua SIN urticaria en paciente que toma enalapril", "Angioedema por IECA (mediado por bradicinina)"),
        ("Episodios recurrentes de edema sin habones + dolor abdominal + antecedente familiar", "Angioedema hereditario por d&eacute;ficit de C1-INH"),
        ("Edema de glotis SIN urticaria que NO responde a adrenalina ni antihistam&iacute;nicos", "<b>Angioedema bradicin&iacute;nico (v&iacute;a a&eacute;rea en riesgo)</b>"),
        ("Edema facial + urticaria + prurito tras nuevo f&aacute;rmaco", "Angioedema histamin&eacute;rgico (al&eacute;rgico)"),
        ("Edema laringeo recurrente con C4 bajo y C1-INH funcional disminuido", "Angioedema hereditario tipo II"),
        ("Edema sin habones de inicio tard&iacute;o (a&ntilde;os) con paraproteinemia", "Angioedema adquirido por d&eacute;ficit de C1-INH"),
    ]),
    ("Exantema farmacol&oacute;gico grave con afectaci&oacute;n sist&eacute;mica", [
        ("Exantema + fiebre + edema facial + eosinofilia 2-6 semanas tras f&aacute;rmaco", "<b>DRESS (afectaci&oacute;n de &oacute;rgano: h&iacute;gado/ri&ntilde;&oacute;n)</b>"),
        ("Lesiones en diana + despegamiento &lt;10% superficie + afectaci&oacute;n de mucosas", "<b>S&iacute;ndrome de Stevens-Johnson (SSJ)</b>"),
        ("Despegamiento &gt;30% de la piel + Nikolsky positivo + mucosas erosionadas", "<b>Necr&oacute;lisis epid&eacute;rmica t&oacute;xica (NET)</b>"),
        ("Exantema + eosinofilia + transaminasas elevadas + linfadenopat&iacute;a", "<b>DRESS (s&iacute;ndrome de hipersensibilidad)</b>"),
        ("Pustulas est&eacute;riles sobre base eritematosa + fiebre + neutrofilia r&aacute;pida tras f&aacute;rmaco", "PEGA (pustulosis exantem&aacute;tica aguda generalizada)"),
        ("Exantema maculopapular leve sin mucosas ni eosinofilia tras antibi&oacute;tico", "Exantema medicamentoso simple (benigno)"),
    ]),
]

ESTACIONES = [
    ("VALORACI&Oacute;N DE V&Iacute;A A&Eacute;REA / RESPIRATORIA", [
        ("Estridor inspiratorio", "Edema de labios y lengua", "Voz apagada o disfon&iacute;a", "<b>Anafilaxia / angioedema con compromiso de v&iacute;a a&eacute;rea</b>", "adrenalina IM 0.5 mg en vasto externo YA + preparar v&iacute;a a&eacute;rea"),
        ("Edema de glotis SIN urticaria", "Toma de IECA", "No responde a adrenalina", "<b>Angioedema bradicin&iacute;nico (IECA / C1-INH)</b>", "suspender IECA + icatibant o C1-INH; asegurar v&iacute;a a&eacute;rea"),
        ("Sibilancias + broncoespasmo", "Tiraje supraesternal", "Saturaci&oacute;n &lt; 92%", "<b>Anafilaxia (afectaci&oacute;n respiratoria)</b>", "adrenalina IM + ox&iacute;geno + broncodilatador"),
        ("Edema lingual progresivo", "Imposibilidad de tragar saliva", "Disnea creciente", "<b>Angioedema de v&iacute;a a&eacute;rea (riesgo de obstrucci&oacute;n)</b>", "intubaci&oacute;n precoz antes de que progrese el edema"),
    ]),
    ("INSPECCI&Oacute;N DE PIEL Y MUCOSAS", [
        ("Habones + prurito generalizado", "Mejora con antihistam&iacute;nico", "Sin afectaci&oacute;n de mucosas", "Urticaria aguda al&eacute;rgica", "antihistam&iacute;nico; vigilar progresi&oacute;n a anafilaxia"),
        ("Edema facial SIN habones", "Recurrente + antecedente familiar", "Dolor abdominal asociado", "Angioedema hereditario por d&eacute;ficit de C1-INH", "C1-INH o icatibant; NO responde a adrenalina"),
        ("Lesiones en diana + mucosas erosionadas", "Signo de Nikolsky positivo", "Despegamiento cut&aacute;neo", "<b>SSJ / NET</b>", "suspender f&aacute;rmaco + unidad de quemados + soporte"),
        ("Exantema + edema facial", "Eosinofilia en hemograma", "Linfadenopat&iacute;a", "<b>DRESS</b>", "suspender f&aacute;rmaco + corticoides + control de &oacute;rgano"),
    ]),
    ("SIGNOS VITALES / HIPOTENSI&Oacute;N", [
        ("Hipotensi&oacute;n + taquicardia", "Urticaria + estridor", "Inicio en minutos tras desencadenante", "<b>Anafilaxia (shock distributivo)</b>", "adrenalina IM YA + dec&uacute;bito con piernas elevadas + fluidos"),
        ("Hipotensi&oacute;n refractaria a fluidos", "Antecedente de reacci&oacute;n previa", "Prurito palmoplantar prodr&oacute;mico", "<b>Anafilaxia grave</b>", "repetir adrenalina IM cada 5-10 min + cristaloides en bolo"),
        ("Fiebre + taquicardia", "Exantema extenso + eosinofilia", "Transaminasas elevadas", "<b>DRESS (afectaci&oacute;n sist&eacute;mica)</b>", "suspender f&aacute;rmaco + corticoides sist&eacute;micos"),
        ("Fiebre + hipotensi&oacute;n", "Despegamiento &gt;30% + Nikolsky", "P&eacute;rdida de l&iacute;quidos por piel", "<b>NET (riesgo vital)</b>", "manejo como gran quemado + reposici&oacute;n hidroelectrol&iacute;tica"),
    ]),
]
