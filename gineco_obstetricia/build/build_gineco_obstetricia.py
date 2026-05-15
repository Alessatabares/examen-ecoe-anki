"""Generador de 4 subdecks Anki para ECOE de Ginecología y Obstetricia.

Capas 1-3: Cloze (reglas CLAUDE.md).
Capa 4 (Manejo): Q&A clásico.
Verbalización ECOE siempre en campo Extra/Dorso.
"""
import os
import genanki

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "output")
os.makedirs(OUTPUT_DIR, exist_ok=True)

MODEL_CLOZE_ID = 1607392319
MODEL_QA_ID = 1607392320

DECK_ID_C1 = 1794603832
DECK_ID_C2 = 1117503696
DECK_ID_C3 = 2128563382
DECK_ID_C4 = 1409388293

DECK_NAME_C1 = "Gineco-Obstetricia Adulto::Capa 1 - Reconocimiento de Patron"
DECK_NAME_C2 = "Gineco-Obstetricia Adulto::Capa 2 - Exploracion Verbalizada"
DECK_NAME_C3 = "Gineco-Obstetricia Adulto::Capa 3 - Interpretacion de Estudios"
DECK_NAME_C4 = "Gineco-Obstetricia Adulto::Capa 4 - Manejo"

CSS_BASE = """
.card {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  font-size: 19px; text-align: left; color: #1a1a1a;
  background-color: #fafafa; padding: 20px; line-height: 1.55;
}
.cloze { font-weight: 600; color: #2563eb; }
#extra { margin-top: 16px; border: none; border-top: 1px solid #d4d4d4; padding-top: 12px; }
.ecoe { color: #b45309; font-style: italic; margin-top: 10px; display: block; }
.contraste { color: #6d28d9; display: block; margin-top: 6px; }
.tag { display: inline-block; padding: 2px 8px; background: #eef; border-radius: 4px; font-size: 13px; color: #334; }
b { color: #111; }
"""

model_cloze = genanki.Model(
    MODEL_CLOZE_ID,
    "Estudio Medico Cloze",
    fields=[{"name": "Text"}, {"name": "Extra"}],
    templates=[{
        "name": "Cloze",
        "qfmt": "{{cloze:Text}}",
        "afmt": '{{cloze:Text}}<hr id="extra">{{Extra}}',
    }],
    css=CSS_BASE,
    model_type=genanki.Model.CLOZE,
)

model_qa = genanki.Model(
    MODEL_QA_ID,
    "Estudio Medico QA",
    fields=[{"name": "Front"}, {"name": "Back"}],
    templates=[{
        "name": "QA",
        "qfmt": "{{Front}}",
        "afmt": '{{Front}}<hr id="extra">{{Back}}',
    }],
    css=CSS_BASE,
)

deck_c1 = genanki.Deck(DECK_ID_C1, DECK_NAME_C1)
deck_c2 = genanki.Deck(DECK_ID_C2, DECK_NAME_C2)
deck_c3 = genanki.Deck(DECK_ID_C3, DECK_NAME_C3)
deck_c4 = genanki.Deck(DECK_ID_C4, DECK_NAME_C4)

BASE_TAGS = ["gineco_obstetricia", "ecoe"]


def add_cloze(deck, text, extra, tags):
    note = genanki.Note(
        model=model_cloze,
        fields=[text, extra],
        tags=BASE_TAGS + tags,
    )
    deck.add_note(note)


def add_qa(deck, front, back, tags):
    note = genanki.Note(
        model=model_qa,
        fields=[front, back],
        tags=BASE_TAGS + tags,
    )
    deck.add_note(note)


# ============================================================
# CAPA 1 - RECONOCIMIENTO DE PATRON (40 cloze)
# ============================================================
C1 = ["capa1", "reconocimiento"]

# --- ITS / lesiones genitales (8)
add_cloze(deck_c1,
    "Vesiculas dolorosas en racimo + ardor + episodios recurrentes en region genital -> {{c1::Herpes genital}}",
    '<span class="contraste">Contraste: sifilis = ulcera UNICA INDOLORA.</span>'
    '<span class="ecoe">ECOE: "Cuadro compatible con herpes genital; diagnostico clinico, considerar PCR si duda."</span>',
    C1 + ["its", "herpes"])

add_cloze(deck_c1,
    "Ulcera unica + {{c1::indolora}} + bordes firmes + adenopatia {{c2::no dolorosa}} -> {{c3::Sifilis primaria (chancro)}}",
    '<span class="contraste">Contraste: herpes = vesiculas DOLOROSAS; chancroide = ulcera blanda DOLOROSA.</span>'
    '<span class="ecoe">ECOE: "Sospecho sifilis primaria, solicito VDRL/RPR y confirmacion treponemica."</span>',
    C1 + ["its", "sifilis"])

add_cloze(deck_c1,
    "Ulceras multiples + bordes irregulares + base purulenta + {{c1::dolorosas}} + adenopatia inguinal {{c2::dolorosa y fluctuante}} -> {{c3::Chancroide}}",
    '<span class="contraste">Agente: Haemophilus ducreyi.</span>'
    '<span class="ecoe">ECOE: "Patron de ulcera dolorosa con linfadenitis supurativa = chancroide."</span>',
    C1 + ["its", "chancroide"])

add_cloze(deck_c1,
    "Verrugas en coliflor + indoloras + multiples + region vulvar/perianal -> {{c1::Condilomas acuminados (VPH 6 y 11)}}",
    '<span class="contraste">No causan ulcera; serotipos 16 y 18 son los oncogenicos.</span>'
    '<span class="ecoe">ECOE: "Lesiones condilomatosas, tratamiento topico o ablativo; tamizaje cervical."</span>',
    C1 + ["its", "vph"])

add_cloze(deck_c1,
    "Fiebre + dolor pelvico bilateral + flujo + {{c1::dolor a la movilizacion cervical}} -> {{c2::EIP (Enfermedad Inflamatoria Pelvica)}}",
    '<span class="contraste">Criterio de Hager: 3 mayores (dolor abdominal bajo, anexial, movilizacion cervical) + 1 menor.</span>'
    '<span class="ecoe">ECOE: "Cuadro compatible con EIP, riesgo de infertilidad si no se trata; iniciar antibioticos."</span>',
    C1 + ["its", "eip"])

add_cloze(deck_c1,
    "Flujo {{c1::amarillo-verdoso espumoso}} + mal olor + cervix en {{c2::fresa}} + prurito -> {{c3::Tricomoniasis}}",
    '<span class="contraste">Trichomonas vaginalis. ITS: tratar pareja.</span>'
    '<span class="ecoe">ECOE: "Patron clasico de tricomoniasis; metronidazol VO."</span>',
    C1 + ["its", "tricomoniasis"])

add_cloze(deck_c1,
    "Flujo {{c1::blanco grumoso (queso cottage)}} + prurito vulvar intenso + sin olor -> {{c2::Candidiasis vulvovaginal}}",
    '<span class="contraste">No es ITS clasica. Factores: ATB, embarazo, DM.</span>'
    '<span class="ecoe">ECOE: "Candidiasis no complicada; fluconazol VO 150 mg dosis unica."</span>',
    C1 + ["its", "candidiasis"])

add_cloze(deck_c1,
    "Flujo {{c1::gris homogeneo}} con olor a {{c2::pescado}} + SIN inflamacion ni prurito + pH >4.5 -> {{c3::Vaginosis bacteriana}}",
    '<span class="contraste">Criterios de Amsel (3 de 4); celulas clue al microscopio.</span>'
    '<span class="ecoe">ECOE: "Vaginosis bacteriana, no requiere tratar pareja."</span>',
    C1 + ["its", "vaginosis"])

# --- Cervix / tamizaje (5)
add_cloze(deck_c1,
    "{{c1::Sangrado postcoital}} + lesion friable visible en cuello uterino + mujer sexualmente activa -> {{c2::Lesion cervical (NIC alto grado o Ca cervix hasta descartar)}}",
    '<span class="contraste">Toda lesion sospechosa requiere biopsia, NO solo PAP.</span>'
    '<span class="ecoe">ECOE: "Lesion sospechosa, refiero a colposcopia y biopsia."</span>',
    C1 + ["cervix", "tamizaje"])

add_cloze(deck_c1,
    "PAP con resultado {{c1::ASCUS}} en mujer >=25 anos -> conducta: {{c2::test de VPH}}",
    '<span class="contraste">ASCUS = atipia escamosa de significado indeterminado.</span>'
    '<span class="ecoe">ECOE: "Triage con VPH; si positivo, colposcopia."</span>',
    C1 + ["cervix", "pap"])

add_cloze(deck_c1,
    "PAP con {{c1::LSIL}} (lesion intraepitelial bajo grado) -> conducta: {{c2::colposcopia con biopsia dirigida}}",
    '<span class="contraste">LSIL en <25 anos puede vigilarse 12 meses.</span>'
    '<span class="ecoe">ECOE: "LSIL requiere colposcopia para descartar NIC2-3."</span>',
    C1 + ["cervix", "pap"])

add_cloze(deck_c1,
    "PAP con {{c1::HSIL}} (lesion intraepitelial alto grado) -> conducta: {{c2::colposcopia con biopsia inmediata}}, considerar {{c3::cono cervical}} si se confirma",
    '<span class="contraste">HSIL = NIC2-3, precursor de Ca cervical.</span>'
    '<span class="ecoe">ECOE: "HSIL requiere manejo escisional (LEEP/cono)."</span>',
    C1 + ["cervix", "pap"])

add_cloze(deck_c1,
    "{{c1::Sangrado postmenopausico}} + endometrio engrosado >5 mm en USG -> {{c2::Ca de endometrio hasta demostrar lo contrario}}",
    '<span class="contraste">Estudio de eleccion: biopsia endometrial.</span>'
    '<span class="ecoe">ECOE: "Sangrado postmenopausico = bandera roja, biopsia endometrial."</span>',
    C1 + ["endometrio", "cancer"])

