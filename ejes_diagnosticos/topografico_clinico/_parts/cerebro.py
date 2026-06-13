# -*- coding: utf-8 -*-

NAME = "Cerebro / SNC"

EJES = [
    ("D&eacute;ficit focal agudo (vascular)", [
        ("Hemiparesia + afasia de instauraci&oacute;n s&uacute;bita, &lt;4.5 h", "<b>EVC isqu&eacute;mico</b> &rarr; activar c&oacute;digo ictus"),
        ("D&eacute;ficit focal + FA / valvulopat&iacute;a / soplo carot&iacute;deo", "<b>EVC isqu&eacute;mico cardioembolico / aterotrombotico</b>"),
        ("D&eacute;ficit focal + cefalea intensa + HTA + vomito + deterioro r&aacute;pido", "<b>EVC hemorragico (hematoma intraparenquimatoso)</b>"),
        ("D&eacute;ficit focal que revierte por completo en &lt;1 h, sin lesi&oacute;n en TC", "AIT (accidente isqu&eacute;mico transitorio) &rarr; estudio urgente, ABCD2"),
        ("Cefalea en trueno (peor de la vida) + rigidez nucal &plusmn; s&iacute;ncope", "<b>HSA (hemorragia subaracnoidea)</b> &rarr; TC sin contraste; si normal, punci&oacute;n lumbar"),
        ("V&eacute;rtigo + diplop&iacute;a + dis&aacute;rtria + ataxia (s&iacute;ndrome cruzado)", "<b>EVC de fosa posterior / territorio vertebrobasilar</b>"),
    ]),
    ("Cefalea con red flags", [
        ("Cefalea en trueno que alcanza m&aacute;ximo en segundos", "<b>HSA</b> hasta demostrar lo contrario"),
        ("Cefalea progresiva semanas + vomito matutino + papiledema", "<b>HIC / tumor cerebral</b> (efecto masa)"),
        ("Cefalea + fiebre + rigidez nucal + fotofobia", "<b>Meningitis</b> &rarr; hemocultivos + PL + antibi&oacute;tico precoz"),
        ("Cefalea + fiebre + foco infeccioso (otitis/sinusitis) + d&eacute;ficit focal", "<b>Absceso cerebral</b>"),
        ("Cefalea + alteraci&oacute;n del comportamiento + crisis + fiebre", "<b>Encefalitis</b> (herp&eacute;tica: aciclovir emp&iacute;rico)"),
        ("Cefalea peor en dec&uacute;bito/Valsalva + marcha inestable + incontinencia", "<b>Hidrocefalia</b> (HTIC / normotensiva si triada de Hakim)"),
        ("Cefalea + dolor mand&iacute;bula al masticar + arteria temporal indurada (&gt;50 a)", "Arteritis de c&eacute;lulas gigantes &rarr; corticoide urgente, VSG"),
    ]),
    ("Alteraci&oacute;n de la conciencia", [
        ("Anciano con cefalea progresiva + somnolencia tras ca&iacute;da/ACO", "<b>Hematoma subdural cr&oacute;nico</b>"),
        ("TCE con intervalo l&uacute;cido y luego deterioro r&aacute;pido + anisocoria", "<b>Hematoma epidural</b> (sangrado arterial) &rarr; ciruga urgente"),
        ("Confusi&oacute;n postcr&iacute;tica (postictal) tras movimientos t&oacute;nico-cl&oacute;nicos", "Crisis convulsiva (estado postictal)"),
        ("Crisis continuas o sin recuperar conciencia &gt;5 min", "<b>Estatus epil&eacute;ptico</b> &rarr; benzodiacepina IV"),
        ("Deterioro de conciencia + fiebre + rigidez nucal", "<b>Meningoencefalitis</b>"),
        ("Coma + hipertensi&oacute;n + bradicardia + respiraci&oacute;n irregular (triada Cushing)", "<b>HTIC / herniaci&oacute;n inminente</b>"),
    ]),
    ("Debilidad / par&aacute;lisis (patr&oacute;n)", [
        ("Hemiparesia + hiperreflexia + Babinski + espasticidad (1.ª neurona)", "Lesi&oacute;n central (corteza/c&aacute;psula/tronco) &rarr; EVC / masa"),
        ("Debilidad ascendente sim&eacute;trica + arreflexia, sin nivel sensitivo", "<b>S&iacute;ndrome de Guillain-Barr&eacute;</b> &rarr; vigilar fuerza respiratoria"),
        ("Para/tetraparesia + nivel sensitivo + retenci&oacute;n urinaria + dolor dorsal", "<b>Compresi&oacute;n medular</b> &rarr; RM urgente + corticoide"),
        ("Brotes neurol&oacute;gicos diseminados en tiempo y espacio (neuritis &oacute;ptica, diplopia)", "Esclerosis m&uacute;ltiple"),
        ("Debilidad facial perif&eacute;rica que afecta frente (no respeta) sin otro foco", "Par&aacute;lisis de Bell (VII perif&eacute;rico)"),
        ("Temblor de reposo + bradicinesia + rigidez en rueda dentada", "Enfermedad de Parkinson"),
    ]),
    ("Cronicidad / degenerativo", [
        ("Deterioro cognitivo progresivo de memoria, sin deficit focal agudo", "Demencia (Alzheimer)"),
        ("Deterioro cognitivo escalonado + factores de riesgo vascular", "Demencia vascular"),
        ("Triada marcha apr&aacute;xica + incontinencia + deterioro cognitivo", "Hidrocefalia normotensiva (Hakim)"),
        ("Temblor de reposo unilateral + micrograf&iacute;a + cara hipom&iacute;mica", "Enfermedad de Parkinson"),
        ("Fluctuaci&oacute;n cognitiva + alucinaciones visuales + parkinsonismo", "Demencia por cuerpos de Lewy"),
    ]),
]

