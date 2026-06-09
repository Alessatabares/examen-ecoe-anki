"""FINAL — Matriz ECOE de razonamiento (no hay tiempo).

Arquitectura por EJE de razonamiento, no por enfermedad. Cada Dx se indexa
en varios ejes (su pregunta, su hallazgo, su estudio, su manejo) y se memoriza
por convergencia. ~26 cartas cubren las 6 especialidades.

  EJE 1 INTERROGATORIO  llave madre reutilizable        (pregunta -> Dx)
  EJE 2 EXPLORACION     por region                      (hallazgo -> Dx)
  EJE 3 ESTUDIOS        por herramienta                 (patron -> Dx)
  EJE 4 MANEJO          por conducta compartida         (bucket + switch)
  EJE 5 ALGORITMOS      secuencia fija                  (paro/PALS/ATLS)
  + RECETA peds y URGENCIA OBSTETRICA (localizacion-especificas)

Sin acentos (convencion del repo). Verifica dosis/metas/umbrales sede-dependientes
y la guia vigente (AHA/ESC, ADA, KDIGO, GOLD, GINA, ATLS, OMS) antes del examen.
"""
import os
import genanki

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "output")
os.makedirs(OUTPUT_DIR, exist_ok=True)

MODEL_ID = 1990010001
DECK_ID = 1990009500
DECK_NAME = "No hay tiempo::FINAL - Matriz ECOE"

CSS_BASE = """
.card { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  font-size: 18px; text-align: left; color: #1a1a1a; background-color: #fafafa;
  padding: 18px; line-height: 1.5; }
.caso { font-size: 21px; font-weight: 800; color: #1e3a8a; display:block; }
.eje { font-size:12px; font-weight:800; letter-spacing:.8px; text-transform:uppercase; color:#64748b; display:block;}
.prompt { display:block; margin-top:6px; color:#b45309; font-style:italic; }
#extra { margin-top: 14px; border: none; border-top: 1px solid #d4d4d4; padding-top: 10px; }
.b { display: block; margin: 9px 0; padding: 9px 12px; border-radius: 8px; }
.l { display: block; font-size: 12px; font-weight: 800; letter-spacing: .6px;
  text-transform: uppercase; margin-bottom: 4px; }
.itg { background:#eef2ff; border-left:4px solid #1e3a8a; } .itg .l{color:#1e3a8a;}
.exp { background:#ecfeff; border-left:4px solid #0e7490; } .exp .l{color:#0e7490;}
.ddx { background:#f5f3ff; border-left:4px solid #6d28d9; } .ddx .l{color:#6d28d9;}
.est { background:#f1f5f9; border-left:4px solid #334155; } .est .l{color:#334155;}
.mng { background:#ecfdf5; border-left:4px solid #047857; } .mng .l{color:#047857;}
.rec { background:#fffbeb; border-left:4px solid #b45309; } .rec .l{color:#b45309;}
.com { background:#fdf2f8; border-left:4px solid #be185d; } .com .l{color:#be185d;}
.alr { background:#fef2f2; border-left:4px solid #b91c1c; } .alr .l{color:#b91c1c;}
b { color: #111; } .v { color:#b45309; font-style:italic; } u { text-decoration-color:#6d28d9; }
table.k { border-collapse:collapse; width:100%; font-size:15px; margin-top:4px;}
table.k td { border:1px solid #cbd5e1; padding:3px 6px; vertical-align:top;}
table.k td:first-child{ font-weight:700; white-space:nowrap; background:#fff;}
"""

model = genanki.Model(
    MODEL_ID, "NHT Matriz",
    fields=[{"name": "Front"}, {"name": "Back"}],
    templates=[{"name": "Caso", "qfmt": "{{Front}}", "afmt": '{{Front}}<hr id="extra">{{Back}}'}],
    css=CSS_BASE)

deck = genanki.Deck(DECK_ID, DECK_NAME)
BASE_TAGS = ["no_hay_tiempo", "ecoe", "final", "matriz"]


def B(clase, label, html):
    return f'<span class="b {clase}"><span class="l">{label}</span>{html}</span>'


def kt(rows):
    body = "".join(f"<tr><td>{a}</td><td>{b}</td></tr>" for a, b in rows)
    return f'<table class="k">{body}</table>'


def card(eje, titulo, prompt, back, tags):
    front = (f'<span class="eje">{eje}</span><span class="caso">{titulo}</span>'
             f'<span class="prompt">{prompt}</span>')
    deck.add_note(genanki.Note(model=model, fields=[front, back], tags=BASE_TAGS + tags))


# ====================================================================
# EJE 1 — INTERROGATORIO (llave madre reutilizable: pregunta -> Dx)
# ====================================================================

