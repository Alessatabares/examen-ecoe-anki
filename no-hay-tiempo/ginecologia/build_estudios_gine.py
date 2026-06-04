"""Generador de 3 subdecks Anki — Exploracion + Estudios / Ginecologia (ECOE).

DOS formas distintas de estudio (la clave del pilar 3):
  A) DISCRIMINADOR  -> una herramienta separa un grupo por un hallazgo.
     Organizas por herramienta. Front = herramienta, Back = tabla hallazgo -> dx.
  B) PANEL / workup -> una enfermedad pide una bateria; cada estudio tiene un ROL
     (confirma / descarta imitador / evalua repercusion). Organizas por enfermedad.

Subdecks:
  1 - Discriminadores (por herramienta)  ->  8 cartas
  2 - Paneles de estudio (por enfermedad)->  8 cartas
  3 - Menos preguntados                  -> 17 cartas

Guia: GPC mexicanas + ACOG + Williams.
"""
import os
import genanki

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "output")
os.makedirs(OUTPUT_DIR, exist_ok=True)

MODEL_QA_ID = 1990002003

DECK_ID_DISC = 1990001021
DECK_ID_PANEL = 1990001022
DECK_ID_MENOS = 1990001023

DECK_NAME_DISC = "No hay tiempo::Ginecologia::Estudios::1 - Discriminadores (herramienta)"
DECK_NAME_PANEL = "No hay tiempo::Ginecologia::Estudios::2 - Paneles (por enfermedad)"
DECK_NAME_MENOS = "No hay tiempo::Ginecologia::Estudios::3 - Menos preguntados"

CSS_BASE = """
.card {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  font-size: 19px; text-align: left; color: #1a1a1a;
  background-color: #fafafa; padding: 20px; line-height: 1.5;
}
.caso { font-size: 21px; font-weight: 700; color: #1e3a8a; }
#extra { margin-top: 16px; border: none; border-top: 1px solid #d4d4d4; padding-top: 12px; }

.bloque { display: block; margin: 12px 0; padding: 10px 14px; border-radius: 8px; }
.lab { display: block; font-size: 13px; font-weight: 700; letter-spacing: .5px;
       text-transform: uppercase; margin-bottom: 4px; }

.paraque { background: #eef2ff; border-left: 4px solid #1e3a8a; }
.trampa  { background: #fef2f2; border-left: 4px solid #b91c1c; }
.pido    { background: #eef2ff; border-left: 4px solid #1e3a8a; }
.descarto{ background: #fff7ed; border-left: 4px solid #b45309; }
.clave   { background: #ecfdf5; border-left: 4px solid #047857; }
.paraque .lab { color: #1e3a8a; }
.trampa .lab  { color: #b91c1c; }
.pido .lab    { color: #1e3a8a; }
.descarto .lab{ color: #b45309; }
.clave .lab   { color: #047857; }

table.disc { border-collapse: collapse; width: 100%; margin: 6px 0 4px 0; font-size: 17px; }
table.disc td { border-bottom: 1px solid #e5e7eb; padding: 7px 8px; vertical-align: top; }
table.disc td.dx { font-weight: 700; color: #065f46; white-space: nowrap; }
b { color: #111; }
"""

model_qa = genanki.Model(
    MODEL_QA_ID,
    "No Hay Tiempo Estudios QA",
    fields=[{"name": "Front"}, {"name": "Back"}],
    templates=[{
        "name": "QA",
        "qfmt": "{{Front}}",
        "afmt": '{{Front}}<hr id="extra">{{Back}}',
    }],
    css=CSS_BASE,
)

deck_disc = genanki.Deck(DECK_ID_DISC, DECK_NAME_DISC)
deck_panel = genanki.Deck(DECK_ID_PANEL, DECK_NAME_PANEL)
deck_menos = genanki.Deck(DECK_ID_MENOS, DECK_NAME_MENOS)

BASE_TAGS = ["gineco", "ecoe", "no_hay_tiempo", "estudios"]


def add(deck, front, back, tags):
    deck.add_note(genanki.Note(model=model_qa, fields=[front, back], tags=BASE_TAGS + tags))


def caso(txt):
    return f'<span class="caso">{txt}</span>'


def disc(paraque, filas, trampa):
    """filas: lista de (hallazgo, dx)."""
    rows = "".join(f'<tr><td>{h}</td><td class="dx">{d}</td></tr>' for h, d in filas)
    return (
        f'<span class="bloque paraque"><span class="lab">Para que lo pido</span>{paraque}</span>'
        f'<table class="disc">{rows}</table>'
        f'<span class="bloque trampa"><span class="lab">Trampa</span>{trampa}</span>'
    )


