NAME = "Ap. reproductor femenino"

EJES = [
    ("Sangrado uterino anormal", [
        ("Sangrado intermenstrual + &uacute;tero aumentado e irregular", "Miomas / leiomiomas"),
        ("Menometrorragia en edad f&eacute;rtil sin causa estructural", "Sangrado uterino disfuncional"),
        ("Sangrado posmenopausico (alarma) &rarr; descartar siempre", "Ca de endometrio"),
        ("Sangrado poscoital en mujer con cuello visible an&oacute;malo", "Ca cervicouterino"),
        ("Goteo escaso + cuello fri&aacute;ble e inflamado", "Cervicitis"),
        ("Sangrado del primer trimestre con &beta;-hCG presente", "Amenaza de aborto / aborto"),
    ]),
    ("Dolor p&eacute;lvico", [
        ("Dolor s&uacute;bito intenso unilateral + n&aacute;useas + masa anexial", "<b>Torsi&oacute;n ov&aacute;rica</b>"),
        ("Amenorrea + dolor + inestabilidad hemodin&aacute;mica + abdomen agudo", "<b>Embarazo ect&oacute;pico roto</b>"),
        ("Dolor a la movilizaci&oacute;n cervical + fiebre + flujo purulento", "EPI (enfermedad p&eacute;lvica inflamatoria)"),
        ("Masa anexial qu&iacute;stica asintom&aacute;tica o con dolor hipog&aacute;strico leve, sin signos de torsi&oacute;n", "Quiste ov&aacute;rico funcional"),
        ("Dismenorrea progresiva + dispareunia profunda", "Endometriosis"),
        ("Distensi&oacute;n + ascitis + masa ov&aacute;rica s&oacute;lida en posmenop&aacute;usica", "Ca de ovario"),
    ]),
    ("Hemorragia obst&eacute;trica", [
        ("Dolor abdominal s&uacute;bito + hipertono uterino + sangrado oscuro escaso", "<b>DPPNI (abruptio placentae)</b>"),
        ("Sangrado rojo brillante INDOLORO en 2&ordm;-3&ordm; trimestre", "Placenta previa"),
        ("Amenorrea + dolor anexial + &beta;-hCG &gt; 1500 sin saco intrauterino", "<b>Embarazo ect&oacute;pico</b>"),
        ("Sangrado + dolor c&oacute;lico + cuello dilatado con restos", "Aborto en curso / incompleto"),
        ("Sangrado escaso + cuello cerrado + embri&oacute;n vivo", "Amenaza de aborto"),
        ("Hemorragia posparto + &uacute;tero blando que no se contrae", "Atonia uterina"),
    ]),
    ("HTA y edema en el embarazo", [
        ("TA &ge; 140/90 + proteinuria tras 20 semanas", "Preeclampsia"),
        ("Preeclampsia + cefalea, escotomas, epigastralgia + plaquetopenia", "Preeclampsia grave / s&iacute;ndrome HELLP"),
        ("HTA + proteinuria + convulsiones tonicocl&oacute;nicas", "<b>Eclampsia</b>"),
        ("HTA cr&oacute;nica previa al embarazo o antes de 20 sem", "HTA cr&oacute;nica"),
        ("Edema fisiol&oacute;gico de miembros sin HTA ni proteinuria", "Edema gestacional benigno"),
    ]),
    ("Flujo vaginal", [
        ("Flujo gris-blanquecino homog&eacute;neo + olor a pescado (KOH +)", "Vaginosis bacteriana"),
        ("Flujo blanco grumoso (reques&oacute;n) + prurito y eritema", "Candidiasis vulvovaginal"),
        ("Flujo amarillo-verdoso espumoso + cuello en fresa", "Tricomoniasis (ITS)"),
        ("Flujo mucopurulento cervical + dolor + pareja con uretritis", "Cervicitis por clamidia / gonococo"),
        ("&Uacute;lcera genital indolora de bordes indurados", "S&iacute;filis (ITS)"),
    ]),
    ("Masa mamaria", [
        ("Masa dura, fija, irregular + retracci&oacute;n y piel de naranja", "Ca de mama"),
        ("N&oacute;dulo bien delimitado, m&oacute;vil, el&aacute;stico en mujer joven", "Fibroadenoma"),
        ("Mama roja, caliente, dolorosa + fiebre en lactancia", "Mastitis"),
        ("N&oacute;dulos m&uacute;ltiples dolorosos que cambian con el ciclo", "Cambios fibroqu&iacute;sticos"),
        ("Eczema unilateral del pez&oacute;n que no cura", "Enfermedad de Paget de la mama"),
    ]),
]