card("Eje 1 - Interrogatorio", "Llave del DOLOR (ALICIA)",
 'Cualquier dolor. "Una sola bateria de preguntas; la respuesta te tira hacia el Dx."',
 B("itg", "Bateria comun (ALICIA / OPQRST)", """<b>A</b>paricion (subito vs gradual) &middot;
 <b>L</b>ocalizacion + <u>irradiacion/migracion</u> &middot; <b>I</b>ntensidad &middot;
 <b>C</b>aracter (colico, opresivo, urente, desgarrante) &middot; <b>I</b>rradiacion &middot;
 <b>A</b>tenua/agrava + <u>asociados</u> (fiebre, vomito, transito, orina) &middot; y en mujer fertil <b>FUM/βhCG</b>.""") +
 B("ddx", "La respuesta orienta", kt([
   ("Subito 'lo peor de mi vida'", "vascular/rotura: SAH, diseccion, AAA, ectopico roto"),
   ("Migra periumbilical -> FID", "apendicitis"),
   ("Colico flanco -> ingle + hematuria", "colico renal"),
   ("Opresivo retroesternal con esfuerzo", "SCA / angina"),
   ("Urente epigastrico, relacion con comida", "ulcera / ERGE"),
   ("En barra a la espalda + alcohol", "pancreatitis"),
   ("Pleuritico + disnea subita", "TEP / neumotorax")])) +
 B("alr", "Trampa", "El dolor subito y maximo desde el inicio es vascular hasta probar lo contrario; el que migra cambia de Dx con el tiempo."),
 ["interrogatorio", "dolor", "alicia"])

card("Eje 1 - Interrogatorio", "Llave de la DISNEA / dolor toracico",
 'Disnea o dolor toracico. "Primero descarto lo que mata en menos de 10 min."',
 B("itg", "Comun", """Inicio (subito vs progresivo), esfuerzo/ortopnea, dolor pleuritico vs opresivo,
 fiebre, tos/expectoracion, <u>factores de riesgo</u> (TVP/inmovilidad, FRCV, tabaco). ECG + SatO2 + signos vitales ya.""") +
 B("ddx", "Pista -> Dx (las que matan primero)", kt([
   ("Opresivo + irradia + diaforesis", "SCA"),
   ("Subito pleuritico + FR de TVP", "TEP"),
   ("Subito + timpanismo + IY + desvia traquea", "neumotorax a tension"),
   ("Desgarrante a espalda + asimetria de pulsos", "diseccion aortica"),
   ("Ortopnea + crepitantes + edema", "IC / edema agudo pulmon"),
   ("Fiebre + tos productiva + crepitantes focales", "neumonia"),
   ("Sibilancias difusas + atopia/tabaco", "asma / EPOC")])) +
 B("alr", "Trampa", "ECG y troponina normales NO descartan SCA temprano ni TEP: usa la clinica y repite/seria."),
 ["interrogatorio", "disnea", "dolor_toracico"])

card("Eje 1 - Interrogatorio", "Llave del SANGRADO (por sitio)",
 'Paciente que sangra. "El sitio define el cuestionario y el riesgo."',
 B("itg", "Comun", "Cuantia, tiempo, <u>repercusion hemodinamica</u> (mareo, sincope), anticoagulantes/AINE, hepatopatia.") +
 B("ddx", "Sitio -> que pregunto / Dx", kt([
   ("Hematemesis / melena", "HDA: varices (hepatopata) vs ulcera (AINE/dolor epigastrico)"),
   ("Rectorragia", "HDB: divertculos, angiodisplasia, neoplasia, hemorroides"),
   ("Hemoptisis", "via aerea: TEP, Ca, TB, bronquiectasias"),
   ("Sangrado vaginal 1er T", "aborto / ectopico / mola (FUM, βhCG)"),
   ("Sangrado vaginal 3er T", "placenta previa (indoloro) vs DPPNI (doloroso)"),
   ("Epistaxis / petequias / equimosis", "trastorno plaquetario/coagulacion")])) +
 B("alr", "Trampa", "Toda mujer fertil que sangra = βhCG. Sangrado + inestabilidad = reanima primero, estudia despues."),
 ["interrogatorio", "sangrado"])

card("Eje 1 - Interrogatorio", "Llave de la FIEBRE (foco + huesped)",
 'Sindrome febril. "Dos preguntas que ordenan todo: donde esta el foco y como es el huesped."',
 B("itg", "Comun", """Tiempo, patron, <u>localizar foco</u> (urinario, respiratorio, abdominal, piel, SNC, cateter),
 y <u>caracterizar al huesped</u> (edad, inmunosupresion, protesis/valvula, viajes, contactos).""") +
 B("ddx", "Foco -> Dx", kt([
   ("Disuria + fiebre + puno-percusion", "pielonefritis"),
   ("Tos + crepitantes focales", "neumonia"),
   ("Dolor abdominal + ictericia + fiebre", "colangitis (Charcot)"),
   ("Cefalea + rigidez de nuca + fotofobia", "meningitis"),
   ("Soplo nuevo + UDIV/valvula", "endocarditis"),
   ("Fiebre sin foco en lactante", "enfoque por edad + reactantes")])) +
 B("alr", "Trampa", "Fiebre + hipotension + foco = sepsis: bundle hora-1 (lactato, hemocultivos, ATB, cristaloides). No esperes el cultivo."),
 ["interrogatorio", "fiebre", "sepsis"])


# ====================================================================
# EJE 2 — EXPLORACION (por region: hallazgo -> Dx)
# ====================================================================