def panel(pido, descarto, clave):
    return (
        f'<span class="bloque pido"><span class="lab">Pido (bateria + para que)</span>{pido}</span>'
        f'<span class="bloque descarto"><span class="lab">Descarto imitadores</span>{descarto}</span>'
        f'<span class="bloque clave"><span class="lab">Clave / criterio</span>{clave}</span>'
    )


# ============================================================
# SUBDECK 1 - DISCRIMINADORES (por herramienta): 8 cartas
# ============================================================
D = ["discriminador"]

add(deck_disc, caso("USG transvaginal — utero y anexos"),
    disc("Discriminar masa/sangrado uterino y masa anexial; medir endometrio.",
         [("Masa miometrial <b>hipoecoica, bien delimitada</b>, sombra acustica", "Mioma"),
          ("Utero <b>globular, miometrio heterogeneo, quistes</b>, zona union &gt;12 mm", "Adenomiosis"),
          ("Quiste con ecos en <b>vidrio esmerilado</b>, pared lisa", "Endometrioma"),
          ("Foco <b>hiperecoico en cavidad</b> con pediculo vascular unico", "Polipo"),
          ("Endometrio <b>&gt;4-5 mm posmenopausico con sangrado</b>, irregular", "Ca endometrio"),
          ("Quiste <b>anecoico unilocular, pared fina &lt;5 cm</b>", "Quiste funcional"),
          ("Masa <b>solida/septada, papilas, ascitis</b>", "Ca ovario")],
         "Mioma vs adenomiosis = <b>bien delimitado</b> vs <b>difuso y globular</b>."),
    D + ["usg_tv"])

add(deck_disc, caso("Tacto bimanual — utero y anexos"),
    disc("Definir tama&ntilde;o/forma/movilidad uterina y masas/dolor anexial.",
         [("Utero aumentado, <b>irregular/nodular, firme, NO doloroso</b>", "Miomatosis"),
          ("Utero aumentado, <b>globular/simetrico, blando, DOLOROSO</b>", "Adenomiosis"),
          ("<b>Nodulos dolorosos en uterosacros</b>, utero fijo retrovertido", "Endometriosis"),
          ("<b>Dolor a la movilizacion cervical</b> + dolor anexial + masa", "EIP / absceso TO"),
          ("Masa anexial <b>separada del utero</b>", "Tumor/quiste ovarico")],
         "Forma (irregular=mioma / simetrico=adenomiosis) + dolor (mioma no, adenomiosis si)."),
    D + ["bimanual"])

add(deck_disc, caso("Especuloscopia — flujo y cervix"),
    disc("Ver caracteristicas del flujo y del cervix (friabilidad, lesion).",
         [("Flujo <b>blanco grumoso</b> adherente, sin olor", "Candidiasis"),
          ("Flujo <b>gris homogeneo</b>, olor a aminas", "Vaginosis"),
          ("Flujo <b>verde espumoso</b> + <b>cervix en fresa</b>", "Tricomoniasis"),
          ("Secrecion <b>mucopurulenta</b> + cervix <b>friable que sangra</b>", "Cervicitis (GC/clamidia)"),
          ("Lesion <b>exofitica/ulcerada que sangra al contacto</b>", "Ca cervix")],
         "Se confirma en laboratorio con pH + fresco + KOH."),
    D + ["especulo"])

add(deck_disc, caso("pH vaginal + fresco + KOH (whiff)"),
    disc("Confirmar el agente del flujo en consulta.",
         [("pH <b>&lt;4.5</b> + <b>hifas/pseudohifas</b> en KOH", "Candidiasis"),
          ("pH <b>&gt;4.5</b> + <b>whiff+</b> (olor pescado) + <b>clue cells</b>", "Vaginosis (Amsel)"),
          ("pH <b>&gt;4.5</b> + <b>protozoo flagelado movil</b> + leucocitos", "Tricomoniasis")],
         "Candida es el unico con pH normal (&lt;4.5). VB y trico suben el pH."),
    D + ["ph_fresco"])

