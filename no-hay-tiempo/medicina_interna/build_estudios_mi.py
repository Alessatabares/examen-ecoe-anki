"""No hay tiempo / Medicina Interna — PILAR EXPLORACION + ESTUDIOS.

A) DISCRIMINADOR: una herramienta separa un grupo por un hallazgo (por herramienta).
B) PANEL/workup: una entidad pide una bateria con rol de cada estudio (por enfermedad).
Guia: ESC, ADA, KDIGO, GOLD, GINA, AHA/ACC, EASL, GPC mexicanas.
"""
import os
import genanki

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "output")
os.makedirs(OUTPUT_DIR, exist_ok=True)

MODEL_QA_ID = 1990008003
DECK_ID_D, DECK_ID_P, DECK_ID_M = 1990007021, 1990007022, 1990007023
DECK_NAME_D = "No hay tiempo::Medicina Interna::Estudios::1 - Discriminadores (herramienta)"
DECK_NAME_P = "No hay tiempo::Medicina Interna::Estudios::2 - Paneles (por entidad)"
DECK_NAME_M = "No hay tiempo::Medicina Interna::Estudios::3 - Signos y scores"

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
model_qa = genanki.Model(MODEL_QA_ID, "NHT MI Estudios QA",
    fields=[{"name": "Front"}, {"name": "Back"}],
    templates=[{"name": "QA", "qfmt": "{{Front}}", "afmt": '{{Front}}<hr id="extra">{{Back}}'}],
    css=CSS_BASE)

deck_d = genanki.Deck(DECK_ID_D, DECK_NAME_D)
deck_p = genanki.Deck(DECK_ID_P, DECK_NAME_P)
deck_m = genanki.Deck(DECK_ID_M, DECK_NAME_M)
BASE_TAGS = ["medicina_interna", "ecoe", "no_hay_tiempo", "estudios"]


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
add(deck_d, caso("ECG en dolor toracico / palpitaciones"),
    disc("Separar el SCA y las arritmias en los primeros minutos.",
         [("<b>Elevacion del ST</b> (o BRI nuevo)", "IAMCEST -> reperfusion"),
          ("<b>Infra-ST / T invertidas</b>", "SCASEST / isquemia"),
          ("<b>Sin onda P, R-R irregular</b>", "Fibrilacion auricular"),
          ("Elevacion ST <b>difusa concava + descenso PR</b>", "Pericarditis"),
          ("<b>T picudas -> QRS ancho</b>", "Hiperkalemia")],
         "Un ECG normal NO descarta SCA: si la clinica sugiere, troponina seriada y observa."),
    D + ["ecg"])

add(deck_d, caso("Troponina (alta sensibilidad)"),
    disc("Confirmar dano miocardico y, con la curva, distinguir agudo de cronico.",
         [("<b>Elevada con curva (sube/baja)</b> + clinica", "IAM (tipo 1)"),
          ("Elevada estable sin curva", "Dano cronico (ERC, IC) / tipo 2"),
          ("Negativa seriada + clinica de bajo riesgo", "Descarta IAM (alto VPN)")],
         "Troponina elevada NO siempre es IAM tipo 1: TEP, sepsis, IC, miocarditis, ERC tambien la elevan."),
    D + ["troponina"])

add(deck_d, caso("BNP / NT-proBNP en disnea"),
    disc("Apoyar o descartar origen cardiaco de la disnea.",
         [("<b>Muy elevado</b> + clinica", "IC como causa de la disnea"),
          ("<b>Bajo/normal</b>", "IC poco probable (alto VPN)"),
          ("Elevado en TEP/FA/ERC", "Inespecifico (interpretar con clinica)")],
         "Obesidad da BNP falsamente bajo; edad, FA y ERC lo elevan. Usalo con la clinica, no aislado."),
    D + ["bnp"])

add(deck_d, caso("Dimero D + score de probabilidad (Wells/PERC)"),
    disc("Descartar TEP/TVP en probabilidad BAJA-INTERMEDIA.",
         [("Probabilidad baja + <b>dimero D negativo</b>", "Descarta TEP (no imagen)"),
          ("Probabilidad alta", "Anticoagular e ir directo a angio-TAC"),
          ("Dimero D positivo", "No confirma: requiere imagen")],
         "El dimero D solo sirve para DESCARTAR en baja probabilidad: en alta probabilidad ve directo a la imagen."),
    D + ["dimero_d"])

