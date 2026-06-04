"""No hay tiempo / Obstetricia — PILAR INTERROGATORIO (tronco + llaves).

Tronco contextual por motivo de consulta + llave que fija el dx.
Guia: GPC mexicanas + ACOG + Williams.
"""
import os
import genanki

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "output")
os.makedirs(OUTPUT_DIR, exist_ok=True)

MODEL_QA_ID = 1990004002
DECK_ID_T, DECK_ID_C, DECK_ID_M = 1990003011, 1990003012, 1990003013
DECK_NAME_T = "No hay tiempo::Obstetricia::Interrogatorio::1 - Troncos (ejes)"
DECK_NAME_C = "No hay tiempo::Obstetricia::Interrogatorio::2 - Llaves comunes (core)"
DECK_NAME_M = "No hay tiempo::Obstetricia::Interrogatorio::3 - Llaves menos preguntadas"

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
model_qa = genanki.Model(MODEL_QA_ID, "NHT Obst Interrogatorio QA",
    fields=[{"name": "Front"}, {"name": "Back"}],
    templates=[{"name": "QA", "qfmt": "{{Front}}", "afmt": '{{Front}}<hr id="extra">{{Back}}'}],
    css=CSS_BASE)

deck_t = genanki.Deck(DECK_ID_T, DECK_NAME_T)
deck_c = genanki.Deck(DECK_ID_C, DECK_NAME_C)
deck_m = genanki.Deck(DECK_ID_M, DECK_NAME_M)
BASE_TAGS = ["obstetricia", "ecoe", "no_hay_tiempo", "interrogatorio"]


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
add(deck_t, caso("TRONCO — Obstetrico general (toda gestante)"),
    tronco("<b>FUM / FPP y semanas</b>, gestas-paras-abortos-cesareas, control prenatal y USG previos, "
           "grupo <b>Rh</b>, tamizajes hechos (DMG, EGB), patologia del embarazo actual y previos, "
           "<b>movimientos fetales</b>, medicamentos/alergias.",
           "Es el encuadre de cualquier estacion obstetrica: ubica semanas, riesgo y antecedentes antes de ir al motivo."),
    T + ["general"])

add(deck_t, caso("TRONCO — Sangrado en el embarazo"),
    tronco("Semanas de gestacion (<b>1er vs 3er trimestre</b>), cantidad y color, <b>dolor</b> (si/no, tipo), "
           "tono uterino, salida de tejido/liquido, <b>movimientos fetales</b>, trauma, relaciones recientes, "
           "estabilidad (mareo). Grupo Rh.",
           "<b>1T:</b> ectopico / aborto / mola.<br><b>3T indoloro</b> &rarr; placenta previa.<br>"
           "<b>3T doloroso + hipertonia</b> &rarr; DPPNI."),
    T + ["sangrado"])

add(deck_t, caso("TRONCO — Cefalea / edema / TA en el embarazo (preeclampsia)"),
    tronco("Semanas (&gt;20?), <b>cefalea</b>, <b>fosfenos/vision borrosa</b>, <b>epigastralgia/dolor en barra</b>, "
           "edema de aparicion rapida (cara/manos), TA habitual, antecedente de preeclampsia/HTA/renal, "
           "movimientos fetales.",
           "<b>TA &ge;140/90 tras 20 sem + proteinuria</b> &rarr; preeclampsia.<br>"
           "<b>+ cefalea/fosfenos/epigastralgia</b> &rarr; datos de severidad.<br>"
           "<b>+ convulsion</b> &rarr; eclampsia."),
    T + ["preeclampsia"])

add(deck_t, caso("TRONCO — Contracciones / dolor de parto"),
    tronco("Semanas, <b>frecuencia y regularidad</b> de contracciones, intensidad, <b>salida de liquido</b> "
           "(hora, color, olor) y de <b>tapon/sangre</b>, movimientos fetales, fiebre. Paridad y partos previos "
           "(cesarea?).",
           "<b>Regulares + cambio cervical</b> &rarr; trabajo de parto verdadero.<br>"
           "<b>&lt;37 sem</b> &rarr; amenaza de parto pretermino.<br>"
           "<b>Salida de liquido</b> &rarr; RPM (&plusmn; corioamnionitis si fiebre)."),
    T + ["parto"])

