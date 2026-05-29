"""Generador de los 4 subdecks Anki para ECOE de Pediatria.

Capa 1 - Flujo Macro (Cloze)               - secuencia y bifurcaciones, sin numeros
Capa 2 - Componentes (Cloze)               - numeros, dosis, criterios, esquemas
Capa 3 - Ejes (Cloze)                      - fisiopatologia -> presentacion -> pista -> manejo
Capa 4 - Manejo y Dx Diferencial (Q&A)     - casos integradores tipo examen

Guias base (verificadas may-2026):
AHA/AAP NRP 2025, AAP hiperbilirrubinemia 2022, AAP fiebre lactante 2021,
AAP bronquiolitis 2014, IDSA/PIDS CAP 2011/2026, AAP OMA 2013, IDSA faringitis 2012,
AAP ITU 2011/2016, AAP convulsion febril 2011, AHA/AAP PALS 2025, AHA Kawasaki 2017,
GINA 2025, OMS deshidratacion, CDC/ACIP + Red Book, AAP Bright Futures, UpToDate.

Foco ampliado en INFECCIONES (peticion de la usuaria).
Cortos (puente a otros decks): abdomen quirurgico -> Cirugia,
shock pediatrico -> Patrones Madre, ruidos cardiacos -> Ruidos Cardiacos Pediatrico.
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

GUIA = ("AHA/AAP NRP 2025 + AAP hiperbilirrubinemia 2022 + AAP fiebre lactante 2021 + "
        "AAP bronquiolitis 2014 + IDSA/PIDS CAP 2011/2026 + AAP OMA 2013 + IDSA faringitis 2012 + "
        "AAP ITU 2011/2016 + AAP convulsion febril 2011 + AHA/AAP PALS 2025 + AHA Kawasaki 2017 + "
        "GINA 2025 + OMS + CDC/ACIP + Red Book + Bright Futures + UpToDate")

DECK_NAMES = {
    1: "Pediatria Pediátrico::Capa 1 - Flujo Macro",
    2: "Pediatria Pediátrico::Capa 2 - Componentes",
    3: "Pediatria Pediátrico::Capa 3 - Ejes",
    4: "Pediatria Pediátrico::Capa 4 - Manejo y Diagnostico Diferencial",
}
DECK_IDS = {1: 1611472033, 2: 1622556641, 3: 1633667722, 4: 1644778833}

with open(IDS_PATH, encoding="utf-8") as f:
    ids = json.load(f)
existing = {d["deck_id"] for d in ids["decks"]}


def resolve_deck_id(capa):
    match = [d for d in ids["decks"] if d.get("tema") == "Pediatria"
             and d.get("audiencia") == "Pediátrico" and d.get("capa") == capa]
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

BASE_TAGS = ["pediatria", "ecoe"]


def cz(deck, key, text, extra, tags):
    text = text.replace("<", "&lt;").replace(">", "&gt;")
    deck.add_note(genanki.Note(model=model_cloze, fields=[text, extra],
                               tags=BASE_TAGS + tags, guid=genanki.guid_for(key)))


def qa(deck, key, front, back, tags):
    deck.add_note(genanki.Note(model=model_qa, fields=[front, back],
                               tags=BASE_TAGS + tags, guid=genanki.guid_for(key)))


# ============================================================
# CAPA 1 - FLUJO MACRO (sin numeros)
# ============================================================

# --- NEONATOLOGIA ---
T = ["capa1", "reanimacion_neonatal", "neonatologia"]
cz(deck1, "ped-c1-nrp-1",
   "Recien nacido: pasos iniciales {{c1::calentar, secar, estimular y posicionar via aerea}}; reevaluar {{c2::respiracion y frecuencia cardiaca}}",
   '<span class="ecoe">ECOE: "Lo recibo, seco y estimulo, y reevaluo respiracion y frecuencia cardiaca."</span>', T + ["ecoe"])
cz(deck1, "ped-c1-nrp-2",
   "Si apnea/jadeo o FC baja pese a estimular -> {{c1::ventilacion con presion positiva}}; si la FC sigue muy baja pese a VPP efectiva -> {{c2::compresiones + adrenalina}}",
   '<span class="viva">El paso que mas cambia el pronostico del RN es una VPP efectiva.</span>', T)

T = ["capa1", "ictericia", "neonatologia"]
cz(deck1, "ped-c1-ictericia-1",
   "Ictericia neonatal {{c1::patologica}} si aparece en las primeras 24 h, asciende rapido o supera el umbral por edad; la {{c2::fisiologica}} aparece tras las 24 h y es leve",
   '<span class="redflag">Ictericia en &lt;24 h de vida = patologica hasta demostrar lo contrario (descartar hemolisis).</span>', T)
cz(deck1, "ped-c1-ictericia-2",
   "Manejo segun bilirrubina total: {{c1::fototerapia}} sobre umbral por edad/EG/factores; si muy alta o no responde -> {{c2::exanguinotransfusion}}",
   '<span class="viva">AAP 2022: umbrales mas altos que la guia previa, individualizados por neurotoxicidad.</span>', T)

T = ["capa1", "sepsis_neonatal", "neonatologia", "infeccioso"]
cz(deck1, "ped-c1-sepsisneo-1",
   "Sepsis neonatal {{c1::precoz}} (&lt;72 h, vertical: SGB, E. coli) vs {{c2::tardia}} (&gt;72 h, nosocomial/comunitaria)", "", T)
cz(deck1, "ped-c1-sepsisneo-2",
   "RN con sospecha de sepsis -> {{c1::hemocultivo + estudio}} y NO retrasar el {{c2::antibiotico empirico}}",
   '<span class="ecoe">ECOE: "Es un neonato septico: cultivos y antibiotico empirico de inmediato."</span>', T + ["ecoe"])

# --- INFECCIONES (bloque grande) ---
T = ["capa1", "fiebre_lactante", "infeccioso"]
cz(deck1, "ped-c1-fiebre-1",
   "Lactante febril (>=38 C) se estratifica por edad: {{c1::8-21 dias}}, {{c2::22-28 dias}} y {{c3::29-60 dias}}; a menor edad, mas agresivo el estudio",
   '<span class="ecoe">ECOE: "Lactante febril menor de 2 meses: estratifico por edad y descarto infeccion bacteriana grave."</span>', T + ["ecoe"])
cz(deck1, "ped-c1-fiebre-2",
   "8-21 dias: estudio completo (sangre, orina y {{c1::puncion lumbar}}) + antibiotico empirico + {{c2::hospitalizar}}",
   '<span class="redflag">En el menor de 21 dias NO se observa en casa: estudio completo y antibiotico siempre.</span>', T)
cz(deck1, "ped-c1-fiebre-3",
   "AAP 2021 usa la {{c1::procalcitonina}} (y PCR) para estratificar riesgo; el {{c2::recuento de leucocitos}} ya NO se recomienda como marcador",
   "", T)

T = ["capa1", "bronquiolitis", "respiratorio", "infeccioso"]
cz(deck1, "ped-c1-bronquiolitis-1",
   "Bronquiolitis = primer episodio de sibilancias en {{c1::&lt;2 anos}} por virus ({{c2::VSR}}); diagnostico {{c3::clinico}}",
   "", T)
cz(deck1, "ped-c1-bronquiolitis-2",
   "Manejo de bronquiolitis = {{c1::soporte}} (hidratacion y oxigeno); NO de rutina {{c2::broncodilatadores, corticoides, antibioticos ni radiografia}}",
   '<span class="contraste">A diferencia del asma, aqui los broncodilatadores y corticoides NO ayudan de rutina.</span>', T)

T = ["capa1", "neumonia", "respiratorio", "infeccioso"]
cz(deck1, "ped-c1-neumonia-1",
   "Neumonia pediatrica: la {{c1::taquipnea}} es el mejor signo clinico; sospechar bacteriana (neumococo) si fiebre alta + dificultad respiratoria + foco",
   "", T)
cz(deck1, "ped-c1-neumonia-2",
   "Neumonia tipica no complicada y ambulatoria -> primera linea {{c1::amoxicilina}}",
   "", T)

T = ["capa1", "otitis", "infeccioso"]
cz(deck1, "ped-c1-oma-1",
   "Otitis media aguda: diagnostico por {{c1::abombamiento timpanico}} + signos de derrame e inflamacion (otalgia)", "", T)
cz(deck1, "ped-c1-oma-2",
   "OMA -> primera linea {{c1::amoxicilina a dosis altas}}; en &gt;=2 anos sin gravedad se puede {{c2::observar 48-72 h}}", "", T)

T = ["capa1", "faringitis", "infeccioso"]
cz(deck1, "ped-c1-faringitis-1",
   "Faringoamigdalitis: estimar probabilidad de estreptococo con {{c1::Centor/McIsaac}} y confirmar con {{c2::test rapido o cultivo}} antes de dar antibiotico",
   '<span class="redflag">No antibiotico empirico a toda faringitis: la mayoria son virales.</span>', T)
cz(deck1, "ped-c1-faringitis-2",
   "Faringitis estreptococica confirmada -> {{c1::penicilina o amoxicilina}} (previene fiebre reumatica)", "", T)

T = ["capa1", "crup", "respiratorio", "infeccioso"]
cz(deck1, "ped-c1-crup-1",
   "Crup (laringotraqueitis): {{c1::tos perruna + estridor inspiratorio + disfonia}}, de origen viral", "", T)
cz(deck1, "ped-c1-crup-2",
   "Manejo del crup: {{c1::dexametasona}} a casi todos; si estridor en reposo -> {{c2::adrenalina nebulizada}}", "", T)

T = ["capa1", "itu", "infeccioso", "nefrologia"]
cz(deck1, "ped-c1-itu-1",
   "ITU en el lactante puede presentarse solo como {{c1::fiebre sin foco}}; la muestra valida es por {{c2::sondaje o puncion suprapubica}}, NO por bolsa",
   '<span class="redflag">El urocultivo por bolsa colectora se contamina: no sirve para confirmar ITU.</span>', T)
cz(deck1, "ped-c1-itu-2",
   "Tras una ITU febril en el lactante, valorar {{c1::ecografia renal}} y estudiar segun hallazgos", "", T)

T = ["capa1", "gea", "deshidratacion", "infeccioso", "digestivo"]
cz(deck1, "ped-c1-gea-1",
   "Gastroenteritis aguda: la prioridad es valorar el {{c1::grado de deshidratacion}}, no el germen", "", T)
cz(deck1, "ped-c1-gea-2",
   "Manejo segun deshidratacion (plan OMS): leve/moderada -> {{c1::rehidratacion oral (sales)}}; grave o shock -> {{c2::liquidos IV}}",
   '<span class="ecoe">ECOE: "Valoro el grado de deshidratacion y prefiero la via oral salvo intolerancia o shock."</span>', T + ["ecoe"])

T = ["capa1", "meningitis", "infeccioso", "neurologia"]
cz(deck1, "ped-c1-meningitis-1",
   "Sospecha de meningitis bacteriana -> {{c1::antibiotico empirico urgente}} (no esperar la puncion); anadir {{c2::dexametasona}} segun caso",
   '<span class="redflag">El antibiotico NO se retrasa por la puncion lumbar ni por la TAC.</span>', T)
cz(deck1, "ped-c1-meningitis-2",
   "El empirico depende de la {{c1::edad}} (neonato cubre SGB/Listeria/E.coli; mayor, neumococo y meningococo)", "", T)

T = ["capa1", "exantemas", "infeccioso", "dermatologia"]
cz(deck1, "ped-c1-exantema-1",
   "Exantema con {{c1::manchas de Koplik}} + fiebre, tos, coriza y conjuntivitis = {{c2::sarampion}}", "", T)
cz(deck1, "ped-c1-exantema-2",
   "Fiebre alta 3 dias que cede y APARECE el exantema al desaparecer la fiebre = {{c1::exantema subito (roseola, VHH-6)}}", "", T)
cz(deck1, "ped-c1-exantema-3",
   "Mejillas eritematosas \"abofeteadas\" = {{c1::eritema infeccioso (parvovirus B19)}}; lengua aframbuesada + piel en lija = {{c2::escarlatina}}", "", T)
cz(deck1, "ped-c1-exantema-4",
   "Vesiculas en distintos estadios a la vez (\"cielo estrellado\") = {{c1::varicela}}; vesiculas en manos, pies y boca = {{c2::enfermedad mano-pie-boca}}", "", T)

T = ["capa1", "kawasaki", "infeccioso", "cardiovascular"]
cz(deck1, "ped-c1-kawasaki-1",
   "Kawasaki: {{c1::fiebre >=5 dias}} + criterios clinicos (conjuntivitis, labios/lengua, exantema, cambios en extremidades, adenopatia cervical)", "", T)
cz(deck1, "ped-c1-kawasaki-2",
   "Importa tratar pronto porque el riesgo es el {{c1::aneurisma coronario}}; manejo {{c2::inmunoglobulina IV + aspirina}}",
   '<span class="redflag">Toda sospecha de Kawasaki necesita ecocardiograma por riesgo coronario.</span>', T)

# --- RESPIRATORIO CRONICO / EMERGENCIAS ---
T = ["capa1", "asma", "respiratorio"]
cz(deck1, "ped-c1-asma-1",
   "Crisis asmatica pediatrica -> {{c1::oxigeno}} + {{c2::broncodilatador (SABA)}} + {{c3::corticoide sistemico}}; reevaluar respuesta", "", T)

T = ["capa1", "convulsion_febril", "neurologia"]
cz(deck1, "ped-c1-cf-1",
   "Convulsion febril {{c1::simple}} (generalizada, &lt;15 min, una en 24 h, 6 m-5 anos) vs {{c2::compleja}} (focal, prolongada o repetida)", "", T)
cz(deck1, "ped-c1-cf-2",
   "Ante convulsion febril simple lo clave es {{c1::buscar el foco de la fiebre}}; no requiere de rutina puncion, EEG ni neuroimagen", "", T)

T = ["capa1", "pals", "reanimacion"]
cz(deck1, "ped-c1-pals-1",
   "Paro pediatrico -> {{c1::RCP de alta calidad}} + ventilacion; la causa mas frecuente es {{c2::hipoxia/respiratoria}} (no cardiaca como en el adulto)", "", T)
cz(deck1, "ped-c1-pals-2",
   "Ritmos: desfibrilables = {{c1::FV / TV sin pulso}}; no desfibrilables = {{c2::asistolia / AESP}} (lo mas frecuente en ninos)", "", T)

# --- PREVENTIVO / DESARROLLO ---
T = ["capa1", "desarrollo"]
cz(deck1, "ped-c1-desarrollo-1",
   "El desarrollo se evalua por areas: {{c1::motor grueso, motor fino, lenguaje y social}}; las {{c2::senales de alarma}} pesan mas que un hito aislado", "", T)

T = ["capa1", "vacunas", "preventivo"]
cz(deck1, "ped-c1-vacunas-1",
   "Ante un nino, revisar siempre el {{c1::esquema de vacunacion}} y completarlo segun edad (oportunidad perdida = vacunar hoy)", "", T)

T = ["capa1", "crecimiento", "preventivo"]
cz(deck1, "ped-c1-crecimiento-1",
   "El crecimiento se vigila con {{c1::percentiles/curvas (peso, talla, perimetro cefalico)}}; lo que alarma es el {{c2::cambio de carril}}, no un valor aislado", "", T)

# --- CORTOS (puente a otros decks) ---
T = ["capa1", "abdomen", "cirugia_enlace"]
cz(deck1, "ped-c1-abdomen-1",
   "Abdomen quirurgico pediatrico (detalle en deck Cirugia): invaginacion ({{c1::heces en jalea de grosella}}), estenosis pilorica ({{c2::vomito en proyectil}}), apendicitis", "", T)

T = ["capa1", "shock", "patrones_enlace"]
cz(deck1, "ped-c1-shock-1",
   "Shock pediatrico (detalle en deck Patrones Madre): la {{c1::taquicardia}} es el signo precoz y la {{c2::hipotension}} es TARDIA (signo de descompensacion)",
   '<span class="redflag">En el nino la TA se mantiene hasta el final: no esperar a la hipotension para actuar.</span>', T)

T = ["capa1", "ruidos_cardiacos", "cardiovascular", "ruidos_enlace"]
cz(deck1, "ped-c1-ruidos-1",
   "Soplos pediatricos (detalle en deck Ruidos Cardiacos Pediatrico): la mayoria son {{c1::inocentes/funcionales}}; sospechar {{c2::patologico}} si diastolico, intenso, con sintomas o pulsos anormales", "", T)

# ============================================================
# CAPA 2 - COMPONENTES (numeros, dosis, criterios)
# ============================================================
T = ["capa2", "reanimacion_neonatal", "neonatologia"]
cz(deck2, "ped-c2-nrp-1",
   "Neonato: relacion compresiones:ventilaciones = {{c1::3:1}} (90 compresiones + 30 ventilaciones por minuto); iniciar compresiones si FC &lt;{{c2::60}} pese a VPP efectiva", "", T)
cz(deck2, "ped-c2-nrp-2",
   "Iniciar VPP si apnea/jadeo o FC &lt;{{c1::100}}; adrenalina {{c2::0.01-0.03 mg/kg IV}} si FC &lt;60 pese a VPP + compresiones", "", T)

T = ["capa2", "ictericia", "neonatologia"]
cz(deck2, "ped-c2-ictericia-1",
   "El umbral de fototerapia (AAP 2022) depende de {{c1::edad en horas}}, {{c2::edad gestacional}} y {{c3::factores de neurotoxicidad}}; se lee en nomograma, no es un valor unico", "", T)

T = ["capa2", "sepsis_neonatal", "neonatologia", "infeccioso"]
cz(deck2, "ped-c2-sepsisneo-1",
   "Empirico de sepsis neonatal precoz: {{c1::ampicilina + gentamicina}} (cubre SGB, Listeria y gramnegativos)", "", T)

T = ["capa2", "fiebre_lactante", "infeccioso"]
cz(deck2, "ped-c2-fiebre-1",
   "Fiebre relevante en el lactante = temperatura rectal >={{c1::38.0 C}}", "", T)
cz(deck2, "ped-c2-fiebre-2",
   "22-28 dias: siempre sangre y orina; la {{c1::puncion lumbar}} se decide segun inflamatorios (procalcitonina, PCR, neutrofilos)", "", T)

T = ["capa2", "bronquiolitis", "respiratorio", "infeccioso"]
cz(deck2, "ped-c2-bronquiolitis-1",
   "En bronquiolitis dar oxigeno si la SatO2 cae por debajo de {{c1::90%}}", "", T)

T = ["capa2", "neumonia", "respiratorio", "infeccioso"]
cz(deck2, "ped-c2-neumonia-1",
   "Taquipnea por edad (OMS): &lt;2 m >={{c1::60}}; 2-12 m >={{c2::50}}; 1-5 a >={{c3::40}} respiraciones/min", "", T)
cz(deck2, "ped-c2-neumonia-2",
   "Amoxicilina a dosis alta {{c1::80-90 mg/kg/dia}} como primera linea de la neumonia tipica", "", T)

T = ["capa2", "otitis", "infeccioso"]
cz(deck2, "ped-c2-oma-1",
   "OMA: amoxicilina {{c1::80-90 mg/kg/dia}}; duracion {{c2::10 dias}} en &lt;2 anos, perforacion, fallo o recurrencia", "", T)

T = ["capa2", "faringitis", "infeccioso"]
cz(deck2, "ped-c2-faringitis-1",
   "Tratamiento de faringitis estreptococica: penicilina/amoxicilina durante {{c1::10 dias}} (cumplir la duracion previene fiebre reumatica)", "", T)

T = ["capa2", "crup", "respiratorio", "infeccioso"]
cz(deck2, "ped-c2-crup-1",
   "Crup: dexametasona dosis unica {{c1::0.15-0.6 mg/kg}}; adrenalina nebulizada si estridor en reposo (vigilar {{c2::rebote 2-4 h}})", "", T)

T = ["capa2", "gea", "deshidratacion", "infeccioso"]
cz(deck2, "ped-c2-gea-1",
   "Deshidratacion grave / shock (plan C OMS): bolo IV de cristaloide {{c1::20 mL/kg}}, repetible segun respuesta", "", T)
cz(deck2, "ped-c2-gea-2",
   "Signos de deshidratacion a buscar: {{c1::estado de conciencia, ojos hundidos, lagrimas, mucosas, signo del pliegue y llenado capilar}}", "", T)

T = ["capa2", "meningitis", "infeccioso", "neurologia"]
cz(deck2, "ped-c2-meningitis-1",
   "Empirico &gt;1 mes: {{c1::cefalosporina de 3a (cefotaxima/ceftriaxona)}} + {{c2::vancomicina}}; neonato: ampicilina + cefotaxima/gentamicina", "", T)

T = ["capa2", "kawasaki", "infeccioso", "cardiovascular"]
cz(deck2, "ped-c2-kawasaki-1",
   "Kawasaki clasico: fiebre >={{c1::5 dias}} + al menos {{c2::4 de 5}} criterios clinicos principales", "", T)
cz(deck2, "ped-c2-kawasaki-2",
   "Tratamiento: {{c1::inmunoglobulina IV (IGIV)}} + {{c2::aspirina}}; ecocardiograma para vigilar coronarias", "", T)

T = ["capa2", "convulsion_febril", "neurologia"]
cz(deck2, "ped-c2-cf-1",
   "Convulsion febril: edad {{c1::6 meses a 5 anos}}; la simple dura &lt;{{c2::15 min}}, es generalizada y unica en 24 h", "", T)

T = ["capa2", "pals", "reanimacion"]
cz(deck2, "ped-c2-pals-1",
   "RCP pediatrica: comprimir {{c1::1/3 del diametro AP}} del torax, a {{c2::100-120/min}}; en lactante, tecnica de {{c3::dos pulgares}} (no dos dedos)",
   '<span class="viva">PALS 2025: en lactante se prefiere la tecnica de dos pulgares; ya no se recomienda la de dos dedos.</span>', T)
cz(deck2, "ped-c2-pals-2",
   "Adrenalina {{c1::0.01 mg/kg}}; desfibrilacion {{c2::2 J/kg}} la primera y {{c3::4 J/kg}} las siguientes", "", T)
cz(deck2, "ped-c2-pals-3",
   "PALS 2025: en ritmo no desfibrilable, adrenalina {{c1::precoz}}; en desfibrilable, adrenalina {{c2::tras la 2a descarga}}; objetivo post-paro TA &gt; {{c3::percentil 10}} y evitar hipertermia", "", T)

T = ["capa2", "desarrollo"]
cz(deck2, "ped-c2-desarrollo-1",
   "Hitos guia: sosten cefalico ~{{c1::3 m}}, sedestacion sin apoyo ~{{c2::6 m}}, marcha autonoma ~{{c3::12 m}}, primeras palabras ~{{c4::12 m}}", "", T)

# ============================================================
# CAPA 3 - EJES (fisiopatologia -> presentacion -> pista -> manejo)
# ============================================================
T = ["capa3", "ictericia", "neonatologia"]
cz(deck3, "ped-c3-ictericia-1",
   "Ictericia neonatal: inmadurez de la conjugacion + (a veces) hemolisis -> {{c1::bilirrubina indirecta alta}}; la pista de gravedad es la {{c2::aparicion &lt;24 h o ascenso rapido}}; el riesgo temido es el {{c3::kernicterus}}; el manejo es {{c4::fototerapia/exanguino}}", "", T)

T = ["capa3", "fiebre_lactante", "infeccioso"]
cz(deck3, "ped-c3-fiebre-1",
   "Lactante pequeno febril: inmadurez inmune -> riesgo de {{c1::infeccion bacteriana invasiva}} con pocos signos localizadores; la pista es la {{c2::edad + inflamatorios (procalcitonina/PCR)}}; el manejo escala estudio y antibiotico a menor edad", "", T)

T = ["capa3", "bronquiolitis", "respiratorio", "infeccioso"]
cz(deck3, "ped-c3-bronquiolitis-1",
   "Bronquiolitis: el virus inflama la {{c1::pequena via aerea}} -> tapones e hiperinsuflacion; se presenta con {{c2::sibilancias/crepitos + dificultad para alimentarse}}; el manejo es de {{c3::soporte}} (no broncodilatador de rutina)", "", T)

T = ["capa3", "gea", "deshidratacion", "infeccioso"]
cz(deck3, "ped-c3-gea-1",
   "GEA: perdida de agua y electrolitos -> {{c1::deshidratacion}}; el nino lo compensa con {{c2::taquicardia}} antes de caer la TA; la pista es el {{c3::grado clinico de deshidratacion}}; el manejo es {{c4::rehidratacion (oral o IV)}}", "", T)

T = ["capa3", "meningitis", "infeccioso", "neurologia"]
cz(deck3, "ped-c3-meningitis-1",
   "Meningitis: inflamacion meningea -> {{c1::fiebre, irritabilidad y signos meningeos}}; en el lactante puede faltar la rigidez y dar solo {{c2::fontanela abombada, rechazo del alimento e irritabilidad}}; el manejo es {{c3::antibiotico urgente +/- dexametasona}}", "", T)

T = ["capa3", "kawasaki", "infeccioso", "cardiovascular"]
cz(deck3, "ped-c3-kawasaki-1",
   "Kawasaki: vasculitis de mediano vaso -> dano de {{c1::arterias coronarias}}; se presenta como {{c2::fiebre prolongada + criterios mucocutaneos}}; la pista es la fiebre que no cede con criterios; el manejo {{c3::IGIV + aspirina}} reduce los aneurismas", "", T)

T = ["capa3", "crup", "respiratorio", "infeccioso"]
cz(deck3, "ped-c3-crup-1",
   "Crup: edema {{c1::subglotico}} -> obstruccion alta -> {{c2::estridor inspiratorio + tos perruna}}; la pista es el estridor en reposo (gravedad); el manejo es {{c3::dexametasona +/- adrenalina nebulizada}}",
   '<span class="contraste">Estridor que empeora con baberos y voz apagada -> pensar epiglotitis, no crup.</span>', T)

T = ["capa3", "convulsion_febril", "neurologia"]
cz(deck3, "ped-c3-cf-1",
   "Convulsion febril: cerebro inmaduro sensible al {{c1::ascenso febril}} -> crisis; la pista es que es {{c2::simple y autolimitada}} con buen estado tras la crisis; el manejo es {{c3::tratar la fiebre y buscar el foco}}, tranquilizar a la familia", "", T)

T = ["capa3", "pals", "reanimacion"]
cz(deck3, "ped-c3-pals-1",
   "Paro pediatrico: suele ser por {{c1::hipoxia/insuficiencia respiratoria}} (no fibrilacion primaria); por eso la prioridad es {{c2::oxigenar y ventilar}}; reconocer y tratar el deterioro respiratorio/circulatorio PREVIENE el paro", "", T)

T = ["capa3", "sepsis_neonatal", "neonatologia", "infeccioso"]
cz(deck3, "ped-c3-sepsisneo-1",
   "Sepsis neonatal: signos {{c1::inespecificos}} (mala succion, hipotermia/fiebre, letargia, dificultad respiratoria, ictericia); por eso el umbral para cultivar y tratar es {{c2::bajo}}", "", T)

# ============================================================
# CAPA 4 - MANEJO Y DIAGNOSTICO DIFERENCIAL (Q&A)
# ============================================================
T = ["capa4", "fiebre_lactante", "infeccioso"]
qa(deck4, "ped-c4-fiebre-1",
   "Manejo: <b>lactante de 15 dias con fiebre rectal de 38.4 C, buen aspecto</b>",
   "Grupo 8-21 dias = el de mayor riesgo. Estudio COMPLETO: hemograma con procalcitonina/PCR, hemocultivo, orina con urocultivo (sondaje) y puncion lumbar. Iniciar antibiotico empirico parenteral y HOSPITALIZAR. En este grupo no aplica la observacion ambulatoria, aunque luzca bien."
   '<span class="ecoe">ECOE: "Menor de 21 dias febril: estudio completo incluida puncion lumbar, antibiotico empirico e ingreso."</span>', T + ["ecoe"])
qa(deck4, "ped-c4-fiebre-2",
   "Diferencial de <b>fiebre sin foco en el lactante</b>",
   "ITU (la mas frecuente y a menudo el unico foco), bacteriemia oculta, neumonia, meningitis, GEA viral, otitis, y causas virales (incluida roseola antes del exantema). Por eso el urocultivo es obligado y la edad guia cuanto estudiar.", T)

T = ["capa4", "bronquiolitis", "respiratorio", "infeccioso"]
qa(deck4, "ped-c4-bronquiolitis-1",
   "Manejo: <b>lactante de 6 meses con tos, sibilancias, rinorrea y dificultad para alimentarse en invierno</b>",
   "Bronquiolitis (probable VSR). Diagnostico clinico, sin radiografia de rutina. Manejo de soporte: aspiracion de secreciones, hidratacion (fraccionada o IV/SNG si no tolera), oxigeno si SatO2 &lt;90%. NO dar de rutina broncodilatadores, corticoides ni antibioticos. Vigilar signos de agotamiento y apneas en los mas pequenos.", T)

T = ["capa4", "exantemas", "infeccioso"]
qa(deck4, "ped-c4-exantema-1",
   "Diferencial rapido de <b>exantemas febriles clasicos</b> (pista -> dx)",
   "Koplik + tos/coriza/conjuntivitis -> sarampion. Fiebre 3 dias que cede y entonces brota el exantema -> roseola (VHH-6). Mejillas abofeteadas -> eritema infeccioso (parvovirus B19). Lengua aframbuesada + piel en lija + Pastia -> escarlatina. Vesiculas en distintos estadios -> varicela. Vesiculas en manos, pies y boca -> mano-pie-boca (coxsackie). Adenopatia retroauricular -> rubeola.", T)

T = ["capa4", "kawasaki", "infeccioso", "cardiovascular"]
qa(deck4, "ped-c4-kawasaki-1",
   "Manejo: <b>nino de 2 anos con fiebre de 6 dias, conjuntivitis bilateral no exudativa, labios fisurados, exantema y adenopatia cervical</b>",
   "Enfermedad de Kawasaki (fiebre >=5 dias + >=4 criterios). 1) IGIV + aspirina lo antes posible (idealmente en los primeros 10 dias) para reducir aneurismas coronarios. 2) Ecocardiograma basal y de seguimiento. 3) Descartar imitadores (escarlatina, sarampion, reaccion farmacologica)."
   '<span class="redflag">La fiebre prolongada con criterios mucocutaneos obliga a descartar Kawasaki por el riesgo coronario.</span>', T + ["ecoe"])

T = ["capa4", "gea", "deshidratacion", "infeccioso"]
qa(deck4, "ped-c4-gea-1",
   "Manejo: <b>nino con diarrea, vomitos, ojos hundidos, mucosas secas y llenado capilar lento</b>",
   "GEA con deshidratacion. 1) Estimar el grado (este parece moderado-grave). 2) Si tolera y no hay shock: rehidratacion oral con sales (plan B). 3) Si deshidratacion grave/shock: bolo IV de cristaloide 20 mL/kg, repetir segun respuesta (plan C). 4) Reintroducir alimentacion precoz; el zinc ayuda en entornos de riesgo. Antibiotico solo en casos seleccionados.", T)

T = ["capa4", "crup", "respiratorio", "infeccioso"]
qa(deck4, "ped-c4-crup-1",
   "Manejo y diferencial: <b>nino con tos perruna y estridor</b>",
   "Crup viral. Manejo: dexametasona a casi todos; si estridor en reposo, adrenalina nebulizada y observar por rebote. Mantener al nino tranquilo (el llanto empeora la obstruccion). Diferencial del estridor: epiglotitis (toxico, babeante, sin tos perruna), aspiracion de cuerpo extrano (inicio subito), absceso retrofaringeo, traqueitis bacteriana.", T)

T = ["capa4", "convulsion_febril", "neurologia"]
qa(deck4, "ped-c4-cf-1",
   "Manejo: <b>nino de 18 meses con crisis generalizada de 2 min durante un cuadro febril, ya recuperado</b>",
   "Convulsion febril simple. 1) Si activa &gt;5 min, benzodiacepina; aqui ya cedio. 2) Buscar el FOCO de la fiebre (exploracion: oidos, garganta, orina). 3) No se requieren de rutina puncion lumbar, EEG ni neuroimagen en la simple. 4) Tranquilizar a la familia: buen pronostico, recurrencia posible, no causa epilepsia ni dano. Antitermicos para confort."
   '<span class="ecoe">ECOE: "Es una convulsion febril simple; busco el foco de la fiebre y tranquilizo a los padres."</span>', T + ["ecoe"])

T = ["capa4", "otitis", "faringitis", "infeccioso"]
qa(deck4, "ped-c4-orl-1",
   "Decision antibiotica: <b>cuando SI tratar otitis y faringitis</b>",
   "OMA: tratar con amoxicilina alta dosis si &lt;2 anos, otorrea, bilateral o grave; en &gt;=2 anos leve se puede observar 48-72 h. Faringitis: solo tratar si estreptococo confirmado (test rapido/cultivo) o McIsaac alto; la mayoria virales NO llevan antibiotico. Tratar el estreptococo previene fiebre reumatica.", T)

T = ["capa4", "ictericia", "neonatologia"]
qa(deck4, "ped-c4-ictericia-1",
   "Manejo: <b>RN de 36 h con ictericia visible</b>",
   "1) Medir bilirrubina (transcutanea o serica), no estimar a ojo. 2) Comparar con el umbral del nomograma AAP 2022 segun horas de vida, EG y factores de neurotoxicidad. 3) Si supera umbral -> fototerapia; si muy alta o no responde -> exanguinotransfusion. 4) Buscar causa si es precoz/intensa (Coombs, grupo, hemolisis). La ictericia &lt;24 h es siempre patologica.", T)

T = ["capa4", "shock", "patrones_enlace"]
qa(deck4, "ped-c4-shock-1",
   "Diferencial: <b>signos de shock en el nino vs el adulto</b>",
   "En el nino la TA se mantiene por vasoconstriccion hasta fases tardias: la TAQUICARDIA y el llenado capilar lento son los signos PRECOCES, y la hipotension es tardia (shock descompensado, casi preparada). Tipos como en el adulto (hipovolemico el mas comun por GEA, distributivo/septico, cardiogenico, obstructivo). Detalle en el deck Patrones Madre.", T)

# ============================================================
# BUILD + actualizar ids.json
# ============================================================
def build(deck, capa, fname):
    out = os.path.join(OUTPUT_DIR, fname)
    genanki.Package(deck).write_to_file(out)
    n = len(deck.notes)
    print(f"OK Capa {capa}: {fname}  deck_id={DECK_IDS[capa]}  notas={n}")
    entry = {"tema": "Pediatria", "audiencia": "Pediátrico", "capa": capa,
             "deck_id": DECK_IDS[capa], "deck_name": DECK_NAMES[capa], "guia": GUIA,
             "output": f"pediatria/output/{fname}", "notas": n}
    m = [d for d in ids["decks"] if d.get("tema") == "Pediatria"
         and d.get("audiencia") == "Pediátrico" and d.get("capa") == capa]
    if m:
        m[0].update(entry)
    else:
        ids["decks"].append(entry)
    return n


total = 0
total += build(deck1, 1, "Pediatria_Pediatrico_Capa1.apkg")
total += build(deck2, 2, "Pediatria_Pediatrico_Capa2.apkg")
total += build(deck3, 3, "Pediatria_Pediatrico_Capa3.apkg")
total += build(deck4, 4, "Pediatria_Pediatrico_Capa4.apkg")

genanki.Package([deck1, deck2, deck3, deck4]).write_to_file(
    os.path.join(OUTPUT_DIR, "Pediatria_Pediatrico_TODOS.apkg"))
print(f"OK combinado: Pediatria_Pediatrico_TODOS.apkg  ({total} notas en total)")

with open(IDS_PATH, "w", encoding="utf-8") as f:
    json.dump(ids, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("ids.json actualizado")
