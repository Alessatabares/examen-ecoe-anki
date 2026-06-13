# -*- coding: utf-8 -*-
NAME = "Intestino"

EJES = [
    ("Dolor abdominal agudo", [
        ("Migra de epigastrio a FID + Blumberg + anorexia", "Apendicitis"),
        ("FII en &gt;50a + fiebre + masa palpable", "Diverticulitis"),
        ("S&uacute;bito epig&aacute;strico + abdomen en tabla + AINE", "<b>&Uacute;lcera perforada</b>"),
        ("Desproporcionado a la exploraci&oacute;n + FA/cardiopat&iacute;a", "<b>Isquemia mesent&eacute;rica</b>"),
        ("C&oacute;lico + distensi&oacute;n + no ventosea + vac&iacute;o de heces", "Obstrucci&oacute;n intestinal"),
        ("Difuso + tabla r&iacute;gida + sepsis + silencio abdominal", "<b>Peritonitis</b>"),
        ("FID/periumbilical recurrente + diarrea + fisura perianal", "Crohn"),
    ]),
    ("Hemorragia digestiva alta", [
        ("Hematemesis en posos de caf&eacute; + AINE/H. pylori", "&Uacute;lcera p&eacute;ptica (HDA)"),
        ("Hematemesis masiva + hep&aacute;topata/alcohol", "<b>Varices esof&aacute;gicas</b>"),
        ("Sangrado tras v&oacute;mitos/arcadas repetidas", "Mallory-Weiss"),
        ("Melenas + s&iacute;ndrome constitucional + saciedad precoz", "C&aacute;ncer g&aacute;strico"),
        ("Dolor tor&aacute;cico + enfisema subcut&aacute;neo tras v&oacute;mito", "<b>Boerhaave</b> (perforaci&oacute;n esof&aacute;gica, NO es HDA: la urgencia es mediastinitis, no el sangrado)"),
    ]),
    ("Hemorragia digestiva baja", [
        ("Hematoquezia indolora + &gt;50a + cambio del ritmo", "C&aacute;ncer de colon"),
        ("Rectorragia roja brillante al final de la defecaci&oacute;n", "Hemorroides"),
        ("Sangre roja + dolor intenso al defecar + estre&ntilde;imiento", "Fisura anal"),
        ("Diarrea sanguinolenta + moco + tenesmo + brotes", "Colitis ulcerosa"),
        ("Sangrado rojo oscuro abundante en &gt;60a indoloro", "HDB (diverticular/angiodisplasia)"),
        ("Diverticulitis previa + hematoquezia autolimitada", "HDB diverticular"),
    ]),
    ("Disfagia", [
        ("Disfagia a s&oacute;lidos progresiva + p&eacute;rdida de peso + &gt;55a", "C&aacute;ncer de es&oacute;fago"),
        ("Disfagia a s&oacute;lidos y l&iacute;quidos + regurgitaci&oacute;n nocturna", "Acalasia"),
        ("Pirosis retroesternal + regurgitaci&oacute;n &aacute;cida postprandial", "ERGE"),
        ("Disfagia + impactaci&oacute;n alimentaria en joven at&oacute;pico", "Esofagitis eosinof&iacute;lica"),
    ]),
    ("V&oacute;mito y obstrucci&oacute;n", [
        ("V&oacute;mito bilioso + distensi&oacute;n + cirug&iacute;a abdominal previa", "Obstrucci&oacute;n por bridas"),
        ("Distensi&oacute;n masiva + anciano encamado + asa en grano de caf&eacute;", "<b>V&oacute;lvulo de sigma</b>"),
        ("V&oacute;mito fecaloideo + ausencia total de gas/heces", "<b>Obstrucci&oacute;n completa</b>"),
        ("Obstrucci&oacute;n + ancianos + cambio ritmo + p&eacute;rdida de peso", "Obstrucci&oacute;n por Ca colon"),
        ("V&oacute;mito + dolor desproporcionado + lactato elevado", "<b>Isquemia mesent&eacute;rica</b>"),
    ]),
]

