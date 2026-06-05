"""No hay tiempo / Medicina Interna — PILAR INTERROGATORIO (tronco + llaves).

Tronco contextual por motivo de consulta + llave que fija el dx.
Guia: ESC, ADA, KDIGO, GOLD, GINA, AHA/ACC, EASL, GPC mexicanas.
"""
import os
import genanki

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "output")
os.makedirs(OUTPUT_DIR, exist_ok=True)

MODEL_QA_ID = 1990008002
DECK_ID_T, DECK_ID_C, DECK_ID_M = 1990007011, 1990007012, 1990007013
DECK_NAME_T = "No hay tiempo::Medicina Interna::Interrogatorio::1 - Troncos (ejes)"
DECK_NAME_C = "No hay tiempo::Medicina Interna::Interrogatorio::2 - Llaves comunes (core)"
DECK_NAME_M = "No hay tiempo::Medicina Interna::Interrogatorio::3 - Llaves menos comunes"

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
model_qa = genanki.Model(MODEL_QA_ID, "NHT MI Interrogatorio QA",
    fields=[{"name": "Front"}, {"name": "Back"}],
    templates=[{"name": "QA", "qfmt": "{{Front}}", "afmt": '{{Front}}<hr id="extra">{{Back}}'}],
    css=CSS_BASE)

deck_t = genanki.Deck(DECK_ID_T, DECK_NAME_T)
deck_c = genanki.Deck(DECK_ID_C, DECK_NAME_C)
deck_m = genanki.Deck(DECK_ID_M, DECK_NAME_M)
BASE_TAGS = ["medicina_interna", "ecoe", "no_hay_tiempo", "interrogatorio"]


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


# ===================== TRONCOS (7) =====================
T = ["tronco"]
add(deck_t, caso("TRONCO — Dolor toracico"),
    tronco("<b>Caracter</b> (opresivo, pleuritico, desgarrante), <b>irradiacion</b>, esfuerzo/reposo, duracion, "
           "disnea, sintomas vegetativos, factores de riesgo CV, antecedentes (HTA, DM, tabaco), "
           "inmovilizacion/cirugia reciente (TEP).",
           "<b>Opresivo con esfuerzo + vegetativo</b> &rarr; SCA. <b>Pleuritico + disnea + factores</b> &rarr; TEP. "
           "<b>Desgarrante a espalda + asimetria de pulsos</b> &rarr; diseccion. <b>Pleuritico que mejora sentado "
           "inclinado adelante</b> &rarr; pericarditis."),
    T + ["dolor_toracico"])

add(deck_t, caso("TRONCO — Disnea"),
    tronco("<b>Tiempo</b> (subita vs progresiva), <b>ortopnea/DPN</b>, edema, tos/esputo, fiebre, sibilancias, "
           "dolor pleuritico, factores (IC, EPOC, asma, inmovilizacion), <b>SatO2</b>.",
           "<b>Ortopnea + DPN + edema</b> &rarr; IC. <b>Sibilancias + tabaquismo</b> &rarr; EPOC/asma. "
           "<b>Subita + pleuritica + factores</b> &rarr; TEP. <b>Fiebre + tos productiva + foco</b> &rarr; NAC."),
    T + ["disnea"])

add(deck_t, caso("TRONCO — Alteracion del estado de alerta / confusion"),
    tronco("<b>Glucemia capilar SIEMPRE</b>, tiempo de instauracion, focalidad, fiebre, farmacos/toxicos/alcohol, "
           "hepatopatia, funcion renal, antecedentes (diabetes, tiroides, suprarrenal), Na conocido.",
           "<b>Hipoglucemia</b> (siempre primero). <b>Hepatopatia + asterixis</b> &rarr; encefalopatia hepatica. "
           "<b>Hiperglucemia + deshidratacion</b> &rarr; CAD/EHH. <b>Na muy bajo</b> &rarr; hiponatremia. "
           "<b>Focalidad</b> &rarr; EVC."),
    T + ["confusion"])