add(deck_t, caso("TRONCO — Disminucion de movimientos fetales / vigilancia"),
    tronco("Semanas, <b>patron habitual de movimientos</b> y cambio, ultima vez que lo sintio, "
           "factores de riesgo (RCIU, DMG, HTA, postermino, tabaquismo), sangrado/contracciones, TA.",
           "<b>Movimientos disminuidos/ausentes</b> &rarr; evaluar bienestar (RCTG/USG/Doppler).<br>"
           "<b>+ RCIU/HTA</b> &rarr; insuficiencia placentaria.<br>"
           "<b>+ &ge;42 sem</b> &rarr; postermino."),
    T + ["vigilancia_fetal"])

add(deck_t, caso("TRONCO — Fiebre / flujo / sintomas urinarios en el embarazo"),
    tronco("Semanas, <b>salida de liquido</b> (RPM), fiebre y escalofrios, <b>dolor uterino</b>, caracteristicas del "
           "flujo, disuria/dolor lumbar, movimientos y FCF. Cultivos/EGB previos.",
           "<b>Fiebre + utero doloroso + liquido fetido + taquicardia fetal</b> &rarr; corioamnionitis.<br>"
           "<b>Disuria/poliaquiuria</b> &rarr; IVU; <b>+ fiebre/lumbar</b> &rarr; pielonefritis.<br>"
           "<b>Liquido claro continuo</b> &rarr; RPM."),
    T + ["infeccion"])

add(deck_t, caso("TRONCO — Control prenatal (visita y consejeria)"),
    tronco("FUM/FPP y semanas, gestas/antecedentes obstetricos, <b>Rh y Coombs</b>, tamizajes por trimestre "
           "(<b>CTOG 24-28, EGB 36-37</b>), TA y peso, suplementos (folato/hierro), vacunas (Tdap/influenza), "
           "habitos (tabaco/alcohol), red de apoyo.",
           "Cada visita = 'cosechar' el tamizaje del trimestre + reforzar suplementos, vacunas y datos de alarma."),
    T + ["control_prenatal"])


# ===================== LLAVES CORE (18) =====================
C = ["core"]
add(deck_c, caso("Sangrado + dolor + amenorrea en 1er trimestre"),
    llave("&iquest;<b>Dolor pelvico de un lado</b> + atraso menstrual? &iquest;mareo/desmayo? &iquest;beta-hCG en meseta?",
          "Dolor anexial, beta-hCG que <b>no duplica</b>, utero vacio en USG; abdomen agudo si roto.",
          "Embarazo ectopico"),
    C + ["ectopico"])

add(deck_c, caso("Sangrado 1T + utero grande + hiperemesis"),
    llave("&iquest;<b>Nausea/vomito intensos</b>? &iquest;utero mayor que las semanas? &iquest;expulsa <b>vesiculas</b>? &iquest;beta-hCG muy alta?",
          "Utero &gt; amenorrea, beta-hCG muy elevada, <b>USG en copos de nieve</b>, sin FCF; a veces preeclampsia precoz.",
          "Mola hidatiforme"),
    C + ["mola"])

add(deck_c, caso("Sangrado 1T + dolor colico + tejido"),
    llave("&iquest;<b>Colicos</b> y <b>expulsion de tejido/coagulos</b>? &iquest;cuello abierto o cerrado?",
          "Sangrado con dolor; cuello cerrado + embrion vivo = amenaza; cuello abierto/restos = en evolucion/incompleto.",
          "Aborto"),
    C + ["aborto"])

add(deck_c, caso("Sangrado 3T INDOLORO"),
    llave("&iquest;Sangrado <b>rojo brillante SIN dolor</b>? &iquest;utero blando? &iquest;placenta baja en USG previo?",
          "Sangre roja rutilante, indolora, utero relajado, FCF conservada; NO tactar.",
          "Placenta previa"),
    C + ["placenta_previa"])

