"""No hay tiempo / Medicina Interna — PILAR MANEJO (ejes/patrones madre + core + menos).

Carta de manejo (Back): VERBALIZO (al sinodal) / CONDUCTA-CONSEJERIA / CIERRE (red flag).
Carta de eje (Back): REGLA MADRE / BIFURCACION / TRAMPA.
Guia: ESC (IC 2021/2023, SCA 2023, FA 2024), ADA 2025, KDIGO, GOLD 2025, GINA 2024,
AHA/ACC HTA, Surviving Sepsis 2021, EASL/AASLD, GPC mexicanas.
"""
import os
import genanki

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "output")
os.makedirs(OUTPUT_DIR, exist_ok=True)

MODEL_QA_ID = 1990008001
DECK_ID_E, DECK_ID_C, DECK_ID_M = 1990007001, 1990007002, 1990007003
DECK_NAME_E = "No hay tiempo::Medicina Interna::1 - Ejes / patrones madre"
DECK_NAME_C = "No hay tiempo::Medicina Interna::2 - Manejos comunes (core)"
DECK_NAME_M = "No hay tiempo::Medicina Interna::3 - Menos comunes"

CSS_BASE = """
.card { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  font-size: 19px; text-align: left; color: #1a1a1a; background-color: #fafafa;
  padding: 20px; line-height: 1.55; }
.caso { font-size: 21px; font-weight: 700; color: #1e3a8a; }
#extra { margin-top: 16px; border: none; border-top: 1px solid #d4d4d4; padding-top: 12px; }
.bloque { display: block; margin: 12px 0; padding: 10px 14px; border-radius: 8px; }
.lab { display: block; font-size: 13px; font-weight: 700; letter-spacing: .5px;
  text-transform: uppercase; margin-bottom: 4px; }
.verbalizo { background: #eef2ff; border-left: 4px solid #1e3a8a; }
.conducta { background: #ecfdf5; border-left: 4px solid #047857; }
.cierre { background: #fef2f2; border-left: 4px solid #b91c1c; }
.verbalizo .lab { color: #1e3a8a; } .conducta .lab { color: #047857; } .cierre .lab { color: #b91c1c; }
.regla { background: #eef2ff; border-left: 4px solid #1e3a8a; }
.bif { background: #f5f3ff; border-left: 4px solid #6d28d9; }
.trampa { background: #fef2f2; border-left: 4px solid #b91c1c; }
.regla .lab { color: #1e3a8a; } .bif .lab { color: #6d28d9; } .trampa .lab { color: #b91c1c; }
b { color: #111; }
"""
model_qa = genanki.Model(MODEL_QA_ID, "NHT MI Manejo QA",
    fields=[{"name": "Front"}, {"name": "Back"}],
    templates=[{"name": "QA", "qfmt": "{{Front}}", "afmt": '{{Front}}<hr id="extra">{{Back}}'}],
    css=CSS_BASE)

deck_e = genanki.Deck(DECK_ID_E, DECK_NAME_E)
deck_c = genanki.Deck(DECK_ID_C, DECK_NAME_C)
deck_m = genanki.Deck(DECK_ID_M, DECK_NAME_M)
BASE_TAGS = ["medicina_interna", "ecoe", "no_hay_tiempo"]


def add(deck, front, back, tags):
    deck.add_note(genanki.Note(model=model_qa, fields=[front, back], tags=BASE_TAGS + tags))

def caso(t): return f'<span class="caso">{t}</span>'

def manejo(v, c, ci):
    return (f'<span class="bloque verbalizo"><span class="lab">Verbalizo (al sinodal)</span>{v}</span>'
            f'<span class="bloque conducta"><span class="lab">Conducta / consejeria</span>{c}</span>'
            f'<span class="bloque cierre"><span class="lab">Red flag / cierre</span>{ci}</span>')

def eje(r, b, t):
    return (f'<span class="bloque regla"><span class="lab">Regla madre</span>{r}</span>'
            f'<span class="bloque bif"><span class="lab">Bifurcacion</span>{b}</span>'
            f'<span class="bloque trampa"><span class="lab">Trampa ECOE</span>{t}</span>')


# ===================== EJES / PATRONES MADRE (8) =====================
E = ["eje"]
add(deck_e, caso("EJE 1 — Primero ABC + monitor + glucosa + ECG, no el diagnostico fino"),
    eje("Imagen: estabilizo la maquina antes de leer el manual. Ante el paciente medico grave: "
        "<b>A</b> via aerea, <b>B</b> O2 y SatO2, <b>C</b> via + monitor + TA/FC, <b>D</b> <b>glucosa capilar</b> "
        "y estado neurologico, <b>E</b> temperatura. Y siempre un <b>ECG</b> y un acceso venoso.",
        "<b>Inestable</b> (hipotension, hipoxia, alteracion del estado de alerta) &rarr; resucito y trato en paralelo. "
        "<b>Estable</b> &rarr; tengo tiempo para el workup ordenado.",
        "No pidas la TAC ni esperes el laboratorio para tratar una hipoglucemia, una hiperkalemia con ECG alterado "
        "o un choque: esos se tratan al lado de la cama."),
    E + ["abc"])

add(deck_e, caso("EJE 2 — Toda descompensacion cronica tiene un DESENCADENANTE: buscalo"),
    eje("Imagen: la chispa que prendio el fuego. En IC, EPOC, cirrosis, diabetes, encefalopatia, la pregunta "
        "no es solo 'que tiene' sino '<b>que lo descompenso HOY</b>'.",
        "Gatillos frecuentes: <b>infeccion</b>, <b>falta de apego</b> al tratamiento, <b>transgresion</b> (sal, "
        "liquidos, dieta, alcohol), <b>farmaco nuevo</b> (AINE, esteroide), <b>SCA/arritmia</b>, sangrado, "
        "alteracion electrolitica.",
        "Tratar la descompensacion sin corregir el desencadenante = recae. Siempre verbaliza 'busco el factor "
        "precipitante'."),
    E + ["desencadenante"])

