# -*- coding: utf-8 -*-
NAME = "Cabeza / Craneofacial"

EJES = [
  ("Cefalea primaria", [
    ("Bilateral en banda + opresiva + no empeora con esfuerzo + sin n&aacute;useas", "Cefalea tensional"),
    ("Pulsatil hemicraneal + fotofobia/sonofobia + n&aacute;useas + aura visual previa", "Migra&ntilde;a"),
    ("Unilateral periorbitaria atroz + l&aacute;grimeo + rinorrea + Horner + agitaci&oacute;n", "Cefalea en racimos (cluster)"),
    ("Hemicraneal pulsatil + empeora con la actividad + el paciente busca cuarto oscuro", "Migra&ntilde;a sin aura"),
    ("Diaria + uso de analg&eacute;sicos &gt;15 d&iacute;as/mes", "Cefalea por abuso de medicaci&oacute;n"),
  ]),
  ("Cefalea secundaria (red flags)", [
    ("En trueno + intensidad m&aacute;xima en segundos + rigidez de nuca", "<b>Hemorragia subaracnoidea</b>"),
    ("+ fiebre + rigidez de nuca + fotofobia (s&iacute;ndrome men&iacute;ngeo)", "Meningitis"),
    ("+ foco neurol&oacute;gico + papiledema + empeora al despertar/Valsalva", "Masa intracraneal / HTIC"),
    ("Nueva + &gt;50 a&ntilde;os + arteria temporal indurada + claudicaci&oacute;n mandibular", "<b>Arteritis de c&eacute;lulas gigantes</b>"),
    ("+ inmunodepresi&oacute;n o c&aacute;ncer conocido + curso progresivo", "Lesi&oacute;n estructural (absceso/met&aacute;stasis)"),
    ("Postural: empeora de pie y mejora tumbado tras punci&oacute;n lumbar", "Cefalea por hipotensi&oacute;n de LCR"),
  ]),
  ("Dolor facial", [
    ("Hemifacial + congesti&oacute;n + rinorrea purulenta &gt;10 d&iacute;as + empeora al inclinarse", "Sinusitis"),
    ("Paroxismos l&aacute;ncinantes en territorio V2-V3 + gatillo al tocar/masticar", "Neuralgia del trig&eacute;mino"),
    ("Retroocular + ptosis + midriasis + diplopia + dolor s&uacute;bito intenso", "<b>Aneurisma de comunicante posterior (III par)</b> — la disecci&oacute;n carot&iacute;dea da Horner con MIOSIS, no midriasis"),
    ("Preauricular + dolor al masticar + chasquido + bruxismo", "Disfunci&oacute;n temporomandibular"),
    ("Maxilar + relaci&oacute;n con pieza dental + percusi&oacute;n dolorosa", "Origen odontog&eacute;nico"),
  ]),
  ("Par&aacute;lisis facial", [
    ("Hemicara COMPLETA incluida la frente + no cierra el ojo + signo de Bell", "Par&aacute;lisis de Bell (perif&eacute;rica)"),
    ("Respeta la frente (la arruga) + d&eacute;ficit de extremidades asociado", "Lesi&oacute;n central (ictus)"),
    ("Perif&eacute;rica + ves&iacute;culas en pabell&oacute;n auricular + otalgia", "S&iacute;ndrome de Ramsay-Hunt"),
    ("Perif&eacute;rica bilateral + parestesias ascendentes + arreflexia", "Guillain-Barr&eacute;"),
    ("Perif&eacute;rica + masa parot&iacute;dea de crecimiento lento", "Tumor de par&oacute;tida"),
  ]),
  ("Tumefacci&oacute;n facial / preauricular", [
    ("Preauricular bilateral + dolor al masticar + fiebre + contacto epid&eacute;mico", "Parotiditis (paperas)"),
    ("Submandibular + dolor c&oacute;lico que aumenta antes de comer + se palpa c&aacute;lculo", "Sialolitiasis"),
    ("Preauricular + fiebre + eritema + pus por el conducto de Stenon", "Parotiditis bacteriana aguda"),
    ("Indolora + crecimiento lento + consistencia firme unilateral", "Tumor de gl&aacute;ndula salival"),
    ("Difusa + crepitaci&oacute;n + tras infecci&oacute;n dental + fiebre alta", "Celulitis facial / angina de Ludwig"),
  ]),
]