# --- Mama (6)
add_cloze(deck_c1,
    "Nodulo mamario {{c1::duro}}, {{c2::fijo}}, irregular, {{c3::indoloro}} + retraccion de piel o pezon -> {{c4::Carcinoma de mama}}",
    '<span class="contraste">Edad >40, signos de alarma cutaneos = referencia urgente.</span>'
    '<span class="ecoe">ECOE: "Nodulo con caracteristicas malignas, mastografia + biopsia core."</span>',
    C1 + ["mama", "cancer"])

add_cloze(deck_c1,
    "Mujer joven (15-30 anos) + nodulo mamario {{c1::movil}}, firme, {{c2::indoloro}}, bien delimitado -> {{c3::Fibroadenoma}}",
    '<span class="contraste">Benigno; USG es el estudio inicial.</span>'
    '<span class="ecoe">ECOE: "Fibroadenoma, observacion + USG control 6 meses."</span>',
    C1 + ["mama", "benigno"])

add_cloze(deck_c1,
    "Masa mamaria {{c1::movil}}, {{c2::dolorosa}}, ciclica (premenstrual) + fluctuante -> {{c3::Quiste mamario}}",
    '<span class="contraste">Confirmar con USG; aspiracion si sintomatico.</span>'
    '<span class="ecoe">ECOE: "Quiste mamario; aspiracion guiada por USG si molesta."</span>',
    C1 + ["mama", "benigno"])

add_cloze(deck_c1,
    "Mama eritematosa + dolorosa + caliente + fiebre + paciente {{c1::lactando}} -> {{c2::Mastitis puerperal}}",
    '<span class="contraste">Agente mas frecuente: S. aureus. Continuar lactancia.</span>'
    '<span class="ecoe">ECOE: "Mastitis puerperal, dicloxacilina VO + vaciamiento."</span>',
    C1 + ["mama", "infeccion"])

add_cloze(deck_c1,
    "Telorrea {{c1::sanguinolenta}} {{c2::unilateral}} espontanea por un solo conducto -> sospecha de {{c3::papiloma intraductal o Ca}}",
    '<span class="contraste">Mastografia + ductografia/USG.</span>'
    '<span class="ecoe">ECOE: "Telorrea sanguinolenta unilateral: descartar malignidad."</span>',
    C1 + ["mama", "telorrea"])

add_cloze(deck_c1,
    "{{c1::Eccema unilateral del pezon}} que no responde a topicos + descamacion + retraccion -> {{c2::Enfermedad de Paget de la mama}}",
    '<span class="contraste">Asociada a carcinoma subyacente. Biopsia obligada.</span>'
    '<span class="ecoe">ECOE: "Paget de mama, biopsia y mastografia."</span>',
    C1 + ["mama", "paget"])

# --- Ginecologia general (8)
add_cloze(deck_c1,
    "Mujer joven + {{c1::oligomenorrea}} + {{c2::hirsutismo}}/acne + obesidad + acantosis -> {{c3::SOP (Sindrome de ovario poliquistico)}}",
    '<span class="contraste">Rotterdam: 2 de 3 (oligo-anovulacion, hiperandrogenismo, ovarios poliquisticos).</span>'
    '<span class="ecoe">ECOE: "Patron compatible con SOP, evaluar metabolico + fertilidad."</span>',
    C1 + ["sop"])

add_cloze(deck_c1,
    "{{c1::Dismenorrea progresiva}} + {{c2::dispareunia profunda}} + {{c3::infertilidad}} + dolor pelvico cronico -> {{c4::Endometriosis}}",
    '<span class="contraste">Gold standard dx: laparoscopia con biopsia.</span>'
    '<span class="ecoe">ECOE: "Triada clasica de endometriosis; inicio empirico AINE + ACO."</span>',
    C1 + ["endometriosis"])

add_cloze(deck_c1,
    "{{c1::Sangrado menstrual abundante}} + utero {{c2::aumentado de tamano irregular}} + sensacion de masa pelvica -> {{c3::Miomatosis uterina}}",
    '<span class="contraste">Confirmacion: USG pelvico.</span>'
    '<span class="ecoe">ECOE: "Miomatosis sintomatica; opciones medicas o quirurgicas."</span>',
    C1 + ["miomatosis"])

add_cloze(deck_c1,
    "{{c1::Amenorrea >12 meses}} + bochornos + sudoracion nocturna + atrofia vaginal en mujer {{c2::~50 anos}} -> {{c3::Menopausia/climaterio}}",
    '<span class="contraste">Dx clinico; FSH >25-40 mUI/mL confirma si duda.</span>'
    '<span class="ecoe">ECOE: "Climaterio sintomatico; evaluar TRH si <60 anos sin contraindicaciones."</span>',
    C1 + ["climaterio"])

add_cloze(deck_c1,
    "{{c1::Sensacion de bulto vaginal}} que empeora con esfuerzo + incontinencia o disuria + multipara -> {{c2::Prolapso de organos pelvicos}}",
    '<span class="contraste">Clasificacion POP-Q.</span>'
    '<span class="ecoe">ECOE: "Prolapso; ejercicios de Kegel, pesario o cirugia segun grado."</span>',
    C1 + ["prolapso"])

add_cloze(deck_c1,
    "Tumoracion dolorosa en {{c1::labio mayor}} + fluctuante + edema + fiebre local -> {{c2::Absceso de glandula de Bartholino}}",
    '<span class="contraste">Tratamiento: drenaje (marsupializacion o cateter de Word).</span>'
    '<span class="ecoe">ECOE: "Absceso de Bartholino, drenaje + antibiotico si celulitis."</span>',
    C1 + ["bartholino"])

add_cloze(deck_c1,
    "Mujer >50 anos + {{c1::masa pelvica}} + {{c2::ascitis}} + perdida de peso + distension abdominal -> {{c3::Ca de ovario hasta demostrar lo contrario}}",
    '<span class="contraste">Marcador CA-125. USG transvaginal inicial.</span>'
    '<span class="ecoe">ECOE: "Sospecha Ca ovario, referencia a oncologia ginecologica."</span>',
    C1 + ["ovario", "cancer"])

add_cloze(deck_c1,
    "Pareja con {{c1::>=1 ano}} de relaciones sin proteccion sin lograr embarazo (o {{c2::>=6 meses}} si mujer >35 anos) -> {{c3::Infertilidad - iniciar estudio de pareja}}",
    '<span class="contraste">Estudio basico: espermograma + USG + perfil hormonal + permeabilidad tubaria.</span>'
    '<span class="ecoe">ECOE: "Infertilidad primaria; estudio integral de pareja."</span>',
    C1 + ["infertilidad"])

# --- Obstetricia: sangrado (5)
add_cloze(deck_c1,
    "Mujer ~7 sem + {{c1::dolor abdominal unilateral}} + sangrado escaso + beta-hCG (+) {{c2::sin saco intrauterino}} en USG -> {{c3::Embarazo ectopico}}",
    '<span class="contraste">Zona discriminatoria beta-hCG: 1500-2000 mUI/mL.</span>'
    '<span class="ecoe">ECOE: "Sospecha de ectopico; estabilizar y definir manejo medico vs quirurgico."</span>',
    C1 + ["obstetricia", "sangrado_1t", "ectopico"])

add_cloze(deck_c1,
    "8 sem + sangrado leve + dolor leve + {{c1::cuello cerrado}} + embrion vivo en USG -> {{c2::Amenaza de aborto}}",
    '<span class="contraste">Aborto en curso = cuello abierto + sangrado activo; diferido = embrion sin LCF.</span>'
    '<span class="ecoe">ECOE: "Amenaza de aborto, reposo relativo, vigilancia."</span>',
    C1 + ["obstetricia", "sangrado_1t", "aborto"])

add_cloze(deck_c1,
    ">20 sem + sangrado {{c1::indoloro}} + rojo rutilante + sin dolor abdominal + utero NO doloroso -> {{c2::Placenta previa}}",
    '<span class="contraste">NO HACER TACTO VAGINAL hasta USG.</span>'
    '<span class="ecoe">ECOE: "Sangrado del 3er trimestre indoloro = placenta previa hasta demostrar lo contrario."</span>',
    C1 + ["obstetricia", "sangrado_3t", "previa"])

add_cloze(deck_c1,
    ">20 sem + {{c1::dolor abdominal subito}} + sangrado oscuro escaso + {{c2::abdomen en tabla (utero leniroso)}} + sufrimiento fetal -> {{c3::DPPNI (Desprendimiento Prematuro de Placenta Normoinserta)}}",
    '<span class="contraste">Factor de riesgo principal: HTA / preeclampsia, cocaina, trauma.</span>'
    '<span class="ecoe">ECOE: "DPPNI, interrupcion urgente; riesgo CID."</span>',
    C1 + ["obstetricia", "sangrado_3t", "dppni"])

add_cloze(deck_c1,
    "1er trimestre + sangrado + altura uterina {{c1::mayor}} a lo esperado + hiperemesis + beta-hCG {{c2::muy elevada}} + USG en panal de abeja -> {{c3::Enfermedad trofoblastica (mola hidatiforme)}}",
    '<span class="contraste">No hay embrion en mola completa.</span>'
    '<span class="ecoe">ECOE: "Mola hidatiforme; AMEU + seguimiento de beta-hCG semanal hasta negativizar."</span>',
    C1 + ["obstetricia", "mola"])