add(deck_e, caso("EJE 3 — Dolor toracico / disnea: descarto primero LO QUE MATA"),
    eje("Imagen: las '5 que matan' antes que la causa benigna. ECG + troponina + signos vitales + SatO2 "
        "en los <b>primeros 10 min</b>.",
        "Las letales: <b>SCA</b> (ECG/troponina), <b>TEP</b> (disnea + factores + hipoxia), <b>diseccion aortica</b> "
        "(dolor desgarrante + asimetria de pulsos), <b>neumotorax a tension</b>, <b>taponamiento</b>.",
        "Un ECG normal NO descarta SCA: si la clinica es sugestiva, troponina seriada y observacion."),
    E + ["dolor_toracico"])

add(deck_e, caso("EJE 4 — Crisis metabolica/endocrina: LIQUIDOS + corregir el deficit + tratar el gatillo"),
    eje("Imagen: tres palancas que muevo siempre juntas. Casi toda urgencia endocrina (CAD, EHH, crisis "
        "suprarrenal, tormenta tiroidea) comparte: <b>reanimacion con liquidos</b>, <b>correccion del eje hormonal/"
        "metabolico</b> y <b>tratar el desencadenante</b> (casi siempre infeccion).",
        "CAD/EHH &rarr; liquidos + insulina + potasio. Crisis suprarrenal &rarr; liquidos + hidrocortisona. "
        "Tormenta tiroidea &rarr; betabloqueante + tionamida + yodo + esteroide. Mixedema &rarr; T4 + hidrocortisona.",
        "En crisis suprarrenal y mixedema da <b>hidrocortisona ANTES</b> de la hormona tiroidea (riesgo de crisis "
        "adrenal). No esperes la confirmacion hormonal para tratar."),
    E + ["crisis_endocrina"])

add(deck_e, caso("EJE 5 — Electrolitos/Na: la VELOCIDAD de correccion importa tanto como el numero"),
    eje("Imagen: corregir despacio para no romper la membrana. En sodio y potasio el riesgo no es solo el valor, "
        "es <b>cuan rapido lo cambio</b>.",
        "<b>Hiponatremia</b>: no subir Na &gt;8-10 mEq/L en 24 h (mielinolisis pontina). "
        "<b>Hiperkalemia con cambios en ECG</b>: <b>gluconato de calcio YA</b> (estabiliza membrana) y luego bajar K. "
        "<b>Hipokalemia</b>: corrige tambien el <b>magnesio</b> o no sube el K.",
        "Subir el sodio demasiado rapido produce dano neurologico irreversible (desmielinizacion osmotica)."),
    E + ["electrolitos"])

add(deck_e, caso("EJE 6 — Insuficiencia respiratoria: la META de O2 depende de si RETIENE CO2"),
    eje("Imagen: dos termostatos de oxigeno. Doy O2 para una <b>meta</b>, no a chorro indiscriminado.",
        "Paciente <b>sin riesgo de retencion</b> (NAC, TEP, IC) &rarr; SatO2 meta <b>94-98%</b>. "
        "Paciente <b>retenedor de CO2</b> (EPOC) &rarr; meta <b>88-92%</b>. "
        "Acidosis respiratoria persistente (EPOC/edema agudo) &rarr; <b>VMNI</b>.",
        "Inundar de O2 al EPOC retenedor puede aumentar la PaCO2 y producir narcosis. Titula a la meta."),
    E + ["insuf_respiratoria"])

add(deck_e, caso("EJE 7 — El RIESGO CV GLOBAL decide la intensidad del tratamiento preventivo"),
    eje("Imagen: una balanza de riesgo que define las metas. No trato cifras aisladas: integro <b>HTA, diabetes/"
        "prediabetes, lipidos, tabaquismo, renal, obesidad/sx metabolico</b> en un riesgo total.",
        "<b>Alto riesgo / enfermedad establecida</b> &rarr; metas estrictas (LDL bajo con estatina alta potencia, "
        "TA &lt;130/80, antiagregacion en prevencion 2a, iSGLT2/GLP1 si diabetes con riesgo CV/renal). "
        "<b>Bajo riesgo</b> &rarr; estilo de vida + metas menos agresivas.",
        "Tratar un solo factor e ignorar los demas (p.ej. bajar TA pero no tocar LDL/tabaco) deja el riesgo casi intacto."),
    E + ["riesgo_cv"])

add(deck_e, caso("EJE 8 — Sepsis: bundle de 1 hora y control del FOCO"),
    eje("Imagen: el reloj de la primera hora. Sospecho infeccion + disfuncion organica (qSOFA/SOFA) y actuo ya.",
        "<b>Bundle 1 h</b>: medir <b>lactato</b>, <b>hemocultivos antes del antibiotico</b>, <b>antibiotico de "
        "amplio espectro</b>, <b>cristaloide 30 mL/kg</b> si hipotension/lactato &ge;4, <b>vasopresor</b> "
        "(noradrenalina) si TAM &lt;65 tras volumen. Y <b>control del foco</b> (drenar/retirar).",
        "Retrasar el antibiotico esperando cultivos o imagen aumenta la mortalidad por hora. Cultivos primero, "
        "pero rapido."),
    E + ["sepsis"])