card("Eje 2 - Exploracion", "ABDOMEN por cuadrante (hallazgo -> Dx)",
 'Dolor abdominal. "La maniobra localiza y el cuadrante jerarquiza."',
 B("exp", "Maniobra -> que indica", kt([
   ("McBurney / Rovsing / psoas / obturador", "apendicitis"),
   ("Murphy (paro inspiratorio)", "colecistitis"),
   ("Puno-percusion lumbar", "pielonefritis / colico"),
   ("Rebote / defensa / abdomen en tabla", "irritacion peritoneal (perforacion)"),
   ("Masa pulsatil expansible", "AAA"),
   ("Dolor desproporcionado a la exploracion", "isquemia mesenterica"),
   ("Silencio auscultatorio", "ileo / peritonitis")])) +
 B("ddx", "Cuadrante -> sospecha", kt([
   ("FID", "apendicitis, ectopico, ovario"),
   ("HCD", "biliar, hepatitis"),
   ("Epigastrio", "pancreatitis, ulcera, SCA inferior"),
   ("FII", "diverticulitis"),
   ("Difuso/subito", "perforacion, isquemia, AAA")])) +
 B("alr", "Alarma", "Tabla + inestabilidad o masa pulsatil = quirofano. Tacto rectal siempre."),
 ["exploracion", "abdomen", "cirugia"])

card("Eje 2 - Exploracion", "CARDIACA (soplo/ruido -> Dx)",
 'Soplo o disnea. "El ruido te dice la valvula y la falla."',
 B("exp", "Hallazgo -> que indica", kt([
   ("Soplo sistolico foco aortico, irradia a carotidas, pulso parvus", "estenosis aortica"),
   ("Soplo holosistolico apical irradia a axila", "insuficiencia mitral"),
   ("Soplo diastolico decrescendo", "insuficiencia aortica"),
   ("Retumbo diastolico apical + chasquido", "estenosis mitral"),
   ("S3", "sobrecarga de volumen / IC"),
   ("S4", "ventriculo rigido (HVI, isquemia)"),
   ("IY + reflujo hepatoyugular + edema", "IC derecha / congestion"),
   ("Roce pericardico", "pericarditis")])) +
 B("alr", "Alarma", "Sincope + soplo de estenosis aortica severa = riesgo de muerte subita. Soplo nuevo + fiebre = endocarditis."),
 ["exploracion", "cardiaca", "soplos"])

card("Eje 2 - Exploracion", "PULMONAR (patron -> Dx)",
 'Tos/disnea. "Combina percusion + auscultacion: cada patron es una entidad."',
 B("exp", "Patron -> que indica", kt([
   ("Matidez + crepitantes + broncofonia/pectoriloquia", "consolidacion = neumonia"),
   ("Matidez basal + ausencia de murmullo + vibraciones disminuidas", "derrame pleural"),
   ("Timpanismo + ausencia de murmullo + IY", "neumotorax (a tension si IY/desvia)"),
   ("Sibilancias espiratorias difusas", "asma / EPOC / broncoespasmo"),
   ("Crepitantes bibasales finos 'velcro'", "edema pulmonar / fibrosis"),
   ("Espiracion alargada + torax en tonel", "EPOC")])) +
 B("alr", "Alarma", "Torax silente + somnolencia + normocapnia que sube en crisis asmatica = fatiga inminente (intubar). SatO2 &lt; 90%."),
 ["exploracion", "pulmonar"])

card("Eje 2 - Exploracion", "ORL / CUELLO (hallazgo -> Dx)",
 'Tos, fiebre, otalgia, odinofagia. "Donde esta la infeccion alta?"',
 B("exp", "Hallazgo -> que indica", kt([
   ("Timpano abombado, opaco, sin reflejo", "OMA"),
   ("Dolor al traccionar el pabellon + CAE inflamado", "otitis externa"),
   ("Dolor a presion senos + transiluminacion opaca + secrecion >10 d", "sinusitis bacteriana"),
   ("Exudado amigdalino + adenopatia + fiebre sin tos (Centor)", "faringitis estreptococica"),
   ("Adenopatia cervical dura, fija, indolora", "neoplasia / linfoma"),
   ("Tiroides aumentada + soplo + exoftalmos", "Graves")])) +
 B("alr", "Alarma", "Trismus + voz de papa caliente + desviacion uvula = absceso periamigdalino. Proptosis + oftalmoplejia post-sinusitis = celulitis orbitaria."),
 ["exploracion", "orl", "familiar"])

card("Eje 2 - Exploracion", "GENITOURINARIO alta vs baja",
 'Sintomas urinarios. "El nivel cambia el riesgo y el manejo."',
 B("exp", "Localizar (alta vs baja)", kt([
   ("Disuria + frecuencia + urgencia + dolor suprapubico, AFEBRIL", "cistitis (baja)"),
   ("Fiebre + escalofrio + dolor lumbar + puno-percusion +", "pielonefritis (alta)"),
   ("Dolor colico flanco-ingle + hematuria + inquieto", "colico renal/litiasis"),
   ("Goteo + chorro debil + globo vesical (varon mayor)", "obstruccion prostatica"),
   ("Flujo/lesion + dispareunia (mujer)", "considerar ITS / EPI -> tacto bimanual")])) +
 B("alr", "Alarma", "Pielo + sepsis u obstruccion (litiasis + fiebre) = urgencia, drenaje. Embarazada con bacteriuria = tratar siempre."),
 ["exploracion", "urinario", "familiar"])