# --- Obstetricia: HTA (4)
add_cloze(deck_c1,
    ">20 sem + TA >=140/90 (2 tomas) + {{c1::proteinuria >=300 mg/24h}} -> {{c2::Preeclampsia}}",
    '<span class="contraste">Sin proteinuria, criterios de organo blanco tambien diagnostican.</span>'
    '<span class="ecoe">ECOE: "Preeclampsia, vigilancia hospitalaria + planeacion de interrupcion."</span>',
    C1 + ["obstetricia", "preeclampsia"])

add_cloze(deck_c1,
    "Preeclampsia + TA &gt;=160/110 + {{c1::cefalea persistente}} + {{c2::epigastralgia}} + {{c3::vision borrosa/escotomas}} -> {{c4::Preeclampsia con datos de severidad}}",
    '<span class="contraste">Cualquier criterio de severidad = manejo intensivo + interrupcion segun semanas.</span>'
    '<span class="ecoe">ECOE: "Preeclampsia severa, sulfato de Mg + antihipertensivo + interrupcion."</span>',
    C1 + ["obstetricia", "preeclampsia"])

add_cloze(deck_c1,
    "{{c1::Convulsion tonico-clonica}} en embarazada con preeclampsia (o sin dx previo) sin otra causa -> {{c2::Eclampsia}}",
    '<span class="contraste">Tratamiento de eleccion: sulfato de Mg.</span>'
    '<span class="ecoe">ECOE: "Eclampsia, ABC, sulfato de Mg, interrupcion del embarazo."</span>',
    C1 + ["obstetricia", "eclampsia"])

add_cloze(deck_c1,
    "Preeclampsia + {{c1::hemolisis (LDH alta, esquistocitos)}} + {{c2::AST/ALT elevadas}} + {{c3::plaquetas &lt;100,000}} -> {{c4::Sindrome HELLP}}",
    '<span class="contraste">Variante grave de preeclampsia; interrupcion sin demora.</span>'
    '<span class="ecoe">ECOE: "HELLP, riesgo materno alto, interrupcion urgente."</span>',
    C1 + ["obstetricia", "hellp"])

# --- Obstetricia: otros (4)
add_cloze(deck_c1,
    "Embarazada {{c1::24-36.6 sem}} + contracciones regulares + {{c2::modificaciones cervicales}} -> {{c3::Trabajo de parto pretermino}}",
    '<span class="contraste">Tocolisis + maduracion pulmonar + neuroproteccion <32 sem.</span>'
    '<span class="ecoe">ECOE: "Parto pretermino, tocolisis + betametasona + sulfato Mg <32 sem."</span>',
    C1 + ["obstetricia", "pretermino"])

add_cloze(deck_c1,
    "{{c1::RPM}} + fiebre materna + taquicardia materna y fetal + dolor uterino + leucorrea fetida -> {{c2::Corioamnionitis}}",
    '<span class="contraste">Independiente de edad gestacional: ANTIBIOTICO + interrupcion.</span>'
    '<span class="ecoe">ECOE: "Corioamnionitis, ampicilina + gentamicina + interrupcion."</span>',
    C1 + ["obstetricia", "corioamnionitis"])

add_cloze(deck_c1,
    "Embarazo de {{c1::>=42 semanas}} sin trabajo de parto -> {{c2::Embarazo prolongado/postermino}}",
    '<span class="contraste">Riesgo: oligohidramnios, sufrimiento fetal, macrosomia.</span>'
    '<span class="ecoe">ECOE: "Postermino, evaluar Bishop e inducir."</span>',
    C1 + ["obstetricia", "postermino"])

add_cloze(deck_c1,
    "Postparto + sangrado >{{c1::500 mL (parto) / 1000 mL (cesarea)}} + utero {{c2::blando, no contraido}} -> {{c3::Hemorragia postparto por atonia uterina}}",
    '<span class="contraste">Causa mas frecuente de HPP (la primera T).</span>'
    '<span class="ecoe">ECOE: "Atonia uterina, masaje + oxitocina + uterotonicos adicionales."</span>',
    C1 + ["obstetricia", "hpp"])

# ============================================================
# CAPA 2 - EXPLORACION VERBALIZADA (35 cloze)
# ============================================================
C2 = ["capa2", "exploracion"]

add_cloze(deck_c2,
    "Exploracion ginecologica completa - secuencia: {{c1::consentimiento informado}} -> {{c2::posicion de litotomia}} -> {{c3::inspeccion vulvar}} -> {{c4::especuloscopia}} -> {{c5::PAP si indicado}} -> {{c6::retiro de especulo}} -> {{c7::tacto bimanual}} -> {{c8::explicacion y plan}}",
    '<span class="ecoe">ECOE: verbalizar cada paso al sinodal; este flujo da el 70% de la calificacion.</span>',
    C2 + ["ginecologica"])

add_cloze(deck_c2,
    "Insercion del especulo: {{c1::lubricar con agua tibia (no gel)}} -> {{c2::inserir oblicuo cerrado}} -> {{c3::rotar a horizontal}} -> {{c4::abrir lentamente para visualizar cervix}}",
    '<span class="ecoe">ECOE: "Voy a colocar el especulo; le aviso, sentira presion."</span>',
    C2 + ["especuloscopia"])

add_cloze(deck_c2,
    "En especuloscopia describir: {{c1::color y caracteristicas de la mucosa}}, {{c2::flujo (cantidad, color, olor)}}, {{c3::lesiones cervicales o vaginales}}, {{c4::sangrado activo}}, {{c5::aspecto del cervix (forma del orificio, friabilidad)}}",
    '<span class="ecoe">ECOE: "Describo el cervix como rosado, con flujo fisiologico, sin lesiones."</span>',
    C2 + ["especuloscopia"])

add_cloze(deck_c2,
    "Toma de PAP convencional: {{c1::espatula de Ayre en exocervix con giro de 360 grados}} + {{c2::cytobrush en endocervix con giro de 180 grados}} -> {{c3::extendido en portaobjetos}} -> {{c4::fijacion con alcohol o spray}}",
    '<span class="ecoe">ECOE: "Tomo muestra exo y endocervical, fijo y rotulo correctamente."</span>',
    C2 + ["pap"])

add_cloze(deck_c2,
    "Indicaciones de PAP: inicio a los {{c1::25 anos}} o 3 anos posteriores al inicio de vida sexual; hasta los {{c2::65 anos}}; intervalo {{c3::cada 3 anos}} hasta los 30 y luego {{c4::cada 5 anos con co-test VPH}}",
    '<span class="ecoe">ECOE: "Esta paciente requiere PAP por su edad y antecedentes."</span>',
    C2 + ["pap", "tamizaje"])

add_cloze(deck_c2,
    "Tacto bimanual evalua: {{c1::tamano, posicion y consistencia uterina}}; {{c2::dolor a la movilizacion cervical}}; {{c3::presencia de masas anexiales}}; {{c4::caracteristicas del fondo de saco}}",
    '<span class="ecoe">ECOE: "Realizo tacto bimanual con consentimiento; informo a la paciente."</span>',
    C2 + ["tacto_bimanual"])

add_cloze(deck_c2,
    "Utero no gravido normal: tamano {{c1::7-8 cm}}, {{c2::movil}}, {{c3::indoloro}}, en {{c4::anteversoflexion}} habitualmente",
    '<span class="ecoe">ECOE: "Utero de caracteristicas normales en exploracion."</span>',
    C2 + ["tacto_bimanual"])

add_cloze(deck_c2,
    "Exploracion de mama - inspeccion estatica: paciente {{c1::sentada con brazos relajados}}; buscar {{c2::asimetria}}, {{c3::retraccion de piel}}, {{c4::piel de naranja}}, {{c5::cambios del pezon (desviacion, retraccion, ulceracion)}}",
    '<span class="ecoe">ECOE: "Inspeccion estatica: mamas simetricas, sin retracciones."</span>',
    C2 + ["mama"])

add_cloze(deck_c2,
    "Exploracion de mama - inspeccion dinamica: {{c1::brazos elevados}}, {{c2::manos en cadera empujando}}, {{c3::inclinarse hacia adelante}} para evidenciar retracciones cutaneas",
    '<span class="ecoe">ECOE: "Maniobras dinamicas sin alteraciones."</span>',
    C2 + ["mama"])

add_cloze(deck_c2,
    "Palpacion mamaria: paciente {{c1::en decubito con brazo ipsilateral elevado}}; patron {{c2::sistematico (radial o concentrico)}}; con {{c3::pulpejos de 3 dedos}} en {{c4::3 presiones (superficial, media, profunda)}}",
    '<span class="ecoe">ECOE: "Palpacion sistematica en los 4 cuadrantes y cola axilar."</span>',
    C2 + ["mama"])

add_cloze(deck_c2,
    "Palpacion ganglionar mamaria: regiones {{c1::axilar}}, {{c2::supraclavicular}}, {{c3::infraclavicular}}",
    '<span class="ecoe">ECOE: "Sin adenopatias palpables."</span>',
    C2 + ["mama"])

add_cloze(deck_c2,
    "Exploracion del pezon: {{c1::expresion suave}} para descartar telorrea; si secrecion, caracterizar {{c2::color, unilateralidad, espontanea vs provocada}}",
    '<span class="ecoe">ECOE: "Sin telorrea a la expresion."</span>',
    C2 + ["mama"])

add_cloze(deck_c2,
    "Exploracion obstetrica basica: {{c1::TA}}, {{c2::peso}}, {{c3::edema}}, {{c4::reflejos osteotendinosos}}, {{c5::altura uterina}}, {{c6::FCF}}, {{c7::movimientos fetales reportados}}",
    '<span class="ecoe">ECOE: "Exploracion obstetrica sin datos de alarma."</span>',
    C2 + ["obstetrica"])

add_cloze(deck_c2,
    "Altura uterina (regla de McDonald) coincide con {{c1::semanas de gestacion +/- 2 cm}} entre las {{c2::20 y 34 semanas}}",
    '<span class="ecoe">ECOE: "AU acorde a edad gestacional."</span>',
    C2 + ["obstetrica"])