ESTACIONES = [
    ("INSPECCION", [
        ("Distensi&oacute;n abdominal generalizada", "Timpanismo a la percusi&oacute;n", "Ausencia de ventoseo/heces", "Obstrucci&oacute;n intestinal", "valorar nivel: TC con contraste; SNG descompresi&oacute;n"),
        ("Cicatrices de laparotom&iacute;a previas", "Distensi&oacute;n + c&oacute;lico", "Peristaltismo visible de lucha", "Obstrucci&oacute;n por bridas", "causa m&aacute;s frecuente de obstrucci&oacute;n de delgado"),
        ("Asa distendida asim&eacute;trica en grano de caf&eacute;", "Anciano + estre&ntilde;imiento cr&oacute;nico", "Timpanismo difuso", "<b>V&oacute;lvulo de sigma</b>", "Rx con asa en grano de caf&eacute;; desvolvulaci&oacute;n endosc&oacute;pica"),
        ("Ictericia + circulaci&oacute;n colateral", "Ascitis + telangiectasias", "Distensi&oacute;n por l&iacute;quido", "Hepatopat&iacute;a (riesgo de varices)", "buscar varices: endoscopia + profilaxis betabloqueante"),
    ]),
    ("AUSCULTACION", [
        ("Ruidos aumentados met&aacute;licos de lucha", "Distensi&oacute;n + c&oacute;lico", "V&oacute;mito bilioso", "Obstrucci&oacute;n mec&aacute;nica", "fase inicial hiperperist&aacute;ltica antes del silencio"),
        ("Silencio abdominal (ausencia de ruidos)", "Abdomen en tabla + defensa", "Fiebre + taquicardia", "<b>Peritonitis / &iacute;leo paral&iacute;tico</b>", "abdomen agudo quir&uacute;rgico: cirug&iacute;a urgente"),
        ("Ruidos ausentes + dolor desproporcionado", "FA/cardiopat&iacute;a embol&iacute;gena", "Lactato y D-d&iacute;mero elevados", "<b>Isquemia mesent&eacute;rica</b>", "angioTC urgente; tiempo es intestino"),
        ("Soplo abdominal", "Dolor postprandial cr&oacute;nico + p&eacute;rdida de peso", "Sitofobia", "Isquemia mesent&eacute;rica cr&oacute;nica", "angina abdominal por ateromatosis"),
    ]),
    ("PALPACION", [
        ("Dolor m&aacute;ximo en punto de McBurney", "Blumberg (rebote) positivo", "Psoas/Rovsing positivos", "Apendicitis", "Alvarado &ge;7; ecograf&iacute;a/TC; apendicectom&iacute;a"),
        ("Defensa y masa dolorosa en FII", "Fiebre + &gt;50a", "Blumberg local", "Diverticulitis", "TC: clasificaci&oacute;n de Hinchey; ATB +/- drenaje"),
        ("Abdomen en tabla (defensa generalizada)", "Blumberg difuso", "Inmovilidad antial&aacute;gica", "<b>Peritonitis por perforaci&oacute;n</b>", "aire libre en Rx t&oacute;rax; laparotom&iacute;a urgente"),
        ("Masa palpable en FID + febr&iacute;cula", "Diarrea cr&oacute;nica + p&eacute;rdida de peso", "Fisura perianal asociada", "Crohn (plast&oacute;n/absceso)", "colonoscopia + calprotectina; biolog&iacute;a si fistuliza"),
        ("Masa abdominal dura irregular + adenopat&iacute;as", "S&iacute;ndrome constitucional", "Hepatomegalia nodular", "C&aacute;ncer de colon", "colonoscopia + biopsia; estadiaje TC; CEA"),
    ]),
    ("PERCUSION", [
        ("Timpanismo generalizado aumentado", "Distensi&oacute;n + obstrucci&oacute;n", "Asa fija dilatada", "Obstrucci&oacute;n intestinal", "diferenciar mec&aacute;nica de &iacute;leo"),
        ("P&eacute;rdida de la matidez hep&aacute;tica", "Aire libre subdiafragm&aacute;tico", "Abdomen en tabla", "<b>V&iacute;scera perforada</b>", "signo de Jobert; neumoperitoneo: cirug&iacute;a urgente"),
        ("Matidez cambiante (ascitis)", "Oleada asc&iacute;tica", "Hepatopat&iacute;a + colaterales", "Ascitis (hipertensi&oacute;n portal)", "paracentesis diagn&oacute;stica; descartar PBE"),
    ]),
    ("TACTO RECTAL", [
        ("Sangre roja brillante en el dedo de guante", "Paquetes hemorroidales no dolorosos", "Prolapso al esfuerzo", "Hemorroides", "grado y tratamiento seg&uacute;n cl&iacute;nica; ligadura/cirug&iacute;a"),
        ("Dolor intenso que impide el tacto + esp&aacute;sticidad", "Desgarro posterior en l&iacute;nea media", "Sangre roja al defecar + estre&ntilde;imiento", "Fisura anal", "ba&ntilde;os de asiento + nitroglicerina/diltiazem t&oacute;pico"),
        ("Tumoraci&oacute;n fluctuante perianal dolorosa", "Fiebre + eritema local", "Supuraci&oacute;n", "<b>Absceso perianal</b>", "drenaje quir&uacute;rgico urgente; vigilar f&iacute;stula"),
        ("Masa rectal dura fija + sangre/moco", "Dedil manchado de sangre oscura", "Cambio del ritmo intestinal", "C&aacute;ncer de recto", "colonoscopia + biopsia; RM pelvis para estadiaje"),
        ("Heces negras alquitranadas (melena) en el dedil", "Hematemesis + AINE", "Anemia", "HDA por &uacute;lcera p&eacute;ptica", "endoscopia urgente; IBP iv; clasificaci&oacute;n de Forrest"),
    ]),
]
