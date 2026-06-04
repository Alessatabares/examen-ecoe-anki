"""No hay tiempo / Cirugia — PILAR INTERROGATORIO (tronco + llaves).

Tronco contextual por motivo de consulta + llave que fija el dx.
Guia: ATLS, GPC mexicanas, Sabiston/Schwartz.
"""
import os
import genanki

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "output")
os.makedirs(OUTPUT_DIR, exist_ok=True)

MODEL_QA_ID = 1990006002
DECK_ID_T, DECK_ID_C, DECK_ID_M = 1990005011, 1990005012, 1990005013
DECK_NAME_T = "No hay tiempo::Cirugia::Interrogatorio::1 - Troncos (ejes)"
DECK_NAME_C = "No hay tiempo::Cirugia::Interrogatorio::2 - Llaves comunes (core)"
DECK_NAME_M = "No hay tiempo::Cirugia::Interrogatorio::3 - Llaves menos comunes"

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
model_qa = genanki.Model(MODEL_QA_ID, "NHT Cir Interrogatorio QA",
    fields=[{"name": "Front"}, {"name": "Back"}],
    templates=[{"name": "QA", "qfmt": "{{Front}}", "afmt": '{{Front}}<hr id="extra">{{Back}}'}],
    css=CSS_BASE)

deck_t = genanki.Deck(DECK_ID_T, DECK_NAME_T)
deck_c = genanki.Deck(DECK_ID_C, DECK_NAME_C)
deck_m = genanki.Deck(DECK_ID_M, DECK_NAME_M)
BASE_TAGS = ["cirugia", "ecoe", "no_hay_tiempo", "interrogatorio"]


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
add(deck_t, caso("TRONCO — Trauma (ATLS)"),
    tronco("<b>Mecanismo</b> (cinetico/penetrante, velocidad, altura, arma), tiempo de evolucion, "
           "<b>ABCDE</b> y signos vitales, sangrados visibles, <b>AMPLIA</b> (alergias, medicamentos, patologia, "
           "ultima ingesta, ambiente).",
           "<b>Inestable</b> &rarr; quirofano segun foco. <b>B comprometido</b> &rarr; tension/hemotorax/tamponade. "
           "<b>C sin foco externo</b> &rarr; sangrado interno (torax/abdomen/pelvis)."),
    T + ["trauma"])

add(deck_t, caso("TRONCO — Dolor abdominal agudo"),
    tronco("<b>Inicio</b> (subito vs gradual), <b>localizacion y migracion</b>, caracter (colico vs continuo), "
           "irradiacion, relacion con comida, nausea/vomito, <b>transito y canalizacion de gases</b>, fiebre, "
           "ultima menstruacion/embarazo, cirugias previas, AINEs/alcohol.",
           "<b>Migra a FID</b> &rarr; apendicitis. <b>HD + Murphy</b> &rarr; colecistitis. <b>En barra a espalda</b> "
           "&rarr; pancreatitis. <b>Colico + distension + no canaliza</b> &rarr; obstruccion. "
           "<b>Desproporcionado</b> &rarr; isquemia."),
    T + ["dolor_abdominal"])

add(deck_t, caso("TRONCO — Hemorragia digestiva"),
    tronco("<b>Forma:</b> hematemesis/posos de cafe (alta) vs <b>melena</b> (alta) vs <b>hematoquecia</b> (baja o alta "
           "masiva). Cantidad, <b>hemodinamia</b> (mareo, sincope), <b>AINEs, alcohol, hepatopatia/varices</b>, "
           "anticoagulantes, episodios previos.",
           "<b>Hematemesis/melena + AINEs</b> &rarr; ulcera. <b>+ hepatopatia/estigmas</b> &rarr; varices. "
           "<b>Hematoquecia en mayor</b> &rarr; diverticulos/angiodisplasia/neoplasia (HDB)."),
    T + ["hda_hdb"])