add(deck_c, caso("Sangrado 3T DOLOROSO"),
    llave("&iquest;<b>Dolor</b> y <b>utero duro/contraido</b>? &iquest;sangre oscura? &iquest;hipertension/trauma?",
          "Dolor + <b>hipertonia uterina</b>, sangre oscura (o sangrado oculto), sufrimiento fetal; factor de riesgo HTA.",
          "DPPNI"),
    C + ["dppni"])

add(deck_c, caso("TA alta tras 20 sem + cefalea"),
    llave("&iquest;<b>Cefalea, fosfenos, epigastralgia</b>? &iquest;proteinuria? &iquest;TA &ge;160/110?",
          "TA &ge;140/90 + proteinuria (o datos de organo); severidad si sintomas o TA &ge;160/110.",
          "Preeclampsia (con/sin severidad)"),
    C + ["preeclampsia"])

add(deck_c, caso("Convulsion en embarazada con TA alta"),
    llave("&iquest;<b>Convulsion tonico-clonica</b> con preeclampsia? (sin otra causa)",
          "Crisis convulsiva en gestante &gt;20 sem con hipertension/proteinuria; emergencia.",
          "Eclampsia"),
    C + ["eclampsia"])

add(deck_c, caso("Preeclampsia + dolor en epigastrio/hipocondrio derecho"),
    llave("&iquest;<b>Dolor en barra/epigastrio</b>, nausea, malestar? &iquest;plaquetas bajas, transaminasas altas?",
          "Hemolisis + enzimas hepaticas elevadas + plaquetas &lt;100k sobre preeclampsia.",
          "Sindrome HELLP"),
    C + ["hellp"])

add(deck_c, caso("Tamizaje de diabetes en 2do trimestre"),
    llave("&iquest;Factores (obesidad, antecedente DMG/macrosomia, familiar)? &iquest;<b>CTOG 24-28 sem</b> alterada?",
          "Glucosa en ayuno/poscarga sobre umbral en CTOG; a veces polihidramnios o feto grande.",
          "Diabetes gestacional"),
    C + ["dmg"])

add(deck_c, caso("Contracciones regulares antes de las 37 sem"),
    llave("&iquest;Contracciones <b>regulares &lt;37 sem</b> con <b>cambio cervical</b>? &iquest;salida de liquido?",
          "Dinamica uterina regular + borramiento/dilatacion antes del termino.",
          "Amenaza de parto pretermino"),
    C + ["pretermino"])

add(deck_c, caso("Salida de liquido por la vagina"),
    llave("&iquest;<b>Salida de liquido claro, continua</b>, que moja la ropa? &iquest;hora? &iquest;color/olor?",
          "Liquido en fondo de saco, <b>nitrazina+ / cristalografia (helecho)+</b>; antes del inicio del parto.",
          "Ruptura prematura de membranas (RPM)"),
    C + ["rpm"])

add(deck_c, caso("Fiebre intraparto + utero doloroso"),
    llave("&iquest;<b>Fiebre</b> + <b>dolor uterino</b> + <b>liquido fetido</b>? &iquest;taquicardia materna y fetal? &iquest;RPM prolongada?",
          "Fiebre + hipersensibilidad uterina + taquicardia fetal + leucocitosis tras RPM.",
          "Corioamnionitis"),
    C + ["corioamnionitis"])

add(deck_c, caso("Madre Rh negativa"),
    llave("&iquest;Grupo <b>Rh negativo</b>? &iquest;Rh del padre? &iquest;<b>Coombs indirecto</b>? &iquest;evento sensibilizante?",
          "Rh- no sensibilizada (Coombs-) &rarr; profilaxis; Coombs+ &rarr; ya sensibilizada (vigilar anemia fetal).",
          "Isoinmunizacion Rh (riesgo)"),
    C + ["rh"])

add(deck_c, caso("Disminucion de movimientos fetales"),
    llave("&iquest;<b>Siente menos al bebe</b> que de costumbre? &iquest;desde cuando? &iquest;factores (RCIU/HTA/DMG)?",
          "Reduccion del patron habitual de movimientos &rarr; evaluar bienestar (RCTG/PBF/Doppler).",
          "Compromiso del bienestar fetal"),
    C + ["vigilancia_fetal"])

