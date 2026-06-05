"""No hay tiempo / Urgencias — PILAR EXPLORACION + ESTUDIOS.

A) DISCRIMINADOR: una herramienta separa un grupo por un hallazgo (por herramienta).
B) PANEL/workup: una entidad pide una bateria con rol de cada estudio (por enfermedad).
Signos y scores de urgencias + tabla de antidotos y toxidromes.
Guia: AHA/ACLS, ESC, Surviving Sepsis, ADA, GINA, GOLD, toxicologia, GPC MX.
"""
import os
import genanki

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "output")
os.makedirs(OUTPUT_DIR, exist_ok=True)

MODEL_QA_ID = 1990011903
DECK_ID_D, DECK_ID_P, DECK_ID_M = 1990011021, 1990011022, 1990011023
DECK_NAME_D = "No hay tiempo::Urgencias::Estudios::1 - Discriminadores (herramienta)"
DECK_NAME_P = "No hay tiempo::Urgencias::Estudios::2 - Paneles (por entidad)"
DECK_NAME_M = "No hay tiempo::Urgencias::Estudios::3 - Signos, scores y antidotos"

CSS_BASE = """
.card { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  font-size: 19px; text-align: left; color: #1a1a1a; background-color: #fafafa;
  padding: 20px; line-height: 1.5; }
.caso { font-size: 21px; font-weight: 700; color: #1e3a8a; }
#extra { margin-top: 16px; border: none; border-top: 1px solid #d4d4d4; padding-top: 12px; }
.bloque { display: block; margin: 12px 0; padding: 10px 14px; border-radius: 8px; }
.lab { display: block; font-size: 13px; font-weight: 700; letter-spacing: .5px;
  text-transform: uppercase; margin-bottom: 4px; }
.paraque { background: #eef2ff; border-left: 4px solid #1e3a8a; }
.trampa { background: #fef2f2; border-left: 4px solid #b91c1c; }
.pido { background: #eef2ff; border-left: 4px solid #1e3a8a; }
.descarto { background: #fff7ed; border-left: 4px solid #b45309; }
.clave { background: #ecfdf5; border-left: 4px solid #047857; }
.paraque .lab { color: #1e3a8a; } .trampa .lab { color: #b91c1c; }
.pido .lab { color: #1e3a8a; } .descarto .lab { color: #b45309; } .clave .lab { color: #047857; }
table.disc { border-collapse: collapse; width: 100%; margin: 6px 0 4px 0; font-size: 17px; }
table.disc td { border-bottom: 1px solid #e5e7eb; padding: 7px 8px; vertical-align: top; }
table.disc td.dx { font-weight: 700; color: #065f46; white-space: nowrap; }
b { color: #111; }
"""
model_qa = genanki.Model(MODEL_QA_ID, "NHT Urg Estudios QA",
    fields=[{"name": "Front"}, {"name": "Back"}],
    templates=[{"name": "QA", "qfmt": "{{Front}}", "afmt": '{{Front}}<hr id="extra">{{Back}}'}],
    css=CSS_BASE)

deck_d = genanki.Deck(DECK_ID_D, DECK_NAME_D)
deck_p = genanki.Deck(DECK_ID_P, DECK_NAME_P)
deck_m = genanki.Deck(DECK_ID_M, DECK_NAME_M)
BASE_TAGS = ["urgencias", "ecoe", "no_hay_tiempo", "estudios"]


def add(deck, front, back, tags):
    deck.add_note(genanki.Note(model=model_qa, fields=[front, back], tags=BASE_TAGS + tags))

def caso(t): return f'<span class="caso">{t}</span>'

def disc(pq, filas, tr):
    rows = "".join(f'<tr><td>{h}</td><td class="dx">{d}</td></tr>' for h, d in filas)
    return (f'<span class="bloque paraque"><span class="lab">Para que lo pido</span>{pq}</span>'
            f'<table class="disc">{rows}</table>'
            f'<span class="bloque trampa"><span class="lab">Trampa</span>{tr}</span>')

