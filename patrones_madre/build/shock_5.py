"""Patron Madre: Shock 5 - Mapa por Estacion ECOE.

Quinto y ultimo deck de la serie shock. Deck integrador que conecta
los patrones clinicos con la estacion del examen y el manejo.

Formato dual (NO embudo de 4 niveles): cada escenario produce 2 cards.
- Card A (clinica -> dx): front = patron clinico; back = estacion + dx.
- Card B (dx -> manejo): front = estacion + dx; back = manejo.

16 escenarios x 2 cards = 32 cards.
Estaciones: medicina interna (5), cirugia (4), gineco-obstetricia (4), pediatria (3).
"""
import os
import genanki

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "output")
os.makedirs(OUTPUT_DIR, exist_ok=True)

MODEL_QA_ID = 1607392320  # reusable Q&A (mismo que shock_1-4 y gineco capa 5)
DECK_ID = 1593847062
DECK_NAME = "Patrones Madre::Shock 5 - Mapa por Estacion"

CSS = """
.card {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  font-size: 19px; text-align: left; color: #1a1a1a;
  background-color: #fafafa; padding: 20px; line-height: 1.55;
}
.nivel {
  display: inline-block; padding: 4px 12px; margin-bottom: 14px;
  background: #047857; color: #fff; border-radius: 6px;
  font-size: 13px; letter-spacing: 0.5px; font-weight: 600;
}
.estacion {
  display: inline-block; padding: 3px 10px; margin-left: 6px;
  background: #e0f2fe; color: #075985; border-radius: 6px;
  font-size: 13px; font-weight: 600;
}
.clinica {
  font-style: italic; margin-bottom: 12px; color: #374151;
  background: #fef3c7; padding: 10px 14px; border-radius: 6px;
}
.dx {
  font-size: 21px; font-weight: 700; color: #047857; margin-top: 4px;
}
.rama {
  color: #6b21a8; margin-top: 6px; font-size: 16px;
}
.manejo { margin-top: 8px; }
.prompt { color: #2563eb; font-weight: 600; margin-top: 10px; }
ol.items { margin: 8px 0 14px 0; padding-left: 24px; }
ol.items li { margin: 6px 0; }
#extra { margin-top: 16px; border: none; border-top: 1px solid #d4d4d4; padding-top: 12px; }
"""

model_qa = genanki.Model(
    MODEL_QA_ID,
    "Estudio Medico QA",
    fields=[{"name": "Front"}, {"name": "Back"}],
    templates=[{
        "name": "QA",
        "qfmt": "{{Front}}",
        "afmt": '{{Front}}<hr id="extra">{{Back}}',
    }],
    css=CSS,
)

deck = genanki.Deck(DECK_ID, DECK_NAME)

BASE_TAGS = ["patrones_madre", "ecoe", "shock_mapa_estacion"]


def add_note(front, back, tags):
    deck.add_note(genanki.Note(
        model=model_qa,
        fields=[front, back],
        tags=BASE_TAGS + tags,
    ))


def items(lst):
    return "<ol class='items'>" + "".join(f"<li>{x}</li>" for x in lst) + "</ol>"


HEADER_A = '<div class="nivel">CLINICA &rarr; ESTACION + DX</div>'
HEADER_B = '<div class="nivel">ESTACION + DX &rarr; MANEJO</div>'


def add_pair(estacion, estacion_slug, escenario_slug, clinica_front, dx_back, dx_front_estacion_label, dx_front_dx_label, manejo_back_list, rama=""):
    """Genera el par de cards A (clinica->dx) y B (dx->manejo)."""
    # Card A
    rama_html = f'<div class="rama">{rama}</div>' if rama else ""
    add_note(
        front=(
            HEADER_A +
            f'<div class="clinica">{clinica_front}</div>'
            '<div class="prompt">&iquest;Que estacion ECOE y que diagnostico?</div>'
        ),
        back=(
            f'<div class="dx">{estacion} &middot; {dx_back}</div>' + rama_html
        ),
        tags=["clinica_a_dx", estacion_slug, escenario_slug],
    )
    # Card B
    add_note(
        front=(
            HEADER_B +
            f'<div><span class="estacion">{dx_front_estacion_label}</span></div>'
            f'<div class="dx" style="margin-top:10px">{dx_front_dx_label}</div>'
            '<div class="prompt">&iquest;Cual es el manejo?</div>'
        ),
        back='<div class="manejo">' + items(manejo_back_list) + '</div>',
        tags=["dx_a_manejo", estacion_slug, escenario_slug],
    )


