"""No hay tiempo / Cirugia — PILAR EXPLORACION + ESTUDIOS.

A) DISCRIMINADOR: una herramienta separa un grupo por un hallazgo (por herramienta).
B) PANEL/workup: una entidad pide una bateria con rol de cada estudio (por enfermedad).
Guia: ATLS, GPC mexicanas, Sabiston/Schwartz, Tokyo, Surviving Sepsis.
"""
import os
import genanki

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "output")
os.makedirs(OUTPUT_DIR, exist_ok=True)

MODEL_QA_ID = 1990006003
DECK_ID_D, DECK_ID_P, DECK_ID_M = 1990005021, 1990005022, 1990005023
DECK_NAME_D = "No hay tiempo::Cirugia::Estudios::1 - Discriminadores (herramienta)"
DECK_NAME_P = "No hay tiempo::Cirugia::Estudios::2 - Paneles (por entidad)"
DECK_NAME_M = "No hay tiempo::Cirugia::Estudios::3 - Signos y scores"

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
model_qa = genanki.Model(MODEL_QA_ID, "NHT Cir Estudios QA",
    fields=[{"name": "Front"}, {"name": "Back"}],
    templates=[{"name": "QA", "qfmt": "{{Front}}", "afmt": '{{Front}}<hr id="extra">{{Back}}'}],
    css=CSS_BASE)

deck_d = genanki.Deck(DECK_ID_D, DECK_NAME_D)
deck_p = genanki.Deck(DECK_ID_P, DECK_NAME_P)
deck_m = genanki.Deck(DECK_ID_M, DECK_NAME_M)
BASE_TAGS = ["cirugia", "ecoe", "no_hay_tiempo", "estudios"]


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
add(deck_d, caso("eFAST (ecografia en trauma)"),
    disc("En el paciente inestable: buscar sangre/aire que obligue a quirofano sin salir de la sala.",
         [("<b>Liquido libre</b> en Morrison/esplenorrenal/Douglas", "Hemoperitoneo"),
          ("<b>Liquido pericardico</b>", "Taponamiento"),
          ("<b>Ausencia de deslizamiento pleural</b> / lung point", "Neumotorax"),
          ("Derrame pleural (sangre)", "Hemotorax")],
         "FAST <b>+</b> e inestable = quirofano. FAST <b>-</b> NO descarta lesion de viscera hueca ni retroperitoneo."),
    D + ["fast"])

add(deck_d, caso("Rx de torax en trauma / disnea"),
    disc("Identificar lesiones de la B y vasculares mayores.",
         [("Hemitorax <b>hiperclaro</b> + colapso pulmonar (&plusmn; desviacion)", "Neumotorax (tension si clinico)"),
          ("Hemitorax <b>opaco</b> con menisco", "Hemotorax"),
          ("<b>Mediastino ancho</b> (&gt;8 cm)", "Lesion aortica / diseccion"),
          ("Aire bajo el diafragma", "Neumoperitoneo (perforacion)")],
         "El neumotorax a tension es <b>clinico</b>: no esperes la Rx para descomprimir."),
    D + ["rx_torax"])

add(deck_d, caso("Rx de abdomen (de pie y decubito)"),
    disc("Tamizar obstruccion, perforacion y volvulo.",
         [("<b>Niveles hidroaereos</b> + asas dilatadas", "Obstruccion intestinal"),
          ("<b>Aire libre subdiafragmatico</b> (de pie)", "Perforacion (neumoperitoneo)"),
          ("Imagen en <b>grano de cafe</b>", "Volvulo de sigmoides"),
          ("<b>Asa centinela</b> / colon cortado", "Pancreatitis / ileo localizado")],
         "Rx normal NO descarta patologia: ante alta sospecha, TAC."),
    D + ["rx_abdomen"])

add(deck_d, caso("TAC de abdomen con contraste"),
    disc("Caracterizar el abdomen agudo en el paciente ESTABLE.",
         [("Apendice &gt;6 mm, grasa peri-apendicular inflamada", "Apendicitis"),
          ("Engrosamiento colon izq + diverticulos &plusmn; absceso/aire", "Diverticulitis (Hinchey)"),
          ("<b>Neumatosis, falta de realce, gas portal</b>", "Isquemia mesenterica"),
          ("Coleccion con realce periferico", "Absceso"),
          ("Extravasacion de contraste", "Sangrado activo")],
         "No mandes al TAC al inestable: estabiliza o lleva a quirofano primero."),
    D + ["tac"])

add(deck_d, caso("Exploracion abdominal: signos"),
    disc("Localizar el foco y detectar irritacion peritoneal.",
         [("<b>McBurney + Blumberg + Rovsing + psoas</b>", "Apendicitis"),
          ("<b>Murphy</b> (detiene la inspiracion)", "Colecistitis"),
          ("<b>Defensa involuntaria + rigidez + rebote difuso</b>", "Peritonitis -> quirofano"),
          ("<b>Cullen / Grey-Turner</b> (equimosis periumbilical / flancos)", "Hemorragia retroperitoneal / pancreatitis grave")],
         "Defensa involuntaria que NO cede al distraer = peritonismo real."),
    D + ["signos"])

