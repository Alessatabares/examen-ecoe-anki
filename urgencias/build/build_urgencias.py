"""Generador de los 4 subdecks Anki para ECOE de Urgencias (Medicina de Emergencias).

Capa 1 - Flujo Macro (Cloze)               - secuencia y bifurcaciones, sin numeros
Capa 2 - Componentes (Cloze)               - numeros, dosis, tiempos, criterios
Capa 3 - Ejes (Cloze)                      - fisiopatologia -> presentacion -> pista -> manejo
Capa 4 - Manejo y Dx Diferencial (Q&A)     - casos integradores tipo examen

Guias base (verificadas may-2026):
ACC/AHA 2025 SCA, AHA/ASA 2026 ictus, Surviving Sepsis 2021,
JTFPP 2023 anafilaxia, ADA/EASD 2024 crisis hiperglucemicas,
AHA 2025 ACLS, NCS/AES status epileptico, ACC/AHA 2025 HTA,
GINA/GOLD 2025, CHEST/ESC TEP, UpToDate.

Filosofia (estilo Musel): primero el algoritmo macro, luego los numeros,
luego los ejes transversales, luego la integracion. Una idea por tarjeta.
Paro/ACLS y Trauma van CORTOS: detalle completo en los decks RCP y Cirugia.
"""
import os
import json
import random
import genanki

HERE = os.path.dirname(__file__)
OUTPUT_DIR = os.path.join(HERE, "..", "output")
IDS_PATH = os.path.join(HERE, "..", "..", "ids.json")
os.makedirs(OUTPUT_DIR, exist_ok=True)

MODEL_CLOZE_ID = 1607392319
MODEL_QA_ID = 1607392320

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

GUIA = ("ACC/AHA 2025 SCA + AHA/ASA 2026 ictus + Surviving Sepsis 2021 + "
        "JTFPP 2023 anafilaxia + ADA/EASD 2024 crisis hiperglucemicas + AHA 2025 ACLS + "
        "NCS/AES + ACC/AHA 2025 HTA + GINA/GOLD 2025 + CHEST/ESC TEP + UpToDate")

DECK_NAMES = {
    1: "Urgencias Adulto::Capa 1 - Flujo Macro",
    2: "Urgencias Adulto::Capa 2 - Componentes",
    3: "Urgencias Adulto::Capa 3 - Ejes",
    4: "Urgencias Adulto::Capa 4 - Manejo y Diagnostico Diferencial",
}
# deck_ids estables propuestos; se validan/reasignan contra ids.json
DECK_IDS = {1: 1311472058, 2: 1322556677, 3: 1433667788, 4: 1544778899}

# ---- cargar ids.json y resolver deck_ids sin colision ----
with open(IDS_PATH, encoding="utf-8") as f:
    ids = json.load(f)
existing = {d["deck_id"] for d in ids["decks"]}


def resolve_deck_id(capa):
    match = [d for d in ids["decks"] if d.get("tema") == "Urgencias"
             and d.get("audiencia") == "Adulto" and d.get("capa") == capa]
    if match:
        return match[0]["deck_id"]
    did = DECK_IDS[capa]
    others = existing - {DECK_IDS[c] for c in DECK_IDS if c != capa}
    while did in others:
        did = random.randrange(1 << 30, 1 << 31)
    return did


for c in (1, 2, 3, 4):
    DECK_IDS[c] = resolve_deck_id(c)

deck1 = genanki.Deck(DECK_IDS[1], DECK_NAMES[1])
deck2 = genanki.Deck(DECK_IDS[2], DECK_NAMES[2])
deck3 = genanki.Deck(DECK_IDS[3], DECK_NAMES[3])
deck4 = genanki.Deck(DECK_IDS[4], DECK_NAMES[4])

BASE_TAGS = ["urgencias", "ecoe"]


def cz(deck, key, text, extra, tags):
    # El campo cloze no lleva HTML intencional: escapamos < y > para que
    # comparaciones como "pH <7.3" o "<=90 min" no se lean como etiquetas.
    text = text.replace("<", "&lt;").replace(">", "&gt;")
    deck.add_note(genanki.Note(model=model_cloze, fields=[text, extra],
                               tags=BASE_TAGS + tags, guid=genanki.guid_for(key)))


def qa(deck, key, front, back, tags):
    deck.add_note(genanki.Note(model=model_qa, fields=[front, back],
                               tags=BASE_TAGS + tags, guid=genanki.guid_for(key)))


# ============================================================
# CAPA 1 - FLUJO MACRO (sin numeros)
# ============================================================
T = ["capa1", "sca", "cardiovascular"]
cz(deck1, "urg-c1-sca-1",
   "Dolor toracico isquemico -> primer paso {{c1::ECG de 12 derivaciones inmediato}} -> define la via de manejo",
   '<span class="ecoe">ECOE: "Ante dolor toracico, lo primero es un ECG en menos de 10 minutos y monitorizacion."</span>', T + ["ecoe"])