# ============================================================
# MEDICINA INTERNA (5 escenarios x 2 = 10 cards)
# ============================================================

add_pair(
    estacion="Medicina Interna",
    estacion_slug="medicina_interna",
    escenario_slug="sepsis",
    clinica_front="Adulto con fiebre + foco infeccioso identificable (neumonia, IVU, abdomen, piel) + hipotension + confusion / alteracion mental.",
    dx_back="Shock septico (distributivo)",
    dx_front_estacion_label="Medicina Interna",
    dx_front_dx_label="Shock septico",
    manejo_back_list=[
        "ABCDE + monitor + 2 vias IV",
        "<b>Hemocultivos antes</b> de antibiotico (si no retrasan)",
        "<b>Antibiotico empirico &lt; 1 hora</b> segun foco",
        "Cristaloides 30 mL/kg en bolos",
        "Lactato seriado",
        "<b>Noradrenalina</b> si TAM &lt; 65 tras volumen",
        "Control del foco (drenaje / cirugia / retirar dispositivo)",
        "UCI",
    ],
    rama="Rama madre: <b>septico / distributivo</b> (Shock 2)",
)

add_pair(
    estacion="Medicina Interna",
    estacion_slug="medicina_interna",
    escenario_slug="tep_masivo",
    clinica_front="Postquirurgica / inmovilizada con disnea subita + hipoxia + hipotension + ingurgitacion yugular + ansiedad intensa.",
    dx_back="Shock obstructivo por TEP masivo",
    dx_front_estacion_label="Medicina Interna",
    dx_front_dx_label="TEP masivo con shock",
    manejo_back_list=[
        "ABCDE + O&#8322; + monitor + 2 vias IV",
        "ECG + troponina",
        "<b>Eco bedside</b> (busca dilatacion de VD)",
        "AngioTAC pulmonar solo si estable",
        "<b>HNF IV</b> si no hay contraindicacion",
        "<b>Trombolisis sistemica</b> si TEP masivo con shock",
        "Noradrenalina; <b>evitar bolos grandes</b> (sobrecarga VD)",
        "UCI",
    ],
    rama="Rama madre: <b>obstructivo</b> (Shock 4)",
)

add_pair(
    estacion="Medicina Interna",
    estacion_slug="medicina_interna",
    escenario_slug="iam_complicado",
    clinica_front="Adulto con dolor toracico opresivo irradiado + diaforesis + hipotension + estertores bibasales + piel fria.",
    dx_back="Shock cardiogenico por IAM complicado",
    dx_front_estacion_label="Medicina Interna",
    dx_front_dx_label="IAM complicado con shock cardiogenico",
    manejo_back_list=[
        "ABCDE + monitor con desfibrilador + 2 vias IV",
        "<b>ECG &lt; 10 min</b> + troponinas seriadas",
        "O&#8322; solo si hipoxemia",
        "AAS + segundo antiagregante segun protocolo",
        "<b>Reperfusion urgente</b> (ICP primaria &lt; 90 min; fibrinolisis si no disponible)",
        "Noradrenalina &plusmn; dobutamina si shock",
        "<b>Evitar bolos de liquido</b> (salvo IAM de VD)",
        "UCC / hemodinamia",
    ],
    rama="Rama madre: <b>cardiogenico</b> (Shock 3)",
)

