# -*- coding: utf-8 -*-

NAME = "Ap. reproductor masculino"

EJES = [
    ("Dolor escrotal agudo", [
        ("Dolor s&uacute;bito intenso + n&aacute;useas + testes ascendido y horizontal + Prehn negativo + sin reflejo cremast&eacute;rico (joven)", "<b>Torsi&oacute;n testicular</b>"),
        ("Dolor escrotal gradual + fiebre + Prehn positivo + reflejo cremast&eacute;rico conservado + secreci&oacute;n/disuria", "Epididimitis aguda"),
        ("Dolor intenso de inicio agudo + n&oacute;dulo doloroso en polo superior (signo del punto azul)", "Torsi&oacute;n de hidatide de Morgagni"),
        ("Dolor + eritema escrotal + crepitaci&oacute;n + sepsis en diab&eacute;tico/inmunodeprimido", "<b>Gangrena de Fournier</b>"),
        ("Dolor escrotal + edema + antecedente de paperas reciente", "Orquitis (parotid&iacute;tica)"),
    ]),
    ("Masa o aumento escrotal", [
        ("N&oacute;dulo testicular duro indoloro + no transilumina + var&oacute;n joven 15-35 a", "Ca de test&iacute;culo"),
        ("Aumento escrotal indoloro + transilumina positivo + no se palpa masa s&oacute;lida (test&iacute;culo no diferenciable)", "Hidrocele"),
        ("Masa blanda en bolsa de gusanos + desaparece en dec&uacute;bito + izquierdo + Valsalva la aumenta", "Varicocele"),
        ("Varicocele derecho de aparici&oacute;n s&uacute;bita en adulto que no desaparece en dec&uacute;bito", "Varicocele 2&deg; a tumor renal (alerta)"),
        ("Masa qu&iacute;stica indolora separada del test&iacute;culo en epid&iacute;dimo + transilumina", "Espermatocele/quiste de epid&iacute;dimo"),
        ("Tumefacci&oacute;n inguinoescrotal reductible que aumenta con Valsalva + ruidos hidroa&eacute;reos", "Hernia inguinoescrotal"),
    ]),
    ("S&iacute;ntomas urinarios bajos (LUTS)", [
        ("Var&oacute;n &gt;50 a + chorro d&eacute;bil + goteo + nicturia + tacto rectal pr&oacute;stata lisa el&aacute;stica agrandada", "HBP"),
        ("Var&oacute;n &gt;60 a + n&oacute;dulo p&eacute;treo irregular al tacto rectal + APE elevado + dolor &oacute;seo", "Ca de pr&oacute;stata"),
        ("Fiebre + dolor perineal + disuria + tacto rectal pr&oacute;stata caliente muy dolorosa (no masajear)", "Prostatitis aguda bacteriana"),
        ("Dolor pelviano cr&oacute;nico + molestia miccional fluctuante &ge;3 meses + tacto poco expresivo", "Prostatitis cr&oacute;nica/dolor pelviano cr&oacute;nico"),
        ("Imposibilidad s&uacute;bita de orinar + globo vesical doloroso palpable", "<b>Retenci&oacute;n aguda de orina</b>"),
    ]),
    ("Secreci&oacute;n uretral y disfunci&oacute;n sexual", [
        ("Secreci&oacute;n uretral purulenta abundante + disuria + inicio agudo tras contacto sexual", "Uretritis gonoc&oacute;cica"),
        ("Secreci&oacute;n mucoide escasa + disuria + inicio subagudo (Chlamydia/Mycoplasma)", "Uretritis no gonoc&oacute;cica"),
        ("Dificultad mantenida para lograr/mantener erecci&oacute;n + factores vasculares (DM, HTA, tabaco)", "Disfunci&oacute;n er&eacute;ctil"),
        ("Erecci&oacute;n dolorosa &gt;4 h sin estimulaci&oacute;n + isquemia (anemia falciforme, f&aacute;rmacos)", "<b>Priapismo isqu&eacute;mico</b>"),
        ("Glande eritematoso + pruriginoso + secreci&oacute;n bajo prepucio + diab&eacute;tico/falta de higiene", "Balanitis (candidi&aacute;sica)"),
        ("Imposibilidad de retraer el prepucio + anillo constrictivo", "Fimosis"),
    ]),
]

