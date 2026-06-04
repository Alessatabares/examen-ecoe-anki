"""No hay tiempo / Cirugia — PILAR MANEJO (ejes/patrones madre + core + menos).

Carta de manejo (Back): VERBALIZO (al sinodal) / CONDUCTA-CONSEJERIA / CIERRE (red flag).
Carta de eje (Back): REGLA MADRE / BIFURCACION / TRAMPA.
Guia: ATLS, GPC mexicanas, Sabiston/Schwartz, Surviving Sepsis, Tokyo (biliar).
"""
import os
import genanki

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "output")
os.makedirs(OUTPUT_DIR, exist_ok=True)

MODEL_QA_ID = 1990006001
DECK_ID_E, DECK_ID_C, DECK_ID_M = 1990005001, 1990005002, 1990005003
DECK_NAME_E = "No hay tiempo::Cirugia::1 - Ejes / patrones madre"
DECK_NAME_C = "No hay tiempo::Cirugia::2 - Manejos comunes (core)"
DECK_NAME_M = "No hay tiempo::Cirugia::3 - Menos comunes"

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
model_qa = genanki.Model(MODEL_QA_ID, "NHT Cir Manejo QA",
    fields=[{"name": "Front"}, {"name": "Back"}],
    templates=[{"name": "QA", "qfmt": "{{Front}}", "afmt": '{{Front}}<hr id="extra">{{Back}}'}],
    css=CSS_BASE)

deck_e = genanki.Deck(DECK_ID_E, DECK_NAME_E)
deck_c = genanki.Deck(DECK_ID_C, DECK_NAME_C)
deck_m = genanki.Deck(DECK_ID_M, DECK_NAME_M)
BASE_TAGS = ["cirugia", "ecoe", "no_hay_tiempo"]


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


# ===================== EJES / PATRONES MADRE (7) =====================
E = ["eje"]
add(deck_e, caso("EJE 1 — ABCDE: trato primero lo que MATA, no lo que duele"),
    eje("Imagen: una escalera que no se salta. <b>A</b> via aerea + control cervical, <b>B</b> ventilacion, "
        "<b>C</b> circulacion/hemorragia, <b>D</b> deficit neurologico, <b>E</b> exposicion. Reevaluo desde A ante deterioro.",
        "Lo que mata en B: <b>neumotorax a tension, hemotorax masivo, torax inestable, neumotorax abierto</b>.<br>"
        "Lo que mata en C: <b>hemorragia</b> (externa, torax, abdomen, pelvis, huesos largos).",
        "El neumotorax a tension y el tamponade se tratan <b>SIN esperar imagen</b> (dx clinico)."),
    E + ["atls"])

add(deck_e, caso("EJE 2 — ESTABLE vs INESTABLE decide TAC vs QUIROFANO"),
    eje("Imagen: una balanza con la TA. <b>Inestable que no responde a reanimacion &rarr; quirofano YA</b> "
        "(no pierdas tiempo en TAC). <b>Estable &rarr; imagen (TAC)</b> para caracterizar y decidir.",
        "Trauma penetrante con inestabilidad/evisceracion/peritonitis &rarr; laparotomia. "
        "Estable &rarr; TAC y manejo selectivo.<br>"
        "FAST+ inestable &rarr; quirofano; FAST equivoco estable &rarr; TAC.",
        "Nunca mandes al TAC a un paciente inestable: 'el TAC es el tunel de la muerte'."),
    E + ["triage"])

add(deck_e, caso("EJE 3 — Hemorragia: control de dano + reanimacion equilibrada"),
    eje("Imagen: tapar la fuga mientras repones. <b>Control de la hemorragia</b> (compresion/torniquete/quirofano/angio) "
        "+ <b>protocolo de transfusion masiva 1:1:1</b> (plasma:plaquetas:concentrados) + <b>acido tranexamico</b> &lt;3 h.",
        "<b>Hipotension permisiva</b> (TAS ~90) hasta controlar el sangrado (salvo TCE). "
        "Evitar cristaloides en exceso. Corregir la <b>triada letal</b>: hipotermia, acidosis, coagulopatia.",
        "Reanimar con litros de cristaloide diluye factores y empeora el sangrado: prioriza hemoderivados."),
    E + ["hemorragia"])