add(deck_t, caso("TRONCO — Edema / retencion de liquidos"),
    tronco("<b>Distribucion</b> (bilateral/generalizado vs unilateral), tiempo, disnea/ortopnea, orina espumosa, "
           "estigmas de hepatopatia, proteinuria, antecedentes cardiacos/renales/hepaticos, farmacos.",
           "<b>Edema + ortopnea/IY</b> &rarr; IC. <b>Edema + orina espumosa + proteinuria</b> &rarr; nefrotico. "
           "<b>Ascitis + estigmas hepaticos</b> &rarr; cirrosis. <b>Edema unilateral de pierna</b> &rarr; TVP."),
    T + ["edema"])

add(deck_t, caso("TRONCO — Sindrome febril / sospecha de infeccion"),
    tronco("<b>Foco</b> (respiratorio, urinario, abdominal, piel, cardiaco), tiempo, <b>hemodinamia y estado "
           "mental (qSOFA)</b>, inmunosupresion/diabetes, dispositivos/protesis, viajes, contacto, soplos.",
           "<b>Disuria + dolor lumbar/punopercusion</b> &rarr; pielonefritis. <b>Tos + foco pulmonar</b> &rarr; NAC. "
           "<b>Soplo nuevo + fiebre + factores</b> &rarr; endocarditis. <b>qSOFA &ge;2</b> &rarr; sepsis."),
    T + ["fiebre"])

add(deck_t, caso("TRONCO — Astenia / sindrome anemico / palidez"),
    tronco("<b>Tiempo</b>, sangrados (digestivo, menstrual), dieta, <b>melena/hematoquecia</b>, perdida de peso, "
           "sintomas de cada serie (disnea, palpitaciones), enfermedad cronica/inflamatoria, alcohol, farmacos.",
           "<b>Microcitica + sangrado/dieta</b> &rarr; ferropenica. <b>Normo con enfermedad cronica</b> &rarr; "
           "inflamatoria. <b>Macrocitica + dieta/alcohol/neuro</b> &rarr; B12/folato."),
    T + ["anemia"])

add(deck_t, caso("TRONCO — Disminucion del gasto urinario / sospecha de AKI"),
    tronco("<b>Volemia</b> (perdidas: vomito/diarrea, diureticos; aportes), <b>nefrotoxicos</b> (AINE, contraste, "
           "aminoglucosidos), <b>sintomas obstructivos</b> (chorro debil, globo, prostata), hematuria/edema/HTA, "
           "antecedentes renales.",
           "<b>Hipovolemia/perdidas</b> &rarr; prerrenal. <b>Isquemia/toxico</b> &rarr; NTA. "
           "<b>Globo/prostata/anuria fluctuante</b> &rarr; postrenal. <b>Hematuria + HTA + edema</b> &rarr; "
           "glomerular (nefritico)."),
    T + ["aki"])


# ===================== LLAVES CORE (18) =====================
C = ["core"]
add(deck_c, caso("Dolor opresivo retroesternal con el esfuerzo, irradiado al brazo, con sudor frio"),
    llave("&iquest;Dolor <b>opresivo</b> que aparece con el esfuerzo, irradia a brazo/mandibula, con <b>diaforesis/"
          "nausea</b>? &iquest;factores de riesgo CV?",
          "Dolor anginoso tipico + vegetativo + factores de riesgo; ECG y troponina lo definen.",
          "Sindrome coronario agudo"),
    C + ["sca"])

add(deck_c, caso("Disnea de esfuerzo progresiva con ortopnea y edema de piernas"),
    llave("&iquest;<b>Le falta el aire al acostarse (ortopnea)</b> o despierta ahogado de noche (DPN)? "
          "&iquest;piernas hinchadas, sube de peso?",
          "Ortopnea + DPN + ingurgitacion yugular + edema + crepitos; descompensacion con un gatillo.",
          "Insuficiencia cardiaca (descompensada)"),
    C + ["ic"])

add(deck_c, caso("Palpitaciones irregulares con pulso 'desordenado'"),
    llave("&iquest;Siente el corazon <b>irregular/desordenado</b>? &iquest;mareo, disnea, dolor toracico? "
          "&iquest;tiempo de evolucion (&gt;48 h)?",
          "Pulso irregularmente irregular; ECG sin onda P, R-R variable.",
          "Fibrilacion auricular"),
    C + ["fa"])

