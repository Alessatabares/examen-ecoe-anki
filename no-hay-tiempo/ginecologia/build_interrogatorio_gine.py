"""Generador de 3 subdecks Anki — Interrogatorio "tronco + llaves" / Ginecología (ECOE).

Idea: el interrogatorio de un grupo NO son 6 interrogatorios sueltos. Es
  TRONCO contextual (lo que preguntas igual en todo el grupo, lo recitas una vez)
  + RAMA / LLAVE especifica (la pregunta que separa una enfermedad de otra).

Subdecks (paralelo al paquete de manejos):
  1 - Troncos (ejes)            ->  8 cartas (el guion de apertura por motivo de consulta)
  2 - Llaves comunes (core)     -> 18 cartas (la pregunta-llave de lo mas preguntado)
  3 - Llaves menos preguntadas  -> 17 cartas (segunda pasada)

Formato carta de TRONCO (campo Back):
  CONTEXTO  -> lo que pregunto SIEMPRE en ese motivo de consulta
  RAMIFICA  -> el sintoma guia y a que enfermedad me lleva

Formato carta de LLAVE (campo Back):
  LLAVE     -> la pregunta/maniobra que dispara el dx
  PATRON    -> la respuesta/hallazgo que lo confirma
  DX        -> diagnostico

Guia: GPC mexicanas + ACOG + Williams.
"""
import os
import genanki

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "output")
os.makedirs(OUTPUT_DIR, exist_ok=True)

MODEL_QA_ID = 1990002002

DECK_ID_TRONCOS = 1990001011
DECK_ID_CORE = 1990001012
DECK_ID_MENOS = 1990001013

DECK_NAME_TRONCOS = "No hay tiempo::Ginecologia::Interrogatorio::1 - Troncos (ejes)"
DECK_NAME_CORE = "No hay tiempo::Ginecologia::Interrogatorio::2 - Llaves comunes (core)"
DECK_NAME_MENOS = "No hay tiempo::Ginecologia::Interrogatorio::3 - Llaves menos preguntadas"

CSS_BASE = """
.card {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  font-size: 19px; text-align: left; color: #1a1a1a;
  background-color: #fafafa; padding: 20px; line-height: 1.55;
}
.caso { font-size: 21px; font-weight: 700; color: #1e3a8a; }
#extra { margin-top: 16px; border: none; border-top: 1px solid #d4d4d4; padding-top: 12px; }

.bloque { display: block; margin: 12px 0; padding: 10px 14px; border-radius: 8px; }
.lab { display: block; font-size: 13px; font-weight: 700; letter-spacing: .5px;
       text-transform: uppercase; margin-bottom: 4px; }

.contexto { background: #eef2ff; border-left: 4px solid #1e3a8a; }
.ramifica { background: #f5f3ff; border-left: 4px solid #6d28d9; }
.llave    { background: #eef2ff; border-left: 4px solid #1e3a8a; }
.patron   { background: #f5f3ff; border-left: 4px solid #6d28d9; }
.dx       { background: #ecfdf5; border-left: 4px solid #047857; }
.contexto .lab { color: #1e3a8a; }
.ramifica .lab { color: #6d28d9; }
.llave .lab    { color: #1e3a8a; }
.patron .lab   { color: #6d28d9; }
.dx .lab       { color: #047857; }
.dx b { color: #065f46; }
b { color: #111; }
"""

model_qa = genanki.Model(
    MODEL_QA_ID,
    "No Hay Tiempo Interrogatorio QA",
    fields=[{"name": "Front"}, {"name": "Back"}],
    templates=[{
        "name": "QA",
        "qfmt": "{{Front}}",
        "afmt": '{{Front}}<hr id="extra">{{Back}}',
    }],
    css=CSS_BASE,
)

deck_troncos = genanki.Deck(DECK_ID_TRONCOS, DECK_NAME_TRONCOS)
deck_core = genanki.Deck(DECK_ID_CORE, DECK_NAME_CORE)
deck_menos = genanki.Deck(DECK_ID_MENOS, DECK_NAME_MENOS)

BASE_TAGS = ["gineco", "ecoe", "no_hay_tiempo", "interrogatorio"]