# ===================== CORE / COMUNES (18) =====================
C = ["core"]
add(deck_c, caso("Hipertension arterial (manejo cronico)"),
    manejo("Cambios de estilo de vida + farmaco: <b>IECA/ARA-II + calcioantagonista + tiazida</b> (combinar pronto, "
           "preferible doble de inicio). Meta general <b>&lt;130/80</b>. Busco dano a organo blanco y descarto "
           "causa secundaria si datos atipicos.",
           "Tiene la presion alta de forma cronica; el objetivo es mantenerla controlada con medicamento diario y "
           "habitos (sal, peso, ejercicio) para evitar infarto, EVC y dano renal.",
           "No combines IECA + ARA-II. Vigila K y creatinina al iniciar IECA/ARA-II. Descarta 2aria si es joven, "
           "refractaria o de inicio brusco."),
    C + ["htas"])

add(deck_c, caso("Crisis hipertensiva (urgencia vs emergencia)"),
    manejo("<b>Emergencia</b> (TA muy alta + <b>dano agudo de organo blanco</b>: EVC, SCA, edema pulmonar, diseccion, "
           "eclampsia, encefalopatia) &rarr; <b>IV en monitor</b>, bajar TAM ~<b>10-25% en la 1a hora</b>. "
           "<b>Urgencia</b> (sin dano agudo) &rarr; reduccion <b>gradual VO</b> en horas/dias.",
           "La presion esta peligrosamente alta. Si ya esta danando un organo, la bajamos de forma controlada en el "
           "hospital; si no, la bajamos poco a poco con pastillas.",
           "Bajar la TA demasiado rapido en la urgencia (sin dano de organo) puede causar isquemia cerebral/coronaria. "
           "Excepciones que SI requieren bajada rapida: diseccion aortica y eclampsia."),
    C + ["crisis_htas"])

add(deck_c, caso("Diabetes mellitus tipo 2 (manejo)"),
    manejo("Estilo de vida + <b>metformina</b> de base. Anado segun comorbilidad: <b>iSGLT2</b> (IC, ERC) o "
           "<b>GLP-1</b> (ASCVD, obesidad) <b>independiente de la HbA1c</b> si hay riesgo CV/renal. Meta general "
           "<b>HbA1c &lt;7%</b> (individualizada). Trato TA, LDL (estatina) y tabaquismo.",
           "Tiene diabetes; el control combina alimentacion, ejercicio y medicamento. Ademas de la glucosa, cuidamos "
           "presion, colesterol y rinon porque eso es lo que evita las complicaciones.",
           "El iSGLT2/GLP-1 se eligen por proteccion CV/renal, no solo por la glucosa. Vigila pie diabetico, retina, "
           "rinon (albuminuria) cada ano."),
    C + ["diabetes"])

add(deck_c, caso("Insuficiencia cardiaca con FEr (FEVI reducida)"),
    manejo("<b>Los 4 pilares ('fantasticos')</b> desde el inicio: <b>ARNI/IECA-ARA-II</b>, <b>betabloqueante</b>, "
           "<b>ARM (espironolactona)</b>, <b>iSGLT2</b>. Diuretico de asa para la congestion. Titulo a dosis meta.",
           "El corazon bombea debil. Hay 4 medicamentos que juntos hacen que viva mas y se hospitalice menos; el "
           "diuretico quita el liquido de los pulmones y las piernas. Cuido la sal y el peso diario.",
           "Los 4 pilares mejoran SUPERVIVENCIA; el diuretico solo da sintomas. Vigila K y funcion renal con ARM/IECA. "
           "Betabloqueante NO se inicia en descompensacion aguda con congestion."),
    C + ["ic_fer"])

add(deck_c, caso("Insuficiencia cardiaca con FEp (FEVI preservada)"),
    manejo("<b>iSGLT2</b> (unico con beneficio claro) + <b>diuretico</b> para congestion + tratar agresivamente "
           "las <b>comorbilidades</b> (HTA, FA, obesidad, diabetes, isquemia).",
           "El corazon se llena mal aunque la fuerza este conservada. Controlamos el liquido y, sobre todo, las "
           "enfermedades de fondo (presion, arritmia, peso) que la empeoran.",
           "Aqui los 4 pilares no aplican igual que en FEr; el pilar es el iSGLT2 + control de comorbilidades. "
           "No sobre-diuretizar (cae el gasto)."),
    C + ["ic_fep"])

add(deck_c, caso("Fibrilacion auricular"),
    manejo("<b>Inestable</b> (angina, hipotension, edema, sincope) &rarr; <b>cardioversion electrica</b>. "
           "<b>Estable</b> &rarr; <b>control de frecuencia</b> (betabloqueante/calcioantagonista) y/o ritmo. "
           "Y SIEMPRE evaluar <b>anticoagulacion segun CHA2DS2-VASc</b>.",
           "El corazon late de forma irregular. Bajamos la frecuencia y, lo mas importante, valoramos un "
           "anticoagulante para prevenir un coagulo que cause un EVC.",
           "Anticoagular antes de cardiovertir si la FA es &gt;48 h (o no se sabe) salvo ETE sin trombo. "
           "El control de frecuencia NO sustituye a la anticoagulacion."),
    C + ["fa"])

add(deck_c, caso("IAM con elevacion del ST (IAMCEST)"),
    manejo("<b>Reperfusion urgente</b>: <b>ICP primaria</b> si disponible en &lt;120 min; si no, <b>fibrinolisis</b> "
           "(&lt;12 h sin contraindicacion) y traslado. + <b>doble antiagregacion</b> (AAS + inhibidor P2Y12) + "
           "<b>anticoagulacion</b> + estatina alta potencia. MONA es sintomatico, no es el tratamiento.",
           "(urgencia) Una arteria del corazon esta tapada y el musculo se esta muriendo. Hay que destaparla cuanto "
           "antes con un cateterismo o, si no se puede, con un medicamento que disuelve el coagulo.",
           "<b>Tiempo es musculo.</b> No retrases la reperfusion. El oxigeno solo si SatO2 &lt;90% (no de rutina)."),
    C + ["iamcest"])