add(deck_e, caso("EJE 4 — Abdomen agudo: si hay IRRITACION PERITONEAL, va a quirofano"),
    eje("Imagen: el abdomen 'en tabla'. <b>Defensa involuntaria + rebote (Blumberg) + rigidez</b> = peritonitis = "
        "exploracion quirurgica. La pregunta no es 'que tiene' sino '<b>tiene abdomen quirurgico?</b>'.",
        "<b>Peritonitis/perforacion/isquemia</b> &rarr; laparotomia.<br>"
        "<b>Inflamacion localizada sin peritonitis</b> (diverticulitis no complicada) &rarr; manejo medico.",
        "El neumoperitoneo (aire libre subdiafragmatico) = vispera perforada &rarr; quirofano."),
    E + ["abdomen_agudo"])

add(deck_e, caso("EJE 5 — Obstruccion: descomprimo y vigilo ESTRANGULACION"),
    eje("Imagen: una tuberia tapada que se vigila. <b>NPO + SNG (descompresion) + liquidos + electrolitos</b>, "
        "y busco datos de estrangulacion/isquemia.",
        "<b>Simple/parcial</b> &rarr; manejo conservador y vigilo.<br>"
        "<b>Completa, asa cerrada, estrangulacion, hernia incarcerada, sin resolver en 48 h</b> &rarr; cirugia.",
        "Datos de estrangulacion = urgencia: dolor continuo, fiebre, taquicardia, <b>lactato alto</b>, peritonismo."),
    E + ["obstruccion"])

add(deck_e, caso("EJE 6 — Sepsis quirurgica: control del FOCO manda"),
    eje("Imagen: cerrar la llave de la infeccion. <b>Bundle de 1 hora</b>: lactato, hemocultivos, "
        "<b>antibiotico de amplio espectro</b>, cristaloide 30 mL/kg, vasopresor si TAM &lt;65 tras volumen. "
        "Y lo definitivo: <b>control del foco</b> (drenar/resecar/desbridar).",
        "Absceso &rarr; drenar; viscera perforada &rarr; cirugia; tejido necrotico &rarr; desbridar; "
        "via infectada &rarr; retirar.",
        "Antibiotico sin control del foco fracasa: en cirugia, el dreno/bisturi es parte del 'antibiotico'."),
    E + ["sepsis"])

add(deck_e, caso("EJE 7 — Tiempo = tejido: las urgencias que el reloj mata"),
    eje("Imagen: un cronometro corriendo sobre un organo. En estas el retraso = perdida del organo o muerte; "
        "se actua antes de tener todo el estudio.",
        "<b>Torsion testicular/ovarica</b> (&lt;6 h), <b>isquemia mesenterica</b>, <b>fascitis necrotizante</b>, "
        "<b>sindrome compartimental</b>, <b>diseccion aortica tipo A</b>, <b>AAA roto</b>.",
        "Ante sospecha, la imagen NO debe retrasar el quirofano: se opera con alta sospecha clinica."),
    E + ["tiempo_tejido"])


# ===================== CORE / COMUNES (18) =====================
C = ["core"]
add(deck_c, caso("Apendicitis aguda"),
    manejo("Reanimacion + analgesia + <b>antibiotico</b> (cobertura gram- y anaerobios) + <b>apendicectomia</b> "
           "(laparoscopica de eleccion). NPO, liquidos.",
           "Tiene apendicitis; el tratamiento es una cirugia para retirar el apendice, generalmente por laparoscopia. "
           "Le doy antibiotico y algo para el dolor mientras preparamos quirofano.",
           "No retrasar: el riesgo es perforacion &rarr; peritonitis. Embarazada: dolor mas alto, igual va a cirugia."),
    C + ["apendicitis"])

add(deck_c, caso("Colecistitis aguda"),
    manejo("NPO + liquidos + analgesia + <b>antibiotico</b>; <b>colecistectomia laparoscopica temprana (&lt;72 h)</b>. "
           "Colecistostomia percutanea si alto riesgo quirurgico.",
           "Es una inflamacion de la vesicula por una piedra. El tratamiento es retirarla con cirugia, idealmente "
           "pronto; mientras, antibiotico y ayuno.",
           "Murphy +. Si aparece ictericia/fiebre alta con escalofrios, sospecha colangitis (otra cosa)."),
    C + ["colecistitis"])

