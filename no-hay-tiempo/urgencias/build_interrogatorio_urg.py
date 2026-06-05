"""No hay tiempo / Urgencias — PILAR INTERROGATORIO (tronco + llaves).

Tronco por motivo de consulta de urgencia (AMPLE/foco) + llave que fija el dx.
Guia: AHA/ACLS, ESC, Surviving Sepsis, ADA, GINA, GOLD, toxicologia, GPC MX.
"""
import os
import genanki

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "output")
os.makedirs(OUTPUT_DIR, exist_ok=True)

MODEL_QA_ID = 1990011902
DECK_ID_T, DECK_ID_C, DECK_ID_M = 1990011011, 1990011012, 1990011013
DECK_NAME_T = "No hay tiempo::Urgencias::Interrogatorio::1 - Troncos (ejes)"
DECK_NAME_C = "No hay tiempo::Urgencias::Interrogatorio::2 - Llaves comunes (core)"
DECK_NAME_M = "No hay tiempo::Urgencias::Interrogatorio::3 - Llaves menos comunes"

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
model_qa = genanki.Model(MODEL_QA_ID, "NHT Urg Interrogatorio QA",
    fields=[{"name": "Front"}, {"name": "Back"}],
    templates=[{"name": "QA", "qfmt": "{{Front}}", "afmt": '{{Front}}<hr id="extra">{{Back}}'}],
    css=CSS_BASE)

deck_t = genanki.Deck(DECK_ID_T, DECK_NAME_T)
deck_c = genanki.Deck(DECK_ID_C, DECK_NAME_C)
deck_m = genanki.Deck(DECK_ID_M, DECK_NAME_M)
BASE_TAGS = ["urgencias", "ecoe", "no_hay_tiempo", "interrogatorio"]


def add(deck, front, back, tags):
    deck.add_note(genanki.Note(model=model_qa, fields=[front, back], tags=BASE_TAGS + tags))

def caso(t): return f'<span class="caso">{t}</span>'

def tronco(ctx, ram):
    return (f'<span class="bloque contexto"><span class="lab">Pregunto siempre (contexto / AMPLE)</span>{ctx}</span>'
            f'<span class="bloque ramifica"><span class="lab">Esto me ramifica (sintoma guia -&gt; dx)</span>{ram}</span>')

def llave(p, pat, dx):
    return (f'<span class="bloque llave"><span class="lab">Pregunta-llave</span>{p}</span>'
            f'<span class="bloque patron"><span class="lab">Patron que confirma</span>{pat}</span>'
            f'<span class="bloque dx"><span class="lab">Diagnostico</span><b>{dx}</b></span>')


# ===================== TRONCOS (8) =====================
T = ["tronco"]
add(deck_t, caso("TRONCO — Dolor toracico"),
    tronco("<b>Caracter</b> (opresivo/pleuritico/desgarrante), irradiacion, esfuerzo/reposo, duracion, disnea, "
           "<b>vegetativo</b>, factores de riesgo CV, inmovilizacion/cirugia, ECG y troponina precoces.",
           "<b>Opresivo + esfuerzo + vegetativo</b> &rarr; SCA. <b>Pleuritico + disnea + factores</b> &rarr; TEP. "
           "<b>Desgarrante a espalda + asimetria de pulsos</b> &rarr; diseccion. <b>Subito + hipoxia + sin ruidos</b> "
           "&rarr; neumotorax (tension si inestable). <b>Trauma + Beck</b> &rarr; taponamiento."),
    T + ["dolor_toracico"])

add(deck_t, caso("TRONCO — Disnea"),
    tronco("Tiempo (subita vs progresiva), ortopnea, dolor pleuritico, fiebre/tos, sibilancias, edema, "
           "<b>SatO2</b>, factores (IC/EPOC/asma/inmovilizacion), exposicion (humo/alergeno).",
           "<b>Sibilancias + atopia</b> &rarr; asma. <b>Sibilancias + tabaco</b> &rarr; EPOC. <b>Ortopnea + edema</b> "
           "&rarr; IC. <b>Subita + pleuritica + factores</b> &rarr; TEP. <b>Habon + hipotension</b> &rarr; "
           "anafilaxia. <b>Subita + sin ruidos de un lado</b> &rarr; neumotorax."),
    T + ["disnea"])

