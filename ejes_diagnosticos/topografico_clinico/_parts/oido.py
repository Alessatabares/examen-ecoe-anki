NAME = "Oido"

EJES = [
    ("Otalgia", [
        ("Dolor al traccionar el pabell&oacute;n + signo del trago positivo", "Otitis externa"),
        ("Otalgia tras ba&ntilde;o o limpieza con bastoncillos + prurito previo", "Otitis externa"),
        ("Otalgia interna intensa tras IVAS + fiebre + hipoacusia", "Otitis media aguda"),
        ("Otalgia retroauricular + desplazamiento del pabell&oacute;n hacia delante", "<b>Mastoiditis</b>"),
        ("Otalgia referida sin hallazgos en otoscopia (descartar patolog&iacute;a dentaria/ATM/far&iacute;ngea)", "Otalgia refleja"),
    ]),
    ("Otorrea", [
        ("Otorrea purulenta tras perforaci&oacute;n + cede la otalgia bruscamente", "Otitis media aguda perforada"),
        ("Otorrea cr&oacute;nica fetida + perla blanca en &aacute;tico (otoscopia)", "Colesteatoma"),
        ("Otorrea acuosa-mucoide cr&oacute;nica sin dolor + perforaci&oacute;n central seca", "Otitis media cr&oacute;nica simple"),
        ("Otorrea escasa + conducto edematoso y eccematoso + dolor al trago", "Otitis externa"),
        ("Hipoacusia de transmisi&oacute;n + t&iacute;mpano deslustrado sin perforaci&oacute;n (otoscopia)", "Otitis media con derrame"),
    ]),
    ("Hipoacusia y acufeno", [
        ("Hipoacusia de transmisi&oacute;n + Rinne negativo + Weber lateraliza al o&iacute;do enfermo", "Hipoacusia de transmisi&oacute;n"),
        ("Hipoacusia neurosensorial + Rinne positivo + Weber lateraliza al o&iacute;do sano", "Hipoacusia neurosensorial"),
        ("Hipoacusia fluctuante + acufeno + sensaci&oacute;n de plenitud &oacute;tica + v&eacute;rtigo recurrente", "Enfermedad de M&eacute;ni&egrave;re"),
        ("Hipoacusia neurosensorial unilateral progresiva + acufeno + inestabilidad (descartar)", "Schwannoma vestibular"),
        ("Hipoacusia neurosensorial s&uacute;bita unilateral en horas-d&iacute;as", "<b>Hipoacusia s&uacute;bita</b>"),
    ]),
    ("Vertigo y mareo", [
        ("V&eacute;rtigo breve (&lt; 1 min) desencadenado por cambios de posici&oacute;n cefal&iacute;ca + Dix-Hallpike positivo", "VPPB"),
        ("V&eacute;rtigo rotatorio de horas + acufeno + hipoacusia fluctuante", "Enfermedad de M&eacute;ni&egrave;re"),
        ("V&eacute;rtigo intenso continuo de d&iacute;as tras cuadro viral + sin hipoacusia ni acufeno", "Neuritis vestibular"),
        ("V&eacute;rtigo + hipoacusia s&uacute;bita unilateral", "Laberintitis — pero la hipoacusia s&uacute;bita es URGENCIA ORL: descartar causa central/retrococlear y dar corticoides precoces"),
        ("Inestabilidad + cefalea + foco neurol&oacute;gico o nistagmo vertical/multidireccional", "<b>V&eacute;rtigo central</b>"),
    ]),
]