add(deck_c, caso("Colangitis aguda"),
    manejo("Reanimacion + <b>antibiotico IV</b> + <b>descompresion biliar urgente por CPRE</b> (drenaje de la via). "
           "Es una urgencia (puede ir a sepsis/choque).",
           "La via biliar esta obstruida e infectada. Hay que dar antibiotico y, lo mas importante, destapar la via "
           "con un procedimiento endoscopico (CPRE) cuanto antes.",
           "<b>Triada de Charcot</b> (fiebre+ictericia+dolor); <b>pentada de Reynolds</b> (+hipotension+confusion) = grave."),
    C + ["colangitis"])

add(deck_c, caso("Pancreatitis aguda"),
    manejo("<b>Reanimacion con liquidos</b>, analgesia, antiemeticos, <b>NPO con reinicio precoz</b> de la via oral "
           "segun tolerancia. Trato la causa: <b>biliar &rarr; colecistectomia en el mismo ingreso</b>; CPRE si "
           "obstruccion/colangitis. <b>No antibiotico de rutina</b>.",
           "Es una inflamacion del pancreas, casi siempre por piedras o alcohol. El tratamiento principal es "
           "hidratacion, control del dolor y reposo intestinal; vigilamos la gravedad.",
           "Antibiotico solo si necrosis infectada. Vigilo falla organica (gravedad) las primeras 48 h."),
    C + ["pancreatitis"])

add(deck_c, caso("Diverticulitis aguda"),
    manejo("<b>No complicada:</b> reposo intestinal + analgesia &plusmn; antibiotico (manejo ambulatorio en casos leves). "
           "<b>Complicada:</b> absceso &rarr; <b>drenaje percutaneo</b>; perforacion/peritonitis &rarr; <b>cirugia</b> (Hinchey).",
           "Es una inflamacion de pequenas bolsas del colon. Si es leve, se maneja con reposo del intestino y a veces "
           "antibiotico; si hay absceso o perforacion, requiere drenaje o cirugia.",
           "Colonoscopia <b>tras resolver</b> (no en agudo) para descartar cancer."),
    C + ["diverticulitis"])

add(deck_c, caso("Obstruccion intestinal (alta y baja)"),
    manejo("<b>NPO + SNG (descompresion) + liquidos + correccion de electrolitos</b> + vigilancia. "
           "<b>Cirugia</b> si: estrangulacion, asa cerrada, hernia incarcerada, completa que no resuelve.",
           "El intestino esta obstruido. Empezamos descomprimiendo con una sonda y reponiendo liquidos; muchas se "
           "resuelven asi. Si hay riesgo de que el asa se dane, se opera.",
           "Alta (delgado): vomito temprano, distension menor. Baja (colon): distension marcada, vomito tardio/fecaloide."),
    C + ["obstruccion"])

add(deck_c, caso("Perforacion de viscera hueca"),
    manejo("Reanimacion + <b>antibiotico de amplio espectro</b> + analgesia + SNG + <b>cirugia (laparotomia/lavado y "
           "reparacion)</b>. NPO.",
           "Se perforo una parte del tubo digestivo y su contenido paso al abdomen. Es una urgencia quirurgica: hay "
           "que operar para limpiar y reparar.",
           "<b>Neumoperitoneo</b> (aire libre bajo el diafragma en Rx de pie) confirma la sospecha."),
    C + ["perforacion"])

add(deck_c, caso("HDA por ulcera peptica"),
    manejo("Reanimacion (2 vias, cristaloide, cruzar sangre) + <b>IBP IV en infusion</b> + <b>endoscopia &lt;24 h</b> "
           "(diagnostica y terapeutica: clip/termo/inyeccion). Erradico <b>H. pylori</b> y suspendo AINE.",
           "Esta sangrando por una ulcera del estomago/duodeno. Le reponemos volumen y damos un protector gastrico "
           "potente; con una endoscopia localizamos y detenemos el sangrado.",
           "Transfusion restrictiva (meta Hb ~7). Si la endoscopia falla &rarr; angioembolizacion o cirugia."),
    C + ["hda_ulcera"])

add(deck_c, caso("HDA por varices esofagicas"),
    manejo("Reanimacion + <b>farmaco vasoactivo (octreotido/terlipresina)</b> + <b>antibiotico profilactico "
           "(ceftriaxona)</b> + <b>ligadura endoscopica con bandas</b>. Transfusion restrictiva (Hb ~7).",
           "El sangrado viene de venas dilatadas del esofago por la enfermedad del higado. Damos medicamentos para "
           "bajar la presion de esas venas, antibiotico, y las ligamos por endoscopia.",
           "Si falla: balon de Sengstaken (puente) &rarr; <b>TIPS</b>. El antibiotico mejora supervivencia."),
    C + ["hda_varices"])

