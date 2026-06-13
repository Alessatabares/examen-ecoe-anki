# -*- coding: utf-8 -*-
NAME = "Pulmon / Respiratorio"

EJES = [
  ("Disnea aguda", [
    ("S&uacute;bita + dolor pleur&iacute;tico + timpanismo + sin murmullo unilateral", "Neumot&oacute;rax (a tensi&oacute;n si IY + desviaci&oacute;n traqueal)"),
    ("S&uacute;bita + factor de riesgo TVP/inmovilizaci&oacute;n + Wells alto", "TEP"),
    ("Progresiva en d&iacute;as + fiebre + tos productiva + crepitantes localizados", "Neumon&iacute;a"),
    ("Sibilancias que revierten con broncodilatador", "Crisis asm&aacute;tica"),
    ("Tabaquismo &gt;10 paq-a&ntilde;o + t&oacute;rax en tonel + no revierte del todo", "EPOC reagudizado"),
    ("Ortopnea + DPN + crepitantes bibasales + S3", "Edema agudo de pulm&oacute;n cardiog&eacute;nico"),
    ("Progresiva en meses + crepitantes &laquo;velcro&raquo; + acropaquias", "EPID / fibrosis pulmonar"),
  ]),
  ("Dolor tor&aacute;cico pleur&iacute;tico", [
    ("+ disnea s&uacute;bita + timpanismo + sin murmullo", "Neumot&oacute;rax"),
    ("+ disnea s&uacute;bita + hemoptisis + Wells alto", "TEP con infarto pulmonar"),
    ("+ fiebre + tos + soplo tub&aacute;rico (consolidaci&oacute;n)", "Neumon&iacute;a"),
    ("+ roce pleural tras cuadro viral", "Pleuritis"),
    ("+ matidez basal + abolici&oacute;n del murmullo", "Derrame pleural"),
  ]),
  ("Tos", [
    ("Aguda + fiebre + expectoraci&oacute;n purulenta", "Neumon&iacute;a / bronquitis aguda"),
    ("Cr&oacute;nica + tabaquismo + expectoraci&oacute;n matutina &ge;3 meses/2 a&ntilde;os", "Bronquitis cr&oacute;nica (EPOC)"),
    ("Cr&oacute;nica + hemoptisis + p&eacute;rdida de peso + sudoraci&oacute;n nocturna", "TB / Ca broncog&eacute;nico"),
    ("Seca persistente en paciente con IECA", "Tos farmacol&oacute;gica por IECA"),
    ("Nocturna + sibilancias + desencadenantes estacionales", "Asma"),
  ]),
  ("Hemoptisis", [
    ("+ s&iacute;ndrome constitucional + tabaquismo", "Ca broncog&eacute;nico"),
    ("+ fiebre + sudoraci&oacute;n nocturna + cavitaci&oacute;n apical", "Tuberculosis"),
    ("+ disnea s&uacute;bita + dolor pleur&iacute;tico", "TEP con infarto pulmonar"),
    ("+ expectoraci&oacute;n purulenta cr&oacute;nica abundante", "Bronquiectasias"),
    ("Masiva + hematuria + insuficiencia renal", "S&iacute;ndrome pulm&oacute;n-ri&ntilde;&oacute;n (Goodpasture/vasculitis)"),
  ]),
]

ESTACIONES = [
  ("INSPECCION / SIGNOS VITALES", [
    ("Tiraje + desviaci&oacute;n traqueal contralateral", "Ingurgitaci&oacute;n yugular", "Timpanismo unilateral", "Neumot&oacute;rax a tensi&oacute;n", "es cl&iacute;nico: descompresi&oacute;n con aguja YA, no espero la Rx"),
    ("T&oacute;rax en tonel", "Espiraci&oacute;n prolongada con labios fruncidos", "Tabaquismo &gt;10 paq-a&ntilde;o", "EPOC", "obstrucci&oacute;n que no revierte; espirometr&iacute;a con FEV1/FVC &lt;0.7"),
    ("Uso de m&uacute;sculos accesorios + cianosis", "Incapacidad para completar frases", "Silencio auscultatorio", "Crisis asm&aacute;tica grave", "broncodilatador + esteroide; el t&oacute;rax silente es se&ntilde;al de gravedad"),
  ]),
  ("PALPACION", [
    ("Fr&eacute;mito vocal AUMENTADO localizado", "Fiebre + tos productiva", "Matidez en la misma zona", "Neumon&iacute;a (consolidaci&oacute;n)", "consolidaci&oacute;n: vibraciones aumentadas, pido Rx de t&oacute;rax"),
    ("Fr&eacute;mito vocal ABOLIDO", "Ausencia de expansi&oacute;n", "Matidez basal", "Derrame pleural", "l&iacute;quido en el espacio pleural; confirmo con USG/Rx"),
    ("Enfisema subcut&aacute;neo (crepitaci&oacute;n a la palpaci&oacute;n)", "Antecedente de trauma/barotrauma", "Disnea", "Neumot&oacute;rax", "aire en partes blandas: busco neumot&oacute;rax asociado"),
  ]),
  ("PERCUSION", [
    ("Timpanismo unilateral", "Abolici&oacute;n del murmullo", "Disnea s&uacute;bita", "Neumot&oacute;rax", "hiperresonancia + sin murmullo = aire a presi&oacute;n"),
    ("Matidez basal", "Abolici&oacute;n de vibraciones vocales", "Disminuci&oacute;n del murmullo", "Derrame pleural", "matidez con vibraciones abolidas distingue derrame de consolidaci&oacute;n"),
    ("Matidez localizada", "Fr&eacute;mito AUMENTADO", "Soplo tub&aacute;rico", "Consolidaci&oacute;n neum&oacute;nica", "matidez con vibraciones aumentadas = pulm&oacute;n consolidado"),
  ]),
  ("AUSCULTACION", [
    ("Crepitantes localizados", "Soplo tub&aacute;rico", "Broncofon&iacute;a/pectoriloquia", "Neumon&iacute;a", "foco de consolidaci&oacute;n: antibi&oacute;tico seg&uacute;n CURB-65"),
    ("Crepitantes secos bibasales tipo &laquo;velcro&raquo;", "Acropaquias", "Disnea progresiva en meses", "EPID / fibrosis pulmonar", "patr&oacute;n intersticial: solicito TCAR"),
    ("Sibilancias espiratorias difusas", "Espiraci&oacute;n prolongada", "Reversibilidad COMPLETA con broncodilatador", "Asma (el EPOC apenas revierte)", "reversibilidad completa = asma; en EPOC la obstrucci&oacute;n es fija/poco reversible"),
    ("Crepitantes h&uacute;medos bibasales", "S3 (galope)", "Ortopnea + DPN", "Edema agudo de pulm&oacute;n cardiog&eacute;nico", "crepitantes + S3 apuntan a falla de bomba, no a infecci&oacute;n"),
    ("Ausencia de murmullo unilateral", "Timpanismo", "Disnea s&uacute;bita", "Neumot&oacute;rax", "silencio + timpanismo unilateral = aire pleural"),
    ("Roce pleural", "Dolor que aumenta con la inspiraci&oacute;n", "Antecedente viral", "Pleuritis", "roce que desaparece al contener la respiraci&oacute;n"),
  ]),
]
