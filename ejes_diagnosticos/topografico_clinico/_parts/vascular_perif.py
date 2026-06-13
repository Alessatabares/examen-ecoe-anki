# -*- coding: utf-8 -*-
NAME = "Vascular periferico"

EJES = [
    ("Edema de miembro", [
        ("Edema unilateral con empastamiento y dolor en pantorrilla", "<b>Trombosis venosa profunda (TVP)</b> &rarr; riesgo de TEP"),
        ("Edema bilateral con fovea que mejora al elevar la pierna", "Insuficiencia venosa cr&oacute;nica"),
        ("Edema unilateral cr&oacute;nico SIN fovea con piel engrosada", "Linfedema"),
        ("Edema vespertino bimaleolar con varices visibles", "Insuficiencia venosa cr&oacute;nica"),
        ("Edema unilateral indoloro de dorso del pie con signo de Stemmer positivo", "Linfedema"),
        ("Edema con fovea profunda y duradera al presionar el tobillo", "Edema venoso o sist&eacute;mico"),
    ]),
    ("Dolor de miembro", [
        ("Dolor en pantorrilla al caminar que cede en reposo (claudicaci&oacute;n)", "Enfermedad arterial perif&eacute;rica (EAP) &rarr; ITB &lt; 0.9"),
        ("Dolor de reposo nocturno que mejora colgando la pierna fuera de la cama", "EAP cr&iacute;tica (isquemia cr&oacute;nica avanzada)"),
        ("Dolor s&uacute;bito intenso con miembro fr&iacute;o y p&aacute;lido", "<b>Isquemia arterial aguda</b> &rarr; las 6 P"),
        ("Dolor y pesadez de piernas que empeora de pie y mejora elevando", "Insuficiencia venosa cr&oacute;nica"),
        ("Dolor con empastamiento y aumento de temperatura en una pantorrilla", "<b>Trombosis venosa profunda (TVP)</b>"),
    ]),
    ("&Uacute;lcera de miembro", [
        ("&Uacute;lcera en regi&oacute;n maleolar interna, exudativa, bordes irregulares, poco dolorosa", "&Uacute;lcera venosa"),
        ("&Uacute;lcera distal en dedos o tal&oacute;n, en sacabocados, muy dolorosa, fondo p&aacute;lido", "&Uacute;lcera arterial (EAP)"),
        ("&Uacute;lcera con dermatitis ocre y lipodermatoesclerosis perimaleolar", "&Uacute;lcera venosa"),
        ("&Uacute;lcera en punta de dedo con pulsos ausentes y piel fr&iacute;a", "&Uacute;lcera arterial (EAP)"),
        ("&Uacute;lcera en zona de presi&oacute;n con ausencia de pulsos pedios", "&Uacute;lcera arterial (EAP)"),
    ]),
    ("Aspecto agudo del miembro", [
        ("Miembro fr&iacute;o, p&aacute;lido, sin pulso y doloroso de inicio brusco", "<b>Isquemia arterial aguda</b> &rarr; urgencia"),
        ("Pierna roja, caliente, edematosa y tensa de instauraci&oacute;n r&aacute;pida", "<b>Trombosis venosa profunda (TVP)</b>"),
        ("Par&aacute;lisis y paresia distal con cianosis moteada irreversible", "<b>Isquemia arterial aguda avanzada</b>"),
        ("Pie p&aacute;lido al elevar y rubicundo al colgar (Buerger positivo)", "EAP cr&iacute;tica"),
    ]),
]

ESTACIONES = [
    ("INSPECCION DEL MIEMBRO", [
        ("Dermatitis ocre maleolar", "Varices visibles", "&Uacute;lcera maleolar interna", "Insuficiencia venosa cr&oacute;nica", "&eacute;stasis venoso"),
        ("Palidez distal", "Atrofia cut&aacute;nea y p&eacute;rdida de vello", "U&ntilde;as distr&oacute;ficas", "Enfermedad arterial perif&eacute;rica (EAP)", "isquemia cr&oacute;nica"),
        ("Miembro p&aacute;lido y mot&eacute;ado", "Cianosis distal s&uacute;bita", "Dolor intenso de inicio brusco", "<b>Isquemia arterial aguda</b>", "urgencia vascular"),
        ("Edema sin fovea del dorso del pie", "Piel engrosada en piel de naranja", "Signo de Stemmer positivo", "Linfedema", "obstrucci&oacute;n linf&aacute;tica"),
    ]),
    ("PALPACION DE PULSOS PERIFERICOS", [
        ("Ausencia de pulso pedio y tibial posterior", "Soplo femoral", "Claudicaci&oacute;n al caminar", "Enfermedad arterial perif&eacute;rica (EAP)", "ITB &lt; 0.9"),
        ("Pulso ausente distal a la obstrucci&oacute;n", "Miembro fr&iacute;o y p&aacute;lido", "Inicio brusco", "<b>Isquemia arterial aguda</b>", "ausencia de Pulso (6 P)"),
        ("Pulsos perif&eacute;ricos conservados", "Edema con fovea", "Varices y telangiectasias", "Insuficiencia venosa cr&oacute;nica", "patolog&iacute;a venosa"),
        ("Pulsos presentes con edema unilateral sin fovea", "Sin claudicaci&oacute;n", "Stemmer positivo", "Linfedema", "patolog&iacute;a linf&aacute;tica"),
    ]),
    ("TEMPERATURA Y LLENADO CAPILAR", [
        ("Miembro fr&iacute;o al tacto", "Relleno capilar &gt; 3 segundos", "Palidez al elevar", "Enfermedad arterial perif&eacute;rica (EAP)", "hipoperfusi&oacute;n cr&oacute;nica"),
        ("Frialdad brusca de todo el miembro", "Relleno capilar muy enlentecido", "Dolor y palidez", "<b>Isquemia arterial aguda</b>", "Poiquilotermia (6 P)"),
        ("Aumento de temperatura unilateral en pantorrilla", "Eritema y tensi&oacute;n cut&aacute;nea", "Edema unilateral", "<b>Trombosis venosa profunda (TVP)</b>", "inflamaci&oacute;n venosa"),
        ("Temperatura normal con piel templada", "Relleno capilar conservado", "Edema vespertino", "Insuficiencia venosa cr&oacute;nica", "retorno venoso lento"),
    ]),
    ("SIGNOS DE TVP Y PRUEBA DE FOVEA", [
        ("Edema unilateral con empastamiento gemelar", "Dolor con la dorsiflexi&oacute;n del pie", "Aumento de per&iacute;metro &gt; 3 cm respecto a la otra pierna", "<b>Trombosis venosa profunda (TVP)</b>", "Wells &ge; 2 probable"),
        ("Eritema y calor unilateral", "Cord&oacute;n venoso palpable doloroso", "Riesgo de embolia pulmonar", "<b>Trombosis venosa profunda (TVP) con riesgo de TEP</b>", "urgencia"),
        ("Fovea presente y profunda al presionar el mal&eacute;olo", "Edema bilateral declive", "Mejora al elevar la pierna", "Insuficiencia venosa cr&oacute;nica", "edema con fovea"),
        ("Ausencia de fovea pese a edema marcado", "Piel dura y engrosada", "Signo de Stemmer positivo", "Linfedema", "edema SIN fovea"),
    ]),
]
