# -*- coding: utf-8 -*-
NAME = "Piel"

EJES = [
  ("Lesi&oacute;n eritematosa / infecci&oacute;n de piel", [
    ("Placa eritematosa mal delimitada + caliente + dolorosa + afecta dermis-tejido subcut&aacute;neo", "Celulitis"),
    ("Placa eritematosa MUY bien delimitada + borde sobreelevado + brillante + cara/MMII", "Erisipela"),
    ("Costras melic&eacute;ricas color miel + ni&ntilde;os + periorificial", "Imp&eacute;tigo"),
    ("Dolor DESPROPORCIONADO a la lesi&oacute;n + crepitaci&oacute;n + bullas hemorr&aacute;gicas + toxicidad sist&eacute;mica", "<b>Fascitis necrotizante</b>"),
    ("Eritema + edema + fiebre + linfangitis ascendente (cord&oacute;n rojo)", "Celulitis con linfangitis"),
    ("Eritema perilesional + supuraci&oacute;n + fluctuaci&oacute;n localizada", "Absceso cut&aacute;neo"),
  ]),
  ("Exantema farmacol&oacute;gico grave", [
    ("M&aacute;culas en diana at&iacute;picas + despegamiento &lt;10% superficie + mucosas afectadas + f&aacute;rmaco reciente", "<b>S&iacute;ndrome de Stevens-Johnson (SSJ)</b>"),
    ("Despegamiento epid&eacute;rmico &gt;30% superficie + Nikolsky positivo + mucosas + f&aacute;rmaco", "<b>Necr&oacute;lisis epid&eacute;rmica t&oacute;xica (NET)</b>"),
    ("Exantema morbiliforme extenso + fiebre + eosinofilia + afectaci&oacute;n hep&aacute;tica + f&aacute;rmaco 2-8 semanas antes", "<b>DRESS</b>"),
    ("Edema facial + adenopat&iacute;as + eosinofilia tras anticonvulsivante/alopurinol", "<b>DRESS</b>"),
    ("Eritema doloroso + ampollas fl&aacute;ccidas + Nikolsky positivo + mucosa oral erosionada", "<b>SSJ / NET</b>"),
  ]),
  ("Lesi&oacute;n pigmentada / tumoral", [
    ("L&eacute;si&oacute;n pigmentada Asim&eacute;trica + Bordes irregulares + Color heterog&eacute;neo + Di&aacute;metro &gt;6 mm + Evoluci&oacute;n (ABCDE)", "Melanoma"),
    ("P&aacute;pula perlada + telangiectasias en superficie + borde enrollado + &uacute;lcera central + zona fotoexpuesta", "Carcinoma basocelular"),
    ("Placa o n&oacute;dulo hiperqueratosico + costra + crecimiento sobre queratosis act&iacute;nica/cicatriz", "Carcinoma epidermoide"),
    ("L&eacute;si&oacute;n que sangra/ulcera y no cura + cambio reciente en nevus previo", "Tumor cut&aacute;neo (melanoma/CE) hasta descartar"),
    ("N&oacute;dulo pigmentado + halo inflamatorio + crecimiento r&aacute;pido + adenopat&iacute;a regional", "Melanoma con diseminaci&oacute;n"),
  ]),
  ("&Uacute;lcera cr&oacute;nica", [
    ("&Uacute;lcera supramaleolar interna + bordes irregulares + exudativa + hiperpigmentaci&oacute;n + pulsos presentes", "&Uacute;lcera venosa"),
    ("&Uacute;lcera distal/acra + bordes netos en sacabocados + dolorosa + pulsos AUSENTES + piel fr&iacute;a p&aacute;lida", "&Uacute;lcera arterial"),
    ("&Uacute;lcera plantar en punto de presi&oacute;n + indolora + neuropat&iacute;a + diab&eacute;tico", "&Uacute;lcera diab&eacute;tica (neurop&aacute;tica)"),
    ("&Uacute;lcera sobre prominencia &oacute;sea (sacro/tal&oacute;n) + paciente encamado + inmovilidad", "&Uacute;lcera por presi&oacute;n"),
    ("&Uacute;lcera + dolor desproporcionado + bordes necr&oacute;ticos + progresi&oacute;n r&aacute;pida + crepitaci&oacute;n", "<b>Fascitis necrotizante sobre &uacute;lcera</b>"),
  ]),
  ("Prurito / ampollas", [
    ("Ampollas fl&aacute;ccidas + Nikolsky positivo + erosiones mucosas cr&oacute;nicas SIN f&aacute;rmaco desencadenante", "P&eacute;nfigo vulgar (cr&oacute;nico autoinmune; el agudo + f&aacute;rmaco ser&iacute;a SSJ/NET)"),
    ("Ampollas TENSAS + base eritematosa + prurito intenso + Nikolsky NEGATIVO + anciano", "Penfigoide ampolloso"),
    ("Exantema pruriginoso + f&aacute;rmaco reciente + posible progresi&oacute;n a despegamiento", "<b>Reacci&oacute;n farmacol&oacute;gica grave (vigilar SSJ/NET)</b>"),
    ("Costras melic&eacute;ricas pruriginosas + contagio en ni&ntilde;os", "Imp&eacute;tigo"),
  ]),
]