add(deck_d, caso("Gasometria arterial"),
    disc("Clasificar el trastorno acido-base y la insuficiencia respiratoria.",
         [("pH bajo + <b>HCO3 bajo + brecha alta</b>", "Acidosis metabolica (CAD, lactica, uremia)"),
          ("pH bajo + <b>PCO2 alta</b>", "Acidosis respiratoria (EPOC, hipoventilacion)"),
          ("<b>PaO2 baja</b> con PCO2 baja", "Insuf. respiratoria tipo I (NAC, TEP, edema)"),
          ("PaO2 baja + <b>PCO2 alta</b>", "Insuf. respiratoria tipo II (EPOC)")],
         "Una PCO2 'normal' en una crisis asmatica grave (deberia estar baja) anuncia fatiga y paro inminente."),
    D + ["gasometria"])

add(deck_d, caso("Examen general de orina (EGO) + sedimento"),
    disc("Orientar la nefropatia y la infeccion urinaria.",
         [("<b>Cilindros hematicos</b> + proteinuria + dismorfia", "Glomerulonefritis (nefritico)"),
          ("<b>Proteinuria masiva</b> + lipiduria", "Sindrome nefrotico"),
          ("<b>Cilindros granulosos pardos</b>", "NTA"),
          ("<b>Leucocituria + nitritos + bacterias</b>", "Infeccion urinaria"),
          ("Sedimento limpio + AKI", "Prerrenal o postrenal")],
         "Tira positiva a sangre sin eritrocitos en el sedimento = mioglobinuria (rabdomiolisis) o hemoglobinuria."),
    D + ["ego"])

add(deck_d, caso("Indices urinarios (FeNa, Na urinario) en AKI"),
    disc("Separar la AKI prerrenal de la NTA.",
         [("<b>FeNa &lt;1%</b>, Na urinario &lt;20, orina concentrada", "Prerrenal (responde a volumen)"),
          ("<b>FeNa &gt;2%</b>, Na urinario &gt;40, orina isostenurica", "NTA (intrinseca)"),
          ("FeNa baja pero no responde a volumen", "Considera sx hepatorrenal / cardiorrenal")],
         "El diuretico invalida la FeNa (usa FeUrea). La FeNa baja tambien aparece en glomerulonefritis y contraste."),
    D + ["indices_urinarios"])

add(deck_d, caso("Indices de la anemia (VCM, ferritina, reticulocitos)"),
    disc("Clasificar la anemia para dirigir el estudio.",
         [("<b>VCM bajo</b> + ferritina baja", "Ferropenica"),
          ("VCM bajo/normal + <b>ferritina normal/alta</b>", "Enfermedad cronica"),
          ("<b>VCM alto</b> + neutrofilos hipersegmentados", "Megaloblastica (B12/folato)"),
          ("Reticulocitos <b>altos</b>", "Hemolisis / sangrado (perdida)"),
          ("Reticulocitos <b>bajos</b>", "Falla de produccion")],
         "La ferritina es reactante de fase aguda: puede estar 'normal' y aun haber ferropenia con inflamacion (mira saturacion)."),
    D + ["indices_anemia"])


# ===================== PANELES (8) =====================
P = ["panel"]
add(deck_p, caso("Panel del SCA / dolor toracico"),
    panel("<b>ECG seriado</b> (en &lt;10 min) + <b>troponina de alta sensibilidad seriada</b>, BH, "
          "electrolitos, funcion renal, glucosa, lipidos; Rx de torax. Ecocardiograma si dudas.",
          "Diagnosticos que matan: TEP, diseccion (angio-TAC si sospecha), neumotorax, pericarditis/taponamiento.",
          "ECG + troponina definen CEST vs SEST. Troponina elevada es inespecifica: integra con la clinica y la curva."),
    P + ["sca"])