def add(deck, front, back, tags):
    deck.add_note(genanki.Note(model=model_qa, fields=[front, back], tags=BASE_TAGS + tags))


def caso(txt):
    return f'<span class="caso">{txt}</span>'


def tronco(contexto, ramifica):
    return (
        f'<span class="bloque contexto"><span class="lab">Pregunto siempre (contexto)</span>{contexto}</span>'
        f'<span class="bloque ramifica"><span class="lab">Esto me ramifica (sintoma guia -&gt; dx)</span>{ramifica}</span>'
    )


def llave(pregunta, patron, dx):
    return (
        f'<span class="bloque llave"><span class="lab">Pregunta-llave</span>{pregunta}</span>'
        f'<span class="bloque patron"><span class="lab">Patron que confirma</span>{patron}</span>'
        f'<span class="bloque dx"><span class="lab">Diagnostico</span><b>{dx}</b></span>'
    )


# ============================================================
# SUBDECK 1 - TRONCOS (ejes): 8 cartas
# ============================================================
T = ["tronco"]

add(deck_troncos,
    caso("TRONCO — ITS / lesion o flujo genital (riesgo sexual)"),
    tronco(
        "1) Motivo: &iquest;ulcera, verruga, flujo o dolor? 2) Tiempo y &iquest;1er episodio o recurrente? "
        "3) Conducta sexual: n&ordm; de parejas (6-12 m), parejas nuevas, sexo de parejas, practicas (vaginal/anal/oral). "
        "4) Condon (consistente o no). 5) ITS previas / pareja con sintomas. 6) VIH + vacunas (VPH, HepB). "
        "7) Fiebre, adenopatias, exantema. 8) <b>Siempre: embarazo, FUM, anticoncepcion.</b>",
        "<b>ULCERA</b> &rarr; sifilis / herpes / chancroide (llave: &iquest;duele?).<br>"
        "<b>VERRUGA</b> &rarr; VPH/condiloma.<br>"
        "<b>FLUJO</b> &rarr; candida / vaginosis / tricomonas / cervicitis.<br>"
        "<b>DOLOR PELVICO + fiebre</b> &rarr; EIP.",
    ),
    T + ["its"])

add(deck_troncos,
    caso("TRONCO — Sangrado uterino anormal (SUA)"),
    tronco(
        "Menarca, FUM, <b>&iquest;es posmenopausica?</b> Ciclo (regular/irregular), cantidad "
        "(coagulos, n&ordm; toallas, anemia), patron (intermenstrual, <b>poscoital</b>, posmenopausico). "
        "Dolor/dismenorrea, dispareunia. Sintomas androgenicos. Anticonceptivos/DIU/tamoxifeno. "
        "Paridad, citologia al dia, ultimo embarazo.",
        "<b>Posmenopausico</b> &rarr; descartar <b>ca endometrio</b> (bandera roja).<br>"
        "<b>Abundante + utero aumentado</b> &rarr; miomatosis / adenomiosis.<br>"
        "<b>Irregular + hiperandrogenismo</b> &rarr; SOP.<br>"
        "<b>Poscoital</b> &rarr; cervicitis / ca cervix.",
    ),
    T + ["sua"])

add(deck_troncos,
    caso("TRONCO — Dolor pelvico"),
    tronco(
        "Agudo vs cronico (&gt;6 m). Localizacion, irradiacion, intensidad. <b>Relacion con el ciclo</b> "
        "(ciclico?), <b>dispareunia</b> (superficial/profunda). Fiebre, flujo, sangrado, sintomas urinarios/digestivos. "
        "<b>Posibilidad de embarazo</b> (FUM, prueba). Antecedente de ITS/EIP, cirugias.",
        "<b>Agudo + fiebre + flujo + dolor a movilizacion cervical</b> &rarr; EIP.<br>"
        "<b>Agudo + amenorrea + sangrado</b> &rarr; descartar ectopico.<br>"
        "<b>Ciclico + dispareunia profunda + infertilidad</b> &rarr; endometriosis.<br>"
        "<b>Cronico + reglas abundantes + utero globular</b> &rarr; adenomiosis.",
    ),
    T + ["dolor_pelvico"])

