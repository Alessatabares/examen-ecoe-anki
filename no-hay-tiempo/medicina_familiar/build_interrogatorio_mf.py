"""No hay tiempo / Medicina Familiar — PILAR INTERROGATORIO (tronco + llaves).

Tronco contextual por motivo de consulta + llave que fija el dx (1er contacto).
Guia: GPC MX, GINA, GOLD, ADA, AHA/ACC, ESC, IDSA, USPSTF, CENETEC.
"""
import os
import genanki

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "output")
os.makedirs(OUTPUT_DIR, exist_ok=True)

MODEL_QA_ID = 1990009902
DECK_ID_T, DECK_ID_C, DECK_ID_M = 1990009011, 1990009012, 1990009013
DECK_NAME_T = "No hay tiempo::Medicina Familiar::Interrogatorio::1 - Troncos (ejes)"
DECK_NAME_C = "No hay tiempo::Medicina Familiar::Interrogatorio::2 - Llaves comunes (core)"
DECK_NAME_M = "No hay tiempo::Medicina Familiar::Interrogatorio::3 - Llaves menos comunes"

CSS_BASE = """
.card { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  font-size: 19px; text-align: left; color: #1a1a1a; background-color: #fafafa;
  padding: 20px; line-height: 1.55; }
.caso { font-size: 21px; font-weight: 700; color: #1e3a8a; }
#extra { margin-top: 16px; border: none; border-top: 1px solid #d4d4d4; padding-top: 12px; }
.bloque { display: block; margin: 12px 0; padding: 10px 14px; border-radius: 8px; }
.lab { display: block; font-size: 13px; font-weight: 700; letter-spacing: .5px;
  text-transform: uppercase; margin-bottom: 4px; }
.contexto { background: #eef2ff; border-left: 4px solid #1e3a8a; }
.ramifica { background: #f5f3ff; border-left: 4px solid #6d28d9; }
.llave { background: #eef2ff; border-left: 4px solid #1e3a8a; }
.patron { background: #f5f3ff; border-left: 4px solid #6d28d9; }
.dx { background: #ecfdf5; border-left: 4px solid #047857; }
.contexto .lab { color: #1e3a8a; } .ramifica .lab { color: #6d28d9; }
.llave .lab { color: #1e3a8a; } .patron .lab { color: #6d28d9; } .dx .lab { color: #047857; }
.dx b { color: #065f46; }
b { color: #111; }
"""
model_qa = genanki.Model(MODEL_QA_ID, "NHT MF Interrogatorio QA",
    fields=[{"name": "Front"}, {"name": "Back"}],
    templates=[{"name": "QA", "qfmt": "{{Front}}", "afmt": '{{Front}}<hr id="extra">{{Back}}'}],
    css=CSS_BASE)

deck_t = genanki.Deck(DECK_ID_T, DECK_NAME_T)
deck_c = genanki.Deck(DECK_ID_C, DECK_NAME_C)
deck_m = genanki.Deck(DECK_ID_M, DECK_NAME_M)
BASE_TAGS = ["medicina_familiar", "ecoe", "no_hay_tiempo", "interrogatorio"]


def add(deck, front, back, tags):
    deck.add_note(genanki.Note(model=model_qa, fields=[front, back], tags=BASE_TAGS + tags))

def caso(t): return f'<span class="caso">{t}</span>'

def tronco(ctx, ram):
    return (f'<span class="bloque contexto"><span class="lab">Pregunto siempre (contexto)</span>{ctx}</span>'
            f'<span class="bloque ramifica"><span class="lab">Esto me ramifica (sintoma guia -&gt; dx)</span>{ram}</span>')

def llave(p, pat, dx):
    return (f'<span class="bloque llave"><span class="lab">Pregunta-llave</span>{p}</span>'
            f'<span class="bloque patron"><span class="lab">Patron que confirma</span>{pat}</span>'
            f'<span class="bloque dx"><span class="lab">Diagnostico</span><b>{dx}</b></span>')