add(deck_c, caso("Altura uterina menor que las semanas"),
    llave("&iquest;<b>Fondo uterino &lt; edad gestacional</b>? &iquest;HTA/tabaco/antecedente de RCIU? &iquest;movimientos?",
          "Biometria &lt;p10 + Doppler alterado; oligohidramnios frecuente.",
          "Restriccion del crecimiento (RCIU)"),
    C + ["rciu"])

add(deck_c, caso("Embarazo que paso de la fecha"),
    llave("&iquest;<b>&ge;42 semanas</b> por FUM confiable/USG temprano? &iquest;movimientos fetales? &iquest;liquido?",
          "Gestacion &ge;42 sem; riesgo de insuficiencia placentaria, oligohidramnios, macrosomia.",
          "Embarazo postermino"),
    C + ["postermino"])

add(deck_c, caso("Disuria / poliaquiuria en embarazo"),
    llave("&iquest;<b>Ardor al orinar, frecuencia</b>? &iquest;<b>fiebre + dolor lumbar</b> (sube a rinon)? &iquest;urocultivo?",
          "Cistitis: disuria sin fiebre. Pielonefritis: fiebre + punopercusion+. Bacteriuria asintomatica: urocultivo+ sin sintomas.",
          "IVU en el embarazo"),
    C + ["ivu"])

add(deck_c, caso("Saber si es trabajo de parto verdadero"),
    llave("&iquest;Contracciones <b>regulares que aumentan</b> y <b>NO ceden con reposo</b>? &iquest;cambio cervical?",
          "Verdadero: regulares + borramiento/dilatacion progresivos. Falso: irregulares, sin cambio, ceden.",
          "Trabajo de parto verdadero"),
    C + ["trabajo_parto"])