add_cloze(deck_c2,
    "Maniobras de Leopold: {{c1::1a fondo (que polo: cefalico/pelvico)}} -> {{c2::2a flancos (situacion y dorso)}} -> {{c3::3a segmento inferior (presentacion movil vs encajada)}} -> {{c4::4a pelvis (grado de encajamiento)}}",
    '<span class="ecoe">ECOE: "Realizo Leopold para determinar situacion, presentacion y posicion."</span>',
    C2 + ["leopold"])

add_cloze(deck_c2,
    "FCF normal: {{c1::110-160 lpm}}; auscultacion con {{c2::Doppler obstetrico}} desde semana {{c3::10-12}} y con {{c4::Pinard}} desde semana 20",
    '<span class="ecoe">ECOE: "FCF dentro de parametros normales."</span>',
    C2 + ["fcf"])

add_cloze(deck_c2,
    "Tacto vaginal obstetrico evalua: {{c1::dilatacion}}, {{c2::borramiento}}, {{c3::consistencia cervical}}, {{c4::posicion del cervix}}, {{c5::altura de la presentacion (planos de Hodge / De Lee)}}",
    '<span class="ecoe">ECOE: "Cervix con X cm dilatacion, Y% borramiento."</span>',
    C2 + ["tacto_obstetrico"])

add_cloze(deck_c2,
    "Score de Bishop evalua: {{c1::dilatacion}}, {{c2::borramiento}}, {{c3::consistencia}}, {{c4::posicion cervical}}, {{c5::altura de presentacion}}; favorable para induccion si >={{c6::7-8}}",
    '<span class="ecoe">ECOE: "Bishop X, cervix favorable/desfavorable para induccion."</span>',
    C2 + ["bishop"])

add_cloze(deck_c2,
    "Fases del trabajo de parto: {{c1::fase latente (<6 cm)}} -> {{c2::fase activa (>=6 cm hasta dilatacion completa)}} -> {{c3::expulsivo}} -> {{c4::alumbramiento}}",
    '<span class="ecoe">ECOE: "Paciente en fase activa de trabajo de parto."</span>',
    C2 + ["parto"])

add_cloze(deck_c2,
    "Signos de trabajo de parto verdadero: contracciones {{c1::regulares}} en frecuencia/duracion/intensidad creciente + {{c2::modificaciones cervicales}}",
    '<span class="contraste">Falso trabajo (Braxton-Hicks): irregulares, sin modificaciones.</span>'
    '<span class="ecoe">ECOE: "Trabajo de parto verdadero, ingreso a labor."</span>',
    C2 + ["parto"])

add_cloze(deck_c2,
    "Signos de RPM: {{c1::salida franca de liquido por vagina}}; pruebas: {{c2::cristalizacion en helecho}} y {{c3::test de nitrazina (vira a azul, pH alcalino)}}",
    '<span class="ecoe">ECOE: "Sospecho RPM, confirmo con cristalizacion y nitrazina."</span>',
    C2 + ["rpm"])

add_cloze(deck_c2,
    "Datos de alarma en embarazo (verbalizar siempre al alta): {{c1::cefalea persistente}}, {{c2::vision borrosa/escotomas}}, {{c3::epigastralgia}}, {{c4::edema subito}}, {{c5::sangrado vaginal}}, {{c6::disminucion de movimientos fetales}}, {{c7::perdida de liquido}}, {{c8::contracciones <37 sem}}",
    '<span class="ecoe">ECOE: "Explico datos de alarma para acudir a urgencias."</span>',
    C2 + ["alarma"])

add_cloze(deck_c2,
    "Conteo de movimientos fetales (test de Cardiff): {{c1::>=10 movimientos en 2 horas}}; si menos -> {{c2::acudir a urgencias}}",
    '<span class="ecoe">ECOE: "Si nota menos de 10 movimientos en 2 horas, acude."</span>',
    C2 + ["alarma"])

add_cloze(deck_c2,
    "Indicaciones de USG urgente en embarazo: {{c1::sangrado vaginal}}, {{c2::dolor abdominal severo}}, {{c3::disminucion de movimientos fetales}}, {{c4::altura uterina discordante}}",
    '<span class="ecoe">ECOE: "USG obstetrico urgente por X dato de alarma."</span>',
    C2 + ["alarma"])

add_cloze(deck_c2,
    "Consejeria previa a PAP: {{c1::explicar para que sirve (tamizaje de cancer cervical)}}, {{c2::describir el procedimiento}}, {{c3::informar sensaciones esperadas}}, {{c4::aclarar cuando y como recibira el resultado}}",
    '<span class="ecoe">ECOE: "Le explico que tomare una muestra del cuello uterino..."</span>',
    C2 + ["consejeria"])

add_cloze(deck_c2,
    "Autoexploracion mamaria: a partir de los {{c1::20 anos}}, {{c2::una vez al mes}}, {{c3::dia 7-10 del ciclo (postmenstrual)}}; en postmenopausia, dia fijo del mes",
    '<span class="ecoe">ECOE: "Le ensenare la autoexploracion paso a paso."</span>',
    C2 + ["mama", "consejeria"])

add_cloze(deck_c2,
    "Tamizaje de cancer de mama: mamografia a partir de los {{c1::40 anos}} (o 50 segun guia) cada {{c2::1-2 anos}}; USG complementario si {{c3::mama densa}} o {{c4::<40 anos}}",
    '<span class="ecoe">ECOE: "Por edad le corresponde mamografia de tamizaje."</span>',
    C2 + ["mama", "tamizaje"])

add_cloze(deck_c2,
    "Consejeria anticonceptiva: explorar {{c1::deseo reproductivo}}, {{c2::comorbilidades}}, {{c3::lactancia}}, {{c4::edad y tabaquismo}}, {{c5::riesgo de ITS}}",
    '<span class="ecoe">ECOE: "Le explico los metodos disponibles segun su perfil."</span>',
    C2 + ["anticoncepcion", "consejeria"])

add_cloze(deck_c2,
    "Maniobra de McRoberts: {{c1::hiperflexion de muslos sobre el abdomen materno}} + {{c2::presion suprapubica}} ante {{c3::distocia de hombros}}",
    '<span class="ecoe">ECOE: "Pido McRoberts y presion suprapubica, NUNCA presion fundica."</span>',
    C2 + ["distocia"])

add_cloze(deck_c2,
    "Despegamiento de membranas (maniobra de Hamilton): {{c1::dedo en orificio cervical interno}} con movimiento {{c2::circular}} para separar membranas, para {{c3::favorecer inicio espontaneo de trabajo de parto}}",
    '<span class="ecoe">ECOE: "Realizo despegamiento para favorecer trabajo de parto."</span>',
    C2 + ["induccion"])

add_cloze(deck_c2,
    "Compresion bimanual uterina (ante atonia): {{c1::una mano en vagina sobre cara anterior del utero}} + {{c2::la otra abdominal sobre el fondo}} comprimiendo entre ambas",
    '<span class="ecoe">ECOE: "Compresion bimanual mientras administro uterotonicos."</span>',
    C2 + ["hpp"])

add_cloze(deck_c2,
    "NO realizar tacto vaginal en: {{c1::sangrado del 3er trimestre antes de descartar placenta previa}} ni en {{c2::RPM sin trabajo de parto activo}} (riesgo de infeccion)",
    '<span class="ecoe">ECOE: "Difiero el tacto hasta descartar placenta previa por USG."</span>',
    C2 + ["contraindicaciones"])

add_cloze(deck_c2,
    "Posiciones obstetricas utiles: {{c1::litotomia}} para parto y exploracion; {{c2::decubito lateral izquierdo}} para optimizar perfusion utero-placentaria (evita compresion de cava)",
    '<span class="ecoe">ECOE: "La coloco en decubito lateral izquierdo para mejorar el flujo."</span>',
    C2 + ["posicion"])

add_cloze(deck_c2,
    "Test de Cristalizacion (RPM): liquido amniotico en porta + secado al aire -> patron en {{c1::hojas de helecho}} = positivo",
    '<span class="ecoe">ECOE: "Cristalizacion positiva confirma RPM."</span>',
    C2 + ["rpm"])

add_cloze(deck_c2,
    "Auscultacion cardiaca fetal: localizar dorso por Leopold; FCF se ausculta sobre {{c1::el dorso fetal}}; en cefalica = {{c2::cuadrante inferior}}, en pelvica = {{c3::cuadrante superior}}",
    '<span class="ecoe">ECOE: "Ausculto FCF en cuadrante correspondiente al dorso."</span>',
    C2 + ["fcf", "leopold"])

# ============================================================
# CAPA 3 - INTERPRETACION DE ESTUDIOS (40 cloze)
# ============================================================
C3 = ["capa3", "estudios"]

add_cloze(deck_c3,
    "PAP ASCUS en mujer >=25 anos -> conducta: {{c1::triage con VPH}}; si VPH (-) repetir en {{c2::1 ano}}, si VPH (+) {{c3::colposcopia}}",
    '<span class="ecoe">ECOE: "ASCUS, indico VPH para definir conducta."</span>',
    C3 + ["pap"])

add_cloze(deck_c3,
    "PAP LSIL -> {{c1::colposcopia con biopsia dirigida}}",
    '<span class="contraste">En <25 anos puede vigilarse 12 meses.</span>'
    '<span class="ecoe">ECOE: "LSIL, refiero a colposcopia."</span>',
    C3 + ["pap"])

add_cloze(deck_c3,
    "PAP HSIL -> {{c1::colposcopia con biopsia INMEDIATA}}; si confirma -> {{c2::cono cervical (LEEP/LLETZ)}}",
    '<span class="ecoe">ECOE: "HSIL, manejo escisional."</span>',
    C3 + ["pap"])