# ===================== TRONCOS (8) =====================
T = ["tronco"]
add(deck_t, caso("TRONCO — Tos / sintomas respiratorios"),
    tronco("<b>Tiempo</b>, fiebre, esputo (color/cantidad), disnea, dolor pleuritico, sibilancias, "
           "<b>tabaquismo</b>, contactos/epidemiologia, vacunas, comorbilidad (asma/EPOC/IC).",
           "<b>Fiebre + esputo + foco/crepitos</b> &rarr; NAC. <b>Tos seca + cuadro viral</b> &rarr; IVAS/bronquitis. "
           "<b>Sibilancias episodicas reversibles</b> &rarr; asma. <b>Disnea + tabaco cronico</b> &rarr; EPOC. "
           "<b>Subita + pleuritica + factores</b> &rarr; TEP/neumotorax."),
    T + ["respiratorio"])

add(deck_t, caso("TRONCO — Dolor / sintomas ORL (oido, nariz, garganta)"),
    tronco("<b>Localizacion</b> (oido/nariz/garganta), tiempo, fiebre, otorrea/rinorrea, dolor al tragar/al "
           "traccionar el pabellon, voz, contexto viral/alergico, recurrencia.",
           "<b>Otalgia + fiebre (timpano abombado)</b> &rarr; OMA. <b>Dolor al traccionar pabellon</b> &rarr; otitis "
           "externa. <b>Odinofagia + Centor alto</b> &rarr; faringitis estrep. <b>Congestion + dolor facial &gt;10 "
           "dias</b> &rarr; sinusitis. <b>Estornudos + prurito + moco claro</b> &rarr; rinitis alergica."),
    T + ["orl"])

add(deck_t, caso("TRONCO — Dolor toracico"),
    tronco("<b>Caracter</b> (opresivo/pleuritico/desgarrante), irradiacion, esfuerzo/reposo, duracion, disnea, "
           "<b>vegetativo</b>, factores de riesgo CV, inmovilizacion/cirugia reciente.",
           "<b>Opresivo con esfuerzo + vegetativo</b> &rarr; SCA. <b>Pleuritico + disnea + factores</b> &rarr; TEP. "
           "<b>Desgarrante a espalda + asimetria de pulsos</b> &rarr; diseccion. <b>Pleuritico que mejora inclinado "
           "adelante</b> &rarr; pericarditis. <b>Reproducible a la palpacion</b> &rarr; costocondritis (exclusion)."),
    T + ["dolor_toracico"])

add(deck_t, caso("TRONCO — Dolor abdominal"),
    tronco("<b>Inicio</b> (subito/gradual), <b>localizacion y migracion</b>, caracter, relacion con comida, "
           "nausea/vomito, transito, fiebre, <b>FUM/embarazo</b>, cirugias previas, AINE/alcohol.",
           "<b>Migra a FID</b> &rarr; apendicitis. <b>HD + Murphy tras grasas</b> &rarr; colecistitis. <b>En barra a "
           "espalda</b> &rarr; pancreatitis. <b>FII + cambio de habito</b> &rarr; diverticulitis. <b>Colico + "
           "distension + no canaliza</b> &rarr; obstruccion. <b>Difuso + diarrea/vomito</b> &rarr; gastroenteritis."),
    T + ["abdominal"])

add(deck_t, caso("TRONCO — Cefalea"),
    tronco("<b>Tiempo y forma de inicio</b>, caracter, localizacion, intensidad, sintomas asociados "
           "(nausea, foto/fonofobia, aura, fiebre), <b>banderas rojas (SNNOOP)</b>, patron previo, analgesicos.",
           "<b>Pulsatil + nausea + foto/fonofobia</b> &rarr; migrana. <b>Opresiva 'en banda' sin nausea</b> &rarr; "
           "tensional. <b>En trueno/maxima en segundos</b> &rarr; HSA. <b>Fiebre + rigidez de nuca</b> &rarr; "
           "meningitis. <b>&gt;50 a de novo + claudicacion mandibular</b> &rarr; arteritis."),
    T + ["cefalea"])