add(deck_d, caso("Lactato + gasometria"),
    disc("Medir hipoperfusion/gravedad y orientar isquemia.",
         [("<b>Lactato elevado</b> + acidosis metabolica", "Hipoperfusion / shock"),
          ("Lactato muy alto + dolor desproporcionado", "Isquemia mesenterica / estrangulacion"),
          ("Deficit de base negativo", "Gravedad del shock hemorragico"),
          ("Lactato que NO aclara con reanimacion", "Mal pronostico / foco no controlado")],
         "Lactato normal no descarta isquemia temprana; reevalua si la clinica persiste."),
    D + ["lactato"])

add(deck_d, caso("SNG + tacto rectal"),
    disc("Orientar el nivel de la hemorragia digestiva y descomprimir.",
         [("Aspirado por SNG con <b>sangre/posos</b>", "HDA confirmada"),
          ("<b>Melena</b> en el tacto", "Sangrado alto (digerido)"),
          ("<b>Hematoquecia</b>", "HDB (o HDA masiva si inestable)"),
          ("SNG: gran debito en obstruccion", "Descompresion (alta)")],
         "Aspirado por SNG limpio no descarta HDA por completo (sangrado pospilorico)."),
    D + ["sng_tacto"])

add(deck_d, caso("Eco Doppler (torsion testicular / ovarica)"),
    disc("Valorar flujo del organo ante dolor subito.",
         [("Testiculo <b>sin flujo</b> Doppler + dolor subito", "Torsion testicular"),
          ("Ovario <b>aumentado, edematoso, flujo ausente/disminuido</b>", "Torsion ovarica"),
          ("Aumento de flujo (hiperemia)", "Epididimitis / orquitis (no torsion)")],
         "Si la clinica de torsion es clara, la <b>cirugia no espera al Doppler</b> (puede ser normal)."),
    D + ["doppler"])


# ===================== PANELES (8) =====================
P = ["panel"]
add(deck_p, caso("Panel del paciente con trauma (ATLS)"),
    panel("<b>eFAST</b>, <b>Rx torax y pelvis</b>, gasometria + <b>lactato</b>, BH, <b>grupo y cruzar</b>, "
          "coagulacion, beta-hCG en mujer fertil; <b>TAC</b> de cuerpo si estable.",
          "Lesiones que matan en el primary survey; hemorragia oculta (torax/abdomen/pelvis/huesos).",
          "<b>Inestable = quirofano</b> guiado por FAST/Rx; el TAC es solo para el estable."),
    P + ["trauma"])

add(deck_p, caso("Panel de pancreatitis aguda"),
    panel("<b>Lipasa (&gt;3x)</b>, BH, PFH (causa biliar), <b>calcio, trigliceridos</b>, glucosa, LDH, PCR; "
          "<b>USG</b> (litiasis) y <b>TAC con contraste a las 72 h</b> si dudas/gravedad.",
          "Gravedad por falla organica (las primeras 48 h); necrosis infectada (tardia).",
          "Dx con 2 de 3: clinica + lipasa &gt;3x + imagen. <b>No</b> pidas TAC de entrada en la leve."),
    P + ["pancreatitis"])

add(deck_p, caso("Panel biliar / colangitis"),
    panel("BH, <b>PFH patron colestasico</b> (BT, FA, GGT), lipasa, <b>USG</b> (litos, dilatacion de via), "
          "<b>colangioRM/CPRE</b> segun probabilidad de coledocolitiasis.",
          "Colecistitis vs colangitis vs coledocolitiasis vs pancreatitis biliar.",
          "Colangitis = infeccion + obstruccion &rarr; <b>CPRE</b> (dx y terapeutica: descompresion)."),
    P + ["biliar"])

add(deck_p, caso("Panel de sepsis (bundle de 1 hora)"),
    panel("<b>Lactato</b>, <b>2 hemocultivos antes del antibiotico</b> + cultivos del foco, BH, PCR/PCT, "
          "funcion renal/hepatica, coagulacion, gasometria. Imagen del foco.",
          "Identificar y controlar el FOCO (absceso, viscera, via, tejido).",
          "Bundle 1 h: lactato + cultivos + antibiotico + 30 mL/kg cristaloide + vasopresor si TAM &lt;65."),
    P + ["sepsis"])

add(deck_p, caso("Panel de hemorragia / transfusion masiva"),
    panel("<b>BH</b> (Hb seriada), <b>grupo y cruzar</b>, <b>coagulacion + fibrinogeno + plaquetas</b>, gasometria/"
          "lactato, calcio (citrato). Tromboelastografia si disponible.",
          "Triada letal: hipotermia + acidosis + coagulopatia; foco del sangrado.",
          "Protocolo masivo <b>1:1:1</b> (plasma:plaquetas:concentrados) + <b>TXA &lt;3 h</b> + hipotension permisiva."),
    P + ["transfusion"])