cz(deck1, "urg-c1-sca-2",
   "ECG con elevacion del ST = {{c1::STEMI}} -> objetivo {{c2::reperfusion urgente}} (ICP primaria preferida; fibrinolisis si no hay cateterismo a tiempo)",
   '<span class="contraste">Sin elevacion del ST no se descarta infarto: la troponina y la clinica reclasifican.</span>', T)
cz(deck1, "urg-c1-sca-3",
   "ECG sin elevacion del ST + troponina/clinica compatibles -> {{c1::SCASEST}} -> estratificar riesgo y decidir estrategia {{c2::invasiva vs conservadora}}",
   "", T)
cz(deck1, "urg-c1-sca-4",
   "Tratamiento base de todo SCA: {{c1::antiagregacion doble}} + {{c2::anticoagulacion}} + {{c3::estatina de alta intensidad}}",
   '<span class="viva">ACC/AHA 2025: acceso radial preferido en ICP; revascularizacion completa.</span>', T)

T = ["capa1", "acv", "neurologico"]
cz(deck1, "urg-c1-acv-1",
   "Deficit neurologico subito -> registrar {{c1::hora de inicio / ultima vez visto bien}} + {{c2::TAC simple urgente}} para excluir hemorragia",
   '<span class="ecoe">ECOE: "Activo codigo ictus, confirmo hora de inicio y pido TAC craneal urgente."</span>', T + ["ecoe"])
cz(deck1, "urg-c1-acv-2",
   "TAC sin hemorragia + dentro de ventana -> candidato a {{c1::trombolisis IV}}; antes descartar {{c2::contraindicaciones}}",
   '<span class="viva">AHA/ASA 2026: tenecteplasa 0.25 mg/kg es clase 1, equivalente a alteplasa.</span>', T)
cz(deck1, "urg-c1-acv-3",
   "Oclusion de gran vaso -> valorar {{c1::trombectomia mecanica}} (ademas de / en lugar de la trombolisis)",
   "", T)

T = ["capa1", "sepsis", "infeccioso"]
cz(deck1, "urg-c1-sepsis-1",
   "Infeccion sospechada + disfuncion organica -> {{c1::sepsis}}; si requiere vasopresores + lactato alto pese a liquidos -> {{c2::shock septico}}", "", T)
cz(deck1, "urg-c1-sepsis-2",
   "Bundle hora-1: {{c1::lactato}}, {{c2::hemocultivos antes del antibiotico}}, {{c3::antibiotico de amplio espectro}} y {{c4::cristaloides}}",
   '<span class="ecoe">ECOE: "Tomo hemocultivos, inicio antibiotico de amplio espectro en la primera hora y reanimo con cristaloides."</span>', T + ["ecoe"])
cz(deck1, "urg-c1-sepsis-3",
   "Hipotension que no responde a liquidos -> iniciar {{c1::vasopresor (noradrenalina)}}", "", T)

T = ["capa1", "anafilaxia", "alergia"]
cz(deck1, "urg-c1-anafilaxia-1",
   "Reaccion alergica con compromiso {{c1::respiratorio, circulatorio o de dos sistemas}} tras un alergeno -> anafilaxia", "", T)
cz(deck1, "urg-c1-anafilaxia-2",
   "Farmaco mas importante y primero: {{c1::adrenalina IM}} en cara anterolateral del muslo (no retrasar)",
   '<span class="ecoe">ECOE: "Es anafilaxia: administro adrenalina intramuscular de inmediato."</span>'
   '<span class="redflag">No usar la adrenalina como prueba diagnostica ni sustituirla por antihistaminicos.</span>', T + ["ecoe"])
cz(deck1, "urg-c1-anafilaxia-3",
   "Tras la adrenalina: {{c1::oxigeno}}, {{c2::liquidos}} y decubito; antihistaminicos y corticoides son {{c3::de segunda linea}}", "", T)

T = ["capa1", "cad", "ehh", "endocrino"]
cz(deck1, "urg-c1-hiperglucemia-1",
   "Hiperglucemia + acidosis + cetonas = {{c1::CAD}}; hiperglucemia muy alta + hiperosmolaridad sin cetoacidosis marcada = {{c2::EHH}}",
   '<span class="viva">ADA/EASD 2024: el beta-hidroxibutirato entra en los criterios diagnosticos y de resolucion.</span>', T)
cz(deck1, "urg-c1-hiperglucemia-2",
   "Pilares del manejo: {{c1::liquidos IV}}, {{c2::insulina}}, {{c3::reposicion de potasio}} y corregir el desencadenante",
   '<span class="ecoe">ECOE: "Inicio fluidoterapia, repongo potasio segun niveles e inicio insulina."</span>', T + ["ecoe"])