add(deck_t, caso("TRONCO — Alteracion del estado de alerta / 'encontrado inconsciente'"),
    tronco("<b>Glucemia capilar SIEMPRE</b>, tiempo, ultimo estado normal, <b>toxicos/farmacos/alcohol</b> "
           "(frascos, jeringas, ambiente), trauma, fiebre, antecedentes (DM, epilepsia, hepatopatia, psiquiatrico), "
           "pupilas y foco.",
           "<b>Hipoglucemia</b> (siempre primero). <b>Miosis + depresion respiratoria</b> &rarr; opioides. "
           "<b>Focalidad</b> &rarr; ACV. <b>Fiebre + rigidez</b> &rarr; meningitis. <b>Toxico/frascos</b> &rarr; "
           "intoxicacion. <b>Na bajo/uremia</b> &rarr; metabolico."),
    T + ["alteracion_alerta"])

add(deck_t, caso("TRONCO — Deficit neurologico subito"),
    tronco("<b>Hora exacta de inicio / ultimo normal</b> (define ventana), glucemia, tipo de deficit, cefalea, "
           "crisis, TA, <b>FA/anticoagulantes</b>, trauma, factores de riesgo CV.",
           "<b>Deficit focal subito</b> &rarr; ACV (isquemico vs hemorragico por TAC). <b>+ cefalea en trueno</b> "
           "&rarr; hemorragia. <b>Transitorio que resolvio</b> &rarr; AIT. <b>Tras crisis</b> &rarr; deficit "
           "postictal (Todd)."),
    T + ["deficit_neuro"])

add(deck_t, caso("TRONCO — Reaccion alergica (habon / hinchazon / disnea tras exposicion)"),
    tronco("<b>Desencadenante</b> (alimento, farmaco, picadura) y tiempo, <b>afectacion de la via aerea</b> "
           "(ronquera, estridor, lengua), disnea/sibilancias, <b>hipotension/sincope</b>, vomito/dolor abdominal, "
           "exantema/habones, episodios previos.",
           "<b>Piel/mucosa + (respiratorio o hipotension o GI), inicio rapido tras exposicion</b> &rarr; anafilaxia. "
           "<b>Solo habones/prurito</b> &rarr; urticaria/reaccion leve. <b>Edema sin habones (a veces por IECA)</b> "
           "&rarr; angioedema."),
    T + ["alergia"])

add(deck_t, caso("TRONCO — Intoxicacion / sobredosis"),
    tronco("<b>Que, cuanto, cuando y por que via</b> (intencional?), co-ingestas (alcohol, <b>paracetamol</b>), "
           "frascos/recetas, <b>glucemia, ECG</b>, toxidrome (pupilas, piel, secreciones, FC, temperatura), riesgo "
           "suicida.",
           "<b>Miosis + depresion respiratoria</b> &rarr; opioides. <b>Secreciones + miosis + fasciculaciones</b> "
           "&rarr; colinergico (organofosforados). <b>Seco, rojo, caliente, midriasis, delirio</b> &rarr; "
           "anticolinergico. <b>Agitado, midriasis, taquicardia, HTA</b> &rarr; simpaticomimetico."),
    T + ["intoxicacion"])

add(deck_t, caso("TRONCO — Sindrome febril / sospecha de sepsis"),
    tronco("<b>Foco</b> (respiratorio, urinario, abdominal, piel, SNC, dispositivos), tiempo, <b>hemodinamia y "
           "estado mental (qSOFA)</b>, inmunosupresion/diabetes, viajes, contactos, <b>exantema/petequias</b>, "
           "duracion (FUO si prolongada).",
           "<b>qSOFA &ge;2 + foco</b> &rarr; sepsis. <b>Petequias que no blanquean + mal estado</b> &rarr; "
           "meningococemia. <b>Fiebre &gt;3 semanas sin dx</b> &rarr; FUO. <b>Foco claro</b> &rarr; su entidad "
           "(NAC, pielonefritis, etc.)."),
    T + ["fiebre"])

