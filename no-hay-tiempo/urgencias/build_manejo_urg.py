"""No hay tiempo / Urgencias — PILAR MANEJO (ejes/patrones madre + core + menos).

Carta de manejo (Back): VERBALIZO (al sinodal) / CONDUCTA-CONSEJERIA / CIERRE (red flag).
Carta de eje (Back): REGLA MADRE / BIFURCACION / TRAMPA.
Enfoque de urgencias: ABCDE, tiempo es organo, antidotos, estabilizar y disponer.
Guia: AHA/ACLS, ESC, Surviving Sepsis, ADA, GINA, GOLD, guias de toxicologia, GPC MX.
"""
import os
import genanki

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "output")
os.makedirs(OUTPUT_DIR, exist_ok=True)

MODEL_QA_ID = 1990011901
DECK_ID_E, DECK_ID_C, DECK_ID_M = 1990011001, 1990011002, 1990011003
DECK_NAME_E = "No hay tiempo::Urgencias::1 - Ejes / patrones madre"
DECK_NAME_C = "No hay tiempo::Urgencias::2 - Manejos comunes (core)"
DECK_NAME_M = "No hay tiempo::Urgencias::3 - Menos comunes"

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
model_qa = genanki.Model(MODEL_QA_ID, "NHT Urg Manejo QA",
    fields=[{"name": "Front"}, {"name": "Back"}],
    templates=[{"name": "QA", "qfmt": "{{Front}}", "afmt": '{{Front}}<hr id="extra">{{Back}}'}],
    css=CSS_BASE)

deck_e = genanki.Deck(DECK_ID_E, DECK_NAME_E)
deck_c = genanki.Deck(DECK_ID_C, DECK_NAME_C)
deck_m = genanki.Deck(DECK_ID_M, DECK_NAME_M)
BASE_TAGS = ["urgencias", "ecoe", "no_hay_tiempo"]


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

def core(deck, t, v, c, ci, tags):
    add(deck, caso(t), manejo(v, c, ci), ["core"] + tags)

def menos(deck, t, v, c, ci, tags):
    add(deck, caso(t), manejo(v, c, ci), ["menos_comun"] + tags)


# ===================== EJES / PATRONES MADRE (8) =====================
E = ["eje"]
add(deck_e, caso("EJE 1 — ABCDE: trato primero lo que MATA, no lo que duele"),
    eje("Imagen: una escalera que no se salta. <b>A</b> via aerea (+ control cervical si trauma), <b>B</b> "
        "ventilacion/O2, <b>C</b> circulacion (2 vias, monitor, hemorragia), <b>D</b> deficit neurologico + "
        "<b>glucemia</b>, <b>E</b> exposicion/temperatura. Reevaluo desde A ante cualquier deterioro.",
        "Cada letra tiene su accion antes de pasar a la siguiente: A comprometida &rarr; abrir/asegurar via aerea; "
        "B &rarr; O2/descomprimir; C &rarr; volumen/control de sangrado; D &rarr; tratar hipoglucemia/convulsion.",
        "No saltes a la TAC ni al diagnostico fino con una via aerea o una circulacion sin resolver. La glucemia "
        "capilar es parte de la D y se mide SIEMPRE."),
    E + ["abcde"])

add(deck_e, caso("EJE 2 — ESTABLE vs INESTABLE: si esta inestable, resucito en paralelo al diagnostico"),
    eje("Imagen: dos carriles a la vez. En el inestable, el tratamiento NO espera al diagnostico: monitorizo, "
        "2 vias, O2 y trato lo amenazante mientras estudio.",
        "<b>Inestable</b> (hipotension, hipoxia, alteracion del alerta, arritmia con datos de mala perfusion) &rarr; "
        "resucitar YA. <b>Estable</b> &rarr; tengo tiempo para el workup ordenado.",
        "Mandar a un inestable a un estudio fuera del area de choque ('el tunel de la muerte') es un error. "
        "Estabiliza primero."),
    E + ["triage"])

add(deck_e, caso("EJE 3 — Alteracion del alerta: glucemia + 'coctel del coma' + descartar lo reversible"),
    eje("Imagen: abrir todas las puertas reversibles antes de la TAC. Ante un paciente con bajo nivel de alerta: "
        "<b>glucemia capilar</b> y, segun el caso, <b>O2, tiamina, naloxona</b>; protejo la via aerea.",
        "Causas (AEIOU-TIPS): Alcohol, Epilepsia/Electrolitos, Insulina (gluco), Opioides/O2, Uremia, "
        "Trauma/Temperatura, Infeccion, Psiquiatrico, Stroke/SNC. Cada una tiene su tratamiento.",
        "Da <b>tiamina antes (o con) la glucosa</b> en el desnutrido/alcoholico (Wernicke). No olvides medir la "
        "glucemia: la hipoglucemia es la causa reversible que mas se pasa por alto."),
    E + ["alteracion_alerta"])