def panel(pido, des, clave):
    return (f'<span class="bloque pido"><span class="lab">Pido (bateria + para que)</span>{pido}</span>'
            f'<span class="bloque descarto"><span class="lab">Descarto / vigilo</span>{des}</span>'
            f'<span class="bloque clave"><span class="lab">Clave / criterio</span>{clave}</span>')


# ===================== DISCRIMINADORES (8) =====================
D = ["discriminador"]
add(deck_d, caso("ECG en urgencias"),
    disc("Tamizar isquemia, arritmia letal y datos toxico-metabolicos en minutos.",
         [("<b>Elevacion del ST</b> (o BRI nuevo)", "IAMCEST -> reperfusion"),
          ("Infra-ST / T invertidas", "Isquemia / SCASEST"),
          ("<b>T picudas -> QRS ancho -> sinusoidal</b>", "Hiperkalemia"),
          ("<b>QRS ancho</b> en intoxicado", "Triciclicos (-> bicarbonato)"),
          ("QT largo / FV-TV / asistolia", "Riesgo de paro / ritmo de paro")],
         "ECG normal NO descarta SCA (troponina seriada). Un QRS ancho en el intoxicado orienta a triciclicos."),
    D + ["ecg"])

add(deck_d, caso("Gasometria + brecha anionica"),
    disc("Clasificar el trastorno acido-base y orientar la causa.",
         [("pH bajo + <b>HCO3 bajo + brecha ALTA</b>", "Acidosis metabolica con brecha (ver MUDPILES)"),
          ("Acidosis con brecha normal (hipercloremica)", "Diarrea / acidosis tubular renal"),
          ("pH bajo + <b>PCO2 alta</b>", "Acidosis respiratoria (EPOC, hipoventilacion, opioides)"),
          ("<b>Alcalosis respiratoria + acidosis metabolica</b>", "Salicilatos / sepsis")],
         "Brecha anionica alta = <b>MUDPILES</b> (metanol, uremia, CAD, ... lactato, etilenglicol, salicilatos). "
         "Anade brecha osmolar si sospechas alcoholes toxicos."),
    D + ["gasometria"])

add(deck_d, caso("Lactato"),
    disc("Medir hipoperfusion/gravedad y guiar la reanimacion.",
         [("<b>Lactato elevado</b> + clinica de choque", "Hipoperfusion / sepsis"),
          ("Lactato muy alto + dolor abdominal desproporcionado", "Isquemia mesenterica"),
          ("Lactato que NO aclara con reanimacion", "Mal pronostico / foco no controlado"),
          ("Lactato alto + toxico (metformina, CO, cianuro)", "Acidosis lactica toxica")],
         "Lactato normal no descarta enfermedad grave temprana; su <b>aclaramiento</b> guia y es pronostico."),
    D + ["lactato"])

add(deck_d, caso("TAC de craneo simple (urgente)"),
    disc("Separar el ictus isquemico del hemorragico y decidir tratamiento.",
         [("<b>Sin sangre</b> + clinica de ACV en ventana", "Isquemico -> valorar trombolisis/trombectomia"),
          ("<b>Sangre (hiperdensa)</b> intraparenquimatosa", "ACV hemorragico -> control TA/revertir/neurocx"),
          ("Sangre en cisternas/subaracnoidea", "HSA -> (si TAC normal y alta sospecha: PL)"),
          ("Efecto de masa / desviacion de linea media", "Lesion ocupante / herniacion")],
         "<b>NO des antitromboticos hasta descartar hemorragia con la TAC.</b> La TAC precoz puede ser normal en el "
         "isquemico (no lo descarta)."),
    D + ["tac_craneo"])

add(deck_d, caso("Toxidromes (reconocer el patron)"),
    disc("Identificar el grupo de toxico por el patron clinico.",
         [("<b>Miosis + depresion respiratoria + bajo alerta</b>", "Opioide (-> naloxona)"),
          ("<b>Salivacion, lagrimeo, broncorrea, miosis, fasciculaciones</b>", "Colinergico / organofosforado (-> atropina)"),
          ("<b>Seco, rojo, caliente, midriasis, delirio, retencion</b>", "Anticolinergico"),
          ("<b>Agitacion, midriasis, taquicardia, HTA, diaforesis</b>", "Simpaticomimetico"),
          ("Sedacion con signos vitales conservados", "Sedante-hipnotico (benzo/alcohol)")],
         "El toxidrome orienta el antidoto y el soporte. 'Seco' (anticolinergico) vs 'mojado' (colinergico) es la "
         "dicotomia clave."),
    D + ["toxidromes"])