cz(deck1, "urg-c1-hiperglucemia-3",
   "Antes de iniciar insulina hay que vigilar el {{c1::potasio}}: si esta bajo, {{c2::reponer primero}}",
   '<span class="redflag">La insulina mete el potasio a la celula: arrancarla con hipopotasemia puede causar arritmia.</span>', T)

T = ["capa1", "status_epileptico", "neurologico"]
cz(deck1, "urg-c1-status-1",
   "Crisis > 5 min o crisis repetidas sin recuperar la conciencia -> {{c1::status epileptico}} -> tratar de inmediato",
   '<span class="ecoe">ECOE: "ABC, glucemia capilar y benzodiacepina como primera linea."</span>', T + ["ecoe"])
cz(deck1, "urg-c1-status-2",
   "Primera linea: {{c1::benzodiacepina}}; si persiste -> segunda linea {{c2::antiepileptico IV (levetiracetam / valproato / fosfenitoina)}}", "", T)
cz(deck1, "urg-c1-status-3",
   "Status refractario (no cede a 1a y 2a linea) -> {{c1::sedacion/anestesia e intubacion}} en UCI", "", T)

T = ["capa1", "emergencia_htn", "cardiovascular"]
cz(deck1, "urg-c1-htn-1",
   "PA muy elevada + {{c1::dano agudo de organo blanco}} = emergencia hipertensiva (vs urgencia, que es sin dano)", "", T)
cz(deck1, "urg-c1-htn-2",
   "Manejo: {{c1::antihipertensivo IV titulable}} con reduccion {{c2::controlada y gradual}} de la presion",
   '<span class="redflag">Bajar la PA bruscamente puede causar hipoperfusion (cerebral, coronaria, renal).</span>', T)
cz(deck1, "urg-c1-htn-3",
   "El objetivo y la velocidad de bajada dependen del {{c1::organo afectado}} (excepcion: diseccion aortica, donde se baja rapido)", "", T)

T = ["capa1", "asma", "epoc", "respiratorio"]
cz(deck1, "urg-c1-broncoespasmo-1",
   "Exacerbacion de asma/EPOC -> {{c1::oxigeno}} + {{c2::broncodilatadores inhalados (SABA +/- anticolinergico)}} + {{c3::corticoide sistemico}}", "", T)
cz(deck1, "urg-c1-broncoespasmo-2",
   "Signos de gravedad o fatiga respiratoria -> valorar {{c1::soporte ventilatorio (VNI o intubacion)}}",
   '<span class="redflag">Torax silente, somnolencia o normocapnia que sube = fatiga inminente.</span>', T)
cz(deck1, "urg-c1-broncoespasmo-3",
   "En EPOC, dar oxigeno con {{c1::objetivo de SatO2 controlado}} para no abolir el estimulo respiratorio", "", T)

T = ["capa1", "tep", "respiratorio", "cardiovascular"]
cz(deck1, "urg-c1-tep-1",
   "Disnea o dolor pleuritico subito + factores de riesgo -> estimar {{c1::probabilidad clinica}} (Wells/Geneva)", "", T)
cz(deck1, "urg-c1-tep-2",
   "Probabilidad baja -> {{c1::dimero D}}; probabilidad alta o paciente inestable -> {{c2::angioTAC}} (o eco a pie de cama si inestable)", "", T)
cz(deck1, "urg-c1-tep-3",
   "TEP de alto riesgo (inestable) -> {{c1::trombolisis}}; TEP estable -> {{c2::anticoagulacion}}", "", T)

T = ["capa1", "intoxicaciones", "toxicologia"]
cz(deck1, "urg-c1-tox-1",
   "Paciente intoxicado -> primero {{c1::ABC y glucemia}}, luego identificar el {{c2::toxidrome}}", "", T)
cz(deck1, "urg-c1-tox-2",
   "Antidotos clave: paracetamol -> {{c1::N-acetilcisteina}}; opioides -> {{c2::naloxona}}; benzodiacepinas -> {{c3::flumazenil (con cautela)}}",
   '<span class="contraste">El flumazenil puede precipitar convulsiones en dependientes o coingesta de proconvulsivantes.</span>', T)
cz(deck1, "urg-c1-tox-3",
   "Toxidrome colinergico -> antidoto {{c1::atropina}}; reconocer el patron (colinergico / simpaticomimetico / anticolinergico / opioide / sedante)", "", T)

T = ["capa1", "shock", "cardiovascular"]
cz(deck1, "urg-c1-shock-1",
   "Shock = hipoperfusion tisular; los 4 tipos: {{c1::hipovolemico}}, {{c2::cardiogenico}}, {{c3::distributivo}} y {{c4::obstructivo}}", "", T)
cz(deck1, "urg-c1-shock-2",
   "Abordaje inicial comun a todo shock: {{c1::ABC}}, accesos, {{c2::liquidos}} y buscar/tratar la causa", "", T)