add(deck_e, caso("EJE 4 — Dolor toracico / disnea: descarto primero LAS QUE MATAN"),
    eje("Imagen: las '5 letales' antes de la causa benigna. ECG + troponina + signos vitales + SatO2 en los "
        "primeros minutos.",
        "<b>SCA</b> (ECG/troponina), <b>TEP</b> (disnea + factores + hipoxia), <b>diseccion aortica</b> (desgarrante "
        "+ asimetria de pulsos), <b>neumotorax a tension</b> (hipotension + ausencia de ruidos + traquea desviada), "
        "<b>taponamiento</b> (Beck).",
        "ECG normal NO descarta SCA (troponina seriada). Neumotorax a tension y taponamiento se tratan SIN esperar "
        "imagen (dx clinico)."),
    E + ["dolor_toracico"])

add(deck_e, caso("EJE 5 — Choque: clasifico el TIPO y trato la causa + soporte hemodinamico"),
    eje("Imagen: cuatro motores que pueden fallar distinto. <b>Hipovolemico</b> (sangrado/perdidas), "
        "<b>distributivo</b> (septico, anafilactico, neurogenico), <b>cardiogenico</b> (bomba), <b>obstructivo</b> "
        "(taponamiento, neumotorax a tension, TEP masivo).",
        "Hipovolemico/distributivo &rarr; volumen + tratar causa (&plusmn; vasopresor). Cardiogenico &rarr; cuidado "
        "con el volumen (inotropico/revascularizar). Obstructivo &rarr; <b>quitar la obstruccion</b> "
        "(descomprimir/pericardiocentesis/trombolisis).",
        "No llenes de liquido al cardiogenico ni al obstructivo: en el obstructivo, el tratamiento es resolver la "
        "obstruccion, no el suero."),
    E + ["choque"])

add(deck_e, caso("EJE 6 — Toxicologia: trata al PACIENTE, no al toxico (ABC + antidoto + descontaminacion + soporte)"),
    eje("Imagen: primero estabilizo, luego pienso en el veneno. <b>ABC</b> + glucemia + ECG; identifico el "
        "<b>toxidrome</b>; doy <b>antidoto si existe</b>; valoro descontaminacion (carbon activado si util y via "
        "aerea segura); el resto es <b>soporte</b>.",
        "Antidotos clave: paracetamol&rarr;NAC; opioide&rarr;naloxona; benzo&rarr;flumazenil (con cautela); "
        "organofosforado&rarr;atropina+pralidoxima; tricíclico&rarr;bicarbonato; CO&rarr;O2 100%; metanol/etilenglicol"
        "&rarr;fomepizol; digoxina&rarr;Fab.",
        "La mayoria de las intoxicaciones se tratan con SOPORTE, no con antidoto. El carbon activado no se da a "
        "ciegas (riesgo de broncoaspiracion si bajo nivel de alerta)."),
    E + ["toxicologia"])

add(deck_e, caso("EJE 7 — Sepsis: bundle de 1 hora + control del FOCO"),
    eje("Imagen: el reloj de la primera hora. Sospecho infeccion + disfuncion organica y actuo ya.",
        "<b>Bundle 1 h</b>: <b>lactato</b>, <b>hemocultivos antes del antibiotico</b>, <b>antibiotico amplio "
        "espectro</b>, <b>cristaloide 30 mL/kg</b> si hipotension/lactato &ge;4, <b>noradrenalina</b> si TAM "
        "&lt;65 tras volumen. Y <b>control del foco</b>.",
        "Retrasar el antibiotico esperando estudios aumenta la mortalidad por hora. Toma cultivos, pero rapido."),
    E + ["sepsis"])

add(deck_e, caso("EJE 8 — TIEMPO ES ORGANO: las ventanas que no perdono"),
    eje("Imagen: varios cronometros corriendo a la vez. En estas, el retraso = perdida del organo o la vida; "
        "actuo con alta sospecha.",
        "<b>Anafilaxia</b> &rarr; adrenalina IM YA. <b>SCACEST</b> &rarr; reperfusion (ICP &lt;120 min). "
        "<b>ACV isquemico</b> &rarr; trombolisis/trombectomia en ventana. <b>Status</b> &rarr; benzodiacepina ya. "
        "<b>Sepsis</b> &rarr; antibiotico 1a hora. <b>Neumotorax a tension</b> &rarr; aguja.",
        "La duda NO debe retrasar el tratamiento tiempo-dependiente: la adrenalina, la reperfusion y la benzo se "
        "dan ante alta sospecha, no tras confirmar todo."),
    E + ["tiempo_organo"])


# ===================== CORE / COMUNES (18) =====================
C = ["core"]
core(deck_c, "Sindrome coronario agudo (SCA)",
     "ECG en &lt;10 min + troponina. <b>CEST</b> &rarr; <b>reperfusion</b> (ICP primaria &lt;120 min o fibrinolisis "
     "&lt;12 h) + doble antiagregacion (AAS + P2Y12) + anticoagulacion + estatina. <b>SEST</b> &rarr; antitrombotico "
     "+ <b>estratificar (GRACE)</b> + coronariografia segun riesgo. O2 solo si SatO2 &lt;90%.",
     "(urgencia) Es un infarto/angina. Lo prioritario es destapar la arteria cuanto antes (cateterismo o, si no se "
     "puede, fibrinolitico) y dar antiagregantes.",
     "ECG normal NO descarta SCA (troponina seriada). <b>NO fibrinolisis en el SEST</b>. Tiempo es musculo.", C + ["sca"])