add(deck_c, caso("Hemorragia digestiva baja (HDB)"),
    manejo("Reanimacion + estabilizar. <b>Colonoscopia</b> (dx y tratamiento) tras preparacion; si <b>masiva/inestable</b> "
           "&rarr; <b>angio-TAC + angioembolizacion</b> (o cirugia). Descarto origen alto con SNG/endoscopia si dudas.",
           "Esta sangrando por la parte baja del tubo digestivo. Lo estabilizamos y buscamos el punto con una "
           "colonoscopia; si el sangrado es muy intenso, lo localizamos y tapamos por arteriografia.",
           "Hematoquecia abundante puede ser HDA masiva: si inestable, descarta origen alto primero."),
    C + ["hdb"])

add(deck_c, caso("Neumotorax a tension"),
    manejo("Dx <b>CLINICO</b> (no esperar Rx): <b>descompresion inmediata con aguja</b> (2&ordm; EIC linea medioclavicular "
           "o 5&ordm; EIC linea axilar anterior) &rarr; luego <b>tubo de torax</b>.",
           "(urgencia, se actua de inmediato) Hay aire a presion comprimiendo el pulmon y el corazon; lo libero con "
           "una aguja ahora mismo y luego coloco un tubo.",
           "Signos: hipotension + ingurgitacion yugular + ausencia de ruidos + desviacion traqueal. NO esperes imagen."),
    C + ["neumotorax_tension"])

add(deck_c, caso("Taponamiento cardiaco"),
    manejo("Reanimacion + <b>pericardiocentesis</b> (descompresion) o <b>toracotomia</b> si trauma penetrante. "
           "FAST confirma liquido pericardico.",
           "(urgencia) Hay sangre alrededor del corazon que no lo deja llenarse; necesito drenarla de inmediato para "
           "que vuelva a bombear.",
           "<b>Triada de Beck</b>: hipotension + ingurgitacion yugular + ruidos cardiacos velados."),
    C + ["tamponade"])

add(deck_c, caso("Hemotorax masivo"),
    manejo("<b>Tubo de torax</b> + reanimacion con hemoderivados. <b>Toracotomia</b> si: drenaje inicial &gt;1500 mL "
           "o &gt;200 mL/h por 2-4 h, o inestabilidad persistente.",
           "(urgencia) Hay mucha sangre en el torax comprimiendo el pulmon; coloco un tubo para drenarla y repongo "
           "sangre; si sale demasiada, hay que operar.",
           "Es a la vez problema de B (ventilacion) y de C (hemorragia): repon volumen al drenar."),
    C + ["hemotorax"])

add(deck_c, caso("Choque hipovolemico / reanimacion"),
    manejo("ABC + <b>2 vias gruesas</b> + control de la hemorragia + <b>hemoderivados (protocolo masivo 1:1:1)</b> + "
           "TXA &lt;3 h. Identifico el origen del sangrado (torax, abdomen, pelvis, huesos, externo).",
           "(urgencia) Perdio mucha sangre y la presion cayo; repongo volumen y sangre mientras encuentro y detengo "
           "el sangrado.",
           "Clase III-IV: taquicardia + hipotension + oliguria + alteracion del estado mental. No solo cristaloides."),
    C + ["choque"])

add(deck_c, caso("Aneurisma de aorta abdominal (AAA) roto"),
    manejo("<b>Reanimacion hipotensiva</b> + cruzar sangre + <b>cirugia/EVAR INMEDIATA</b>. Si <b>inestable, al "
           "quirofano SIN esperar TAC</b>; TAC angio solo si estable.",
           "(urgencia vital) Se rompio un aneurisma de la arteria principal del abdomen; necesita cirugia de "
           "emergencia ahora.",
           "Triada: <b>dolor abdominal/lumbar + masa pulsatil + hipotension</b>. No retrasar por imagen si inestable."),
    C + ["aaa"])