# ===================== LLAVES MENOS (17) =====================
M = ["menos_preguntado"]
pares = [
    ("Hiperemesis gravidica", "&iquest;Vomito incoercible con <b>perdida de peso &gt;5%</b>, cetonuria, deshidratacion?",
     "Vomito intenso del 1T con cetosis/desequilibrio; descartar mola y gestacion multiple.", "Hiperemesis gravidica", "hiperemesis"),
    ("Toxoplasmosis en embarazo", "&iquest;Contacto con <b>gato/heces, carne cruda</b>? &iquest;seroconversion IgM/IgG?",
     "Seroconversion materna; riesgo de infeccion congenita (mas grave si es temprana).", "Toxoplasmosis (TORCH)", "torch"),
    ("Rubeola / exantema en embarazo", "&iquest;Exantema + adenopatias? &iquest;estado de <b>vacunacion/IgG</b>? &iquest;trimestre?",
     "Rubeola en 1T &rarr; sindrome de rubeola congenita; no se vacuna en embarazo.", "Rubeola (TORCH)", "torch"),
    ("Sifilis en embarazo", "&iquest;VDRL/RPR reactivo? &iquest;tratada antes? &iquest;alergia a penicilina?",
     "Tamizaje +; tratar con <b>penicilina</b> (desensibilizar si alergica) para evitar sifilis congenita.", "Sifilis gestacional (TORCH)", "torch"),
    ("Colestasis intrahepatica del embarazo", "&iquest;<b>Prurito palmoplantar nocturno</b> sin exantema en 3T? &iquest;acidos biliares altos?",
     "Prurito + acidos biliares elevados &plusmn; transaminasas; riesgo fetal &rarr; vigilar/interrumpir cerca del termino.", "Colestasis del embarazo", "colestasis"),
    ("Indice de Bishop", "&iquest;Dilatacion, borramiento, consistencia, posicion y altura del cuello?",
     "Puntaje &ge;6-8 = cuello favorable para induccion con oxitocina; &lt;6 = madurar primero.", "Bishop (induccion)", "induccion"),
    ("Suplemento de acido folico", "&iquest;Antecedente de <b>defecto del tubo neural</b>, diabetes o anticonvulsivos?",
     "400 mcg/dia general; <b>4-5 mg</b> si alto riesgo, desde antes de concebir.", "Acido folico (dosis)", "suplementos"),
    ("Vacunas en embarazo", "&iquest;<b>Tdap (27-36 sem)</b> e influenza puestas? &iquest;alguna vacuna VIVA pendiente?",
     "Recomendadas Tdap e influenza; contraindicadas las vivas (SRP, varicela).", "Vacunacion gestacional", "vacunas"),
    ("Anticoncepcion posparto", "&iquest;<b>Lactando</b>? &iquest;tiempo desde el parto? &iquest;riesgo trombotico?",
     "Lactancia &rarr; solo progestina o DIU; evitar estrogenos las primeras 6 semanas.", "Anticoncepcion en lactancia", "anticoncepcion"),
    ("Tabaquismo/alcohol en embarazo", "&iquest;Consume <b>tabaco, alcohol o drogas</b>? &iquest;cuanto?",
     "Tabaco &rarr; RCIU/DPPNI; alcohol &rarr; sindrome alcoholico fetal; consejeria de cese.", "Habitos toxicos (consejeria)", "habitos"),
    ("Gestacion multiple", "&iquest;Utero/altura mayor a las semanas? &iquest;hiperemesis? &iquest;USG con 2 sacos?",
     "Mas riesgo de preeclampsia, DMG, pretermino, RCIU; define corionicidad temprano.", "Embarazo gemelar", "multiple"),
    ("Presentacion pelvica a termino", "&iquest;Polo <b>duro en fondo</b> (cabeza arriba)? &iquest;semanas? &iquest;USG?",
     "Pelvico a termino &rarr; ofrecer version cefalica externa o cesarea.", "Presentacion pelvica", "presentacion"),
    ("Macrosomia / feto grande", "&iquest;DMG? &iquest;altura uterina grande? &iquest;peso fetal estimado &gt;4000-4500 g?",
     "Macrosomia &rarr; riesgo de distocia de hombros; valorar via de nacimiento.", "Macrosomia fetal", "macrosomia"),
    ("Oligo / polihidramnios", "&iquest;ILA bajo (oligo) o alto (poli)? &iquest;RPM, RCIU, DMG, malformacion?",
     "Oligo &rarr; insuficiencia placentaria/RPM; poli &rarr; DMG/atresias.", "Alteracion del liquido amniotico", "liquido"),
    ("Trombofilia / antecedente de TVP", "&iquest;Antecedente de <b>trombosis</b> o perdidas recurrentes? &iquest;SAF?",
     "Riesgo trombotico aumentado &rarr; valorar <b>heparina</b> (no warfarina en embarazo).", "Trombofilia gestacional", "trombofilia"),
    ("Depresion en el embarazo/posparto", "&iquest;Animo triste, anhedonia, ideas de dano? (<b>Edimburgo</b>)",
     "Tamizaje con escala de Edimburgo; sertralina + psicoterapia; urgente si ideacion suicida.", "Depresion perinatal", "salud_mental"),
    ("Datos de alarma obstetricos (consejeria)", "&iquest;Le explicaron cuando volver de inmediato?",
     "Sangrado, cefalea intensa/fosfenos, salida de liquido, fiebre, <b>disminucion de movimientos</b>, contracciones regulares.", "Datos de alarma", "consejeria"),
]
for titulo, p, pat, dx, tag in pares:
    add(deck_m, caso(titulo), llave(p, pat, dx), M + [tag])


def build():
    for d, f in [(deck_t, "Interrogatorio_01_Troncos.apkg"), (deck_c, "Interrogatorio_02_Llaves_core.apkg"),
                 (deck_m, "Interrogatorio_03_Llaves_menos.apkg")]:
        genanki.Package(d).write_to_file(os.path.join(OUTPUT_DIR, f))
        print(f"  -> {f} ({len(d.notes)} notas)")
    genanki.Package([deck_t, deck_c, deck_m]).write_to_file(
        os.path.join(OUTPUT_DIR, "No_Hay_Tiempo_Obst_Interrogatorio_TODOS.apkg"))
    print(f"  -> TODOS ({sum(len(d.notes) for d in [deck_t, deck_c, deck_m])} notas)")


if __name__ == "__main__":
    build()