ESTACIONES = [
    ("ESTADO MENTAL Y GLASGOW", [
        ("Apertura ocular al dolor", "Respuesta verbal confusa", "Localiza el dolor", "Glasgow 11 &rarr; deterioro de conciencia, vigilar va a&eacute;rea", "Glasgow = ocular(4) + verbal(5) + motor(6); &le;8 valoro intubaci&oacute;n"),
        ("No apertura ocular", "Sin respuesta verbal", "Sin respuesta motora", "Glasgow 3 &rarr; coma profundo", "Glasgow &le;8: protejo va a&eacute;rea, TC urgente"),
        ("Desorientado en tiempo y lugar", "Memoria reciente alterada", "C&aacute;lculo y atenci&oacute;n fallidos", "Deterioro cognitivo &rarr; aplico Minimental", "exploro funciones superiores; descarto delirium vs demencia"),
        ("Inicio s&uacute;bito de confusi&oacute;n", "Fluctuaci&oacute;n horaria", "Inatenci&oacute;n marcada", "Delirium &rarr; busco causa org&aacute;nica", "delirium es agudo y fluctuante; demencia es cr&oacute;nica y estable"),
    ]),
    ("PARES CRANEALES Y FONDO DE OJO", [
        ("Papiledema bilateral en fondo de ojo", "Cefalea progresiva", "V&oacute;mito matutino", "<b>HTIC</b> &rarr; TC urgente, no hago PL antes de TC", "papiledema = hipertensi&oacute;n intracraneal; contraindica PL hasta descartar masa"),
        ("Anisocoria con pupila midri&aacute;tica arreactiva", "Ptosis ipsilateral", "Ojo desviado abajo y afuera", "<b>Par&aacute;lisis del III par por herniaci&oacute;n uncal</b>", "midriasis fija unilateral = compresi&oacute;n del III &rarr; emergencia neuroquir&uacute;rgica"),
        ("Desviaci&oacute;n de comisura con frente conservada", "Pliegues frontales sim&eacute;tricos", "Cierra el ojo del lado par&eacute;tico", "Par&aacute;lisis facial central (EVC)", "central respeta la frente; perif&eacute;rica (Bell) la afecta"),
        ("Boca desviada + frente lisa del mismo lado", "No cierra el ojo (signo de Bell)", "Borramiento del surco nasogeniano", "Par&aacute;lisis facial perif&eacute;rica (VII)", "afecta toda la hemicara: descarto Bell vs otitis vs zoster"),
        ("Hemianopsia homonima en campimetr&iacute;a", "D&eacute;ficit motor asociado", "Inicio s&uacute;bito", "EVC de territorio posterior / cerebral media", "el defecto campim&eacute;trico localiza la lesi&oacute;n retroquiasm&aacute;tica"),
    ]),
    ("FUERZA, TONO Y REFLEJOS", [
        ("Hemiparesia con balance 3/5", "Hiperreflexia del hemicuerpo", "Babinski extensor presente", "<b>Lesi&oacute;n de 1.ª neurona (central)</b> &rarr; EVC/masa", "Babinski + hiperreflexia + espasticidad = s&iacute;ndrome piramidal"),
        ("Debilidad distal con arreflexia", "Hipoton&iacute;a flaccida", "Babinski ausente (flexor)", "Lesi&oacute;n de 2.ª neurona / perif&eacute;rica &rarr; Guillain-Barr&eacute;", "patr&oacute;n perif&eacute;rico: arreflexia + flaccidez, sin Babinski"),
        ("Debilidad ascendente sim&eacute;trica", "Arreflexia generalizada progresiva", "Disociaci&oacute;n alb&uacute;mino-citol&oacute;gica en LCR", "<b>S&iacute;ndrome de Guillain-Barr&eacute;</b>", "vigilo capacidad vital: riesgo de fallo respiratorio"),
        ("Para/tetraparesia espstica", "Hiperreflexia por debajo del nivel", "Babinski bilateral", "<b>Compresi&oacute;n medular</b> &rarr; RM urgente + corticoide", "el nivel motor y sensitivo localiza el segmento medular"),
        ("Temblor de reposo", "Rigidez en rueda dentada", "Bradicinesia", "Enfermedad de Parkinson", "triada parkinsoniana; reflejos normales, sin Babinski"),
    ]),
    ("SENSIBILIDAD Y NIVEL", [
        ("Nivel sensitivo neto en t&oacute;rax/abdomen", "Anestesia por debajo del nivel", "Retenci&oacute;n urinaria + dolor dorsal", "<b>Compresi&oacute;n medular</b> &rarr; RM urgente", "el nivel sensitivo es el sello topogr&aacute;fico de la m&eacute;dula"),
        ("Hipoestesia hemicorporal con d&eacute;ficit motor mismo lado", "Inicio s&uacute;bito", "Acompa&ntilde;a a hemiparesia", "EVC (territorio tal&aacute;mico / cerebral media)", "hemihipoestesia + hemiparesia = lesi&oacute;n central contralateral"),
        ("Parestesias en guante y calcet&iacute;n", "Sim&eacute;tricas y distales", "Curso cr&oacute;nico", "Polineuropat&iacute;a (diab&eacute;tica) &rarr; no es agudo", "patr&oacute;n longitud-dependiente: distinto del nivel medular"),
        ("P&eacute;rdida disociada (term&oacute;algica) suspendida", "Tacto conservado", "Curso cr&oacute;nico cervical", "Siringomielia / lesi&oacute;n centromedular", "disociaci&oacute;n termoalg&eacute;sica orienta al centro medular"),
    ]),
    ("SIGNOS MENINGEOS Y CEREBELO/MARCHA", [
        ("Rigidez de nuca a la flexi&oacute;n pasiva", "Signo de Kernig positivo", "Signo de Brudzinski positivo", "<b>Meningitis</b> &rarr; PL + antibi&oacute;tico precoz; no demoro por TC si no hay focalidad", "Kernig (extender rodilla con cadera flexionada duele) y Brudzinski (flexi&oacute;n cuello &rarr; flexi&oacute;n caderas)"),
        ("Cefalea en trueno + rigidez nucal", "Fotofobia", "Sin fiebre", "<b>HSA</b> &rarr; TC sin contraste; si normal, PL buscando xantocrom&iacute;a", "irritaci&oacute;n men&iacute;ngea por sangre, no por infecci&oacute;n"),
        ("Marcha at&aacute;xica con aumento de la base", "Dismetr&iacute;a dedo-nariz", "Romberg que no empeora al cerrar ojos", "S&iacute;ndrome cerebeloso &rarr; EVC de fosa posterior", "ataxia con ojos abiertos = cerebelosa; Romberg + = cordonal posterior"),
        ("Marcha festinante con pasos cortos", "Giro en bloque", "Reflejos posturales abolidos", "Enfermedad de Parkinson", "marcha festinante e hipocinesia distinguen del cerebelo"),
        ("Marcha apr&aacute;xica im&aacute;n al suelo", "Incontinencia urinaria", "Deterioro cognitivo", "Hidrocefalia normotensiva (triada de Hakim)", "triada de Hakim &rarr; valoro derivaci&oacute;n ventr&iacute;culo-peritoneal"),
    ]),
]