add(deck_disc, caso("Inspeccion vulvar / perineal"),
    disc("Caracterizar lesion vulvar y ulceras del grupo ITS.",
         [("Ulcera <b>unica, indurada, INDOLORA</b> + adenopatia indolora", "Sifilis (chancro)"),
          ("<b>Vesiculas dolorosas</b> agrupadas + adenopatia dolorosa", "Herpes"),
          ("Ulcera <b>dolorosa, sucia</b> + <b>bubon que supura</b>", "Chancroide"),
          ("Verrugas <b>en coliflor, indoloras</b>", "VPH/condiloma"),
          ("<b>Placas blancas atroficas</b>, prurito cronico", "Liquen escleroso"),
          ("<b>Tumefaccion dolorosa</b> en labio (4-5/7-8 h)", "Bartholino")],
         "Llave de ulcera: <b>&iquest;duele?</b> (no=sifilis, si=herpes/chancroide)."),
    D + ["vulvar"])

add(deck_disc, caso("Exploracion mamaria"),
    disc("Caracterizar nodulo, piel, pezon y axila.",
         [("Nodulo firme, <b>movil</b>, liso, &lt;3 cm, joven", "Fibroadenoma"),
          ("Nodulo que <b>fluctua con el ciclo</b>, liso", "Quiste"),
          ("Nodulo <b>duro, fijo</b>, piel de naranja, retraccion, ganglio", "Ca mama"),
          ("Eritema, calor, dolor + fiebre en <b>lactancia</b>", "Mastitis"),
          ("Zona <b>fluctuante</b> en mastitis", "Absceso"),
          ("<b>Eccema unilateral del pezon</b> que no cura", "Paget")],
         "Movil=benigno; fijo + piel naranja=maligno. Confirmas con USG/mamografia + core."),
    D + ["mama"])

add(deck_disc, caso("Citologia (Papanicolaou) + colposcopia"),
    disc("Tamizar y graduar lesion cervical; dirigir biopsia.",
         [("Citologia <b>ASC-US</b>", "VPH reflejo (si+ colposcopia)"),
          ("Citologia <b>LSIL / ASC-H / HSIL</b>", "Colposcopia + biopsia"),
          ("Colposcopia: <b>acetoblanco, yodo negativo, mosaico/puntilleo</b>", "Lesion -> biopsia dirigida"),
          ("Biopsia <b>NIC 1</b> vs <b>NIC 2-3</b>", "Vigilar vs cono LEEP")],
         "La citologia tamiza, la <b>colposcopia con biopsia confirma</b>; no tratas con citologia sola."),
    D + ["citologia"])

add(deck_disc, caso("USG mama + mamografia (BI-RADS)"),
    disc("Caracterizar hallazgo mamario y decidir biopsia.",
         [("USG: <b>anecoico, pared fina</b>", "Quiste simple (benigno)"),
          ("USG: <b>solido, irregular, mas alto que ancho</b>", "Sospechoso -> biopsia"),
          ("Mamografia: <b>microcalcificaciones agrupadas pleomorfas</b>", "Sospecha de malignidad"),
          ("Mamografia: <b>densidad espiculada</b> con retraccion", "Ca probable")],
         "BI-RADS 4-5 -> <b>biopsia core</b>, nunca FNAC como unico estudio."),
    D + ["birads"])


# ============================================================
# SUBDECK 2 - PANELES (por enfermedad): 8 cartas
# ============================================================
P = ["panel"]

add(deck_panel, caso("Estudio del SOP"),
    panel(
        "<b>Hiperandrogenismo:</b> testosterona total/libre, androstenediona, SHBG. "
        "<b>Metabolico:</b> glucosa/curva, HbA1c, perfil lipidico. "
        "<b>USG-TV:</b> &ge;20 foliculos o volumen &gt;10 mL.",
        "<b>17-OH-progesterona</b> (hiperplasia suprarrenal no clasica), <b>prolactina</b> (prolactinoma), "
        "<b>TSH</b> (tiroides), cortisol si Cushing; testosterona &gt;150 o DHEA-S muy alto &rarr; <b>tumor</b>.",
        "Dx por <b>Rotterdam 2 de 3</b> (oligoanovulacion / hiperandrogenismo / USG) <b>tras excluir</b> imitadores.",
    ),
    P + ["sop"])

add(deck_panel, caso("Estudio de infertilidad (de la pareja)"),
    panel(
        "<b>Masculino:</b> seminograma (1&ordm;, mas simple). <b>Ovulatorio:</b> progesterona dia 21. "
        "<b>Reserva ovarica:</b> AMH, FSH/estradiol dia 3, foliculos antrales. "
        "<b>Tubario/uterino:</b> histerosalpingografia (HSG).",
        "TSH y prolactina si anovula; serologias ITS; glucemia.",
        "Estudiar tras <b>12 meses</b> sin lograrlo (<b>6 meses si &ge;35 a</b>). Se estudia a <b>ambos</b>.",
    ),
    P + ["infertilidad"])