add_cloze(deck_c3,
    "PAP con celulas malignas o sospecha de invasion -> {{c1::referencia urgente a oncologia ginecologica}}",
    '<span class="ecoe">ECOE: "Reporte sugiere invasion; referencia inmediata."</span>',
    C3 + ["pap"])

add_cloze(deck_c3,
    "Co-test PAP + VPH ambos negativos en mujer >=30 anos -> repetir en {{c1::5 anos}}",
    '<span class="ecoe">ECOE: "Co-test negativo, alargo intervalo de tamizaje."</span>',
    C3 + ["vph"])

add_cloze(deck_c3,
    "VPH 16 o 18 positivo (alto riesgo) -> {{c1::colposcopia}} aunque PAP sea normal",
    '<span class="ecoe">ECOE: "VPH 16/18 positivo, colposcopia directa."</span>',
    C3 + ["vph"])

add_cloze(deck_c3,
    "Sifilis: VDRL/RPR positivo -> confirmar con prueba treponemica especifica: {{c1::FTA-ABS}} o {{c2::TP-PA}}",
    '<span class="ecoe">ECOE: "VDRL reactivo, confirmo con prueba treponemica."</span>',
    C3 + ["sifilis"])

add_cloze(deck_c3,
    "Sifilis primaria diagnostico precoz: {{c1::microscopia de campo oscuro de la lesion}} (serologia puede ser negativa al inicio)",
    '<span class="ecoe">ECOE: "Campo oscuro de chancro para diagnostico inmediato."</span>',
    C3 + ["sifilis"])

add_cloze(deck_c3,
    "Herpes genital: dx {{c1::clinico}}; confirmacion en duda con {{c2::PCR de la lesion}} o cultivo viral",
    '<span class="ecoe">ECOE: "Cuadro clinico compatible con herpes, PCR si duda."</span>',
    C3 + ["herpes"])

add_cloze(deck_c3,
    "VIH en embarazo: tamizaje en {{c1::primera consulta prenatal}} y nuevamente en el {{c2::3er trimestre}} si factores de riesgo",
    '<span class="ecoe">ECOE: "Solicito tamizaje VIH como rutina prenatal."</span>',
    C3 + ["vih"])

add_cloze(deck_c3,
    "Zona discriminatoria de beta-hCG: con USG transvaginal debe verse saco intrauterino a partir de {{c1::1500-2000 mUI/mL}}",
    '<span class="ecoe">ECOE: "Beta arriba de zona discriminatoria sin saco IU = sospecha ectopico."</span>',
    C3 + ["hcg"])

add_cloze(deck_c3,
    "Beta-hCG que no duplica en {{c1::48 horas}} sugiere {{c2::embarazo ectopico o no viable}}",
    '<span class="ecoe">ECOE: "Beta sin duplicar adecuada, estudio dirigido."</span>',
    C3 + ["hcg"])

add_cloze(deck_c3,
    "Beta-hCG >100,000 + altura uterina mayor + USG en {{c1::panal de abeja / tormenta de nieve}} -> {{c2::mola hidatiforme}}",
    '<span class="ecoe">ECOE: "Imagen compatible con mola, AMEU + seguimiento."</span>',
    C3 + ["mola"])

add_cloze(deck_c3,
    "Endometrio postmenopausico engrosado >=5 mm + sangrado -> {{c1::biopsia endometrial (Pipelle de Cornier)}}",
    '<span class="ecoe">ECOE: "Endometrio >5 mm con sangrado, biopsia."</span>',
    C3 + ["endometrio"])

add_cloze(deck_c3,
    "Masa anexial sospechosa: tamano >{{c1::10 cm}}, tabicada, componente solido, ascitis, papilas, vascularizada -> alta sospecha de {{c2::Ca de ovario}} -> referencia",
    '<span class="ecoe">ECOE: "Masa anexial compleja, refiero a oncologia."</span>',
    C3 + ["ovario"])

add_cloze(deck_c3,
    "Folliculo dominante listo para ovulacion mide {{c1::18-24 mm}}",
    '<span class="ecoe">ECOE: "Folliculo maduro, induccion de ovulacion exitosa."</span>',
    C3 + ["fertilidad"])

add_cloze(deck_c3,
    "USG de 1er trimestre confirma viabilidad con: {{c1::saco gestacional intrauterino}} + {{c2::vesicula vitelina}} + {{c3::embrion con FCF}}",
    '<span class="ecoe">ECOE: "Embarazo viable intrauterino confirmado."</span>',
    C3 + ["usg"])

add_cloze(deck_c3,
    "Translucencia nucal aumentada (>{{c1::3 mm}}) en semanas {{c2::11-14}} -> marcador de aneuploidia (trisomia 21 principalmente)",
    '<span class="ecoe">ECOE: "TN elevada, ofrezco estudios diagnosticos."</span>',
    C3 + ["usg"])

add_cloze(deck_c3,
    "USG estructural/morfologico: se realiza entre semanas {{c1::18-22}}",
    '<span class="ecoe">ECOE: "Programo USG morfologico en semana 20."</span>',
    C3 + ["usg"])

add_cloze(deck_c3,
    "Liquido amniotico: oligohidramnios si ILA &lt;{{c1::5 cm}}; polihidramnios si ILA &gt;{{c2::24 cm}}",
    '<span class="ecoe">ECOE: "ILA fuera de rango, estudio etiologico."</span>',
    C3 + ["usg"])

add_cloze(deck_c3,
    "Estudio inicial de mama segun edad: &lt;{{c1::40 anos}} -> {{c2::USG mamario}}; &gt;={{c1::40-50 anos}} -> {{c3::mastografia}}",
    '<span class="ecoe">ECOE: "Por su edad solicito mastografia (o USG si joven)."</span>',
    C3 + ["mama"])

add_cloze(deck_c3,
    "BI-RADS 1-2 -> {{c1::benigno, control rutinario}}",
    '<span class="ecoe">ECOE: "Estudio sin sospecha, control habitual."</span>',
    C3 + ["mama"])

add_cloze(deck_c3,
    "BI-RADS 3 -> {{c1::probablemente benigno}}, control en {{c2::6 meses}}",
    '<span class="ecoe">ECOE: "BI-RADS 3, control corto en 6 meses."</span>',
    C3 + ["mama"])

add_cloze(deck_c3,
    "BI-RADS 4 -> {{c1::sospechoso}}; BI-RADS 5 -> {{c2::altamente sugestivo de malignidad}}; ambos requieren {{c3::biopsia}}",
    '<span class="ecoe">ECOE: "BI-RADS 4 o 5, biopsia con aguja gruesa."</span>',
    C3 + ["mama"])

add_cloze(deck_c3,
    "BI-RADS 6 -> {{c1::malignidad ya confirmada por biopsia}}",
    '<span class="ecoe">ECOE: "Diagnostico establecido, manejo oncologico."</span>',
    C3 + ["mama"])

add_cloze(deck_c3,
    "SOP - criterios de Rotterdam (2 de 3): {{c1::oligo/anovulacion}}, {{c2::hiperandrogenismo clinico o bioquimico}}, {{c3::ovarios poliquisticos en USG}}",
    '<span class="ecoe">ECOE: "Cumple Rotterdam para SOP."</span>',
    C3 + ["sop"])

add_cloze(deck_c3,
    "Endometrioma tipico en USG: imagen {{c1::quistica homogenea con ecos finos en vidrio esmerilado}}",
    '<span class="ecoe">ECOE: "Endometrioma sugestivo, referir a especialista."</span>',
    C3 + ["endometriosis"])

add_cloze(deck_c3,
    "Proteinuria significativa en preeclampsia: >={{c1::300 mg/24 h}} o cociente proteina/creatinina >={{c2::0.3}}",
    '<span class="ecoe">ECOE: "Confirmo proteinuria significativa."</span>',
    C3 + ["preeclampsia"])

add_cloze(deck_c3,
    "Datos de severidad de preeclampsia: TA &gt;={{c1::160/110}}, {{c2::plaquetas &lt;100,000}}, {{c3::creatinina &gt;1.1}}, {{c4::AST/ALT &gt;=2x basal}}, {{c5::sintomas neurologicos/visuales}}, {{c6::edema pulmonar}}",
    '<span class="ecoe">ECOE: "Cumple criterios de severidad, manejo intensivo."</span>',
    C3 + ["preeclampsia"])

add_cloze(deck_c3,
    "HELLP: {{c1::Hemolisis (LDH alta, esquistocitos en frotis)}} + {{c2::Elevacion de enzimas hepaticas (AST/ALT)}} + {{c3::Plaquetas Low (&lt;100,000)}}",
    '<span class="ecoe">ECOE: "HELLP, interrupcion sin demora."</span>',
    C3 + ["hellp"])

add_cloze(deck_c3,
    "Tamiz para diabetes gestacional: glucosa {{c1::1 hora postcarga de 50 g}} en semana {{c2::24-28}}; si >140 mg/dL -> {{c3::CTOG diagnostica}}",
    '<span class="ecoe">ECOE: "Solicito tamiz de OSullivan en 24-28 sem."</span>',
    C3 + ["dmg"])

add_cloze(deck_c3,
    "Dx DMG con CTOG 75 g (criterios IADPSG, basta 1 valor): ayuno >={{c1::92}}, 1h >={{c2::180}}, 2h >={{c3::153}}",
    '<span class="ecoe">ECOE: "Cumple criterios para DMG."</span>',
    C3 + ["dmg"])

add_cloze(deck_c3,
    "Metas de glucosa en DMG: ayuno <{{c1::95}}, 1h postprandial <{{c2::140}}, 2h postprandial <{{c3::120}}",
    '<span class="ecoe">ECOE: "Ajusto plan medico-nutricional o insulina."</span>',
    C3 + ["dmg"])

