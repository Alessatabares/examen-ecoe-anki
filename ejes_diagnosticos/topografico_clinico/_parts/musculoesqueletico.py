# -*- coding: utf-8 -*-
NAME = "Musculoesqueletico"

EJES = [
    ("Monoartritis aguda", [
        ("Primer dedo del pie (podagra), inicio nocturno, varon, hiperuricemia", "Gota"),
        ("Cristales de urato monos&oacute;dico, birrefringencia negativa, tofos", "Gota"),
        ("Rodilla caliente y tumefacta, fiebre, no puede apoyar, artrocentesis purulenta", "<b>Artritis s&eacute;ptica</b>"),
        ("Cristales de pirofosfato c&aacute;lcico, birrefringencia positiva, anciano, condrocalcinosis", "Pseudogota"),
        ("Monoartritis aguda en cualquier articulaci&oacute;n: artrocentesis SIEMPRE para descartar s&eacute;ptica", "<b>Artritis s&eacute;ptica</b>"),
        ("Tumefacci&oacute;n migratoria, joven sexualmente activo, tenosinovitis y p&uacute;stulas", "Artritis gonoc&oacute;cica"),
    ]),
    ("Poliartritis", [
        ("Simetrica, peque&ntilde;as articulaciones de manos, rigidez matutina &gt; 1 hora", "Artritis reumatoide"),
        ("Anti-CCP positivo, factor reumatoide, erosiones, desviaci&oacute;n cubital", "Artritis reumatoide"),
        ("Mujer joven, rash malar, fotosensibilidad, artritis no erosiva, ANA positivo", "Lupus eritematoso sist&eacute;mico"),
        ("Dactilitis (dedo en salchicha), psoriasis cut&aacute;nea, afectaci&oacute;n de interfal&aacute;ngicas distales", "Artritis psori&aacute;sica"),
        ("Oligoartritis asim&eacute;trica de miembros inferiores, entesitis, uretritis previa", "Artritis reactiva"),
    ]),
    ("Debilidad de cinturas (&gt; 50 a&ntilde;os)", [
        ("Dolor y rigidez de cintura escapular y pelvica, VSG y PCR muy elevadas", "Polimialgia reum&aacute;tica"),
        ("Asociaci&oacute;n con cefalea, claudicaci&oacute;n mandibular y amaurosis", "<b>Arteritis de c&eacute;lulas gigantes</b>"),
        ("Debilidad proximal sim&eacute;trica, elevaci&oacute;n de CK, dificultad para peinarse o subir escaleras", "Polimiositis"),
        ("Debilidad proximal con rash heliotropo y p&aacute;pulas de Gottron", "Dermatomiositis"),
    ]),
    ("Dolor &oacute;seo", [
        ("Dolor tras traumatismo, deformidad, impotencia funcional, crepitaci&oacute;n", "Fractura"),
        ("Dolor &oacute;seo localizado con fiebre, eritema y calor sobre el hueso", "Osteomielitis"),
        ("Fractura por fragilidad (vertebral, cadera, mu&ntilde;eca), T-score &le; -2.5", "Osteoporosis"),
        ("Dolor &oacute;seo nocturno, antecedente de neoplasia (mama, pr&oacute;stata, pulm&oacute;n), hipercalcemia", "Met&aacute;stasis &oacute;seas"),
        ("Dolor &oacute;seo, anemia, insuficiencia renal, hipercalcemia, lesiones l&iacute;ticas en sacabocados", "Mieloma m&uacute;ltiple"),
    ]),
    ("Lumbalgia y dolor radicular", [
        ("Dolor lumbar que mejora con reposo, empeora con esfuerzo, sin red flags", "Lumbalgia mec&aacute;nica"),
        ("Dolor irradiado por la pierna (citi&aacute;tica), Lasegue positivo, par&eacute;sia de un dermatoma", "Hernia discal"),
        ("Lumbalgia con fiebre, p&eacute;rdida de peso, dolor nocturno o antecedente de c&aacute;ncer: red flags", "Lumbalgia secundaria (red flag)"),
        ("Anestesia en silla de montar, retenci&oacute;n urinaria, p&eacute;rdida de tono del esf&iacute;nter anal", "<b>S&iacute;ndrome de cola de caballo</b>"),
        ("Dolor inflamatorio, rigidez matutina, var&oacute;n joven, HLA-B27, sacroile&iacute;tis", "Espondilitis anquilosante"),
    ]),
]