add(deck_panel, caso("Estudio del climaterio / menopausia"),
    panel(
        "Dx <b>CLINICO</b> (bochornos + FUM &gt;12 m): no requiere hormonas de rutina. "
        "<b>FSH &gt;25-40</b> solo en duda o <b>menopausia precoz &lt;40 a</b> (repetir + descartar falla ovarica). DXA para osteoporosis.",
        "En menopausia precoz: cariotipo, descartar falla ovarica prematura; TSH/prolactina si amenorrea atipica.",
        "<b>Antes de THR:</b> mamografia, citologia al dia, TA, glucosa/lipidos y descartar contraindicaciones.",
    ),
    P + ["climaterio"])

add(deck_panel, caso("Estudio de la amenorrea (algoritmo)"),
    panel(
        "<b>1&ordm; SIEMPRE beta-hCG.</b> Luego TSH, prolactina. <b>FSH/LH/estradiol</b>: "
        "FSH <b>alta</b> = falla ovarica (hipergonadotropo); FSH <b>baja/normal</b> = central (hipogonadotropo).",
        "Embarazo (lo primero), tiroides, hiperprolactinemia (RM hipofisis si alta), causa androgenica.",
        "Test de <b>progesterona</b>: sangrado por deprivacion = hay estrogeno y via permeable.",
    ),
    P + ["amenorrea"])

add(deck_panel, caso("Estudio del sangrado uterino anormal / sospecha de Ca endometrio"),
    panel(
        "<b>USG-TV</b> (grosor endometrial), <b>biopsia endometrial</b> (Pipelle) si engrosado/factores, "
        "histeroscopia con biopsia si persiste. BH (anemia), beta-hCG en edad fertil.",
        "Coagulopatia (si desde menarca), tiroides, polipo, mioma submucoso.",
        "<b>Todo sangrado posmenopausico</b> obliga a biopsia (endometrio &gt;4 mm) = ca endometrio hasta demostrar lo contrario.",
    ),
    P + ["sua", "cancer_endometrio"])

add(deck_panel, caso("Estudio de ITS (bateria)"),
    panel(
        "<b>NAAT</b> de gonococo y clamidia (1ra eleccion). <b>VDRL/RPR</b> (sifilis). "
        "<b>VIH</b>, hepatitis B y C. Fresco/cultivo de flujo segun clinica.",
        "Siempre ofrecer tamizaje del <b>resto de ITS</b> ante una confirmada (co-infeccion frecuente).",
        "Tratar pareja y abstinencia en ITS reales (no en VB/candida). Notificacion segun norma.",
    ),
    P + ["its"])

add(deck_panel, caso("Sifilis: interpretacion serologica (VDRL vs FTA)"),
    panel(
        "<b>No treponemicas (VDRL/RPR):</b> tamizaje y <b>seguimiento</b> (titulan, bajan con tratamiento). "
        "<b>Treponemicas (FTA-ABS/TPHA/TPPA):</b> <b>confirmacion</b>; quedan positivas de por vida.",
        "Falsos positivos de VDRL: embarazo, LES/SAF, infecciones virales (por eso se confirma con treponemica).",
        "Para ver respuesta al tratamiento se usa la <b>NO treponemica</b> (descenso de 4x en titulos).",
    ),
    P + ["sifilis"])

add(deck_panel, caso("Estudio de masa anexial / sospecha Ca ovario"),
    panel(
        "<b>USG-TV</b> (reglas IOTA: solido, papilas, ascitis, Doppler). <b>CA-125</b> (sobre todo posmenopausica), "
        "HE4 + indice <b>ROMA</b>. En joven: AFP, beta-hCG, LDH (germinales).",
        "Endometrioma, EIP, mioma y embarazo elevan CA-125 (poco especifico en premenopausica).",
        "No se biopsia percutaneo: el dx y la estadificacion se hacen en la <b>cirugia</b>. Referir oncologia.",
    ),
    P + ["cancer_ovario"])


# ============================================================
# SUBDECK 3 - MENOS PREGUNTADOS: 17 cartas
# ============================================================
M = ["menos_preguntado"]