add(deck_troncos,
    caso("TRONCO — Masa o sintoma mamario"),
    tronco(
        "Tiempo y crecimiento, <b>cambio con el ciclo</b>, dolor. Cambios de piel (<b>naranja</b>, retraccion, "
        "ulceracion), del pezon (retraccion, eccema), <b>telorrea</b> (uni/bilateral, espontanea, color). "
        "Lactancia actual. Factores de riesgo: edad, <b>antecedente familiar/personal</b>, menarca/menopausia, "
        "nuliparidad, hormonales.",
        "<b>Movil, joven, &lt;3 cm</b> &rarr; fibroadenoma.<br>"
        "<b>Fluctua con el ciclo</b> &rarr; quiste.<br>"
        "<b>Dura, fija, piel de naranja, retraccion</b> &rarr; ca.<br>"
        "<b>Dolor + eritema + fiebre + lactancia</b> &rarr; mastitis/absceso.<br>"
        "<b>Eccema del pezon</b> &rarr; Paget.",
    ),
    T + ["mama"])

add(deck_troncos,
    caso("TRONCO — Masa anexial / pelvica"),
    tronco(
        "Edad y <b>estado menopausico</b>. Dolor, <b>distension, saciedad temprana, cambio de habito intestinal</b>. "
        "Sangrado, sintomas hormonales. Antecedente familiar de ca mama/ovario (BRCA). Hallazgo en USG "
        "(simple vs solida/septada, tama&ntilde;o), CA-125.",
        "<b>Joven + quiste simple + asintomatico</b> &rarr; quiste funcional.<br>"
        "<b>Posmenopausica + masa solida/septada + ascitis + CA-125 alto</b> &rarr; ca ovario.<br>"
        "<b>Dolor agudo + masa + nausea</b> &rarr; descartar torsion.",
    ),
    T + ["masa_anexial"])

add(deck_troncos,
    caso("TRONCO — Sintomas vulvares"),
    tronco(
        "Prurito, ardor, dispareunia, dolor. <b>Lesion</b> (placa, verruga, ulcera, tumefaccion) y tiempo. "
        "Cambios de color de la piel, sangrado/herida que no cura. Higiene/irritantes, menopausia, "
        "antecedente de ITS, inmunosupresion.",
        "<b>Placas blancas atroficas + prurito cronico</b> &rarr; liquen escleroso.<br>"
        "<b>Verrugas coliflor indoloras</b> &rarr; condiloma/VPH.<br>"
        "<b>Tumefaccion dolorosa en labio (4-5 / 7-8 h)</b> &rarr; Bartholino.<br>"
        "<b>Lesion/herida que no cura</b> &rarr; biopsia (VIN/ca vulvar).",
    ),
    T + ["vulvar"])

add(deck_troncos,
    caso("TRONCO — Eje menstrual-endocrino (amenorrea / SOP / climaterio)"),
    tronco(
        "Menarca, patron de ciclos (oligo/amenorrea), FUM. <b>Bochornos, insomnio, sequedad</b> (climaterio). "
        "<b>Hirsutismo, acne, alopecia</b> (androgenico). Galactorrea, cefalea/campos visuales. Peso/IMC, "
        "resistencia a insulina. <b>Siempre descartar embarazo primero.</b>",
        "<b>Bochornos + FUM &gt;12 m + &gt;45 a</b> &rarr; climaterio.<br>"
        "<b>Oligomenorrea + hiperandrogenismo + sobrepeso</b> &rarr; SOP.<br>"
        "<b>Amenorrea</b> &rarr; 1&ordm; prueba de embarazo, luego eje (prolactina, TSH, FSH).",
    ),
    T + ["menstrual_endocrino"])

add(deck_troncos,
    caso("TRONCO — Piso pelvico / prolapso e incontinencia"),
    tronco(
        "<b>Sensacion de bulto o cuerpo extrano</b>, peso vaginal, que empeora al final del dia/esfuerzo. "
        "<b>Incontinencia</b> (de esfuerzo vs urgencia), dificultad para evacuar/orinar, dispareunia. "
        "<b>Paridad y tipo de partos</b> (macrosomia, instrumentado), menopausia, estrenimiento cronico, "
        "tos/EPOC, peso, cirugia pelvica previa.",
        "<b>Bulto + esfuerzo + multipara</b> &rarr; prolapso (por compartimento).<br>"
        "<b>Escape con tos/esfuerzo</b> &rarr; IU de esfuerzo.<br>"
        "<b>Urgencia/frecuencia</b> &rarr; vejiga hiperactiva.",
    ),
    T + ["prolapso"])