add(deck_t, caso("TRONCO — Dolor toracico / disnea subita (no coronario)"),
    tronco("Inicio y caracter del dolor, <b>trauma?</b>, disnea, <b>asimetria de pulsos/TA</b>, antecedente de "
           "EPOC/altos delgados (neumotorax), HTA/Marfan (diseccion), inmovilizacion (TEP).",
           "<b>Subito + hipoxia + ausencia de ruidos</b> &rarr; neumotorax (tension si inestable). "
           "<b>Desgarrante a espalda + asimetria de pulsos</b> &rarr; diseccion aortica. "
           "<b>Trauma + Beck</b> &rarr; tamponade."),
    T + ["torax"])

add(deck_t, caso("TRONCO — Obstruccion intestinal"),
    tronco("<b>Dolor colico</b>, <b>distension</b>, <b>vomito</b> (precoz/biliar = alto; tardio/fecaloide = bajo), "
           "<b>ausencia de canalizacion de gases y heces</b>, <b>cirugias abdominales previas</b> (bridas), hernias, "
           "cambio del habito/sangrado (neoplasia).",
           "<b>Cirugia previa</b> &rarr; bridas. <b>Hernia dolorosa</b> &rarr; incarcerada. "
           "<b>Mayor + cambio de habito</b> &rarr; neoplasia. <b>Continuo + fiebre + lactato</b> &rarr; estrangulacion."),
    T + ["obstruccion"])

add(deck_t, caso("TRONCO — Dolor escrotal / pelvico subito (torsiones)"),
    tronco("<b>Inicio subito</b>, intensidad, nausea/vomito, trauma, episodios previos autolimitados, en mujer "
           "<b>ultima menstruacion y posibilidad de embarazo</b>, masa anexial conocida.",
           "<b>Escroto: dolor subito + reflejo cremasterico ausente</b> &rarr; torsion testicular. "
           "<b>Mujer: dolor subito + masa anexial</b> &rarr; torsion ovarica / ectopico (si embarazo + hipotension &rarr; roto)."),
    T + ["torsiones"])

add(deck_t, caso("TRONCO — Fiebre + foco / sospecha de sepsis"),
    tronco("Foco probable (herida, absceso, via, abdomen, urinario, piel), tiempo, <b>hemodinamia</b> "
           "(TA, FC, FR, estado mental), <b>qSOFA</b>, inmunosupresion/diabetes, dispositivos/cirugias recientes.",
           "<b>qSOFA &ge;2</b> &rarr; sepsis (bundle). <b>Dolor desproporcionado + crepitos + ampollas</b> &rarr; "
           "fascitis. <b>Coleccion localizada</b> &rarr; absceso (drenar)."),
    T + ["sepsis"])


# ===================== LLAVES CORE (18) =====================
C = ["core"]
add(deck_c, caso("Dolor que empezo periumbilical y MIGRO a fosa iliaca derecha"),
    llave("&iquest;El dolor <b>empezo en el ombligo y bajo a la derecha</b>? &iquest;anorexia, nausea, febricula?",
          "Migracion + dolor en McBurney + Blumberg/Rovsing/psoas + leucocitosis.",
          "Apendicitis aguda"),
    C + ["apendicitis"])

add(deck_c, caso("Dolor en hipocondrio derecho tras comida grasa"),
    llave("&iquest;Dolor en HD que <b>detiene la inspiracion</b> al palpar (Murphy)? &iquest;tras grasas? &iquest;fiebre?",
          "Murphy+, dolor HD, fiebre/leucocitosis, USG con pared engrosada y litos.",
          "Colecistitis aguda"),
    C + ["colecistitis"])

add(deck_c, caso("Ictericia + fiebre con escalofrios + dolor HD"),
    llave("&iquest;<b>Fiebre con escalofrios + ictericia + dolor</b> (Charcot)? &iquest;+ hipotension/confusion (Reynolds)?",
          "Triada de Charcot + colestasis (BT/FA altas) + via biliar dilatada; grave si pentada.",
          "Colangitis aguda"),
    C + ["colangitis"])

add(deck_c, caso("Dolor epigastrico en barra que irradia a la espalda"),
    llave("&iquest;Dolor <b>en barra hacia la espalda</b> que mejora inclinado adelante? &iquest;alcohol o litiasis? &iquest;vomito?",
          "Dolor epigastrico transfixiante + <b>lipasa &gt;3x</b>; causa biliar o alcoholica.",
          "Pancreatitis aguda"),
    C + ["pancreatitis"])