add(deck_t, caso("TRONCO — Lumbalgia / dolor de espalda"),
    tronco("<b>Tiempo</b>, mecanico vs inflamatorio, irradiacion a pierna, <b>deficit (fuerza, sensibilidad, "
           "esfinteres)</b>, trauma, <b>banderas rojas</b> (fiebre, perdida de peso, cancer, edad, nocturno), "
           "ocupacion.",
           "<b>Mecanico sin banderas</b> &rarr; lumbalgia inespecifica. <b>Irradia bajo la rodilla + Lasegue</b> "
           "&rarr; ciatica. <b>Retencion + anestesia en silla + deficit bilateral</b> &rarr; cauda equina. "
           "<b>Fiebre/perdida de peso/cancer/nocturno</b> &rarr; secundaria (infeccion/tumor)."),
    T + ["lumbalgia"])

add(deck_t, caso("TRONCO — Sintomas urinarios"),
    tronco("<b>Disuria/polaquiuria/urgencia</b>, fiebre, dolor lumbar, hematuria, <b>chorro/vaciado (LUTS)</b>, "
           "<b>embarazo</b>, sexo y edad, sonda/instrumentacion, factores de complicacion (DM, litiasis).",
           "<b>Disuria sin fiebre (mujer)</b> &rarr; cistitis. <b>+ fiebre + punopercusion</b> &rarr; pielonefritis. "
           "<b>Colico lumbar irradiado a ingle + hematuria</b> &rarr; litiasis. <b>LUTS + prostatismo (varon "
           "mayor)</b> &rarr; HPB. <b>Embarazada con bacteriuria</b> &rarr; tratar siempre."),
    T + ["urinario"])

add(deck_t, caso("TRONCO — Consulta del paciente cronico / control y prevencion"),
    tronco("<b>Apego</b> al tratamiento, control de cifras (TA/glucosa/lipidos), sintomas de dano de organo, "
           "habitos (tabaco/alcohol/dieta/actividad), <b>tamizajes y vacunas al dia</b>, animo, red de apoyo.",
           "<b>Cifras fuera de meta</b> &rarr; ajustar + reforzar adherencia. <b>Sintoma nuevo</b> &rarr; descartar "
           "complicacion. <b>Brecha en prevencion</b> &rarr; ofrecer tamizaje/vacuna/consejo (tabaco, VIH)."),
    T + ["cronico_prevencion"])


# ===================== LLAVES CORE (18) =====================
C = ["core"]
add(deck_c, caso("Fiebre con tos productiva y dolor pleuritico"),
    llave("&iquest;<b>Fiebre + tos con esputo + dolor pleuritico</b>? &iquest;disnea? &iquest;confusion/edad "
          "(CURB-65)?",
          "Fiebre + foco respiratorio + crepitos/consolidacion; infiltrado en Rx.",
          "Neumonia (NAC)"),
    C + ["nac"])

add(deck_c, caso("Disnea con sibilancias episodicas, peor de noche, en joven atopico"),
    llave("&iquest;Episodios <b>reversibles</b> de disnea/sibilancias/tos, peor de noche o con gatillos? "
          "&iquest;atopia/rinitis?",
          "Sibilancias episodicas reversibles + atopia + desencadenantes; mejora con broncodilatador.",
          "Asma"),
    C + ["asma"])

add(deck_c, caso("Disnea y tos cronicas con esputo en fumador"),
    llave("&iquest;<b>Tabaquismo</b> + disnea de esfuerzo progresiva + tos cronica? &iquest;mas esputo/purulencia "
          "(exacerbacion)?",
          "Disnea + sibilancias/roncus en fumador; limitacion cronica al flujo (espirometria).",
          "EPOC"),
    C + ["epoc"])