add(deck_t, caso("TRONCO — Convulsion"),
    tronco("<b>Glucemia</b>, primera vez vs conocida, duracion y numero, <b>generalizada vs focal</b>, recuperacion, "
           "fiebre, trauma, <b>toxicos/abstinencia (alcohol)</b>, embarazo (eclampsia), adherencia a "
           "antiepilepticos, Na.",
           "<b>Crisis &ge;5 min o repetidas sin recuperar</b> &rarr; status (benzodiacepina YA). <b>Hipoglucemia/"
           "hiponatremia</b> &rarr; metabolica. <b>Embarazo + HTA</b> &rarr; eclampsia. <b>Abstinencia "
           "alcoholica</b> &rarr; convulsion por privacion."),
    T + ["convulsion"])


# ===================== LLAVES CORE (16) =====================
C = ["core"]
add(deck_c, caso("Dolor opresivo retroesternal con esfuerzo, irradiado, con sudor frio"),
    llave("&iquest;Dolor <b>opresivo</b> con el esfuerzo, irradia a brazo/mandibula, con <b>diaforesis/nausea</b>? "
          "&iquest;factores de riesgo CV?",
          "Dolor anginoso tipico + vegetativo + factores; ECG y troponina lo definen.",
          "Sindrome coronario agudo"),
    C + ["sca"])

add(deck_c, caso("Disnea subita y dolor pleuritico tras inmovilizacion o cirugia"),
    llave("&iquest;Disnea <b>subita</b> + dolor pleuritico + <b>factores</b> (cirugia, inmovilidad, cancer, "
          "anticonceptivos, TVP)? &iquest;pierna hinchada?",
          "Disnea/dolor pleuritico subitos + taquicardia + hipoxia con factores (Wells).",
          "Tromboembolia pulmonar"),
    C + ["tep"])

add(deck_c, caso("Habones, hinchazon de labios y disnea minutos despues de un alimento o farmaco"),
    llave("&iquest;<b>Inicio rapido tras una exposicion</b> con <b>piel/mucosa + via aerea o hipotension o "
          "sintomas GI</b>?",
          "Afectacion de &ge;2 sistemas de inicio rapido tras alergeno (o hipotension tras alergeno conocido).",
          "Anafilaxia"),
    C + ["anafilaxia"])

add(deck_c, caso("Deficit neurologico focal de inicio subito"),
    llave("&iquest;<b>Debilidad/asimetria facial/alteracion del habla SUBITAS</b>? &iquest;<b>hora exacta de "
          "inicio</b>? &iquest;FA/anticoagulantes? &iquest;glucemia?",
          "Focalidad neurologica subita (FAST); la TAC separa isquemico de hemorragico.",
          "ACV / ictus"),
    C + ["acv"])

add(deck_c, caso("Convulsion que no cede o se repite sin recuperar la conciencia"),
    llave("&iquest;La crisis <b>dura &ge;5 min</b> o <b>se repite sin recuperar</b>? &iquest;glucemia? "
          "&iquest;abstinencia/toxico? &iquest;embarazo?",
          "Actividad convulsiva continua/recurrente sin recuperacion; emergencia tiempo-dependiente.",
          "Status epileptico"),
    C + ["status"])

add(deck_c, caso("Fiebre + hipotension + taquicardia + confusion con un foco"),
    llave("&iquest;<b>qSOFA &ge;2</b> (TAS &le;100, FR &ge;22, alteracion mental) con un foco infeccioso? "
          "&iquest;inmunosupresion/dispositivos?",
          "Disfuncion organica por infeccion; lactato alto y/o hipotension que requiere vasopresor.",
          "Sepsis / shock septico"),
    C + ["sepsis"])