T = ["capa1", "paro", "rcp_enlace"]
cz(deck1, "urg-c1-paro-1",
   "Paro cardiaco -> {{c1::RCP de alta calidad}} + {{c2::desfibrilar si el ritmo es desfibrilable}} (detalle completo en el deck RCP)", "", T)
cz(deck1, "urg-c1-paro-2",
   "Ritmos desfibrilables = {{c1::FV / TV sin pulso}}; no desfibrilables = {{c2::asistolia / AESP}}", "", T)

T = ["capa1", "trauma", "cirugia_enlace"]
cz(deck1, "urg-c1-trauma-1",
   "Politraumatizado -> {{c1::ABCDE del ATLS}} en orden (detalle completo en el deck Cirugia)", "", T)
cz(deck1, "urg-c1-trauma-2",
   "Hipotension en el paciente traumatizado = {{c1::hemorragia}} hasta demostrar lo contrario", "", T)

# ============================================================
# CAPA 2 - COMPONENTES (numeros, dosis, tiempos, criterios)
# ============================================================
T = ["capa2", "sca", "cardiovascular"]
cz(deck2, "urg-c2-sca-1",
   "Tiempos STEMI: ECG en {{c1::<=10 min}} desde llegada; ICP primaria puerta-balon {{c2::<=90 min}} (si traslado, <=120 min); fibrinolisis puerta-aguja {{c3::<=30 min}}", "", T)
cz(deck2, "urg-c2-sca-2",
   "Carga antiagregante: AAS {{c1::162-325 mg}} masticada + inhibidor P2Y12 ({{c2::ticagrelor, prasugrel o clopidogrel}}); DAPT {{c3::>=12 meses}} si no hay alto riesgo de sangrado", "", T)
cz(deck2, "urg-c2-sca-3",
   "Troponina de {{c1::alta sensibilidad}} seriada (0 y {{c2::1-2 h}}) para reclasificar SCASEST",
   '<span class="viva">ACC/AHA 2025: estatina de alta intensidad +/- ezetimibe desde el ingreso.</span>', T)

T = ["capa2", "acv", "neurologico"]
cz(deck2, "urg-c2-acv-1",
   "Ventana de trombolisis IV: {{c1::4.5 h}} desde el inicio; trombectomia hasta {{c2::24 h}} en oclusion de gran vaso seleccionada por imagen", "", T)
cz(deck2, "urg-c2-acv-2",
   "Dosis: alteplasa {{c1::0.9 mg/kg}} (max 90 mg, 10% en bolo) o tenecteplasa {{c2::0.25 mg/kg}} (max 25 mg en bolo unico)", "", T)
cz(deck2, "urg-c2-acv-3",
   "La PA debe ser {{c1::<185/110 mmHg}} antes de trombolisar; glucemia objetivo {{c2::140-180 mg/dL}}",
   '<span class="redflag">Si la PA no baja de 185/110 de forma segura, no se puede dar el fibrinolitico.</span>', T)

T = ["capa2", "sepsis", "infeccioso"]
cz(deck2, "urg-c2-sepsis-1",
   "Reanimacion: cristaloides {{c1::30 mL/kg}} en las primeras {{c2::3 h}}; antibiotico de amplio espectro idealmente en {{c3::1 h}}", "", T)
cz(deck2, "urg-c2-sepsis-2",
   "Objetivo de presion: {{c1::PAM >=65 mmHg}}; vasopresor de 1a linea {{c2::noradrenalina}}, se anade {{c3::vasopresina}} si no se alcanza", "", T)
cz(deck2, "urg-c2-sepsis-3",
   "Guiar la reanimacion por {{c1::aclaramiento de lactato}} y respuesta dinamica a volumen (no por PVC aislada)", "", T)

T = ["capa2", "anafilaxia", "alergia"]
cz(deck2, "urg-c2-anafilaxia-1",
   "Adrenalina IM adulto: {{c1::0.3-0.5 mg}} de la solucion {{c2::1 mg/mL}}; repetir cada {{c3::5-15 min}} si no responde", "", T)
cz(deck2, "urg-c2-anafilaxia-2",
   "Adrenalina IM pediatrica: {{c1::0.01 mg/kg}} (max 0.3-0.5 mg); refractaria -> {{c2::adrenalina IV en infusion}}", "", T)
cz(deck2, "urg-c2-anafilaxia-3",
   "Observar tras la resolucion por riesgo de reaccion {{c1::bifasica}}",
   '<span class="redflag">No dar de alta inmediata: la fase bifasica puede aparecer horas despues.</span>', T)

T = ["capa2", "cad", "ehh", "endocrino"]
cz(deck2, "urg-c2-cad-1",
   "Criterios de CAD: glucosa >{{c1::250 mg/dL}}, pH <{{c2::7.3}}, bicarbonato <{{c3::18}} y cetonemia/beta-OH >={{c4::3.0 mmol/L}} con anion gap elevado", "", T)
