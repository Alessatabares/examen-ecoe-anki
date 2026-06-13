# -*- coding: utf-8 -*-

NAME = "Higado / Biliar / Pancreas"

EJES = [
    ("Ictericia", [
        ("Ictericia + coluria + acolia + prurito + GGT/FA muy altas", "Ictericia obstructiva (colestasis)"),
        ("Ictericia + dolor c&oacute;lico HCD + Murphy + fiebre", "<b>Colecistitis / coledocolitiasis</b>"),
        ("Ictericia + fiebre con escalofr&iacute;os + dolor HCD (tr&iacute;ada de Charcot)", "<b>Colangitis aguda</b>"),
        ("Ictericia indolora + ves&iacute;cula palpable no dolorosa (Courvoisier) + p&eacute;rdida de peso", "<b>C&aacute;ncer de cabeza de p&aacute;ncreas</b>"),
        ("Ictericia + AST/ALT &gt; 1000 + astenia + transaminasas en miles", "Hepatitis viral aguda"),
        ("Ictericia + AST/ALT &gt; 2 con AST &lt; 300 + GGT alta + h&aacute;bito enol&iacute;co", "Hepatitis alcoh&oacute;lica"),
        ("Ictericia + flapping + ascitis + INR alto en hep&aacute;tata cr&oacute;nico", "<b>Insuficiencia hep&aacute;tica / cirrosis descompensada</b>"),
    ]),
    ("Dolor en hipocondrio derecho / epigastrio", [
        ("Dolor c&oacute;lico HCD tras comida grasa + ecograf&iacute;a con c&aacute;lculos, sin fiebre", "C&oacute;lico biliar (colelitiasis)"),
        ("Dolor HCD continuo + Murphy positivo + fiebre + leucocitosis", "<b>Colecistitis aguda</b>"),
        ("Dolor epig&aacute;strico en cintur&oacute;n irradiado a espalda + lipasa &gt; 3x + v&oacute;mitos", "<b>Pancreatitis aguda</b>"),
        ("Dolor epig&aacute;strico sordo + p&eacute;rdida de peso + esteatorrea + DM de novo", "C&aacute;ncer de p&aacute;ncreas"),
        ("Dolor HCD sordo + hepatomegalia dolorosa + estigmas de hepatopat&iacute;a", "Hepatitis / hepatomegalia congestiva"),
        ("Dolor epig&aacute;strico cr&oacute;nico + esteatorrea + calcificaciones pancre&aacute;ticas", "Pancreatitis cr&oacute;nica"),
    ]),
    ("Ascitis / distensi&oacute;n abdominal", [
        ("Ascitis + circulaci&oacute;n colateral + esplenomegalia + varices esof&aacute;gicas", "Hipertensi&oacute;n portal (cirrosis)"),
        ("Ascitis + GASA &ge; 1.1 g/dL + albuminemia baja", "Ascitis por cirrosis (transudado portal)"),
        ("Ascitis + fiebre + dolor abdominal difuso + PMN &gt; 250/mm3 en l&iacute;quido", "<b>Peritonitis bacteriana espont&aacute;nea</b>"),
        ("Distensi&oacute;n + AST/ALT &lt; 1 + obesidad + DM2 + dislipemia", "MASLD / MASH (esteatosis metab&oacute;lica)"),
        ("Ascitis + oliguria + creatinina al alza sin otra causa renal", "<b>S&iacute;ndrome hepatorrenal</b>"),
        ("Ascitis + ves&iacute;cula y v&iacute;a biliar normales + n&oacute;dulos hep&aacute;ticos", "Cirrosis / hepatocarcinoma"),
    ]),
    ("Hemorragia digestiva / anemia", [
        ("Hematemesis en chorro + melenas + hepatopat&iacute;a conocida", "<b>Hemorragia por varices esof&aacute;gicas</b>"),
        ("Melenas + hipotensi&oacute;n + estigmas de cirrosis + esplenomegalia", "<b>Hipertensi&oacute;n portal con sangrado</b>"),
        ("Anemia + trombopenia + leucopenia (hiperesplenismo) en cir&oacute;tico", "Hiperesplenismo por hipertensi&oacute;n portal"),
        ("Hematemesis + dolor epig&aacute;strico + AINE / alcohol, sin hepatopat&iacute;a", "&Uacute;lcera / gastritis (diagn&oacute;stico diferencial)"),
        ("Sangrado + INR prolongado + bilirrubina alta + flapping", "<b>Coagulopat&iacute;a por insuficiencia hep&aacute;tica</b>"),
    ]),
    ("Alteraci&oacute;n del estado mental / metab&oacute;lica", [
        ("Confusi&oacute;n + asterixis (flapping) + fetor hep&aacute;tico + amonio alto", "<b>Encefalopat&iacute;a hep&aacute;tica</b>"),
        ("Somnolencia + estre&ntilde;imiento o sangrado digestivo como desencadenante en cir&oacute;tico", "<b>Encefalopat&iacute;a hep&aacute;tica precipitada</b>"),
        ("Sudoraci&oacute;n + temblor + confusi&oacute;n que cede con glucosa (tr&iacute;ada de Whipple)", "<b>Hipoglucemia / insulinoma</b>"),
        ("Poliuria + polidipsia + p&eacute;rdida de peso + glucemia &gt; 200 + cetosis", "<b>Diabetes mellitus descompensada</b>"),
        ("Ictericia + encefalopat&iacute;a + INR &gt; 1.5 sin hepatopat&iacute;a previa (&lt; 26 sem)", "<b>Insuficiencia hep&aacute;tica aguda (fallo fulminante)</b>"),
    ]),
]