add_pair(
    estacion="Medicina Interna",
    estacion_slug="medicina_interna",
    escenario_slug="deshidratacion_severa",
    clinica_front="Vomito / diarrea de varios dias + mucosas secas + taquicardia + hipotension ortostatica + oliguria.",
    dx_back="Shock hipovolemico por perdidas GI",
    dx_front_estacion_label="Medicina Interna",
    dx_front_dx_label="Shock hipovolemico por perdidas GI",
    manejo_back_list=[
        "ABCDE + 2 vias IV",
        "Cristaloides IV en bolos",
        "<b>Electrolitos sericos (Na / K / HCO&#8323;)</b>",
        "Urea / creatinina",
        "Gasometria + lactato",
        "Vigilar diuresis",
    ],
    rama="Rama madre: <b>hipovolemico</b> (Shock 1)",
)

add_pair(
    estacion="Medicina Interna",
    estacion_slug="medicina_interna",
    escenario_slug="hda",
    clinica_front="Melena / hematemesis + palidez + taquicardia + hipotension.",
    dx_back="Shock hipovolemico hemorragico (HDA)",
    dx_front_estacion_label="Medicina Interna",
    dx_front_dx_label="Shock hemorragico por HDA",
    manejo_back_list=[
        "ABCDE + <b>2 vias gruesas</b>",
        "Cristaloide inicial",
        "<b>BH, grupo y cruzadas, coagulacion</b>",
        "Protocolo de transfusion si inestable",
        "IBP IV",
        "<b>Endoscopia urgente</b>",
        "Ingreso para vigilancia",
    ],
    rama="Rama madre: <b>hipovolemico hemorragico</b> (Shock 1)",
)


# ============================================================
# CIRUGIA (4 escenarios x 2 = 8 cards)
# ============================================================

add_pair(
    estacion="Cirugia",
    estacion_slug="cirugia",
    escenario_slug="trauma_abdominal",
    clinica_front="Golpe / arma blanca / proyectil de arma de fuego en abdomen + dolor + hipotension + palidez + abdomen distendido.",
    dx_back="Shock hipovolemico hemorragico por sangrado intraabdominal",
    dx_front_estacion_label="Cirugia",
    dx_front_dx_label="Trauma abdominal con shock",
    manejo_back_list=[
        "ABCDE / ATLS + <b>2 vias gruesas</b>",
        "Cristaloide inicial controlado",
        "Grupo y cruzadas",
        "<b>FAST</b>",
        "Protocolo de transfusion masiva si inestable",
        "<b>Laparotomia urgente</b> si FAST(+) e inestable",
    ],
    rama="Rama madre: <b>hipovolemico hemorragico</b> (Shock 1)",
)

add_pair(
    estacion="Cirugia",
    estacion_slug="cirugia",
    escenario_slug="hemorragia_interna",
    clinica_front="Palidez + dolor abdominal + abdomen distendido (aneurisma roto, sangrado retroperitoneal, ruptura de viscera) + hipotension.",
    dx_back="Shock hipovolemico hemorragico (hemorragia interna no traumatica)",
    dx_front_estacion_label="Cirugia",
    dx_front_dx_label="Hemorragia interna no traumatica en shock",
    manejo_back_list=[
        "ABCDE + 2 vias gruesas",
        "Cristaloide",
        "BH / grupo y cruzadas / coagulacion",
        "<b>eFAST</b> o <b>TAC</b> si estable",
        "Protocolo transfusion si inestable",
        "Cirugia / angioembolizacion segun hallazgo",
    ],
    rama="Rama madre: <b>hipovolemico hemorragico</b> (Shock 1)",
)

add_pair(
    estacion="Cirugia",
    estacion_slug="cirugia",
    escenario_slug="abdomen_septico",
    clinica_front="Dolor abdominal intenso + rebote / abdomen en tabla + fiebre + hipotension + taquicardia.",
    dx_back="Shock septico por peritonitis / abdomen septico",
    dx_front_estacion_label="Cirugia",
    dx_front_dx_label="Abdomen septico",
    manejo_back_list=[
        "ABCDE + ayuno + SNG + 2 vias",
        "Cristaloides + lactato",
        "<b>Piperacilina-tazobactam IV</b>",
        "TAC con contraste si estable (o Rx con aire libre)",
        "Hemocultivos + BH",
        "<b>Cirugia urgente &mdash; control de foco</b>",
    ],
    rama="Rama madre: <b>septico</b> (Shock 2)",
)