add(deck_c, caso("Cefalea intensa con cifras tensionales muy elevadas"),
    llave("&iquest;TA muy alta + <b>sintomas de dano de organo</b> (dolor toracico, disnea, deficit neurologico, "
          "vision borrosa)? &iquest;apego al tratamiento?",
          "TA severamente elevada; la presencia de dano agudo de organo separa emergencia de urgencia.",
          "Crisis hipertensiva"),
    C + ["crisis_htas"])

add(deck_c, caso("Disnea con sibilancias y tos en fumador con reagudizaciones"),
    llave("&iquest;<b>Tabaquismo</b>, disnea de esfuerzo cronica, <b>aumento de esputo/purulencia</b>? "
          "&iquest;sibilancias, uso de inhaladores?",
          "Disnea + sibilancias + tabaquismo con exacerbacion (mas disnea/esputo/purulencia).",
          "EPOC exacerbado"),
    C + ["epoc"])

add(deck_c, caso("Crisis de disnea con sibilancias en paciente joven atopico"),
    llave("&iquest;Episodios <b>reversibles</b> de disnea/sibilancias/tos, peor de noche o con gatillos (ejercicio, "
          "alergenos)? &iquest;atopia?",
          "Sibilancias episodicas reversibles + atopia + desencadenantes; mejora con broncodilatador.",
          "Asma (crisis)"),
    C + ["asma"])

add(deck_c, caso("Fiebre con tos productiva y dolor pleuritico"),
    llave("&iquest;<b>Fiebre + tos con esputo + dolor pleuritico</b>? &iquest;disnea, escalofrios? "
          "&iquest;confusion, edad, comorbilidad (CURB-65)?",
          "Fiebre + foco respiratorio + crepitos/consolidacion; infiltrado en Rx.",
          "Neumonia adquirida en la comunidad"),
    C + ["nac"])

add(deck_c, caso("Disnea subita y dolor pleuritico tras inmovilizacion o cirugia"),
    llave("&iquest;Disnea <b>subita</b> + dolor pleuritico + <b>factores</b> (cirugia, inmovilidad, cancer, "
          "anticonceptivos, TVP previa)? &iquest;pierna hinchada?",
          "Disnea/dolor pleuritico subitos + taquicardia + hipoxia con factores de riesgo (Wells).",
          "Tromboembolia pulmonar"),
    C + ["tep"])

add(deck_c, caso("Disuria, fiebre y dolor lumbar"),
    llave("&iquest;<b>Disuria/polaquiuria + fiebre + dolor lumbar</b>? &iquest;punopercusion renal positiva? "
          "&iquest;factores de complicacion (DM, embarazo, sonda, litiasis)?",
          "Sintomas urinarios bajos + fiebre + punopercusion positiva; piuria en EGO.",
          "Pielonefritis aguda"),
    C + ["pielonefritis"])

add(deck_c, caso("Poliuria, polidipsia, nausea y aliento afrutado en diabetico"),
    llave("&iquest;<b>Mucha sed y orina</b>, nausea/vomito, dolor abdominal, <b>respiracion profunda</b>? "
          "&iquest;omitio insulina o tiene una infeccion?",
          "Hiperglucemia + cetosis + acidosis (Kussmaul, aliento cetonico) con un desencadenante.",
          "Cetoacidosis diabetica"),
    C + ["cad"])

add(deck_c, caso("Ictericia, distension abdominal y confusion en bebedor"),
    llave("&iquest;<b>Estigmas de hepatopatia</b> (ascitis, ictericia, arañas), confusion/asterixis, sangrado? "
          "&iquest;alcohol? &iquest;que lo descompenso?",
          "Cirrosis conocida/estigmas + una descompensacion (ascitis, encefalopatia, sangrado, PBE).",
          "Cirrosis descompensada"),
    C + ["cirrosis"])