add(deck_p, caso("Panel del abdomen agudo (cajon general)"),
    panel("<b>BH, PCR</b>, <b>lactato</b>, <b>amilasa/lipasa</b>, PFH, EGO, electrolitos/funcion renal, "
          "<b>beta-hCG en mujer fertil</b>; imagen segun sospecha (USG/TAC, Rx si perforacion/obstruccion).",
          "Causas medicas que imitan (cetoacidosis, IAM inferior, neumonia basal); embarazo/ectopico.",
          "<b>beta-hCG SIEMPRE</b> en mujer fertil con dolor abdominal antes de imagen/cirugia."),
    P + ["abdomen_agudo"])

add(deck_p, caso("Panel vascular (AAA / diseccion aortica)"),
    panel("<b>Angio-TAC</b> (estudio de eleccion si estable), USG abdominal a pie de cama (AAA), ECG + troponina "
          "(dif. con SICA), grupo y cruzar, BH y coagulacion.",
          "Diferenciar de SICA, TEP, colico renal; rotura inminente.",
          "<b>Inestable con AAA = quirofano sin TAC.</b> En diseccion, controlar FC/TA antes del traslado."),
    P + ["vascular"])

add(deck_p, caso("Panel de obstruccion intestinal"),
    panel("<b>Rx de abdomen</b> (niveles), <b>TAC con contraste</b> (nivel, causa, asa cerrada, isquemia), "
          "electrolitos/funcion renal (vomito), BH, <b>lactato</b> si sospecha de estrangulacion.",
          "Estrangulacion/isquemia (lactato, fiebre, peritonismo); causa (bridas, hernia, neoplasia).",
          "El TAC distingue <b>simple vs estrangulada/asa cerrada</b> (cambia a cirugia urgente)."),
    P + ["obstruccion"])


# ===================== SIGNOS Y SCORES (17) =====================
M = ["signo_score"]
simple = [
    ("Signo de Blumberg (rebote)", "Dolor al <b>retirar</b> bruscamente la mano = irritacion peritoneal.", "signos"),
    ("Signo de Rovsing", "Dolor en <b>FID</b> al palpar la FII = apendicitis.", "apendicitis"),
    ("Signo del psoas / obturador", "Dolor al extender el muslo (psoas) o rotar la cadera (obturador) = apendice irritando.", "apendicitis"),
    ("Signo de Murphy", "Detencion de la inspiracion al palpar el HD bajo el reborde = colecistitis.", "colecistitis"),
    ("Cullen / Grey-Turner", "Equimosis <b>periumbilical (Cullen)</b> o en <b>flancos (Grey-Turner)</b> = hemorragia retroperitoneal (pancreatitis grave, ectopico, AAA).", "signos"),
    ("Neumoperitoneo en Rx", "<b>Aire libre subdiafragmatico</b> en Rx de pie = perforacion de viscera hueca.", "perforacion"),
    ("Niveles hidroaereos", "Asas dilatadas con niveles en escalera = obstruccion intestinal.", "obstruccion"),
    ("Imagen en grano de cafe", "Asa sigmoidea torcida y distendida = volvulo de sigmoides.", "volvulo"),
    ("Mediastino ancho (&gt;8 cm)", "En Rx de torax tras trauma/dolor desgarrante = lesion/diseccion aortica.", "diseccion_aortica"),
    ("Triada de Beck", "Hipotension + ingurgitacion yugular + ruidos velados = <b>taponamiento</b>.", "tamponade"),
    ("Triada de Charcot / pentada de Reynolds", "Fiebre+ictericia+dolor (Charcot) &plusmn; hipotension+confusion (Reynolds) = <b>colangitis</b>.", "colangitis"),
    ("Escala de Alvarado", "Puntua probabilidad de <b>apendicitis</b> (migracion, anorexia, nausea, dolor FID, rebote, fiebre, leucocitosis, neutrofilia).", "apendicitis"),
    ("Clasificacion de Forrest", "Estratifica la ulcera sangrante por endoscopia y predice <b>resangrado</b> (Ia chorro... III base limpia).", "hda_ulcera"),
    ("Gravedad de pancreatitis (Ranson/BISAP/APACHE)", "Estratifican riesgo; <b>BISAP</b> es rapida (BUN, alterado, SIRS, edad, derrame).", "pancreatitis"),
    ("Clasificacion de Hinchey", "Gradua la <b>diverticulitis complicada</b> (absceso a peritonitis fecal) y guia drenaje vs cirugia.", "diverticulitis"),
    ("LRINEC", "Score de laboratorio que apoya la sospecha de <b>fascitis necrotizante</b> (PCR, leucocitos, Na, glucosa, Cr, Hb).", "fascitis"),
    ("Lactato como marcador", "Elevado = hipoperfusion/isquemia; su <b>aclaramiento</b> con la reanimacion es pronostico.", "lactato"),
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
        os.path.join(OUTPUT_DIR, "No_Hay_Tiempo_Cir_Estudios_TODOS.apkg"))
    print(f"  -> TODOS ({sum(len(d.notes) for d in [deck_d, deck_p, deck_m])} notas)")


if __name__ == "__main__":
    build()