add(deck_c, caso("Isquemia mesenterica aguda"),
    manejo("Reanimacion + <b>anticoagulacion</b> + <b>angio-TAC</b> + <b>revascularizacion</b> (endovascular/cirugia) y "
           "<b>reseccion del intestino necrotico</b>. Antibiotico de amplio espectro.",
           "Se obstruyo el riego del intestino y el tejido se esta danando; es una urgencia para restablecer el flujo "
           "y retirar lo que ya no es viable.",
           "<b>Dolor desproporcionado</b> a la exploracion + <b>lactato alto</b> + factor embolico (FA). El tiempo es tejido."),
    C + ["isquemia_mesenterica"])

add(deck_c, caso("Peritonitis"),
    manejo("Reanimacion + <b>antibiotico de amplio espectro</b> + analgesia + <b>cirugia (control del foco + lavado)</b>. "
           "NPO, SNG, Foley para vigilar diuresis.",
           "Hay una infeccion generalizada dentro del abdomen. Necesita antibiotico y casi siempre cirugia para "
           "limpiar y resolver la causa.",
           "Abdomen 'en tabla' (rigidez + rebote difuso) = peritonitis difusa &rarr; quirofano."),
    C + ["peritonitis"])

add(deck_c, caso("Sepsis / choque septico"),
    manejo("<b>Bundle de 1 hora</b>: lactato, <b>2 hemocultivos antes del antibiotico</b>, <b>antibiotico amplio "
           "espectro</b>, <b>cristaloide 30 mL/kg</b>, vasopresor (noradrenalina) si TAM &lt;65 tras volumen. "
           "<b>Control del foco</b> en cuanto sea posible.",
           "(a la familia) Tiene una infeccion grave que afecta todo el cuerpo; iniciamos antibiotico y sueros de "
           "inmediato y buscamos el origen para controlarlo.",
           "qSOFA &ge;2 (TA &le;100, FR &ge;22, confusion) identifica riesgo. Antibiotico en la 1a hora salva vidas."),
    C + ["sepsis"])


# ===================== MENOS COMUNES (17) =====================
M = ["menos_comun"]
def menos(deck, t, v, c, ci, tags):
    add(deck, caso(t), manejo(v, c, ci), M + tags)

menos(deck_m, "Trauma abdominal penetrante",
      "<b>Inestable / evisceracion / peritonitis / empalamiento</b> &rarr; <b>laparotomia</b>. "
      "<b>Estable</b> &rarr; TAC y manejo selectivo (observacion); herida por arma de fuego suele ir a cirugia.",
      "(urgencia) Segun como esta de estable decidimos: si esta inestable o con signos de irritacion, va directo a "
      "cirugia; si esta estable, hacemos TAC para decidir.",
      "Evisceracion o inestabilidad = quirofano, no TAC.", ["trauma_penetrante"])

menos(deck_m, "Trauma abdominal cerrado",
      "ABCDE. <b>Inestable + FAST+</b> &rarr; <b>laparotomia</b>. <b>Estable</b> &rarr; <b>TAC con contraste</b>; "
      "manejo no operatorio de lesiones de organo solido si estable.",
      "(urgencia) Buscamos sangrado interno. Si esta inestable, operamos; si esta estable, el TAC nos dice si hay "
      "lesion de bazo o higado para vigilar u operar.",
      "FAST+ inestable = quirofano. FAST no descarta lesion de viscera hueca.", ["trauma_cerrado"])

menos(deck_m, "Lesion esplenica (signo de Kehr)",
      "FAST/TAC. <b>Estable</b> &rarr; manejo no operatorio + vigilancia &plusmn; <b>angioembolizacion</b>. "
      "<b>Inestable</b> &rarr; <b>esplenectomia</b>. Vacunas post-esplenectomia (encapsulados).",
      "(urgencia) El bazo esta lesionado y sangra. Si esta estable lo vigilamos; si no, hay que operar y a veces "
      "retirarlo.",
      "<b>Signo de Kehr</b>: dolor referido al hombro <b>izquierdo</b> por sangre subdiafragmatica.", ["esplenica"])

menos(deck_m, "Torax inestable (volet costal / flail chest)",
      "<b>Analgesia potente</b> + higiene pulmonar + O2; <b>intubacion/ventilacion</b> si insuficiencia respiratoria. "
      "Lo que mata es la <b>contusion pulmonar</b> subyacente.",
      "(urgencia) Varias costillas rotas hacen que una parte del torax se mueva al reves; controlamos el dolor para "
      "que respire bien y vigilamos el pulmon.",
      "Movimiento paradojico. El problema real es la contusion pulmonar, no las costillas.", ["torax_inestable"])