add(deck_c, caso("Fiebre con hipotension, taquicardia y confusion con un foco"),
    llave("&iquest;<b>qSOFA &ge;2</b> (TAS &le;100, FR &ge;22, alteracion mental) con un foco infeccioso? "
          "&iquest;inmunosupresion/dispositivos?",
          "Disfuncion organica por infeccion; lactato alto y/o hipotension que requiere vasopresor.",
          "Sepsis / choque septico"),
    C + ["sepsis"])

add(deck_c, caso("Disminucion del gasto urinario tras deshidratacion o hipotension"),
    llave("&iquest;<b>Perdidas</b> (vomito/diarrea, diureticos) o hipotension previa? &iquest;orina concentrada y "
          "escasa? &iquest;nefrotoxicos recientes?",
          "Oliguria + elevacion de creatinina con respuesta a volumen; orina concentrada, Na urinario bajo.",
          "AKI prerrenal"),
    C + ["aki_prerrenal"])

add(deck_c, caso("Confusion y letargia con sodio muy bajo"),
    llave("&iquest;<b>Nausea, cefalea, confusion o convulsiones</b> con Na bajo? &iquest;volemia? &iquest;diureticos, "
          "ICC, hepatopatia, SIADH (farmacos, pulmonar, SNC)?",
          "Sintomas neurologicos + hiponatremia; la volemia y la osmolaridad orientan la causa.",
          "Hiponatremia (sintomatica)"),
    C + ["hiponatremia"])

add(deck_c, caso("Articulacion roja, caliente e hipersensible de inicio nocturno (1er dedo del pie)"),
    llave("&iquest;<b>Inicio agudo, nocturno</b>, monoarticular (podagra), roja y muy dolorosa? "
          "&iquest;alcohol, carnes, diureticos, episodios previos?",
          "Monoartritis aguda muy inflamatoria; cristales de urato (negativos, en aguja) confirman.",
          "Gota (ataque agudo)"),
    C + ["gota"])

add(deck_c, caso("Astenia y palidez con dieta pobre o sangrado cronico"),
    llave("&iquest;Cansancio, palidez, disnea de esfuerzo? &iquest;<b>melena, menstruacion abundante, dieta</b>? "
          "&iquest;pica?",
          "Anemia microcitica hipocroma + ferritina baja; buscar la fuente de perdida.",
          "Anemia ferropenica"),
    C + ["ferropenica"])

add(deck_c, caso("Hipertension detectada en consulta, sin sintomas"),
    llave("&iquest;Cifras altas <b>repetidas</b>? &iquest;sintomas de dano de organo, antecedentes familiares, "
          "habitos (sal, alcohol, peso)? &iquest;datos de causa 2aria?",
          "TA elevada confirmada en varias tomas; descartar 'bata blanca' con AMPA/MAPA.",
          "Hipertension arterial"),
    C + ["htas"])

add(deck_c, caso("Poliuria, polidipsia, perdida de peso y fatiga cronicas"),
    llave("&iquest;<b>Sed, orina frecuente, perdida de peso</b>, vision borrosa? &iquest;antecedente familiar, "
          "obesidad, sedentarismo?",
          "Hiperglucemia cronica con sintomas clasicos; HbA1c &ge;6.5% / glucosa elevada confirman.",
          "Diabetes mellitus tipo 2"),
    C + ["diabetes"])