add_cloze(deck_c3,
    "Tamiz para Estreptococo del grupo B (EGB): cultivo {{c1::vagino-rectal}} entre semanas {{c2::35-37}}; si positivo -> profilaxis intraparto",
    '<span class="ecoe">ECOE: "Cultivo EGB en semana 36."</span>',
    C3 + ["egb"])

add_cloze(deck_c3,
    "Madre Rh{{c1::negativo}} con padre Rh{{c2::positivo}}: profilaxis con {{c3::inmunoglobulina anti-D 300 mcg}} en semana {{c4::28}} y postparto si RN Rh+",
    '<span class="ecoe">ECOE: "Programo anti-D en semana 28."</span>',
    C3 + ["rh"])

add_cloze(deck_c3,
    "Coombs indirecto positivo en embarazada Rh negativa: indica {{c1::isoinmunizacion}}; vigilancia con {{c2::Doppler de arteria cerebral media}} para detectar anemia fetal",
    '<span class="ecoe">ECOE: "Isoinmunizacion, refiero a medicina materno-fetal."</span>',
    C3 + ["rh"])

add_cloze(deck_c3,
    "RCTG categoria I (tranquilizador): FCF basal {{c1::110-160}}, variabilidad {{c2::moderada (6-25 lpm)}}, {{c3::aceleraciones}} presentes, {{c4::sin desaceleraciones tardias o variables significativas}}",
    '<span class="ecoe">ECOE: "RCTG categoria I, bienestar fetal."</span>',
    C3 + ["rctg"])

add_cloze(deck_c3,
    "Desaceleraciones {{c1::tardias}} repetidas o variables severas (categoria III) -> sugieren {{c2::insuficiencia utero-placentaria / hipoxia fetal}}; requiere intervencion",
    '<span class="ecoe">ECOE: "Categoria III, reanimacion intrauterina y considerar interrupcion."</span>',
    C3 + ["rctg"])

add_cloze(deck_c3,
    "Bishop &lt;=6 + indicacion de induccion -> usar {{c1::madurador cervical}} (misoprostol intravaginal o sonda Foley) ANTES de oxitocina",
    '<span class="ecoe">ECOE: "Cervix desfavorable, inicio maduracion."</span>',
    C3 + ["bishop"])

add_cloze(deck_c3,
    "Cultivo de orina en embarazo: bacteriuria asintomatica significativa con {{c1::&gt;=10^5 UFC/mL}}; SI tratar (evitar pielonefritis y parto pretermino)",
    '<span class="ecoe">ECOE: "Bacteriuria asintomatica, trato 7 dias."</span>',
    C3 + ["ivu"])

# ============================================================
# CAPA 4 - MANEJO (45 Q&A)
# ============================================================
C4 = ["capa4", "manejo"]

add_qa(deck_c4,
    "Manejo: <b>Herpes genital primario</b>",
    "<b>Aciclovir 400 mg VO c/8 h por 7-10 dias</b> (o valaciclovir 1 g c/12 h, o famciclovir 250 mg c/8 h).<br>"
    "Analgesia + lidocaina topica + educacion sobre transmision (incluso asintomatica) y uso de condon."
    '<span class="ecoe">ECOE: "Tratamiento antiviral 7-10 dias y consejeria."</span>',
    C4 + ["its", "herpes"])

add_qa(deck_c4,
    "Manejo: <b>Herpes genital recurrente</b>",
    "<b>Aciclovir 800 mg VO c/12 h por 5 dias</b> (o valaciclovir 500 mg c/12 h por 3 dias).<br>"
    "Si >=6 recurrencias/ano: terapia supresora diaria con aciclovir 400 mg c/12 h."
    '<span class="ecoe">ECOE: "Episodio recurrente, tratamiento corto + supresion si frecuente."</span>',
    C4 + ["its", "herpes"])

add_qa(deck_c4,
    "Manejo: <b>Sifilis primaria, secundaria o latente temprana</b>",
    "<b>Penicilina G benzatinica 2.4 millones UI IM dosis unica</b>.<br>"
    "Alergia: doxiciclina 100 mg VO c/12 h por 14 dias.<br>"
    "Embarazada alergica -> <b>desensibilizar</b> y dar penicilina (no hay alternativa equivalente)."
    '<span class="ecoe">ECOE: "Penicilina benzatinica dosis unica + control serologico."</span>',
    C4 + ["its", "sifilis"])

add_qa(deck_c4,
    "Manejo: <b>Sifilis latente tardia o de duracion desconocida</b>",
    "<b>Penicilina G benzatinica 2.4 millones UI IM SEMANAL por 3 dosis</b> (total 7.2 millones UI)."
    '<span class="ecoe">ECOE: "3 dosis semanales de penicilina + seguimiento serologico."</span>',
    C4 + ["its", "sifilis"])

add_qa(deck_c4,
    "Manejo: <b>EIP ambulatoria (leve-moderada)</b>",
    "<b>Ceftriaxona 500 mg IM dosis unica</b> + <b>doxiciclina 100 mg VO c/12 h por 14 dias</b> + <b>metronidazol 500 mg VO c/12 h por 14 dias</b>.<br>"
    "Hospitalizar si: embarazo, fiebre alta, intolerancia oral, absceso tubo-ovarico, no mejora en 72 h."
    '<span class="ecoe">ECOE: "Triple esquema 14 dias, retiro DIU solo si no mejora."</span>',
    C4 + ["its", "eip"])

add_qa(deck_c4,
    "Manejo: <b>Tricomoniasis</b>",
    "<b>Metronidazol 2 g VO dosis unica</b> o 500 mg c/12 h por 7 dias.<br>"
    "<b>Tratar a la pareja</b> y abstinencia 7 dias."
    '<span class="ecoe">ECOE: "Tratamiento + pareja + abstinencia 7 dias."</span>',
    C4 + ["its", "tricomoniasis"])

add_qa(deck_c4,
    "Manejo: <b>Candidiasis vulvovaginal no complicada</b>",
    "<b>Fluconazol 150 mg VO dosis unica</b> o clotrimazol vaginal 100 mg/dia por 7 dias.<br>"
    "Embarazo: SOLO topico (clotrimazol/miconazol)."
    '<span class="ecoe">ECOE: "Antimicotico oral o vaginal segun caso."</span>',
    C4 + ["candidiasis"])

add_qa(deck_c4,
    "Manejo: <b>Vaginosis bacteriana</b>",
    "<b>Metronidazol 500 mg VO c/12 h por 7 dias</b> o gel vaginal 0.75% por 5 dias o clindamicina crema 2% por 7 dias.<br>"
    "<b>NO requiere tratar pareja</b>."
    '<span class="ecoe">ECOE: "Metronidazol 7 dias, sin tratar pareja."</span>',
    C4 + ["vaginosis"])

add_qa(deck_c4,
    "Manejo: <b>NIC 1 confirmado por biopsia</b>",
    "<b>Vigilancia</b> con citologia/colposcopia cada 6-12 meses (regresion espontanea frecuente, hasta 60 por ciento).<br>"
    "Tratar solo si persiste >2 anos o progresa."
    '<span class="ecoe">ECOE: "NIC 1, vigilancia activa por probable regresion."</span>',
    C4 + ["nic"])

add_qa(deck_c4,
    "Manejo: <b>NIC 2-3 confirmado</b>",
    "<b>Tratamiento escisional</b>: cono LEEP/LLETZ (de eleccion) o conizacion con bisturi frio.<br>"
    "Alternativa ablativa solo si lesion totalmente visible: criocirugia o laser."
    '<span class="ecoe">ECOE: "NIC 2-3, manejo escisional con LEEP."</span>',
    C4 + ["nic"])

add_qa(deck_c4,
    "Manejo: <b>Ca cervix invasor</b>",
    "<b>Referencia a oncologia ginecologica</b> para estadificacion FIGO + tratamiento (cirugia tipo Wertheim, RT-QT concomitante o ambos segun etapa)."
    '<span class="ecoe">ECOE: "Refiero a oncologia ginecologica."</span>',
    C4 + ["cancer_cervix"])

add_qa(deck_c4,
    "Manejo: <b>Mastitis puerperal</b>",
    "<b>Dicloxacilina 500 mg VO c/6 h por 10-14 dias</b> (o cefalexina); analgesia + compresas tibias + <b>VACIAMIENTO MAMARIO CONTINUO</b>; "
    "<b>NO suspender lactancia</b> (es protectora)."
    '<span class="ecoe">ECOE: "Antibiotico + vaciamiento + mantener lactancia."</span>',
    C4 + ["mama", "mastitis"])

add_qa(deck_c4,
    "Manejo: <b>Absceso mamario</b>",
    "<b>Drenaje</b>: aspiracion con aguja guiada por USG (1ra eleccion en abscesos pequenos) o drenaje quirurgico si grande/multilocular.<br>"
    "Antibiotico (dicloxacilina) + analgesia + continuar lactancia."
    '<span class="ecoe">ECOE: "Drenaje + antibiotico, mantener lactancia."</span>',
    C4 + ["mama", "absceso"])

add_qa(deck_c4,
    "Manejo: <b>BI-RADS 4 o 5</b>",
    "<b>Biopsia con aguja gruesa (core)</b> guiada por imagen -> histologia -> si maligno, referencia oncologica para etapa clinica/imagen + tratamiento multimodal."
    '<span class="ecoe">ECOE: "Biopsia core, no FNAC como unico estudio."</span>',
    C4 + ["mama", "birads"])