add(deck_c, caso("SCA sin elevacion del ST (IAMSEST / angina inestable)"),
    manejo("<b>Antiagregacion</b> (AAS + P2Y12) + <b>anticoagulacion</b> + antianginoso (nitrato, betabloqueante) + "
           "estatina. <b>Estratifico riesgo (GRACE)</b>: alto riesgo &rarr; <b>coronariografia temprana</b> "
           "(&lt;24 h); muy alto riesgo (inestable) &rarr; invasiva inmediata.",
           "Hay isquemia del corazon sin oclusion total. Damos medicamentos para evitar que progrese y, segun el "
           "riesgo, hacemos un cateterismo para ver y tratar las arterias.",
           "NO se da fibrinolisis en el SEST (solo en CEST). El manejo es antitrombotico + estratificar + cateterismo "
           "segun riesgo."),
    C + ["iamsest"])

add(deck_c, caso("EPOC (exacerbacion)"),
    manejo("<b>Broncodilatadores de accion corta</b> (SABA + SAMA nebulizados) + <b>esteroide sistemico</b> (5 dias) "
           "+ <b>antibiotico</b> si esputo purulento/aumento de disnea + <b>O2 con meta 88-92%</b>. "
           "<b>VMNI</b> si acidosis respiratoria (pH &lt;7.35 con hipercapnia).",
           "Se le agravo el EPOC. Abrimos los bronquios con nebulizaciones, damos cortisona unos dias y, si la "
           "flema esta infectada, antibiotico; el oxigeno se da con cuidado para no dormirlo.",
           "Meta de O2 88-92% (riesgo de narcosis por CO2). La VMNI evita la intubacion en la acidosis respiratoria."),
    C + ["epoc"])

add(deck_c, caso("Crisis asmatica"),
    manejo("<b>SABA</b> (salbutamol) repetido + <b>O2 (meta 94-98%)</b> + <b>esteroide sistemico precoz</b> + "
           "<b>ipratropio</b> en crisis grave + <b>sulfato de magnesio IV</b> si grave/refractaria.",
           "Es una crisis de asma. Abrimos los bronquios con el inhalador repetido, damos cortisona y oxigeno; si no "
           "responde, agregamos otros medicamentos en vena.",
           "Signos de gravedad: silencio auscultatorio, agotamiento, SatO2 baja, PCO2 normal/alta (deberia estar "
           "baja). Una PCO2 'normal' en crisis grave anuncia paro respiratorio."),
    C + ["asma"])

add(deck_c, caso("Neumonia adquirida en la comunidad (NAC)"),
    manejo("Evaluo gravedad (<b>CURB-65</b>) para decidir ambulatorio vs hospital vs UCI. <b>Antibiotico empirico</b> "
           "segun el sitio: ambulatorio (amoxicilina/macrolido), hospital (betalactamico + macrolido o fluoroquinolona "
           "respiratoria). O2 y soporte.",
           "Tiene una neumonia. Segun la gravedad decidimos si se trata en casa o ingresado; el pilar es el "
           "antibiotico, mas oxigeno y liquidos si lo necesita.",
           "CURB-65 (Confusion, Urea, FR&ge;30, TA baja, &ge;65) guia el sitio de manejo. Reevalua si no mejora en "
           "48-72 h (derrame/empiema, germen resistente)."),
    C + ["nac"])

add(deck_c, caso("Tromboembolia pulmonar (TEP)"),
    manejo("<b>Inestable / TEP masiva</b> (hipotension, choque) &rarr; <b>trombolisis</b> (o embolectomia). "
           "<b>Estable</b> &rarr; <b>anticoagulacion</b> (HBPM/ACOD). Inicio anticoagulacion empirica si alta "
           "probabilidad mientras confirmo con angio-TAC.",
           "Un coagulo viajo al pulmon. Si esta estable, lo tratamos con anticoagulante; si esta en choque, se usa "
           "un medicamento que disuelve el coagulo de inmediato.",
           "Estable se anticoagula; <b>inestable se trombolisa</b>. Usa Wells/PERC y dimero D para decidir imagen, "
           "no para descartar en alta probabilidad."),
    C + ["tep"])

add(deck_c, caso("Lesion renal aguda (AKI) — enfoque y manejo"),
    manejo("Clasifico <b>prerrenal / renal / postrenal</b>. Manejo: <b>tratar la causa</b>, optimizar volemia y "
           "perfusion, <b>suspender nefrotoxicos</b> (AINE, contraste, aminoglucosidos) y ajustar farmacos. "
           "Vigilo indicaciones de dialisis.",
           "El rinon dejo de funcionar de golpe. Buscamos la causa (deshidratacion, obstruccion, dano directo), la "
           "corregimos y retiramos lo que dane al rinon mientras se recupera.",
           "Indicaciones urgentes de dialisis (<b>AEIOU</b>): Acidosis refractaria, Electrolitos (hiperK), Intoxicacion, "
           "Overload (sobrecarga refractaria), Uremia (encefalopatia/pericarditis)."),
    C + ["aki"])

add(deck_c, caso("Hiponatremia"),
    manejo("Evaluo <b>volemia + osmolaridad + sodio urinario</b>. <b>Sintomatica grave</b> (convulsion, coma) &rarr; "
           "<b>salino hipertonico 3%</b> en bolos. Cronica/leve &rarr; tratar la causa (restriccion hidrica en SIADH, "
           "volumen en hipovolemica). <b>Correccion lenta</b>.",
           "El sodio en sangre esta bajo. Segun la causa y los sintomas, restringimos liquidos o damos suero; lo "
           "subimos despacio para proteger el cerebro.",
           "<b>No subir Na &gt;8-10 mEq/L/24 h</b> (mielinolisis pontina/desmielinizacion osmotica). "
           "La hipertonica 3% se reserva para sintomas neurologicos graves."),
    C + ["hiponatremia"])