# ===================== LLAVES MENOS (20) =====================
M = ["menos_comun"]
pares = [
    ("Sincope o angina de esfuerzo en anciano con soplo sistolico eyectivo",
     "&iquest;<b>Sincope/angina/disnea con el esfuerzo</b>? &iquest;<b>soplo sistolico eyectivo</b> que irradia a carotidas?",
     "Triada (angina, sincope, disnea) + soplo aortico + pulso parvus et tardus.", "Estenosis aortica", "estenosis_aortica"),
    ("Edema agudo de pulmon y soplo holosistolico nuevo tras un infarto",
     "&iquest;Disnea brusca + <b>soplo holosistolico nuevo</b> en apex que irradia a axila tras IAM/endocarditis?",
     "Edema pulmonar + soplo de regurgitacion mitral aguda; deterioro hemodinamico.", "Insuficiencia mitral aguda", "insuf_mitral"),
    ("Dolor toracico pleuritico que mejora al inclinarse hacia adelante",
     "&iquest;Dolor que <b>empeora acostado y al inspirar, mejora sentado inclinado adelante</b>? &iquest;viral reciente?",
     "Dolor posicional + frote pericardico; ECG con elevacion del ST difusa y descenso del PR.", "Pericarditis aguda", "pericarditis"),
    ("Diabetico anciano muy deshidratado con glucemia altisima sin cetosis",
     "&iquest;<b>Deterioro neurologico</b> progresivo + deshidratacion intensa + glucemia muy alta <b>sin</b> aliento cetonico?",
     "Hiperglucemia extrema + hiperosmolaridad + minima cetosis; deterioro del estado de alerta.", "Estado hiperosmolar (EHH)", "ehh"),
    ("Fiebre, taquicardia extrema y agitacion en paciente hipertiroideo",
     "&iquest;<b>Fiebre alta + taquicardia/FA + agitacion/delirio</b> en hipertiroideo, tras un gatillo (infeccion, cirugia)?",
     "Tirotoxicosis + fiebre + disfuncion cardiaca/SNC; emergencia (Burch-Wartofsky).", "Tormenta tiroidea", "tormenta_tiroidea"),
    ("Hipotermia, bradicardia y estupor en paciente hipotiroideo",
     "&iquest;<b>Frio, lento, somnoliento</b>, bradicardico, hiponatremico? &iquest;abandono de levotiroxina, infeccion, frio?",
     "Hipotiroidismo extremo: hipotermia + bradicardia + hipoventilacion + alteracion del alerta.", "Coma mixedematoso", "coma_mixedematoso"),
    ("Hipotension que no responde a liquidos con hiperpigmentacion",
     "&iquest;Hipotension refractaria + <b>hiperpigmentacion</b>, fatiga, nausea, avidez por sal? &iquest;suspendio esteroide?",
     "Hipotension + hiponatremia + hiperkalemia + hipoglucemia; crisis adrenal.", "Crisis suprarrenal", "crisis_suprarrenal"),
    ("Debilidad muscular y palpitaciones con cambios en el ECG (T picudas)",
     "&iquest;Debilidad, parestesias, palpitaciones? &iquest;ERC, IECA/ARA-II/ARM, AINE, lisis tumoral/rabdomiolisis?",
     "Hiperkalemia: ondas T picudas, ensanchamiento del QRS; riesgo de arritmia letal.", "Hiperkalemia", "hiperkalemia"),
    ("Calambres y debilidad con uso de diureticos o vomito/diarrea",
     "&iquest;Calambres, debilidad, palpitaciones? &iquest;<b>diureticos, vomito/diarrea</b>, hiperaldosteronismo?",
     "Hipokalemia: aplanamiento de T, onda U; corregir tambien el magnesio.", "Hipokalemia", "hipokalemia"),
    ("Edema generalizado con orina muy espumosa",
     "&iquest;<b>Edema importante (incluso periorbitario) + orina espumosa</b>? &iquest;diabetes, infecciones a repeticion?",
     "Proteinuria masiva (&gt;3.5 g) + hipoalbuminemia + edema + hiperlipidemia.", "Sindrome nefrotico", "nefrotico"),
    ("Orina oscura (color coca-cola), hipertension y edema",
     "&iquest;<b>Orina como refresco de cola/hematuria</b> + HTA + edema + poca orina? &iquest;faringitis/piel reciente?",
     "Hematuria con cilindros hematicos + HTA + oliguria + proteinuria leve-moderada.", "Sindrome nefritico", "nefritico"),
    ("AKI tras choque o nefrotoxico que no mejora con liquidos",
     "&iquest;Hubo <b>hipotension/choque prolongado</b> o <b>contraste/aminoglucosidos/rabdomiolisis</b>? &iquest;no responde a volumen?",
     "AKI intrinseca + cilindros granulosos 'pardos lodosos' + FeNa &gt;2%.", "Necrosis tubular aguda (NTA)", "nta"),
    ("Anuria con globo vesical o prostatismo",
     "&iquest;<b>Chorro debil, goteo, sensacion de no vaciar</b>, anuria fluctuante? &iquest;globo palpable, prostata?",
     "Oliguria/anuria + globo vesical/hidronefrosis en USG; mejora al sondar.", "AKI postrenal (obstructiva)", "postrenal"),
    ("Confusion fluctuante con temblor 'de aleteo' en cirrotico",
     "&iquest;<b>Confusion/somnolencia con asterixis</b>? &iquest;estrenimiento, sangrado, infeccion, sedantes (precipitante)?",
     "Deterioro cognitivo fluctuante + asterixis en hepatopatia; casi siempre con un gatillo.", "Encefalopatia hepatica", "encefalopatia"),
    ("Ictericia y hepatomegalia dolorosa tras consumo intenso de alcohol",
     "&iquest;<b>Ictericia + fiebre + hepatomegalia dolorosa</b> tras ingesta alcoholica intensa reciente?",
     "Ictericia + AST/ALT &lt;300 con <b>AST:ALT &gt;2</b> + leucocitosis en bebedor.", "Hepatitis alcoholica", "hepatitis_alcoholica"),
    ("Cansancio crónico y anemia en paciente con enfermedad inflamatoria/neoplasia",
     "&iquest;Tiene una <b>enfermedad cronica</b> (inflamatoria, infecciosa, neoplasica, ERC)? &iquest;anemia que no cede a hierro?",
     "Anemia normo/microcitica con <b>ferritina normal/alta</b> y saturacion de transferrina baja.", "Anemia de enfermedad cronica", "anemia_cronica"),
    ("Anemia con parestesias y alteracion de la marcha",
     "&iquest;Hormigueos, alteracion de la marcha/propiocepcion, glositis? &iquest;dieta vegana, gastrectomia, alcohol?",
     "Anemia macrocitica + sintomas neurologicos (cordones posteriores) = deficit de B12.", "Anemia macrocitica (deficit de B12)", "anemia_macrocitica"),
    ("Poliartritis simetrica de manos con rigidez matutina prolongada",
     "&iquest;Dolor e inflamacion <b>simetrica de pequenas articulaciones</b> + <b>rigidez matutina &gt;1 h</b>? &iquest;semanas de evolucion?",
     "Poliartritis simetrica cronica + rigidez matutina prolongada; FR/anti-CCP.", "Artritis reumatoide", "ar"),
    ("Mujer joven con artralgias, eritema malar y fotosensibilidad",
     "&iquest;<b>Eritema malar, fotosensibilidad, ulceras orales, artralgias, serositis</b>? &iquest;sintomas multisistemicos?",
     "Afectacion multisistemica + ANA positivo; vigilar nefritis.", "Lupus eritematoso sistemico", "les"),
    ("Dolor y rigidez de hombros y caderas en mayor de 50 con VSG alta",
     "&iquest;<b>Dolor y rigidez de cinturas escapular y pelvica</b> en &gt;50 anos + VSG/PCR altas? &iquest;cefalea, sintomas visuales?",
     "Dolor/rigidez de cinturas + reactantes altos; respuesta dramatica a esteroide bajo.", "Polimialgia reumatica", "pmr"),
]
for titulo, p, pat, dx, tag in pares:
    add(deck_m, caso(titulo), llave(p, pat, dx), M + [tag])


def build():
    for d, f in [(deck_t, "Interrogatorio_01_Troncos.apkg"), (deck_c, "Interrogatorio_02_Llaves_core.apkg"),
                 (deck_m, "Interrogatorio_03_Llaves_menos.apkg")]:
        genanki.Package(d).write_to_file(os.path.join(OUTPUT_DIR, f))
        print(f"  -> {f} ({len(d.notes)} notas)")
    genanki.Package([deck_t, deck_c, deck_m]).write_to_file(
        os.path.join(OUTPUT_DIR, "No_Hay_Tiempo_MI_Interrogatorio_TODOS.apkg"))
    print(f"  -> TODOS ({sum(len(d.notes) for d in [deck_t, deck_c, deck_m])} notas)")


if __name__ == "__main__":
    build()