simple = [
    ("AMH (hormona antimulleriana)",
     "Marcador de <b>reserva ovarica</b> (no varia con el ciclo). Baja = reserva disminuida; muy alta sugiere SOP.",
     "reserva"),
    ("Histerosalpingografia (HSG)",
     "Evalua <b>permeabilidad tubarica</b> y cavidad uterina en infertilidad. Se hace en fase folicular, tras regla.",
     "infertilidad"),
    ("Histeroscopia",
     "Visualiza la cavidad y permite <b>biopsia dirigida</b>: polipos, miomas submucosos, sinequias, hiperplasia.",
     "sua"),
    ("Escala BI-RADS",
     "0 incompleto; 1 normal; 2 benigno; 3 probablemente benigno (control 6 m); <b>4-5 biopsia</b>; 6 maligno conocido.",
     "birads"),
    ("POP-Q (cuantificacion del prolapso)",
     "Mide descenso por <b>compartimento</b> respecto al himen. Anterior=cistocele, posterior=rectocele, apical=histero/cupula.",
     "prolapso"),
    ("Tests de incontinencia",
     "<b>Test de esfuerzo</b> (escape con tos) y Q-tip (hipermovilidad uretral) = IU de esfuerzo; <b>urodinamia</b> si dudas/mixta.",
     "incontinencia"),
    ("Densitometria (DXA)",
     "Dx de <b>osteoporosis</b> (T-score &le;-2.5) en climaterio/posmenopausia; -1 a -2.5 = osteopenia.",
     "climaterio"),
    ("17-OH-progesterona",
     "Elevada = <b>hiperplasia suprarrenal congenita no clasica</b>, imitador de SOP. Se pide en hiperandrogenismo.",
     "sop"),
    ("Prolactina elevada",
     "Galactorrea/amenorrea: confirmar (en ayuno, sin estres) y si persiste alta &rarr; <b>RM de hipofisis</b> (prolactinoma).",
     "amenorrea"),
    ("Colposcopia: hallazgos",
     "<b>Acetoblanco</b>, yodo (Schiller) <b>negativo</b>, mosaico, puntilleo, <b>vasos atipicos</b> &rarr; biopsia dirigida.",
     "citologia"),
    ("HE4 + indice ROMA",
     "Combinan con CA-125 para estimar <b>riesgo de malignidad</b> de masa anexial y decidir referencia oncologica.",
     "cancer_ovario"),
    ("NAAT vs cultivo (GC/clamidia)",
     "<b>NAAT</b> es la prueba de eleccion (mas sensible). Cultivo de gonococo si se requiere <b>sensibilidad antibiotica</b>.",
     "its"),
    ("Perfil metabolico en SOP",
     "Curva de tolerancia a la glucosa/HbA1c + perfil lipidico + TA: buscar <b>sindrome metabolico</b> y prediabetes.",
     "sop"),
    ("Marcadores de tumor germinal (joven)",
     "En masa ovarica de mujer joven: <b>AFP, beta-hCG, LDH</b> (disgerminoma, saco vitelino, coriocarcinoma).",
     "cancer_ovario"),
    ("Cariotipo en amenorrea",
     "Amenorrea primaria o falla ovarica precoz: descartar <b>Turner (45,X)</b> u otras disgenesias gonadales.",
     "amenorrea"),
    ("CA-125: interpretacion",
     "Util sobre todo en <b>posmenopausica</b>. En premenopausica es inespecifico (sube en endometriosis, EIP, mioma, embarazo).",
     "cancer_ovario"),
    ("Grosor endometrial: umbrales",
     "Posmenopausica con sangrado: <b>&gt;4-5 mm = biopsiar</b>. Sin sangrado el umbral es mayor. Premenopausica varia con el ciclo.",
     "cancer_endometrio"),
]

for titulo, texto, tag in simple:
    add(deck_menos, caso(titulo),
        f'<span class="bloque paraque"><span class="lab">Para que / como se lee</span>{texto}</span>',
        M + [tag])


# ============================================================
# Build / empaquetado
# ============================================================
def build():
    decks = [
        (deck_disc, "Estudios_01_Discriminadores.apkg"),
        (deck_panel, "Estudios_02_Paneles.apkg"),
        (deck_menos, "Estudios_03_Menos_preguntados.apkg"),
    ]
    for d, fname in decks:
        genanki.Package(d).write_to_file(os.path.join(OUTPUT_DIR, fname))
        print(f"  -> {fname} ({len(d.notes)} notas)")

    combined_out = os.path.join(OUTPUT_DIR, "No_Hay_Tiempo_Gineco_Estudios_TODOS.apkg")
    genanki.Package([deck_disc, deck_panel, deck_menos]).write_to_file(combined_out)
    total = sum(len(d.notes) for d in [deck_disc, deck_panel, deck_menos])
    print(f"  -> No_Hay_Tiempo_Gineco_Estudios_TODOS.apkg ({total} notas totales)")


if __name__ == "__main__":
    build()