add(deck_c, caso("Dolor en fosa iliaca IZQUIERDA en adulto mayor"),
    llave("&iquest;Dolor en <b>FII</b>, cambio del habito, fiebre? &iquest;episodios previos? (la 'apendicitis izquierda')",
          "Dolor FII + fiebre + leucocitosis; TAC con engrosamiento/diverticulos &plusmn; absceso.",
          "Diverticulitis aguda"),
    C + ["diverticulitis"])

add(deck_c, caso("Dolor colico + distension + no canaliza gases"),
    llave("&iquest;<b>Vomito, distension y no expulsa gases ni heces</b>? &iquest;cirugias previas o hernias?",
          "Dolor colico + distension + RHA metalicos (luego ausentes) + niveles en Rx.",
          "Obstruccion intestinal"),
    C + ["obstruccion"])

add(deck_c, caso("Dolor abdominal subito e intenso + abdomen en tabla"),
    llave("&iquest;Dolor <b>brusco e intensisimo</b> con <b>rigidez de todo el abdomen</b>? &iquest;ulcera/AINEs?",
          "Abdomen en tabla + ausencia de matidez hepatica; <b>neumoperitoneo</b> en Rx de pie.",
          "Perforacion de viscera hueca"),
    C + ["perforacion"])

add(deck_c, caso("Vomito con sangre o posos de cafe + melena"),
    llave("&iquest;<b>Hematemesis/posos + heces negras</b>? &iquest;<b>AINEs</b>, epigastralgia, H. pylori?",
          "Hematemesis/melena en consumidor de AINEs; endoscopia con ulcera (clasificacion de Forrest).",
          "HDA por ulcera peptica"),
    C + ["hda_ulcera"])

add(deck_c, caso("Hematemesis abundante en paciente con hepatopatia"),
    llave("&iquest;<b>Estigmas de hepatopatia</b> (ascitis, ictericia, circulacion colateral)? &iquest;alcohol? &iquest;varices conocidas?",
          "Hematemesis franca + hipertension portal; endoscopia con varices esofagicas sangrantes.",
          "HDA por varices esofagicas"),
    C + ["hda_varices"])

add(deck_c, caso("Sangrado rojo por el recto"),
    llave("&iquest;<b>Sangre roja por el ano</b>? &iquest;edad/cambio de habito? &iquest;mareo (descartar HDA masiva)?",
          "Hematoquecia; en mayor pensar diverticulos/angiodisplasia/neoplasia; colonoscopia.",
          "Hemorragia digestiva baja"),
    C + ["hdb"])

add(deck_c, caso("Trauma toracico + hipotension + yugulares ingurgitadas + sin ruidos de un lado"),
    llave("&iquest;<b>Disnea subita + hipotension + ausencia de ruidos + traquea desviada</b>?",
          "Insuficiencia respiratoria + colapso hemodinamico tras trauma; dx CLINICO.",
          "Neumotorax a tension"),
    C + ["neumotorax_tension"])

add(deck_c, caso("Trauma toracico + Beck (hipotension, yugulares, ruidos velados)"),
    llave("&iquest;<b>Hipotension + ingurgitacion yugular + ruidos cardiacos velados</b> tras trauma penetrante?",
          "Triada de Beck; FAST con liquido pericardico.",
          "Taponamiento cardiaco"),
    C + ["tamponade"])

add(deck_c, caso("Trauma toracico + hipotension + matidez y sin ruidos de un hemitorax"),
    llave("&iquest;<b>Matidez + ausencia de ruidos</b> de un lado + shock? (vs timpanismo del neumotorax)",
          "Hemitorax mate, hipoventilado, con shock hemorragico; sale sangre por el tubo.",
          "Hemotorax masivo"),
    C + ["hemotorax"])