core(deck_c, "Choque (enfoque por tipo)",
     "ABC + 2 vias + monitor + <b>lactato</b>. Clasifico (hipovolemico/distributivo/cardiogenico/obstructivo) y "
     "trato la causa + soporte: volumen (salvo cardiogenico/obstructivo) y <b>noradrenalina</b> si no responde.",
     "(urgencia) La presion y la perfusion cayeron. Reponemos volumen y damos medicamentos para sostener la "
     "presion mientras encontramos y tratamos la causa.",
     "El obstructivo (taponamiento, neumotorax a tension, TEP masivo) NO mejora con suero: <b>quita la "
     "obstruccion</b>. La hipotension es tardia (choque compensado primero).", C + ["choque"])

core(deck_c, "Paro cardiaco / RCP (ACLS)",
     "<b>RCP de alta calidad</b> (100-120/min, profundo, minima interrupcion) + via aerea/ventilacion + "
     "desfibrilar si <b>FV/TV sin pulso</b>; <b>adrenalina</b> 1 mg c/3-5 min (de inicio en no desfibrilables) + "
     "tratar <b>causas reversibles (5 H y 5 T)</b>.",
     "(urgencia) El corazon se detuvo. Lo que salva es la reanimacion de calidad y, si el ritmo lo permite, la "
     "descarga; buscamos y corregimos la causa.",
     "Desfibrilables = FV/TV sin pulso (descarga); no desfibrilables = asistolia/AESP (no se desfibrilan). "
     "5H: hipoxia, hipovolemia, H+, hipo/hiperK, hipotermia. 5T: neumotorax a Tension, Taponamiento, Toxicos, "
     "Trombosis (coronaria/pulmonar).", C + ["rcp_acls"])

core(deck_c, "ACV / ictus",
     "<b>Codigo ictus</b>: glucemia + <b>TAC de craneo URGENTE</b> (isquemico vs hemorragico) + hora de inicio. "
     "<b>Isquemico en ventana</b> &rarr; trombolisis (alteplasa/tenecteplasa) &plusmn; trombectomia. "
     "<b>Hemorragico</b> &rarr; control de TA, revertir anticoagulacion, neurocirugia.",
     "(urgencia) Es una embolia o un derrame cerebral. Cada minuto cuenta: una tomografia decide si podemos "
     "destapar la arteria con un medicamento o si es un sangrado.",
     "<b>NO des antiagregante/anticoagulante hasta la TAC</b> (descartar hemorragico). 'Tiempo es cerebro'; precisa "
     "la hora de inicio. No bajes la TA agresivamente en el isquemico (salvo limites/trombolisis).", C + ["acv"])

core(deck_c, "Status epileptico",
     "ABC + glucemia + tiempo. <b>Benzodiacepina YA</b> (lorazepam/diazepam/midazolam) como 1a linea; si persiste, "
     "<b>antiepileptico IV</b> (levetiracetam, valproato o fenitoina); refractario &rarr; <b>induccion anestesica</b> "
     "+ UCI. Buscar causa (glucosa, Na, toxico, infeccion, lesion).",
     "(urgencia) Es una convulsion que no cede o se repite sin recuperar. Damos un medicamento para cortarla de "
     "inmediato y otro para mantenerla controlada, mientras buscamos la causa.",
     "Status = crisis &ge;5 min o varias sin recuperar. La <b>benzodiacepina no se retrasa</b>. Corrige hipoglucemia "
     "e hiponatremia. Vigila depresion respiratoria.", C + ["status"])

core(deck_c, "Sepsis / shock septico",
     "<b>Bundle de 1 hora</b>: lactato, hemocultivos antes del antibiotico, <b>antibiotico amplio espectro</b>, "
     "cristaloide 30 mL/kg, <b>noradrenalina</b> si TAM &lt;65 tras volumen. <b>Control del foco</b>.",
     "(urgencia) Es una infeccion grave que afecta todo el cuerpo. Iniciamos antibiotico y sueros de inmediato y "
     "buscamos el origen para controlarlo.",
     "qSOFA &ge;2 (TA &le;100, FR &ge;22, confusion). Antibiotico en la 1a hora salva vidas. Lactato alto = "
     "hipoperfusion.", C + ["sepsis"])

core(deck_c, "Anafilaxia",
     "<b>Adrenalina IM (1:1000) en cara anterolateral del muslo, YA</b> (repetir c/5-15 min) + retirar el "
     "desencadenante + O2 + decubito con piernas elevadas + <b>liquidos IV</b>. Adyuvantes (antihistaminico, "
     "esteroide, broncodilatador) son 2a linea. Observacion (reaccion bifasica).",
     "(urgencia) Es una reaccion alergica grave. La inyeccion de adrenalina en el muslo es lo que salva la vida y "
     "se da de inmediato; lo demas es complementario.",
     "<b>La adrenalina IM es el 1er y mas importante tratamiento</b> (no el antihistaminico/esteroide). No la "
     "retrases. Vigila reaccion bifasica (puede recurrir en horas). Adrenalina IM, no IV de rutina.", C + ["anafilaxia"])

