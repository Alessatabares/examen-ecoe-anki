# -*- coding: utf-8 -*-

NAME = "Nariz / Garganta / Cuello"

EJES = [
    ("Epistaxis", [
        ("Sangrado por una fosa, ceden con presi&oacute;n bidigital, paciente joven", "Epistaxis anterior (plexo de Kiesselbach)"),
        ("Sangrado posterior abundante, deglute sangre, hipertenso/anticoagulado", "Epistaxis posterior (arteria esfenopalatina)"),
        ("Epistaxis unilateral recidivante + obstrucci&oacute;n nasal en var&oacute;n adolescente", "Angiofibroma nasofar&iacute;ngeo juvenil"),
        ("Epistaxis unilateral con secreci&oacute;n f&eacute;tida en ni&ntilde;o peque&ntilde;o", "Cuerpo extra&ntilde;o nasal"),
        ("Epistaxis recurrente + telangiectasias en labios/lengua + antecedente familiar", "Telangiectasia hemorr&aacute;gica hereditaria (Rendu-Osler)"),
        ("Sangrado nasal profuso con inestabilidad &rarr; <b>compromiso hemodin&aacute;mico</b>", "<b>Epistaxis grave con shock hipovol&eacute;mico</b>"),
    ]),
    ("Obstrucci&oacute;n nasal y rinorrea", [
        ("Estornudos en salvas + rinorrea acuosa + prurito + estacionalidad", "Rinitis al&eacute;rgica"),
        ("Obstrucci&oacute;n bilateral + anosmia + rinorrea, asociado a asma/intolerancia AINE", "Poliposis nasosinusal"),
        ("Obstrucci&oacute;n unilateral + rinorrea f&eacute;tida purulenta en ni&ntilde;o", "Cuerpo extra&ntilde;o nasal"),
        ("Rinorrea purulenta + dolor facial + fiebre &gt; 10 d&iacute;as o empeoramiento bif&aacute;sico", "Rinosinusitis bacteriana aguda"),
        ("Congesti&oacute;n cr&oacute;nica por abuso de vasoconstrictores t&oacute;picos", "Rinitis medicamentosa"),
        ("Rinorrea cristalina unilateral tras traumatismo craneal (glucosa positiva)", "Fistula de LCR (rinolicuorrea)"),
    ]),
    ("Odinofagia y disfagia alta", [
        ("Fiebre + exudado amigdalar + adenopat&iacute;as + ausencia de tos (Centor 3-4)", "Faringoamigdalitis estreptoc&oacute;cica (SBHGA)"),
        ("Trismus + voz de papa caliente + &uacute;vula desplazada + abombamiento unilateral", "<b>Absceso periamigdalino</b>"),
        ("Odinofagia intensa + babeo + estridor + posici&oacute;n en tr&iacute;pode, NO bajar lengua", "<b>Epiglotitis aguda</b>"),
        ("Faringitis + adenopat&iacute;as + esplenomegalia + exantema tras amoxicilina, joven", "Mononucleosis infecciosa (VEB)"),
        ("Odinofagia leve + tos + disfon&iacute;a + rinorrea (Centor 0-1)", "Faringitis viral"),
        ("Odinofagia + r&iacute;gidez cervical + abombamiento de pared far&iacute;ngea posterior en ni&ntilde;o", "<b>Absceso retrofar&iacute;ngeo</b>"),
    ]),
    ("Disfon&iacute;a y masa cervical", [
        ("Disfon&iacute;a aguda + tos + cuadro catarral, autolimitada", "Laringitis aguda"),
        ("Disfon&iacute;a &gt; 3 semanas en fumador/bebedor mayor de 40 a&ntilde;os", "Carcinoma de laringe"),
        ("Adenopat&iacute;a cervical dolorosa, m&oacute;vil, de aparici&oacute;n reciente con infecci&oacute;n", "Adenitis cervical reactiva"),
        ("Adenopat&iacute;a dura, fija, indolora &gt; 3 semanas en adulto fumador", "Met&aacute;stasis cervical / neoplasia"),
        ("Masa cervical anterior que asciende con la degluci&oacute;n, l&iacute;nea media", "Quiste del conducto tirogloso"),
        ("Masa lateral blanda en borde anterior del esternocleidomastoideo, cong&eacute;nita", "Quiste branquial"),
    ]),
]