add(deck_d, caso("Glucemia capilar"),
    disc("Descartar la causa reversible mas rapida de alteracion del alerta/foco.",
         [("<b>Baja</b>", "Hipoglucemia (-> glucosa; tiamina antes si desnutrido)"),
          ("Muy alta + cetosis/acidosis", "CAD"),
          ("Muy alta + hiperosmolar sin cetosis", "EHH"),
          ("Normal", "Buscar otra causa (no la descarta como contribuyente)")],
         "Mide glucemia en TODO paciente con alteracion del alerta, foco neurologico o convulsion ANTES de la TAC."),
    D + ["glucemia"])

add(deck_d, caso("Troponina (alta sensibilidad)"),
    disc("Confirmar dano miocardico y, con la curva, separar agudo de cronico.",
         [("<b>Elevada con curva (sube/baja)</b> + clinica", "IAM (tipo 1)"),
          ("Elevada estable sin curva", "Dano cronico (ERC, IC) / tipo 2"),
          ("Negativa seriada + bajo riesgo", "Descarta IAM (alto VPN)")],
         "Troponina elevada NO siempre es IAM tipo 1: TEP, sepsis, miocarditis, IC y ERC tambien la elevan."),
    D + ["troponina"])

add(deck_d, caso("Brecha osmolar"),
    disc("Detectar alcoholes toxicos cuando la brecha anionica aun no explica todo.",
         [("<b>Brecha osmolar alta</b> + acidosis con brecha anionica", "Metanol / etilenglicol"),
          ("Brecha osmolar alta sin acidosis (temprano)", "Ingesta reciente de alcohol toxico"),
          ("Brecha osmolar normal", "No la descarta del todo (tardia se normaliza)")],
         "En acidosis con brecha anionica alta inexplicada + sospecha de ingesta: pide <b>brecha osmolar</b> "
         "(alcoholes toxicos) e inicia fomepizol sin esperar niveles."),
    D + ["brecha_osmolar"])


# ===================== PANELES (8) =====================
P = ["panel"]
add(deck_p, caso("Panel del SCA / dolor toracico"),
    panel("<b>ECG seriado (&lt;10 min) + troponina seriada</b>, BH, electrolitos, funcion renal, glucosa; Rx de "
          "torax. Angio-TAC si sospecha de diseccion/TEP.",
          "Lo que mata: TEP, diseccion, neumotorax, taponamiento; causas benignas (exclusion).",
          "ECG + troponina definen CEST vs SEST. Troponina elevada es inespecifica (integra con clinica/curva)."),
    P + ["sca"])

add(deck_p, caso("Panel de la sepsis (bundle de 1 hora)"),
    panel("<b>Lactato</b>, <b>2 hemocultivos antes del antibiotico</b> + cultivos del foco, BH, PCR/PCT, funcion "
          "renal/hepatica, coagulacion, gasometria; imagen del foco.",
          "Identificar y controlar el FOCO (absceso, viscera, via, tejido, dispositivo).",
          "Bundle 1 h: lactato + cultivos + antibiotico + 30 mL/kg cristaloide + vasopresor si TAM &lt;65."),
    P + ["sepsis"])

add(deck_p, caso("Panel del paciente intoxicado"),
    panel("<b>ABC + glucemia + ECG</b> + gasometria con <b>brecha anionica</b> + <b>niveles de paracetamol "
          "(siempre) y salicilatos</b>, etanol, electrolitos, funcion renal/hepatica; <b>brecha osmolar</b> si "
          "sospecha de alcoholes toxicos. Identificar toxidrome.",
          "Co-ingestas (paracetamol silente), complicaciones (arritmia, acidosis, convulsion), intencion suicida.",
          "<b>Pide paracetamol SIEMPRE</b> (silente y con antidoto eficaz). El QRS ancho orienta a triciclicos."),
    P + ["intoxicaciones"])