core(deck_c, "Cetoacidosis diabetica (CAD)",
     "<b>Liquidos IV (salino 0.9%) + insulina IV en infusion + reposicion de potasio</b> + tratar el "
     "desencadenante. Monitorizo glucosa, K, brecha anionica y pH.",
     "(urgencia) La diabetes se descompenso con acidos en la sangre. Reponemos liquidos, damos insulina en vena y "
     "vigilamos el potasio de cerca.",
     "<b>No inicies insulina si K &lt;3.3</b> (repon K primero &rarr; arritmia). Anade glucosa al suero al bajar de "
     "~200 para seguir cerrando la brecha.", C + ["cad"])

core(deck_c, "Estado hiperosmolar hiperglucemico (EHH)",
     "<b>Reanimacion con liquidos AGRESIVA</b> (deficit mayor que en CAD) + insulina IV + potasio + tratar el "
     "desencadenante. Glucemias muy altas, osmolaridad alta, <b>sin cetoacidosis significativa</b>.",
     "(urgencia) La glucosa subio muchisimo y deshidrato al paciente. Lo principal es reponer mucho liquido, ademas "
     "de insulina y vigilar el potasio.",
     "El pilar inicial es el LIQUIDO (mas que la insulina). Mortalidad mayor que la CAD; suele haber deterioro "
     "neurologico por la hiperosmolaridad.", C + ["ehh"])

core(deck_c, "Crisis asmatica grave",
     "<b>O2 + SABA (salbutamol) nebulizado/continuo + corticoide sistemico precoz + ipratropio</b>; "
     "<b>sulfato de magnesio IV</b> si grave/refractaria. Reevaluo; valorar VMNI/intubacion si fatiga.",
     "(urgencia) Es una crisis de asma grave. Abrimos los bronquios con nebulizaciones, damos cortisona y oxigeno; "
     "si no responde, agregamos magnesio en vena.",
     "Silencio auscultatorio, agotamiento, somnolencia o <b>PCO2 normal/alta</b> (deberia estar baja) = paro "
     "inminente. El corticoide precoz cambia el curso.", C + ["asma"])

core(deck_c, "EPOC exacerbado",
     "<b>Broncodilatadores de accion corta (SABA + SAMA) + corticoide sistemico + antibiotico si purulencia</b> + "
     "<b>O2 con meta 88-92%</b>. <b>VMNI</b> si acidosis respiratoria (pH &lt;7.35 con hipercapnia).",
     "(urgencia) Se le agravo el EPOC. Abrimos los bronquios, damos cortisona y, si la flema esta infectada, "
     "antibiotico; el oxigeno se da con cuidado y, si hace falta, una mascarilla de ventilacion.",
     "Meta de O2 88-92% (riesgo de narcosis por CO2). La <b>VMNI</b> evita la intubacion en la acidosis "
     "respiratoria.", C + ["epoc"])

core(deck_c, "Tromboembolia pulmonar (TEP)",
     "<b>Inestable / TEP masiva</b> (hipotension, choque) &rarr; <b>trombolisis</b> (o embolectomia). "
     "<b>Estable</b> &rarr; <b>anticoagulacion</b> (HBPM/ACOD). Inicio anticoagulacion empirica si alta "
     "probabilidad mientras confirmo con angio-TAC.",
     "(urgencia) Un coagulo viajo al pulmon. Si esta estable, anticoagulante; si esta en choque, un medicamento "
     "que disuelve el coagulo de inmediato.",
     "Estable se anticoagula; <b>inestable se trombolisa</b>. Usa Wells/dimero D para decidir imagen, no para "
     "descartar en alta probabilidad.", C + ["tep"])

core(deck_c, "Emergencia hipertensiva",
     "TA muy alta + <b>dano agudo de organo blanco</b> (EVC, SCA, edema pulmonar, diseccion, eclampsia, "
     "encefalopatia) &rarr; <b>antihipertensivo IV en monitor</b>, bajar TAM ~<b>10-25% en la 1a hora</b>.",
     "(urgencia) La presion esta tan alta que ya esta danando un organo. La bajamos de forma controlada en el "
     "hospital, no de golpe.",
     "Sin dano de organo es <b>urgencia</b> (no emergencia): reduccion gradual VO. Bajar demasiado rapido causa "
     "isquemia. <b>Diseccion y eclampsia</b> SI requieren bajada rapida y agresiva.", C + ["emergencia_htas"])