cz(deck2, "urg-c2-ehh-1",
   "Criterios de EHH: glucosa >{{c1::600 mg/dL}}, osmolaridad efectiva >{{c2::320 mOsm/kg}}, pH >7.3 y cetosis minima", "", T)
cz(deck2, "urg-c2-cad-2",
   "Insulina IV {{c1::0.1 U/kg/h}}; anadir {{c2::dextrosa}} cuando la glucosa baje a ~{{c3::200-250 mg/dL}} para seguir corrigiendo cetosis", "", T)
cz(deck2, "urg-c2-cad-3",
   "Potasio: si <{{c1::3.3}} -> reponer y NO iniciar insulina aun; {{c2::3.3-5.2}} -> anadir K a los sueros; >5.2 -> solo vigilar", "", T)

T = ["capa2", "status_epileptico", "neurologico"]
cz(deck2, "urg-c2-status-1",
   "1a linea: lorazepam {{c1::0.1 mg/kg IV}} (max 4 mg/dosis), o midazolam IM {{c2::10 mg}} si no hay via", "", T)
cz(deck2, "urg-c2-status-2",
   "2a linea IV: levetiracetam {{c1::60 mg/kg}} (max 4500 mg), valproato {{c2::40 mg/kg}} o fosfenitoina {{c3::20 mg EF/kg}}", "", T)

T = ["capa2", "emergencia_htn", "cardiovascular"]
cz(deck2, "urg-c2-htn-1",
   "Regla general: reducir la PAM {{c1::<=25%}} en la primera hora, luego bajar gradualmente en 24-48 h", "", T)
cz(deck2, "urg-c2-htn-2",
   "Diseccion aortica: bajar rapido a PAS <{{c1::120 mmHg}} y FC <{{c2::60 lpm}}, con {{c3::betabloqueo}} primero (luego vasodilatador)",
   '<span class="contraste">El betabloqueo va ANTES del vasodilatador para evitar taquicardia refleja que propaga la diseccion.</span>', T)
cz(deck2, "urg-c2-htn-3",
   "Eclampsia/preeclampsia grave: {{c1::sulfato de magnesio}} (anticonvulsivo) + antihipertensivo (labetalol, hidralazina o nifedipino)", "", T)

T = ["capa2", "asma", "epoc", "respiratorio"]
cz(deck2, "urg-c2-resp-1",
   "Objetivo de SatO2: asma {{c1::93-95%}}; EPOC {{c2::88-92%}} para no abolir el estimulo hipoxico", "", T)
cz(deck2, "urg-c2-resp-2",
   "Asma grave que no responde -> anadir {{c1::sulfato de magnesio IV}}; corticoide sistemico precoz", "", T)
cz(deck2, "urg-c2-resp-3",
   "EPOC con acidosis respiratoria/hipercapnia (pH 7.25-7.35) -> {{c1::VNI (BiPAP)}} antes que intubar", "", T)

T = ["capa2", "tep", "respiratorio"]
cz(deck2, "urg-c2-tep-1",
   "Dimero D ajustado por edad en >50 anos: punto de corte = {{c1::edad x 10}} ng/mL", "", T)
cz(deck2, "urg-c2-tep-2",
   "Anticoagulacion de eleccion {{c1::DOAC}} (o HBPM); TEP de alto riesgo -> trombolisis con {{c2::alteplasa 100 mg en 2 h}}", "", T)

T = ["capa2", "intoxicaciones", "toxicologia"]
cz(deck2, "urg-c2-tox-1",
   "Paracetamol: indicar NAC segun el {{c1::nomograma de Rumack-Matthew}} (nivel a las 4 h post-ingesta)", "", T)
cz(deck2, "urg-c2-tox-2",
   "Naloxona {{c1::0.04-0.4 mg}} titulada hasta ventilacion adecuada; carbon activado util en la 1a {{c2::hora}} si via aerea protegida", "", T)

T = ["capa2", "paro", "rcp_enlace"]
cz(deck2, "urg-c2-paro-1",
   "RCP de calidad (recordatorio, detalle en deck RCP): compresiones {{c1::100-120/min}}, profundidad {{c2::5-6 cm}}, minimas interrupciones",
   '<span class="viva">AHA 2025: una sola descarga, priorizar acceso IV sobre IO en adultos.</span>', T)

# ============================================================
# CAPA 3 - EJES (fisiopatologia -> presentacion -> pista -> manejo)
# ============================================================
T = ["capa3", "sca", "cardiovascular"]
cz(deck3, "urg-c3-sca-1",
   "SCA: rotura/erosion de placa -> {{c1::trombo coronario}} -> isquemia/necrosis; se presenta como {{c2::dolor opresivo retroesternal irradiado}}; la pista es {{c3::cambios en ECG + troponina}}; el manejo es {{c4::reperfusion + antitrombotico}}", "", T)