add(deck_c, caso("Poliuria, nausea y respiracion profunda en diabetico"),
    llave("&iquest;<b>Mucha sed/orina, nausea, dolor abdominal, respiracion profunda</b> (Kussmaul)? &iquest;omitio "
          "insulina o tiene infeccion?",
          "Hiperglucemia + cetosis + acidosis con un desencadenante.",
          "Cetoacidosis diabetica"),
    C + ["cad"])

add(deck_c, caso("Diaforesis, temblor y confusion que ceden al comer (diabetico tratado)"),
    llave("&iquest;<b>Adrenergico (sudor, temblor, palpitaciones) o neuroglucopenico (confusion, foco, crisis)</b> "
          "que mejora con azucar? &iquest;insulina/sulfonilurea, ayuno, alcohol?",
          "Sintomas que revierten con glucosa + glucemia capilar baja (triada de Whipple).",
          "Hipoglucemia"),
    C + ["hipoglucemia"])

add(deck_c, caso("Debilidad y palpitaciones con T picudas en el ECG (paciente renal)"),
    llave("&iquest;Debilidad, parestesias, palpitaciones? &iquest;ERC, IECA/ARA-II/ARM, AINE, lisis tumoral/"
          "rabdomiolisis? &iquest;ECG con T picudas?",
          "Hiperkalemia: T picudas &rarr; QRS ancho; riesgo de arritmia letal.",
          "Hiperkalemia"),
    C + ["hiperkalemia"])

add(deck_c, caso("Crisis de disnea con sibilancias que no responde al inhalador"),
    llave("&iquest;Crisis de asma que <b>no cede con SABA</b>? &iquest;habla entrecortado, usa musculos "
          "accesorios? &iquest;SatO2?",
          "Broncoespasmo grave; busca silencio auscultatorio/agotamiento (paro inminente).",
          "Crisis asmatica grave"),
    C + ["asma"])

add(deck_c, caso("Disnea y mas esputo purulento en fumador con EPOC"),
    llave("&iquest;<b>Aumento de disnea + esputo + purulencia</b> (Anthonisen)? &iquest;SatO2? &iquest;somnolencia "
          "(hipercapnia)?",
          "Exacerbacion de EPOC; vigilar acidosis respiratoria (VMNI).",
          "EPOC exacerbado"),
    C + ["epoc"])

add(deck_c, caso("Cifras tensionales muy altas con dolor toracico / disnea / deficit"),
    llave("&iquest;TA muy alta + <b>dato de dano agudo de organo</b> (toracico, disnea, neurologico, vision)? "
          "&iquest;embarazo (eclampsia)?",
          "TA severamente elevada + dano agudo de organo blanco (separa emergencia de urgencia).",
          "Emergencia hipertensiva"),
    C + ["emergencia_htas"])

add(deck_c, caso("Taquicardia + hipotension + mala perfusion"),
    llave("&iquest;<b>Taquicardia, hipotension, llenado lento, oliguria, confusion</b>? &iquest;cual es el tipo "
          "(sangrado, infeccion, bomba, obstruccion)?",
          "Hipoperfusion sistemica; clasificar el tipo de choque dirige el tratamiento.",
          "Choque"),
    C + ["choque"])

add(deck_c, caso("Vomito con sangre o posos de cafe y heces negras"),
    llave("&iquest;<b>Hematemesis/posos + melena</b>? &iquest;AINE, alcohol, hepatopatia/varices, "
          "anticoagulantes? &iquest;mareo/sincope?",
          "Sangrado digestivo alto + repercusion hemodinamica; varices si hepatopata.",
          "Hemorragia digestiva alta"),
    C + ["hda"])

add(deck_c, caso("Paciente que ingirio medicamentos/sustancia"),
    llave("&iquest;<b>Que, cuanto, cuando, por que via</b>? &iquest;co-ingesta (paracetamol/alcohol)? "
          "&iquest;toxidrome (pupilas, piel, secreciones, FC)? &iquest;intencional?",
          "Cuadro guiado por el toxidrome + tiempo desde la ingesta; pedir paracetamol siempre.",
          "Intoxicacion aguda"),
    C + ["intoxicaciones"])