add(deck_c, caso("Taquicardia + hipotension + palidez + oliguria"),
    llave("&iquest;Signos de <b>mala perfusion</b> (taquicardia, hipotension, llenado lento, oliguria, confusion)? &iquest;origen del sangrado?",
          "Choque clase III-IV; buscar foco (torax, abdomen, pelvis, huesos largos, externo).",
          "Choque hipovolemico"),
    C + ["choque"])

add(deck_c, caso("Dolor abdominal/lumbar subito + masa pulsatil + hipotension"),
    llave("&iquest;<b>Masa abdominal pulsatil</b> + dolor + hipotension en mayor con factores vasculares?",
          "Triada de AAA roto; USG/TAC con aneurisma; si inestable, no esperar imagen.",
          "Aneurisma de aorta abdominal roto"),
    C + ["aaa"])

add(deck_c, caso("Dolor abdominal DESPROPORCIONADO a la exploracion"),
    llave("&iquest;Dolor intensisimo con <b>abdomen casi normal a la palpacion</b>? &iquest;FA/embolismo? &iquest;lactato alto?",
          "Dolor desproporcionado + lactato elevado + factor embolico; angio-TAC confirma.",
          "Isquemia mesenterica aguda"),
    C + ["isquemia_mesenterica"])

add(deck_c, caso("Abdomen rigido y doloroso difusamente + afectacion sistemica"),
    llave("&iquest;<b>Rebote difuso, rigidez y mal estado general</b>? &iquest;origen (perforacion, isquemia, absceso roto)?",
          "Irritacion peritoneal generalizada + datos sistemicos (fiebre, taquicardia, leucocitosis).",
          "Peritonitis"),
    C + ["peritonitis"])

add(deck_c, caso("Fiebre + hipotension + taquipnea + confusion con un foco infeccioso"),
    llave("&iquest;<b>qSOFA &ge;2</b> (TAS &le;100, FR &ge;22, alteracion mental)? &iquest;cual es el foco?",
          "Disfuncion organica por infeccion; lactato alto y/o hipotension que requiere vasopresor (choque septico).",
          "Sepsis / choque septico"),
    C + ["sepsis"])


