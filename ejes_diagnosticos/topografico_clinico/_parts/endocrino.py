# -*- coding: utf-8 -*-
NAME = "Endocrino / Suprarrenal"

EJES = [
    ("Poliuria / polidipsia", [
        ("Poliuria con orina diluida (densidad baja) que no cede al restringir l&iacute;quidos; Na+ normal-alto seg&uacute;n el acceso al agua", "Diabetes ins&iacute;pida (central o nefrog&eacute;nica)"),
        ("Poliuria-polidipsia con glucemia &gt; 200 mg/dL, p&eacute;rdida de peso y cetonuria", "Diabetes mellitus tipo 1"),
        ("Poliuria-polidipsia insidiosa en adulto obeso con acantosis nigricans", "Diabetes mellitus tipo 2"),
        ("Polidipsia compulsiva + orina diluida + hiponatremia dilucional (psiqui&aacute;trico/potomania)", "Polidipsia primaria (el SIADH NO da poliuria: retiene agua y cursa con oliguria)"),
        ("Poliuria con hipercalcemia, estre&ntilde;imiento y litiasis renal recurrente", "Hiperparatiroidismo primario"),
        ("Poliuria con HTA, hipopotasemia y debilidad muscular", "Hiperaldosteronismo primario (Conn)"),
    ]),
    ("Alteraci&oacute;n de peso / intolerancia t&eacute;rmica", [
        ("P&eacute;rdida de peso con apetito conservado, intolerancia al calor, temblor y TSH suprimida (opuesta a la cl&iacute;nica)", "Hipertiroidismo"),
        ("Aumento de peso, intolerancia al fr&iacute;o, estre&ntilde;imiento y TSH elevada (opuesta a la cl&iacute;nica)", "Hipotiroidismo"),
        ("Fiebre, agitaci&oacute;n, taquiarritmia e insuficiencia cardiaca en paciente tirot&oacute;xico", "<b>Tormenta tiroidea</b>"),
        ("Hipotermia, bradicardia, estupor y edema sin f&oacute;vea tras suspender levotiroxina", "<b>Coma mixedematoso</b>"),
        ("Aumento de peso central, cara de luna llena, estr&iacute;as v&iacute;nicas y debilidad proximal", "S&iacute;ndrome de Cushing"),
        ("Crecimiento acral (manos, pies, prognatismo) y cefalea con campos visuales alterados", "Acromegalia"),
    ]),
    ("HTA secundaria", [
        ("HTA parox&iacute;stica con cefalea puls&aacute;til, sudoraci&oacute;n y palpitaciones (tr&iacute;ada cl&aacute;sica)", "<b>Feocromocitoma en crisis</b>"),
        ("HTA mantenida con hipopotasemia espont&aacute;nea y alcalosis metab&oacute;lica", "Hiperaldosteronismo primario (Conn)"),
        ("HTA con obesidad central, equimosis f&aacute;ciles e hiperglucemia", "S&iacute;ndrome de Cushing"),
        ("HTA con intolerancia al calor, taquicardia y bocio difuso", "Hipertiroidismo"),
        ("HTA en joven con crecimiento acral y diabetes de novo", "Acromegalia"),
        ("HTA con hipercalcemia y nefrolitiasis", "Hiperparatiroidismo primario"),
    ]),
    ("Hipo / hiperglucemia", [
        ("Hiperglucemia &gt; 250 con acidosis metab&oacute;lica, cetonas y respiraci&oacute;n de Kussmaul", "<b>Cetoacidosis diab&eacute;tica (CAD)</b>"),
        ("Hiperglucemia extrema &gt; 600 con osmolaridad alta, deshidrataci&oacute;n y sin cetosis relevante", "<b>Estado hiperosmolar hipergluc&eacute;mico (EHH)</b>"),
        ("Hipoglucemia de ayuno con s&iacute;ntomas neurogluc&oacute;penos que ceden con glucosa (tr&iacute;ada de Whipple)", "Insulinoma"),
        ("Hipoglucemia, hipotensi&oacute;n e hiperpigmentaci&oacute;n con hipoNa+ e hiperK+", "Insuficiencia suprarrenal primaria (Addison)"),
        ("Hipoglucemia con astenia, p&eacute;rdida de vello y amenorrea (panhipopituitarismo)", "Panhipopituitarismo"),
        ("Hiperglucemia con obesidad central, estr&iacute;as e HTA", "S&iacute;ndrome de Cushing"),
    ]),
    ("Fatiga / hiper-hipocalcemia / hiperpigmentaci&oacute;n / hipopituitarismo", [
        ("Hipercalcemia con PTH elevada, estre&ntilde;imiento, poliuria y litiasis (huesos, piedras, quejidos)", "Hiperparatiroidismo primario"),
        ("Hipocalcemia con tetania, parestesias peribucales y signos de Chvostek-Trousseau", "Hipoparatiroidismo"),
        ("Fractura vertebral por fragilidad con DMO T-score &le; -2.5", "Osteoporosis"),
        ("Astenia, hipotensi&oacute;n e hiperpigmentaci&oacute;n de pliegues y mucosas con hipoNa+ e hiperK+", "Insuficiencia suprarrenal primaria (Addison)"),
        ("Shock, dolor abdominal y fiebre con hipoglucemia tras estr&eacute;s o suspensi&oacute;n de corticoides", "<b>Crisis suprarrenal</b>"),
        ("Galactorrea, amenorrea y disminuci&oacute;n de libido con campos visuales alterados", "Prolactinoma"),
        ("Astenia, p&aacute;lidez, p&eacute;rdida de vello axilar-pubiano y fallo gonadal-tiroideo-suprarrenal", "Panhipopituitarismo"),
    ]),
]