# ============================================================
# SUBDECK 2 - LLAVES COMUNES (core): 18 cartas
# ============================================================
C = ["core"]

add(deck_core, caso("Ulcera genital UNICA e INDURADA"),
    llave("&iquest;<b>Duele</b>? (no) &iquest;una o varias? &iquest;adenopatia dolorosa?",
          "Ulcera <b>indolora</b>, unica, base limpia indurada (chancro); adenopatia <b>no dolorosa</b>.",
          "Sifilis primaria"),
    C + ["its", "sifilis"])

add(deck_core, caso("Vesiculas genitales agrupadas y DOLOROSAS"),
    llave("&iquest;<b>Ardor/hormigueo antes</b> de las lesiones? &iquest;1er episodio o recurrente?",
          "Vesiculas dolorosas sobre base eritematosa, recurrentes, prodromo; adenopatia <b>dolorosa</b>.",
          "Herpes genital"),
    C + ["its", "herpes"])

add(deck_core, caso("Ulcera genital DOLOROSA y sucia"),
    llave("&iquest;Duele mucho? &iquest;<b>pus/ganglio que se abre</b> en la ingle?",
          "Ulcera dolorosa, fondo gris, bordes irregulares; <b>bubon inguinal que supura</b>.",
          "Chancroide"),
    C + ["its", "chancroide"])

add(deck_core, caso("Flujo vaginal blanco GRUMOSO"),
    llave("&iquest;<b>Prurito intenso</b>? &iquest;aspecto en requeson? &iquest;ardor al orinar?",
          "Flujo blanco grumoso adherente, eritema vulvar, <b>prurito</b>; pH <b>&lt;4.5</b>.",
          "Candidiasis vulvovaginal"),
    C + ["candidiasis"])

add(deck_core, caso("Flujo vaginal gris con MAL OLOR"),
    llave("&iquest;<b>Olor a pescado</b>, peor tras el coito? &iquest;poco prurito?",
          "Flujo gris homogeneo, <b>olor a aminas</b>; pH <b>&gt;4.5</b>, KOH+ (whiff), clue cells.",
          "Vaginosis bacteriana"),
    C + ["vaginosis"])

add(deck_core, caso("Flujo vaginal verdoso ESPUMOSO"),
    llave("&iquest;Flujo <b>amarillo-verde espumoso</b>? &iquest;prurito + disuria? &iquest;pareja con sintomas?",
          "Flujo espumoso maloliente, <b>cervix en fresa</b>, pH &gt;4.5; es ITS.",
          "Tricomoniasis"),
    C + ["tricomoniasis"])

add(deck_core, caso("Flujo cervical mucopurulento + sangrado POSCOITAL"),
    llave("&iquest;<b>Sangra tras relaciones</b>? &iquest;disuria? &iquest;sangrado intermenstrual?",
          "Cervix friable con secrecion mucopurulenta, sangrado al contacto; riesgo de ITS.",
          "Cervicitis (gonococo/clamidia)"),
    C + ["cervicitis"])

add(deck_core, caso("Dolor pelvico bajo + fiebre + flujo"),
    llave("&iquest;<b>Dolor con las relaciones / al mover el cuello</b>? &iquest;fiebre? &iquest;ITS reciente?",
          "Dolor a la <b>movilizacion cervical</b>, dolor anexial, fiebre, flujo; CMT positivo.",
          "Enfermedad inflamatoria pelvica (EIP)"),
    C + ["eip"])

add(deck_core, caso("Sangrado vaginal en mujer POSMENOPAUSICA"),
    llave("&iquest;Hace cuanto fue su <b>ultima regla</b>? (bandera roja: cualquier sangrado posmenopausico)",
          "Todo sangrado posmenopausico es <b>ca endometrio hasta demostrar lo contrario</b> &rarr; USTV + biopsia.",
          "Sospecha de cancer de endometrio"),
    C + ["cancer_endometrio"])