cz(deck3, "urg-c3-sca-2",
   "Equivalentes anginosos (sin dolor tipico) en {{c1::diabeticos, ancianos y mujeres}}: disnea, sincope, epigastralgia",
   '<span class="redflag">No descartar SCA por ausencia de dolor toracico clasico en estos grupos.</span>', T)

T = ["capa3", "acv", "neurologico"]
cz(deck3, "urg-c3-acv-1",
   "ACV isquemico: oclusion arterial -> nucleo infartado + {{c1::penumbra salvable}}; se presenta como {{c2::deficit focal subito}}; la pista es {{c3::NIHSS + TAC/imagen de penumbra}}; el manejo es {{c4::reperfusion dentro de ventana}}", "", T)
cz(deck3, "urg-c3-acv-2",
   "\"Tiempo es cerebro\": el objetivo es salvar la {{c1::penumbra}} antes de que se infarte; cada minuto cuenta", "", T)

T = ["capa3", "sepsis", "infeccioso"]
cz(deck3, "urg-c3-sepsis-1",
   "Sepsis: respuesta inmune desregulada -> {{c1::vasodilatacion + fuga capilar}} -> hipoperfusion; se presenta con {{c2::fiebre/hipotermia, taquicardia, hipotension, confusion}}; la pista es {{c3::lactato + SOFA}}; el manejo es {{c4::antibiotico + liquidos + vasopresor}}", "", T)

T = ["capa3", "anafilaxia", "alergia"]
cz(deck3, "urg-c3-anafilaxia-1",
   "Anafilaxia: degranulacion mastocitaria (IgE) -> {{c1::histamina y mediadores}} -> broncoespasmo + vasodilatacion + edema; la pista es {{c2::inicio rapido tras exposicion}} (triptasa confirma); el manejo es {{c3::adrenalina IM}}", "", T)

T = ["capa3", "cad", "endocrino"]
cz(deck3, "urg-c3-cad-1",
   "CAD: deficit de insulina + hormonas contrarreguladoras -> lipolisis -> {{c1::cuerpos cetonicos}} -> acidosis con anion gap; se presenta con {{c2::poliuria, vomito, respiracion de Kussmaul, aliento cetonico}}; el manejo es {{c3::liquidos + insulina + potasio}}", "", T)

T = ["capa3", "status_epileptico", "neurologico"]
cz(deck3, "urg-c3-status-1",
   "Status: excitacion neuronal sostenida -> {{c1::dano excitotoxico}}; importa tratar pronto porque con el tiempo se vuelve {{c2::refractario al GABA}} (internalizacion de receptores)", "", T)

T = ["capa3", "emergencia_htn", "cardiovascular"]
cz(deck3, "urg-c3-htn-1",
   "Emergencia HTA: fallo de la autorregulacion -> {{c1::dano endotelial e isquemia}} en organos blanco (cerebro=encefalopatia, corazon=EAP/SCA, rinon, retina, aorta); el manejo es {{c2::bajada controlada}} segun el organo", "", T)

T = ["capa3", "asma", "epoc", "respiratorio"]
cz(deck3, "urg-c3-resp-1",
   "Crisis obstructiva: broncoconstriccion + atrapamiento aereo -> {{c1::hiperinsuflacion}} y fatiga; la pista gasometrica de gravedad es {{c2::normo/hipercapnia}} (cuando deberia haber hipocapnia por taquipnea)", "", T)

T = ["capa3", "tep", "respiratorio"]
cz(deck3, "urg-c3-tep-1",
   "TEP: obstruccion arterial pulmonar -> {{c1::aumento de poscarga del VD}} -> fallo de VD e hipotension; pistas ECG {{c2::S1Q3T3 / sobrecarga derecha}}; el manejo depende del {{c3::riesgo (trombolisis vs anticoagulacion)}}", "", T)

T = ["capa3", "intoxicaciones", "toxicologia"]
cz(deck3, "urg-c3-tox-1",
   "El toxidrome orienta el antidoto: {{c1::colinergico}} (DUMBELS, miosis) -> atropina; {{c2::simpaticomimetico}} (midriasis, HTA, taquicardia) -> benzodiacepinas; anticolinergico = \"rojo, seco, caliente, loco\"", "", T)

T = ["capa3", "shock", "cardiovascular"]
cz(deck3, "urg-c3-shock-1",
   "Perfil hemodinamico: hipovolemico y cardiogenico = piel {{c1::fria}} (RVS alta); distributivo (septico/anafilactico) = piel {{c2::caliente}} (RVS baja); obstructivo = signos de {{c3::obstruccion (ingurgitacion yugular, tonos apagados)}}", "", T)