ESTACIONES = [
    ("RINOSCOPIA ANTERIOR / INSPECCION NASAL", [
        ("Punto sangrante en tabique anterior", "Cede con presi&oacute;n bidigital 10-15 min", "Sin sangrado posterior", "Epistaxis anterior (Kiesselbach)", "compresi&oacute;n del ala nasal contra el tabique"),
        ("No se visualiza origen anterior", "Sangre que cae por orofaringe", "Hipertenso/anticoagulado", "Epistaxis posterior", "puede precisar taponamiento posterior o bal&oacute;n"),
        ("Masas pediculadas grises traslucidas", "Bilateral + anosmia", "Mucosa p&aacute;lida edematosa", "Poliposis nasosinusal", "buscar tr&iacute;ada de Samter (asma + AINE)"),
        ("Cuerpo brillante unilateral + secreci&oacute;n f&eacute;tida", "Ni&ntilde;o peque&ntilde;o", "Una sola fosa afectada", "Cuerpo extra&ntilde;o nasal", "unilateralidad f&eacute;tida = cuerpo extra&ntilde;o hasta probar lo contrario"),
    ]),
    ("EXPLORACION OROFARINGEA", [
        ("Exudado amigdalar bilateral + adenopat&iacute;as", "Ausencia de tos + fiebre", "Centor 3-4", "Faringoamigdalitis estreptoc&oacute;cica", "Centor &ge; 3 apoya etiolog&iacute;a bacteriana"),
        ("Abombamiento periamigdalino + &uacute;vula desviada", "Trismus + voz de papa caliente", "Unilateral", "<b>Absceso periamigdalino</b>", "voz de papa caliente = urgencia ORL, drenaje"),
        ("Babeo + estridor + tr&iacute;pode", "Rechazo a tragar saliva", "Aspecto t&oacute;xico", "<b>Epiglotitis aguda</b>", "NO bajar la lengua ni explorar con depresor: riesgo de espasmo gl&oacute;tico"),
        ("Exudado + esplenomegalia + exantema postamoxicilina", "Adenopat&iacute;as generalizadas", "Paciente joven", "Mononucleosis infecciosa", "evitar amoxicilina por exantema; serolog&iacute;a VEB"),
    ]),
    ("PALPACION CERVICAL", [
        ("Adenopat&iacute;a m&oacute;vil dolorosa reciente", "Infecci&oacute;n ORL asociada", "Consistencia el&aacute;stica", "Adenitis cervical reactiva", "dolorosa + m&oacute;vil + corta evoluci&oacute;n = benigna probable"),
        ("Adenopat&iacute;a dura fija indolora &gt; 3 semanas", "Fumador mayor de 40", "Sin foco infeccioso", "Met&aacute;stasis cervical", "dura + fija + indolora + crecimiento = estudio de neoplasia"),
        ("Masa l&iacute;nea media que asciende al tragar y sacar lengua", "Cong&eacute;nita", "Indolora salvo infecci&oacute;n", "Quiste del conducto tirogloso", "asciende con la protrusi&oacute;n lingual"),
        ("Tiroides aumentada + n&oacute;dulo desplazable con degluci&oacute;n", "Sin adenopat&iacute;as patol&oacute;gicas", "Eutiroideo o no", "Masa/n&oacute;dulo tiroideo", "el tiroides se desplaza con la degluci&oacute;n"),
    ]),
    ("VALORACION DE VIA AEREA (ESTRIDOR / TIRAJE)", [
        ("Estridor inspiratorio + tiraje supraesternal", "Disfagia + babeo", "Aspecto t&oacute;xico", "<b>Obstrucci&oacute;n de v&iacute;a a&eacute;rea superior</b>", "estridor + tiraje = compromiso de v&iacute;a a&eacute;rea, asegurar ABC"),
        ("Estridor + cianosis + agitaci&oacute;n", "Uso de m&uacute;sculos accesorios", "Disminuci&oacute;n del nivel de conciencia", "<b>Obstrucci&oacute;n cr&iacute;tica de v&iacute;a a&eacute;rea</b>", "cianosis + bradipnea = obstrucci&oacute;n inminente, v&iacute;a a&eacute;rea avanzada"),
        ("Voz de papa caliente + trismus", "Abombamiento orofar&iacute;ngeo", "Fiebre", "<b>Absceso periamigdalino con riesgo de v&iacute;a a&eacute;rea</b>", "vigilar permeabilidad; drenaje urgente"),
        ("Disfon&iacute;a progresiva + estridor en fumador", "Masa lar&iacute;ngea sospechada", "P&eacute;rdida de peso", "Carcinoma de laringe con compromiso de v&iacute;a a&eacute;rea", "disfon&iacute;a &gt; 3 semanas en fumador = derivar ORL"),
    ]),
]