add(deck_c, caso("Cuadro catarral con rinorrea y odinofagia leve, sin fiebre alta"),
    llave("&iquest;<b>Rinorrea, congestion, odinofagia leve, malestar</b>, pocos dias, sin disnea? &iquest;contexto "
          "epidemico?",
          "Cuadro viral autolimitado de vias altas, sin foco bacteriano.",
          "IVAS / resfriado comun"),
    C + ["ivas"])

add(deck_c, caso("Odinofagia intensa con fiebre, sin tos, con exudado y adenopatias"),
    llave("&iquest;<b>Fiebre + exudado amigdalino + adenopatias + AUSENCIA de tos</b> (Centor)? &iquest;edad?",
          "Centor/McIsaac alto; faringoamigdalitis con datos bacterianos (estreptococo).",
          "Faringitis estreptococica"),
    C + ["faringitis"])

add(deck_c, caso("Otalgia con fiebre y timpano abombado"),
    llave("&iquest;<b>Otalgia + fiebre</b> tras cuadro catarral? &iquest;hipoacusia? &iquest;otorrea?",
          "Timpano abombado, hiperemico, opaco, con derrame; dolor que NO aumenta al traccionar el pabellon.",
          "Otitis media aguda"),
    C + ["oma"])

add(deck_c, caso("Congestion y dolor facial que no mejora tras 10 dias o empeora"),
    llave("&iquest;<b>Congestion + dolor/presion facial + rinorrea purulenta &gt;10 dias</b> o empeora tras "
          "mejorar? &iquest;fiebre?",
          "Sintomas nasosinusales persistentes/que empeoran (doble empeoramiento) = sinusitis bacteriana.",
          "Sinusitis aguda"),
    C + ["sinusitis"])

add(deck_c, caso("Estornudos, prurito nasal y moco claro recurrentes"),
    llave("&iquest;<b>Estornudos en salva + prurito nasal/ocular + rinorrea clara</b>, estacional o con gatillos? "
          "&iquest;antecedente atopico?",
          "Sintomas recurrentes/estacionales con prurito, sin fiebre; mucosa palida y edematosa.",
          "Rinitis alergica"),
    C + ["rinitis"])

add(deck_c, caso("Dolor opresivo retroesternal con esfuerzo, irradiado, con sudor frio"),
    llave("&iquest;Dolor <b>opresivo</b> con el esfuerzo, irradia a brazo/mandibula, con <b>diaforesis/nausea</b>? "
          "&iquest;factores de riesgo CV?",
          "Dolor anginoso tipico + vegetativo + factores; ECG y troponina lo definen (urgencia).",
          "Sindrome coronario agudo"),
    C + ["sca"])

add(deck_c, caso("Disnea de esfuerzo con ortopnea y edema de piernas"),
    llave("&iquest;<b>Se ahoga al acostarse (ortopnea)</b> o despierta ahogado (DPN)? &iquest;piernas hinchadas, "
          "sube de peso?",
          "Ortopnea + DPN + ingurgitacion yugular + edema + crepitos; descompensacion con un gatillo.",
          "Insuficiencia cardiaca"),
    C + ["icc"])

add(deck_c, caso("Diarrea y vomito agudos con dolor abdominal difuso"),
    llave("&iquest;<b>Diarrea + vomito + dolor difuso</b> de inicio agudo? &iquest;alimentos/contactos? "
          "&iquest;sangre en heces, fiebre alta, datos de deshidratacion?",
          "Cuadro digestivo agudo autolimitado; valorar deshidratacion y datos de alarma.",
          "Gastroenteritis aguda"),
    C + ["gastroenteritis"])

add(deck_c, caso("Cefalea pulsatil unilateral con nausea y molestia a la luz"),
    llave("&iquest;Dolor <b>pulsatil</b>, empeora con actividad, con <b>nausea y foto/fonofobia</b>? &iquest;aura? "
          "&iquest;episodios previos similares?",
          "Cefalea recurrente pulsatil + sintomas asociados, sin banderas rojas; patron conocido.",
          "Migrana"),
    C + ["migrana"])