add(deck_p, caso("Panel del ACV / codigo ictus"),
    panel("<b>Glucemia</b> + <b>TAC de craneo simple urgente</b> + hora de inicio; ECG (FA), BH, coagulacion/INR, "
          "electrolitos. Angio/perfusion segun protocolo de trombectomia.",
          "Hemorragico (contraindica trombolisis); imitadores (hipoglucemia, postictal, migrana).",
          "<b>Glucemia + TAC + tiempo</b> deciden todo. No antitromboticos hasta descartar hemorragia."),
    P + ["acv"])

add(deck_p, caso("Panel de la cetoacidosis / EHH"),
    panel("<b>Glucemia, gasometria (pH, HCO3), cetonas, electrolitos seriados (K!), brecha anionica</b>, "
          "osmolaridad, funcion renal, EGO; ECG/Rx/cultivos para el desencadenante.",
          "Desencadenante (infeccion, omision de insulina, SCA, debut); vigilar K y brecha en el tratamiento.",
          "CAD = hiperglucemia + cetosis + acidosis con brecha. EHH = hiperosmolar sin cetoacidosis. K total bajo "
          "aunque el serico parezca normal."),
    P + ["cad_ehh"])

add(deck_p, caso("Panel de la anafilaxia"),
    panel("Es un dx <b>CLINICO</b> (no esperar estudios para tratar): adrenalina YA. <b>Triptasa serica</b> seriada "
          "puede apoyar a posteriori; valorar el desencadenante despues.",
          "Reaccion bifasica (recurrencia en horas); diagnosticos que imitan (asma, sincope, escombroide).",
          "No retrases la adrenalina por estudios. La triptasa apoya el dx pero NO se espera para tratar."),
    P + ["anafilaxia"])

add(deck_p, caso("Panel del shock (indiferenciado)"),
    panel("Monitor + <b>lactato</b> + gasometria + BH + funcion renal + <b>ECG</b> + <b>eco a pie de cama (POCUS: "
          "corazon, vena cava, pulmon, abdomen/FAST)</b> + grupo y cruzar si sangrado.",
          "Tipo de choque (hipovolemico/distributivo/cardiogenico/obstructivo); causa tratable (taponamiento, "
          "neumotorax a tension, TEP, sangrado).",
          "El POCUS clasifica rapido el choque a pie de cama. Lactato alto = hipoperfusion (guia la reanimacion)."),
    P + ["choque"])

add(deck_p, caso("Panel de la fiebre de origen desconocido (FUO)"),
    panel("<b>Estudio escalonado dirigido por pistas</b>: historia/exploracion repetidas, BH, VSG/PCR, "
          "hemocultivos, EGO/urocultivo, PFH, serologias/VIH, Rx/TAC, segun hallazgos. Evitar tratamiento empirico "
          "a ciegas.",
          "Infeccion, neoplasia (linfoma), autoinmune (vasculitis), miscelanea (farmacos).",
          "FUO = fiebre &gt;3 sem sin dx tras estudio adecuado. NO antibiotico/esteroide empirico (enmascara), "
          "salvo inestabilidad. Reexplora seriadamente."),
    P + ["fuo"])