ESTACIONES = [
    ("INSPECCION ARTICULAR", [
        ("Tumefacci&oacute;n", "Eritema", "Primer dedo del pie", "Gota", "podagra cl&aacute;sica"),
        ("Desviaci&oacute;n cubital", "Dedos en cuello de cisne", "Sim&eacute;trica en manos", "Artritis reumatoide", "deformidad cr&oacute;nica"),
        ("Dedo en salchicha", "Placas psori&aacute;sicas", "Pitting ungueal", "Artritis psori&aacute;sica", "dactilitis"),
        ("Tofos en pabell&oacute;n auricular", "N&oacute;dulos blanquecinos", "Hiperuricemia", "Gota", "dep&oacute;sito de urato"),
        ("Rash malar en alas de mariposa", "Fotosensibilidad", "Artritis no erosiva", "Lupus eritematoso sist&eacute;mico", "signo cut&aacute;neo gu&iacute;a"),
    ]),
    ("PALPACION", [
        ("Calor local", "Derrame articular", "Fiebre, no apoya", "<b>Artritis s&eacute;ptica</b>", "aspirar SIEMPRE"),
        ("Calor y derrame en rodilla", "Anciano", "Condrocalcinosis radiol&oacute;gica", "Pseudogota", "pirofosfato c&aacute;lcico"),
        ("Dolor a la palpaci&oacute;n &oacute;sea", "Fiebre", "Eritema sobre hueso", "Osteomielitis", "infecci&oacute;n &oacute;sea"),
        ("Crepitaci&oacute;n", "Deformidad", "Traumatismo previo", "Fractura", "soluci&oacute;n de continuidad"),
        ("N&oacute;dulos reum&aacute;ticos en codos", "Sim&eacute;trico", "Anti-CCP positivo", "Artritis reumatoide", "afectaci&oacute;n cr&oacute;nica"),
    ]),
    ("RANGO DE MOVIMIENTO", [
        ("Limitaci&oacute;n dolorosa de cinturas", "VSG y PCR muy altas", "&gt; 50 a&ntilde;os", "Polimialgia reum&aacute;tica", "rigidez proximal"),
        ("Debilidad proximal sim&eacute;trica", "CK elevada", "No puede subir escaleras", "Polimiositis", "miopat&iacute;a inflamatoria"),
        ("Rigidez matutina &gt; 1 hora", "Mejora con el movimiento", "Sim&eacute;trica", "Artritis reumatoide", "patr&oacute;n inflamatorio"),
        ("P&eacute;rdida de expansi&oacute;n tor&aacute;cica", "Test de Schober positivo", "HLA-B27", "Espondilitis anquilosante", "columna r&iacute;gida"),
    ]),
    ("EXPLORACION DE COLUMNA", [
        ("Lasegue positivo", "Par&eacute;sia radicular de un dermatoma", "Dolor irradiado por la pierna", "Hernia discal", "compresi&oacute;n de ra&iacute;z"),
        ("Anestesia en silla de montar", "P&eacute;rdida de tono del esf&iacute;nter anal", "Retenci&oacute;n urinaria", "<b>S&iacute;ndrome de cola de caballo</b>", "urgencia quir&uacute;rgica"),
        ("Dolor lumbar mec&aacute;nico", "Mejora con reposo", "Sin red flags", "Lumbalgia mec&aacute;nica", "exploraci&oacute;n normal"),
        ("Dolor nocturno con fiebre", "P&eacute;rdida de peso", "Antecedente de c&aacute;ncer", "Lumbalgia secundaria (red flag)", "se&ntilde;al de alarma"),
        ("Sacroile&iacute;tis", "Dolor inflamatorio que despierta", "Var&oacute;n joven", "Espondilitis anquilosante", "dolor de ritmo inflamatorio"),
    ]),
    ("PATRON DE AFECTACION", [
        ("Monoartritis aguda", "Artrocentesis con cristales o pus", "Caliente y tumefacta", "<b>Artritis s&eacute;ptica</b>", "mono = aspirar"),
        ("Poliartritis sim&eacute;trica de peque&ntilde;as articulaciones", "Anti-CCP", "Rigidez matutina", "Artritis reumatoide", "patr&oacute;n sim&eacute;trico"),
        ("Oligoartritis asim&eacute;trica de miembros inferiores", "Entesitis", "Uretritis previa", "Artritis reactiva", "patr&oacute;n asim&eacute;trico"),
        ("Dolor &oacute;seo difuso nocturno", "Hipercalcemia", "Neoplasia conocida", "Met&aacute;stasis &oacute;seas", "afectaci&oacute;n &oacute;sea"),
        ("Fractura por fragilidad", "T-score &le; -2.5", "Sin traumatismo significativo", "Osteoporosis", "hueso fr&aacute;gil"),
    ]),
]