ESTACIONES = [
    ("INSPECCION GENERAL / HABITUS", [
        ("Cara de luna llena", "Giba dorsal y estr&iacute;as v&iacute;nicas abdominales", "Obesidad central con extremidades delgadas", "S&iacute;ndrome de Cushing", "Busca equimosis y debilidad proximal al levantarse de la silla"),
        ("Exoftalmos bilateral con retracci&oacute;n palpebral", "Mirada fija y signo de lid-lag", "Bocio difuso con temblor fino", "Hipertiroidismo (Graves)", "Describe la oftalmopat&iacute;a: proptosis y signo de von Graefe"),
        ("Facies abotargada y edema periorbitario", "Macroglosia y piel seca-amarillenta", "Edema sin f&oacute;vea generalizado (mixedema)", "Hipotiroidismo", "El mixedema del hipotiroidismo es generalizado y sin f&oacute;vea; el mixedema PREtibial localizado es de Graves, no de hipotiroidismo"),
        ("Crecimiento de manos, pies y mand&iacute;bula", "Prognatismo y rasgos toscos", "Separaci&oacute;n dental y macroglosia", "Acromegalia", "Compara fotos antiguas y mide el aumento de la talla del anillo-zapato"),
        ("Hiperpigmentaci&oacute;n de pliegues, cicatrices y mucosa oral", "Adelgazamiento e hipotensi&oacute;n", "Aspecto de astenia intensa", "Insuficiencia suprarrenal primaria (Addison)", "La hiperpigmentaci&oacute;n por ACTH-MSH alta distingue Addison del hipopituitarismo"),
    ]),
    ("CUELLO / TIROIDES (palpaci&oacute;n + soplo)", [
        ("Bocio difuso, blando y simetrico", "Fr&eacute;mito a la palpaci&oacute;n", "Soplo tiroideo a la auscultaci&oacute;n", "Hipertiroidismo (Graves)", "El soplo refleja hipervascularizaci&oacute;n; ausculta el polo superior"),
        ("N&oacute;dulo tiroideo &uacute;nico, firme y desplazable con la degluci&oacute;n", "Sin adenopat&iacute;as cervicales", "Eutiroideo o aut&oacute;nomo", "N&oacute;dulo tiroideo", "Pide al paciente que trague mientras palpas por detr&aacute;s"),
        ("Tiroides aumentada, firme y bocelada (de superficie irregular)", "Consistencia g&oacute;mica", "Hipotiroidismo asociado", "Tiroiditis de Hashimoto", "Correlaciona la consistencia firme con TSH elevada"),
        ("Cuello sin bocio palpable, piel seca", "Bradicardia y voz r&oacute;nca", "Relajaci&oacute;n lenta de reflejos", "Hipotiroidismo", "Aunque no palpes bocio, la TSH elevada confirma el hipotiroidismo"),
        ("Tiroides dolorosa, dura y adherida de crecimiento r&aacute;pido", "Adenopat&iacute;as y disfon&iacute;a", "Posible compresi&oacute;n traqueal", "Carcinoma anapl&aacute;sico de tiroides", "El crecimiento r&aacute;pido y doloroso obliga a descartar malignidad"),
    ]),
    ("SIGNOS DE TIROTOXICOSIS", [
        ("Temblor fino distal con brazos extendidos", "Taquicardia sinusal o fibrilaci&oacute;n auricular", "Piel caliente y sudorosa", "Hipertiroidismo", "Coloca una hoja sobre las manos extendidas para evidenciar el temblor"),
        ("Fiebre alta, agitaci&oacute;n y delirio", "Taquiarritmia con insuficiencia cardiaca", "Diarrea y v&oacute;mitos con deshidrataci&oacute;n", "<b>Tormenta tiroidea</b>", "Aplica la escala de Burch-Wartofsky ante tirotoxicosis descompensada"),
        ("Palpitaciones y p&eacute;rdida de peso con apetito conservado", "Intolerancia al calor e hiperdefecaci&oacute;n", "TSH suprimida con T4 libre alta", "Hipertiroidismo", "La TSH baja con T4 alta confirma tirotoxicosis primaria"),
        ("Crisis de HTA, cefalea, sudoraci&oacute;n y palpitaciones", "Palidez paroxistica y ansiedad", "Hiperglucemia transitoria", "<b>Feocromocitoma en crisis</b>", "Diferencia del hipertiroidismo por el car&aacute;cter paroxistico y la palidez"),
    ]),
    ("PIEL / PIGMENTACION", [
        ("Hiperpigmentaci&oacute;n de codos, nudillos, l&iacute;neas palmares y mucosa", "Vit&iacute;ligo asociado", "HipoTA ortost&aacute;tica", "Insuficiencia suprarrenal primaria (Addison)", "El exceso de ACTH-MSH oscurece pliegues y cicatrices"),
        ("Estr&iacute;as anchas v&iacute;nicas (purp&uacute;reas), equimosis y piel fina", "Hirsutismo y acn&eacute;", "Mala cicatrizaci&oacute;n", "S&iacute;ndrome de Cushing", "Estr&iacute;as &gt; 1 cm y purp&uacute;reas orientan a hipercortisolismo"),
        ("Piel seca, &aacute;spera y fr&iacute;a, amarillenta (carotinemia)", "Ca&iacute;da del tercio externo de la ceja", "Pelo quebradizo", "Hipotiroidismo", "El tinte amarillo sin ictericia escleral sugiere hipotiroidismo"),
        ("Mixedema pretibial (placas induradas en cara anterior de piernas)", "Piel caliente y h&uacute;meda", "Onicolisis (u&ntilde;as de Plummer)", "Hipertiroidismo (Graves)", "El mixedema pretibial es paradoj&iacute;camente signo de tirotoxicosis autoinmune"),
        ("Acantosis nigricans en cuello y axilas", "Obesidad y acrocordones", "Heridas que no cicatrizan", "Diabetes mellitus tipo 2", "La acantosis traduce hiperinsulinismo y resistencia a la insulina"),
    ]),
    ("REFLEJOS / NEUROMUSCULAR", [
        ("Relajaci&oacute;n lenta del reflejo aquileo (fase de relajaci&oacute;n prolongada)", "Bradipsiquia y somnolencia", "Bradicardia", "Hipotiroidismo", "La relajaci&oacute;n lenta del aquileo es signo cl&aacute;sico de hipotiroidismo"),
        ("Reflejos vivos e hiperreflexia con temblor", "Taquicardia y nerviosismo", "Debilidad muscular proximal", "Hipertiroidismo", "Reflejos r&aacute;pidos contrastan con la relajaci&oacute;n lenta del hipotiroidismo"),
        ("Signo de Chvostek (contracci&oacute;n facial al percutir el facial)", "Signo de Trousseau (espasmo carpal con manguito)", "Parestesias peribucales y tetania", "Hipoparatiroidismo", "Ambos signos reflejan hipocalcemia e irritabilidad neuromuscular"),
        ("Debilidad muscular proximal con dificultad para subir escaleras", "Hiporreflexia con hipopotasemia", "HTA asociada", "Hiperaldosteronismo primario (Conn)", "La debilidad por hipoK+ acompa&ntilde;a a HTA con renina baja"),
        ("Hipoton&iacute;a, somnolencia y arreflexia con deshidrataci&oacute;n", "Confusi&oacute;n por hipercalcemia", "Estre&ntilde;imiento", "Hiperparatiroidismo primario", "La hipercalcemia deprime la excitabilidad neuromuscular"),
    ]),
]