add(deck_core, caso("Sangrado abundante + utero grande e irregular"),
    llave("&iquest;Reglas muy <b>abundantes con coagulos</b>? &iquest;sensacion de masa/peso? &iquest;sintomas urinarios?",
          "Utero aumentado, <b>contorno irregular/nodular</b>, anemia por sangrado.",
          "Miomatosis uterina"),
    C + ["miomatosis"])

add(deck_core, caso("Dismenorrea progresiva + dispareunia profunda"),
    llave("&iquest;Dolor que <b>empeora con cada regla</b>? &iquest;dolor profundo al coito? &iquest;cuesta embarazo?",
          "Dismenorrea progresiva, dispareunia profunda, <b>infertilidad</b>; nodulos en fondo de saco.",
          "Endometriosis"),
    C + ["endometriosis"])

add(deck_core, caso("Reglas irregulares + acne / vello"),
    llave("&iquest;Ciclos <b>espaciados/ausentes</b>? &iquest;<b>vello, acne</b>, aumento de peso?",
          "Oligomenorrea + hiperandrogenismo clinico/bioquimico + ovarios poliquisticos (criterios de Rotterdam).",
          "Sindrome de ovario poliquistico (SOP)"),
    C + ["sop"])

add(deck_core, caso("Bochornos + insomnio en mujer &gt;45 a"),
    llave("&iquest;<b>Bochornos, sudores, sequedad vaginal</b>? &iquest;cuanto sin reglas? (&gt;12 meses)",
          "Sintomas vasomotores + <b>FUM &gt;12 meses</b>; dx clinico, no requiere hormonas de rutina.",
          "Climaterio / menopausia"),
    C + ["climaterio"])

add(deck_core, caso("Nodulo mamario MOVIL en mujer joven"),
    llave("&iquest;<b>Se mueve</b> bajo el dedo? &iquest;cambia con el ciclo? &iquest;duele?",
          "Nodulo firme, <b>movil</b> (&laquo;raton mamario&raquo;), liso, &lt;3 cm, mujer &lt;30 a.",
          "Fibroadenoma"),
    C + ["mama", "fibroadenoma"])

add(deck_core, caso("Nodulo mamario DURO y FIJO"),
    llave("&iquest;Esta <b>fijo/adherido</b>? &iquest;<b>piel de naranja</b>, retraccion del pezon, ganglio axilar?",
          "Nodulo duro, irregular, <b>fijo</b>, piel de naranja/retraccion, adenopatia axilar.",
          "Sospecha de cancer de mama"),
    C + ["mama", "cancer"])

add(deck_core, caso("Mama dolorosa, roja y caliente en LACTANCIA"),
    llave("&iquest;Esta <b>amamantando</b>? &iquest;fiebre? &iquest;<b>zona fluctuante</b> (absceso)?",
          "Eritema, dolor, calor, fiebre en puerpera; si fluctua &rarr; absceso.",
          "Mastitis / absceso puerperal"),
    C + ["mama", "mastitis"])

add(deck_core, caso("Sangrado POSCOITAL + citologia alterada"),
    llave("&iquest;<b>Sangra tras relaciones</b>? &iquest;tiene su <b>Papanicolaou</b> al dia? &iquest;factores VPH?",
          "Sangrado poscoital, lesion/cervix friable, citologia anormal &rarr; colposcopia.",
          "NIC / cancer cervicouterino"),
    C + ["nic", "cancer_cervix"])

add(deck_core, caso("Tumefaccion dolorosa en labio mayor"),
    llave("&iquest;<b>Bolita dolorosa</b> en la entrada vaginal (posicion 4-5 o 7-8 h)? &iquest;dificulta sentarse?",
          "Masa fluctuante dolorosa en glandula de Bartholino; si hay fiebre/celulitis valorar ITS.",
          "Absceso de Bartholino"),
    C + ["bartholino"])


# ============================================================
# SUBDECK 3 - LLAVES MENOS PREGUNTADAS: 17 cartas
# ============================================================
M = ["menos_preguntado"]