add_pair(
    estacion="Cirugia",
    estacion_slug="cirugia",
    escenario_slug="obstruccion_avanzada",
    clinica_front="Vomitos + distension + ausencia de canalizacion + deshidratacion + datos de choque (taquicardia / hipotension).",
    dx_back="Shock hipovolemico &plusmn; septico (si isquemia / perforacion)",
    dx_front_estacion_label="Cirugia",
    dx_front_dx_label="Obstruccion intestinal avanzada en shock",
    manejo_back_list=[
        "ABCDE + ayuno",
        "<b>SNG descompresiva</b>",
        "2 vias + cristaloides",
        "Electrolitos",
        "<b>Rx abdomen de pie / TAC abdomen</b>",
        "Valoracion quirurgica urgente si estrangulacion / perforacion",
    ],
    rama="Rama madre: <b>hipovolemico</b> (Shock 1) &plusmn; septico",
)


# ============================================================
# GINECO-OBSTETRICIA (4 escenarios x 2 = 8 cards)
# ============================================================

add_pair(
    estacion="Gineco-Obstetricia",
    estacion_slug="gineco_obstetricia",
    escenario_slug="ectopico_roto",
    clinica_front="Mujer fertil + amenorrea + dolor abdominal subito intenso + hipotension + palidez.",
    dx_back="Shock hipovolemico hemorragico por embarazo ectopico roto",
    dx_front_estacion_label="Gineco-Obstetricia",
    dx_front_dx_label="Ectopico roto en shock",
    manejo_back_list=[
        "ABCDE + 2 vias gruesas",
        "Cristaloide inicial",
        "BH / grupo y cruzadas",
        "<b>&beta;-hCG + USG transvaginal</b>",
        "Protocolo de transfusion",
        "<b>Cirugia urgente (salpingectomia)</b>",
    ],
    rama="Rama madre: <b>hipovolemico hemorragico</b> (Shock 1)",
)

add_pair(
    estacion="Gineco-Obstetricia",
    estacion_slug="gineco_obstetricia",
    escenario_slug="hpp",
    clinica_front="Posparto con sangrado vaginal abundante + utero atonico / trauma / restos placentarios + hipotension.",
    dx_back="Shock hipovolemico hemorragico por hemorragia posparto (HPP)",
    dx_front_estacion_label="Gineco-Obstetricia",
    dx_front_dx_label="HPP en shock",
    manejo_back_list=[
        "ABCDE + 2 vias gruesas + cristaloide",
        "<b>Masaje uterino bimanual + oxitocina IV</b>",
        "Identificar las <b>4 T</b> (tono / trauma / tejido / trombina)",
        "Ergonovina / carboprost / misoprostol segun causa",
        "Grupo y cruzadas + protocolo de transfusion",
        "Balon de Bakri / ligaduras / histerectomia si refractaria",
    ],
    rama="Rama madre: <b>hipovolemico hemorragico</b> (Shock 1)",
)

add_pair(
    estacion="Gineco-Obstetricia",
    estacion_slug="gineco_obstetricia",
    escenario_slug="abruptio",
    clinica_front="Embarazada en 3er trimestre + dolor abdominal + sangrado vaginal oscuro escaso + utero hipertonico / lenoso + sufrimiento fetal.",
    dx_back="Shock hemorragico por abruptio placentae (sangre oculta retroplacentaria, &plusmn; CID)",
    dx_front_estacion_label="Gineco-Obstetricia",
    dx_front_dx_label="Abruptio placentae con shock",
    manejo_back_list=[
        "ABCDE + 2 vias gruesas + cristaloide",
        "Grupo y cruzadas",
        "<b>Coagulacion</b> (riesgo de CID)",
        "<b>Monitoreo fetal continuo</b>",
        "<b>Cesarea urgente</b> si sufrimiento fetal o inestabilidad materna",
    ],
    rama="Rama madre: <b>hipovolemico hemorragico</b> (Shock 1)",
)