# ============================================================
# CAPA 4 - MANEJO Y DIAGNOSTICO DIFERENCIAL (Q&A)
# ============================================================
T = ["capa4", "sca", "cardiovascular"]
qa(deck4, "urg-c4-sca-1",
   "Manejo inicial: <b>varon con dolor toracico opresivo de 1 h e elevacion del ST en cara inferior</b>",
   "STEMI inferior. 1) ECG &lt;10 min + monitor + via. 2) AAS 162-325 mg masticada + P2Y12 + anticoagulacion. 3) Reperfusion URGENTE: ICP primaria (puerta-balon &le;90 min) o fibrinolisis (&le;30 min) si no hay cateterismo a tiempo. 4) Estatina alta intensidad. 5) Cuidado con nitratos/morfina si hay infarto de VD (precarga-dependiente)."
   '<span class="ecoe">ECOE: "Es un STEMI inferior; ECG hecho, doble antiagregacion y activo reperfusion urgente."</span>', T + ["ecoe"])
qa(deck4, "urg-c4-sca-2",
   "Diferencial del <b>dolor toracico agudo que mata</b> (no perderse 5)",
   "1) SCA. 2) Diseccion aortica (dolor migratorio, asimetria de pulsos/TA, mediastino ancho). 3) TEP (disnea, pleuritico, factores de riesgo). 4) Neumotorax a tension (ausencia de murmullo, desviacion traqueal). 5) Taponamiento/pericarditis. Pedir ECG, troponina, RxTx y eco a pie de cama.", T)

T = ["capa4", "acv", "neurologico"]
qa(deck4, "urg-c4-acv-1",
   "Manejo: <b>mujer con hemiparesia derecha y afasia de inicio hace 2 h</b>",
   "Codigo ictus. 1) Hora de inicio (2 h = dentro de ventana). 2) TAC simple urgente para excluir hemorragia. 3) Glucemia y descartar imitadores (hipoglucemia, crisis). 4) Si isquemico y sin contraindicaciones: trombolisis IV (alteplasa 0.9 mg/kg o tenecteplasa 0.25 mg/kg), con PA &lt;185/110. 5) Si oclusion de gran vaso: trombectomia."
   '<span class="ecoe">ECOE: "Activo codigo ictus, confirmo hora de inicio, TAC urgente y valoro trombolisis si no hay contraindicacion."</span>', T + ["ecoe"])
qa(deck4, "urg-c4-acv-2",
   "Diferencial de <b>deficit neurologico focal subito</b>",
   "ACV isquemico, hemorragia intracerebral/HSA, hipoglucemia, crisis con paralisis de Todd, migrana con aura, masa/tumor. El TAC simple separa isquemico de hemorragico; SIEMPRE glucemia capilar primero.", T)

T = ["capa4", "sepsis", "infeccioso"]
qa(deck4, "urg-c4-sepsis-1",
   "Manejo: <b>paciente febril, hipotenso (PAM 58) y lactato 4 tras 30 mL/kg de cristaloide</b>",
   "Shock septico. Bundle hora-1: lactato, hemocultivos ANTES del antibiotico, antibiotico de amplio espectro, cristaloides 30 mL/kg. Como persiste hipotenso pese a volumen -> noradrenalina para PAM >=65. Buscar y controlar el foco (imagen, drenaje)."
   '<span class="ecoe">ECOE: "Shock septico: cultivos, antibiotico amplio en la primera hora, reanimo y arranco noradrenalina para PAM >=65."</span>', T + ["ecoe"])

T = ["capa4", "anafilaxia", "alergia"]
qa(deck4, "urg-c4-anafilaxia-1",
   "Manejo: <b>tras picadura, urticaria + sibilancias + hipotension</b>",
   "Anafilaxia (>=2 sistemas). 1) Adrenalina IM 0.3-0.5 mg en muslo YA, repetir cada 5-15 min. 2) Decubito con piernas elevadas. 3) O2 + cristaloides en bolo. 4) Broncodilatador si broncoespasmo. 5) Antihistaminico/corticoide solo como coadyuvantes. 6) Observar por reaccion bifasica.", T)

T = ["capa4", "cad", "endocrino"]
qa(deck4, "urg-c4-cad-1",
   "Manejo: <b>diabetico tipo 1 con glucosa 480, pH 7.1, K 3.0</b>",
   "CAD con hipopotasemia. ORDEN CRITICO: 1) Cristaloides IV. 2) Como K &lt;3.3 -> reponer potasio y NO iniciar insulina todavia. 3) Cuando K &ge;3.3 -> insulina 0.1 U/kg/h. 4) Anadir dextrosa cuando glucosa ~200-250. 5) Buscar desencadenante (infeccion, omision de insulina). 6) Resolucion por anion gap/beta-OH, no por glucemia."
   '<span class="redflag">Dar insulina con K 3.0 puede causar arritmia letal: primero se repone el potasio.</span>', T + ["ecoe"])

T = ["capa4", "status_epileptico", "neurologico"]
qa(deck4, "urg-c4-status-1",
   "Manejo: <b>crisis tonico-clonica que lleva 8 min sin ceder</b>",
   "Status epileptico. 1) ABC, O2, via, glucemia capilar (tratar hipoglucemia). 2) 1a linea: benzodiacepina (lorazepam 0.1 mg/kg IV o midazolam IM 10 mg). 3) Si persiste: 2a linea IV (levetiracetam 60 mg/kg, valproato 40 mg/kg o fosfenitoina 20 mg EF/kg). 4) Refractario: anestesia/intubacion en UCI + EEG.", T)