add(deck_menos, caso("Prurito vulvar cronico + placas blancas"),
    llave("&iquest;<b>Picor cronico</b>? &iquest;piel <b>blanca y fina (papel de cigarrillo)</b>? &iquest;dispareunia?",
          "Placas blancas atroficas, perdida de arquitectura vulvar; riesgo de ca vulvar (biopsiar dudas).",
          "Liquen escleroso"),
    M + ["liquen"])

add(deck_menos, caso("Verrugas genitales en coliflor"),
    llave("&iquest;Lesiones <b>blandas, indoloras, que crecen</b>? &iquest;pareja con verrugas? &iquest;vacuna VPH?",
          "Condilomas exofiticos, acetoblancos; pueden ser multiples y recidivar.",
          "VPH / condiloma acuminado"),
    M + ["vph"])

add(deck_menos, caso("Reglas muy abundantes + utero globular blando"),
    llave("&iquest;Reglas <b>abundantes y muy dolorosas</b>? &iquest;sensacion de utero agrandado <b>simetrico</b>?",
          "Utero globular, blando, aumentado de forma <b>difusa</b>; dismenorrea + sangrado abundante.",
          "Adenomiosis"),
    M + ["adenomiosis"])

add(deck_menos, caso("Distension + saciedad temprana en posmenopausica"),
    llave("&iquest;<b>Hinchazon, saciedad precoz, cambio intestinal</b>? &iquest;antecedente familiar mama/ovario?",
          "Masa anexial solida/septada + ascitis + CA-125 elevado; sintomas vagos y tardios.",
          "Cancer de ovario"),
    M + ["cancer_ovario"])

add(deck_menos, caso("Nodulo mamario que aparece/duele con la regla"),
    llave("&iquest;<b>Cambia de tama&ntilde;o y duele con el ciclo</b>? &iquest;liso y movil?",
          "Quiste anecoico de pared fina en USG, fluctua con el ciclo; benigno.",
          "Quiste mamario simple"),
    M + ["mama", "quiste"])

add(deck_menos, caso("Eccema/erosion del pezon que no cura"),
    llave("&iquest;Lesion del pezon <b>unilateral que no responde a cremas</b>? &iquest;prurito/costra?",
          "Eccema cronico, erosivo, unilateral del pezon; casi siempre <b>ca subyacente</b> &rarr; biopsia.",
          "Enfermedad de Paget del pezon"),
    M + ["mama", "paget"])

add(deck_menos, caso("Secrecion por el pezon"),
    llave("&iquest;Sale de <b>un solo pecho, un solo poro, sola y con sangre</b>? (vs bilateral, multiporo, provocada)",
          "Telorrea <b>unilateral, uniporo, espontanea, serosanguinolenta</b> = patologica (papiloma/ca).",
          "Telorrea patologica"),
    M + ["mama", "telorrea"])

add(deck_menos, caso("Sensacion de bulto vaginal que empeora al esforzarse"),
    llave("&iquest;<b>Bulto o peso vaginal</b> al final del dia/esfuerzo? &iquest;escapes de orina? &iquest;partos vaginales?",
          "Protrusion de pared/cuello por compartimento, multipara; mejora acostada.",
          "Prolapso de organos pelvicos"),
    M + ["prolapso"])

add(deck_menos, caso("Pareja sin embarazo tras 12 meses"),
    llave("&iquest;<b>12 meses sin lograrlo</b> (6 si &ge;35 a)? &iquest;ovula (ciclos)? &iquest;ITS previa? &iquest;<b>semen de la pareja</b>?",
          "Estudio de <b>la pareja</b>: seminograma, ovulacion, permeabilidad tubarica; no tratar a ciegas.",
          "Infertilidad (estudio inicial)"),
    M + ["infertilidad"])

add(deck_menos, caso("Lesion vulvar persistente o que cambia"),
    llave("&iquest;<b>Lesion/mancha/herida que no cura</b> en semanas? &iquest;prurito, cambio de color?",
          "Toda lesion vulvar persistente o atipica se <b>biopsia</b> (VIN, liquen plano, ca vulvar).",
          "Patologia vulvoperineal (biopsiar)"),
    M + ["vulvoperineal"])