add(deck_c, caso("Cefalea opresiva 'en banda' sin nausea ni foto/fonofobia"),
    llave("&iquest;Dolor <b>opresivo bilateral 'en banda'</b>, leve-moderado, sin nausea ni empeorar con la "
          "actividad? &iquest;estres/postura/sueno?",
          "Cefalea bilateral no pulsatil sin sintomas migranosos ni banderas; relacion con tension.",
          "Cefalea tensional"),
    C + ["cefalea_tensional"])

add(deck_c, caso("Vertigo de segundos desencadenado al girar la cabeza en la cama"),
    llave("&iquest;<b>Giros breves (segundos)</b> al mover/girar la cabeza o acostarse? &iquest;sin sintomas "
          "neurologicos, sin perdida auditiva?",
          "Vertigo posicional breve, fatigable, con Dix-Hallpike positivo; sin focalidad.",
          "Vertigo posicional benigno (VPPB)"),
    C + ["vppb"])

add(deck_c, caso("Dolor lumbar mecanico tras esfuerzo, sin deficit"),
    llave("&iquest;Dolor de espalda <b>mecanico</b> (mejora en reposo, empeora con movimiento) tras esfuerzo? "
          "&iquest;SIN banderas (deficit, fiebre, perdida de peso, esfinteres)?",
          "Dolor lumbar mecanico, exploracion neurologica normal, sin banderas rojas.",
          "Lumbalgia inespecifica"),
    C + ["lumbalgia"])

add(deck_c, caso("Disuria y polaquiuria sin fiebre en mujer"),
    llave("&iquest;<b>Ardor al orinar + orinar a cada rato + urgencia</b>, SIN fiebre ni dolor lumbar? &iquest;sin "
          "factores de complicacion?",
          "Sintomas urinarios bajos sin fiebre ni afectacion sistemica en mujer no embarazada.",
          "Cistitis no complicada"),
    C + ["cistitis"])

add(deck_c, caso("Cansancio, intolerancia al frio, aumento de peso y estrenimiento"),
    llave("&iquest;<b>Fatiga, frio, piel seca, estrenimiento, aumento de peso, bradipsiquia</b>? &iquest;menstruacion "
          "abundante? &iquest;antecedente tiroideo?",
          "Sintomas de hipofuncion + bradicardia/piel seca; TSH alta con T4 baja confirma.",
          "Hipotiroidismo"),
    C + ["hipotiroidismo"])

add(deck_c, caso("Poliuria, polidipsia, perdida de peso y fatiga cronicas"),
    llave("&iquest;<b>Sed, orina frecuente, perdida de peso</b>, vision borrosa? &iquest;antecedente familiar, "
          "obesidad, sedentarismo?",
          "Hiperglucemia cronica con sintomas clasicos; HbA1c &ge;6.5% / glucosa elevada confirman.",
          "Diabetes mellitus tipo 2"),
    C + ["dm2"])

add(deck_c, caso("Astenia y palidez con dieta pobre o sangrado cronico"),
    llave("&iquest;Cansancio, palidez, disnea de esfuerzo? &iquest;<b>melena, menstruacion abundante, dieta</b>? "
          "&iquest;pica?",
          "Anemia (clasificar por VCM); microcitica con ferritina baja = ferropenica; buscar la fuente.",
          "Anemia (ferropenica)"),
    C + ["anemia"])