card("Eje 2 - Exploracion", "PERIANAL + tacto rectal (hallazgo -> Dx)",
 'Dolor/sangrado anal o tacto rectal. "Inspeccion + tacto resuelven casi todo."',
 B("exp", "Hallazgo -> que indica", kt([
   ("Dolor intenso al defecar + sangre roja en papel + desgarro posterior", "fisura anal"),
   ("Tumefaccion azulada dolorosa en margen", "hemorroide trombosada"),
   ("Sangrado rojo indoloro que gotea post-defecacion", "hemorroides internas"),
   ("Dolor + fiebre + masa fluctuante perianal", "absceso perianal (drenar)"),
   ("Orificio con secrecion cronica", "fistula perianal"),
   ("Prostata aumentada lisa elastica / nodular dura", "HPB / Ca prostata"),
   ("Ampolla rectal vacia + dolor", "obstruccion / sospecha")])) +
 B("alr", "Alarma", "Dolor perianal desproporcionado + fiebre + crepitacion en diabetico = gangrena de Fournier (urgencia quirurgica)."),
 ["exploracion", "perianal", "tacto_rectal", "familiar"])


# ====================================================================
# EJE 3 — ESTUDIOS (por herramienta: patron normal/anormal -> Dx)
# ====================================================================

card("Eje 3 - Estudios", "ECG (patron -> Dx)",
 'Te dan un ECG. "Lee ritmo, eje, ST, QRS, T."',
 B("est", "Patron -> que indica (normal entre parentesis)", kt([
   ("Elevacion del ST + reciprocos", "IAMCEST -> reperfusion"),
   ("Infra-ST / T invertida", "isquemia / SCASEST"),
   ("R-R irregular sin onda P", "fibrilacion auricular"),
   ("T picudas -> QRS ancho -> sinusoidal", "HIPERKALEMIA (progresion)"),
   ("QT largo (QTc &lt;440-460)", "riesgo torsade (farmacos, hipoK/Mg/Ca)"),
   ("Bajo voltaje + alternancia electrica", "derrame/taponamiento"),
   ("S1Q3T3 / taqui sinusal", "TEP (poco sensible)")])) +
 B("alr", "Alarma", "ST elevado = activar reperfusion. Cambios de hiperK en dializado = calcio IV YA (estabiliza membrana)."),
 ["estudios", "ecg"])

card("Eje 3 - Estudios", "GASOMETRIA (paso a paso)",
 'Gasometria arterial. "pH -> primario -> compensacion -> anion gap."',
 B("est", "Valores y patron", kt([
   ("pH (7.35-7.45)", "&lt;7.35 acidosis, >7.45 alcalosis"),
   ("HCO3 (22-26)", "bajo = metabolica; alto = compensa/alcalosis met."),
   ("pCO2 (35-45)", "alto = respiratoria/compensa; bajo = hiperventila"),
   ("Anion gap (8-12)", "alto = MUDPILES (lactato, cetonas, uremia, toxicos)"),
   ("Acidosis met. AG alto", "CAD, acidosis lactica (sepsis/isquemia), uremia, toxicos"),
   ("Acidosis met. AG normal", "diarrea, ATR"),
   ("Acidosis respiratoria", "EPOC, depresion del centro (opioides)")])) +
 B("alr", "Alarma", "pH &lt; 7.2, lactato alto que no baja, o pCO2 que sube en asmatico cansado = via aerea/UCI."),
 ["estudios", "gasometria", "electrolitos"])

card("Eje 3 - Estudios", "BIOMETRIA HEMATICA (serie -> Dx)",
 'BH. "Cada serie cuenta una historia."',
 B("est", "Hallazgo -> que indica", kt([
   ("Anemia VCM &lt;80 (micro)", "ferropenia (sangrado), talasemia"),
   ("Anemia VCM 80-100 (normo)", "enf. cronica, sangrado agudo, hemolisis"),
   ("Anemia VCM >100 (macro)", "B12/folato, alcohol, hipotiroidismo"),
   ("Leucocitosis con neutrofilia / bandas", "infeccion bacteriana"),
   ("Leucocitosis con linfocitosis", "viral"),
   ("Eosinofilia", "alergia, parasitos, farmacos"),
   ("Plaquetas &lt;150 mil", "consumo (CID, PTI), esplenomegalia, medula")])) +
 B("alr", "Alarma", "Pancitopenia, blastos, o plaquetas muy bajas con sangrado = urgencia hematologica/onco."),
 ["estudios", "bh", "anemia"])

card("Eje 3 - Estudios", "QUIMICA SANGUINEA + ELECTROLITOS",
 'QS y electrolitos. "Glucosa, funcion renal, iones: normal vs alarma."',
 B("est", "Parametro (normal) -> anormal", kt([
   ("Glucosa (70-100)", "&lt;70 hipoglucemia (tratar YA); >250 crisis hiperglucemica"),
   ("Urea/Creatinina -> TFG", "TFG baja = AKI/ERC; relacion U/Cr alta = prerrenal"),
   ("Na (135-145)", "hipoNa (sintomas SNC); hiperNa (deshidratacion)"),
   ("K (3.5-5.0)", "hipoK (arritmia, U); HIPERK (T picudas -> calcio)"),
   ("Ca (8.5-10.5)", "hiperCa: 'stones, bones, groans, moans'; hipoCa: Chvostek/Trousseau"),
   ("HbA1c", ">=6.5 diabetes; meta &lt;7 en general")])) +
 B("alr", "Alarma", "K >6.5 o con cambios ECG, hipoglucemia, hiperCa sintomatica, hipoNa con convulsion = correccion inmediata."),
 ["estudios", "quimica", "electrolitos", "metabolico"])