add(deck_p, caso("Panel de insuficiencia cardiaca"),
    panel("<b>BNP/NT-proBNP</b>, <b>ecocardiograma</b> (FEVI: FEr vs FEp), ECG, Rx de torax (congestion), "
          "BH, electrolitos, funcion renal/hepatica, TSH, ferritina (deficit de hierro), troponina.",
          "Desencadenante: isquemia, arritmia, infeccion, transgresion, mala adherencia, anemia, tiroides.",
          "La FEVI separa el tratamiento (FEr = 4 pilares; FEp = iSGLT2 + comorbilidades). BNP bajo descarta IC."),
    P + ["ic"])

add(deck_p, caso("Panel de la cetoacidosis diabetica / EHH"),
    panel("<b>Glucemia</b>, <b>gasometria</b> (pH, HCO3), <b>cetonas</b> (beta-hidroxibutirato), "
          "<b>electrolitos seriados (K!)</b> y <b>brecha anionica</b>, osmolaridad, funcion renal, EGO, "
          "cultivos/ECG/Rx para buscar el gatillo.",
          "Desencadenante (infeccion, omision de insulina, SCA, debut). Vigilar K y brecha durante el tratamiento.",
          "CAD = hiperglucemia + cetosis + acidosis con brecha. EHH = hiperosmolaridad sin cetoacidosis. "
          "El K total esta bajo aunque el serico parezca normal."),
    P + ["cad_ehh"])

add(deck_p, caso("Panel de la lesion renal aguda (AKI)"),
    panel("<b>Creatinina/urea seriadas</b>, electrolitos (K!), gasometria, <b>EGO + sedimento</b>, "
          "<b>indices urinarios (FeNa)</b>, <b>USG renal y vesical</b> (descartar obstruccion), "
          "relacion proteina/creatinina; revisar farmacos.",
          "Prerrenal vs intrinseca (NTA, glomerular) vs postrenal; nefrotoxicos; indicaciones de dialisis.",
          "El USG renal descarta obstruccion (postrenal). FeNa &lt;1% = prerrenal; cilindros pardos = NTA; "
          "cilindros hematicos = glomerular."),
    P + ["aki"])

add(deck_p, caso("Panel de la hiponatremia"),
    panel("<b>Osmolaridad serica</b>, <b>osmolaridad y sodio urinarios</b>, evaluacion de la <b>volemia</b>, "
          "funcion renal/tiroidea/suprarrenal, glucosa (corregir), acido urico.",
          "Pseudohiponatremia (hiperglucemia, hiperlipidemia), SIADH, hipovolemia, ICC/cirrosis, hipotiroidismo, "
          "insuficiencia suprarrenal.",
          "Algoritmo: osmolaridad -> volemia -> Na urinario. SIADH = euvolemico, Osm urinaria alta, Na urinario alto."),
    P + ["hiponatremia"])

add(deck_p, caso("Panel del paciente cronico complejo / riesgo CV global"),
    panel("<b>Glucosa/HbA1c</b>, <b>perfil de lipidos</b>, <b>funcion renal + albuminuria (RAC)</b>, TA, IMC/perimetro "
          "abdominal, PFH (esteatosis), acido urico, ECG; calcular el <b>riesgo CV</b>.",
          "Sindrome metabolico, diabetes/prediabetes, ERC, MASLD, dano de organo blanco subclinico.",
          "El objetivo es integrar todos los factores en un riesgo global que define la intensidad (LDL, TA, "
          "iSGLT2/GLP-1). Prediabetes (HbA1c 5.7-6.4%) = ventana de prevencion."),
    P + ["cronico_complejo"])

add(deck_p, caso("Panel de la cirrosis descompensada"),
    panel("BH, <b>PFH + bilirrubina + albumina + INR</b> (MELD/Child-Pugh), funcion renal y electrolitos (Na, K), "
          "<b>paracentesis diagnostica</b> (PMN para PBE), amonio (si duda), EGD para varices, USG/alfa-feto (CHC).",
          "Descompensaciones: ascitis, PBE, sangrado variceal, encefalopatia, sindrome hepatorrenal; precipitante.",
          "Toda ascitis nueva o deterioro -> <b>paracentesis</b>: PMN &ge;250 = PBE. MELD/Child-Pugh estiman pronostico."),
    P + ["cirrosis"])

