# -*- coding: utf-8 -*-
NAME = "Ojo"

EJES = [
  ("Ojo rojo", [
    ("Secreci&oacute;n + sensaci&oacute;n de arenilla + visi&oacute;n conservada + sin dolor profundo", "Conjuntivitis"),
    ("Hiperemia ciliar (periqueratica) + dolor + fotofobia + miosis + Tyndall en c&aacute;mara anterior", "Uve&iacute;tis anterior"),
    ("<b>Dolor intenso + halos de colores + midriasis media fija + ojo duro p&eacute;treo + n&aacute;useas</b>", "<b>Glaucoma agudo de &aacute;ngulo cerrado</b>"),
    ("Dolor profundo que despierta por la noche + enrojecimiento violaceo + asociado a enfermedad reum&aacute;tica", "Escleritis"),
    ("Enrojecimiento sectorial superficial + no doloroso + no afecta visi&oacute;n", "Epiescleritis"),
    ("Inyecci&oacute;n + dolor + defecto que ti&ntilde;e con fluoresce&iacute;na + antecedente de cuerpo extra&ntilde;o", "Queratitis / &uacute;lcera corneal"),
  ]),
  ("P&eacute;rdida visual s&uacute;bita indolora", [
    ("Brusca + altitudinal o total + defecto pupilar aferente + fondo con retina p&aacute;lida y m&aacute;cula rojo cereza", "Oclusi&oacute;n de arteria central de la retina"),
    ("Brusca o en horas + fondo con hemorragias en llama difusas y venas tortuosas (retina en tormenta)", "Oclusi&oacute;n de vena central de la retina"),
    ("Cortina ascendente + destellos (fotopsias) + miodesopsias (moscas) previas", "Desprendimiento de retina"),
    ("Subaguda + dolor con los movimientos oculares + discromatopsia + defecto pupilar aferente", "Neuritis &oacute;ptica"),
    ("Brusca unilateral en mayor de 50 + cefalea temporal + claudicaci&oacute;n mandibular + VSG alta", "<b>Neuropat&iacute;a &oacute;ptica isqu&eacute;mica por arteritis de la temporal</b>"),
    ("Lluvia de moscas/telara&ntilde;a roja + diab&eacute;tico + p&eacute;rdida brusca", "Hemorragia v&iacute;trea"),
  ]),
  ("P&eacute;rdida visual gradual", [
    ("Visi&oacute;n borrosa progresiva + deslumbramiento + halos + leucocoria + reflejo rojo disminuido", "Cataratas"),
    ("P&eacute;rdida del campo perif&eacute;rico (visi&oacute;n en t&uacute;nel) + excavaci&oacute;n papilar + PIO elevada", "Glaucoma cr&oacute;nico de &aacute;ngulo abierto"),
    ("Escotoma central + metamorfopsias + drusas o membrana neovascular en m&aacute;cula en mayor de 60", "Degeneraci&oacute;n macular asociada a la edad (DMAE)"),
    ("Diab&eacute;tico de larga evoluci&oacute;n + microaneurismas + exudados + neovasos en fondo de ojo", "Retinopat&iacute;a diab&eacute;tica"),
    ("Defectos campim&eacute;tricos bitemporales + cefalea + alteraci&oacute;n endocrina", "Compresi&oacute;n quiasm&aacute;tica (adenoma hipofisario)"),
  ]),
  ("Dolor ocular / proptosis", [
    ("<b>Dolor a la mirada + proptosis + oftalmoplej&iacute;a + quemosis + fiebre</b>", "<b>Celulitis orbitaria</b>"),
    ("Edema y eritema palpebral + visi&oacute;n y motilidad normales + sin dolor a la mirada + sin proptosis", "Celulitis preseptal"),
    ("N&oacute;dulo doloroso en el borde palpebral apuntando a pesta&ntilde;as", "Orzuelo"),
    ("N&oacute;dulo indoloro firme alejado del borde, de evoluci&oacute;n lenta", "Chalazion"),
    ("Proptosis bilateral + retracci&oacute;n palpebral + diplopia + bocio/tirotoxicosis", "Orbitopat&iacute;a tiroidea (Graves)"),
  ]),
]