# ===================== LLAVES MENOS (20) =====================
M = ["menos_comun"]
pares = [
    ("Tos seca persistente tras un catarro, sin foco ni fiebre alta",
     "&iquest;<b>Tos que persiste 1-3 semanas tras cuadro viral</b>, sin disnea, fiebre alta ni foco? &iquest;no fumador?",
     "Tos postinfecciosa autolimitada; auscultacion limpia, sin consolidacion.", "Bronquitis aguda", "bronquitis"),
    ("Disnea con matidez y ausencia de ruidos en una base",
     "&iquest;Disnea + <b>matidez + abolicion del murmullo</b> en una base? &iquest;IC, neumonia, cancer, TB?",
     "Sindrome de derrame (matidez + ausencia de vibraciones y murmullo).", "Derrame pleural", "derrame_pleural"),
    ("Disnea y dolor toracico subitos en joven alto y delgado fumador",
     "&iquest;<b>Dolor pleuritico + disnea subitos</b>? &iquest;alto/delgado/fumador o trauma? &iquest;hipotension (a tension)?",
     "Hemitorax hiperresonante con murmullo abolido; subito.", "Neumotorax", "neumotorax"),
    ("Otalgia que aumenta al traccionar el pabellon, en nadador",
     "&iquest;Dolor que <b>aumenta al jalar el pabellon/tragus</b>? &iquest;agua/humedad, hisopos? &iquest;otorrea?",
     "Conducto inflamado/edematoso con otorrea; dolor a la traccion (vs OMA).", "Otitis externa", "otitis_externa"),
    ("Ronquera de pocos dias tras infeccion viral",
     "&iquest;<b>Disfonia/ronquera</b> tras cuadro viral, &lt;2 semanas, sin disnea ni estridor?",
     "Inflamacion laringea viral autolimitada.", "Laringitis aguda", "laringitis"),
    ("Bulto en el cuello que se mueve al tragar",
     "&iquest;<b>Nodulo en la tiroides</b> (se mueve al deglutir)? &iquest;crece rapido, duro, fijo, disfonia, "
     "radiacion previa, adenopatia?",
     "Nodulo tiroideo; TSH + USG estratifican; banderas guian BAAF.", "Nodulo tiroideo", "nodulo_tiroideo"),
    ("Dolor toracico pleuritico que mejora al inclinarse adelante",
     "&iquest;Dolor que <b>empeora acostado y al inspirar, mejora sentado inclinado adelante</b>? &iquest;viral reciente?",
     "Dolor posicional + frote pericardico; ECG con ST difuso y descenso del PR.", "Pericarditis", "pericarditis"),
    ("Sincope o angina de esfuerzo en anciano con soplo eyectivo",
     "&iquest;<b>Sincope/angina/disnea con el esfuerzo</b>? &iquest;soplo sistolico eyectivo que irradia a carotidas?",
     "Triada (angina/sincope/disnea) + soplo aortico + parvus et tardus.", "Estenosis aortica", "estenosis_aortica"),
    ("Pierna hinchada, dolorosa y caliente de forma unilateral",
     "&iquest;<b>Edema unilateral + dolor + calor</b> en pantorrilla? &iquest;inmovilidad, cirugia, cancer, ACO (Wells)?",
     "Edema/dolor unilateral con factores de riesgo; Doppler confirma.", "Trombosis venosa profunda", "tvp"),
    ("Perdida transitoria del conocimiento con recuperacion completa",
     "&iquest;<b>Prodromos</b> (calor/sudor/vision borrosa) y gatillo (calor/dolor/bipedestacion)? &iquest;o fue de "
     "ESFUERZO/en supino/con palpitaciones (rojo)?",
     "Vasovagal = prodromos + gatillo + recuperacion rapida; cardiogenico = banderas.", "Sincope", "sincope"),
    ("Dolor que migra del ombligo a la fosa iliaca derecha",
     "&iquest;El dolor <b>empezo en el ombligo y bajo a la derecha</b>? &iquest;anorexia, nausea, febricula?",
     "Migracion + dolor en McBurney + Blumberg + leucocitosis.", "Apendicitis", "apendicitis"),
    ("Dolor en hipocondrio derecho tras comida grasa con Murphy",
     "&iquest;Dolor en HD que <b>detiene la inspiracion al palpar (Murphy)</b>, tras grasas, con fiebre?",
     "Murphy + dolor HD + fiebre; USG con litos y pared engrosada.", "Colecistitis aguda", "colecistitis"),
    ("Dolor epigastrico en barra que irradia a la espalda",
     "&iquest;Dolor <b>en barra hacia la espalda</b> que mejora inclinado adelante? &iquest;alcohol o litiasis? &iquest;vomito?",
     "Dolor transfixiante + <b>lipasa &gt;3x</b>; causa biliar o alcoholica.", "Pancreatitis aguda", "pancreatitis"),
    ("Dolor en fosa iliaca izquierda con fiebre en adulto mayor",
     "&iquest;Dolor en <b>FII</b> + cambio del habito + fiebre? &iquest;episodios previos?",
     "Dolor FII + fiebre + leucocitosis; TAC con engrosamiento/diverticulos.", "Diverticulitis aguda", "diverticulitis"),
    ("Dolor colico, distension y no canaliza gases",
     "&iquest;<b>Vomito, distension y no expulsa gases ni heces</b>? &iquest;cirugias previas o hernias?",
     "Colico + distension + RHA metalicos/ausentes + niveles en Rx.", "Obstruccion intestinal", "obstruccion"),
    ("Deficit neurologico focal de inicio subito",
     "&iquest;<b>Debilidad/asimetria facial/alteracion del habla SUBITAS</b>? &iquest;hora de inicio exacta? "
     "&iquest;FA, HTA, factores?",
     "Focalidad neurologica subita (FAST); ventana de reperfusion (urgencia).", "EVC", "evc"),
    ("Cefalea brusca 'la peor de mi vida' o con fiebre y rigidez",
     "&iquest;<b>Inicio en trueno (segundos)</b>? &iquest;fiebre + rigidez de nuca? &iquest;&gt;50 a de novo, focal, "
     "papiledema, inmunodeprimido?",
     "Banderas rojas (SNNOOP) = cefalea secundaria peligrosa (HSA, meningitis, arteritis).", "Cefalea red flag", "cefalea_red_flag"),
    ("Lumbalgia con retencion urinaria y anestesia perineal",
     "&iquest;<b>No puede orinar/se le escapa, adormecimiento en la silla de montar, debilidad en ambas piernas</b>?",
     "Compresion de cauda equina: retencion + anestesia en silla + deficit bilateral.", "Cauda equina", "cauda_equina"),
    ("Dolor que baja por la pierna por debajo de la rodilla",
     "&iquest;Dolor que <b>irradia bajo la rodilla</b> con hormigueo? &iquest;Lasegue (elevacion de pierna recta) +? "
     "&iquest;deficit?",
     "Dolor radicular dermatomico + Lasegue; sin cauda equina.", "Ciatica / radiculopatia", "ciatica"),
    ("Sintomas urinarios de vaciado en varon mayor (chorro debil)",
     "&iquest;<b>Chorro debil, goteo, urgencia, nicturia, sensacion de no vaciar (LUTS)</b>? &iquest;edad, tacto "
     "prostatico?",
     "LUTS obstructivos + prostata aumentada lisa (HPB) vs nodulo duro (cancer).", "Hiperplasia prostatica (HPB)", "hpb"),
]
for titulo, p, pat, dx, tag in pares:
    add(deck_m, caso(titulo), llave(p, pat, dx), M + [tag])


def build():
    for d, f in [(deck_t, "Interrogatorio_01_Troncos.apkg"), (deck_c, "Interrogatorio_02_Llaves_core.apkg"),
                 (deck_m, "Interrogatorio_03_Llaves_menos.apkg")]:
        genanki.Package(d).write_to_file(os.path.join(OUTPUT_DIR, f))
        print(f"  -> {f} ({len(d.notes)} notas)")
    genanki.Package([deck_t, deck_c, deck_m]).write_to_file(
        os.path.join(OUTPUT_DIR, "No_Hay_Tiempo_MF_Interrogatorio_TODOS.apkg"))
    print(f"  -> TODOS ({sum(len(d.notes) for d in [deck_t, deck_c, deck_m])} notas)")


if __name__ == "__main__":
    build()