card("Eje 3 - Estudios", "EGO + FUNCION RENAL",
 'EGO. "Sedimento + indices localizan el problema renal."',
 B("est", "Hallazgo -> que indica", kt([
   ("Nitritos + esterasa + piuria", "ITU"),
   ("Hematuria + cilindros hematicos / dismorficos", "glomerular (nefritico)"),
   ("Proteinuria masiva + lipiduria", "sindrome nefrotico"),
   ("Cilindros granulosos 'pardos'", "necrosis tubular aguda (NTA)"),
   ("FENa &lt;1% / Na orina bajo", "prerrenal (responde a volumen)"),
   ("FENa >2%", "renal (NTA establecida)"),
   ("Cristales + hematuria", "litiasis")])) +
 B("alr", "Alarma", "Oliguria + hiperK + acidosis + uremia (pericarditis, encefalopatia) = indicacion de dialisis."),
 ["estudios", "ego", "renal"])

card("Eje 3 - Estudios", "PERFIL HEPATICO (patron -> Dx)",
 'Pruebas de funcion hepatica. "Hepatocelular vs colestasico, y si sintetiza."',
 B("est", "Patron -> que indica", kt([
   ("ALT/AST muy altas (ALT>AST)", "hepatocelular: viral, farmacos, isquemia"),
   ("AST/ALT >2 + GGT alta", "alcoholica"),
   ("FA + GGT + bilirrubina directa altas", "colestasis: obstruccion biliar"),
   ("Bilirrubina indirecta aislada", "hemolisis / Gilbert"),
   ("Albumina baja + INR alto", "falla de sintesis (cirrosis, falla aguda)"),
   ("Patron mixto + ferritina/Cu", "metabolico (hemocromatosis, Wilson)")])) +
 B("alr", "Alarma", "Ictericia + INR alto + encefalopatia = falla hepatica aguda (referir a trasplante). Charcot/Reynolds = colangitis."),
 ["estudios", "hepatico"])

card("Eje 3 - Estudios", "IMAGEN basica (Rx torax / USG / cuando TAC)",
 'Eleccion costo-efectiva. "Que pido primero y que busco."',
 B("est", "Herramienta -> utilidad", kt([
   ("Rx torax", "consolidacion, derrame, neumotorax, cardiomegalia, aire libre subdiafragmatico"),
   ("Rx abdomen de pie", "niveles hidroaereos (obstruccion), aire libre (perforacion)"),
   ("USG abdominal", "1a linea: biliar, AAA, hidronefrosis, liquido libre (FAST)"),
   ("USG pelvico/transvaginal", "ectopico, masa anexial, embarazo"),
   ("AngioTAC torax", "TEP (si probabilidad alta o dimero D +)"),
   ("TAC abdomen c/contraste", "apendicitis dudosa, diverticulitis, isquemia, estadiaje"),
   ("TAC craneo simple", "ACV (excluir sangrado antes de trombolisis), trauma")])) +
 B("alr", "Alarma", "No retrases el tratamiento por la imagen en inestables: el USG a pie de cama (FAST/eco) decide en el shock."),
 ["estudios", "imagen", "rx", "usg"])


# ====================================================================
# EJE 4 — MANEJO (por conducta compartida: bucket + switch)
# ====================================================================

card("Eje 4 - Manejo", "BUCKET: Reperfusion urgente (tiempo = tejido)",
 'Oclusion aguda. "Mismo reloj para corazon, cerebro y pulmon."',
 B("mng", "Logica madre", "Hay un vaso ocluido y un tejido muriendo: <u>abrir el vaso dentro de la ventana</u> manda sobre todo lo demas. Antes, excluir lo que contraindica (sangrado).") +
 B("rec", "Switch por organo", kt([
   ("Corazon (IAMCEST)", "ICP primaria (o fibrinolisis si no hay cateterismo a tiempo) + doble antiagregacion + anticoagulante + estatina"),
   ("Cerebro (ACV isquemico)", "TAC excluye sangrado -> trombolisis IV en ventana +/- trombectomia si gran vaso. Registrar hora de inicio"),
   ("Pulmon (TEP de alto riesgo)", "inestable -> trombolisis; estable -> anticoagulacion")])) +
 B("itg", "Verbalizo", '<span class="v">"Confirmo la oclusion, reviso la ventana y contraindicaciones, y activo el codigo de reperfusion correspondiente sin demora."</span>') +
 B("alr", "Trampa", "El tiempo de inicio define la elegibilidad. Nunca trombolises sin excluir hemorragia (TAC en ACV, anamnesis de sangrado)."),
 ["manejo", "reperfusion", "sca", "acv", "tep"])