add_pair(
    estacion="Gineco-Obstetricia",
    estacion_slug="gineco_obstetricia",
    escenario_slug="sepsis_puerperal",
    clinica_front="Puerpera 3er-5&deg; dia + fiebre + dolor uterino + loquios fetidos + taquicardia + mal estado general.",
    dx_back="Shock septico por endometritis puerperal",
    dx_front_estacion_label="Gineco-Obstetricia",
    dx_front_dx_label="Endometritis puerperal septica",
    manejo_back_list=[
        "ABCDE + monitor + via IV + cristaloides",
        "BH + hemocultivos",
        "<b>Clindamicina + gentamicina IV</b>",
        "USG pelvico (descarta restos)",
        "<b>Legrado uterino si hay restos retenidos</b> (control de foco)",
        "EGO + urocultivo (descarta IVU asociada)",
    ],
    rama="Rama madre: <b>septico</b> (Shock 2)",
)


# ============================================================
# PEDIATRIA (3 escenarios x 2 = 6 cards)
# ============================================================

add_pair(
    estacion="Pediatria",
    estacion_slug="pediatria",
    escenario_slug="gea_pediatrica",
    clinica_front="Nino con diarrea / vomito + ojos hundidos + mucosas secas + llenado capilar &gt; 3 s + irritable que evoluciona a letargico.",
    dx_back="Shock hipovolemico por gastroenteritis",
    dx_front_estacion_label="Pediatria",
    dx_front_dx_label="Shock hipovolemico pediatrico por GEA",
    manejo_back_list=[
        "Vida suero oral en tomas pequenas si tolera",
        "ABCDE si esta en shock",
        "<b>Glucosa capilar</b>",
        "<b>Via IV o intraosea</b>",
        "<b>Bolo cristaloide 20 mL/kg</b> + reevaluar",
        "Corregir electrolitos",
        "Vigilar fontanela y nivel de conciencia",
    ],
    rama="Rama madre: <b>hipovolemico</b> (Shock 1)",
)

add_pair(
    estacion="Pediatria",
    estacion_slug="pediatria",
    escenario_slug="sepsis_neonatal",
    clinica_front="Recien nacido que no come + hipotermico (a veces febril) + letargico + llenado capilar lento + piel moteada.",
    dx_back="Shock septico neonatal",
    dx_front_estacion_label="Pediatria",
    dx_front_dx_label="Sepsis neonatal",
    manejo_back_list=[
        "ABCDE",
        "Control termico (incubadora / contacto piel)",
        "<b>Glucosa capilar</b> + corregir si baja",
        "Acceso IV o intraoseo",
        "Hemocultivo + BH + PCR / procalcitonina",
        "<b>Ampicilina + gentamicina IV urgente</b>",
        "Puncion lumbar si estable",
        "Bolos pequenos de cristaloide + reevaluar",
        "UCIN",
    ],
    rama="Rama madre: <b>septico</b> (Shock 2)",
)

add_pair(
    estacion="Pediatria",
    estacion_slug="pediatria",
    escenario_slug="dengue_sepsis_pediatrica",
    clinica_front="Nino con fiebre + dolor abdominal / vomitos + sangrado (petequias, gingivorragia) + llenado capilar lento + hipotension.",
    dx_back="Shock por dengue grave / sepsis pediatrica",
    dx_front_estacion_label="Pediatria",
    dx_front_dx_label="Choque por dengue grave / sepsis pediatrica",
    manejo_back_list=[
        "ABCDE + monitor + 2 vias IV",
        "<b>Bolo cristaloide 10-20 mL/kg</b> (cauteloso en dengue por fuga capilar)",
        "BH + <b>plaquetas + hematocrito seriado</b>",
        "<b>NS1 / serologia de dengue</b>",
        "Hemocultivos",
        "Antibiotico empirico si sepsis bacteriana",
        "UCIP",
    ],
    rama="Rama madre: <b>septico / distributivo</b> (Shock 2)",
)


# ============================================================
# Build
# ============================================================
def build():
    out_path = os.path.join(OUTPUT_DIR, "Patrones_Madre_Shock_5.apkg")
    genanki.Package(deck).write_to_file(out_path)
    print(f"OK: {out_path}  ({len(deck.notes)} notas)")


if __name__ == "__main__":
    build()
