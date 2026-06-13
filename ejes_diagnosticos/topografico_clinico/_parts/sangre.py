# -*- coding: utf-8 -*-

NAME = "Sangre / Hematologico"

EJES = [
    ("S&iacute;ndrome an&eacute;mico (clasificar por VCM)", [
        ("Astenia + palidez + disnea de esfuerzo + VCM &lt;80 (microc&iacute;tica) + ferritina baja", "Anemia ferrop&eacute;nica &rarr; buscar p&eacute;rdida digestiva/menstrual oculta"),
        ("Microc&iacute;tica + ferritina normal/alta + enfermedad cr&oacute;nica/inflamatoria de base", "Anemia de trastornos cr&oacute;nicos (hierro secuestrado, hepcidina alta)"),
        ("VCM 80-100 (normoc&iacute;tica) + reticulocitos altos + ictericia + LDH alta + haptoglobina baja", "Anemia hemol&iacute;tica &rarr; Coombs, frotis (esquistocitos vs esferocitos)"),
        ("VCM &gt;100 (macroc&iacute;tica) + glositis + parestesias + alteraci&oacute;n de la marcha", "Anemia por d&eacute;ficit de B12 (megaloblastica con afectaci&oacute;n neurol&oacute;gica)"),
        ("Macroc&iacute;tica + alcoholismo o malabsorci&oacute;n, sin cl&iacute;nica neurol&oacute;gica", "D&eacute;ficit de folato (megaloblastica sin neuropat&iacute;a)"),
        ("Pancitopenia + reticulocitos bajos + m&eacute;dula vac&iacute;a en biopsia", "Anemia apl&aacute;sica &rarr; descartar f&aacute;rmacos/t&oacute;xicos"),
        ("Anemia microc&iacute;tica + origen mediterr&aacute;neo + RDW normal + electroforesis con HbA2 alta", "Talasemia (microcitosis desproporcionada al grado de anemia)"),
    ]),
    ("Serie roja alta / poliglobulia", [
        ("Hto/Hb altos + prurito tras la ducha (acuag&eacute;nico) + plaquetas y leucocitos altos + EPO baja", "Policitemia vera &rarr; JAK2; riesgo de trombosis, flebotom&iacute;as"),
        ("Hto alto aislado + EPO alta + EPOC/tabaquismo/altitud/SAOS", "Poliglobulia secundaria (hipoxia cr&oacute;nica, EPO elevada apropiada)"),
        ("Hto alto + plaquetas muy altas + esplenomegalia + leucoeritroblastosis en frotis", "S&iacute;ndrome mieloproliferativo cr&oacute;nico (estudio JAK2/BCR-ABL)"),
        ("Hto aparentemente alto por hemoconcentraci&oacute;n (deshidrataci&oacute;n/diur&eacute;ticos)", "Poliglobulia relativa (masa eritrocitaria normal)"),
    ]),
    ("Serie blanca / m&eacute;dula (s&iacute;ndrome B y fiebre)", [
        ("Fiebre + neutr&oacute;filos &lt;500 en paciente con quimioterapia reciente", "<b>Neutropenia febril</b> &rarr; URGENCIA: antibi&oacute;tico de amplio espectro &lt;1 h"),
        ("Astenia + sangrado + infecciones + blastos &gt;20% en sangre/m&eacute;dula", "<b>Leucemia aguda</b> &rarr; ingreso; riesgo de CID (sobre todo M3 promieloc&iacute;tica)"),
        ("Leucocitosis muy alta + basofilia + esplenomegalia masiva + cromosoma Filadelfia", "Leucemia mieloide cr&oacute;nica (BCR-ABL; imatinib)"),
        ("Adenopat&iacute;a indolora g&oacute;mica + s&iacute;ndrome B (fiebre, sudoraci&oacute;n, p&eacute;rdida de peso)", "Linfoma &rarr; biopsia escisional; Reed-Sternberg si Hodgkin"),
        ("Linfocitosis madura mantenida en anciano + adenopat&iacute;as + sombras de Gumprecht", "Leucemia linf&aacute;tica cr&oacute;nica (frotis con linfocitos rotos)"),
        ("Anciano + dolor &oacute;seo + anemia + hipercalcemia + insuficiencia renal + pico monoclonal", "Mieloma m&uacute;ltiple (CRAB; banda M en electroforesis)"),
    ]),
    ("Plaquetas y sangrado petequial", [
        ("Petequias + equimosis + sangrado mucoso + plaquetas bajas aisladas, resto normal", "PTI (p&uacute;rpura trombocitop&eacute;nica inmune; trombopenia aislada de exclusi&oacute;n)"),
        ("P&eacute;ntada: trombopenia + anemia hemol&iacute;tica microangiop&aacute;tica + fiebre + cl&iacute;nica neurol&oacute;gica + fallo renal", "<b>PTT</b> &rarr; URGENCIA: plasmaf&eacute;resis; ADAMTS13 bajo, esquistocitos"),
        ("Trombopenia + diarrea sanguinolenta (E. coli O157) + fallo renal en ni&ntilde;o", "<b>SHU (s&iacute;ndrome hemol&iacute;tico ur&eacute;mico)</b> &rarr; microangiopat&iacute;a"),
        ("Trombocitosis &gt;450000 + esplenomegalia + s&iacute;ntomas vasomotores (eritromelalgia)", "Trombocitemia esencial (JAK2; riesgo de trombosis y hemorragia)"),
        ("Trombopenia 5-10 d&iacute;as tras heparina + trombosis paradojica (no sangrado)", "<b>Trombopenia inducida por heparina (TIH)</b> &rarr; suspender heparina"),
        ("Trombopenia leve + esplenomegalia + hepatopat&iacute;a cr&oacute;nica", "Hiperesplenismo (secuestro plaquetario en cirrosis)"),
    ]),
    ("Coagulaci&oacute;n (TP / TTPa)", [
        ("Hemartros y hematomas profundos en var&oacute;n + TTPa alargado + TP normal", "Hemofilia A/B (d&eacute;ficit factor VIII/IX; v&iacute;a intr&iacute;nseca)"),
        ("Sangrado mucoso + epistaxis + TTPa algo alargado + tiempo de sangr&iacute;a alargado", "Enfermedad de von Willebrand (defecto plaquetario-coagulaci&oacute;n m&aacute;s frecuente)"),
        ("TP alargado que corrige con vitamina K + antibi&oacute;ticos/colestasis/malnutrici&oacute;n", "D&eacute;ficit de vitamina K (factores II, VII, IX, X)"),
        ("Sangrado difuso por m&uacute;ltiples sitios + TP y TTPa alargados + fibrin&oacute;geno bajo + D-d&iacute;mero alto + esquistocitos", "<b>CID</b> &rarr; URGENCIA: tratar la causa (sepsis, obst&eacute;trica, neoplasia)"),
        ("TP alargado aislado + hepatopat&iacute;a cr&oacute;nica + s&iacute;ntesis disminuida", "Coagulopat&iacute;a hep&aacute;tica (el h&iacute;gado no sintetiza factores)"),
        ("Sangrado + uso de cumar&iacute;nico + INR muy alto", "Sobredosificaci&oacute;n de anticoagulante oral &rarr; vitamina K &plusmn; complejo protromb&iacute;nico"),
    ]),
    ("Trombosis (Wells, edema unilateral)", [
        ("Edema unilateral de pierna + dolor en pantorrilla + cordon venoso palpable + Wells alto", "TVP &rarr; dimero D y eco-Doppler; anticoagular"),
        ("Disnea s&uacute;bita + dolor pleur&iacute;tico + taquicardia + hipoxemia + TVP asociada", "<b>TEP</b> &rarr; URGENCIA: angio-TC; S1Q3T3 en ECG"),
        ("Trombosis recurrentes/en sitios atipicos + abortos de repetici&oacute;n + TTPa alargado", "S&iacute;ndrome antifosfol&iacute;pido (anticoagulante l&uacute;pico; trombosis paradojica)"),
        ("Trombosis en joven + antecedentes familiares + sin desencadenante claro", "Trombofilia hereditaria (factor V Leiden, protrombina, d&eacute;ficit antitrombina/proteina C-S)"),
        ("Trombosis venosa + neoplasia conocida o s&iacute;ndrome constitucional", "Trombosis paraneopl&aacute;sica (s&iacute;ndrome de Trousseau)"),
    ]),
]