core(deck_c, "Intoxicaciones (enfoque general)",
     "<b>ABC + glucemia + ECG</b> + identificar <b>toxidrome</b> + <b>antidoto</b> si existe + valorar "
     "descontaminacion (<b>carbon activado</b> si reciente y via aerea segura) + soporte. Contactar centro "
     "toxicologico; niveles segun toxico (paracetamol, salicilatos, etanol).",
     "(urgencia) Primero estabilizamos (respiracion, circulacion, azucar) y luego identificamos el toxico para dar "
     "el antidoto si lo hay; en la mayoria, el soporte es el tratamiento.",
     "<b>Trata al paciente, no al toxico.</b> Carbon activado NO a ciegas (broncoaspiracion si bajo alerta). "
     "Lavado gastrico casi en desuso. Pide paracetamol SIEMPRE (silente y con antidoto).", C + ["intoxicaciones"])

core(deck_c, "Hipoglucemia",
     "<b>Consciente</b>: <b>15 g de glucosa VO</b> (regla del 15) y reevaluar. <b>Inconsciente/sin via oral</b>: "
     "<b>glucosa IV</b> (o glucagon IM si no hay acceso). Buscar y corregir la causa (insulina/sulfonilurea, ayuno, "
     "alcohol, sepsis).",
     "(urgencia) El azucar esta peligrosamente bajo. Doy azucar rapido; si no puede tragar o esta inconsciente, "
     "glucosa por vena o glucagon, y luego ajustamos el tratamiento.",
     "Mide glucemia en TODO paciente con alteracion del alerta. Sulfonilureas dan hipoglucemia prolongada/"
     "recurrente (observar/ingresar). Tiamina antes de glucosa en el alcoholico/desnutrido.", C + ["hipoglucemia"])

core(deck_c, "Hiperkalemia",
     "<b>Con cambios en ECG &rarr; gluconato de calcio IV YA</b> (estabiliza el miocardio). Luego <b>meter el K a "
     "la celula</b> (insulina + glucosa, beta-2, bicarbonato si acidosis) y <b>eliminarlo</b> (diureticos, resinas/"
     "patiromer, <b>dialisis</b>). Suspender IECA/ARA-II/ARM y aportes.",
     "(urgencia) El potasio esta alto y puede parar el corazon. Primero protegemos el corazon con calcio, luego "
     "metemos el potasio a las celulas y finalmente lo eliminamos.",
     "<b>El calcio NO baja el K</b>, solo protege la membrana (es lo primero si hay cambios en ECG). T picudas "
     "&rarr; QRS ancho &rarr; onda sinusoidal &rarr; paro.", C + ["hiperkalemia"])

core(deck_c, "Alteracion del estado de alerta / coma",
     "ABC + <b>glucemia</b> + 'coctel' segun caso (<b>tiamina, glucosa, naloxona</b>) + proteger via aerea (valorar "
     "intubacion si Glasgow &le;8) + buscar la causa (AEIOU-TIPS) con exploracion, labs, toxicos y <b>TAC</b> si "
     "focalidad/trauma.",
     "(urgencia) El paciente no responde bien. Aseguramos la respiracion, corregimos lo reversible (azucar, "
     "opioides) y buscamos la causa con estudios.",
     "Glucemia y pupilas/foco neurologico orientan rapido. <b>Glasgow &le;8 = asegurar via aerea</b>. No olvides "
     "tiamina antes de glucosa en el desnutrido.", C + ["alteracion_alerta"])

core(deck_c, "Hemorragia digestiva alta (HDA)",
     "Reanimacion (2 vias gruesas, cristaloide, <b>cruzar sangre</b>, transfusion restrictiva meta Hb ~7) + "
     "<b>IBP IV</b> + <b>endoscopia &lt;24 h</b>. Si <b>varices</b>: + vasoactivo (octreotido/terlipresina) + "
     "antibiotico (ceftriaxona) + ligadura.",
     "(urgencia) Esta sangrando del tubo digestivo alto. Lo estabilizamos con sueros/sangre y un protector gastrico, "
     "y con una endoscopia localizamos y detenemos el sangrado.",
     "Hematemesis/melena + hemodinamia. <b>Estabiliza antes de endoscopiar.</b> Hematoquecia con inestabilidad "
     "puede ser HDA masiva. En hepatopata sospecha varices (anade vasoactivo + antibiotico).", C + ["hda"])


# ===================== MENOS COMUNES (20) =====================
menos(deck_m, "Intoxicacion por paracetamol",
      "<b>N-acetilcisteina (NAC)</b> guiada por <b>nivel a las 4 h (nomograma de Rumack-Matthew)</b>; si la "
      "presentacion es tardia/masiva, no esperes el nivel para iniciar. Carbon activado si &lt;1-2 h.",
      "Es una intoxicacion por exceso de paracetamol que dana el higado, a menudo sin sintomas al inicio. Hay un "
      "antidoto (NAC) muy eficaz si se da a tiempo.",
      "Silente al inicio (el dano hepatico aparece a las 24-72 h). <b>Mide el nivel a las 4 h</b>; la NAC es casi "
      "100% eficaz si se inicia temprano (&lt;8 h).", ["tox_paracetamol"])