add_qa(deck_c4,
    "Manejo: <b>Fibroadenoma &lt;2-3 cm en mujer joven</b>",
    "<b>Observacion</b> con USG de control en 6 meses.<br>"
    "Escision si: crece mas del 20 por ciento en 6 meses, mas de 3 cm, sintomatico, dx incierto, preferencia de paciente."
    '<span class="ecoe">ECOE: "Fibroadenoma, vigilancia con USG."</span>',
    C4 + ["mama", "fibroadenoma"])

add_qa(deck_c4,
    "Manejo: <b>SOP con deseo de embarazo</b>",
    "1) <b>Perdida de peso</b> 5-10% (1ra linea no farmacologica).<br>"
    "2) <b>Letrozol 2.5-5 mg/dia por 5 dias</b> (1ra linea farmacologica para ovulacion).<br>"
    "3) Metformina si resistencia a insulina.<br>"
    "4) Gonadotropinas o reproduccion asistida si falla."
    '<span class="ecoe">ECOE: "Letrozol como inductor, NO citrato (ya no es 1ra linea)."</span>',
    C4 + ["sop"])

add_qa(deck_c4,
    "Manejo: <b>SOP sin deseo de embarazo</b>",
    "<b>ACO combinados</b> (regulan ciclo + manejan hiperandrogenismo) + estilo de vida + <b>metformina</b> si resistencia/intolerancia.<br>"
    "Espironolactona para hirsutismo refractario (con ACO, no en monoterapia sin anticoncepcion)."
    '<span class="ecoe">ECOE: "ACO + estilo de vida, espironolactona si hirsutismo."</span>',
    C4 + ["sop"])

add_qa(deck_c4,
    "Manejo: <b>Endometriosis sintomatica</b>",
    "1) AINEs + <b>ACO continuos</b> o progestinas (1ra linea).<br>"
    "2) Analogos de GnRH (con add-back) si refractario.<br>"
    "3) <b>Laparoscopia</b> con reseccion si falla manejo medico o infertilidad."
    '<span class="ecoe">ECOE: "AINE + ACO continuo, laparoscopia si refractario."</span>',
    C4 + ["endometriosis"])

add_qa(deck_c4,
    "Manejo: <b>Miomatosis uterina sintomatica</b>",
    "Sangrado: ACO/DIU-LNG, acido tranexamico, AINEs.<br>"
    "Sintomas masa/dolor: anti-GnRH preoperatorio.<br>"
    "<b>Quirurgico</b>: miomectomia si desea fertilidad, histerectomia si paridad satisfecha o sintomas severos."
    '<span class="ecoe">ECOE: "Manejo segun deseo reproductivo."</span>',
    C4 + ["miomatosis"])

add_qa(deck_c4,
    "Manejo: <b>Climaterio sintomatico</b>",
    "<b>Terapia hormonal sustitutiva</b> si <60 anos o <10 anos desde menopausia, sin contraindicaciones.<br>"
    "Estrogeno solo si histerectomia; estrogeno + progestina si tiene utero.<br>"
    "<b>Contraindicaciones</b>: Ca mama, ETV, EVC, IAM, sangrado uterino sin diagnostico, hepatopatia grave."
    '<span class="ecoe">ECOE: "TRH si <60 anos y sin contraindicaciones."</span>',
    C4 + ["climaterio"])

add_qa(deck_c4,
    "Manejo: <b>Absceso de Bartholino</b>",
    "<b>Drenaje</b>: marsupializacion o <b>cateter de Word</b> (deja drenaje 4-6 semanas para epitelizar).<br>"
    "Antibiotico solo si celulitis perilesional, inmunocompromiso o sospecha de ITS (cefalexina + cobertura ITS)."
    '<span class="ecoe">ECOE: "Cateter de Word + antibiotico si celulitis."</span>',
    C4 + ["bartholino"])

add_qa(deck_c4,
    "Manejo: <b>Anticoncepcion de emergencia</b>",
    "1) <b>Levonorgestrel 1.5 mg VO dosis unica</b> dentro de 72-120 h (mas eficaz &lt;72 h).<br>"
    "2) Ulipristal 30 mg VO hasta 120 h.<br>"
    "3) <b>DIU de cobre</b> hasta 5 dias (el mas eficaz, especialmente en obesidad)."
    '<span class="ecoe">ECOE: "Levonorgestrel &lt;72h; DIU Cu como opcion mas eficaz."</span>',
    C4 + ["anticoncepcion"])

add_qa(deck_c4,
    "Manejo: <b>Contraindicaciones absolutas de ACO combinados</b>",
    "Categoria 4 OMS: <b>&gt;=35 anos + tabaquismo &gt;=15 cig/dia</b>, antecedente de <b>TVP/TEP</b>, <b>migrana con aura</b>, "
    "<b>Ca de mama actual</b>, HAS no controlada (&gt;=160/100), LES con SAF, hepatopatia grave, &lt;6 sem postparto en lactancia."
    '<span class="ecoe">ECOE: "Chequeo de criterios OMS antes de prescribir."</span>',
    C4 + ["anticoncepcion"])

add_qa(deck_c4,
    "Manejo: <b>DIU de cobre</b>",
    "<b>Duracion 10 anos</b>, no hormonal, eficacia &gt;99%.<br>"
    "Aumenta sangrado y dismenorrea.<br>"
    "Contraindicado: embarazo, EIP activa, sangrado inexplicado, Ca cervical/endometrial, anomalias uterinas severas."
    '<span class="ecoe">ECOE: "DIU Cu eficaz, advierto aumento de sangrado y dolor."</span>',
    C4 + ["anticoncepcion"])

add_qa(deck_c4,
    "Manejo: <b>Embarazo ectopico estable</b> (sin ruptura)",
    "<b>Metotrexato IM</b> dosis unica (50 mg/m2) si: hemodinamicamente estable, <b>beta-hCG &lt;5000</b>, sin LCF, masa &lt;3.5 cm, paciente confiable para seguimiento.<br>"
    "Seguimiento de beta-hCG dias 4 y 7 (debe bajar 15 por ciento)."
    '<span class="ecoe">ECOE: "Criterios para MTX; seguimiento estrecho."</span>',
    C4 + ["ectopico"])

add_qa(deck_c4,
    "Manejo: <b>Embarazo ectopico roto o inestable</b>",
    "<b>Cirugia urgente</b>: laparoscopia/laparotomia con salpingectomia (preferida si trompa muy danada) o salpingostomia (preserva trompa).<br>"
    "Reanimacion con cristaloides + hemoderivados."
    '<span class="ecoe">ECOE: "Ectopico inestable, cirugia urgente."</span>',
    C4 + ["ectopico"])

add_qa(deck_c4,
    "Manejo: <b>Amenaza de aborto</b>",
    "<b>Reposo relativo</b>, abstinencia sexual, evitar esfuerzos.<br>"
    "<b>Progesterona</b> si insuficiencia lutea documentada o aborto recurrente.<br>"
    "USG de control en 1-2 semanas. Datos de alarma."
    '<span class="ecoe">ECOE: "Reposo + datos de alarma, USG control."</span>',
    C4 + ["aborto"])

add_qa(deck_c4,
    "Manejo: <b>Aborto incompleto</b>",
    "<b>AMEU (aspiracion manual endouterina)</b> si estable o LUI segun semanas, o <b>misoprostol</b> 600-800 mcg vaginal si paciente estable y prefiere medico.<br>"
    "Hospitalizar si sepsis, sangrado abundante o inestabilidad."
    '<span class="ecoe">ECOE: "AMEU es de eleccion; misoprostol como opcion medica."</span>',
    C4 + ["aborto"])

add_qa(deck_c4,
    "Manejo: <b>Placenta previa con sangrado activo</b>",
    "<b>Hospitalizar, NO TACTO VAGINAL</b>, USG transabdominal/transvaginal cuidadoso.<br>"
    "Estabilizacion + via aerea + 2 vias IV + hemoderivados disponibles.<br>"
    "&lt;34 sem: maduracion pulmonar (betametasona) y manejo expectante si sangrado controlado.<br>"
    "&gt;=37 sem: <b>cesarea programada</b>. Cesarea urgente si sangrado severo."
    '<span class="ecoe">ECOE: "NO tacto, USG, estabilizar, cesarea segun semanas."</span>',
    C4 + ["placenta_previa"])

add_qa(deck_c4,
    "Manejo: <b>DPPNI</b>",
    "<b>ABC materno + reanimacion</b> (cristaloides + hemoderivados).<br>"
    "<b>Interrupcion urgente</b> (cesarea casi siempre); parto vaginal solo si dilatacion avanzada, feto muerto y estabilidad materna.<br>"
    "Vigilar CID y hemorragia postparto."
    '<span class="ecoe">ECOE: "Cesarea urgente, vigilar coagulopatia."</span>',
    C4 + ["dppni"])

add_qa(deck_c4,
    "Manejo: <b>Preeclampsia sin datos de severidad &lt;37 sem</b>",
    "<b>Vigilancia hospitalaria o ambulatoria estrecha</b>: TA, proteinuria, biometria fetal, doppler, RCTG.<br>"
    "Antihipertensivo si TA persistente &gt;=140/90.<br>"
    "<b>Interrupcion electiva a las 37 sem</b> (no antes si estable)."
    '<span class="ecoe">ECOE: "Interrupcion a las 37 sem, hasta entonces vigilancia."</span>',
    C4 + ["preeclampsia"])

add_qa(deck_c4,
    "Manejo: <b>Preeclampsia con datos de severidad</b>",
    "1) <b>Hospitalizar</b> + monitoreo materno-fetal.<br>"
    "2) <b>Sulfato de Mg</b> para neuroproteccion (4-6 g IV bolo + 1-2 g/h por 24 h post-parto).<br>"
    "3) <b>Antihipertensivo</b>: labetalol, hidralazina o nifedipino.<br>"
    "4) <b>Interrupcion</b>: &gt;=34 sem inmediata; &lt;34 sem maduracion pulmonar y evaluar segun estabilidad."
    '<span class="ecoe">ECOE: "Sulfato Mg + antiHTA + interrupcion segun semanas."</span>',
    C4 + ["preeclampsia"])