add(deck_c, caso("Cetoacidosis diabetica (CAD)"),
    manejo("<b>Liquidos IV (salino 0.9%)</b> primero + <b>insulina IV en infusion</b> + <b>reposicion de potasio</b> + "
           "buscar y tratar el <b>desencadenante</b> (infeccion, omision de insulina). Monitorizo glucosa, K, brecha "
           "anionica y pH.",
           "(urgencia) La diabetes se descompenso con acidos en la sangre. Reponemos liquidos, damos insulina en vena "
           "y vigilamos el potasio de cerca hasta que se corrija.",
           "<b>No inicies insulina si K &lt;3.3</b> (la insulina baja mas el K &rarr; arritmia): repon K primero. "
           "Anade glucosa al suero cuando la glucemia baje de ~200 para seguir cerrando la brecha."),
    C + ["cad"])

add(deck_c, caso("Cirrosis descompensada"),
    manejo("Identifico la <b>descompensacion</b> y la trato: <b>ascitis</b> (restriccion de sal + diuretico, "
           "paracentesis); <b>PBE</b> (cefotaxima + <b>albumina</b>); <b>varices sangrantes</b> (vasoactivo + ligadura "
           "+ ATB); <b>encefalopatia</b> (lactulosa). Busco el precipitante.",
           "El higado cirrotico se descompenso. Segun la complicacion (liquido en el abdomen, infeccion, sangrado o "
           "confusion) damos el tratamiento dirigido y buscamos que la disparo.",
           "En PBE: cefotaxima + <b>albumina</b> (previene sindrome hepatorrenal). En toda ascitis nueva o deterioro: "
           "<b>paracentesis diagnostica</b> para descartar PBE."),
    C + ["cirrosis"])

add(deck_c, caso("Sepsis / choque septico"),
    manejo("<b>Bundle de 1 hora</b>: lactato, <b>hemocultivos antes del antibiotico</b>, <b>antibiotico amplio "
           "espectro</b>, <b>cristaloide 30 mL/kg</b>, <b>noradrenalina</b> si TAM &lt;65 tras volumen. "
           "<b>Control del foco</b> en cuanto sea posible.",
           "(a la familia) Tiene una infeccion grave que afecta todo el cuerpo; iniciamos antibiotico y sueros de "
           "inmediato y buscamos el origen para controlarlo.",
           "qSOFA &ge;2 (TA &le;100, FR &ge;22, alteracion mental) marca riesgo. El antibiotico en la 1a hora salva "
           "vidas; no lo retrases por estudios."),
    C + ["sepsis"])

add(deck_c, caso("Gota (ataque agudo)"),
    manejo("<b>Agudo</b>: <b>AINE</b> o <b>colchicina</b> o <b>esteroide</b> (segun comorbilidad) lo antes posible. "
           "<b>NO inicies ni suspendas alopurinol durante el ataque</b>. Urato-bajante (<b>alopurinol</b>) "
           "<b>despues</b>, con profilaxis con colchicina al iniciarlo.",
           "Es un ataque de gota por cristales de acido urico en la articulacion. Primero quitamos la inflamacion y el "
           "dolor; despues, ya en calma, iniciamos el medicamento que baja el acido urico de forma permanente.",
           "Iniciar alopurinol en pleno ataque lo prolonga. En ERC ajusta dosis; la colchicina a dosis altas es toxica."),
    C + ["gota"])


# ===================== MENOS COMUNES (24) =====================
M = ["menos_comun"]
def menos(deck, t, v, c, ci, tags):
    add(deck, caso(t), manejo(v, c, ci), M + tags)

menos(deck_m, "Estenosis aortica",
      "Vigilancia si asintomatica. <b>Sintomatica</b> (angina, sincope, disnea) o severa &rarr; <b>reemplazo "
      "valvular</b> (<b>RVAo quirurgico o TAVI</b> segun riesgo). Cuidado con vasodilatadores y diureticos potentes.",
      "La valvula aortica esta estrecha y el corazon batalla para sacar la sangre. Cuando da sintomas, el tratamiento "
      "que sirve es cambiar la valvula.",
      "Triada: <b>angina, sincope, disnea</b>. Evita nitratos/vasodilatadores en estenosis severa (caida brusca de "
      "TA). El sincope de esfuerzo es bandera roja.", ["estenosis_aortica"])

menos(deck_m, "Insuficiencia mitral",
      "<b>Aguda</b> (rotura de cuerda/musculo papilar post-IAM, endocarditis) &rarr; edema pulmonar &rarr; estabilizar "
      "+ <b>cirugia urgente</b>. <b>Cronica</b> severa sintomatica o con disfuncion del VI &rarr; <b>reparacion/"
      "reemplazo</b> valvular.",
      "La valvula mitral cierra mal y la sangre se regresa. Si es brusca, es una urgencia; si es cronica, se vigila y "
      "se opera cuando da sintomas o el corazon empieza a fallar.",
      "La IM aguda post-IAM se presenta como edema pulmonar + soplo nuevo &rarr; urgencia quirurgica.", ["insuf_mitral"])

menos(deck_m, "Pericarditis aguda",
      "<b>AINE (alta dosis) + colchicina</b> (reduce recurrencia). Restriccion de ejercicio. Busco derrame; si hay "
      "<b>taponamiento</b> &rarr; <b>pericardiocentesis</b>. Evito anticoagulantes.",
      "Es una inflamacion de la bolsa que rodea el corazon. El dolor mejora con antiinflamatorios; agregamos "
      "colchicina para que no recaiga.",
      "ECG: <b>elevacion del ST difusa concava + descenso del PR</b>. Vigila taponamiento (Beck: hipotension, "
      "yugulares, ruidos velados, pulso paradojico).", ["pericarditis"])