menos(deck_m, "Intoxicacion por opioides",
      "<b>Naloxona</b> (IM/IV/intranasal), titulada para revertir la <b>depresion respiratoria</b> (no "
      "necesariamente despertar del todo) + soporte ventilatorio. Vigilar (la naloxona dura menos que muchos "
      "opioides &rarr; puede recurrir).",
      "(urgencia) Es una sobredosis de opioides; lo peligroso es que deja de respirar. La naloxona revierte el "
      "efecto, pero hay que vigilar porque puede volver la depresion respiratoria.",
      "Toxidrome: <b>miosis + depresion respiratoria + bajo alerta</b>. La naloxona puede precipitar abstinencia; "
      "su efecto es corto (observar/repetir).", ["tox_opioides"])

menos(deck_m, "Intoxicacion por benzodiacepinas",
      "<b>Soporte (sobre todo respiratorio)</b>. <b>Flumazenil</b> solo en casos seleccionados y con cautela "
      "(<b>contraindicado si uso cronico o co-ingesta de proconvulsivantes</b> como tricíclicos: riesgo de "
      "convulsiones).",
      "Es una sobredosis de tranquilizantes; suele bastar con vigilar y apoyar la respiracion. El antidoto "
      "(flumazenil) puede ser peligroso, asi que se usa con mucho cuidado.",
      "Casi nunca matan solas (cuidado con co-ingestas). <b>Flumazenil puede provocar convulsiones</b> en "
      "dependientes o con tricíclicos: no de rutina.", ["tox_benzo"])

menos(deck_m, "Intoxicacion por organofosforados / carbamatos",
      "Descontaminacion (retirar ropa, lavar) con proteccion del personal + <b>atropina</b> (titular hasta secar "
      "secreciones) + <b>pralidoxima</b> (organofosforados) + soporte respiratorio.",
      "(urgencia) Es una intoxicacion por insecticidas que produce muchas secreciones y dificultad para respirar. "
      "La atropina las seca y hay otro antidoto que reactiva la enzima.",
      "Toxidrome <b>colinergico (DUMBELS/SLUDGE)</b>: salivacion, lagrimeo, broncorrea, miosis, diarrea, "
      "fasciculaciones. Lo que mata es la broncorrea/broncoespasmo: <b>atropina hasta secar secreciones</b>.", ["tox_organofosforados"])

menos(deck_m, "Intoxicacion por monoxido de carbono",
      "<b>Oxigeno al 100% con mascarilla con reservorio</b> (o <b>camara hiperbarica</b> si grave: perdida de "
      "conciencia, embarazo, isquemia, deficit neurologico). Retirar de la fuente.",
      "(urgencia) Es una intoxicacion por humo/gas (calentadores, incendios) que impide al cuerpo usar el oxigeno. "
      "El tratamiento es oxigeno al 100%; en casos graves, camara hiperbarica.",
      "<b>La oximetria de pulso ENGANA</b> (lee normal): pide carboxihemoglobina y gasometria. Sospecha en varios "
      "conviventes con cefalea/nausea (fuente comun).", ["tox_co"])

menos(deck_m, "Intoxicacion por antidepresivos triciclicos",
      "<b>Bicarbonato de sodio IV</b> si <b>QRS ancho</b> (&gt;100 ms) o arritmia/hipotension + soporte. "
      "Benzodiacepina para convulsiones. Carbon activado si reciente.",
      "(urgencia) Es una sobredosis grave de un antidepresivo antiguo que afecta el corazon y puede convulsionar. "
      "El bicarbonato protege el corazon.",
      "Triada: <b>cardiotoxicidad (QRS ancho) + convulsiones + anticolinergico</b>. El <b>QRS ancho</b> marca "
      "gravedad y guia el bicarbonato. Evita flumazenil (convulsiones).", ["tox_triciclicos"])

menos(deck_m, "Alcoholes toxicos (metanol / etilenglicol)",
      "<b>Fomepizol</b> (o etanol) para bloquear la alcohol-deshidrogenasa + bicarbonato + <b>dialisis</b> si grave "
      "+ cofactores (folato en metanol; tiamina/piridoxina en etilenglicol).",
      "(urgencia) Es una intoxicacion por alcoholes no bebibles (anticongelante, alcohol de quemar) que produce "
      "acidos peligrosos. Damos un antidoto que bloquea su transformacion y, si es grave, dialisis.",
      "<b>Acidosis metabolica con brecha anionica Y brecha osmolar altas</b>. Metanol &rarr; ceguera; etilenglicol "
      "&rarr; cristales de oxalato/fallo renal.", ["tox_alcoholes"])

menos(deck_m, "Intoxicacion por salicilatos (aspirina)",
      "Reanimacion + <b>bicarbonato (alcalinizacion urinaria)</b> + reposicion de K + <b>dialisis</b> si grave. "
      "Carbon activado si reciente. Vigilar glucosa y temperatura.",
      "Es una intoxicacion por aspirina. Damos bicarbonato para ayudar a eliminarla por la orina y, si es grave, "
      "dialisis.",
      "Patron clasico: <b>alcalosis respiratoria + acidosis metabolica con brecha</b> + tinnitus + hipertermia. "
      "No intubar a la ligera (la hiperventilacion compensadora es protectora).", ["tox_salicilatos"])