ESTACIONES = [
    ("EXPLORACION MAMARIA", [
        ("Masa p&eacute;trea fija a planos profundos", "Retracci&oacute;n del pez&oacute;n", "Piel de naranja + adenopat&iacute;a axilar dura", "Ca de mama", "infiltraci&oacute;n y diseminaci&oacute;n linf&aacute;tica"),
        ("N&oacute;dulo liso, m&oacute;vil, bien delimitado", "El&aacute;stico, indoloro", "Sin cambios cut&aacute;neos ni adenopat&iacute;as", "Fibroadenoma", "tumor benigno de mujer joven"),
        ("Cuadrante eritematoso, caliente y doloroso", "Fiebre durante la lactancia", "Posible fluctuaci&oacute;n si absceso", "Mastitis puerperal", "infecci&oacute;n del tejido mamario"),
        ("Eczema del pez&oacute;n-are&oacute;la que no cicatriza", "Prurito y descamaci&oacute;n unilateral", "A veces masa subyacente", "Enfermedad de Paget", "carcinoma intraductal del pez&oacute;n"),
    ]),
    ("ABDOMEN OBSTETRICO", [
        ("Altura uterina acorde con amenorrea", "Maniobras de Leopold para situaci&oacute;n fetal", "Foco cardiaco fetal audible", "Embarazo normoevolutivo", "valoraci&oacute;n del crecimiento y est&aacute;tica fetal"),
        ("&Uacute;tero le&ntilde;oso, hipert&oacute;nico y doloroso", "Sangrado oscuro escaso + sufrimiento fetal", "Madre con HTA o trauma previo", "<b>DPPNI</b>", "desprendimiento placentario, urgencia obst&eacute;trica"),
        ("Altura uterina mayor a la esperada", "Movimientos fetales presentes", "Sin dolor ni sangrado", "Polihidramnios / macrosomia", "discordancia altura-edad gestacional"),
        ("Contracciones uterinas r&iacute;tmicas palpables", "Endurecimiento abdominal peri&oacute;dico", "Borramiento cervical asociado", "Trabajo de parto", "din&aacute;mica uterina activa"),
    ]),
    ("ABDOMEN GINECOLOGICO", [
        ("Masa hipog&aacute;strica firme e irregular", "Crece desde la pelvis, m&oacute;vil", "Sangrado uterino abundante asociado", "Miomatosis uterina", "&uacute;tero aumentado por leiomiomas"),
        ("Defensa y dolor s&uacute;bito en fosa il&iacute;aca", "Masa anexial palpable y dolorosa", "N&aacute;useas y v&oacute;mitos", "<b>Torsi&oacute;n ov&aacute;rica</b>", "isquemia anexial, urgencia quir&uacute;rgica"),
        ("Distensi&oacute;n con masa p&eacute;lvica s&oacute;lida fija", "Ascitis y matidez desplazable", "P&eacute;rdida de peso en posmenop&aacute;usica", "Ca de ovario", "signos de tumor ov&aacute;rico avanzado"),
        ("Dolor a la palpaci&oacute;n de fosas il&iacute;acas bilateral", "Fiebre + defensa + flujo purulento", "Reacci&oacute;n peritoneal baja", "EPI complicada", "inflamaci&oacute;n p&eacute;lvica ascendente"),
    ]),
    ("ESPECULOSCOPIA", [
        ("Cuello con lesi&oacute;n exof&iacute;tica fri&aacute;ble que sangra", "Sangrado poscoital al contacto", "Secreci&oacute;n serohem&aacute;tica", "Ca cervicouterino", "tumor cervical visible al esp&eacute;culo"),
        ("Cuello eritematoso con secreci&oacute;n mucopurulenta", "Sangra con facilidad al roce", "Sin masa exof&iacute;tica", "Cervicitis", "inflamaci&oacute;n del cuello uterino"),
        ("Flujo gris adherente que recubre paredes", "Olor a pescado al a&ntilde;adir KOH", "pH vaginal &gt; 4.5", "Vaginosis bacteriana", "disbiosis vaginal"),
        ("Cuello con punteado hemorr&aacute;gico (en fresa)", "Flujo verdoso espumoso abundante", "Eritema vaginal difuso", "Tricomoniasis", "ITS por protozoo flagelado"),
        ("Saco gestacional o restos asomando por OCE", "Cuello dilatado + sangrado activo", "Dolor c&oacute;lico hipog&aacute;strico", "Aborto en curso", "expulsi&oacute;n del producto de la gestaci&oacute;n"),
    ]),
    ("TACTO BIMANUAL", [
        ("Dolor intenso a la movilizaci&oacute;n cervical", "Anexos engrosados y dolorosos", "Fiebre y flujo purulento", "EPI", "signo del candelabro por irritaci&oacute;n anexial"),
        ("Masa anexial dolorosa + cuello cerrado", "Dolor a la movilizaci&oacute;n + amenorrea", "&beta;-hCG positiva con &uacute;tero vac&iacute;o", "<b>Embarazo ect&oacute;pico</b>", "gestaci&oacute;n extrauterina, riesgo de rotura"),
        ("&Uacute;tero aumentado, irregular y nodular", "Consistencia firme, indoloro", "M&oacute;vil con el cuello", "Miomas uterinos", "&uacute;tero polimiomatoso"),
        ("Masa anexial qu&iacute;stica lisa y m&oacute;vil", "Dolor leve o ausente", "Sin signos sist&eacute;micos", "Quiste de ovario", "tumoraci&oacute;n anexial benigna"),
    ]),
    ("SIGNOS VITALES Y TA EN EMBARAZO", [
        ("TA &ge; 140/90 en gestante &gt; 20 sem", "Proteinuria en tira reactiva", "Edemas y aumento brusco de peso", "Preeclampsia", "trastorno hipertensivo del embarazo"),
        ("HTA grave + cefalea, fosfenos, epigastralgia", "Hiperreflexia y clonus", "Plaquetas bajas + transaminasas altas", "Preeclampsia grave / HELLP", "preeclampsia con criterios de gravedad"),
        ("HTA + proteinuria + crisis convulsiva", "P&eacute;rdida de conciencia posictal", "Riesgo materno-fetal inminente", "<b>Eclampsia</b>", "convulsi&oacute;n por preeclampsia, urgencia vital"),
        ("Taquicardia + hipotensi&oacute;n + palidez en gestante", "Sangrado o dolor abdominal s&uacute;bito", "Relleno capilar lento", "<b>Embarazo ect&oacute;pico roto / DPPNI</b>", "shock hemorr&aacute;gico obst&eacute;trico"),
    ]),
]