card("Eje 4 - Manejo", "BUCKET: Liquidos + corregir deficit + tratar el gatillo",
 'Deshidratado / descompensado metabolico. "Una logica para CAD, EHH, deshidratacion, shock hipovolemico, crisis suprarrenal."',
 B("mng", "Logica madre", "Llena el tanque, ajusta la mezcla, apaga la fuga: <u>volumen -> deficit especifico -> desencadenante</u>. El Dx solo dice cual deficit y cual gatillo.") +
 B("est", "Esqueleto identico", "1) ABC + 2 accesos + glucemia capilar. 2) cristaloide IV (bolos 20 mL/kg en shock/peds). 3) corregir el deficit (switch). 4) tratar el gatillo (infeccion u omision). 5) monitorizar.") +
 B("rec", "Switch", kt([
   ("CAD", "insulina + K (si &lt;3.3 repon antes); cerrar anion gap. Gatillo: infeccion/omision"),
   ("EHH", "volumen (enorme) + insulina baja; bajar glucosa lento. Gatillo: infeccion/debut"),
   ("Deshidratacion peds (Plan C)", "Ringer/SS 30+70 mL/kg + zinc. Gatillo: GEA viral"),
   ("Shock hipovolemico", "volumen/sangre (transfundir si hemorragico). Gatillo: sangrado"),
   ("Crisis suprarrenal", "hidrocortisona 100 mg IV + glucosa. Gatillo: estres/retiro de esteroide")])) +
 B("itg", "Verbalizo", '<span class="v">"Reanimo con cristaloides, corrijo el deficit de forma controlada y trato el factor que descompenso."</span>') +
 B("alr", "Trampa", "No insulina/esteroide sin volumen y K. Bajar glucosa/osmolaridad muy rapido -> edema cerebral. En hemorragico, lo definitivo es parar el sangrado."),
 ["manejo", "liquidos", "cad", "ehh", "metabolico", "hub"])

card("Eje 4 - Manejo", "BUCKET: Antibiotico empirico + control del foco",
 'Infeccion grave. "Mismo reflejo: cultiva, cubre temprano, drena el foco."',
 B("mng", "Logica madre", "En infeccion que amenaza: <u>cultivo antes del ATB -> ATB empirico precoz segun foco/huesped -> control del foco</u> (drenar/retirar). En sepsis, todo en la 1a hora.") +
 B("est", "Esqueleto", "Hemocultivos + del foco, lactato; ATB de amplio espectro precoz; cristaloides si hipotension/lactato alto; <u>source control</u> (drenaje, retiro de cateter/calculo).") +
 B("rec", "Switch por foco", kt([
   ("Sepsis sin foco", "amplio espectro segun huesped + reanimacion bundle hora-1"),
   ("Pielonefritis", "ATB urinario; drenar si obstruccion (litiasis+fiebre)"),
   ("Colangitis", "ATB + descompresion biliar (CPRE)"),
   ("NAC", "amoxicilina alta dosis +/- macrolido (atipicos); CURB-65 decide ingreso"),
   ("Meningitis bacteriana", "ATB urgente +/- dexametasona; no retrasar por la TAC")])) +
 B("itg", "Verbalizo", '<span class="v">"Tomo cultivos, inicio antibiotico empirico precoz segun el foco y controlo la fuente (drenaje/retiro)."</span>') +
 B("alr", "Trampa", "No retrases el ATB por completar estudios en sepsis/meningitis. El ATB sin control del foco (absceso, calculo, cateter) falla."),
 ["manejo", "antibiotico", "sepsis", "foco"])

card("Eje 4 - Manejo", "BUCKET: Soporte / autolimitado (no dar de mas)",
 'Cuadro viral o benigno. "El arte es NO sobretratar y educar."',
 B("mng", "Logica madre", "Muchos cuadros son <u>autolimitados</u>: el manejo es sintomatico + red flags + evitar antibiotico/estudio innecesario. Saber a quien NO tratar es competencia ECOE.") +
 B("rec", "Switch", kt([
   ("IVRA / faringitis viral", "sintomatico; ATB solo si Centro alto/estrep confirmado"),
   ("Bronquitis aguda", "sintomatico; sin antibiotico de rutina"),
   ("Bronquiolitis", "soporte, oxigeno e hidratacion; sin broncodilatador/ATB de rutina"),
   ("GEA viral", "SRO + alimentacion + zinc; sin antidiarreicos/ATB"),
   ("Lumbalgia mecanica", "analgesia + actividad; sin imagen si no hay red flags")])) +
 B("itg", "Verbalizo", '<span class="v">"Es un cuadro autolimitado; doy tratamiento sintomatico, explico signos de alarma y evito antibioticos que no ayudan."</span>') +
 B("alr", "Trampa", "Reevalua si: no mejora en el tiempo esperado, aparece red flag, o el huesped es vulnerable (lactante, inmunosuprimido, anciano)."),
 ["manejo", "soporte", "viral", "familiar"])