menos(deck_m, "Estado hiperosmolar hiperglucemico (EHH)",
      "<b>Reanimacion con liquidos AGRESIVA</b> (deficit mayor que en CAD) + insulina IV + potasio + tratar el "
      "desencadenante. Glucemias muy altas, osmolaridad alta, <b>sin cetoacidosis significativa</b>.",
      "(urgencia) La glucosa subio muchisimo y deshidrato al paciente. Lo principal es reponer mucho liquido, ademas "
      "de insulina y vigilar el potasio.",
      "El pilar inicial es el LIQUIDO (mas que la insulina). Mortalidad mayor que la CAD; suele haber deterioro "
      "neurologico por la hiperosmolaridad.", ["ehh"])

menos(deck_m, "Tormenta tiroidea",
      "<b>Betabloqueante (propranolol)</b> + <b>tionamida (PTU)</b> + <b>yodo (Lugol) 1 h DESPUES de la tionamida</b> "
      "+ <b>hidrocortisona</b> + medidas antitermicas + tratar el gatillo. Soporte.",
      "(urgencia) La tiroides esta hiperactiva al extremo y afecta corazon y temperatura. Damos varios medicamentos "
      "en secuencia para frenarla y proteger al paciente.",
      "El <b>orden importa</b>: tionamida ANTES que el yodo (el yodo antes podria alimentar la sintesis). "
      "Betabloqueante controla la tormenta simpatica.", ["tormenta_tiroidea"])

menos(deck_m, "Coma mixedematoso",
      "<b>Levotiroxina IV</b> + <b>hidrocortisona (ANTES de la T4)</b> + soporte (recalentamiento pasivo, ventilacion, "
      "corregir hiponatremia/hipoglucemia) + tratar el desencadenante.",
      "(urgencia) El hipotiroidismo se descompenso al extremo: el paciente esta frio, lento y con bajo nivel de "
      "alerta. Damos hormona tiroidea y cortisona en vena, ademas de soporte.",
      "Da <b>hidrocortisona antes</b> de la levotiroxina (puede coexistir insuficiencia suprarrenal &rarr; crisis). "
      "No recalentar activamente (vasodilatacion e hipotension).", ["coma_mixedematoso"])

menos(deck_m, "Crisis suprarrenal (addisoniana)",
      "<b>Hidrocortisona 100 mg IV</b> de inmediato (no esperar confirmacion) + <b>liquidos IV (salino + glucosa)</b> "
      "+ tratar el desencadenante. Buscar hiponatremia + hiperkalemia + hipoglucemia.",
      "(urgencia) Las glandulas suprarrenales no producen cortisol y el paciente entra en choque. La cortisona en "
      "vena y los sueros son inmediatos y salvan la vida.",
      "No retrases la hidrocortisona por estudios. Sospecha si hipotension que no responde a liquidos + "
      "hiponatremia + hiperkalemia.", ["crisis_suprarrenal"])

menos(deck_m, "Hiperkalemia",
      "<b>Con cambios en ECG &rarr; gluconato de calcio IV YA</b> (estabiliza miocardio). Luego <b>introducir K a la "
      "celula</b> (insulina + glucosa, beta-2, bicarbonato si acidosis) y <b>eliminar K</b> (diureticos, resinas/"
      "patiromer, dialisis). Suspender IECA/ARA-II/ARM y aportes.",
      "El potasio esta alto y puede alterar el corazon. Primero protegemos el corazon, luego metemos el potasio a "
      "las celulas y finalmente lo eliminamos del cuerpo.",
      "Ondas T picudas &rarr; ensanchamiento del QRS &rarr; onda sinusoidal &rarr; paro. El calcio NO baja el K, "
      "solo protege la membrana.", ["hiperkalemia"])

menos(deck_m, "Hipokalemia",
      "<b>Reponer K</b> (VO si leve; IV en grave/sintomatica, ritmo controlado y monitorizado) y <b>corregir el "
      "magnesio</b> (sin Mg no sube el K). Identificar perdidas (diureticos, vomito/diarrea, hiperaldosteronismo).",
      "El potasio esta bajo, lo que puede causar arritmias y debilidad. Lo reponemos por boca o vena segun la "
      "gravedad y corregimos tambien el magnesio.",
      "Hipokalemia refractaria = revisa el <b>magnesio</b>. ECG: aplanamiento de T, onda U, riesgo de arritmia "
      "(sobre todo con digoxina).", ["hipokalemia"])

menos(deck_m, "Sindrome nefrotico",
      "<b>Proteinuria &gt;3.5 g</b> + hipoalbuminemia + edema + hiperlipidemia. Manejo: <b>IECA/ARA-II</b> "
      "(antiproteinurico), diuretico para el edema, estatina, dieta hiposodica, <b>profilaxis/tratamiento del riesgo "
      "trombotico</b>; tratar la causa (biopsia, esteroide segun etiologia).",
      "El rinon pierde mucha proteina por la orina, lo que hincha al paciente. Damos medicamento que reduce la "
      "perdida de proteina, controlamos el liquido y vigilamos el riesgo de coagulos.",
      "Alto riesgo de <b>trombosis</b> (incluida trombosis de vena renal) e infecciones. Edema con orina espumosa.", ["nefrotico"])