# ===================== SIGNOS, SCORES Y ANTIDOTOS (18) =====================
M = ["signo_score"]
simple = [
    ("Adrenalina IM en anafilaxia", "<b>1er tratamiento</b>: adrenalina 1:1000 IM en cara anterolateral del muslo, repetir c/5-15 min. NO retrasar por antihistaminico/esteroide.", "anafilaxia"),
    ("Tabla de ANTIDOTOS (clave)", "Paracetamol&rarr;NAC; opioide&rarr;naloxona; benzo&rarr;flumazenil; organofosforado&rarr;atropina+pralidoxima; triciclico&rarr;bicarbonato; CO&rarr;O2 100%; metanol/etilenglicol&rarr;fomepizol; digoxina&rarr;Fab; betabloqueante&rarr;glucagon; hierro&rarr;deferoxamina.", "intoxicaciones"),
    ("Toxidrome colinergico (DUMBELS / SLUDGE)", "Defecacion, Ureo, Miosis, Bradicardia/Broncorrea, Emesis, Lagrimeo, Salivacion -> organofosforados (atropina).", "tox_organofosforados"),
    ("Toxidrome anticolinergico", "'Rojo como tomate, seco como hueso, caliente, loco y ciego' (midriasis, retencion, delirio).", "intoxicaciones"),
    ("Toxidrome opioide", "<b>Miosis + depresion respiratoria + bajo alerta</b> -> naloxona (vigilar recurrencia).", "tox_opioides"),
    ("Toxidrome simpaticomimetico", "Agitacion + midriasis + taquicardia + HTA + diaforesis + hipertermia (cocaina/anfetaminas).", "intoxicaciones"),
    ("Brecha anionica alta (MUDPILES)", "Metanol, Uremia, Diabetes (CAD), ... Lactato, Etilenglicol, Salicilatos -> acidosis con brecha.", "gasometria"),
    ("qSOFA", "TAS &le;100, FR &ge;22, alteracion mental (&ge;2 = riesgo de sepsis).", "sepsis"),
    ("Escala de coma de Glasgow (GCS)", "Ocular (4) + Verbal (5) + Motor (6); <b>&le;8 = asegurar via aerea</b> (intubacion).", "alteracion_alerta"),
    ("Regla del 15 (hipoglucemia)", "15 g de glucosa VO -> reevaluar a los 15 min -> repetir; IV/glucagon si no via oral.", "hipoglucemia"),
    ("Wells (TEP)", "Probabilidad pretest de TEP -> guia el dimero D vs angio-TAC directo.", "tep"),
    ("Triada de Beck + pulso paradojico", "Hipotension + ingurgitacion yugular + ruidos velados (+ caida de TAS en inspiracion) = taponamiento.", "taponamiento"),
    ("5 H y 5 T (causas de paro reversibles)", "5H: Hipoxia, Hipovolemia, H+ (acidosis), Hipo/HiperK, Hipotermia. 5T: neumotorax a Tension, Taponamiento, Toxicos, Trombosis (coronaria/pulmonar).", "rcp_acls"),
    ("Triada de Cushing (HTIC)", "HTA + bradicardia + respiracion irregular = hipertension intracraneal (herniacion inminente).", "acv"),
    ("Nomograma de Rumack-Matthew", "Nivel de paracetamol a las 4 h vs tiempo -> decide la NAC.", "tox_paracetamol"),
    ("Profilaxis ANTITETANICA (por herida)", "Herida limpia + &lt;3 dosis/desconocido -> vacuna. Herida sucia/tetanigena + esquema incompleto -> vacuna + <b>inmunoglobulina</b>.", "mordeduras"),
    ("Profilaxis ANTIRRABICA", "Lavado abundante + valorar vacuna &plusmn; <b>inmunoglobulina</b> (infiltrada en la herida) segun animal/exposicion. Rabia = casi 100% mortal, prevenible.", "mordeduras"),
    ("Onda J de Osborn", "Deflexion al final del QRS en la <b>hipotermia</b>; manejo cuidadoso (riesgo de FV).", "hipotermia"),
]
for titulo, texto, tag in simple:
    add(deck_m, caso(titulo),
        f'<span class="bloque paraque"><span class="lab">Que es / como se lee</span>{texto}</span>',
        M + [tag])


def build():
    for d, f in [(deck_d, "Estudios_01_Discriminadores.apkg"), (deck_p, "Estudios_02_Paneles.apkg"),
                 (deck_m, "Estudios_03_Signos_scores.apkg")]:
        genanki.Package(d).write_to_file(os.path.join(OUTPUT_DIR, f))
        print(f"  -> {f} ({len(d.notes)} notas)")
    genanki.Package([deck_d, deck_p, deck_m]).write_to_file(
        os.path.join(OUTPUT_DIR, "No_Hay_Tiempo_Urg_Estudios_TODOS.apkg"))
    print(f"  -> TODOS ({sum(len(d.notes) for d in [deck_d, deck_p, deck_m])} notas)")


if __name__ == "__main__":
    build()