card("Eje 4 - Manejo", "BUCKET: Cronico (meta + apego + buscar descompensante)",
 'Enfermedad cronica en consulta o agudizada. "Misma estructura para DM, HTA, IC, EPOC, ERC, cirrosis, dislipidemia."',
 B("mng", "Logica madre", "El cronico se maneja por <u>meta + apego + prevenir/buscar el descompensante</u>. Si llega agudizado, la pregunta no es 'que tiene' sino '<b>que lo descompenso hoy</b>'.") +
 B("rec", "Switch (meta / descompensante tipico)", kt([
   ("DM2", "meta HbA1c ~7; metformina base + segun RCV (iSGLT2/aGLP1). Gatillo: infeccion/omision"),
   ("HTA", "meta segun riesgo; cambios de estilo + IECA/ARA2/calcioantag/tiazida. Gatillo: apego/AINE/sal"),
   ("IC", "GDMT (IECA/ARA-NI, betabloq, ARM, iSGLT2) + diuretico en congestion. Gatillo: transgresion/FA/SCA/infeccion"),
   ("EPOC", "broncodilatador de base + rehab + vacunas. Gatillo: infeccion. Crisis: O2 controlado + broncodil + esteroide"),
   ("ERC", "control TA/glucosa, IECA/ARA2, evitar nefrotoxicos. Vigilar K"),
   ("Cirrosis", "tratar complicacion (ascitis, PBE, varices, encefalopatia) + buscar precipitante"),
   ("Dislipidemia", "estatina segun riesgo CV; meta LDL por categoria")])) +
 B("itg", "Verbalizo", '<span class="v">"Reviso metas y apego, optimizo el tratamiento de base y, si esta agudizado, busco y trato el factor precipitante."</span>') +
 B("alr", "Trampa", "Tratar la agudizacion sin corregir el desencadenante = recae. Vigila K con IECA/ARA2/ARM y funcion renal."),
 ["manejo", "cronico", "dm", "hta", "ic", "epoc", "metabolico"])


# ====================================================================
# EJE 5 — ALGORITMOS (secuencia fija)
# ====================================================================

card("Eje 5 - Algoritmo", "PARO del adulto - BLS/ACLS + 5H 5T",
 'Paciente que se desploma. "Verbaliza el algoritmo y busca la causa reversible."',
 B("mng", "Secuencia", """<b>1.</b> Seguridad + responde? + respira/boquea? + pulso en 10 s -> activa codigo y pide DEA/desfibrilador.
 <b>2. Compresiones:</b> 100-120/min, 5-6 cm, reexpansion completa, <b>30:2</b> (continuas + 1 vent c/6 s si via aerea avanzada), releva c/2 min.
 <b>3.</b> Analiza ritmo: <u>desfibrilable</u> (FV/TVsp) -> choque; <u>no</u> (asistolia/AESP) -> no choque.
 <b>4. Farmacos:</b> adrenalina 1 mg c/3-5 min (en no desfibrilable, ya; en desfibrilable, tras 2o choque); amiodarona 300 -> 150 mg si FV/TV refractaria.""") +
 B("est", "Buscar causa (5H/5T) por ABCDE y POCUS", kt([
   ("5H", "Hipovolemia, Hipoxia, H+ (acidosis), Hipo/HiperK, Hipotermia"),
   ("5T", "Trombosis coronaria, TEP, Taponamiento, neumoTorax a tension, Toxicos"),
   ("AESP QRS ancho", "hiperK / toxico"),
   ("VD dilatado en eco", "TEP"),
   ("Venas vacias / cava colapsada", "hipovolemia")])) +
 B("alr", "Post-RCE", "ECG 12 derivaciones (STEMI -> cateterismo), oxigenacion/TA controladas, control de temperatura, tratar causa. No declarar muerte en hipotermia hasta recalentar."),
 ["algoritmo", "paro", "bls", "acls", "urgencias", "5h5t"])

card("Eje 5 - Algoritmo", "PALS - nino grave / paro pediatrico",
 'Nino critico. "Triangulo de evaluacion + dosis por peso."',
 B("mng", "Secuencia", """<b>Triangulo (apariencia / respiratorio / circulatorio)</b> -> impresion. Luego ABCDE.
 <b>Compresiones:</b> 100-120/min, profundidad 1/3 del torax; relacion <b>15:2</b> con 2 reanimadores (30:2 si uno solo).
 <b>Shock:</b> bolo cristaloide <b>20 mL/kg</b> y reevalua (cuidado en cardiopata/desnutrido: 10 mL/kg).""") +
 B("rec", "Dosis por peso", kt([
   ("Adrenalina (paro)", "0.01 mg/kg IV/IO = 0.1 mL/kg de 1:10 000, c/3-5 min"),
   ("Desfibrilacion", "2 J/kg -> 4 J/kg -> hasta 10 J/kg"),
   ("Glucosa (hipoglucemia)", "0.5-1 g/kg (D10 5-10 mL/kg)"),
   ("Adrenalina nebulizada (crup/estridor)", "para obstruccion de via aerea superior"),
   ("Convulsion", "benzodiacepina IV/IM/rectal por peso")])) +
 B("alr", "Alarma", "En el nino el deterioro suele ser respiratorio antes que circulatorio: corrige hipoxia temprano. Bradicardia con mala perfusion = ventila/oxigena (compresiones si &lt;60 lpm pese a O2)."),
 ["algoritmo", "pals", "pediatria", "receta"])