T = ["capa4", "emergencia_htn", "cardiovascular"]
qa(deck4, "urg-c4-htn-1",
   "Diferencial: <b>cuando una PA muy alta es emergencia y no solo urgencia</b>",
   "Es EMERGENCIA si hay dano agudo de organo blanco: encefalopatia/ACV, EAP o SCA, diseccion aortica, LRA, eclampsia, retinopatia grado III-IV. Sin dano = urgencia (manejo oral ambulatorio). La emergencia requiere antihipertensivo IV titulable y bajada controlada; la velocidad depende del organo (rapida solo en diseccion aortica y EAP).", T)

T = ["capa4", "tep", "respiratorio"]
qa(deck4, "urg-c4-tep-1",
   "Manejo: <b>postoperatoria con disnea subita, taquicardia e hipoxemia</b>",
   "Sospecha de TEP. 1) Estimar probabilidad (Wells). 2) Si baja -> dimero D (ajustado por edad); si alta o inestable -> angioTAC (o eco a pie de cama si demasiado inestable). 3) Estratificar riesgo (PESI + VD + troponina). 4) Estable -> anticoagulacion (DOAC/HBPM). 5) Alto riesgo/inestable -> trombolisis.", T)

T = ["capa4", "intoxicaciones", "toxicologia"]
qa(deck4, "urg-c4-tox-1",
   "Manejo: <b>encontrado somnoliento, bradipneico, con pupilas puntiformes</b>",
   "Toxidrome opioide. 1) ABC: ventilar/oxigenar. 2) Naloxona 0.04-0.4 mg titulada hasta recuperar ventilacion (vigilar reaparicion por vida media corta de naloxona). 3) Glucemia. 4) Buscar coingestas. La depresion respiratoria es la causa de muerte: priorizar la via aerea.", T)
qa(deck4, "urg-c4-tox-2",
   "Antidotos de alto rendimiento en examen (toxico -> antidoto)",
   "Paracetamol -> N-acetilcisteina. Opioides -> naloxona. Benzodiacepinas -> flumazenil (cauto). Organofosforados/colinergico -> atropina + pralidoxima. Betabloqueante -> glucagon. Metanol/etilenglicol -> fomepizol. Warfarina -> vitamina K + CCP. Digoxina -> anticuerpos antidigoxina.", T)

T = ["capa4", "shock", "cardiovascular"]
qa(deck4, "urg-c4-shock-1",
   "Diferencial: <b>como distinguir los 4 tipos de shock a pie de cama</b>",
   "Hipovolemico: piel fria, yugulares planas, responde a volumen (hemorragia, deshidratacion). Cardiogenico: frio, yugulares llenas, congestion pulmonar (IAM, IC). Distributivo: caliente, RVS baja (septico, anafilactico, neurogenico). Obstructivo: signos de obstruccion (TEP, neumotorax a tension, taponamiento). El eco a pie de cama (corazon, VCI, pulmon) ayuda a separarlos.", T)

# ============================================================
# BUILD + actualizar ids.json
# ============================================================
def build(deck, capa, fname):
    out = os.path.join(OUTPUT_DIR, fname)
    genanki.Package(deck).write_to_file(out)
    n = len(deck.notes)
    print(f"OK Capa {capa}: {fname}  deck_id={DECK_IDS[capa]}  notas={n}")
    entry = {"tema": "Urgencias", "audiencia": "Adulto", "capa": capa,
             "deck_id": DECK_IDS[capa], "deck_name": DECK_NAMES[capa], "guia": GUIA,
             "output": f"urgencias/output/{fname}", "notas": n}
    m = [d for d in ids["decks"] if d.get("tema") == "Urgencias"
         and d.get("audiencia") == "Adulto" and d.get("capa") == capa]
    if m:
        m[0].update(entry)
    else:
        ids["decks"].append(entry)
    return n


total = 0
total += build(deck1, 1, "Urgencias_Adulto_Capa1.apkg")
total += build(deck2, 2, "Urgencias_Adulto_Capa2.apkg")
total += build(deck3, 3, "Urgencias_Adulto_Capa3.apkg")
total += build(deck4, 4, "Urgencias_Adulto_Capa4.apkg")

# paquete combinado con las 4 capas
genanki.Package([deck1, deck2, deck3, deck4]).write_to_file(
    os.path.join(OUTPUT_DIR, "Urgencias_Adulto_TODOS.apkg"))
print(f"OK combinado: Urgencias_Adulto_TODOS.apkg  ({total} notas en total)")

with open(IDS_PATH, "w", encoding="utf-8") as f:
    json.dump(ids, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("ids.json actualizado")