menos(deck_m, "Mordeduras: profilaxis antirrabica + antitetanica",
      "<b>Lavado abundante con agua y jabon</b> (medida mas eficaz) + valorar <b>antibiotico</b> "
      "(amoxi-clavulanico). <b>Antirrabica</b>: vacuna &plusmn; <b>inmunoglobulina</b> segun animal/exposicion/"
      "estado del animal. <b>Antitetanica</b>: segun herida y esquema vacunal.",
      "Limpiamos muy bien la herida (lo que mas reduce el riesgo) y decidimos vacunas: contra la rabia segun el "
      "animal y la mordida, y contra el tetanos segun sus vacunas previas.",
      "Rabia es casi 100% mortal pero PREVENIBLE: ante duda con mamifero, profilaxis. La inmunoglobulina antirrabica "
      "se infiltra en la herida. No suturar de primera intencion mordeduras de alto riesgo.", ["mordeduras"])

menos(deck_m, "Fiebre de origen desconocido (FUO)",
      "<b>Definicion + estudio escalonado dirigido por pistas</b> (historia, exploracion repetida, labs, cultivos, "
      "imagen, serologias). Evitar antibiotico/esteroide empirico a ciegas (enmascara). Causas: infeccion, "
      "neoplasia, autoinmune, miscelanea.",
      "Es fiebre prolongada sin causa clara tras un estudio inicial. Vamos buscando de forma ordenada, guiados por "
      "pistas, sin tapar el cuadro con tratamientos a ciegas.",
      "FUO clasica: fiebre &gt;3 semanas + sin dx tras estudio adecuado. <b>No des antibiotico/esteroide empirico</b> "
      "salvo inestabilidad (enmascara el dx). Reexplora seriadamente.", ["fuo"])

menos(deck_m, "Vacunacion del adulto (en urgencias / oportunidad)",
      "Aprovecho el contacto para revisar/indicar: <b>antitetanica</b> (heridas), influenza, neumococo, "
      "Td/Tdap, hepatitis B, segun edad/riesgo/exposicion. En herida potencialmente tetanigena, profilaxis segun "
      "estado vacunal.",
      "Aprovecho la consulta de urgencia para poner al dia las vacunas que correspondan, sobre todo el refuerzo del "
      "tetanos si hay una herida.",
      "Herida limpia y &lt;3 dosis o desconocido &rarr; vacuna. Herida sucia/tetanigena: vacuna + valorar "
      "<b>inmunoglobulina antitetanica</b> si esquema incompleto/desconocido.", ["vacunas_adulto"])

menos(deck_m, "Golpe de calor",
      "<b>Enfriamiento RAPIDO y agresivo</b> (inmersion en agua fria o evaporativo) hasta ~39 C + ABC + liquidos + "
      "tratar complicaciones (rabdomiolisis, CID, fallo organico).",
      "(urgencia) El cuerpo se sobrecalento y falla; lo prioritario es <b>bajar la temperatura ya</b> con metodos "
      "fisicos, ademas de sueros y soporte.",
      "<b>Hipertermia (&gt;40 C) + alteracion del estado mental + anhidrosis (en el clasico)</b>. Los antitermicos "
      "NO sirven (no es fiebre). El enfriamiento fisico es el tratamiento.", ["golpe_calor"])

menos(deck_m, "Hipotermia",
      "<b>Recalentamiento</b> (externo pasivo/activo; interno si grave) + manejo cuidadoso (riesgo de arritmia) + "
      "ABC. RCP prolongada en paro (no declarar muerte hasta recalentar).",
      "(urgencia) La temperatura corporal bajo demasiado. Lo recalentamos de forma gradual y lo movemos con "
      "cuidado, porque el corazon es muy irritable.",
      "<b>'No esta muerto hasta que esta caliente y muerto'</b>: continua RCP hasta recalentar. Manipulacion brusca "
      "&rarr; fibrilacion. Onda J de Osborn en el ECG.", ["hipotermia"])

menos(deck_m, "Atragantamiento / OVACE en el adulto",
      "<b>Tos efectiva</b> &rarr; animar a toser, NO intervenir. <b>Tos inefectiva consciente</b> &rarr; "
      "<b>5 golpes interescapulares + 5 compresiones abdominales (Heimlich)</b>, alternando. "
      "<b>Inconsciente</b> &rarr; RCP.",
      "(urgencia) Si algo obstruye la via aerea y la persona tose bien, la dejamos toser. Si no puede, alternamos "
      "golpes en la espalda y compresiones abdominales; si se desmaya, iniciamos reanimacion.",
      "Signo universal (manos al cuello). <b>NO barrido digital a ciegas</b>. En embarazada/obeso: compresiones "
      "toracicas en vez de abdominales.", ["atragantamiento"])