ESTACIONES = [
    ("OTOSCOPIA", [
        ("Conducto edematoso y eccematoso", "T&iacute;mpano normal mal visible", "Dolor a la introducci&oacute;n del espejo", "Otitis externa", "limpio y aplico gotas t&oacute;picas con antibi&oacute;tico-corticoide"),
        ("T&iacute;mpano abombado e hiper&eacute;mico", "P&eacute;rdida del tri&aacute;ngulo luminoso", "Nivel hidroa&eacute;reo o pus", "Otitis media aguda", "valoro analgesia &plusmn; antibi&oacute;tico seg&uacute;n criterios"),
        ("T&iacute;mpano deslustrado retra&iacute;do", "Burbujas-nivel tras el t&iacute;mpano", "Sin abombamiento ni otalgia", "Otitis media con derrame", "timpanometr&iacute;a curva B; reviso a las semanas"),
        ("Perla blanca-escamas en &aacute;tico", "Perforaci&oacute;n marginal", "Otorrea fetida cr&oacute;nica", "Colesteatoma", "deriv&oacute; a ORL: TC y cirug&iacute;a"),
        ("Perforaci&oacute;n central seca", "Hipoacusia de transmisi&oacute;n", "Sin colesteatoma", "Otitis media cr&oacute;nica simple", "evito agua y deriv&oacute; para timpanoplastia"),
    ]),
    ("SIGNO DEL TRAGO Y PALPACION", [
        ("Dolor al presionar el trago", "Dolor al traccionar el pabell&oacute;n", "Conducto inflamado", "Otitis externa", "diagn&oacute;stico cl&iacute;nico; trato t&oacute;pico"),
        ("Tumefacci&oacute;n retroauricular", "Pabell&oacute;n desplazado hacia delante-afuera", "Dolor y eritema sobre mastoides", "<b>Mastoiditis</b>", "urgencia: ingreso, antibi&oacute;tico IV y TC"),
        ("Trago indoloro", "Sin dolor mastoideo", "Otalgia interna profunda", "Otitis media aguda", "exploro t&iacute;mpano en otoscopia"),
        ("Adenopat&iacute;a preauricular dolorosa", "Conducto ocupado", "Trago positivo", "Otitis externa difusa", "descarto extensi&oacute;n y trato"),
    ]),
    ("ACUMETRIA RINNE Y WEBER", [
        ("Rinne NEGATIVO en o&iacute;do afecto", "Weber lateraliza al o&iacute;do ENFERMO", "V&iacute;a &oacute;sea &gt; a&eacute;rea", "Hipoacusia de transmisi&oacute;n", "busco causa: cerumen, derrame, perforaci&oacute;n"),
        ("Rinne POSITIVO en ambos", "Weber lateraliza al o&iacute;do SANO", "V&iacute;a a&eacute;rea &gt; &oacute;sea", "Hipoacusia neurosensorial", "audiometr&iacute;a; descarto retrococlear"),
        ("Hipoacusia neurosensorial fluctuante", "Acufeno + plenitud &oacute;tica", "Crisis de vertigo", "Enfermedad de M&eacute;ni&egrave;re", "audiometr&iacute;a seriada y dieta hipos&oacute;dica"),
        ("Hipoacusia neurosensorial s&uacute;bita", "Weber al o&iacute;do sano", "Sin causa transmisiva", "<b>Hipoacusia s&uacute;bita</b>", "urgencia ORL: corticoides precoces"),
    ]),
    ("EXPLORACION VESTIBULAR", [
        ("Dix-Hallpike POSITIVO", "Nistagmo torsional con latencia y agotable", "V&eacute;rtigo breve posicional", "VPPB", "maniobra de Epley reposicionadora"),
        ("Nistagmo horizonto-rotatorio unidireccional", "Inhibido por fijaci&oacute;n visual", "Head-impulse POSITIVO al lado afecto", "Neuritis vestibular", "perif&eacute;rico: sedantes vestibulares cortos y rehabilitaci&oacute;n"),
        ("Nistagmo vertical o multidireccional", "NO se inhibe con fijaci&oacute;n", "Head-impulse NEGATIVO + foco neurol&oacute;gico", "<b>V&eacute;rtigo central</b>", "urgencia: neuroimagen (descarto ictus)"),
        ("V&eacute;rtigo rotatorio episodios horas", "Acufeno e hipoacusia ipsilateral", "Romberg inestable", "Enfermedad de M&eacute;ni&egrave;re", "trato la crisis y derivo a ORL"),
    ]),
]