ESTACIONES = [
  ("INSPECCION DE LA LESION", [
    ("Placa eritematosa MUY bien delimitada + borde sobreelevado", "Brillante + caliente", "Localizaci&oacute;n en cara o pierna", "Erisipela", "borde n&iacute;tido distingue erisipela de celulitis; antibi&oacute;tico antiestreptoc&oacute;cico"),
    ("Placa eritematosa MAL delimitada + l&iacute;mites difusos", "Caliente + edematosa", "Afecta tejido subcut&aacute;neo", "Celulitis", "borde impreciso y profundidad mayor que la erisipela"),
    ("Costras color miel (melic&eacute;ricas)", "Distribuci&oacute;n periorificial", "Ni&ntilde;o + contagio", "Imp&eacute;tigo", "costra mielic&eacute;rica = infecci&oacute;n superficial por S. aureus/estreptococo"),
    ("L&eacute;si&oacute;n pigmentada Asim&eacute;trica + Bordes irregulares", "Color heterog&eacute;neo + Di&aacute;metro &gt;6 mm", "Evoluci&oacute;n/cambio reciente (ABCDE)", "Melanoma", "regla ABCDE: derivo para biopsia escisional, nunca afeitado"),
    ("P&aacute;pula perlada con telangiectasias + borde enrollado", "&Uacute;lcera central que no cura", "Zona fotoexpuesta (cara)", "Carcinoma basocelular", "perla + telangiectasias en zona solar; crecimiento lento y local"),
    ("Placa hiperqueratosica/costrosa sobre piel fotoda&ntilde;ada", "Crece y ulcera", "Sobre queratosis act&iacute;nica o cicatriz", "Carcinoma epidermoide", "puede metastatizar; valoro adenopat&iacute;as regionales"),
  ]),
  ("PALPACION", [
    ("Dolor DESPROPORCIONADO a los hallazgos visibles", "Crepitaci&oacute;n (gas en tejidos)", "Toxicidad sist&eacute;mica + progresi&oacute;n r&aacute;pida", "<b>Fascitis necrotizante</b>", "dolor desproporcionado + crepitaci&oacute;n = urgencia quir&uacute;rgica, desbridamiento inmediato"),
    ("Fluctuaci&oacute;n localizada a la presi&oacute;n", "Eritema y calor perilesional", "Punto de m&aacute;ximo dolor", "Absceso cut&aacute;neo", "fluctuaci&oacute;n = colecci&oacute;n; requiere drenaje, no solo antibi&oacute;tico"),
    ("Induraci&oacute;n y calor sin fluctuaci&oacute;n", "Borde mal definido", "Cord&oacute;n rojo ascendente (linfangitis)", "Celulitis con linfangitis", "trazo eritematoso ascendente sigue v&iacute;a linf&aacute;tica"),
  ]),
  ("SIGNO DE NIKOLSKY / AMPOLLAS", [
    ("Presi&oacute;n tangencial DESPEGA la epidermis (Nikolsky positivo)", "Ampollas fl&aacute;ccidas + erosiones extensas", "F&aacute;rmaco reciente + mucosas afectadas", "<b>SSJ / NET</b>", "Nikolsky positivo + f&aacute;rmaco = emergencia, suspendo el f&aacute;rmaco y derivo a unidad de quemados"),
    ("Ampollas TENSAS que NO se despegan (Nikolsky negativo)", "Base eritematosa + prurito intenso", "Paciente anciano", "Penfigoide ampolloso", "ampolla tensa y Nikolsky negativo lo separan del p&eacute;nfigo y de la NET"),
    ("Ampollas fl&aacute;ccidas + Nikolsky positivo", "Erosiones mucosas dolorosas cr&oacute;nicas", "Sin f&aacute;rmaco desencadenante claro", "P&eacute;nfigo vulgar", "autoinmune; Nikolsky positivo tambi&eacute;n, pero curso cr&oacute;nico no farmacol&oacute;gico"),
  ]),
  ("EXPLORACION DE MUCOSAS", [
    ("Erosiones y costras hemorr&aacute;gicas en labios", "Conjuntivitis + erosiones genitales", "F&aacute;rmaco 1-3 semanas antes", "<b>SSJ / NET</b>", "afectaci&oacute;n de &ge;2 mucosas + f&aacute;rmaco orienta a SSJ/NET, no a un exantema banal"),
    ("Mucosa oral erosionada dolorosa cr&oacute;nica", "Sin desencadenante farmacol&oacute;gico", "Ampollas fl&aacute;ccidas cut&aacute;neas", "P&eacute;nfigo vulgar", "las erosiones orales suelen ser el primer signo del p&eacute;nfigo"),
    ("Mucosas RESPETADAS", "Exantema morbiliforme extenso + edema facial", "Fiebre + eosinofilia + alteraci&oacute;n hep&aacute;tica", "<b>DRESS</b>", "DRESS afecta &oacute;rganos internos m&aacute;s que mucosas; pido hemograma y transaminasas"),
  ]),
  ("PULSOS / PERFUSION EN ULCERAS", [
    ("Pulsos dist&aacute;les AUSENTES + piel fr&iacute;a y p&aacute;lida", "&Uacute;lcera acra dolorosa en sacabocados", "Mejora al colgar la pierna", "&Uacute;lcera arterial", "ausencia de pulsos + dolor = isquemia; pido &iacute;ndice tobillo-brazo, no comprimo"),
    ("Pulsos PRESENTES + edema + hiperpigmentaci&oacute;n", "&Uacute;lcera supramaleolar interna exudativa", "Mejora con elevaci&oacute;n de la pierna", "&Uacute;lcera venosa", "pulsos conservados + estasis venosa = compresi&oacute;n (tras descartar arteriopat&iacute;a)"),
    ("Sensibilidad ABOLIDA (monofilamento) + pulsos variables", "&Uacute;lcera plantar indolora en punto de presi&oacute;n", "Diab&eacute;tico", "&Uacute;lcera diab&eacute;tica (neurop&aacute;tica)", "&uacute;lcera indolora en zona de carga = neuropat&iacute;a; descargo presi&oacute;n y exploro perfusi&oacute;n"),
    ("Eritema que no blanquea sobre prominencia &oacute;sea", "&Uacute;lcera en sacro o tal&oacute;n", "Paciente encamado/inmovilizado", "&Uacute;lcera por presi&oacute;n", "presi&oacute;n mantenida sobre hueso; cambios posturales y al&iacute;vio de presi&oacute;n"),
  ]),
]