# ===================== LLAVES MENOS (17) =====================
M = ["menos_comun"]
pares = [
    ("Herida penetrante abdominal", "&iquest;<b>Inestable, eviscera o tiene peritonitis</b>? &iquest;arma de fuego o blanca?",
     "Inestabilidad/evisceracion/peritonitis = quirofano; estable = TAC y manejo selectivo.", "Trauma penetrante", "trauma_penetrante"),
    ("Trauma cerrado de abdomen", "&iquest;Mecanismo de alta energia? &iquest;estable o inestable? &iquest;dolor/distension?",
     "Inestable + FAST+ = laparotomia; estable = TAC; sospecha de lesion de organo solido.", "Trauma cerrado", "trauma_cerrado"),
    ("Dolor referido al hombro izquierdo tras trauma", "&iquest;Dolor en <b>hombro izquierdo</b> (Kehr) + trauma de flanco/costal izq?",
     "Sangre subdiafragmatica irrita el frenico; lesion esplenica.", "Lesion esplenica (Kehr)", "esplenica"),
    ("Segmento del torax que se mueve al reves", "&iquest;<b>Movimiento paradojico</b> de la pared + multiples costillas rotas?",
     "Volet costal; el riesgo real es la contusion pulmonar subyacente.", "Torax inestable", "torax_inestable"),
    ("Trauma de pelvis con inestabilidad hemodinamica", "&iquest;Dolor/inestabilidad del anillo pelvico + hipotension?",
     "Fractura pelvica sangrante; faja pelvica + reanimacion + angioembolizacion.", "Fractura pelvica", "fractura_pelvica"),
    ("Distension + dolor colico + Rx en 'grano de cafe'", "&iquest;Adulto mayor/encamado, estrenimiento, distension marcada?",
     "Asa sigmoidea torcida (grano de cafe); descompresion endoscopica.", "Volvulo de sigmoides", "volvulo"),
    ("Bulto inguinal doloroso que ya no entra", "&iquest;El bulto <b>no se reduce</b>, duele, esta rojo? &iquest;vomito/no canaliza?",
     "Hernia incarcerada/estrangulada; cirugia urgente (no reducir si estrangulada).", "Hernia complicada", "hernia"),
    ("Distension sin dolor colico tras cirugia", "&iquest;Posoperatorio/opioides/hipokalemia? &iquest;RHA <b>ausentes</b> sin punto de obstruccion?",
     "Ileo paralitico (funcional), no mecanico; tratar la causa.", "Ileo paralitico", "ileo"),
    ("Obstruccion con dolor continuo y deterioro rapido", "&iquest;Dolor que pasa de colico a <b>continuo</b> + fiebre + lactato?",
     "Asa cerrada/estrangulacion; isquemia rapida, urgencia quirurgica.", "Asa cerrada / estrangulacion", "asa_cerrada"),
    ("Fiebre persistente + coleccion localizada", "&iquest;Fiebre en picos tras cirugia/infeccion + masa dolorosa localizada?",
     "Absceso (coleccion encapsulada); drenaje guiado por imagen.", "Absceso intraabdominal", "absceso"),
    ("Dolor desproporcionado + crepitos + ampollas", "&iquest;Dolor extremo, <b>crepitos</b>, ampollas, necrosis, mal estado?",
     "Fascitis necrotizante; desbridamiento quirurgico urgente.", "Fascitis necrotizante", "fascitis"),
    ("Extremidad con tejido negro / gas", "&iquest;Tejido necrotico, mal olor, gas? &iquest;isquemica o infecciosa (Clostridium)?",
     "Gangrena; retirar tejido no viable; gaseosa = urgencia quirurgica.", "Gangrena", "gangrena"),
    ("Dolor testicular subito en adolescente", "&iquest;<b>Inicio brusco</b>, nausea, <b>reflejo cremasterico ausente</b>, teste elevado?",
     "Torsion testicular; ventana ~6 h, cirugia inmediata.", "Torsion testicular", "torsion_testicular"),
    ("Dolor pelvico subito + masa anexial en mujer", "&iquest;Inicio brusco, nausea/vomito, masa anexial, quiste conocido?",
     "Torsion ovarica; Doppler puede ser normal, la sospecha indica cirugia.", "Torsion ovarica", "torsion_ovarica"),
    ("Dolor toracico desgarrante que migra a la espalda", "&iquest;Dolor <b>'que rasga'</b> + <b>asimetria de pulsos/TA</b> + HTA/Marfan?",
     "Diseccion aortica; mediastino ancho; tipo A quirurgica, B medica.", "Diseccion aortica", "diseccion_aortica"),
    ("Dolor desproporcionado en extremidad con yeso/trauma", "&iquest;Dolor que aumenta al <b>estirar pasivamente</b> + parestesias + tension?",
     "Sindrome compartimental; fasciotomia (no esperar ausencia de pulso).", "Sindrome compartimental", "compartimental"),
    ("Mujer en edad fertil con dolor + hipotension", "&iquest;<b>Prueba de embarazo</b>? &iquest;atraso menstrual + dolor + mareo?",
     "Ectopico roto con hemoperitoneo; FAST+; cirugia urgente.", "Ectopico roto", "ectopico"),
]
for titulo, p, pat, dx, tag in pares:
    add(deck_m, caso(titulo), llave(p, pat, dx), M + [tag])


def build():
    for d, f in [(deck_t, "Interrogatorio_01_Troncos.apkg"), (deck_c, "Interrogatorio_02_Llaves_core.apkg"),
                 (deck_m, "Interrogatorio_03_Llaves_menos.apkg")]:
        genanki.Package(d).write_to_file(os.path.join(OUTPUT_DIR, f))
        print(f"  -> {f} ({len(d.notes)} notas)")
    genanki.Package([deck_t, deck_c, deck_m]).write_to_file(
        os.path.join(OUTPUT_DIR, "No_Hay_Tiempo_Cir_Interrogatorio_TODOS.apkg"))
    print(f"  -> TODOS ({sum(len(d.notes) for d in [deck_t, deck_c, deck_m])} notas)")


if __name__ == "__main__":
    build()