add(deck_c, caso("Encontrado inconsciente, sin respuesta"),
    llave("&iquest;<b>Glucemia? respira? pulso?</b> &iquest;pupilas/foco? &iquest;toxicos/frascos? &iquest;ultimo "
          "estado normal? (coctel: tiamina/glucosa/naloxona)",
          "Bajo nivel de alerta; ABC + glucemia + descartar causas reversibles (AEIOU-TIPS).",
          "Alteracion del estado de alerta / coma"),
    C + ["alteracion_alerta"])


# ===================== LLAVES MENOS (16) =====================
M = ["menos_comun"]
pares = [
    ("Nausea y vomito horas tras tomar 'muchas pastillas' de paracetamol, asintomatico",
     "&iquest;<b>Cuanto y hace cuanto</b>? &iquest;sintomas (suele estar asintomatico al inicio)? &iquest;"
     "co-ingestas?",
     "Sobredosis de paracetamol; nivel a las 4 h (nomograma) guia la NAC.", "Intoxicacion por paracetamol", "tox_paracetamol"),
    ("Bajo nivel de alerta con miosis puntiforme y respiracion lenta",
     "&iquest;<b>Miosis + depresion respiratoria + bajo alerta</b>? &iquest;uso de opioides/jeringas?",
     "Toxidrome opioide (miosis + hipoventilacion); responde a naloxona.", "Intoxicacion por opioides", "tox_opioides"),
    ("Trabajador agricola con salivacion, lagrimeo, miosis y dificultad respiratoria",
     "&iquest;<b>Secreciones (salivacion/broncorrea) + miosis + fasciculaciones + diarrea</b>? &iquest;contacto "
     "con insecticidas?",
     "Toxidrome colinergico (DUMBELS/SLUDGE); atropina + pralidoxima.", "Intoxicacion por organofosforados", "tox_organofosforados"),
    ("Varias personas de una casa con cefalea, nausea y mareo en invierno",
     "&iquest;<b>Varios convivientes con los mismos sintomas</b>? &iquest;calentador/combustion en espacio "
     "cerrado? &iquest;mejora al salir?",
     "Cefalea/nausea en multiples expuestos a combustion; carboxihemoglobina alta.", "Intoxicacion por monoxido de carbono", "tox_co"),
    ("Sobredosis con convulsiones y QRS ancho en el ECG",
     "&iquest;Ingirio <b>antidepresivo triciclico</b>? &iquest;convulsiones, hipotension? &iquest;ECG con "
     "<b>QRS ancho</b>?",
     "Cardiotoxicidad (QRS ancho) + convulsiones + anticolinergico; bicarbonato.", "Intoxicacion por triciclicos", "tox_triciclicos"),
    ("Acidosis grave con brecha osmolar tras ingerir 'alcohol' no bebible",
     "&iquest;Ingirio <b>anticongelante/alcohol de quemar</b>? &iquest;vision borrosa (metanol)? &iquest;"
     "dolor lumbar (etilenglicol)?",
     "Acidosis con brecha anionica Y osmolar altas; fomepizol/etanol + dialisis.", "Alcoholes toxicos (metanol/etilenglicol)", "tox_alcoholes"),
    ("Tinnitus, hiperventilacion y fiebre tras tomar muchas aspirinas",
     "&iquest;<b>Tinnitus + hiperventilacion + nausea</b>? &iquest;cuanta aspirina? &iquest;fiebre/confusion?",
     "Alcalosis respiratoria + acidosis metabolica con brecha + tinnitus.", "Intoxicacion por salicilatos", "tox_salicilatos"),
    ("Mordedura de perro/animal en la mano",
     "&iquest;<b>Que animal, provocado o no, estado de vacunacion del animal</b>? &iquest;profundidad/localizacion? "
     "&iquest;sus vacunas (tetanos)?",
     "Herida por mordedura; decidir profilaxis antirrabica y antitetanica + lavado.", "Mordeduras (rabia/tetanos)", "mordeduras"),
    ("Fiebre prolongada de semanas sin causa clara pese al estudio inicial",
     "&iquest;<b>Cuanto tiempo (&gt;3 semanas)</b>? &iquest;viajes, contactos, animales, farmacos, sintomas B, "
     "antecedentes? &iquest;estudio inicial ya hecho?",
     "Fiebre &gt;3 semanas sin dx tras estudio adecuado (infeccion/neoplasia/autoinmune).", "Fiebre de origen desconocido (FUO)", "fuo"),
    ("Persona joven que colapsa tras ejercicio intenso con calor, piel caliente y confusa",
     "&iquest;<b>Exposicion al calor/ejercicio + temperatura muy alta + alteracion del estado mental</b>? "
     "&iquest;deja de sudar (clasico)?",
     "Hipertermia (&gt;40 C) + disfuncion del SNC; enfriamiento agresivo.", "Golpe de calor", "golpe_calor"),
    ("Persona hallada en el frio, bradicardica y con bajo nivel de alerta",
     "&iquest;<b>Exposicion al frio</b>? &iquest;temperatura central baja? &iquest;bradicardia, alteracion del "
     "alerta? &iquest;onda J en el ECG?",
     "Temperatura central baja + bradicardia + alteracion del alerta (onda de Osborn).", "Hipotermia", "hipotermia"),
    ("Persona que se lleva las manos al cuello mientras comia y no puede hablar",
     "&iquest;<b>Tose de forma efectiva o no</b>? &iquest;puede hablar/respirar? &iquest;signo universal "
     "(manos al cuello)?",
     "Obstruccion de via aerea por cuerpo extrano; la tos inefectiva indica intervenir.", "Atragantamiento (OVACE)", "atragantamiento"),
    ("Perdida transitoria del conocimiento con recuperacion completa",
     "&iquest;<b>Prodromos</b> y gatillo (vasovagal) o fue <b>de esfuerzo/en supino/con palpitaciones</b> (rojo)? "
     "&iquest;cardiopatia? &iquest;ECG?",
     "Vasovagal (prodromos + gatillo) vs cardiogenico (banderas de alto riesgo).", "Sincope", "sincope"),
    ("Trauma toracico con hipotension, yugulares ingurgitadas y sin ruidos de un lado",
     "&iquest;<b>Disnea subita + hipotension + ausencia de ruidos + traquea desviada</b>?",
     "Insuficiencia respiratoria + colapso hemodinamico; dx CLINICO.", "Neumotorax a tension", "neumotorax_tension"),
    ("Hipotension con yugulares ingurgitadas y ruidos cardiacos velados",
     "&iquest;<b>Hipotension + ingurgitacion yugular + ruidos velados</b> (Beck) + pulso paradojico? &iquest;trauma/"
     "pericarditis/cancer?",
     "Triada de Beck + pulso paradojico; FAST con liquido pericardico.", "Taponamiento cardiaco", "taponamiento"),
    ("Dolor toracico desgarrante que migra a la espalda con asimetria de pulsos",
     "&iquest;Dolor <b>'que rasga'</b> que migra a la espalda + <b>asimetria de pulsos/TA</b>? &iquest;HTA/Marfan?",
     "Dolor desgarrante migratorio + asimetria de pulsos + mediastino ancho.", "Diseccion aortica", "diseccion"),
]
for titulo, p, pat, dx, tag in pares:
    add(deck_m, caso(titulo), llave(p, pat, dx), M + [tag])


def build():
    for d, f in [(deck_t, "Interrogatorio_01_Troncos.apkg"), (deck_c, "Interrogatorio_02_Llaves_core.apkg"),
                 (deck_m, "Interrogatorio_03_Llaves_menos.apkg")]:
        genanki.Package(d).write_to_file(os.path.join(OUTPUT_DIR, f))
        print(f"  -> {f} ({len(d.notes)} notas)")
    genanki.Package([deck_t, deck_c, deck_m]).write_to_file(
        os.path.join(OUTPUT_DIR, "No_Hay_Tiempo_Urg_Interrogatorio_TODOS.apkg"))
    print(f"  -> TODOS ({sum(len(d.notes) for d in [deck_t, deck_c, deck_m])} notas)")


if __name__ == "__main__":
    build()