ESTACIONES = [
    ("EXPLORACI&Oacute;N ESCROTAL Y TESTICULAR", [
        ("Testes ascendido y horizontal", "Reflejo cremast&eacute;rico ausente", "Prehn negativo (no alivia al elevar)", "<b>Torsi&oacute;n testicular</b>", "Urgencia: ventana &le;6 h &rarr; cirug&iacute;a inmediata"),
        ("Epid&iacute;dimo engrosado y doloroso", "Reflejo cremast&eacute;rico conservado", "Prehn positivo (alivia al elevar)", "Epididimitis aguda", "Doppler: flujo aumentado"),
        ("Transiluminaci&oacute;n positiva", "Masa quistica indolora", "No se palpa por separado el test&iacute;culo", "Hidrocele", "Eco si dudas para descartar tumor"),
        ("Transiluminaci&oacute;n negativa", "N&oacute;dulo duro p&eacute;treo indoloro", "No reductible", "Ca de test&iacute;culo", "Eco escrotal + marcadores AFP/&beta;-hCG/LDH"),
        ("Bolsa de gusanos al palpar", "Aumenta con Valsalva de pie", "Desaparece en dec&uacute;bito (izquierdo)", "Varicocele", "Si derecho s&uacute;bito &rarr; descartar masa renal"),
        ("Signo del punto azul en polo superior", "N&oacute;dulo selectivo doloroso", "Reflejo cremast&eacute;rico presente", "Torsi&oacute;n de hidatide", "Manejo conservador habitual"),
    ]),
    ("TACTO RECTAL DE PR&Oacute;STATA", [
        ("Pr&oacute;stata aumentada sim&eacute;trica", "Superficie lisa el&aacute;stica", "Surco medio conservado", "HBP", "APE leve-moderado; IPSS para s&iacute;ntomas"),
        ("N&oacute;dulo p&eacute;treo irregular", "Asimetr&iacute;a + surco borrado", "Fija/adherida", "Ca de pr&oacute;stata", "APE elevado &rarr; biopsia + RM"),
        ("Pr&oacute;stata caliente y muy dolorosa", "Tumefacta", "No masajear (riesgo bacteriemia)", "Prostatitis aguda", "Fiebre + sedimento; antibi&oacute;tico"),
        ("Tono esfinteriano normal", "Ampolla rectal sin masas", "Pr&oacute;stata poco expresiva", "Prostatitis cr&oacute;nica/DPC", "S&iacute;ntomas &ge;3 meses fluctuantes"),
    ]),
    ("INSPECCI&Oacute;N DEL PENE Y URETRA", [
        ("Secreci&oacute;n purulenta abundante", "Meato eritematoso", "Disuria de inicio agudo", "Uretritis gonoc&oacute;cica", "Gram: diplococos intracelulares; ITS"),
        ("Secreci&oacute;n mucoide escasa", "S&iacute;ntomas subagudos", "Pareja con ITS", "Uretritis no gonoc&oacute;cica", "PCR Chlamydia/Mycoplasma; tratar pareja"),
        ("Glande eritematoso pruriginoso", "Exudado blanquecino subprepucial", "Diab&eacute;tico/mala higiene", "Balanitis", "Glucemia + antif&uacute;ngico t&oacute;pico"),
        ("Prepucio no retr&aacute;til", "Anillo fibroso constrictor", "Sin compromiso vascular", "Fimosis", "Corticoide t&oacute;pico o circuncisi&oacute;n"),
        ("Glande atrapado y edematoso", "Prepucio retra&iacute;do que no reduce", "Dolor + congesti&oacute;n", "<b>Parafimosis</b>", "Urgencia: reducci&oacute;n manual inmediata"),
        ("Pene en erecci&oacute;n persistente", "Rigidez dolorosa de cuerpos cavernosos", "Glande blando &gt;4 h", "<b>Priapismo isqu&eacute;mico</b>", "Urgencia: aspiraci&oacute;n + fenilefrina"),
    ]),
]