ESTACIONES = [
  ("PALPACION DE LA ARTERIA TEMPORAL", [
    ("Arteria temporal indurada, engrosada y no pulsatil", "Hipersensibilidad al peinarse o apoyar la cabeza", "&gt;50 a&ntilde;os + claudicaci&oacute;n mandibular + VSG &gt;50", "<b>Arteritis de c&eacute;lulas gigantes</b>", "es urgencia: corticoide a dosis altas YA antes de la biopsia para salvar la visi&oacute;n"),
    ("Amaurosis fugax o p&eacute;rdida visual mono-ocular", "Cefalea temporal nueva + s&iacute;ndrome constitucional", "VSG y PCR muy elevadas", "<b>Arteritis de c&eacute;lulas gigantes con afecci&oacute;n ocular</b>", "la NOIA es irreversible; no espero la biopsia para tratar"),
    ("Arteria temporal pulsatil normal y no dolorosa", "Cefalea pulsatil hemicraneal recurrente", "Fotofobia + n&aacute;useas", "Migra&ntilde;a", "arteria normal aleja la arteritis; manejo de migra&ntilde;a"),
  ]),
  ("EXPLORACION DE PARES CRANEALES (V y VII)", [
    ("Par&aacute;lisis facial que afecta la FRENTE (no arruga ese lado)", "No cierra el ojo + desviaci&oacute;n de la comisura", "Hiperacusia + alteraci&oacute;n del gusto", "Par&aacute;lisis de Bell (VII perif&eacute;rico)", "afecta la frente: la lesi&oacute;n es perif&eacute;rica; protejo el ojo y doy corticoide precoz"),
    ("Par&aacute;lisis facial que RESPETA la frente (s&iacute; arruga)", "Hemiparesia o disartria asociadas", "Inicio s&uacute;bito", "Lesi&oacute;n central (ictus)", "respeta la frente por inervaci&oacute;n bilateral del frontal; activo c&oacute;digo ictus"),
    ("Dolor paroxistico l&aacute;ncinante en mejilla/mand&iacute;bula", "Zona gatillo al tocar o masticar", "Exploraci&oacute;n neurol&oacute;gica normal entre crisis", "Neuralgia del trig&eacute;mino", "V sin d&eacute;ficit sensitivo fijo; carbamazepina, descarto causa estructural si hay foco"),
    ("Ves&iacute;culas en el conducto auditivo + par&aacute;lisis perif&eacute;rica", "Otalgia intensa + hipoacusia/v&eacute;rtigo", "Erupci&oacute;n en territorio del VII", "S&iacute;ndrome de Ramsay-Hunt", "par&aacute;lisis perif&eacute;rica con ves&iacute;culas: antiviral + corticoide, peor pron&oacute;stico que Bell"),
  ]),
  ("PALPACION DE SENOS PARANASALES", [
    ("Dolor a la presi&oacute;n sobre senos frontales y maxilares", "Rinorrea purulenta &gt;10 d&iacute;as", "Empeora al inclinar la cabeza hacia delante", "Sinusitis aguda", "dolor + rinorrea purulenta prolongada: sinusitis; antibi&oacute;tico si no mejora o empeora"),
    ("Dolor periorbitario + edema palpebral + proptosis", "Fiebre alta + afecci&oacute;n del estado general", "Limitaci&oacute;n de la motilidad ocular", "<b>Celulitis orbitaria (complicaci&oacute;n de sinusitis)</b>", "proptosis y oftalmoplej&iacute;a son alarma: TC urgente y antibi&oacute;tico IV"),
    ("Senos no dolorosos a la palpaci&oacute;n", "Cefalea opresiva bilateral en banda", "Sin rinorrea ni fiebre", "Cefalea tensional", "senos indoloros sin rinorrea descartan sinusitis como causa"),
  ]),
  ("PALPACION DE GLANDULAS SALIVALES", [
    ("Tumefacci&oacute;n preauricular bilateral dolorosa", "Dolor al masticar + fiebre + malestar", "Contacto epid&eacute;mico, no vacunado", "Parotiditis (paperas)", "par&oacute;tida bilateral dolorosa v&iacute;rica; vigilo orquitis y meningitis como complicaciones"),
    ("C&aacute;lculo palpable en suelo de boca + dolor c&oacute;lico", "El dolor aumenta justo antes de comer", "Tumefacci&oacute;n submandibular intermitente", "Sialolitiasis", "c&aacute;lico ductal que aumenta con la salivaci&oacute;n; hidrataci&oacute;n y sialogogos, ecograf&iacute;a"),
    ("Salida de pus por el conducto de Stenon al ordenar", "Par&oacute;tida eritematosa, caliente y muy dolorosa", "Anciano deshidratado, mala higiene oral", "Parotiditis bacteriana aguda", "pus al exprimir = bacteriana; antibi&oacute;tico, hidrataci&oacute;n y sialogogos"),
    ("Masa firme indolora de crecimiento lento", "Par&aacute;lisis facial asociada (signo de malignidad)", "Fija a planos profundos", "Tumor maligno de gl&aacute;ndula salival", "masa con par&aacute;lisis del VII orienta a malignidad; derivo para imagen y biopsia"),
  ]),
  ("FONDO DE OJO (papiledema)", [
    ("Papila de bordes borrosos y elevada, sin pulso venoso", "Cefalea que empeora al despertar y con Valsalva", "N&aacute;useas en escopetazo + diplop&iacute;a por VI", "<b>Papiledema por hipertensi&oacute;n intracraneal</b>", "papiledema bilateral = HTIC; neuroimagen urgente antes de cualquier punci&oacute;n lumbar"),
    ("Edema de papila + p&eacute;rdida visual + arteria temporal indurada", "&gt;50 a&ntilde;os + claudicaci&oacute;n mandibular", "VSG muy elevada", "<b>Neuropat&iacute;a &oacute;ptica isqu&eacute;mica (arteritis)</b>", "papila p&aacute;lida edematosa en mayor de 50: corticoide inmediato para salvar el otro ojo"),
    ("Papila normal, excavaci&oacute;n fisiol&oacute;gica conservada", "Cefalea pulsatil con aura visual reversible", "Exploraci&oacute;n neurol&oacute;gica normal", "Migra&ntilde;a con aura", "fondo de ojo normal apoya cefalea primaria frente a HTIC"),
  ]),
]