ESTACIONES = [
    ("INSPECCION", [
        ("Coloraci&oacute;n amarilla de escleras", "Coloraci&oacute;n amarilla de piel", "Lechos ungueales/frenillo ict&eacute;ricos", "Ictericia", "explorar con luz natural; descartar carotenemia (escleras respetadas)"),
        ("Abdomen distendido en batracio", "Ombligo evertido", "Flancos abombados", "Ascitis", "confirmar con matidez cambiante; GASA &ge; 1.1 sugiere origen portal"),
        ("Ara&ntilde;as vasculares en t&oacute;rax", "Circulaci&oacute;n colateral abdominal (cabeza de medusa)", "Ginecomastia", "Estigmas de hepatopat&iacute;a cr&oacute;nica", "signos de hiperestrogenismo e hipertensi&oacute;n portal"),
        ("Equimosis y petequias", "Sangrado de mucosas", "Hematomas espont&aacute;neos", "Coagulopat&iacute;a", "<b>insuficiencia hep&aacute;tica: corregir con vitamina K / plasma</b>"),
    ]),
    ("PALPACION ABDOMINAL", [
        ("Borde hep&aacute;tico &gt; 2 cm bajo reborde costal", "Superficie nodular y dura", "Hepatomegalia dolorosa", "Hepatomegalia", "dura/nodular sugiere cirrosis o tumor; dolorosa sugiere congesti&oacute;n/hepatitis"),
        ("Dolor en HCD al inspirar con palpaci&oacute;n subcostal", "Detenci&oacute;n brusca de la inspiraci&oacute;n", "Defensa local", "Signo de Murphy positivo", "<b>colecistitis aguda: ecograf&iacute;a + antibi&oacute;tico + colecistectom&iacute;a</b>"),
        ("Ves&iacute;cula palpable lisa e indolora", "Sin defensa", "Asociada a ictericia", "Signo de Courvoisier", "<b>obstrucci&oacute;n maligna distal (c&aacute;ncer de p&aacute;ncreas)</b>"),
        ("Polo de bazo palpable bajo reborde costal izquierdo", "Crece hacia FID en inspiraci&oacute;n", "Asociado a citopenias", "Esplenomegalia", "hiperesplenismo por hipertensi&oacute;n portal"),
        ("Defensa epig&aacute;strica + dolor en cintur&oacute;n", "Equimosis periumbilical (Cullen)", "Equimosis en flanco (Grey-Turner)", "Pancreatitis grave", "<b>pancreatitis necrohemorr&aacute;gica: ingreso/UCI</b>"),
    ]),
    ("PERCUSION", [
        ("Matidez en flancos en dec&uacute;bito supino", "Matidez que se desplaza al girar al paciente", "Timpanismo central", "Matidez cambiante", "confirma ascitis libre &gt; 1.5 L"),
        ("Onda transmitida al percutir un flanco", "Se palpa en el flanco contralateral", "Bloqueo con mano en l&iacute;nea media", "Oleada/signo de la ola", "ascitis a tensi&oacute;n; valorar paracentesis evacuadora"),
        ("Matidez hep&aacute;tica disminuida o ausente", "Timpanismo sobre &aacute;rea hep&aacute;tica", "Dolor a la percusi&oacute;n", "P&eacute;rdida de matidez hep&aacute;tica", "<b>neumoperitoneo: sospechar perforaci&oacute;n de v&iacute;scera hueca</b>"),
        ("Aumento del &aacute;rea de matidez hep&aacute;tica (&gt; 12 cm LMC)", "Borde inferior descendido", "Sin desplazamiento", "Hepatomegalia por percusi&oacute;n", "estimar tama&ntilde;o hep&aacute;tico en l&iacute;nea medioclavicular"),
    ]),
    ("SIGNOS NEUROLOGICOS Y CUTANEOS", [
        ("Temblor aleteante al extender las mu&ntilde;ecas", "Lapsos de tono postural", "Bilateral y arr&iacute;tmico", "Asterixis (flapping)", "<b>encefalopat&iacute;a hep&aacute;tica: lactulosa + tratar precipitante</b>"),
        ("Enrojecimiento de eminencias tenar e hipotenar", "Respeta zona central", "Indoloro", "Eritema palmar", "estigma de hepatopat&iacute;a cr&oacute;nica / hiperestrogenismo"),
        ("Aliento dulz&oacute;n / a tierra h&uacute;meda", "Asociado a desorientaci&oacute;n", "En hepat&oacute;pata", "Fetor hep&aacute;tico", "marcador de insuficiencia hepatocelular grave"),
        ("Contractura indolora de aponeurosis palmar", "Dedos en flexi&oacute;n fija (4&ordm;-5&ordm;)", "Asociada a enolismo", "Contractura de Dupuytren", "asociada a hepatopat&iacute;a alcoh&oacute;lica cr&oacute;nica"),
    ]),
]