ESTACIONES = [
  ("INSPECCION DEL OJO ROJO", [
    ("Pupila en midriasis media fija + ojo duro p&eacute;treo a la palpaci&oacute;n", "Halos de colores + visi&oacute;n borrosa", "Dolor intenso + n&aacute;useas y v&oacute;mitos", "<b>Glaucoma agudo de &aacute;ngulo cerrado</b>", "es cl&iacute;nico: bajar la PIO YA con acetazolamida IV + hipotensores t&oacute;picos (manitol si no cede); la pilocarpina va DESPU&Eacute;S de bajar la PIO, no de primera; derivaci&oacute;n urgente"),
    ("Hiperemia ciliar periqueratica + miosis", "Tyndall (c&eacute;lulas en c&aacute;mara anterior) + hipopion", "Fotofobia + dolor profundo", "Uve&iacute;tis anterior", "midri&aacute;ticos + corticoide t&oacute;pico y buscar enfermedad sist&eacute;mica asociada"),
    ("Hiperemia conjuntival difusa + secreci&oacute;n", "Visi&oacute;n conservada + sin dolor profundo", "Reflejo pupilar normal", "Conjuntivitis", "diferencio v&iacute;rica/bacteriana/al&eacute;rgica; alarma si dolor o baja visi&oacute;n &rarr; descarto causa grave"),
    ("Defecto epitelial que ti&ntilde;e verde con fluoresce&iacute;na", "Dolor + sensaci&oacute;n de cuerpo extra&ntilde;o + blefaroespasmo", "Antecedente de lente de contacto o trauma", "Queratitis / &uacute;lcera corneal", "no parchear ni dar anest&eacute;sico t&oacute;pico cr&oacute;nico; cubrir y derivar"),
  ]),
  ("PUPILAS Y REFLEJOS", [
    ("Defecto pupilar aferente relativo (Marcus Gunn) al test de luz alternante", "Visi&oacute;n muy disminuida en ese ojo", "Dolor con los movimientos o fondo p&aacute;lido", "Neuritis &oacute;ptica / neuropat&iacute;a &oacute;ptica", "el DPAR localiza la lesi&oacute;n en nervio &oacute;ptico/retina extensa, no en el cristalino"),
    ("Midriasis arreactiva unilateral + ptosis + ojo desviado abajo y afuera", "Cefalea brusca intensa", "Posible aneurisma de comunicante posterior", "<b>Paresia del III par compresiva</b>", "midriasis + dolor = urgencia neuroquir&uacute;rgica, descartar aneurisma"),
    ("Anisocoria mayor en oscuridad + ptosis leve (mismo lado) + anhidrosis facial", "Sin afectaci&oacute;n de la motilidad", "Posible disecci&oacute;n carot&iacute;dea o masa apical", "S&iacute;ndrome de Horner", "la miosis del lado afecto se hace evidente en penumbra"),
    ("Pupilas peque&ntilde;as que no reaccionan a la luz pero s&iacute; a la convergencia", "Disociaci&oacute;n luz-cerca bilateral", "Antecedente neurol&oacute;gico/l&uacute;es", "Pupila de Argyll Robertson", "diferenciar de la pupila t&oacute;nica de Adie (unilateral, reacci&oacute;n lenta)"),
  ]),
  ("AGUDEZA VISUAL Y CAMPOS", [
    ("Agudeza que mejora al mirar por un agujero estenopeico", "Borrosidad + halos sin ojo rojo", "Sin defecto pupilar", "Defecto refractivo o catarata", "el estenopeico que mejora orienta a causa &oacute;ptica, no neurol&oacute;gica"),
    ("Campimetr&iacute;a con p&eacute;rdida perif&eacute;rica progresiva (visi&oacute;n en t&uacute;nel)", "PIO elevada + excavaci&oacute;n papilar aumentada", "Asintom&aacute;tico hasta fases avanzadas", "Glaucoma cr&oacute;nico de &aacute;ngulo abierto", "el campo central se conserva hasta el final; cribado de PIO y papila"),
    ("Hemianopsia bitemporal en la confrontaci&oacute;n", "Cefalea + s&iacute;ntomas endocrinos", "Defecto que respeta el meridiano vertical", "Lesi&oacute;n del quiasma &oacute;ptico", "el patr&oacute;n campim&eacute;trico localiza la lesi&oacute;n en la v&iacute;a visual"),
    ("Escotoma central con rejilla de Amsler distorsionada (metamorfopsias)", "Mayor de 60 + drusas en m&aacute;cula", "Dificultad para leer caras y letras", "Degeneraci&oacute;n macular (DMAE)", "afecta visi&oacute;n central fina; deriva la forma h&uacute;meda urgente por anti-VEGF"),
  ]),
  ("FONDO DE OJO", [
    ("Retina p&aacute;lida y edematosa con m&aacute;cula rojo cereza + arterias filiformes", "P&eacute;rdida visual brusca indolora total", "Defecto pupilar aferente", "<b>Oclusi&oacute;n de arteria central de la retina</b>", "ventana terap&eacute;utica corta: masaje ocular y derivaci&oacute;n inmediata, descartar arteritis"),
    ("Hemorragias en llama difusas + venas tortuosas + edema de papila (retina en tormenta)", "P&eacute;rdida visual subaguda", "Factores de riesgo cardiovascular", "Oclusi&oacute;n de vena central de la retina", "patr&oacute;n hemorr&aacute;gico difuso por estasis venoso, no por isquemia arterial"),
    ("Microaneurismas + exudados duros + hemorragias puntiformes + neovasos", "Diab&eacute;tico de larga evoluci&oacute;n", "Visi&oacute;n a&uacute;n conservada o borrosa", "Retinopat&iacute;a diab&eacute;tica", "la fase proliferativa con neovasos exige panfotocoagulaci&oacute;n"),
    ("Papila con borde difuminado y elevada (edema de papila) bilateral", "Cefalea + n&aacute;useas + visi&oacute;n transitoriamente borrosa", "Sin defecto pupilar aferente (bilateral)", "Papiledema por hipertensi&oacute;n intracraneal", "edema bilateral + cefalea &rarr; descarto masa/HTIC, no es neuritis"),
    ("Excavaci&oacute;n papilar aumentada (relaci&oacute;n copa/disco &gt; 0.6)", "PIO elevada", "Campo perif&eacute;rico reducido", "Glaucoma cr&oacute;nico", "la excavaci&oacute;n progresiva del nervio es el da&ntilde;o estructural del glaucoma"),
  ]),
  ("MOTILIDAD OCULAR", [
    ("<b>Dolor a la mirada + limitaci&oacute;n de la motilidad + proptosis + quemosis</b>", "Fiebre + edema palpebral", "Diplopia", "<b>Celulitis orbitaria</b>", "dolor a la mirada + proptosis = orbitaria (no preseptal): TC e ingreso con antibi&oacute;tico IV"),
    ("Motilidad y visi&oacute;n normales + edema y eritema palpebral sin proptosis", "Sin dolor a los movimientos oculares", "Afebril o febr&iacute;cula", "Celulitis preseptal", "la motilidad y visi&oacute;n conservadas la distinguen de la orbitaria"),
    ("Diplopia binocular + ojo desviado abajo y afuera + ptosis + midriasis", "Cefalea", "Empeora al cerrar el ojo sano", "Paresia del III par craneal", "comprobar pupila: si est&aacute; afectada, sospecho compresi&oacute;n/aneurisma"),
    ("Diplopia horizontal que aumenta al mirar al lado afecto (no abduce)", "Antecedente de HTIC o trauma", "Ojo en aducci&oacute;n en reposo", "Paresia del VI par craneal", "es el de recorrido m&aacute;s largo: falso signo localizador de HTIC"),
    ("Proptosis bilateral + retracci&oacute;n palpebral + restricci&oacute;n a la supraversi&oacute;n", "Bocio + temblor + p&eacute;rdida de peso", "Diplopia", "Orbitopat&iacute;a tiroidea (Graves)", "la restricci&oacute;n muscular es mec&aacute;nica por engrosamiento, no neurol&oacute;gica"),
  ]),
]