menos(deck_m, "Sindrome nefritico",
      "<b>Hematuria (cilindros hematicos) + HTA + edema + oliguria + proteinuria leve-moderada</b>. Manejo: "
      "<b>control de TA y volumen</b> (diuretico, restriccion de sal), tratar la causa (post-infecciosa, IgA, "
      "vasculitis, anti-MBG); biopsia y, segun etiologia, inmunosupresion.",
      "El rinon esta inflamado: aparece sangre en la orina, sube la presion y se retiene liquido. Controlamos presion "
      "y liquido y buscamos la causa para tratarla.",
      "El <b>cilindro hematico</b> es la pista de glomerulonefritis. Las rapidamente progresivas (semilunas) son "
      "urgencia: biopsia + inmunosupresion pronto.", ["nefritico"])

menos(deck_m, "Necrosis tubular aguda (NTA)",
      "AKI <b>intrinseca</b> por isquemia (choque prolongado) o nefrotoxicos (contraste, aminoglucosidos, "
      "rabdomiolisis). Manejo: <b>soporte</b>, optimizar perfusion, suspender toxicos, evitar nuevas agresiones, "
      "dialisis si indicacion. Suele recuperar en 1-3 semanas.",
      "El tejido del rinon se dano por falta de riego o por una sustancia toxica. No hay 'cura' rapida: damos soporte "
      "y tiempo, evitando danarlo mas, hasta que se recupere.",
      "FeNa &gt;2%, Na urinario alto, <b>cilindros granulosos 'pardos lodosos'</b>. Diferenciar de prerrenal "
      "(que SI responde a volumen).", ["nta"])

menos(deck_m, "AKI postrenal (obstructiva)",
      "<b>Identificar y resolver la obstruccion</b> (USG con hidronefrosis): <b>sonda vesical</b> si globo/prostata, "
      "<b>nefrostomia/cateter ureteral</b> si obstruccion alta. Vigilar <b>diuresis post-obstructiva</b> y reponer.",
      "La orina no puede salir y se 'represa' danando el rinon. Lo principal es destapar la via (con una sonda o un "
      "drenaje) y la funcion suele recuperarse.",
      "Tras desobstruir puede haber poliuria masiva (diuresis post-obstructiva) &rarr; reponer liquidos y "
      "electrolitos. USG es la clave (hidronefrosis).", ["postrenal"])

menos(deck_m, "Encefalopatia hepatica",
      "<b>Lactulosa</b> (meta 2-3 evacuaciones/dia) &plusmn; <b>rifaximina</b> + <b>buscar y corregir el "
      "precipitante</b> (infeccion/PBE, sangrado digestivo, estrenimiento, hipokalemia, deshidratacion, sedantes).",
      "El higado enfermo no limpia las toxinas y el paciente se confunde. Damos un laxante especial que las elimina "
      "por el intestino y buscamos que lo disparo (infeccion, sangrado, estrenimiento).",
      "El amonio NO se usa para titular el tratamiento; guiate por la clinica. Casi siempre hay un precipitante: "
      "buscalo (sobre todo infeccion y sangrado).", ["encefalopatia"])

menos(deck_m, "Hepatitis alcoholica",
      "Abstinencia + soporte nutricional + tratar abstinencia/infeccion. <b>Grave</b> (Maddrey &ge;32 / MELD alto) &rarr; "
      "valorar <b>corticoide (prednisolona)</b> y reevaluar respuesta (Lille). Tiamina antes de glucosa.",
      "El alcohol inflamo el higado de forma aguda. Lo principal es suspender el alcohol y dar soporte; en casos "
      "graves se valora cortisona.",
      "Da <b>tiamina antes de la glucosa</b> (Wernicke). El corticoide solo en grave y se reevalua respuesta a los "
      "7 dias; descarta infeccion antes.", ["hepatitis_alcoholica"])

menos(deck_m, "Higado graso metabolico (MASLD / MASH)",
      "Base del tratamiento: <b>perdida de peso (7-10%)</b>, ejercicio y control de comorbilidades (diabetes, "
      "dislipidemia, HTA). iSGLT2/GLP-1 si diabetes; resmetirom en MASH con fibrosis segun disponibilidad. "
      "Vigilar progresion a fibrosis.",
      "Es grasa en el higado ligada al sindrome metabolico. El tratamiento mas efectivo es bajar de peso y controlar "
      "azucar, colesterol y presion; asi se revierte y se evita que cicatrice.",
      "MASLD = esteatosis; <b>MASH</b> = esteatohepatitis (inflamacion + dano) que puede progresar a cirrosis. "
      "Estratifica fibrosis (FIB-4, elastografia).", ["masld_mash"])

menos(deck_m, "Anemia de enfermedad cronica (inflamatoria)",
      "<b>Tratar la enfermedad de base</b> (inflamacion/infeccion/neoplasia). Hierro normal-alto con <b>ferritina "
      "normal/alta</b> y <b>saturacion de transferrina baja</b>. No suele responder a hierro solo.",
      "La anemia viene de una enfermedad cronica que 'esconde' el hierro. Lo que mas ayuda es controlar esa "
      "enfermedad de fondo.",
      "Diferencia de la ferropenica: aqui la <b>ferritina esta normal/alta</b> (es reactante de fase aguda). "
      "Puede coexistir con ferropenia (revisa indices).", ["anemia_cronica"])

menos(deck_m, "Anemia macrocitica (B12 / folato)",
      "Identifico la causa: <b>deficit de B12</b> (anemia perniciosa, malabsorcion, dieta) o <b>folato</b>. "
      "<b>Reponer B12 IM/VO o folato</b>. Buscar causas no megaloblasticas (alcohol, hipotiroidismo, farmacos).",
      "Los globulos rojos salen grandes por falta de vitamina B12 o acido folico. Reponemos la vitamina que falta y "
      "buscamos por que faltaba.",
      "<b>Repon B12 ANTES o junto con folato</b>: dar solo folato con deficit de B12 puede precipitar/empeorar dano "
      "neurologico. Busca clinica neurologica en deficit de B12.", ["anemia_macrocitica"])