card("Eje 5 - Algoritmo", "ATLS - politrauma (primary survey)",
 'Trauma grave. "ABCDE con control de hemorragia primero."',
 B("mng", "Secuencia (XABCDE)", """<b>X</b> control de hemorragia exanguinante (torniquete/presion).
 <b>A</b> via aerea + <u>control cervical</u>. <b>B</b> ventilacion (descarta neumotorax a tension/abierto, hemotorax).
 <b>C</b> circulacion: 2 vias gruesas, control de sangrado, <b>FAST</b>, cristaloide y <u>transfusion 1:1:1</u> si choque.
 <b>D</b> Glasgow + pupilas. <b>E</b> exposicion + evitar hipotermia.""") +
 B("est", "FAST / pistas", kt([
   ("Liquido libre en FAST + hipotension", "hemorragia abdominal -> quirofano"),
   ("IY + ruidos velados + hipotension", "taponamiento"),
   ("Asimetria + timpanismo + desvia traquea", "neumotorax a tension -> descompresion"),
   ("Pelvis inestable", "faja pelvica + hemorragia")])) +
 B("alr", "Alarma", "Acido tranexamico 1 g si hemorragia (en &lt;3 h). La triada letal: hipotermia + acidosis + coagulopatia. Reevalua ABC tras cada intervencion."),
 ["algoritmo", "atls", "trauma", "cirugia"])


# ====================================================================
# RECETA / LOCALIZACION-ESPECIFICAS (lo que no comprime sin perder dosis)
# ====================================================================

card("Receta - Pediatria", "RECETARIO pediatrico esencial (por peso)",
 'Nino que se va a casa. "Las dosis que mas se piden en ECOE."',
 B("rec", "Hidratacion (GEA)", kt([
   ("Plan A (sin deshid.)", "SRO baja osm: &lt;2 a 50-100 mL, >=2 a 100-200 mL tras cada evacuacion. Zinc &lt;6m 10 mg/d, >=6m 20 mg/d x 10-14 d"),
   ("Plan B (algun grado)", "SRO 75 mL/kg VO en 4 h, reevalua"),
   ("Plan C (grave)", "Ringer/SS IV: &lt;12m 30 mL/kg/1h + 70 mL/kg/5h; >=12m 30/30 min + 70/2.5 h"),
   ("Vomito impide VO", "ondansetron 0.15 mg/kg VO unica (2 mg 8-15 kg; 4 mg 15-30 kg)")])) +
 B("rec", "Antibioticos / via aerea", kt([
   ("OMA / neumonia", "amoxicilina 80-90 mg/kg/d divididos c/8-12 h x 5-7 d"),
   ("Faringitis estrep.", "penicilina o amoxicilina 50 mg/kg/d"),
   ("Crup", "dexametasona 0.15-0.6 mg/kg dosis unica; adrenalina nebulizada si estridor en reposo"),
   ("Asma/sibilancias", "salbutamol inhalado + esteroide sistemico si crisis"),
   ("Fiebre/dolor", "paracetamol 10-15 mg/kg c/4-6 h; ibuprofeno 5-10 mg/kg c/6-8 h")])) +
 B("alr", "Alarma", "Sin antidiarreicos en ninos. Verifica peso real y dosis maxima. Lactante febril &lt;3 meses = evaluacion completa, no manejo ambulatorio."),
 ["receta", "pediatria", "dosis"])

card("Localizacion - Obstetricia", "URGENCIA obstetrica (sangrado y HTA del embarazo)",
 'Embarazada con sangrado o crisis. "Lo que mata a madre y feto."',
 B("itg", "Localiza por trimestre y dolor", kt([
   ("1er T: dolor + amenorrea + βhCG", "ectopico / aborto / mola (USG transvaginal)"),
   ("3er T: sangrado indoloro, rojo brillante", "placenta previa (NO tacto antes de USG)"),
   ("3er T: doloroso, oscuro, utero leñoso + sufrimiento fetal", "DPPNI (riesgo CID)"),
   ("Cefalea/epigastralgia/fosfenos + TA alta + proteinuria", "preeclampsia")])) +
 B("mng", "Manejo", """<b>Sangrado:</b> ABC materno, 2 vias, cruzar sangre, monitoreo fetal, <u>anti-D si Rh-</u>;
 inestable o sufrimiento fetal -> cesarea urgente; estable pretermino -> conservar + corticoide.
 <b>Preeclampsia con datos de severidad/eclampsia:</b> <b>sulfato de Mg</b> (anticonvulsivo) + antihipertensivo + el parto es el tratamiento definitivo.""") +
 B("rec", "Recetas clave", kt([
   ("Madurez pulmonar (24-34 sem)", "betametasona 12 mg IM c/24 h x 2"),
   ("Isoinmunizacion", "inmunoglobulina anti-D 300 mcg IM si Rh- no sensibilizada"),
   ("Eclampsia", "sulfato de Mg IV (impregnacion + mantenimiento); vigilar reflejos/FR/diuresis")])) +
 B("alr", "Alarma", "Choque materno, utero leñoso, FCF anormal, CID, convulsion (eclampsia) = quirofano + codigo de hemorragia. Sulfato de Mg: antidoto = gluconato de calcio."),
 ["obstetricia", "hemorragia", "preeclampsia", "gineco_obstetricia", "receta"])


# ====================================================================
genanki.Package(deck).write_to_file(
    os.path.join(OUTPUT_DIR, "No_Hay_Tiempo_FINAL_Matriz.apkg"))
print(f"OK -> {len(deck.notes)} cartas -> No_Hay_Tiempo_FINAL_Matriz.apkg")