ESTACIONES = [
    ("INSPECCI&Oacute;N DE PIEL Y MUCOSAS", [
        ("Palidez de conjuntivas y lecho ungueal", "Astenia y disnea de esfuerzo", "Taquicardia compensadora", "S&iacute;ndrome an&eacute;mico &rarr; solicito hemograma con VCM y reticulocitos", "la palidez mucocon-juntival orienta a anemia; clasifico luego por VCM"),
        ("Ictericia de escleras", "Coluria + palidez", "Esplenomegalia palpable", "Anemia hemol&iacute;tica &rarr; LDH, bilirrubina indirecta, haptoglobina, Coombs", "ictericia + anemia + reticulocitosis = hem&oacute;lisis"),
        ("Petequias en miembros inferiores que no desaparecen a la vitropresi&oacute;n", "Equimosis espont&aacute;neas", "Sangrado de enc&iacute;as", "Trombopenia &rarr; cuento plaquetas y reviso frotis", "petequia = capilar; no blanquea a la presi&oacute;n (distingue de eritema)"),
        ("P&uacute;rpura palpable en gl&uacute;teos y piernas", "Lesiones sobreelevadas", "Artralgias y dolor abdominal", "P&uacute;rpura vascul&iacute;tica (Sch&ouml;nlein-Henoch) &rarr; plaquetas normales", "p&uacute;rpura palpable orienta a vasculitis, no a trombopenia"),
        ("Prurito intenso tras el ba&ntilde;o caliente", "Plet&oacute;rico/rubicundo", "Eritromelalgia en dedos", "Policitemia vera &rarr; pido Hto, EPO y JAK2", "prurito acuag&eacute;nico + plet&oacute;ra = sospecha de poliglobulia primaria"),
    ]),
    ("PALPACI&Oacute;N DE ADENOPAT&Iacute;AS", [
        ("Adenopat&iacute;a cervical dura, fija y mayor de 2 cm", "Indolora", "Crecimiento progresivo", "Adenopat&iacute;a maligna &rarr; biopsia escisional", "dura, fija, indolora y &gt;2 cm = banderas de malignidad"),
        ("Adenopat&iacute;as m&oacute;viles, blandas y dolorosas", "Asociadas a faringitis/infecci&oacute;n local", "Resoluci&oacute;n en semanas", "Adenopat&iacute;a reactiva (infecciosa benigna)", "blanda, dolorosa y m&oacute;vil orienta a causa inflamatoria"),
        ("Adenopat&iacute;as generalizadas en varios territorios", "Fiebre + sudoraci&oacute;n nocturna + p&eacute;rdida de peso", "Esplenomegalia asociada", "Linfoma con s&iacute;ndrome B &rarr; biopsia y TC de estadiaje", "s&iacute;ntomas B definen estadio y pron&oacute;stico en linfomas"),
        ("Adenopat&iacute;a que duele tras ingesta de alcohol", "Mediast&iacute;nica en radiograf&iacute;a", "Paciente joven", "Linfoma de Hodgkin (dolor adenop&aacute;tico con alcohol)", "explorar todas las cadenas: cervical, axilar, inguinal, epitroclear"),
    ]),
    ("PALPACI&Oacute;N DE BAZO E H&Iacute;GADO", [
        ("Bazo palpable bajo reborde costal en inspiraci&oacute;n", "Matidez espl&eacute;nica aumentada en percusi&oacute;n", "Borde con escotadura caracter&iacute;stica", "Esplenomegalia &rarr; oriento seg&uacute;n tama&ntilde;o y cl&iacute;nica", "el bazo crece hacia fosa il&iacute;aca derecha y tiene escotadura"),
        ("Esplenomegalia masiva que cruza la l&iacute;nea media", "Leucocitosis con basofilia", "Astenia", "Leucemia mieloide cr&oacute;nica &rarr; estudio BCR-ABL", "esplenomegalia gigante: pienso en LMC, mielofibrosis, leishmaniasis"),
        ("Esplenomegalia + hepatomegalia firme + estigmas de hepatopat&iacute;a", "Trombopenia y leucopenia", "Varices/circulaci&oacute;n colateral", "Hiperesplenismo por hipertensi&oacute;n portal", "el bazo grande secuestra c&eacute;lulas &rarr; citopenias"),
        ("Hepatomegalia + esplenomegalia + adenopat&iacute;as", "S&iacute;ndrome B", "Anemia asociada", "S&iacute;ndrome linfoproliferativo &rarr; estudio de extensi&oacute;n", "organomegalias + adenopat&iacute;as = sospecha de linfoma/leucemia"),
    ]),
    ("SIGNOS DE TROMBOSIS (EDEMA UNILATERAL)", [
        ("Edema y aumento de per&iacute;metro en una sola pierna", "Dolor a la palpaci&oacute;n de pantorrilla", "Eritema y calor local", "TVP &rarr; aplico escala de Wells y pido eco-Doppler", "edema unilateral + signos locales = sospecho TVP; mido per&iacute;metros"),
        ("Empastamiento de pantorrilla", "Cord&oacute;n venoso palpable", "Dilataci&oacute;n de venas superficiales colaterales", "TVP confirmada cl&iacute;nicamente &rarr; anticoagulaci&oacute;n", "Wells suma edema, dolor, inmovilizaci&oacute;n, c&aacute;ncer y antecedentes"),
        ("Disnea s&uacute;bita + dolor pleur&iacute;tico", "Taquicardia e hipoxemia", "TVP en la pierna", "<b>TEP</b> &rarr; URGENCIA: angio-TC pulmonar", "toda TVP puede embolizar; busco s&iacute;ntomas respiratorios"),
        ("Edema bilateral de ambas piernas con f&oacute;vea", "Sin dolor localizado ni eritema", "Asociado a cardiopat&iacute;a/hepatopat&iacute;a", "Edema sist&eacute;mico (no trombo) &rarr; descarta TVP", "el edema bilateral simetrico apunta a causa sist&eacute;mica, no trombo&iacute;tica"),
    ]),
    ("EXPLORACI&Oacute;N DE SANGRADO MUCOSO", [
        ("Sangrado de enc&iacute;as al cepillado", "Epistaxis de repetici&oacute;n", "Equimosis ante m&iacute;nimos traumatismos", "Sangrado de patr&oacute;n plaquetario &rarr; pido recuento y funci&oacute;n plaquetar", "mucoso + petequial = plaquetas; profundo + hematomas = coagulaci&oacute;n"),
        ("Hemartros y hematomas musculares profundos", "Antecedente familiar varon&iacute;l", "Sangrado tard&iacute;o tras heridas", "Hemofilia &rarr; mido TTPa y factores VIII/IX", "v&iacute;a intr&iacute;nseca (TTPa) alargada con TP normal sugiere hemofilia"),
        ("Sangrado difuso por puntos de venopunci&oacute;n y heridas", "Paciente s&eacute;ptico o cr&iacute;tico", "TP y TTPa alargados con plaquetas bajas", "<b>CID</b> &rarr; URGENCIA: D-d&iacute;mero, fibrin&oacute;geno y tratar la causa", "sangrado por m&uacute;ltiples sitios + consumo = coagulaci&oacute;n intravascular diseminada"),
        ("Menorragia abundante y prolongada", "Epistaxis frecuente desde la infancia", "Antecedente familiar de sangrado", "Enfermedad de von Willebrand &rarr; estudio de factor vW", "sangrado mucoso cr&oacute;nico hereditario sin trombopenia orienta a vW"),
    ]),
]