menos(deck_m, "Fractura pelvica (inestable)",
      "<b>Faja/cinturon pelvico</b> (cierra el anillo) + reanimacion con hemoderivados + TXA. Sangrado persistente "
      "&rarr; <b>angioembolizacion</b> o <b>packing preperitoneal</b>. Fijacion ortopedica.",
      "(urgencia) La pelvis rota puede sangrar mucho; le colocamos una faja para cerrarla y reponemos sangre; si "
      "sigue sangrando, lo tapamos por arteriografia.",
      "No 'balancear' la pelvis repetidamente (moviliza coagulos). Foley solo si no hay lesion uretral.", ["fractura_pelvica"])

menos(deck_m, "Volvulo (sigmoides / ciego)",
      "<b>Sigmoides:</b> <b>descompresion endoscopica + sonda rectal</b>; cirugia si gangrena/recurrencia. "
      "<b>Ciego:</b> <b>cirugia</b> (reseccion). Reanimacion + NPO + SNG.",
      "El intestino se torcio sobre si mismo. En el sigmoides muchas veces se destuerce por endoscopia; en el ciego "
      "suele requerir cirugia.",
      "Rx: imagen en <b>grano de cafe</b>. Si hay peritonismo/gangrena &rarr; cirugia directa.", ["volvulo"])

menos(deck_m, "Hernia incarcerada / estrangulada",
      "<b>Incarcerada reductible sin sufrimiento:</b> intento de reduccion + cirugia electiva. "
      "<b>Estrangulada</b> (dolor, eritema, no reduce, signos sistemicos) &rarr; <b>cirugia URGENTE</b> (no reducir a la fuerza).",
      "La hernia se atoro. Si se puede reintroducir sin dano, se programa cirugia; si el asa esta sufriendo, hay que "
      "operar de urgencia.",
      "No reducir una hernia estrangulada (metes intestino necrotico al abdomen).", ["hernia"])

menos(deck_m, "Ileo paralitico",
      "<b>Tratar la causa</b> (posoperatorio, electrolitos -K+-, opioides, sepsis, isquemia) + NPO + SNG + liquidos + "
      "<b>corregir electrolitos</b> + movilizacion. Suele ser autolimitado.",
      "El intestino esta 'dormido', sin movimiento, por una causa de fondo. Lo descomprimimos y corregimos la causa; "
      "casi siempre se recupera solo.",
      "Diferencia con obstruccion mecanica: en ileo NO hay punto de obstruccion y los RHA estan <b>ausentes</b>.", ["ileo"])

menos(deck_m, "Obstruccion en asa cerrada (closed loop)",
      "<b>Urgencia quirurgica</b>: el segmento ocluido en dos puntos se distiende e <b>isquemiza rapido</b>. "
      "Reanimacion + antibiotico + <b>cirugia sin demora</b>.",
      "(urgencia) Un tramo de intestino quedo cerrado por dos lados y se daña muy rapido; hay que operar pronto.",
      "Alta sospecha de estrangulacion: no la manejes como obstruccion simple.", ["asa_cerrada"])

menos(deck_m, "Absceso intraabdominal",
      "<b>Drenaje percutaneo guiado por imagen</b> (1ra eleccion) + <b>antibiotico</b>. Drenaje quirurgico si "
      "inaccesible/multiloculado o falla.",
      "Hay una coleccion de pus encapsulada. El tratamiento es drenarla, casi siempre con una aguja guiada por "
      "imagen, ademas de antibiotico.",
      "Antibiotico solo, sin drenar el absceso, no resuelve (control del foco).", ["absceso"])

menos(deck_m, "Fascitis necrotizante",
      "<b>Desbridamiento quirurgico URGENTE y amplio</b> + <b>antibiotico de amplio espectro</b> (carbapenem + "
      "clindamicina) + reanimacion. Reintervenciones programadas ('second look').",
      "(urgencia vital) Es una infeccion que destruye el tejido muy rapido; hay que llevarlo a cirugia ya para "
      "retirar todo el tejido danado, junto con antibioticos potentes.",
      "Dolor desproporcionado, crepitos, ampollas, necrosis, toxicidad sistemica. <b>La cirugia no espera al cultivo</b>.", ["fascitis"])