menos(deck_m, "Sincope (enfoque en urgencias)",
      "ECG + glucemia + TA en bipedestacion. Estratifico riesgo: <b>bajo</b> (vasovagal, prodromos, gatillo) &rarr; "
      "alta + educacion; <b>alto</b> (cardiaco) &rarr; monitor/ingreso y estudio.",
      "Es un desmayo. La mayoria es benigno; revisamos el corazon (ECG) para descartar una causa peligrosa que "
      "requiera vigilancia.",
      "Banderas de sincope cardiaco (ingreso): <b>de esfuerzo, en supino, sin prodromos, palpitaciones, cardiopatia, "
      "ECG anormal, muerte subita familiar</b>.", ["sincope"])

menos(deck_m, "Neumotorax a tension",
      "Dx <b>CLINICO</b> (no esperar Rx): <b>descompresion inmediata con aguja</b> (2&ordm; EIC linea "
      "medioclavicular o 5&ordm; EIC linea axilar anterior) &rarr; luego <b>tubo de torax</b>.",
      "(urgencia) Hay aire a presion comprimiendo el pulmon y el corazon; lo libero con una aguja de inmediato y "
      "luego coloco un tubo.",
      "Hipotension + ingurgitacion yugular + ausencia de ruidos + desviacion traqueal. <b>NO esperes imagen.</b> "
      "Es una causa de choque obstructivo y de paro (5T).", ["neumotorax_tension"])

menos(deck_m, "Taponamiento cardiaco",
      "<b>Pericardiocentesis</b> (descompresion) + liquidos como puente. FAST/eco confirma liquido pericardico.",
      "(urgencia) Hay liquido alrededor del corazon que no lo deja llenarse; hay que drenarlo de inmediato para que "
      "vuelva a bombear.",
      "<b>Triada de Beck</b> (hipotension + ingurgitacion yugular + ruidos velados) + <b>pulso paradojico</b>. "
      "Causa de choque obstructivo y AESP (5T).", ["taponamiento"])

menos(deck_m, "Hemorragia masiva / transfusion masiva (enlace Trauma)",
      "Control de la hemorragia + <b>protocolo de transfusion masiva 1:1:1</b> (plasma:plaquetas:concentrados) + "
      "<b>acido tranexamico &lt;3 h</b> + <b>hipotension permisiva</b> (salvo TCE) + corregir la <b>triada letal</b> "
      "(hipotermia, acidosis, coagulopatia).",
      "(urgencia) Perdio mucha sangre. Reponemos sangre y derivados de forma equilibrada mientras detenemos el "
      "sangrado, evitando enfriarlo y diluir sus factores de coagulacion.",
      "Reanimar solo con cristaloides diluye factores y empeora el sangrado. TXA &lt;3 h. Detalle en el deck de "
      "Cirugia/Trauma.", ["transfusion_masiva"])

menos(deck_m, "Quemaduras (enlace Cirugia)",
      "ABC (<b>via aerea</b> si sospecha de inhalacion) + <b>reanimacion con liquidos (Parkland)</b> en quemaduras "
      "extensas + analgesia + cuidado de la herida + profilaxis antitetanica. Referir a centro de quemados segun "
      "criterios.",
      "(urgencia) Segun la extension y profundidad reponemos liquidos calculados, controlamos el dolor y cuidamos "
      "la herida; vigilamos la via aerea si hubo humo.",
      "<b>Sospecha de lesion de via aerea</b> (humo, hollin, esputo carbonaceo, estridor) &rarr; intubar pronto "
      "(antes de que edematice). Calcula superficie quemada (regla de los 9). Detalle en Cirugia.", ["quemaduras"])

menos(deck_m, "Diseccion aortica",
      "Control de FC y TA: <b>betabloqueante IV (esmolol/labetalol) PRIMERO</b> (meta FC &lt;60, TAS 100-120), luego "
      "vasodilatador + analgesia. <b>Tipo A &rarr; cirugia urgente</b>; <b>Tipo B no complicada &rarr; manejo "
      "medico</b>.",
      "(urgencia) Se desgarro la pared de la arteria principal. Bajamos con cuidado el pulso y la presion; segun "
      "donde sea, requiere cirugia inmediata o tratamiento medico.",
      "Dolor toracico <b>desgarrante que migra a la espalda</b> + <b>asimetria de pulsos/TA</b> + mediastino ancho. "
      "<b>Betabloqueante ANTES que el vasodilatador</b> (evita taquicardia refleja).", ["diseccion"])


def build():
    for d, f in [(deck_e, "Manejo_01_Ejes.apkg"), (deck_c, "Manejo_02_Core.apkg"), (deck_m, "Manejo_03_Menos.apkg")]:
        genanki.Package(d).write_to_file(os.path.join(OUTPUT_DIR, f))
        print(f"  -> {f} ({len(d.notes)} notas)")
    genanki.Package([deck_e, deck_c, deck_m]).write_to_file(
        os.path.join(OUTPUT_DIR, "No_Hay_Tiempo_Urg_Manejo_TODOS.apkg"))
    print(f"  -> TODOS ({sum(len(d.notes) for d in [deck_e, deck_c, deck_m])} notas)")


if __name__ == "__main__":
    build()
