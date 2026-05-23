"""Generador de 4 subdecks Anki para ECOE de Cirugia.

Capa 1 - Reconocimiento de Patron Quirurgico (Cloze)
Capa 2 - Exploracion y ATLS Verbalizado (Cloze)
Capa 3 - Interpretacion de Estudios (Cloze)
Capa 4 - Manejo y Diagnostico Diferencial (Q&A)

Guias base: ATLS 10a ed (ACS), Tokyo Guidelines 2018/2024,
WSES, ACG 2021/2024, IDSA 2010 + SIS 2017, Surviving Sepsis 2021,
ACOG + ASRM, SVS 2018, SAGES, UpToDate.

Filosofia (estilo Musel): patrones fisiopatologicos antes que enfermedades.
Cirugia = fisiologia bajo amenaza. ANCLA -> CONTRASTE -> VARIACION.
"""
import os
import genanki

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "output")
os.makedirs(OUTPUT_DIR, exist_ok=True)

MODEL_CLOZE_ID = 1607392319
MODEL_QA_ID = 1607392320

DECK_ID_C1 = 1866373995
DECK_ID_C2 = 1481697194
DECK_ID_C3 = 1796015227
DECK_ID_C4 = 1705364983

DECK_NAME_C1 = "Cirugia Adulto::Capa 1 - Reconocimiento de Patron Quirurgico"
DECK_NAME_C2 = "Cirugia Adulto::Capa 2 - Exploracion y ATLS Verbalizado"
DECK_NAME_C3 = "Cirugia Adulto::Capa 3 - Interpretacion de Estudios"
DECK_NAME_C4 = "Cirugia Adulto::Capa 4 - Manejo y Diagnostico Diferencial"

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
.redflag { color: #b91c1c; font-weight: 600; display: block; margin-top: 6px; }
.viva { color: #047857; display: block; margin-top: 6px; font-style: italic; }
b { color: #111; }
"""

model_cloze = genanki.Model(
    MODEL_CLOZE_ID, "Estudio Medico Cloze",
    fields=[{"name": "Text"}, {"name": "Extra"}],
    templates=[{"name": "Cloze", "qfmt": "{{cloze:Text}}",
                "afmt": '{{cloze:Text}}<hr id="extra">{{Extra}}'}],
    css=CSS_BASE, model_type=genanki.Model.CLOZE,
)
model_qa = genanki.Model(
    MODEL_QA_ID, "Estudio Medico QA",
    fields=[{"name": "Front"}, {"name": "Back"}],
    templates=[{"name": "QA", "qfmt": "{{Front}}",
                "afmt": '{{Front}}<hr id="extra">{{Back}}'}],
    css=CSS_BASE,
)

deck_c1 = genanki.Deck(DECK_ID_C1, DECK_NAME_C1)
deck_c2 = genanki.Deck(DECK_ID_C2, DECK_NAME_C2)
deck_c3 = genanki.Deck(DECK_ID_C3, DECK_NAME_C3)
deck_c4 = genanki.Deck(DECK_ID_C4, DECK_NAME_C4)

BASE_TAGS = ["cirugia", "ecoe"]


def add_cloze(deck, text, extra, tags):
    deck.add_note(genanki.Note(model=model_cloze, fields=[text, extra], tags=BASE_TAGS + tags))


def add_qa(deck, front, back, tags):
    deck.add_note(genanki.Note(model=model_qa, fields=[front, back], tags=BASE_TAGS + tags))


# ============================================================
# CAPA 1 - RECONOCIMIENTO DE PATRON QUIRURGICO (40 cloze)
# Pregunta clave: "se muere o no?"
# ============================================================
C1 = ["capa1", "reconocimiento"]

# --- TRAUMA (8)
add_cloze(deck_c1,
    "Objeto penetrante (cuchillo, varilla) clavado en abdomen/torax -> {{c1::NO retirar}}; el objeto actua como {{c2::tapon temporal}} de la lesion vascular",
    '<span class="contraste">Retirarlo en sala = hemorragia exsanguinante. Solo se retira en quirofano con campo abierto.</span>'
    '<span class="ecoe">ECOE: "No retiro el objeto, lo estabilizo, activo codigo trauma y aplico ATLS."</span>',
    C1 + ["trauma", "penetrante"])

add_cloze(deck_c1,
    "Trauma penetrante abdominal + {{c1::inestabilidad hemodinamica}} -> conducta inmediata: {{c2::laparotomia exploradora}} (no TAC)",
    '<span class="contraste">Estable + penetrante = TAC con triple contraste; inestable = quirofano.</span>'
    '<span class="ecoe">ECOE: "Paciente inestable con trauma penetrante = quirofano sin retraso."</span>',
    C1 + ["trauma", "penetrante", "decision"])

add_cloze(deck_c1,
    "Trauma cerrado abdominal + dolor referido al {{c1::hombro izquierdo}} (signo de Kehr) -> sospecha {{c2::lesion esplenica con hemoperitoneo}}",
    '<span class="contraste">Irritacion diafragmatica por sangre = dolor referido C3-C5.</span>'
    '<span class="ecoe">ECOE: "Signo de Kehr sugiere irritacion diafragmatica por sangrado esplenico."</span>',
    C1 + ["trauma", "cerrado", "bazo"])

add_cloze(deck_c1,
    "Disnea subita + {{c1::desviacion traqueal contralateral}} + {{c2::ingurgitacion yugular}} + hipersonoridad + ausencia de murmullo unilateral -> {{c3::neumotorax a tension}}",
    '<span class="redflag">Diagnostico CLINICO, no esperar Rx. Toracostomia inmediata.</span>'
    '<span class="ecoe">ECOE: "Cuadro de neumotorax a tension; descomprimo con aguja en 2do EIC linea medioclavicular."</span>',
    C1 + ["trauma", "torax", "neumotorax"])

add_cloze(deck_c1,
    "Triada de Beck ({{c1::hipotension}} + {{c2::ingurgitacion yugular}} + {{c3::ruidos cardiacos apagados}}) en trauma toracico -> {{c4::tamponade cardiaco}}",
    '<span class="contraste">FAST subxifoideo confirma; toracotomia/pericardiocentesis emergente.</span>'
    '<span class="ecoe">ECOE: "Triada de Beck = tamponade; FAST cardiaco y pericardiocentesis o toracotomia."</span>',
    C1 + ["trauma", "tamponade"])

add_cloze(deck_c1,
    "Salida inicial por sonda pleural >{{c1::1500 mL}} o >{{c2::200 mL/h durante 4 h}} -> {{c3::hemotorax masivo}}, indicacion de toracotomia",
    '<span class="redflag">Hemotorax masivo es indicacion quirurgica formal (ATLS 10a).</span>'
    '<span class="ecoe">ECOE: "Drenaje masivo persistente = paciente a quirofano, no solo manejo con sonda."</span>',
    C1 + ["trauma", "hemotorax"])

add_cloze(deck_c1,
    "Segmento toracico que se {{c1::mueve paradojicamente}} (hacia adentro en inspiracion) tras trauma cerrado -> {{c2::torax inestable (flail chest)}}, asociado a {{c3::contusion pulmonar}}",
    '<span class="contraste">Lo que mata es la contusion pulmonar subyacente, no la fractura.</span>'
    '<span class="ecoe">ECOE: "Torax inestable + contusion pulmonar; analgesia agresiva, considerar ventilacion."</span>',
    C1 + ["trauma", "torax"])

add_cloze(deck_c1,
    "Trauma de alta energia + dolor pelvico + inestabilidad hemodinamica + apertura del anillo pelvico -> {{c1::fractura pelvica inestable con sangrado retroperitoneal}}; aplicar {{c2::faja pelvica}} (binder) en sala",
    '<span class="contraste">Causa frecuente de shock oculto; no se aspira con FAST inicialmente.</span>'
    '<span class="ecoe">ECOE: "Coloco faja pelvica, activo protocolo de transfusion masiva, valoro angioembolizacion."</span>',
    C1 + ["trauma", "pelvis"])

# --- HEMORRAGIA (8)
add_cloze(deck_c1,
    "Mujer en edad fertil + {{c1::amenorrea}} + dolor abdominal bajo subito + {{c2::inestabilidad hemodinamica}} + liquido libre en FAST -> {{c3::embarazo ectopico roto}}",
    '<span class="redflag">Sangrado hasta demostrar lo contrario; quirofano si inestable.</span>'
    '<span class="contraste">Estable + masa anexial + sin liquido libre = ectopico no roto (metotrexato posible).</span>'
    '<span class="ecoe">ECOE: "Mujer fertil inestable con liquido libre = ectopico roto, laparoscopia/laparotomia urgente."</span>',
    C1 + ["hemorragia", "ectopico"])

add_cloze(deck_c1,
    "{{c1::Hematemesis}} (vomito de sangre fresca o en posos de cafe) + {{c2::melena}} + antecedente de AINE/H. pylori -> {{c3::HDA por ulcera peptica}}",
    '<span class="contraste">Mas frecuente: ulcera duodenal. Forrest clasifica riesgo de resangrado.</span>'
    '<span class="ecoe">ECOE: "Sospecho HDA no varicial; IBP IV, estabilizar y endoscopia &lt;24 h."</span>',
    C1 + ["hemorragia", "hda"])

add_cloze(deck_c1,
    "Hematemesis abundante con sangre fresca + {{c1::estigmas de hepatopatia cronica}} (arana, eritema palmar, ascitis) -> {{c2::HDA por varices esofagicas}}",
    '<span class="contraste">Mortalidad alta; manejo distinto a ulcera (octreotido + ligadura, ATB profilactico).</span>'
    '<span class="ecoe">ECOE: "Paciente cirrotico con HDA = varices hasta demostrar lo contrario; octreotido y endoscopia urgente."</span>',
    C1 + ["hemorragia", "hda", "varices"])

add_cloze(deck_c1,
    "{{c1::Hematoquezia}} (sangre roja brillante por recto) en >60 anos con diverticulosis conocida -> {{c2::HDB por diverticulo}}; segunda causa: {{c3::angiodisplasia colonica}}",
    '<span class="contraste">HDA masiva puede simular hematoquezia (transito acelerado) - poner SNG/lavado.</span>'
    '<span class="ecoe">ECOE: "HDB en adulto mayor; descarto HDA con SNG, colonoscopia urgente."</span>',
    C1 + ["hemorragia", "hdb"])

add_cloze(deck_c1,
    "Triada clasica de AAA roto: {{c1::dolor abdominal/lumbar subito}} + {{c2::masa pulsatil}} + {{c3::hipotension}} en >60 a, varon, fumador",
    '<span class="redflag">Mortalidad >80%; quirofano sin retraso (no esperar TAC si inestable).</span>'
    '<span class="ecoe">ECOE: "Sospecho AAA roto; reanimacion hipotensiva permisiva y quirofano YA."</span>',
    C1 + ["hemorragia", "aaa"])

add_cloze(deck_c1,
    "{{c1::Equimosis periumbilical}} (signo de Cullen) o {{c2::equimosis en flancos}} (signo de Grey-Turner) -> {{c3::sangrado retroperitoneal/intraperitoneal}} (pancreatitis hemorragica, ectopico roto, AAA)",
    '<span class="contraste">Signo tardio (24-48 h), no util para deteccion temprana.</span>'
    '<span class="ecoe">ECOE: "Cullen y Grey-Turner sugieren hemoperitoneo o sangrado retroperitoneal."</span>',
    C1 + ["hemorragia", "signos"])

add_cloze(deck_c1,
    "Choque hipovolemico clase III (ATLS): perdida {{c1::30-40%}} (1500-2000 mL); FC {{c2::>120}}; PA {{c3::disminuida}}; estado mental {{c4::confuso}}; requiere {{c5::cristaloides + hemoderivados}}",
    '<span class="contraste">Clase IV (>40%): hipotension severa, anuria, letargia, riesgo de paro.</span>'
    '<span class="ecoe">ECOE: "Clasifico choque clase III por ATLS; activo protocolo de transfusion masiva."</span>',
    C1 + ["choque", "hipovolemico"])

add_cloze(deck_c1,
    "Reanimacion hipotensiva permisiva en hemorragia traumatica: meta {{c1::PAS 80-90}} mmHg (o pulso radial palpable) hasta {{c2::control quirurgico del sangrado}}",
    '<span class="contraste">Excepcion: TCE - se requiere PAS >=110 para perfusion cerebral.</span>'
    '<span class="ecoe">ECOE: "Reanimacion balanceada; no sobrecargar cristaloides, hemoderivados 1:1:1."</span>',
    C1 + ["choque", "reanimacion"])

# --- ABDOMEN AGUDO (10)
add_cloze(deck_c1,
    "Dolor {{c1::periumbilical}} que migra a {{c2::FID}} en 12-24 h + anorexia + febricula + nausea -> {{c3::apendicitis aguda}}",
    '<span class="contraste">Migracion = inflamacion peritoneal local (de visceral a parietal).</span>'
    '<span class="ecoe">ECOE: "Patron clasico de apendicitis; calculo Alvarado y solicito imagen segun edad/sexo."</span>',
    C1 + ["abdomen_agudo", "apendicitis"])

add_cloze(deck_c1,
    "Apendicitis evolucion >48-72 h + {{c1::defensa abdominal generalizada}} + fiebre alta + leucocitosis marcada + taquicardia -> {{c2::apendicitis perforada con peritonitis}}",
    '<span class="redflag">Es abdomen quirurgico; quirofano y ATB IV.</span>'
    '<span class="ecoe">ECOE: "Apendicitis complicada con peritonitis difusa; laparotomia/laparoscopia urgente + ATB."</span>',
    C1 + ["abdomen_agudo", "apendicitis", "perforacion"])

add_cloze(deck_c1,
    "Dolor en {{c1::hipocondrio derecho}} postprandial (alimento graso) + {{c2::Murphy positivo}} + fiebre + leucocitosis -> {{c3::colecistitis aguda}}",
    '<span class="contraste">Colico biliar: SIN fiebre, SIN leucocitosis, dolor &lt;6 h y autolimitado.</span>'
    '<span class="ecoe">ECOE: "Patron de colecistitis; USG y colecistectomia laparoscopica temprana (&lt;72 h)."</span>',
    C1 + ["abdomen_agudo", "colecistitis"])

add_cloze(deck_c1,
    "Triada de Charcot: {{c1::fiebre con escalofrios}} + {{c2::ictericia}} + {{c3::dolor en hipocondrio derecho}} -> {{c4::colangitis aguda}}",
    '<span class="redflag">Sepsis biliar; requiere descompresion biliar urgente.</span>'
    '<span class="ecoe">ECOE: "Triada de Charcot = colangitis; ATB IV y CPRE de descompresion."</span>',
    C1 + ["abdomen_agudo", "colangitis"])

add_cloze(deck_c1,
    "Pentada de Reynolds: triada de Charcot + {{c1::hipotension}} + {{c2::alteracion del estado mental}} -> {{c3::colangitis grave (Tokyo grado III)}}",
    '<span class="redflag">Sepsis severa biliar; descompresion en &lt;24 h, UCI.</span>'
    '<span class="ecoe">ECOE: "Pentada de Reynolds = colangitis grave, UCI + CPRE urgente."</span>',
    C1 + ["abdomen_agudo", "colangitis"])

add_cloze(deck_c1,
    "Dolor {{c1::epigastrico en cinturon}} con irradiacion a espalda + vomito + {{c2::lipasa >3x}} valor normal -> {{c3::pancreatitis aguda}} (criterios de Atlanta revisados)",
    '<span class="contraste">Causas mas frecuentes: litiasis biliar (mujer) y alcohol (varon).</span>'
    '<span class="ecoe">ECOE: "Dolor en cinturon + lipasa elevada = pancreatitis; busco causa con USG + perfil hepatico."</span>',
    C1 + ["abdomen_agudo", "pancreatitis"])

add_cloze(deck_c1,
    "Dolor en {{c1::fosa iliaca izquierda}} en paciente >50 a + fiebre + cambio de habito intestinal -> {{c2::diverticulitis aguda}} (la apendicitis del lado izquierdo)",
    '<span class="contraste">Clasificacion de Hinchey (I-IV) guia manejo medico vs quirurgico.</span>'
    '<span class="ecoe">ECOE: "Patron de diverticulitis; TAC para clasificar Hinchey y decidir manejo."</span>',
    C1 + ["abdomen_agudo", "diverticulitis"])

add_cloze(deck_c1,
    "Dolor abdominal {{c1::subito en punalada}} + abdomen en tabla + antecedente de AINE o ulcera -> {{c2::perforacion de ulcera peptica}}; Rx con {{c3::aire libre subdiafragmatico}}",
    '<span class="redflag">Quirofano urgente (parche de Graham + lavado).</span>'
    '<span class="ecoe">ECOE: "Abdomen en tabla con neumoperitoneo = perforacion; laparotomia/laparoscopia urgente."</span>',
    C1 + ["abdomen_agudo", "perforacion"])

add_cloze(deck_c1,
    "Adulto mayor + distension abdominal masiva {{c1::asimetrica}} + dolor colico + ausencia de evacuaciones; Rx con asa en {{c2::grano de cafe}} o U invertida -> {{c3::volvulo de sigmoides}}",
    '<span class="contraste">Volvulo cecal = adulto joven, distension diferente; ambos = obstruccion en asa cerrada.</span>'
    '<span class="ecoe">ECOE: "Patron de volvulo sigmoides; descompresion endoscopica y cirugia electiva."</span>',
    C1 + ["abdomen_agudo", "volvulo"])

add_cloze(deck_c1,
    "Dolor abdominal {{c1::desproporcionado a los hallazgos}} de exploracion + acidosis metabolica + lactato elevado + {{c2::fibrilacion auricular}}/cardiopatia embolica -> {{c3::isquemia mesenterica aguda}}",
    '<span class="redflag">Ventana terapeutica breve; TAC angiografico + laparotomia urgente.</span>'
    '<span class="ecoe">ECOE: "Dolor desproporcionado en paciente con FA = isquemia mesenterica hasta demostrar lo contrario."</span>',
    C1 + ["abdomen_agudo", "isquemia"])

# --- OBSTRUCCION (6)
add_cloze(deck_c1,
    "Vomito {{c1::bilioso}} + dolor colico + distension {{c2::leve}} + antecedente de cirugia abdominal previa -> {{c3::SOI alta por adherencias}}",
    '<span class="contraste">Causa #1 de SOI = adherencias postquirurgicas. Hernias en pacientes sin cirugia previa.</span>'
    '<span class="ecoe">ECOE: "SOI alta por probable adherencia; SNG, hidratacion, prueba terapeutica con Gastrografin."</span>',
    C1 + ["obstruccion", "soi"])

add_cloze(deck_c1,
    "Distension abdominal marcada + vomito tardio {{c1::fecaloide}} + ausencia de paso de gas y heces + Rx con niveles hidroaereos y ausencia de gas distal -> {{c2::SOI baja completa}}",
    '<span class="redflag">Mayor riesgo de estrangulacion; TAC + manejo quirurgico si no resuelve.</span>'
    '<span class="ecoe">ECOE: "SOI distal completa; cirugia si no resuelve en 24-48 h o signos de isquemia."</span>',
    C1 + ["obstruccion", "soi"])

add_cloze(deck_c1,
    "Hernia inguinal/umbilical/incisional + masa {{c1::irreductible}} + dolor + signos de obstruccion intestinal -> {{c2::hernia incarcerada}}; si ademas hay cambio de coloracion, fiebre, sepsis = {{c3::hernia estrangulada}}",
    '<span class="redflag">Estrangulada = isquemia intestinal, quirofano urgente.</span>'
    '<span class="ecoe">ECOE: "Hernia estrangulada; reseccion intestinal si necrosis, hernioplastia."</span>',
    C1 + ["obstruccion", "hernia"])

add_cloze(deck_c1,
    "Distension abdominal + ausencia de RHA + sin causa mecanica identificada (postoperatorio, sepsis, alteraciones electroliticas, opioides) -> {{c1::ileo paralitico}}",
    '<span class="contraste">A diferencia de SOI mecanica: RHA AUSENTES (no metalicos), no hay nivel obstructivo.</span>'
    '<span class="ecoe">ECOE: "Ileo paralitico; manejo conservador, corregir electrolitos, retirar opioides."</span>',
    C1 + ["obstruccion", "ileo"])

add_cloze(deck_c1,
    "Adulto mayor encamado + estrenimiento cronico + distension subita + Rx con asa dilatada en {{c1::flanco izquierdo}} hacia hipocondrio derecho -> {{c2::volvulo sigmoides}} (forma de grano de cafe)",
    '<span class="contraste">Cecal = adulto joven, asa en cuadrante superior izquierdo.</span>'
    '<span class="ecoe">ECOE: "Patron radiografico de volvulo sigmoides; descompresion endoscopica."</span>',
    C1 + ["obstruccion", "volvulo"])

add_cloze(deck_c1,
    "Obstruccion intestinal con {{c1::asa cerrada}} (volvulo, hernia estrangulada, banda adhesiva) tiene mayor riesgo de {{c2::isquemia y perforacion}} -> requiere cirugia mas urgente que SOI por adherencia simple",
    '<span class="redflag">Datos de isquemia: lactato elevado, taquicardia, dolor desproporcionado, defensa.</span>'
    '<span class="ecoe">ECOE: "Asa cerrada = no esperar resolucion; quirofano."</span>',
    C1 + ["obstruccion", "asa_cerrada"])

# --- INFECCION QUIRURGICA (5)
add_cloze(deck_c1,
    "Abdomen {{c1::en tabla}} (rigidez generalizada) + dolor a cualquier movimiento + sepsis -> {{c2::peritonitis secundaria}} (perforacion de viscera hueca)",
    '<span class="redflag">Indicacion quirurgica de control de foco.</span>'
    '<span class="ecoe">ECOE: "Peritonitis difusa; ATB de amplio espectro + control quirurgico del foco."</span>',
    C1 + ["infeccion", "peritonitis"])

add_cloze(deck_c1,
    "Fiebre persistente + leucocitosis + dolor focal + sintomas sistemicos en {{c1::postoperatorio (5-10 dias)}} -> sospecha {{c2::absceso intraabdominal}}",
    '<span class="contraste">TAC con contraste oral/IV es el estudio de eleccion.</span>'
    '<span class="ecoe">ECOE: "Sospecho absceso postoperatorio; TAC y drenaje percutaneo guiado."</span>',
    C1 + ["infeccion", "absceso"])

add_cloze(deck_c1,
    "Dolor {{c1::desproporcionado}} a hallazgos cutaneos + edema + {{c2::crepitacion}} + lesiones bullosas/equimosis + toxicidad sistemica -> {{c3::fascitis necrotizante}}",
    '<span class="redflag">Emergencia quirurgica; desbridamiento amplio + ATB + soporte.</span>'
    '<span class="ecoe">ECOE: "Fascitis necrotizante; quirofano YA + carbapenem + clindamicina + vancomicina."</span>',
    C1 + ["infeccion", "fascitis"])

add_cloze(deck_c1,
    "Diabetico + lesion en pie + olor fetido + drenaje + {{c1::crepitacion}} en partes blandas -> {{c2::gangrena gaseosa / infeccion polimicrobiana}}; Rx muestra {{c3::aire en tejido subcutaneo}}",
    '<span class="redflag">Desbridamiento amplio + ATB; valorar amputacion.</span>'
    '<span class="ecoe">ECOE: "Gangrena en diabetico; desbridamiento + amplio espectro + control glucemico."</span>',
    C1 + ["infeccion", "gangrena"])

add_cloze(deck_c1,
    "Sepsis quirurgica = sospecha de infeccion + {{c1::qSOFA >=2}} (FR>=22, PAS&lt;=100, alt mental) o disfuncion organica -> activar bundle hora-1 de {{c2::Surviving Sepsis Campaign 2021}}",
    '<span class="contraste">Shock septico = sepsis + vasopresor para PAM>=65 + lactato >2 pese a resucitacion.</span>'
    '<span class="ecoe">ECOE: "Activo bundle: lactato, hemocultivos, ATB &lt;1 h, cristaloides 30 mL/kg, control foco."</span>',
    C1 + ["infeccion", "sepsis"])

# --- ESPECIALES (3)
add_cloze(deck_c1,
    "Cefalea {{c1::subita, en trueno, la peor de la vida}} + meningismo + fotofobia -> {{c2::hemorragia subaracnoidea (HSA)}} por ruptura aneurismatica",
    '<span class="redflag">TAC simple urgente; si negativa y alta sospecha, puncion lumbar (xantocromia).</span>'
    '<span class="ecoe">ECOE: "Cefalea centinela; TAC simple urgente, neurocirugia."</span>',
    C1 + ["especiales", "hsa"])

add_cloze(deck_c1,
    "Dolor {{c1::desgarrante}} toracico que se irradia a espalda + {{c2::diferencia de pulsos/PA en ambos brazos}} + mediastino ensanchado en Rx -> {{c3::diseccion aortica}}",
    '<span class="redflag">Tipo A (aorta ascendente) = quirofano urgente; tipo B = manejo medico.</span>'
    '<span class="ecoe">ECOE: "Cuadro de diseccion aortica; TAC con contraste y control de PA con esmolol."</span>',
    C1 + ["especiales", "diseccion"])

add_cloze(deck_c1,
    "Adolescente/joven + dolor testicular {{c1::subito intenso}} + nausea + {{c2::ausencia de reflejo cremasterico}} + signo de Prehn negativo (no mejora al elevar) -> {{c3::torsion testicular}}",
    '<span class="redflag">Ventana de 6 h para salvar el testiculo; cirugia urgente.</span>'
    '<span class="contraste">Epididimitis: Prehn positivo (mejora al elevar), febril, gradual.</span>'
    '<span class="ecoe">ECOE: "Torsion testicular; exploracion quirurgica urgente con orquidopexia bilateral."</span>',
    C1 + ["especiales", "torsion"])


# ============================================================
# CAPA 2 - EXPLORACION Y ATLS VERBALIZADO (35 cloze)
# Pregunta clave: "donde esta fallando?"
# ============================================================
C2 = ["capa2", "exploracion", "atls"]

# --- ATLS PRIMARY SURVEY (8)
add_cloze(deck_c2,
    "ATLS - {{c1::A}}irway con control de columna cervical: verificar permeabilidad, voz, cuerpo extrano; si compromiso -> {{c2::cricotiroidotomia/IOT}}; mantener {{c3::collarin}} hasta descartar lesion cervical",
    '<span class="ecoe">ECOE: "Inicio ABCDE; via aerea permeable, mantengo control cervical con collarin."</span>',
    C2 + ["atls", "via_aerea"])

add_cloze(deck_c2,
    "ATLS - {{c1::B}}reathing: exposicion toracica, inspeccion (asimetria, paradoja), palpacion (crepitos, enfisema), auscultacion, oxigeno {{c2::15 L/min con mascarilla reservorio}}",
    '<span class="contraste">Buscar y tratar de inmediato: neumotorax tension, hemotorax masivo, torax inestable, neumotorax abierto.</span>'
    '<span class="ecoe">ECOE: "Auscultacion bilateral simetrica; saturacion ___, oxigeno suplementario."</span>',
    C2 + ["atls", "ventilacion"])

add_cloze(deck_c2,
    "ATLS - {{c1::C}}irculation: dos accesos venosos perifericos {{c2::gruesos (16-18G)}}, evaluar pulsos, llenado capilar, color, PA; control de hemorragias externas con {{c3::compresion directa o torniquete}}",
    '<span class="contraste">Sangrado interno se sospecha por taquicardia + hipotension sin foco externo evidente.</span>'
    '<span class="ecoe">ECOE: "Dos vias gruesas, cristaloide tibio inicial, activo protocolo de transfusion masiva."</span>',
    C2 + ["atls", "circulacion"])

add_cloze(deck_c2,
    "ATLS - {{c1::D}}isability: nivel de conciencia con {{c2::Escala de Glasgow}}, pupilas (tamano, simetria, reactividad), focalidad/lateralizacion, glucemia capilar",
    '<span class="contraste">Glasgow &lt;=8 = considerar intubacion para proteccion de via aerea.</span>'
    '<span class="ecoe">ECOE: "Calculo Glasgow ___; pupilas isocoricas reactivas; descarto hipoglucemia."</span>',
    C2 + ["atls", "neurologico"])

add_cloze(deck_c2,
    "ATLS - {{c1::E}}xposicion completa + control termico: desnudar, examinar dorso (logroll), {{c2::cubrir con mantas tibias}} para prevenir hipotermia (triada letal)",
    '<span class="redflag">Triada letal: hipotermia + acidosis + coagulopatia = mortalidad masiva.</span>'
    '<span class="ecoe">ECOE: "Exposicion completa, logroll para revisar dorso, cubro al paciente."</span>',
    C2 + ["atls", "exposicion"])

add_cloze(deck_c2,
    "ATLS - Adjuntos al primary survey: monitorizacion {{c1::ECG, oximetria, capnografia}}, gases arteriales, lactato, {{c2::Rx torax y pelvis}}, FAST/e-FAST, sonda Foley y SNG (con contraindicaciones)",
    '<span class="contraste">Foley NO si: sangre en meato, equimosis perineal, hematoma escrotal, prostata flotante. SNG NO si fractura base craneo.</span>'
    '<span class="ecoe">ECOE: "Solicito Rx torax y pelvis, FAST, gases, lactato y BH; coloco Foley si no hay contraindicacion."</span>',
    C2 + ["atls", "adjuntos"])

add_cloze(deck_c2,
    "ATLS - Anamnesis dirigida {{c1::AMPLIA}}: {{c2::Alergias, Medicamentos, Patologia previa, Libaciones/ultima ingesta, Ambiente y mecanismo}} del trauma",
    '<span class="ecoe">ECOE: "Recabo AMPLIA con familiares o paramedicos."</span>',
    C2 + ["atls", "amplia"])

add_cloze(deck_c2,
    "Secondary survey (ATLS): exploracion {{c1::cabeza a pies}} sistematica tras estabilizar; reevaluacion continua de ABCDE; manejo definitivo de lesiones",
    '<span class="contraste">Si en algun momento el paciente se deteriora -> reiniciar ABCDE desde A.</span>'
    '<span class="ecoe">ECOE: "Inicio secondary survey, reevaluo ABCDE cada vez que hay cambio clinico."</span>',
    C2 + ["atls", "secondary"])

# --- EXPLORACION ABDOMINAL (10)
add_cloze(deck_c2,
    "Orden correcto de exploracion abdominal: {{c1::inspeccion -> auscultacion -> percusion -> palpacion superficial -> palpacion profunda}}",
    '<span class="contraste">Auscultar ANTES de palpar para no alterar los RHA.</span>'
    '<span class="ecoe">ECOE: "Exploro en orden: inspecciono, ausculto, percuto y palpo de menor a mayor profundidad."</span>',
    C2 + ["exploracion", "orden"])

add_cloze(deck_c2,
    "Inspeccion abdominal busca: {{c1::cicatrices previas}}, {{c2::distension}}, eventraciones, equimosis (Cullen, Grey-Turner), peristalsis visible, circulacion colateral",
    '<span class="viva">Imagen: el abdomen cuenta su historia antes de tocarlo.</span>'
    '<span class="ecoe">ECOE: "Inspecciono buscando cicatrices, distension y signos cutaneos."</span>',
    C2 + ["exploracion", "inspeccion"])

add_cloze(deck_c2,
    "Auscultacion: RHA {{c1::aumentados/metalicos}} = obstruccion temprana; RHA {{c2::ausentes}} = ileo paralitico o peritonitis avanzada",
    '<span class="contraste">RHA normales no descartan patologia quirurgica.</span>'
    '<span class="ecoe">ECOE: "Auscultacion en 4 cuadrantes durante 1 minuto."</span>',
    C2 + ["exploracion", "auscultacion"])

add_cloze(deck_c2,
    "Percusion: {{c1::timpanismo}} en gas/obstruccion; {{c2::matidez en flancos cambiante}} = ascitis/liquido libre; matidez hepatica desplazada = {{c3::neumoperitoneo}}",
    '<span class="ecoe">ECOE: "Percuto en cuatro cuadrantes; busco matidez cambiante y timpanismo."</span>',
    C2 + ["exploracion", "percusion"])

add_cloze(deck_c2,
    "Palpacion: superficial primero (toda la mano apoyada), luego profunda; distinguir {{c1::defensa voluntaria (cede al distraer)}} de {{c2::defensa involuntaria (no cede, peritonitis)}}",
    '<span class="ecoe">ECOE: "Diferencio defensa voluntaria de involuntaria; busco megalias y masas."</span>',
    C2 + ["exploracion", "palpacion"])

add_cloze(deck_c2,
    "Signo de {{c1::Murphy}}: paciente detiene la inspiracion profunda al palpar el HD bajo el reborde costal -> {{c2::colecistitis aguda}}",
    '<span class="contraste">Murphy ecografico = dolor selectivo al colocar el transductor sobre la vesicula.</span>'
    '<span class="ecoe">ECOE: "Murphy positivo, sospecho colecistitis."</span>',
    C2 + ["signos", "murphy"])

add_cloze(deck_c2,
    "Punto de {{c1::McBurney}}: ubicado a {{c2::un tercio externo}} de la linea que une espina iliaca anterosuperior derecha con el ombligo; dolor maximo en apendicitis",
    '<span class="ecoe">ECOE: "Dolor maximo en punto de McBurney."</span>',
    C2 + ["signos", "mcburney"])

add_cloze(deck_c2,
    "Signo de {{c1::Blumberg}} (rebote): dolor al {{c2::soltar bruscamente}} la palpacion profunda; indica {{c3::irritacion peritoneal}}",
    '<span class="contraste">No realizar si ya hay defensa generalizada (peritonitis clara).</span>'
    '<span class="ecoe">ECOE: "Rebote positivo = irritacion peritoneal."</span>',
    C2 + ["signos", "blumberg"])

add_cloze(deck_c2,
    "Signo de {{c1::Rovsing}}: palpacion en {{c2::fosa iliaca izquierda}} produce dolor en {{c3::FID}} -> sugiere apendicitis",
    '<span class="ecoe">ECOE: "Rovsing positivo apoya diagnostico de apendicitis."</span>',
    C2 + ["signos", "rovsing"])

add_cloze(deck_c2,
    "Signo del {{c1::psoas}}: dolor a la {{c2::extension de la cadera derecha}} con paciente en decubito lateral izquierdo = apendice retrocecal; signo del {{c3::obturador}}: rotacion interna con cadera flexionada = apendice pelvico",
    '<span class="ecoe">ECOE: "Psoas/obturador positivos sugieren apendice retrocecal o pelvico."</span>',
    C2 + ["signos", "psoas", "obturador"])

# --- SIGNOS ESPECIFICOS (8)
add_cloze(deck_c2,
    "Signo de {{c1::Cullen}}: equimosis {{c2::periumbilical}}; significa sangrado intra o retroperitoneal (pancreatitis hemorragica, ectopico roto)",
    '<span class="ecoe">ECOE: "Cullen sugiere hemorragia intraperitoneal."</span>',
    C2 + ["signos", "cullen"])

add_cloze(deck_c2,
    "Signo de {{c1::Grey-Turner}}: equimosis en {{c2::flancos}}; indica sangrado {{c3::retroperitoneal}} (pancreatitis necrohemorragica, AAA roto contenido)",
    '<span class="ecoe">ECOE: "Grey-Turner = sangrado retroperitoneal."</span>',
    C2 + ["signos", "grey_turner"])

add_cloze(deck_c2,
    "Signo de {{c1::Kehr}}: dolor referido al {{c2::hombro izquierdo}} por irritacion diafragmatica; clasico de {{c3::lesion esplenica}} con hemoperitoneo",
    '<span class="contraste">Kehr derecho = irritacion del diafragma derecho (sangre, absceso subfrenico).</span>'
    '<span class="ecoe">ECOE: "Kehr sugiere irritacion diafragmatica por sangrado esplenico."</span>',
    C2 + ["signos", "kehr"])

add_cloze(deck_c2,
    "Maniobra/test de {{c1::Carnett}}: dolor abdominal que {{c2::aumenta al tensar la pared}} (levantar cabeza/piernas) -> origen {{c3::parietal}}; si disminuye -> visceral",
    '<span class="ecoe">ECOE: "Carnett positivo orienta a dolor parietal, no visceral."</span>',
    C2 + ["signos", "carnett"])

add_cloze(deck_c2,
    "Signo de {{c1::Courvoisier}}: vesicula {{c2::palpable e indolora}} + ictericia -> sugiere obstruccion {{c3::maligna distal}} (cancer de cabeza de pancreas, ampuloma)",
    '<span class="contraste">En coledocolitiasis cronica la vesicula esta fibrotica y NO se palpa (Courvoisier negativo).</span>'
    '<span class="ecoe">ECOE: "Courvoisier sugiere obstruccion biliar maligna."</span>',
    C2 + ["signos", "courvoisier"])

add_cloze(deck_c2,
    "Signo del {{c1::talon}} (Markle): el paciente se eleva en puntas y deja caer en talones -> dolor abdominal = {{c2::peritonitis}}",
    '<span class="ecoe">ECOE: "Markle positivo, signo de irritacion peritoneal."</span>',
    C2 + ["signos", "markle"])

add_cloze(deck_c2,
    "Tacto rectal: evaluar tono esfinteriano, {{c1::sangre/melena}}, masas, dolor en {{c2::fondo de saco de Douglas}} (apendicitis pelvica, EIP, absceso), prostata (sospecha de uretra lesionada en trauma)",
    '<span class="ecoe">ECOE: "Realizo tacto rectal buscando sangre, dolor en Douglas y prostata."</span>',
    C2 + ["exploracion", "tacto_rectal"])

add_cloze(deck_c2,
    "Exploracion de hernias: paciente {{c1::de pie}}, palpar anillo inguinal, pedir {{c2::Valsalva/tos}}, evaluar reducibilidad, dolor, signos de incarceracion",
    '<span class="ecoe">ECOE: "Exploro hernias en bipedestacion con Valsalva."</span>',
    C2 + ["exploracion", "hernias"])

# --- FAST + PROCEDIMIENTOS (6)
add_cloze(deck_c2,
    "FAST 4 ventanas: {{c1::perihepatica (Morrison/saco hepatorrenal)}}, {{c2::periesplenica}}, {{c3::suprapubica (Douglas)}}, {{c4::pericardica subxifoidea}}",
    '<span class="ecoe">ECOE: "Realizo FAST: cuatro ventanas buscando liquido libre."</span>',
    C2 + ["fast", "procedimientos"])

add_cloze(deck_c2,
    "e-FAST anade {{c1::ventanas pleurales}} para detectar {{c2::neumotorax}}: ausencia de deslizamiento pleural y de lineas B; signo del codigo de barras en modo M",
    '<span class="ecoe">ECOE: "e-FAST descarta neumotorax y hemotorax."</span>',
    C2 + ["fast", "neumotorax"])

add_cloze(deck_c2,
    "Sonda nasogastrica (SNG): indicada en SOI, perforacion, sangrado digestivo alto, ileo; contraindicada si {{c1::fractura de base de craneo}} (riesgo intracraneal); evalua contenido: bilioso, fecaloide, sangre",
    '<span class="ecoe">ECOE: "Coloco SNG salvo contraindicacion, valoro caracter del drenaje."</span>',
    C2 + ["procedimientos", "sng"])

add_cloze(deck_c2,
    "Sonda Foley contraindicada si: {{c1::sangre en meato uretral}}, {{c2::equimosis perineal en mariposa}}, hematoma escrotal, prostata flotante o no palpable (sospecha {{c3::lesion uretral}}) -> realizar uretrografia retrograda primero",
    '<span class="ecoe">ECOE: "Inspecciono meato y periné antes de Foley; uretrografia si sospecho lesion."</span>',
    C2 + ["procedimientos", "foley"])

add_cloze(deck_c2,
    "Accesos vasculares en trauma: {{c1::dos vias perifericas gruesas (16-18G)}} en fosa antecubital; si falla -> {{c2::intraosea}} (humero/tibia); ultima opcion: cateter central (femoral en trauma de cuello/torax)",
    '<span class="contraste">Cristaloide tibio inicial; transfusion 1:1:1 (plasma : plaquetas : globulos) si hemorragia masiva.</span>'
    '<span class="ecoe">ECOE: "Dos accesos gruesos, intraosea si fallo, Ringer lactato tibio."</span>',
    C2 + ["procedimientos", "accesos"])

add_cloze(deck_c2,
    "Descompresion de neumotorax a tension: aguja en {{c1::2do espacio intercostal linea medioclavicular}} (ATLS 9a) o {{c2::4to-5to EIC linea axilar anterior}} (ATLS 10a, mas efectivo) -> seguido de toracostomia con tubo",
    '<span class="ecoe">ECOE: "Descomprimo con aguja, luego coloco tubo en 5to EIC linea axilar anterior."</span>',
    C2 + ["procedimientos", "neumotorax"])

# --- FRASES CODIGO ECOE (3)
add_cloze(deck_c2,
    "Frase ECOE clave: {{c1::Paciente hemodinamicamente inestable, activo codigo de trauma}}",
    '<span class="ecoe">ECOE: Decir esto en voz alta gana puntos por reconocimiento de gravedad.</span>',
    C2 + ["frases", "ecoe"])

add_cloze(deck_c2,
    "Frase ECOE clave: {{c1::Abdomen quirurgico con datos de irritacion peritoneal generalizada}}",
    '<span class="ecoe">ECOE: Comunica al sinodal que has reconocido el patron de peritonitis.</span>',
    C2 + ["frases", "ecoe"])

add_cloze(deck_c2,
    "Frase ECOE clave: {{c1::Paciente candidato a laparotomia exploradora de urgencia}}",
    '<span class="ecoe">ECOE: Indica decision quirurgica definitiva.</span>',
    C2 + ["frases", "ecoe"])


# ============================================================
# CAPA 3 - INTERPRETACION DE ESTUDIOS (35 cloze)
# ============================================================
C3 = ["capa3", "estudios"]

# --- LABORATORIO (12)
add_cloze(deck_c3,
    "Lactato {{c1::>2 mmol/L}} = hipoperfusion; {{c2::>4 mmol/L}} = shock establecido; {{c3::persistente alto tras resucitacion}} = mortalidad alta",
    '<span class="ecoe">ECOE: "Lactato es marcador de perfusion; sigue tendencia tras resucitacion."</span>',
    C3 + ["lactato", "perfusion"])

add_cloze(deck_c3,
    "Gasometria: {{c1::acidosis metabolica con anion gap elevado}} en abdomen agudo sugiere {{c2::hipoperfusion, isquemia mesenterica o sepsis severa}}",
    '<span class="contraste">Anion gap = Na - (Cl + HCO3); normal 8-12.</span>'
    '<span class="ecoe">ECOE: "Acidosis con anion gap orienta a isquemia o sepsis."</span>',
    C3 + ["gasometria", "anion_gap"])

add_cloze(deck_c3,
    "Deficit de base {{c1::menor a -6 mEq/L}} en trauma = predictor de {{c2::sangrado activo y necesidad de transfusion masiva}}",
    '<span class="ecoe">ECOE: "Deficit de base profundo en trauma = activo protocolo masivo."</span>',
    C3 + ["gasometria", "trauma"])

add_cloze(deck_c3,
    "BH: leucocitosis con neutrofilia y {{c1::bandemia (>10% de bandas)}} indica {{c2::infeccion bacteriana o sepsis con respuesta medular intensa}}",
    '<span class="contraste">Leucopenia + bandemia = sepsis severa, pronostico peor.</span>'
    '<span class="ecoe">ECOE: "Bandemia marcada apunta a sepsis con respuesta medular intensa."</span>',
    C3 + ["bh", "sepsis"])

add_cloze(deck_c3,
    "Hb {{c1::inicial NO refleja}} el sangrado agudo: hasta {{c2::6-24 h}} por hemodilucion compensatoria; usar lactato/deficit de base como marcadores tempranos",
    '<span class="ecoe">ECOE: "No me confio del Hb inicial en trauma agudo; valoro tendencia."</span>',
    C3 + ["bh", "trauma"])

add_cloze(deck_c3,
    "Lipasa {{c1::>3 veces el limite superior normal}} con dolor compatible = {{c2::pancreatitis aguda}} (criterios de Atlanta revisados)",
    '<span class="contraste">Lipasa mas especifica que amilasa; lipasa permanece elevada mas tiempo.</span>'
    '<span class="ecoe">ECOE: "Lipasa >3x con dolor en cinturon = pancreatitis."</span>',
    C3 + ["lipasa", "pancreatitis"])

add_cloze(deck_c3,
    "BUN/Cr {{c1::>20-36}} en sangrado digestivo apoya origen {{c2::alto (HDA)}} por digestion de proteinas + hipovolemia prerrenal",
    '<span class="ecoe">ECOE: "BUN/Cr elevado en sangrado digestivo orienta a HDA."</span>',
    C3 + ["hda", "bun"])

add_cloze(deck_c3,
    "Score de Glasgow-Blatchford (HDA): variables incluyen {{c1::BUN, Hb, PAS, FC, melena, sincope, hepatopatia, falla cardiaca}}; puntaje 0 = manejo ambulatorio seguro",
    '<span class="contraste">Rockall (post-endoscopia) estima mortalidad y resangrado.</span>'
    '<span class="ecoe">ECOE: "Aplico Glasgow-Blatchford para triage de HDA."</span>',
    C3 + ["hda", "scores"])

add_cloze(deck_c3,
    "Beta-hCG cuantitativa {{c1::>1500-2000 mUI/mL}} sin saco gestacional intrauterino en USG transvaginal -> {{c2::embarazo ectopico hasta demostrar lo contrario}}",
    '<span class="ecoe">ECOE: "Discordancia beta-hCG/USG sugiere ectopico."</span>',
    C3 + ["beta_hcg", "ectopico"])

add_cloze(deck_c3,
    "Procalcitonina elevada (>0.5 ng/mL) sugiere {{c1::infeccion bacteriana sistemica}}; util para diferenciar de respuesta inflamatoria esteril",
    '<span class="contraste">No reemplaza juicio clinico; sirve para guiar suspension de ATB.</span>'
    '<span class="ecoe">ECOE: "Procalcitonina apoya infeccion bacteriana sistemica."</span>',
    C3 + ["procalcitonina", "sepsis"])

add_cloze(deck_c3,
    "INR {{c1::>1.5}} + albumina baja + bilirrubina elevada en paciente quirurgico = {{c2::hepatopatia avanzada}} -> alto riesgo perioperatorio (MELD, Child-Pugh)",
    '<span class="ecoe">ECOE: "Riesgo quirurgico alto por hepatopatia; calculo MELD."</span>',
    C3 + ["coagulacion", "hepatico"])

add_cloze(deck_c3,
    "PCR elevada + leucocitosis + clinica focal apoya {{c1::proceso inflamatorio/infeccioso}} (apendicitis, colecistitis, diverticulitis); PCR sola no decide cirugia",
    '<span class="ecoe">ECOE: "PCR es marcador inflamatorio, no diagnostico unico."</span>',
    C3 + ["pcr", "inflamacion"])

# --- IMAGEN RX (5)
add_cloze(deck_c3,
    "{{c1::Aire libre subdiafragmatico}} en Rx de torax en bipedestacion = {{c2::perforacion de viscera hueca}} -> indicacion quirurgica",
    '<span class="contraste">Sensibilidad 75-80%; TAC es mas sensible si Rx negativa con alta sospecha.</span>'
    '<span class="ecoe">ECOE: "Neumoperitoneo = perforacion, laparotomia urgente."</span>',
    C3 + ["rx", "perforacion"])

add_cloze(deck_c3,
    "{{c1::Niveles hidroaereos multiples en escalera}} con dilatacion intestinal = {{c2::obstruccion intestinal mecanica (SOI)}}; ausencia de gas distal sugiere SOI completa",
    '<span class="ecoe">ECOE: "Patron radiografico de SOI completa."</span>',
    C3 + ["rx", "soi"])

add_cloze(deck_c3,
    "Imagen radiologica en {{c1::grano de cafe / U invertida}} con asa dilatada masiva = {{c2::volvulo de sigmoides}}",
    '<span class="ecoe">ECOE: "Imagen en grano de cafe = volvulo sigmoides."</span>',
    C3 + ["rx", "volvulo"])

add_cloze(deck_c3,
    "{{c1::Asa centinela}} (segmento intestinal dilatado fijo) en cuadrante superior izquierdo en Rx = {{c2::pancreatitis aguda}} con ileo localizado",
    '<span class="ecoe">ECOE: "Asa centinela apoya pancreatitis."</span>',
    C3 + ["rx", "pancreatitis"])

add_cloze(deck_c3,
    "Borramiento de la {{c1::sombra del psoas}} o asimetria = sugiere {{c2::proceso retroperitoneal}} (absceso, sangrado, masa)",
    '<span class="ecoe">ECOE: "Borramiento del psoas indica patologia retroperitoneal."</span>',
    C3 + ["rx", "retroperitoneo"])

# --- USG (5)
add_cloze(deck_c3,
    "Criterios USG de colecistitis: pared {{c1::>4-5 mm}}, {{c2::liquido perivesicular}}, distension vesicular, litos impactados en el cuello, {{c3::Murphy ecografico positivo}}",
    '<span class="ecoe">ECOE: "USG con criterios para colecistitis aguda."</span>',
    C3 + ["usg", "colecistitis"])

add_cloze(deck_c3,
    "Via biliar comun dilatada {{c1::>6 mm}} (o >10 mm en colecistectomizados) = {{c2::obstruccion biliar}} (litiasis, neoplasia, estenosis)",
    '<span class="ecoe">ECOE: "Coledoco dilatado, sospecho coledocolitiasis y solicito CPRE."</span>',
    C3 + ["usg", "biliar"])

add_cloze(deck_c3,
    "FAST positivo: {{c1::imagen anecoica}} (sangre/liquido) en cualquiera de las cuatro ventanas; el {{c2::receso hepatorrenal (Morrison)}} es la mas sensible",
    '<span class="contraste">FAST positivo + paciente inestable = laparotomia sin TAC.</span>'
    '<span class="ecoe">ECOE: "Morrison con liquido libre + paciente inestable = quirofano."</span>',
    C3 + ["fast", "trauma"])

add_cloze(deck_c3,
    "Apendice por USG: diametro {{c1::>6-7 mm}}, {{c2::no compresible}}, pared engrosada, dolor selectivo al transductor = apendicitis",
    '<span class="contraste">USG operador-dependiente; TAC si dudoso, sobre todo en obeso o gas.</span>'
    '<span class="ecoe">ECOE: "Apendice no compresible >7 mm con dolor al transductor."</span>',
    C3 + ["usg", "apendicitis"])

add_cloze(deck_c3,
    "USG transvaginal en sospecha de ectopico: {{c1::ausencia de saco gestacional intrauterino}} con beta-hCG >1500-2000; {{c2::masa anexial complex}} y/o {{c3::liquido libre en Douglas}}",
    '<span class="ecoe">ECOE: "USG sin saco intrauterino con beta-hCG positiva = ectopico."</span>',
    C3 + ["usg", "ectopico"])

# --- TAC (8)
add_cloze(deck_c3,
    "TAC de apendicitis: apendice {{c1::engrosado >6 mm}}, {{c2::apendicolito}}, {{c3::grasa periapendicular sucia (estriacion)}}, posible coleccion o aire extraluminal (perforacion)",
    '<span class="ecoe">ECOE: "TAC con criterios para apendicitis no complicada vs complicada."</span>',
    C3 + ["tac", "apendicitis"])

add_cloze(deck_c3,
    "{{c1::Neumoperitoneo}} en TAC abdominal = perforacion de viscera hueca; TAC detecta cantidades minimas que la Rx no muestra",
    '<span class="ecoe">ECOE: "TAC con neumoperitoneo confirma perforacion."</span>',
    C3 + ["tac", "perforacion"])

add_cloze(deck_c3,
    "TAC en pancreatitis: clasificacion {{c1::Atlanta revisada}}; busca {{c2::edema, necrosis, colecciones (APFC, ANC, pseudoquiste, WON)}}; TAC se hace optimamente a las {{c3::72-96 h}} (no en agudo)",
    '<span class="ecoe">ECOE: "TAC tardio en pancreatitis para detectar necrosis y colecciones."</span>',
    C3 + ["tac", "pancreatitis"])

add_cloze(deck_c3,
    "TAC de diverticulitis: {{c1::engrosamiento mural}} + {{c2::estriacion grasa pericolica izquierda}} + diverticulos; clasificacion {{c3::Hinchey}} I-IV segun complicaciones (absceso, fistula, peritonitis)",
    '<span class="ecoe">ECOE: "Diverticulitis Hinchey I/II por TAC = manejo medico; III/IV = cirugia."</span>',
    C3 + ["tac", "diverticulitis"])

add_cloze(deck_c3,
    "Liquido libre intraperitoneal con densidad {{c1::>30 UH}} en TAC = {{c2::hemoperitoneo}} (sangre); densidad &lt;15 UH = liquido seroso/ascitis",
    '<span class="ecoe">ECOE: "Liquido hiperdenso = sangre, busco fuente."</span>',
    C3 + ["tac", "hemoperitoneo"])

add_cloze(deck_c3,
    "{{c1::Extravasacion de contraste intraarterial}} en TAC con contraste = {{c2::sangrado activo}} -> indicacion de angiografia con embolizacion o cirugia",
    '<span class="ecoe">ECOE: "Extravasacion activa, valoro embolizacion."</span>',
    C3 + ["tac", "sangrado"])

add_cloze(deck_c3,
    "TAC de isquemia mesenterica: {{c1::defecto de llenado}} en mesenterica superior (embolia/trombosis), {{c2::engrosamiento mural}}, {{c3::neumatosis intestinal}} (signo tardio), gas en porta",
    '<span class="redflag">Neumatosis y gas portal = necrosis transmural, mortalidad alta.</span>'
    '<span class="ecoe">ECOE: "Hallazgos de isquemia mesenterica avanzada en TAC."</span>',
    C3 + ["tac", "isquemia"])

add_cloze(deck_c3,
    "Aneurisma aortico abdominal: cribado en {{c1::varones 65-75 a fumadores}}; quirurgico si {{c2::>=5.5 cm}}, crecimiento >1 cm/ano o sintomatico; signos de roto en TAC: {{c3::halo perianeurismatico, perdida de plano graso retroperitoneal}}",
    '<span class="ecoe">ECOE: "AAA >5.5 cm = referir; signos de roto = quirofano."</span>',
    C3 + ["tac", "aaa"])

# --- SCORES (5)
add_cloze(deck_c3,
    "Score de {{c1::Alvarado}} para apendicitis (8 puntos): MANTRELS (Migracion, Anorexia, Nausea, Tenderness/dolor en FID, Rebote, Elevacion temp, Leucocitosis, Shift/desviacion izq); {{c2::>=7}} = alta probabilidad",
    '<span class="ecoe">ECOE: "Alvarado >=7 apoya apendicitis."</span>',
    C3 + ["scores", "alvarado"])

add_cloze(deck_c3,
    "Criterios de Ranson al ingreso (pancreatitis): {{c1::edad >55, GB >16000, glucosa >200, LDH >350, AST >250}}; >=3 = severidad",
    '<span class="contraste">A las 48 h: caida Hto >10%, BUN >5, calcio &lt;8, PaO2 &lt;60, deficit base >4, secuestro liquido >6 L.</span>'
    '<span class="ecoe">ECOE: "Ranson al ingreso para clasificar severidad."</span>',
    C3 + ["scores", "ranson"])

add_cloze(deck_c3,
    "BISAP (pancreatitis): {{c1::BUN >25, Impaired mental, SIRS, Edad >60, derrame Pleural}}; >=3 = severa, mortalidad alta",
    '<span class="contraste">Mas practico que Ranson; calcula en 24 h con datos sencillos.</span>'
    '<span class="ecoe">ECOE: "BISAP >=3 = pancreatitis severa, UCI."</span>',
    C3 + ["scores", "bisap"])

add_cloze(deck_c3,
    "qSOFA (al lado de la cama): {{c1::FR >=22, alteracion del estado mental, PAS &lt;=100}}; >=2 puntos = mayor mortalidad por sepsis",
    '<span class="contraste">SOFA completo se usa en UCI para definir disfuncion organica.</span>'
    '<span class="ecoe">ECOE: "qSOFA >=2 = sospecha sepsis, activo bundle."</span>',
    C3 + ["scores", "qsofa"])

add_cloze(deck_c3,
    "Clasificacion endoscopica de {{c1::Forrest}} para HDA por ulcera: Ia chorro arterial, Ib babeo, IIa vaso visible, IIb coagulo adherido, IIc mancha pigmentada, III fondo limpio; {{c2::Ia, Ib, IIa}} requieren endohemostasia",
    '<span class="ecoe">ECOE: "Forrest Ia-IIa = endohemostasia y nuevo control."</span>',
    C3 + ["scores", "forrest"])


# ============================================================
# CAPA 4 - MANEJO Y DDX (50 Q&A)
# ============================================================
C4 = ["capa4", "manejo"]

# --- TRAUMA (8)
add_qa(deck_c4,
    "Manejo: <b>Trauma penetrante por objeto encajado (cuchillo, varilla)</b>",
    "1) <b>NO retirar el objeto</b> en sala (actua como tapon).<br>"
    "2) Estabilizar el objeto con apositos.<br>"
    "3) Activar codigo de trauma; aplicar <b>ABCDE de ATLS</b>.<br>"
    "4) Dos vias gruesas + cristaloides tibios.<br>"
    "5) Si <b>inestable</b> -> <b>laparotomia exploradora</b> (objeto se retira en quirofano).<br>"
    "6) Si <b>estable</b> -> <b>TAC con contraste IV</b> para evaluar trayectoria y organos."
    '<span class="ecoe">ECOE: "No retiro, ABCDE, dos vias, quirofano si inestable o TAC si estable."</span>',
    C4 + ["trauma", "penetrante"])

add_qa(deck_c4,
    "Manejo: <b>Trauma penetrante abdominal con inestabilidad hemodinamica</b>",
    "1) ABCDE + dos accesos vasculares gruesos.<br>"
    "2) Cristaloide tibio (max 1 L) + <b>protocolo de transfusion masiva (1:1:1)</b>.<br>"
    "3) <b>Acido tranexamico (TXA) 1 g IV en 10 min</b>, segunda dosis 1 g en 8 h (CRASH-2 si &lt;3 h).<br>"
    "4) <b>Laparotomia exploradora urgente</b> (no TAC).<br>"
    "5) Antibiotico profilactico de amplio espectro (cefalosporina + metronidazol)."
    '<span class="ecoe">ECOE: "Reanimacion balanceada, TXA temprano, quirofano YA."</span>',
    C4 + ["trauma", "inestable"])

add_qa(deck_c4,
    "Manejo: <b>Trauma cerrado abdominal estable</b>",
    "1) ABCDE + monitorizacion.<br>"
    "2) <b>FAST</b> al ingreso; si positivo + estable -> <b>TAC con contraste IV</b>.<br>"
    "3) Lesion esplenica/hepatica baja grado en estable -> <b>manejo no operatorio</b> con UCI/observacion y serie de Hb.<br>"
    "4) Datos de inestabilidad o sangrado activo persistente -> laparotomia o angioembolizacion."
    '<span class="ecoe">ECOE: "Trauma cerrado estable = TAC, manejo conservador si estable."</span>',
    C4 + ["trauma", "cerrado"])

add_qa(deck_c4,
    "Manejo: <b>Neumotorax a tension</b>",
    "<b>Diagnostico clinico, no esperar Rx</b>:<br>"
    "1) <b>Descompresion con aguja</b>: 5to EIC linea axilar anterior (ATLS 10a) o 2do EIC linea medioclavicular.<br>"
    "2) Seguido de <b>toracostomia con tubo</b> (calibre 28-32 Fr) en 5to EIC linea axilar anterior.<br>"
    "3) Oxigeno + analgesia + monitorizacion."
    '<span class="ecoe">ECOE: "Descomprimo con aguja YA, luego tubo de toracostomia."</span>',
    C4 + ["trauma", "neumotorax"])

add_qa(deck_c4,
    "Manejo: <b>Tamponade cardiaco</b>",
    "1) Reconocer triada de Beck (hipotension, ingurgitacion yugular, ruidos apagados).<br>"
    "2) <b>FAST subxifoideo</b> confirma.<br>"
    "3) <b>Pericardiocentesis</b> de emergencia (subxifoidea, guiada por USG si posible).<br>"
    "4) En trauma penetrante torácico inestable: <b>toracotomia de reanimacion</b> en sala.<br>"
    "5) Manejo definitivo quirurgico (ventana pericardica/esternotomia)."
    '<span class="ecoe">ECOE: "Pericardiocentesis o toracotomia segun mecanismo."</span>',
    C4 + ["trauma", "tamponade"])

add_qa(deck_c4,
    "Manejo: <b>Hemotorax masivo</b>",
    "1) Colocar <b>toracostomia con tubo</b> (28-32 Fr) en 5to EIC linea axilar anterior.<br>"
    "2) Si <b>drenaje inicial >1500 mL</b> o <b>>200 mL/h por 4 h</b> -> <b>toracotomia urgente</b>.<br>"
    "3) Reanimacion con hemoderivados (1:1:1) + TXA.<br>"
    "4) Considerar autotransfusion en algunos centros."
    '<span class="ecoe">ECOE: "Tubo de toracostomia + toracotomia si criterios de hemotorax masivo."</span>',
    C4 + ["trauma", "hemotorax"])

add_qa(deck_c4,
    "Manejo: <b>Choque hipovolemico hemorragico</b> (transfusion masiva)",
    "1) Control inmediato de sangrado evidente (compresion, torniquete).<br>"
    "2) Dos accesos perifericos gruesos; <b>1 L cristaloide tibio max</b>, luego hemoderivados.<br>"
    "3) <b>Protocolo de transfusion masiva 1:1:1</b> (plasma fresco congelado : plaquetas : concentrados eritrocitarios).<br>"
    "4) <b>TXA 1 g IV en 10 min</b>, repetir 1 g en 8 h (CRASH-2, &lt;3 h del trauma).<br>"
    "5) Reanimacion hipotensiva permisiva (PAS 80-90) excepto TCE (PAS >=110).<br>"
    "6) Calcio (gluconato 1 g cada 4 U) para prevenir hipocalcemia por citrato.<br>"
    "7) Control definitivo en quirofano."
    '<span class="ecoe">ECOE: "Protocolo masivo 1:1:1 + TXA + control quirurgico definitivo."</span>',
    C4 + ["trauma", "transfusion"])

add_qa(deck_c4,
    "Manejo: <b>Fractura pelvica inestable con sangrado</b>",
    "1) <b>Faja/binder pelvico</b> colocado a nivel de trocanteres mayores en sala.<br>"
    "2) Reanimacion + protocolo de transfusion masiva.<br>"
    "3) Si persiste inestable -> <b>angioembolizacion</b> (sangrado arterial) o <b>fijacion externa</b>.<br>"
    "4) Empaquetamiento pelvico preperitoneal si no hay angio disponible.<br>"
    "5) NO laparotomia inicial salvo otra indicacion (puede empeorar sangrado venoso retroperitoneal)."
    '<span class="ecoe">ECOE: "Binder pelvico + angioembolizacion como primera linea."</span>',
    C4 + ["trauma", "pelvis"])

# --- HEMORRAGIA (6)
add_qa(deck_c4,
    "Manejo: <b>Embarazo ectopico roto</b>",
    "1) Estabilizar (dos vias, cristaloides, hemoderivados).<br>"
    "2) Tipificar y cruzar; considerar <b>Ig anti-D</b> si Rh negativa.<br>"
    "3) <b>Cirugia urgente</b>: laparoscopia (estandar) o laparotomia segun estabilidad y experiencia.<br>"
    "4) <b>Salpingectomia</b> (eleccion en ectopico roto) vs salpingostomia (si deseo de fertilidad, tuba contralateral danada).<br>"
    "5) Postop: seguimiento de beta-hCG hasta &lt;5."
    '<span class="ecoe">ECOE: "Ectopico roto = quirofano YA, salpingectomia."</span>',
    C4 + ["hemorragia", "ectopico"])

add_qa(deck_c4,
    "Manejo: <b>HDA por ulcera peptica</b> (ACG 2021)",
    "1) Reanimacion + accesos vasculares; transfundir si <b>Hb &lt;7</b> (o &lt;8 si cardiopata).<br>"
    "2) <b>IBP IV en bolo 80 mg + infusion 8 mg/h por 72 h</b> (o bolos altas dosis intermitentes).<br>"
    "3) <b>Endoscopia &lt;24 h</b> (urgente &lt;12 h si inestable).<br>"
    "4) Endohemostasia segun <b>Forrest Ia/Ib/IIa</b>: termocoagulacion + inyeccion adrenalina + clips.<br>"
    "5) Erradicar H. pylori si positivo; revisar AINE/anticoagulantes."
    '<span class="ecoe">ECOE: "IBP IV + endoscopia &lt;24 h + endohemostasia + erradicacion H. pylori."</span>',
    C4 + ["hemorragia", "hda_ulcera"])

add_qa(deck_c4,
    "Manejo: <b>HDA por varices esofagicas</b>",
    "1) Reanimacion con cristaloides moderada (evitar sobrecarga = aumenta presion portal); transfundir Hb &lt;7.<br>"
    "2) <b>Octreotido 50 mcg IV bolo + 50 mcg/h infusion por 2-5 dias</b> (o terlipresina si disponible).<br>"
    "3) <b>Ceftriaxona 1 g IV/24 h</b> (profilaxis SBP y mortalidad).<br>"
    "4) <b>Endoscopia &lt;12 h</b> con <b>ligadura endoscopica</b> (eleccion); escleroterapia si no posible.<br>"
    "5) Falla -> sonda de <b>Sengstaken-Blakemore</b> como puente a <b>TIPS</b>.<br>"
    "6) Profilaxis secundaria con <b>betabloqueador no selectivo (propranolol/nadolol)</b> + ligaduras seriadas."
    '<span class="ecoe">ECOE: "Octreotido + ceftriaxona + endoscopia con ligadura."</span>',
    C4 + ["hemorragia", "varices"])

add_qa(deck_c4,
    "Manejo: <b>HDB grave</b> (ACG 2023)",
    "1) Reanimacion + estabilizacion; descartar HDA con SNG/endoscopia si dudoso.<br>"
    "2) <b>Colonoscopia preparada urgente (&lt;24 h)</b> en HDB severa; endohemostasia si lesion identificable.<br>"
    "3) Si paciente inestable o sangrado activo -> <b>angio-TC</b> y <b>angiografia con embolizacion</b>.<br>"
    "4) Cirugia (colectomia segmentaria) si no se localiza y persiste sangrado masivo (ultima opcion)."
    '<span class="ecoe">ECOE: "Colonoscopia urgente; angio-embolizacion si inestable."</span>',
    C4 + ["hemorragia", "hdb"])

add_qa(deck_c4,
    "Manejo: <b>Aneurisma aortico abdominal roto</b>",
    "1) Reconocer triada (dolor abdominal/lumbar + masa pulsatil + hipotension).<br>"
    "2) Reanimacion <b>hipotensiva permisiva (PAS 70-90)</b>.<br>"
    "3) <b>Quirofano sin retraso</b>; TAC solo si paciente estable y sospecha incierta.<br>"
    "4) <b>Reparacion endovascular (EVAR)</b> como primera opcion si anatomia favorable; cirugia abierta si no.<br>"
    "5) Cribado preventivo: USG en varones 65-75 a fumadores (USPSTF)."
    '<span class="ecoe">ECOE: "AAA roto = quirofano YA, hipotension permisiva, EVAR si posible."</span>',
    C4 + ["hemorragia", "aaa"])

add_qa(deck_c4,
    "Manejo: <b>Sangrado activo en paciente anticoagulado</b>",
    "<b>Warfarina</b>: vitamina K 10 mg IV + <b>concentrado de complejo protrombinico (CCP, 4 factores)</b> 25-50 U/kg.<br>"
    "<b>Heparina no fraccionada</b>: <b>protamina</b> 1 mg por 100 U.<br>"
    "<b>HBPM</b>: protamina parcial (60% reversion).<br>"
    "<b>Dabigatran</b>: <b>idarucizumab</b> 5 g IV.<br>"
    "<b>Apixaban/rivaroxaban</b>: <b>andexanet alfa</b> (si disponible) o CCP 4 factores 50 U/kg.<br>"
    "Soporte transfusional segun necesidad."
    '<span class="ecoe">ECOE: "Reversion segun anticoagulante + soporte transfusional."</span>',
    C4 + ["hemorragia", "anticoagulado"])

# --- ABDOMEN AGUDO (12)
add_qa(deck_c4,
    "Manejo: <b>Apendicitis no complicada</b>",
    "1) <b>NPO</b>, hidratacion IV, analgesia.<br>"
    "2) <b>Antibiotico perioperatorio</b>: cefoxitina o ceftriaxona + metronidazol (cobertura aerobios y anaerobios) 30-60 min preincision.<br>"
    "3) <b>Apendicectomia laparoscopica</b> (eleccion) dentro de las 24 h.<br>"
    "4) Alta temprana, sin ATB postoperatorio prolongado."
    '<span class="ecoe">ECOE: "NPO + ATB perioperatorio + apendicectomia laparoscopica."</span>',
    C4 + ["apendicitis"])

add_qa(deck_c4,
    "Manejo: <b>Apendicitis complicada con plastron/absceso</b>",
    "1) Si <b>absceso bien definido + paciente estable</b> -> <b>drenaje percutaneo</b> guiado por TAC + <b>ATB IV de amplio espectro</b>.<br>"
    "2) Apendicectomia de intervalo en 6-12 sem (controversial).<br>"
    "3) Si <b>peritonitis difusa</b> o falla de manejo conservador -> <b>laparotomia/laparoscopia urgente</b>.<br>"
    "4) ATB cobertura aerobios + anaerobios (piperacilina-tazobactam o ceftriaxona + metronidazol)."
    '<span class="ecoe">ECOE: "Plastron = drenaje + ATB; peritonitis = quirofano."</span>',
    C4 + ["apendicitis", "complicada"])

add_qa(deck_c4,
    "Manejo: <b>Colecistitis aguda</b> (Tokyo Guidelines 2018/2024)",
    "1) NPO, hidratacion IV, analgesia, antiemetico.<br>"
    "2) <b>Antibiotico IV</b>: comunitaria leve -> cefazolina o cefuroxima; comunitaria moderada/severa -> piperacilina-tazobactam o cefepime + metronidazol.<br>"
    "3) <b>Grado I-II (leve/moderada)</b>: <b>colecistectomia laparoscopica temprana &lt;72 h</b> del inicio.<br>"
    "4) <b>Grado III (severa)</b>: estabilizar + considerar <b>colecistostomia percutanea</b> si alto riesgo quirurgico, luego cirugia diferida.<br>"
    "5) Postop: dieta progresiva, alta temprana."
    '<span class="ecoe">ECOE: "ATB + colecistectomia laparoscopica temprana en Tokyo I/II."</span>',
    C4 + ["colecistitis"])

add_qa(deck_c4,
    "Manejo: <b>Colangitis aguda</b> (Tokyo Guidelines)",
    "1) Reanimacion + UCI segun severidad.<br>"
    "2) <b>Antibiotico IV temprano</b> (mismo espectro que colecistitis severa, cubrir gram negativos y anaerobios).<br>"
    "3) <b>Descompresion biliar urgente</b>:<br>"
    "&nbsp;&nbsp;&nbsp;- <b>CPRE con esfinterotomia + extraccion de litos/stent</b> (primera linea).<br>"
    "&nbsp;&nbsp;&nbsp;- Drenaje transhepatico percutaneo (PTC) si CPRE fallida.<br>"
    "&nbsp;&nbsp;&nbsp;- Cirugia si todo lo anterior falla.<br>"
    "4) <b>Grado III (sepsis severa) -> descompresion &lt;24 h</b>; colecistectomia despues de resolver.<br>"
    "5) Soporte hemodinamico + correccion coagulopatia."
    '<span class="ecoe">ECOE: "ATB + CPRE de descompresion urgente."</span>',
    C4 + ["colangitis"])

add_qa(deck_c4,
    "Manejo: <b>Pancreatitis aguda leve</b> (ACG 2024)",
    "1) NPO inicial breve; <b>reinicio temprano de dieta oral</b> (24-72 h) si tolera (mejora resultados).<br>"
    "2) <b>Cristaloides Ringer lactato</b>: bolo 10 mL/kg, luego 1.5 mL/kg/h; meta diuresis >0.5 mL/kg/h y lactato normal (evitar sobrecarga).<br>"
    "3) <b>Analgesia</b> (opioides si requerido).<br>"
    "4) Buscar causa: USG abdominal (litiasis), perfil hepatico, triglicericdos.<br>"
    "5) Si causa biliar y leve -> <b>colecistectomia en el mismo ingreso</b>.<br>"
    "6) <b>NO ATB</b> profilacticos rutinarios."
    '<span class="ecoe">ECOE: "Cristaloides moderados, dieta temprana, sin ATB profilactico."</span>',
    C4 + ["pancreatitis", "leve"])

add_qa(deck_c4,
    "Manejo: <b>Pancreatitis aguda severa</b>",
    "1) <b>UCI</b>, soporte hemodinamico, vigilancia de disfuncion organica.<br>"
    "2) Reanimacion cristaloides (Ringer lactato) moderada y guiada por metas.<br>"
    "3) Nutricion <b>enteral temprana</b> (sonda nasogastrica o nasoyeyunal) en 48-72 h - reduce mortalidad y traslocacion.<br>"
    "4) <b>ATB solo si infeccion documentada</b> de necrosis (carbapenem o quinolona + metronidazol).<br>"
    "5) Necrosis infectada -> <b>step-up approach</b>: drenaje percutaneo/endoscopico primero, necrosectomia minimamente invasiva despues.<br>"
    "6) Pancreatitis biliar con colangitis -> <b>CPRE urgente</b>."
    '<span class="ecoe">ECOE: "UCI, nutricion enteral temprana, step-up para necrosis infectada."</span>',
    C4 + ["pancreatitis", "severa"])

add_qa(deck_c4,
    "Manejo: <b>Diverticulitis no complicada</b> (ACG 2021)",
    "1) Confirmar con <b>TAC abdominal</b> y clasificar <b>Hinchey</b>.<br>"
    "2) <b>Hinchey I (flemón/absceso pequeño &lt;4 cm)</b>: ambulatorio si selectos.<br>"
    "3) <b>ATB controversial</b> en casos leves no complicados sin comorbilidades (estudios AVOD/DIABOLO): manejo selectivo, no rutinario.<br>"
    "4) Si se da ATB: amoxicilina-clavulanico o ciprofloxacino + metronidazol 7-10 dias.<br>"
    "5) Dieta liquida -> progresar segun tolerancia; colonoscopia a las 6-8 sem (descartar neoplasia)."
    '<span class="ecoe">ECOE: "Hinchey I = ATB selectivo, dieta liquida, colonoscopia tardia."</span>',
    C4 + ["diverticulitis", "no_complicada"])

add_qa(deck_c4,
    "Manejo: <b>Diverticulitis complicada (Hinchey II/III/IV)</b>",
    "<b>Hinchey II (absceso >4 cm)</b>: ATB IV + <b>drenaje percutaneo</b>; cirugia electiva si recurrente o fistula.<br>"
    "<b>Hinchey III (peritonitis purulenta)</b>: cirugia urgente - resección sigmoidea con anastomosis primaria + ileostomia derivativa, o procedimiento de <b>Hartmann</b>.<br>"
    "<b>Hinchey IV (peritonitis fecal)</b>: <b>Hartmann</b> de emergencia.<br>"
    "ATB amplio espectro IV (piperacilina-tazobactam o carbapenem).<br>"
    "Colonoscopia diferida (6-8 sem) si no se realizo cirugia."
    '<span class="ecoe">ECOE: "Hinchey III/IV = cirugia urgente; II = drenaje percutaneo + ATB."</span>',
    C4 + ["diverticulitis", "complicada"])

add_qa(deck_c4,
    "Manejo: <b>Perforacion de ulcera peptica</b>",
    "1) NPO, SNG, IBP IV, ATB (cefalosporina + metronidazol).<br>"
    "2) Reanimacion.<br>"
    "3) <b>Cirugia urgente</b>: <b>parche de Graham (omentopexia)</b> sobre la perforacion + lavado peritoneal.<br>"
    "4) Toma de muestras para H. pylori.<br>"
    "5) Postop: <b>IBP continuo + erradicacion de H. pylori</b> + control endoscopico a las 6-8 sem (descartar malignidad si ulcera gastrica).<br>"
    "6) Considerar cierre laparoscopico en centros con experiencia."
    '<span class="ecoe">ECOE: "Parche de Graham + IBP + erradicacion H. pylori."</span>',
    C4 + ["perforacion"])

add_qa(deck_c4,
    "Manejo: <b>Volvulo de sigmoides</b>",
    "1) Reanimacion + correccion electrolitos.<br>"
    "2) <b>Descompresion endoscopica</b> con rectosigmoidoscopia rigida o colonoscopia + colocacion de sonda rectal (tasa exito 70-90%).<br>"
    "3) <b>Sigmoidectomia electiva</b> en el mismo ingreso (alta tasa de recurrencia 50-90%).<br>"
    "4) Si signos de <b>peritonitis, perforacion o isquemia</b> -> <b>cirugia urgente</b> (resección + Hartmann o anastomosis)."
    '<span class="ecoe">ECOE: "Descompresion endoscopica + cirugia electiva mismo ingreso."</span>',
    C4 + ["volvulo"])

add_qa(deck_c4,
    "Manejo: <b>Isquemia mesenterica aguda</b>",
    "1) Reanimacion + corrección de acidosis + ATB amplio espectro.<br>"
    "2) <b>Angio-TC urgente</b> es la prueba de eleccion.<br>"
    "3) Heparinizacion temprana (excepto si sangrado).<br>"
    "4) <b>Laparotomia exploradora urgente</b>: revascularizar (embolectomia, bypass, stent intraoperatorio) + resección de intestino necrótico.<br>"
    "5) <b>Second-look</b> a las 24-48 h si viabilidad intestinal dudosa.<br>"
    "6) Tratar causa (FA -> anticoagulacion cronica)."
    '<span class="ecoe">ECOE: "Angio-TC, heparina, laparotomia con revascularizacion + second-look."</span>',
    C4 + ["isquemia"])

add_qa(deck_c4,
    "Manejo: <b>SOI por adherencias (parcial)</b>",
    "1) <b>NPO</b>, <b>SNG con aspiracion</b>, hidratacion IV, correccion electrolitos.<br>"
    "2) <b>Prueba terapeutica con Gastrografin</b> (oral o por SNG, 100 mL): diagnostica y terapeutica - si paso a colon en 24 h sugiere resolucion.<br>"
    "3) Vigilar 24-72 h.<br>"
    "4) Indicaciones de cirugia: <b>fallo del manejo conservador, signos de isquemia/estrangulacion (taquicardia, defensa, fiebre, leucocitosis, acidosis, asa cerrada en TAC)</b>, obstruccion completa.<br>"
    "5) En SOI por hernia incarcerada/estrangulada o cuerpo extrano -> cirugia."
    '<span class="ecoe">ECOE: "SOI parcial por adherencias = SNG + Gastrografin; cirugia si falla o isquemia."</span>',
    C4 + ["soi"])

# --- INFECCIONES (5)
add_qa(deck_c4,
    "Manejo: <b>Peritonitis secundaria</b>",
    "1) Reanimacion + soporte hemodinamico segun severidad (Surviving Sepsis 2021).<br>"
    "2) <b>Antibiotico IV empirico temprano (&lt;1 h)</b> de amplio espectro.<br>"
    "3) <b>Control quirurgico del foco</b> urgente (laparotomia/laparoscopia): reparar perforacion, drenar pus, lavar cavidad.<br>"
    "4) Toma de cultivos intraoperatorios para ajuste posterior.<br>"
    "5) Soporte en UCI segun necesidad; nutricion enteral temprana."
    '<span class="ecoe">ECOE: "ATB &lt;1 h + control quirurgico del foco urgente."</span>',
    C4 + ["peritonitis"])

add_qa(deck_c4,
    "Antibiotico empirico: <b>Peritonitis secundaria comunitaria</b> (IDSA 2010 / SIS 2017)",
    "<b>Leve-moderada</b>: cefoxitina o cefuroxima + metronidazol; o ticarcilina-clavulanico; o ertapenem; o ceftriaxona + metronidazol.<br>"
    "<b>Severa/alta gravedad</b>: piperacilina-tazobactam; o cefepime + metronidazol; o carbapenem (meropenem, imipenem).<br>"
    "Cobertura aerobios gram - y anaerobios.<br>"
    "Duracion: 4-7 dias tras control de foco adecuado (estudio STOP-IT)."
    '<span class="ecoe">ECOE: "Pip-tazo o cefa + metro para peritonitis comunitaria; ajuste por cultivo."</span>',
    C4 + ["atb", "peritonitis"])

add_qa(deck_c4,
    "Antibiotico empirico: <b>Peritonitis nosocomial / postquirurgica</b>",
    "<b>Carbapenem</b> (meropenem o imipenem) o piperacilina-tazobactam altas dosis.<br>"
    "<b>+/- vancomicina</b> (cobertura MRSA, enterococo).<br>"
    "<b>+/- antifungico (fluconazol o equinocandina)</b> si factores de riesgo (perforacion alta, inmunosuprimido, cultivos previos de Candida).<br>"
    "Ajustar segun cultivos y sensibilidades."
    '<span class="ecoe">ECOE: "Carbapenem + considero vancomicina y antifungico segun riesgo."</span>',
    C4 + ["atb", "peritonitis"])

add_qa(deck_c4,
    "Manejo: <b>Fascitis necrotizante</b>",
    "1) Reanimacion + UCI (sepsis frecuentemente).<br>"
    "2) <b>Desbridamiento quirurgico urgente y amplio</b> de todo tejido necrotico (no diferir por estudios).<br>"
    "3) <b>Antibiotico IV de amplio espectro inmediato</b>:<br>"
    "&nbsp;&nbsp;- <b>Carbapenem</b> (meropenem) o piperacilina-tazobactam<br>"
    "&nbsp;&nbsp;- <b>+ vancomicina o linezolid</b> (MRSA)<br>"
    "&nbsp;&nbsp;- <b>+ clindamicina</b> (antitoxina, inhibe sintesis proteica de gram+)<br>"
    "4) Re-desbridamientos seriados cada 24-48 h hasta tejido viable.<br>"
    "5) Considerar IgG IV en casos severos por estreptococo grupo A.<br>"
    "6) Soporte nutricional + cierre por colgajos posterior."
    '<span class="ecoe">ECOE: "Desbridamiento amplio YA + carbapenem + vanco + clinda."</span>',
    C4 + ["fascitis"])

add_qa(deck_c4,
    "Manejo: <b>Sepsis quirurgica - bundle hora-1</b> (Surviving Sepsis Campaign 2021)",
    "Dentro de la <b>primera hora</b> tras reconocimiento:<br>"
    "1) <b>Medir lactato</b>; remedir si >2 mmol/L.<br>"
    "2) <b>Hemocultivos antes de antibiotico</b> (si no retrasa).<br>"
    "3) <b>Antibiotico de amplio espectro</b> IV inmediato.<br>"
    "4) <b>Cristaloide 30 mL/kg</b> en hipotension o lactato >=4.<br>"
    "5) <b>Vasopresor (norepinefrina)</b> si hipotension no responde a cristaloides; meta PAM >=65 mmHg.<br>"
    "6) <b>Control del foco infeccioso</b> tan pronto sea factible (drenaje, cirugia).<br>"
    "7) Reevaluacion continua de perfusion (lactato, llenado capilar, diuresis)."
    '<span class="ecoe">ECOE: "Bundle hora 1: lactato + hemocultivos + ATB + 30 mL/kg + control de foco."</span>',
    C4 + ["sepsis", "bundle"])

# --- DDX (8)
add_qa(deck_c4,
    "DDx: <b>Dolor en fosa iliaca derecha (FID)</b>",
    "<b>Quirurgicas</b>: apendicitis aguda, hernia inguinal incarcerada, diverticulitis cecal, ileitis terminal (Crohn).<br>"
    "<b>Ginecologicas</b>: embarazo ectopico, ruptura/torsion de quiste ovarico derecho, EIP, endometriosis.<br>"
    "<b>Urologicas</b>: colico renal/ureteral, ITU, torsion testicular (irradiado).<br>"
    "<b>Medicas</b>: adenitis mesenterica, gastroenteritis, porfiria, cetoacidosis diabetica."
    '<span class="ecoe">ECOE: "DDx FID: apendicitis, ectopico, ovario, Crohn, colico ureteral."</span>',
    C4 + ["ddx", "fid"])

add_qa(deck_c4,
    "DDx: <b>Dolor en hipocondrio derecho (HD)</b>",
    "<b>Hepatobiliar</b>: colecistitis aguda, colico biliar, colangitis, hepatitis, absceso hepatico, sindrome de Fitz-Hugh-Curtis.<br>"
    "<b>Pulmonar</b>: neumonia basal derecha, empiema, embolia pulmonar.<br>"
    "<b>Cardiaco</b>: IAM inferior, pericarditis (irradiado).<br>"
    "<b>Otro</b>: ulcera duodenal perforada, pancreatitis (cabeza), apendicitis retrocecal, colon (angulo hepatico)."
    '<span class="ecoe">ECOE: "DDx HD: colecistitis, hepatitis, neumonia, IAM inferior."</span>',
    C4 + ["ddx", "hd"])

add_qa(deck_c4,
    "DDx: <b>Dolor epigastrico</b>",
    "<b>Digestivo</b>: ulcera peptica (gastrica/duodenal), perforacion peptica, gastritis, pancreatitis aguda, obstruccion gastroduodenal.<br>"
    "<b>Cardiaco</b>: <b>IAM inferior/posterior</b> (siempre descartar con ECG), pericarditis.<br>"
    "<b>Vascular</b>: <b>diseccion aortica</b>, AAA, isquemia mesenterica.<br>"
    "<b>Pulmonar</b>: neumonia basal."
    '<span class="ecoe">ECOE: "DDx epigastrio: pancreatitis, ulcera, IAM, diseccion aortica."</span>',
    C4 + ["ddx", "epigastrio"])

add_qa(deck_c4,
    "DDx: <b>Dolor en fosa iliaca izquierda (FII)</b>",
    "<b>Digestivo</b>: diverticulitis sigmoidea (la mas frecuente >50 a), colitis isquemica, neoplasia obstructiva, EII (colitis ulcerosa).<br>"
    "<b>Ginecologico</b>: quiste/torsion ovario izq, ectopico izq, EIP.<br>"
    "<b>Urologico</b>: colico ureteral, ITU.<br>"
    "<b>Vascular</b>: AAA roto puede irradiar."
    '<span class="ecoe">ECOE: "DDx FII: diverticulitis (mayor), ovario, colon."</span>',
    C4 + ["ddx", "fii"])

add_qa(deck_c4,
    "DDx: <b>Dolor en hipogastrio (mujer joven)</b>",
    "<b>Ginecologico</b>: <b>embarazo ectopico (siempre primero)</b>, EIP, torsion ovarica, ruptura de quiste, endometriosis, dismenorrea.<br>"
    "<b>Urologico</b>: cistitis, retencion urinaria.<br>"
    "<b>Digestivo</b>: apendicitis pelvica, EII, gastroenteritis.<br>"
    "Siempre solicitar <b>beta-hCG</b>."
    '<span class="ecoe">ECOE: "Mujer fertil + dolor bajo = beta-hCG SIEMPRE."</span>',
    C4 + ["ddx", "hipogastrio"])

add_qa(deck_c4,
    "DDx: <b>Abdomen en tabla (rigidez generalizada)</b>",
    "<b>Perforacion de viscera hueca</b> (ulcera, divertículo, apendicitis, intestino).<br>"
    "<b>Peritonitis difusa</b> (apendicitis perforada, diverticulitis perforada).<br>"
    "<b>Pancreatitis necrohemorragica grave</b>.<br>"
    "<b>Isquemia mesenterica con infarto</b>.<br>"
    "<b>Ruptura de viscera solida con peritonitis quimica</b> (bazo, higado en trauma).<br>"
    "Conducta: <b>laparotomia urgente</b> tras estabilizacion."
    '<span class="ecoe">ECOE: "Abdomen en tabla = peritonitis difusa = quirofano."</span>',
    C4 + ["ddx", "tabla"])

add_qa(deck_c4,
    "DDx: <b>Hematemesis</b>",
    "<b>Ulcera peptica</b> (mas frecuente, 50%).<br>"
    "<b>Varices esofagicas/gastricas</b> (cirrosis).<br>"
    "<b>Sindrome de Mallory-Weiss</b> (vomito previo, desgarro union esofagogastrica).<br>"
    "<b>Esofagitis erosiva / gastritis erosiva</b>.<br>"
    "<b>Neoplasia gastrica o esofagica</b>.<br>"
    "<b>Lesion de Dieulafoy</b> (vaso submucoso aberrante).<br>"
    "<b>Fistula aortoenterica</b> (rara, mortal; antecedente de cirugia aortica)."
    '<span class="ecoe">ECOE: "DDx hematemesis: ulcera (1ra), varices, Mallory-Weiss."</span>',
    C4 + ["ddx", "hematemesis"])

add_qa(deck_c4,
    "DDx: <b>Mujer fertil con dolor abdominal bajo agudo</b>",
    "1) <b>Embarazo ectopico</b> (roto vs no roto) - beta-hCG SIEMPRE.<br>"
    "2) <b>Torsion ovarica</b> (dolor subito intenso, USG con flujo Doppler ausente).<br>"
    "3) <b>Ruptura de quiste ovarico</b> (dolor subito, liquido libre).<br>"
    "4) <b>EIP / absceso tuboovarico</b> (fiebre, flujo, dolor a movilizacion cervical).<br>"
    "5) <b>Apendicitis</b>.<br>"
    "6) <b>Endometriosis</b> (cronica).<br>"
    "7) <b>ITU/pielonefritis</b>."
    '<span class="ecoe">ECOE: "Mujer fertil + dolor bajo: ectopico, torsion, ruptura, EIP, apendicitis."</span>',
    C4 + ["ddx", "mujer"])

# --- DECISION QUIRURGICA (6)
add_qa(deck_c4,
    "Decision: <b>Colico biliar vs colecistitis vs colangitis vs pancreatitis biliar</b>",
    "<b>Colico biliar</b>: dolor postprandial graso, <b>SIN fiebre, SIN leucocitosis</b>, autolimitado (&lt;6 h); USG con litos sin colecistitis. <b>Manejo</b>: colecistectomia electiva.<br>"
    "<b>Colecistitis</b>: + fiebre + Murphy + leucocitosis + USG con criterios. <b>Manejo</b>: colecistectomia temprana &lt;72 h + ATB.<br>"
    "<b>Colangitis</b>: triada de Charcot. <b>Manejo</b>: ATB + CPRE de descompresion urgente.<br>"
    "<b>Pancreatitis biliar</b>: lipasa elevada + dolor en cinturon. <b>Manejo</b>: soporte; CPRE si colangitis asociada; colecistectomia mismo ingreso si leve."
    '<span class="ecoe">ECOE: "Distingo los 4 por fiebre, ictericia, lipasa y Murphy."</span>',
    C4 + ["decision", "biliar"])

add_qa(deck_c4,
    "Decision: <b>Quirofano YA (sin demora)</b>",
    "<b>Indicaciones de cirugia inmediata</b>:<br>"
    "- Hemorragia incontrolable o inestabilidad hemodinamica persistente.<br>"
    "- Trauma penetrante abdominal inestable o con evisceracion.<br>"
    "- Peritonitis generalizada (abdomen en tabla, neumoperitoneo).<br>"
    "- Perforacion de viscera hueca con sepsis.<br>"
    "- Isquemia mesenterica con infarto.<br>"
    "- AAA roto.<br>"
    "- Volvulo con sospecha de necrosis.<br>"
    "- Fascitis necrotizante.<br>"
    "- Hernia estrangulada.<br>"
    "- Embarazo ectopico roto inestable."
    '<span class="ecoe">ECOE: "Reconozco indicacion absoluta de cirugia inmediata."</span>',
    C4 + ["decision", "urgente"])

add_qa(deck_c4,
    "Decision: <b>Diferible / manejo conservador inicial</b>",
    "Procesos que pueden manejarse inicialmente sin cirugia:<br>"
    "- <b>Apendicitis con plastron/absceso</b> bien definido (drenaje percutaneo + ATB).<br>"
    "- <b>Diverticulitis no complicada</b> (Hinchey I).<br>"
    "- <b>SOI parcial por adherencias</b> sin isquemia (SNG + Gastrografin).<br>"
    "- <b>Pancreatitis aguda</b> (manejo medico).<br>"
    "- <b>Colecistitis Tokyo III alto riesgo</b> (colecistostomia + cirugia diferida).<br>"
    "- <b>Trauma cerrado estable con FAST(-)</b> (observacion)."
    '<span class="ecoe">ECOE: "Selecciono pacientes con criterios para manejo conservador inicial."</span>',
    C4 + ["decision", "conservador"])

add_qa(deck_c4,
    "Decision: <b>USG vs TAC como primera imagen</b>",
    "<b>USG primero</b>: HD (colecistitis), embarazo (FAST/ginecologico), pediatricos, sospecha apendicitis en mujer joven, AAA cribado.<br>"
    "<b>TAC primero (con contraste IV)</b>: trauma cerrado estable, abdomen agudo en adulto, sospecha de perforacion/isquemia/diverticulitis, sospecha pancreatitis grave (a las 72-96 h), AAA confirmacion.<br>"
    "<b>FAST</b>: trauma a la cama, embarazada, niño - rapido para liquido libre.<br>"
    "<b>NO TAC primario</b>: hipersensibilidad severa al contraste, embarazo (relativo), inestabilidad hemodinamica (mejor quirofano)."
    '<span class="ecoe">ECOE: "USG si HD/gineco/joven; TAC en trauma estable y abdomen agudo en adulto."</span>',
    C4 + ["decision", "imagen"])

add_qa(deck_c4,
    "Decision: <b>Cuando NO operar</b>",
    "Patologias que NO son quirurgicas (al menos en agudo):<br>"
    "- <b>Pancreatitis aguda</b> (manejo medico; cirugia solo para necrosis infectada step-up).<br>"
    "- <b>Gastroenteritis aguda</b>.<br>"
    "- <b>EII no complicada</b> (Crohn, colitis ulcerosa - tratamiento medico primero).<br>"
    "- <b>Adenitis mesenterica</b>.<br>"
    "- <b>Sindrome de intestino irritable</b>.<br>"
    "- <b>Dolor abdominal indiferenciado</b> en paciente estable sin signos de alarma (observacion + reevaluacion).<br>"
    "- <b>Apendicitis cronica/atipica</b> en paciente seleccionable (manejo con ATB en estudios)."
    '<span class="ecoe">ECOE: "No todo abdomen agudo es quirurgico; identifico cuando observar."</span>',
    C4 + ["decision", "no_operar"])

add_qa(deck_c4,
    "Preparacion preoperatoria del paciente quirurgico urgente",
    "1) <b>NPO</b>.<br>"
    "2) <b>SNG</b> si obstruccion o vomito persistente.<br>"
    "3) <b>Sonda Foley</b> (valorar contraindicaciones).<br>"
    "4) <b>Dos accesos vasculares</b>; cristaloides + hemoderivados segun necesidad.<br>"
    "5) <b>Tipificacion + cruce</b>; pruebas preoperatorias (BH, QS, electrolitos, TP/TPT, ECG).<br>"
    "6) <b>Antibiotico profilactico</b> 30-60 min preincision.<br>"
    "7) <b>Profilaxis tromboembolica</b> (HBPM a dosis profilactica, salvo sangrado activo).<br>"
    "8) Correccion de electrolitos y coagulopatia.<br>"
    "9) Consentimiento informado.<br>"
    "10) Marcado quirurgico + check-list de seguridad (OMS)."
    '<span class="ecoe">ECOE: "Preparo paciente: NPO, accesos, ATB, profilaxis VTE, consentimiento."</span>',
    C4 + ["preop"])

# --- ESPECIALES (5)
add_qa(deck_c4,
    "Manejo: <b>Torsion testicular</b>",
    "1) <b>Sospecha clinica = ventana de 6 h</b> para salvar el testiculo.<br>"
    "2) Si dispoinble inmediatamente, USG Doppler escrotal (flujo ausente confirma).<br>"
    "3) Si no hay USG inmediato o alta sospecha -> <b>exploracion quirurgica urgente</b>.<br>"
    "4) Intraoperatorio: detorsion + valoracion de viabilidad + <b>orquidopexia bilateral</b> (testiculo contralateral fijado por riesgo de torsion futura).<br>"
    "5) Si no viable: orquiectomia."
    '<span class="ecoe">ECOE: "Torsion testicular = exploracion urgente; orquidopexia bilateral."</span>',
    C4 + ["torsion"])

add_qa(deck_c4,
    "Manejo: <b>Diseccion aortica tipo A vs tipo B</b>",
    "<b>Tipo A (aorta ascendente, Stanford)</b>: <b>cirugia urgente</b> (reemplazo aorta ascendente +/- arco) - mortalidad sin cirugia ~1%/h.<br>"
    "<b>Tipo B (descendente, distal a subclavia izquierda)</b>: <b>manejo medico</b>:<br>"
    "&nbsp;&nbsp;- <b>Control de PA y FC</b>: <b>esmolol o labetalol IV</b> (meta FC &lt;60, PAS 100-120).<br>"
    "&nbsp;&nbsp;- Despues vasodilatador (nitroprusiato) si requiere.<br>"
    "&nbsp;&nbsp;- Analgesia (morfina).<br>"
    "&nbsp;&nbsp;- Cirugia/TEVAR solo si complicaciones (isquemia visceral, ruptura, progresion)."
    '<span class="ecoe">ECOE: "Tipo A = cirugia urgente; Tipo B = control FC y PA con betabloqueador."</span>',
    C4 + ["diseccion"])

add_qa(deck_c4,
    "Manejo: <b>Hemorragia subaracnoidea (HSA) por aneurisma roto</b>",
    "1) ABCDE; intubacion si Glasgow &lt;=8.<br>"
    "2) <b>TAC simple urgente</b>; si negativa y alta sospecha -> <b>puncion lumbar</b> (xantocromia).<br>"
    "3) Confirmar aneurisma: <b>angio-TC</b> o angiografia.<br>"
    "4) <b>Control de PA</b> (meta PAS &lt;160) con labetalol/nicardipino.<br>"
    "5) <b>Nimodipino 60 mg VO/SNG cada 4 h por 21 dias</b> (prevenir vasoespasmo).<br>"
    "6) <b>Clipaje quirurgico o coiling endovascular</b> precoz (&lt;72 h) por neurocirugia/neurorradiologia.<br>"
    "7) Vigilar complicaciones: vasoespasmo (5-14 d), hidrocefalia, resangrado."
    '<span class="ecoe">ECOE: "TAC + nimodipino + coiling/clipaje precoz."</span>',
    C4 + ["hsa"])

add_qa(deck_c4,
    "Manejo: <b>Embarazo ectopico estable (no roto)</b>",
    "<b>Metotrexato</b> (medico): si cumple criterios - beta-hCG &lt;5000, sin actividad cardiaca, masa &lt;3.5 cm, paciente estable, asintomatica, capacidad de seguimiento, sin contraindicaciones.<br>"
    "Dosis: 50 mg/m2 IM dosis unica; vigilar beta-hCG dias 4 y 7 (caida >=15%).<br>"
    "<b>Conducta expectante</b>: ectopico muy pequeno con beta-hCG en descenso.<br>"
    "<b>Cirugia (laparoscopia)</b>: si falla metotrexato, ectopico >3.5 cm, dolor severo, deseo de seguimiento limitado, contraindicaciones a metotrexato:<br>"
    "&nbsp;&nbsp;- <b>Salpingostomia</b> (conservadora; si desea fertilidad y trompa contralateral danada).<br>"
    "&nbsp;&nbsp;- <b>Salpingectomia</b> (si trompa contralateral sana o tubaria muy danada)."
    '<span class="ecoe">ECOE: "Ectopico estable: metotrexato si criterios, laparoscopia si no."</span>',
    C4 + ["ectopico"])

add_qa(deck_c4,
    "Profilaxis antibiotica preoperatoria: <b>principios y ejemplos</b>",
    "<b>Principios</b>:<br>"
    "- Administrar <b>30-60 min antes de incision</b>.<br>"
    "- Cobertura de flora esperada segun cirugia.<br>"
    "- <b>Una sola dosis</b> en la mayoria; repetir si cirugia >4 h o sangrado >1.5 L.<br>"
    "- No continuar postoperatorio salvo infeccion establecida.<br>"
    "<b>Ejemplos</b>:<br>"
    "- Limpia (mama, hernia, vascular): <b>cefazolina</b>.<br>"
    "- Limpia-contaminada (colecistectomia, apendicectomia no perforada, colorrectal): <b>cefazolina + metronidazol</b> o cefoxitina.<br>"
    "- Colorrectal: <b>preparacion mecanica + ATB oral (neomicina + metronidazol) + cefazolina IV</b>.<br>"
    "- Contaminada/sucia: tratamiento ATB, no solo profilaxis."
    '<span class="ecoe">ECOE: "Profilaxis ATB 30-60 min preincision, una dosis, segun tipo de cirugia."</span>',
    C4 + ["profilaxis"])


# ============================================================
# Build packages
# ============================================================
def build():
    decks = [
        (deck_c1, "Cirugia_Adulto_Capa1.apkg"),
        (deck_c2, "Cirugia_Adulto_Capa2.apkg"),
        (deck_c3, "Cirugia_Adulto_Capa3.apkg"),
        (deck_c4, "Cirugia_Adulto_Capa4.apkg"),
    ]
    for d, fname in decks:
        pkg = genanki.Package(d)
        out = os.path.join(OUTPUT_DIR, fname)
        pkg.write_to_file(out)
        print(f"  -> {fname} ({len(d.notes)} notas)")

    combined = genanki.Package([deck_c1, deck_c2, deck_c3, deck_c4])
    combined_out = os.path.join(OUTPUT_DIR, "Cirugia_Adulto_TODOS.apkg")
    combined.write_to_file(combined_out)
    total = sum(len(d.notes) for d in [deck_c1, deck_c2, deck_c3, deck_c4])
    print(f"  -> Cirugia_Adulto_TODOS.apkg ({total} notas totales)")


if __name__ == "__main__":
    build()