add_qa(deck_c4,
    "Manejo: <b>Eclampsia</b>",
    "1) ABC + posicion lateral izquierda + oxigeno + proteccion via aerea.<br>"
    "2) <b>Sulfato de Mg</b>: 4-6 g IV bolo en 20 min, luego 2 g/h.<br>"
    "3) Si convulsion persiste: bolo adicional 2 g; si refractario, midazolam o diazepam.<br>"
    "4) <b>Interrupcion del embarazo</b> una vez estable."
    '<span class="ecoe">ECOE: "ABC + sulfato Mg + interrupcion una vez estable."</span>',
    C4 + ["eclampsia"])

add_qa(deck_c4,
    "Manejo: <b>Dosis y monitoreo de Sulfato de Magnesio</b>",
    "<b>Carga 4-6 g IV en 20 min</b> -> <b>mantenimiento 1-2 g/h IV</b> por 24 h post-parto.<br>"
    "<b>Vigilar</b>: reflejo patelar (si abolido suspender), FR &gt;=12, diuresis &gt;=30 mL/h, niveles si renal."
    '<span class="ecoe">ECOE: "Vigilo reflejo patelar, FR y diuresis."</span>',
    C4 + ["sulfato_mg"])

add_qa(deck_c4,
    "Manejo: <b>Intoxicacion por Sulfato de Magnesio</b>",
    "<b>Suspender infusion</b> + <b>gluconato de calcio 1 g IV (10 mL al 10%) en 10 min</b>.<br>"
    "Soporte ventilatorio si depresion respiratoria."
    '<span class="ecoe">ECOE: "Antidoto: gluconato de calcio IV."</span>',
    C4 + ["sulfato_mg"])

add_qa(deck_c4,
    "Manejo: <b>Antihipertensivos seguros y prohibidos en embarazo</b>",
    "<b>Seguros</b>: alfa-metildopa (cronico), labetalol, hidralazina, nifedipino.<br>"
    "<b>EVITAR</b>: <b>IECA</b>, <b>ARA-II</b>, inhibidores de renina, atenolol, diureticos de inicio en preeclampsia.<br>"
    "Meta de TA: 130-150 / 80-100 (no bajar mucho para no comprometer perfusion utero-placentaria).&nbsp;"
    '<span class="ecoe">ECOE: "Nunca IECA/ARA-II en embarazo."</span>',
    C4 + ["hta_embarazo"])

add_qa(deck_c4,
    "Manejo: <b>Trabajo de parto pretermino (24-34 sem)</b>",
    "1) <b>Tocolisis</b> 48 h: nifedipino o atosiban (1ra eleccion segun guia).<br>"
    "2) <b>Maduracion pulmonar</b>: betametasona 12 mg IM c/24 h x 2 dosis (o dexametasona 6 mg IM c/12 h x 4).<br>"
    "3) <b>Neuroproteccion fetal</b> con sulfato de Mg si &lt;32 sem.<br>"
    "4) Antibiotico EGB segun cultivo."
    '<span class="ecoe">ECOE: "Tocolisis + corticoide + Mg <32 sem."</span>',
    C4 + ["pretermino"])

add_qa(deck_c4,
    "Manejo: <b>RPM a termino (>=37 sem)</b>",
    "<b>Induccion de trabajo de parto</b> si no inicia espontaneamente en 24 h (algunos recomiendan inmediato).<br>"
    "Profilaxis EGB segun cultivo o factores de riesgo."
    '<span class="ecoe">ECOE: "Inducir, no esperar mas de 24 h."</span>',
    C4 + ["rpm"])

add_qa(deck_c4,
    "Manejo: <b>RPM pretermino (&lt;34 sem)</b>",
    "<b>Manejo expectante hospitalizado</b>: <b>antibiotico</b> (ampicilina + azitromicina o eritromicina 7 dias) + <b>maduracion pulmonar</b> + vigilancia de corioamnionitis.<br>"
    "Interrumpir si: corioamnionitis, sufrimiento fetal, &gt;=34 sem alcanzado."
    '<span class="ecoe">ECOE: "Antibiotico + corticoide + expectante hasta 34 sem si estable."</span>',
    C4 + ["rpm"])

add_qa(deck_c4,
    "Manejo: <b>Corioamnionitis</b>",
    "<b>Antibiotico IV de amplio espectro</b>: ampicilina + gentamicina (anadir clindamicina o metronidazol si cesarea).<br>"
    "<b>Interrupcion del embarazo independiente de la edad gestacional</b>."
    '<span class="ecoe">ECOE: "Antibiotico + interrupcion ya, sea cual sea la edad."</span>',
    C4 + ["corioamnionitis"])

add_qa(deck_c4,
    "Manejo: <b>Distocia de hombros</b>",
    "Nemotecnia <b>HELPERR</b>:<br>"
    "H - llamar ayuda; E - episiotomia (evaluar); L - <b>maniobra de McRoberts</b> (flexion muslos); P - <b>presion suprapubica</b> (no fundica); "
    "E - maniobras internas (Rubin, Woods, Jacquemier/extraccion brazo posterior); R - rotacion; R - posicion en cuatro puntos (Gaskin)."
    '<span class="ecoe">ECOE: "McRoberts + presion suprapubica como primera linea."</span>',
    C4 + ["distocia"])

add_qa(deck_c4,
    "Manejo: <b>Hemorragia postparto por atonia uterina</b>",
    "1) <b>Masaje uterino bimanual</b>.<br>"
    "2) <b>Oxitocina 20-40 UI en 1000 mL IV</b> (no en bolo).<br>"
    "3) <b>Carbetocina</b> 100 mcg IV (eleccion postcesarea), <b>ergonovina</b> 0.2 mg IM (NO si HTA), <b>misoprostol</b> 600-1000 mcg rectal/sublingual.<br>"
    "4) Si falla: balon de Bakri, suturas de B-Lynch, ligadura de arterias uterinas/hipogastricas, <b>histerectomia obstetrica</b>."
    '<span class="ecoe">ECOE: "Masaje + uterotonicos escalonados, balon de Bakri si refractario."</span>',
    C4 + ["hpp"])

add_qa(deck_c4,
    "Manejo: <b>Las 4 T de la hemorragia postparto</b>",
    "<b>T1 Tono</b> (atonia uterina - 70%): uterotonicos.<br>"
    "<b>T2 Trauma</b> (laceraciones/desgarros, ruptura uterina): reparacion quirurgica.<br>"
    "<b>T3 Tejido</b> (restos placentarios, acretismo): revision/AMEU/legrado.<br>"
    "<b>T4 Trombina</b> (coagulopatia, CID): hemoderivados + correccion."
    '<span class="ecoe">ECOE: "Penso las 4 T para descartar etiologias."</span>',
    C4 + ["hpp"])

add_qa(deck_c4,
    "Manejo: <b>Endometritis puerperal</b>",
    "<b>Clindamicina 900 mg IV c/8 h + Gentamicina 1.5 mg/kg IV c/8 h</b> (o esquema cada 24 h) hasta 48 h afebril; no requiere VO posterior salvo bacteriemia."
    '<span class="ecoe">ECOE: "Clinda + genta IV hasta 48 h afebril."</span>',
    C4 + ["endometritis"])

add_qa(deck_c4,
    "Manejo: <b>Depresion postparto</b>",
    "Tamizar con <b>Escala de Edimburgo</b> a las 2-6 sem postparto y en visitas pediatricas.<br>"
    "Tratamiento: psicoterapia + <b>ISRS (sertralina de eleccion, compatible con lactancia)</b>.<br>"
    "Hospitalizacion si ideacion suicida/infanticida o psicosis postparto."
    '<span class="ecoe">ECOE: "Sertralina + psicoterapia; tamizo con Edimburgo."</span>',
    C4 + ["postparto", "salud_mental"])

add_qa(deck_c4,
    "Manejo: <b>Profilaxis intraparto para Estreptococo grupo B (EGB)</b>",
    "<b>Penicilina G 5 millones UI IV dosis inicial, luego 2.5-3 millones UI IV c/4 h hasta el parto</b>.<br>"
    "Alternativa: ampicilina; alergica: cefazolina o clindamicina/vancomicina segun sensibilidad."
    '<span class="ecoe">ECOE: "Penicilina G intraparto cada 4 h."</span>',
    C4 + ["egb"])

# ============================================================
# Build packages
# ============================================================
def build():
    decks = [
        (deck_c1, "Gineco_Obstetricia_Adulto_Capa1.apkg"),
        (deck_c2, "Gineco_Obstetricia_Adulto_Capa2.apkg"),
        (deck_c3, "Gineco_Obstetricia_Adulto_Capa3.apkg"),
        (deck_c4, "Gineco_Obstetricia_Adulto_Capa4.apkg"),
    ]
    for d, fname in decks:
        pkg = genanki.Package(d)
        out = os.path.join(OUTPUT_DIR, fname)
        pkg.write_to_file(out)
        print(f"  -> {fname} ({len(d.notes)} notas)")

    # Combined deck (all 4 subdecks in one .apkg with hierarchy preserved)
    combined = genanki.Package([deck_c1, deck_c2, deck_c3, deck_c4])
    combined_out = os.path.join(OUTPUT_DIR, "Gineco_Obstetricia_Adulto_TODOS.apkg")
    combined.write_to_file(combined_out)
    total = sum(len(d.notes) for d in [deck_c1, deck_c2, deck_c3, deck_c4])
    print(f"  -> Gineco_Obstetricia_Adulto_TODOS.apkg ({total} notas totales)")


if __name__ == "__main__":
    build()