menos(deck_m, "Artritis reumatoide",
      "<b>FAME (DMARD) precoz</b>, de eleccion <b>metotrexato</b> (+ acido folico); biologico/JAK si no responde. "
      "AINE/esteroide como puente sintomatico. Meta: <b>remision o baja actividad (treat-to-target)</b>.",
      "Es una artritis autoinmune que dana las articulaciones si no se trata pronto. El medicamento de fondo "
      "(metotrexato) frena el dano; lo iniciamos temprano.",
      "Poliartritis <b>simetrica</b> de pequenas articulaciones + rigidez matutina &gt;1 h. El FAME modifica el "
      "curso; el AINE/esteroide solo alivia. Iniciar pronto evita erosiones.", ["ar"])

menos(deck_m, "Lupus eritematoso sistemico (LES)",
      "<b>Hidroxicloroquina para todos</b> + esteroide e <b>inmunosupresor segun organo</b> (nefritis lupica &rarr; "
      "micofenolato/ciclofosfamida). Foto-proteccion. Trato brotes y vigilo organo blanco (rinon, hemato, SNC).",
      "Es una enfermedad autoinmune que puede afectar varios organos. La hidroxicloroquina es base para todos; segun "
      "el organo afectado se agregan otros medicamentos.",
      "La <b>nefritis lupica</b> cambia el pronostico: tamiza con EGO/proteinuria. Vigila infecciones (inmunosupresion) "
      "y eventos tromboticos (sx antifosfolipido).", ["les"])

menos(deck_m, "Polimialgia reumatica (PMR)",
      "Dolor y rigidez de <b>cinturas escapular y pelvica</b> en &gt;50 anos, VSG/PCR altas. <b>Corticoide a dosis "
      "baja-moderada</b> con respuesta rapida y dramatica. Descenso lento.",
      "Es un dolor y rigidez de hombros y caderas en personas mayores. Responde muy rapido a una dosis baja de "
      "cortisona, que luego se baja poco a poco.",
      "Vigila <b>arteritis de celulas gigantes</b> asociada (cefalea, claudicacion mandibular, alteracion visual) &rarr; "
      "es urgencia, dosis ALTA de esteroide para salvar la vision.", ["pmr"])

menos(deck_m, "Enfermedad de Graves / hipertiroidismo",
      "<b>Betabloqueante</b> para sintomas + <b>tionamida (metimazol)</b>; opciones definitivas: <b>yodo radiactivo</b> "
      "o <b>cirugia</b>. En Graves vigilar oftalmopatia. PTU de eleccion en 1er trimestre del embarazo.",
      "La tiroides produce hormona de mas y acelera todo el cuerpo. Damos un medicamento para frenarla y otro para "
      "los sintomas del corazon; a veces se trata de forma definitiva con yodo o cirugia.",
      "Metimazol de eleccion (salvo 1er trimestre embarazo = PTU). Vigila <b>agranulocitosis</b> (fiebre/odinofagia "
      "&rarr; suspender y hemograma) y hepatotoxicidad.", ["graves"])

menos(deck_m, "Endocarditis infecciosa",
      "<b>3 sets de hemocultivos</b> + <b>ecocardiograma</b> (vegetaciones) + criterios de <b>Duke</b>. "
      "<b>Antibiotico IV prolongado</b> (4-6 sem dirigido). <b>Cirugia</b> si IC por disfuncion valvular, infeccion "
      "no controlada o embolismos recurrentes/vegetacion grande.",
      "Hay una infeccion en una valvula del corazon. Necesita antibiotico en vena por varias semanas; a veces, "
      "ademas, cirugia para reparar o cambiar la valvula.",
      "Sospecha en fiebre + soplo nuevo + factores (valvulopatia, protesis, drogas IV). Toma hemocultivos ANTES del "
      "antibiotico (salvo sepsis). Fenomenos embolicos/inmunes (Janeway, Osler, Roth).", ["endocarditis"])

menos(deck_m, "Pielonefritis aguda / ITU complicada",
      "<b>Antibiotico empirico</b> (segun gravedad/resistencias locales; ambulatorio fluoroquinolona/cefalosporina, "
      "grave IV) + hidratacion + analgesia. <b>Imagen (USG/TAC)</b> si no mejora en 48-72 h, sepsis, o sospecha de "
      "obstruccion/absceso. Urocultivo SIEMPRE en complicada.",
      "Es una infeccion del rinon. Damos antibiotico (en vena si esta grave) y liquidos; si no mejora pronto, "
      "buscamos una obstruccion o un absceso con un estudio de imagen.",
      "ITU + obstruccion (litiasis) = <b>pionefrosis</b> &rarr; urgencia para drenar (antibiotico solo no basta). "
      "Toma urocultivo antes del antibiotico en la complicada.", ["pielonefritis"])


def build():
    for d, f in [(deck_e, "Manejo_01_Ejes.apkg"), (deck_c, "Manejo_02_Core.apkg"), (deck_m, "Manejo_03_Menos.apkg")]:
        genanki.Package(d).write_to_file(os.path.join(OUTPUT_DIR, f))
        print(f"  -> {f} ({len(d.notes)} notas)")
    genanki.Package([deck_e, deck_c, deck_m]).write_to_file(
        os.path.join(OUTPUT_DIR, "No_Hay_Tiempo_MI_Manejo_TODOS.apkg"))
    print(f"  -> TODOS ({sum(len(d.notes) for d in [deck_e, deck_c, deck_m])} notas)")


if __name__ == "__main__":
    build()