add(deck_p, caso("Panel del patron de pruebas hepaticas (transaminasas)"),
    panel("<b>AST, ALT, FA, GGT, bilirrubina</b> + <b>albumina e INR</b> (funcion sintetica). Segun patron: serologias "
          "virales, perfil metabolico, autoinmune, hierro/cobre, USG.",
          "Diferenciar <b>hepatocelular</b> (ALT/AST altas) de <b>colestasico</b> (FA/GGT altas) y la gravedad real "
          "(la funcion sintetica).",
          "<b>AST:ALT &gt;2</b> sugiere alcohol; ALT &gt;&gt; AST sugiere viral/MASLD; <b>FA + GGT</b> altas = colestasis. "
          "La albumina/INR miden la funcion, no las transaminasas."),
    P + ["transaminasas"])


# ===================== SIGNOS Y SCORES (18) =====================
M = ["signo_score"]
simple = [
    ("CHA2DS2-VASc", "Estima el riesgo embolico en <b>FA</b> y decide anticoagulacion (ICC, HTA, edad, DM, EVC previo, vascular, sexo).", "fa"),
    ("CURB-65", "Gravedad de la <b>neumonia</b> (Confusion, Urea &gt;7, FR &ge;30, TA baja, edad &ge;65) y decide sitio de manejo.", "nac"),
    ("Score de Wells (TEP/TVP)", "Probabilidad pretest de <b>TEP/TVP</b>; guia el uso del dimero D vs imagen directa.", "tep"),
    ("qSOFA", "Tamizaje de gravedad en infeccion: TAS &le;100, FR &ge;22, alteracion mental (&ge;2 = riesgo de sepsis).", "sepsis"),
    ("GRACE", "Estratifica riesgo en <b>SCASEST</b> y define la urgencia de la coronariografia.", "iamsest"),
    ("Killip", "Clasifica la <b>IC en el contexto del IAM</b> (I sin fallo a IV choque) y predice mortalidad.", "iamcest"),
    ("NYHA", "Clase funcional de la <b>insuficiencia cardiaca</b> por sintomas con el esfuerzo (I a IV).", "ic"),
    ("Child-Pugh / MELD", "Estiman gravedad/pronostico de la <b>cirrosis</b> (bilirrubina, albumina, INR, ascitis, encefalopatia / Cr, Na).", "cirrosis"),
    ("Maddrey (FD) / Lille", "Maddrey &ge;32 marca <b>hepatitis alcoholica grave</b> (corticoide); Lille evalua la respuesta al 7o dia.", "hepatitis_alcoholica"),
    ("Criterios de Duke", "Diagnostico de <b>endocarditis</b> (hemocultivos persistentes + hallazgos ecocardiograficos + criterios menores).", "endocarditis"),
    ("Frote pericardico", "Sonido aspero de 3 componentes = <b>pericarditis</b>; con elevacion ST difusa y descenso del PR.", "pericarditis"),
    ("Pulso parvus et tardus", "Pulso carotideo pequeno y retrasado + soplo eyectivo = <b>estenosis aortica</b> severa.", "estenosis_aortica"),
    ("Pulso paradojico / triada de Beck", "Caida de TAS &gt;10 mmHg en inspiracion; con Beck (hipotension, yugulares, ruidos velados) = <b>taponamiento</b>.", "pericarditis"),
    ("Signo de Kussmaul (respiracion)", "Respiracion rapida y profunda = compensacion de <b>acidosis metabolica</b> (CAD).", "cad"),
    ("Asterixis (flapping)", "Temblor 'de aleteo' al extender las manos = <b>encefalopatia</b> (hepatica, uremica, hipercapnica).", "encefalopatia"),
    ("Punopercusion renal (Giordano)", "Dolor al percutir la fosa renal = <b>pielonefritis</b> / patologia renal.", "pielonefritis"),
    ("Onda T picuda -> QRS ancho", "Progresion electrocardiografica de la <b>hiperkalemia</b> (riesgo de arritmia letal).", "hiperkalemia"),
    ("Onda U / aplanamiento de T", "Cambios en el ECG de la <b>hipokalemia</b>; riesgo de arritmia (mas con digoxina).", "hipokalemia"),
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
        os.path.join(OUTPUT_DIR, "No_Hay_Tiempo_MI_Estudios_TODOS.apkg"))
    print(f"  -> TODOS ({sum(len(d.notes) for d in [deck_d, deck_p, deck_m])} notas)")


if __name__ == "__main__":
    build()