menos(deck_m, "Gangrena (isquemica / gaseosa)",
      "<b>Seca/isquemica:</b> revascularizar si viable; amputacion del tejido no viable. <b>Gaseosa (Clostridium):</b> "
      "<b>desbridamiento urgente</b> + penicilina + clindamicina &plusmn; camara hiperbarica.",
      "El tejido perdio su riego y murio. Hay que retirar lo no viable y, si se puede, restaurar la circulacion; la "
      "gangrena gaseosa es una urgencia infecciosa.",
      "Gas en tejidos + dolor intenso + toxicidad = gangrena gaseosa &rarr; quirofano inmediato.", ["gangrena"])

menos(deck_m, "Torsion testicular",
      "<b>URGENCIA</b>: <b>exploracion quirurgica inmediata + orquidopexia bilateral</b> (no esperar Doppler si la "
      "clinica es clara). Detorsion manual como puente.",
      "(urgencia, &lt;6 h) El testiculo se torcio y perdio su riego; hay que operar de inmediato para salvarlo y fijar "
      "ambos lados.",
      "Ventana ~6 h. <b>Reflejo cremasterico ausente</b>; no pierdas tiempo: la cirugia manda sobre la imagen.", ["torsion_testicular"])

menos(deck_m, "Torsion ovarica",
      "<b>Cirugia (laparoscopia) urgente: detorsion y preservacion del ovario</b> (aunque se vea oscuro). "
      "Quistectomia si hay quiste causante.",
      "(urgencia) El ovario se torcio y se quedo sin riego; operamos pronto para destorcerlo y, casi siempre, "
      "conservarlo.",
      "Dolor pelvico subito + masa anexial; Doppler puede ser normal. La sospecha clinica indica cirugia.", ["torsion_ovarica"])

menos(deck_m, "Diseccion aortica",
      "Control de TA y FC: <b>betabloqueante IV (esmolol/labetalol)</b> primero (meta FC &lt;60, TAS 100-120), luego "
      "vasodilatador. <b>Tipo A &rarr; cirugia</b>; <b>Tipo B no complicada &rarr; manejo medico</b>.",
      "Se desgarro la capa interna de la arteria principal. Hay que bajar con cuidado la presion y el pulso; segun "
      "donde sea el desgarro, requiere cirugia o tratamiento medico.",
      "Dolor toracico <b>desgarrante</b> que migra a la espalda + asimetria de pulsos/TA + mediastino ancho. "
      "Betabloqueante ANTES que vasodilatador.", ["diseccion_aortica"])

menos(deck_m, "Sindrome compartimental agudo (extremidad)",
      "<b>Fasciotomia urgente</b>. Retirar vendajes/yesos compresivos, alinear, analgesia. No esperar a que "
      "desaparezca el pulso (es signo tardio).",
      "(urgencia) La presion dentro del compartimento muscular esta cortando la circulacion; hay que abrir la fascia "
      "de inmediato para salvar el miembro.",
      "<b>6 P</b>: dolor (desproporcionado y al estiramiento pasivo), parestesias, palidez, paralisis, "
      "poiquilotermia, ausencia de pulso (tardio).", ["compartimental"])

menos(deck_m, "Embarazo ectopico roto (abdomen agudo hemorragico)",
      "Reanimacion (2 vias, cruzar sangre) + <b>cirugia urgente (salpingectomia)</b>. (Manejo detallado en el paquete "
      "de Obstetricia.)",
      "(urgencia) Un embarazo fuera del utero se rompio y hay sangrado interno; operamos de inmediato.",
      "Mujer en edad fertil + dolor + hipotension &rarr; <b>prueba de embarazo SIEMPRE</b> + FAST.", ["ectopico"])


def build():
    for d, f in [(deck_e, "Manejo_01_Ejes.apkg"), (deck_c, "Manejo_02_Core.apkg"), (deck_m, "Manejo_03_Menos.apkg")]:
        genanki.Package(d).write_to_file(os.path.join(OUTPUT_DIR, f))
        print(f"  -> {f} ({len(d.notes)} notas)")
    genanki.Package([deck_e, deck_c, deck_m]).write_to_file(
        os.path.join(OUTPUT_DIR, "No_Hay_Tiempo_Cir_Manejo_TODOS.apkg"))
    print(f"  -> TODOS ({sum(len(d.notes) for d in [deck_e, deck_c, deck_m])} notas)")


if __name__ == "__main__":
    build()