add(deck_menos, caso("&iquest;Cuando inicio y cada cuanto el tamizaje cervical?"),
    llave("&iquest;Edad? &iquest;ultima citologia y resultado? &iquest;vacuna VPH? &iquest;inmunosupresion?",
          "Citologia desde <b>21 a c/3 anos</b>; <b>25-30 a 65 a co-test c/5 anos</b>; suspender a los 65 si previo negativo.",
          "Tamizaje cervicouterino"),
    M + ["tamizaje"])

add(deck_menos, caso("Papanicolaou con resultado anormal"),
    llave("&iquest;Que grado reporta? &iquest;prueba de VPH? &iquest;visible la lesion?",
          "<b>ASC-US</b> &rarr; VPH reflejo; <b>LSIL/ASC-H/HSIL</b> &rarr; colposcopia + biopsia; AGC &rarr; estudio endometrial.",
          "Conducta ante citologia anormal"),
    M + ["papanicolau"])

add(deck_menos, caso("Serologia reactiva sin lesion genital"),
    llave("&iquest;Tuvo <b>chancro o exantema</b> en el pasado? &iquest;tiempo desde posible contagio? &iquest;tratamientos previos?",
          "Sifilis <b>asintomatica</b> detectada por serologia; clasificar temprana vs tardia define dosis.",
          "Sifilis latente"),
    M + ["sifilis"])

add(deck_menos, caso("Quiste anexial en mujer joven asintomatica"),
    llave("&iquest;<b>Asintomatica</b>? &iquest;quiste <b>simple &lt;5 cm</b> en USG? &iquest;relacion con el ciclo?",
          "Quiste anecoico unilocular de pared fina, premenopausica; casi siempre <b>funcional</b> (control USG).",
          "Quiste ovarico funcional"),
    M + ["masa_anexial"])

add(deck_menos, caso("Antes de dar terapia hormonal en climaterio: que pregunto"),
    llave("&iquest;Antecedente de <b>Ca de mama, trombosis (TVP/TEP), EVC/IAM, sangrado sin dx, hepatopatia</b>? &iquest;edad/tiempo de menopausia?",
          "Esas son las <b>contraindicaciones</b>; ademas ventana: &lt;60 a o &lt;10 a de menopausia.",
          "Banderas para contraindicar THR"),
    M + ["climaterio"])

add(deck_menos, caso("Sangrado menstrual abundante DESDE LA MENARCA"),
    llave("&iquest;<b>Abundante desde la primera regla</b>? &iquest;moretones, epistaxis, sangrado en cirugias/dental? &iquest;familiar?",
          "SUA desde menarca + sangrado en otros sitios &rarr; sospechar <b>coagulopatia</b> (von Willebrand).",
          "SUA por trastorno de la coagulacion"),
    M + ["sua", "adolescente"])

add(deck_menos, caso("Amenorrea (no menstrua)"),
    llave("&iquest;Posibilidad de <b>embarazo</b>? (1&ordm; siempre) Luego: &iquest;galactorrea, bochornos, estres/peso, sintomas androgenicos?",
          "Descartar embarazo <b>primero</b>; luego eje: prolactina, TSH, FSH/estradiol segun clinica.",
          "Amenorrea (algoritmo de descarte)"),
    M + ["amenorrea"])


# ============================================================
# Build / empaquetado
# ============================================================
def build():
    decks = [
        (deck_troncos, "Interrogatorio_01_Troncos.apkg"),
        (deck_core, "Interrogatorio_02_Llaves_core.apkg"),
        (deck_menos, "Interrogatorio_03_Llaves_menos.apkg"),
    ]
    for d, fname in decks:
        genanki.Package(d).write_to_file(os.path.join(OUTPUT_DIR, fname))
        print(f"  -> {fname} ({len(d.notes)} notas)")

    combined_out = os.path.join(OUTPUT_DIR, "No_Hay_Tiempo_Gineco_Interrogatorio_TODOS.apkg")
    genanki.Package([deck_troncos, deck_core, deck_menos]).write_to_file(combined_out)
    total = sum(len(d.notes) for d in [deck_troncos, deck_core, deck_menos])
    print(f"  -> No_Hay_Tiempo_Gineco_Interrogatorio_TODOS.apkg ({total} notas totales)")


if __name__ == "__main__":
    build()
