# -*- coding: utf-8 -*-
"""Deck 2 — Exploración Física Básica por sistema (transversal ECOE).

Formato Q&A con FLIP pedagógico:
- Front: QUÉ HACES (maniobras verbalizadas paso a paso) + QUÉ BUSCAS (signos
  a observar / palpar / auscultar).
- Back: POR QUÉ se hace cada maniobra + SIGNIFICADO de cada hallazgo
  positivo (qué patología orienta o descarta).

Cobertura:
- 20 cards por sistema (universal, sirve a las 6 estaciones).
- 5 cards especiales por estación (ATLS, mama, gineco resumen, ped lactante,
  ped adolescente).
- Total: 25 cards.

Tags por sistema y estación → filtrar con Custom Study en Anki.

Guías: Bates 13ª + ATLS 10ª + ACC/AHA 2017 + Sepsis-3 + Tokyo Guidelines 2024
+ Alvarado + ACOG + AAP Bright Futures + Glasgow original + Babinski +
GALS Doherty 1992 + UpToDate.
"""
import os
import genanki

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "output")
os.makedirs(OUTPUT_DIR, exist_ok=True)

MODEL_QA_ID = 1607392320       # mismo Q&A reusable
DECK_ID = 1582740396           # nuevo, único — registrar en ids.json
DECK_NAME = "Preparación Verbalizada::Deck 2 - Exploración Física Básica"

# ============================================================
# CSS — badge por sistema, secciones diferenciadas en back
# ============================================================
CSS = """
.card {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  font-size: 17px; text-align: left; color: #1a1a1a;
  background-color: #fafafa; padding: 20px; line-height: 1.55;
}
.badge {
  display: inline-block; padding: 5px 14px; margin-bottom: 12px;
  color: #fff; border-radius: 6px;
  font-size: 12px; letter-spacing: 0.7px; font-weight: 700;
  text-transform: uppercase;
}
.sis-grales  { background: #475569; }
.sis-cuello  { background: #78350f; }
.sis-linf    { background: #92400e; }
.sis-cardio  { background: #b91c1c; }
.sis-vasc    { background: #7f1d1d; }
.sis-pulm    { background: #1d4ed8; }
.sis-abd     { background: #b45309; }
.sis-uro     { background: #65a30d; }
.sis-neuro   { background: #7e22ce; }
.sis-msk     { background: #047857; }
.sis-piel    { background: #be185d; }
.sis-cx      { background: #991b1b; }
.sis-gyo     { background: #db2777; }
.sis-ped     { background: #c2410c; }

.titulo { font-size: 16px; font-weight: 700; color: #111;
          margin: 0 0 10px 0; }
.subt   { margin-top: 12px; font-weight: 700; font-size: 13px;
          letter-spacing: 0.5px; text-transform: uppercase;
          color: #374151; }
.haces  { color: #1e40af; font-weight: 500;
          background: #eff6ff; border-left: 3px solid #2563eb;
          padding: 10px 14px; margin: 6px 0 12px 0; border-radius: 3px;
          white-space: pre-line; }
.buscas { color: #047857; font-weight: 500;
          background: #ecfdf5; border-left: 3px solid #059669;
          padding: 10px 14px; margin: 6px 0 0 0; border-radius: 3px;
          white-space: pre-line; }
ul.porque { margin: 6px 0 0 0; padding-left: 22px; }
ul.porque li { margin: 5px 0; }
.tip-ecoe { background: #ecfdf5; border-left: 3px solid #059669;
            padding: 8px 12px; margin: 10px 0; border-radius: 3px;
            font-size: 15px; }
.penaliza { background: #fef2f2; border-left: 3px solid #dc2626;
            padding: 8px 12px; margin: 10px 0; border-radius: 3px;
            font-size: 15px; }
.fuente { color: #6b7280; font-size: 13px; font-style: italic;
          margin-top: 10px; }
#extra { margin-top: 14px; border: none;
         border-top: 1px solid #d4d4d4; padding-top: 12px; }
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
BASE_TAGS = ["exploracion_fisica", "ecoe", "preparacion_verbalizada"]


def make_card(badge_text, badge_class, titulo, haces, buscas,
              porque, ecoe_tip, penaliza, fuente, *extra_tags):
    """Genera nota Q&A: front=maniobras+qué buscas, back=porqué+significado."""
    front = (
        f'<div class="badge {badge_class}">{badge_text}</div>'
        f'<div class="titulo">{titulo}</div>'
        f'<div class="subt">¿Qué haces?</div>'
        f'<div class="haces">{haces}</div>'
        f'<div class="subt">¿Qué buscas?</div>'
        f'<div class="buscas">{buscas}</div>'
    )
    porque_html = "".join(f"<li>{p}</li>" for p in porque)
    back = (
        f'<div class="subt">¿Por qué se hace y qué significa cada hallazgo?</div>'
        f'<ul class="porque">{porque_html}</ul>'
        f'<div class="tip-ecoe">🗣️ ECOE: {ecoe_tip}</div>'
        f'<div class="penaliza">⚠️ Penaliza si: {penaliza}</div>'
        f'<div class="fuente">📚 {fuente}</div>'
    )
    note = genanki.Note(
        model=model_qa,
        fields=[front, back],
        tags=BASE_TAGS + list(extra_tags),
    )
    deck.add_note(note)


# ============================================================
# A · POR SISTEMA — 20 cards
# ============================================================

make_card(
    "GENERALES", "sis-grales",
    "EF1 · Signos vitales completos + inspección general + impresión clínica",
    'TA bilateral, paciente sentado, 5 min reposo, brazalete adecuado.\n'
    'FC palpando radial 30 s × 2 (60 s si arrítmico).\n'
    'FR contando 30 s × 2 sin que lo note el paciente.\n'
    'Temperatura axilar o timpánica.\n'
    'SatO₂ percutánea (dedo limpio, sin barniz).\n'
    'Peso, talla, IMC, perímetro abdominal.\n'
    'Inspección general: edad aparente, biotipo, postura, marcha, fascies, color piel/mucosas, hidratación, estado de alerta, lenguaje.',
    'TA &lt;90/60 hipoperfusión; ≥140/90 HTA; asimetría &gt;10 mmHg.\n'
    'FC &gt;100 taquicardia, &lt;60 bradicardia, irregular = arritmia.\n'
    'FR &gt;24 taquipnea (Kussmaul, Cheyne-Stokes), &lt;12 bradipnea.\n'
    'T &gt;38 fiebre, &lt;35 hipotermia.\n'
    'SatO₂ &lt;94 hipoxemia; &lt;88 en EPOC.\n'
    'Mucosas secas / signo del pliegue / llenado capilar &gt;3 s = deshidratación o shock.\n'
    'Fascies: cushingoide, hipertiroidea, mitral, parkinsoniana, urémica.',
    [
        "TA bilateral con diferencia &gt;10 mmHg = disección aórtica o estenosis subclavia.",
        "TA con brazalete pequeño sobreestima 10-30 mmHg; con paciente parado debe caer &lt;20/10 (hipotensión ortostática si mayor).",
        "qSOFA ≥2 (FR ≥22 + alteración mental + TAS ≤100) = sepsis con mortalidad alta — activar protocolo Surviving Sepsis.",
        "SatO₂ &lt;90 = falla respiratoria (PaO₂ ~60); en EPOC objetivo 88-92% para no inhibir centro respiratorio.",
        "IMC ≥25 sobrepeso, ≥30 obesidad, ≥40 mórbida; perímetro abdominal &gt;94 cm H / &gt;80 cm M = obesidad central + riesgo metabólico.",
        "Fascies acromegálica, cushingoide, mitral, esclerodérmica orientan a dx endocrino, cardio o autoinmune sin necesidad de labs.",
        "Llenado capilar &gt;3 s y/o frialdad distal = mala perfusión (shock, hipotermia, vasoconstricción periférica).",
    ],
    "iniciar SIEMPRE por SV completos antes de cualquier otra maniobra.",
    "tomas TA con paciente parado o sin reposo previo, brazalete inadecuado.",
    "ACC/AHA 2017 HTA; Sepsis-3 (Singer 2016); Bates 13ª.",
    "signos_vitales", "inspeccion_general", "universal",
)

make_card(
    "CABEZA-CUELLO", "sis-cuello",
    "EF2 · Cabeza · ORL · cuello · tiroides",
    'Cabeza: cráneo, cuero cabelludo (heridas, masas, hundimientos).\n'
    'Ojos: pupilas (tamaño, simetría, reactividad), conjuntivas, escleras, fondo de ojo, movimientos OCM.\n'
    'ORL: otoscopia (membrana timpánica), tabique nasal, narinas, senos paranasales (Frankenberg).\n'
    'Orofaringe: dientes, encías, lengua, paladar, amígdalas, Mallampati, hidratación.\n'
    'Cuello: inspección + palpación (movilidad, masas, traquea centrada).\n'
    'Tiroides: inspección, palpación bimanual desde atrás mientras el paciente deglute agua.',
    'Pupilas anisocóricas (Horner, herniación), midriasis fija (muerte cerebral, intoxicación anticolinérgica).\n'
    'Conjuntivas pálidas = anemia; ictéricas = hepático/hemólisis.\n'
    'Membrana timpánica eritematosa abombada = OMA; opaca con nivel = otitis serosa.\n'
    'Orofaringe: exudados blanquecinos (Candida), placas (faringitis estreptocócica), úlceras (afta, Behçet).\n'
    'Tiroides: tamaño (Lerma 0-IV OMS), nódulos (consistencia, dolor, movilidad).\n'
    'Tráquea desviada = neumotórax, masa, derrame masivo.',
    [
        "Anisocoria + ptosis + miosis = síndrome de Horner (lesión simpática cervical, Pancoast, disección carotídea).",
        "Midriasis arreactiva unilateral = herniación uncal (urgencia neuroquirúrgica).",
        "Mallampati III-IV + cuello corto + apertura bucal &lt;3 cm = vía aérea difícil (informar a anestesia).",
        "Bocio difuso + oftalmopatía + mixedema pretibial = Graves; nódulo único frío en gammagrafía + microcalcificaciones en USG = ca papilar hasta descartar.",
        "Adenopatía supraclavicular (Virchow / Troisier izquierda) = neoplasia abdominal (gástrico, páncreas) hasta descartar.",
        "Tráquea desplazada contralateral al pulmón hipertimpánico + ↓ ruidos = neumotórax a tensión (descompresión inmediata 2EIC LMC).",
    ],
    "verbalizar 'palpo tiroides desde atrás mientras deglute' y describir tamaño + nódulos.",
    "olvidas explorar pupilas, fondo de ojo en cefalea, o no palpas tiroides en mujer con sospecha endocrina.",
    "Bates 13ª; ATA tiroides 2015; ESMO neoplasias.",
    "cabeza_cuello", "tiroides", "ojos", "universal",
)

make_card(
    "LINFÁTICO", "sis-linf",
    "EF3 · Cadenas ganglionares completas",
    'Cabeza-cuello: occipitales, retroauriculares, preauriculares, submentonianos, submaxilares, cervicales anteriores y posteriores, supraclaviculares.\n'
    'Axila: paciente sentado con brazo apoyado y relajado, palpación profunda en 5 grupos (apical, central, lateral, pectoral, subescapular).\n'
    'Ingle: horizontal e inguinal superficial/profunda, paciente decúbito dorsal.\n'
    'Documentar: tamaño, consistencia, dolor, movilidad, agrupación.',
    'Tamaño: &gt;1 cm cervical/axilar, &gt;1.5 cm inguinal, &gt;0.5 cm supraclavicular = patológico.\n'
    'Consistencia: blanda (inflamatorio), firme (TB, sarcoidosis), pétrea (neoplásico).\n'
    'Dolor: doloroso (infeccioso), no doloroso (neoplásico, TB).\n'
    'Movilidad: móvil (benigno), fijo a planos (neoplásico).\n'
    'Agrupación: conglomerado (TB, linfoma), aislado.',
    [
        "Cualquier adenopatía supraclavicular es PATOLÓGICA hasta demostrar lo contrario (Virchow izq = gástrico/abdominal; derecho = torácico).",
        "Adenopatía generalizada (≥2 cadenas no contiguas) → VIH, EBV/CMV, linfoma, autoinmune, sífilis, sarcoidosis.",
        "Adenopatía indolora, pétrea, fija + síndrome B = linfoma hasta demostrar lo contrario (biopsia escisional).",
        "Adenopatía cervical persistente &gt;3 sem sin causa clara en &gt;40 a → estudio neoplasia ORL, TB, linfoma.",
        "Linfadenitis localizada con eritema y dolor agudo → buscar puerta de entrada (orofaríngea, dérmica, dental).",
        "Adenopatía inguinal aislada puede ser fisiológica (1 cm); patológica si crece o duele.",
    ],
    "explorar SIEMPRE las cadenas pertinentes al MC (ORL si cuello, ITS si inguinal, mama si axila).",
    "no exploras supraclavicular o no documentas tamaño/consistencia/movilidad.",
    "Bates 13ª; NICE NG12; UpToDate 'Evaluation of peripheral lymphadenopathy'.",
    "linfatico", "adenopatias", "universal",
)

make_card(
    "CARDIOVASCULAR", "sis-cardio",
    "EF4 · Cuello vascular: ingurgitación yugular + reflejo HY + carótidas + pulsos centrales",
    'Paciente decúbito 30-45°, cuello relajado en rotación leve.\n'
    'Localizar pulsación de yugular interna entre los haces del ECM.\n'
    'Medir altura vertical del menisco respecto al ángulo de Louis + 5 cm = PVC estimada (cm H₂O).\n'
    'Reflejo hepato-yugular: presión sostenida en HD por 10-15 s.\n'
    'Auscultar carótidas con campana, paciente conteniendo respiración.\n'
    'Palpar pulsos centrales: carotídeo, axilar, braquial, femoral.',
    'IVY visible &gt;3 cm sobre ángulo de Louis (PVC &gt;8 cm H₂O) = sobrecarga venosa.\n'
    'RHY positivo (sostenido &gt;15 s) = IC derecha o falla diastólica.\n'
    'Soplo carotídeo: ateroma; thrill = estenosis significativa.\n'
    'Pulso parvus et tardus carotídeo = estenosis aórtica severa.\n'
    'Pulso bisferiens = doble lesión aórtica o miocardiopatía hipertrófica obstructiva.\n'
    'Pulso celer (Corrigan, en martillo de agua) = insuficiencia aórtica.\n'
    'Ausencia o asimetría de pulsos = coartación, disección aórtica, EAP.',
    [
        "IVY persistente = falla derecha (cor pulmonale, ICC global, valvulopatía tricuspídea, tamponade, pericarditis constrictiva).",
        "PVC &gt;10 cm H₂O + hipotensión + ruidos cardíacos apagados = tríada de Beck (taponamiento).",
        "RHY positivo separa IC derecha (positivo) de hepatopatía pura (negativo).",
        "Soplo carotídeo en paciente &gt;65 a = riesgo de ECV/ictus; pedir USG doppler carotídeo (estenosis ≥70% = revascularización).",
        "Pulso parvus + soplo sistólico irradiado a cuello + síncope de esfuerzo = estenosis aórtica severa (clase I para reemplazo si sintomática).",
        "Asimetría TA braquial &gt;15 mmHg o pulsos asimétricos = disección aórtica hasta descartar (angio-TC).",
        "Ausencia pulsos femorales bilateral = coartación de aorta (típicamente joven con HTA en miembros superiores).",
    ],
    "verbalizar 'IVY a X cm sobre el ángulo de Louis' y 'auscultación carotídea sin soplos'.",
    "no exploras IVY en paciente con disnea o edema, o no auscultas carótidas en &gt;65 a o con sospecha ECV.",
    "ACC/AHA 2020 valvulopatías; Bates 13ª; ESC 2022 disección aórtica.",
    "cardiovascular", "ivy", "carotidas", "universal",
)

make_card(
    "CARDIOVASCULAR", "sis-cardio",
    "EF5 · Precordio: inspección + palpación + percusión",
    'Inspección: tórax simétrico, presencia de pectus, cicatrices (esternotomía, marcapasos), latido visible.\n'
    'Palpación choque de la punta: paciente decúbito dorsal o lateral izquierdo, palma sobre 5° EIC LMC izquierda.\n'
    'Caracterizar: localización, extensión (&lt;2.5 cm normal), amplitud, duración.\n'
    'Buscar frémitos en focos (palmar abierta), pulsación paraesternal izquierda (RV heave).\n'
    'Percusión del área cardíaca: matidez relativa y absoluta.',
    'Choque desplazado lateral/inferior (más allá de LMC o 6° EIC) = cardiomegalia, hipertrofia VI.\n'
    'Choque difuso ("en cúpula") = aneurisma de pared anterior post-IAM, miocardiopatía dilatada.\n'
    'Frémito sistólico foco aórtico = estenosis aórtica severa; en mitral = IM severa.\n'
    'Levantamiento paraesternal izquierdo = hipertrofia VD (cor pulmonale, EP crónico).\n'
    'Matidez cardíaca aumentada = cardiomegalia, derrame pericárdico.',
    [
        "Choque de la punta es el reflejo más simple de la contractilidad y tamaño del VI.",
        "Desplazamiento a la izquierda/abajo + amplitud aumentada = sobrecarga de volumen (IM, IA, anemia, fístulas).",
        "Choque sostenido sin desplazamiento = sobrecarga de presión (HTA, estenosis aórtica).",
        "Frémito (palpación de la vibración del soplo) implica soplo ≥4/6 = lesión significativa.",
        "Pulsación paraesternal izquierda + onda 'a' visible en yugular = hipertensión pulmonar.",
        "Matidez cardíaca borrada (timpanismo) + ↓ ruidos = enfisema; matidez aumentada con choque desplazado = derrame pericárdico o cardiomegalia.",
    ],
    "verbalizar localización del choque ('en 5° EIC LMC, no desplazado, normal').",
    "no palpas el choque o no buscas frémitos en focos.",
    "Bates 13ª; UpToDate 'Examination of the heart'.",
    "cardiovascular", "precordio", "universal",
)

make_card(
    "CARDIOVASCULAR", "sis-cardio",
    "EF6 · Auscultación cardíaca: 4 focos + maniobras dinámicas",
    'Focos:\n'
    ' • Aórtico: 2° EIC paraesternal derecho.\n'
    ' • Pulmonar: 2° EIC paraesternal izquierdo.\n'
    ' • Tricuspídeo: 4° EIC paraesternal izquierdo (xifoides).\n'
    ' • Mitral: 5° EIC LMC izquierda (ápex).\n'
    'Maniobras: decúbito lateral izq (mitral con campana), sedente inclinado hacia adelante en espiración (IA con membrana), Valsalva (↓ todo salvo MCH y prolapso mitral), handgrip (↑ IM/IA), in-/espiración (regla de Carvallo: ↑ derechos en inspiración).',
    'R1 (cierre mitro-tricuspídeo), R2 (cierre Ao-Pulm con desdoblamiento fisiológico en inspiración).\n'
    'R3 (galope ventricular, falla VI o ↑ flujo); R4 (galope auricular, falla diastólica).\n'
    'Soplos: sistólico de eyección (EA, EP, ASD), pansistólico (IM, IT, CIV), diastólico decrescendo (IA, IP), retumbo diastólico (EM, ET), continuo (CAP, fístula AV).\n'
    'Clicks: eyección (válvula bicúspide), mesosistólico no eyectivo (prolapso mitral); chasquido de apertura (EM); roce pericárdico (3 fases).',
    [
        "R3 patológico &gt;40 a = falla VI con dilatación; en jóvenes y embarazadas suele ser fisiológico.",
        "R4 = ↓ distensibilidad VI (HTA, EA, isquemia, miocardiopatía hipertrófica); requiere ritmo sinusal (no audible en FA).",
        "Soplo sistólico foco aórtico irradiado a cuello + pulso parvus = estenosis aórtica severa (clase I reemplazo si sintomática).",
        "Soplo pansistólico apical irradiado a axila = insuficiencia mitral; a borde esternal izquierdo = IT o CIV.",
        "Soplo diastólico decrescendo en foco Ao paciente sentado en espiración = insuficiencia aórtica.",
        "Maniobras dinámicas distinguen MCH (↑ con Valsalva) de EA (↓ con Valsalva) y de IM (↑ con handgrip).",
        "Regla de Carvallo: soplos derechos AUMENTAN en inspiración; izquierdos en espiración.",
    ],
    "auscultar los 4 focos + realizar AL MENOS una maniobra dinámica (decúbito lateral o sentado en espiración).",
    "no realizas maniobras dinámicas o no identificas la fase del ciclo (sistólico vs diastólico).",
    "ACC/AHA 2020 valvulopatías; Carvallo 1946; Bates 13ª.",
    "cardiovascular", "auscultacion", "soplos", "universal",
)

make_card(
    "VASCULAR", "sis-vasc",
    "EF7 · Vascular periférico: pulsos + perfusión + edema + signos TVP + ITB",
    'Pulsos: radial, cubital, braquial, axilar, carotídeo, femoral, poplíteo, tibial posterior, pedio. Comparar bilaterales.\n'
    'Perfusión: temperatura, llenado capilar, color piel, pelo distal, atrofia.\n'
    'Edema: presión digital sobre tibia y maleolar, godet 1+ a 4+, descripción bilateralidad.\n'
    'Signos de TVP: dolor en pantorrilla a la dorsiflexión (Homans), empastamiento, ↑ diámetro &gt;3 cm, calor, eritema, cordón palpable.\n'
    'Índice tobillo-brazo (ITB): TA tibial posterior o pedio / TA braquial mayor.',
    'Pulsos disminuidos/ausentes en MMII = EAP; asimetría &gt;15 mmHg = disección o estenosis subclavia.\n'
    'Frialdad distal + palidez + dolor + parestesias + parálisis (5 P) = isquemia aguda.\n'
    'Úlceras arteriales: pretibiales/maleolares laterales, secas, dolorosas, "en sacabocado".\n'
    'Úlceras venosas: maleolar interno, húmedas, indoloras, fondo granular.\n'
    'Edema bilateral con godet = sistémico (IC, ERC, hipoalbuminemia); unilateral + calor = TVP.\n'
    'ITB &lt;0.9 = EAP; &lt;0.5 = isquemia crítica.',
    [
        "Asimetría de pulsos en miembros superiores = disección aórtica, takayasu, coartación.",
        "Ausencia de pulso pedio + pelo escaso + atrofia = EAP; claudicación intermitente confirma.",
        "Isquemia aguda (Rutherford IIa/b) = urgencia vascular: anticoagular y revascularizar &lt;6 h.",
        "TVP probabilidad pre-test (Wells): combinar puntaje + dímero D + USG compresivo (gold standard).",
        "Homans tiene baja sensibilidad/especificidad — la regla de Wells es más útil.",
        "Edema unilateral en pierna que SIEMPRE pensar TVP, especialmente postoperatorio o inmovilizado.",
        "ITB &gt;1.3 = arterias calcificadas (DM, ERC) — falso negativo; usar índice dedo-brazo o doppler.",
    ],
    "auscultar femorales (soplo = ateroma) + medir ITB en sospecha de EAP.",
    "no comparas pulsos bilateralmente o no mides ITB en paciente con claudicación.",
    "ACC/AHA 2016 EAP; Wells DVT score; Rutherford clasificación EAP; Bates 13ª.",
    "vascular", "pulsos", "tvp", "eap", "universal",
)

make_card(
    "PULMONAR", "sis-pulm",
    "EF8 · Pulmonar: inspección + palpación + percusión",
    'Inspección: simetría, tipo respiratorio (toracoabdominal, costal alta), tiraje (intercostal, supraclavicular, supraesternal), aleteo nasal, cianosis, uso musculatura accesoria, deformidades (cifoscoliosis, tórax en quilla, en tonel).\n'
    'Frecuencia y patrón respiratorio.\n'
    'Palpación: expansibilidad simétrica (manos en bases, pulgares en xifoides), vibraciones vocales pidiendo "treinta y tres".\n'
    'Percusión: comparativa, dedo a dedo, de ápices a bases.',
    'Tiraje + aleteo + cianosis = falla respiratoria.\n'
    'Expansibilidad asimétrica = derrame, neumotórax, atelectasia, consolidación masiva.\n'
    'Vibraciones aumentadas = consolidación (neumonía); disminuidas = derrame, neumotórax, EPOC, obstrucción bronquial.\n'
    'Percusión: claro pulmonar (normal), mate (consolidación, derrame), timpánico (neumotórax, enfisema).\n'
    'Matidez en bases bilateral con ↓ vibraciones = derrame; unilateral asociado a desplazamiento traqueal contralateral = derrame masivo.',
    [
        "Tórax en tonel (↑ diámetro AP) + uso de musculatura accesoria + labios fruncidos = EPOC enfisematoso.",
        "Tórax en quilla o pectus excavatum severo puede comprimir corazón → disnea de esfuerzo.",
        "Expansibilidad ↓ unilateral + matidez + vibraciones ↑ + soplo tubárico = síndrome de condensación (neumonía lobar).",
        "Expansibilidad ↓ unilateral + matidez + vibraciones ↓ + abolición de murmullo = síndrome de derrame pleural.",
        "Expansibilidad ↓ unilateral + timpanismo + vibraciones ↓ + abolición de murmullo = neumotórax.",
        "Vibraciones aumentadas requieren parénquima consolidado con bronquio permeable (transmisión).",
        "Patrón Kussmaul (taquipnea + amplitud aumentada) = acidosis metabólica (DKA, AKI); Cheyne-Stokes = IC, lesión SNC.",
    ],
    "verbalizar 'expansibilidad simétrica, vibraciones vocales normales, percusión claro pulmonar en ambos hemitórax'.",
    "no realizas percusión comparativa o no buscas tiraje.",
    "Bates 13ª; UpToDate 'Examination of the chest'.",
    "pulmonar", "inspeccion", "percusion", "universal",
)

make_card(
    "PULMONAR", "sis-pulm",
    "EF9 · Auscultación pulmonar + transmisión vocal",
    'Auscultación con membrana, paciente respirando profundamente por la boca, sentado, comparativa apex-bases-axilares-posterior.\n'
    'Identificar: murmullo vesicular, soplo traqueal/tubárico/bronquial, broncofonía, egofonía, pectoriloquia áfona.\n'
    'Ruidos agregados: estertores crepitantes (finos/gruesos), sibilancias, roncus, frote pleural, estridor.\n'
    'Pedir al paciente: decir "treinta y tres" (broncofonía), decir "i" (egofonía: se oye "e"), susurrar "uno-dos-tres" (pectoriloquia áfona).',
    'Murmullo vesicular ↓ o abolido = derrame, neumotórax, EPOC, obstrucción bronquial.\n'
    'Soplo tubárico = consolidación (neumonía).\n'
    'Crepitantes finos al final de inspiración: EPI, IC, atelectasia.\n'
    'Crepitantes gruesos: edema agudo de pulmón, neumonía, bronquiectasias.\n'
    'Sibilancias espiratorias: asma, EPOC; en inspiración: estridor (obstrucción alta).\n'
    'Roncus: secreciones bronquiales (movilizan con tos).\n'
    'Frote pleural ("cuero crujiente"): pleuritis, TEP, pericarditis (audible en sístole/diástole).',
    [
        "Egofonía positiva (i→e) en borde superior de derrame = compresión parenquimatosa (síndrome de Skoda) — sutil pero patognomónico.",
        "Pectoriloquia áfona indica consolidación con bronquio permeable; con egofonía = consolidación más densa.",
        "Estridor inspiratorio = obstrucción supraglótica/glótica (epiglotitis, cuerpo extraño, edema laríngeo) → urgencia.",
        "Sibilancia única persistente en mismo sitio = obstrucción local (tumor, cuerpo extraño).",
        "Crepitantes finos bibasales en velcro (no movilizan con tos) = fibrosis pulmonar (EPI).",
        "Crepitantes movilizan con tos = atelectasia o secreciones (pedirle que tosa antes de concluir).",
        "Silencio auscultatorio en asma severo = signo de gravedad (tórax silente) — preparar para intubar.",
    ],
    "incluir TRANSMISIÓN VOCAL al menos una vez; identifica consolidación oculta.",
    "no buscas egofonía/pectoriloquia o no pides toser antes de afirmar crepitantes patológicos.",
    "GINA 2024; GOLD 2024; Bates 13ª; UpToDate 'Lung auscultation'.",
    "pulmonar", "auscultacion", "universal",
)

make_card(
    "ABDOMEN", "sis-abd",
    "EF10 · Abdomen: inspección + auscultación",
    'Paciente decúbito dorsal, brazos a los lados, exposición xifoides-pubis, abdomen relajado.\n'
    'Inspección: contorno (plano/globoso/excavado), simetría, cicatrices, hernias, circulación colateral, estrías, masas visibles, pulsaciones, peristaltismo visible.\n'
    'Auscultación ANTES de palpar (evita alterar RHA): membrana en los 4 cuadrantes 1-2 min cada uno.\n'
    'Auscultar soplos: aórtico (epigastrio), renales (paraumbilical), ilíacos, femorales.',
    'Contorno globoso: obesidad, ascitis, megacolon, embarazo, distensión por gas.\n'
    'Excavado: caquexia, deshidratación severa, obstrucción alta con vómito.\n'
    'Circulación colateral en "cabeza de medusa" = HTP; en flancos = obstrucción vena cava.\n'
    'Estrías violáceas + giba + cara de luna = Cushing; estrías pálidas en gestantes/obesidad.\n'
    'Cicatrices: pensar en bridas → obstrucción.\n'
    'RHA: aumentados (gastroenteritis, obstrucción intestinal incipiente), disminuidos/ausentes (íleo paralítico, peritonitis tardía).\n'
    'Soplo aórtico: AAA, ateroma; soplo renal: estenosis arteria renal (HTA secundaria).',
    [
        "Auscultar ANTES de palpar es regla fundamental — la palpación puede alterar transitoriamente RHA.",
        "RHA hiperactivos + dolor cólico + vómito + distensión = obstrucción mecánica (luchando contra obstáculo).",
        "RHA ausentes &gt;5 min en 4 cuadrantes = íleo paralítico o peritonitis (signo tardío).",
        "Distensión + timpanismo + ausencia eliminación gases = obstrucción intestinal mecánica completa.",
        "Soplo abdominal sistólico-diastólico = AAA (palpar pulsación expansiva &gt;3 cm); riesgo de ruptura si &gt;5.5 cm.",
        "Signo de Cullen (equimosis periumbilical) + Grey-Turner (flancos) = pancreatitis hemorrágica severa o ruptura ectópico.",
        "Caput medusae + ascitis + ictericia + telangiectasias = cirrosis con HTP.",
    ],
    "auscultar SIEMPRE antes de palpar; verbalizar al sinodal el orden.",
    "palpas antes de auscultar (altera RHA).",
    "Bates 13ª; UpToDate 'Acute abdominal pain in adults'.",
    "abdomen", "inspeccion", "auscultacion", "universal",
)

make_card(
    "ABDOMEN", "sis-abd",
    "EF11 · Abdomen: percusión + palpación + visceromegalias + ascitis",
    'Percusión sistemática 4 cuadrantes: timpanismo vs matidez.\n'
    'Matidez hepática: borde superior (4°-5° EIC LMC derecha) y borde inferior (rebasa reborde costal &gt;2 cm = hepatomegalia).\n'
    'Espacio de Traube (8°-12° EIC línea axilar anterior izquierda): timpanismo normal; matidez = esplenomegalia.\n'
    'Palpación superficial (relajada, mano plana): tono, dolor, masas superficiales, signo del rebote.\n'
    'Palpación profunda en 4 cuadrantes: visceromegalias, masas profundas.\n'
    'Hígado: técnica bimanual o de Mathieu; baja con inspiración profunda.\n'
    'Bazo: maniobra de Schuster (paciente en decúbito lateral derecho); palpable solo si crece 2-3 veces su tamaño.\n'
    'Ascitis: matidez desplazable (cambios de decúbito), onda ascítica.',
    'Hepatomegalia: dolorosa (hepatitis, IC), no dolorosa (cirrosis, esteatosis, neoplasia).\n'
    'Borde irregular y duro = cirrosis o metástasis.\n'
    'Esplenomegalia palpable: leucemias, linfomas, HTP, paludismo, mononucleosis, leishmaniasis.\n'
    'Masa pulsátil expansiva en epigastrio = AAA.\n'
    'Masa móvil periumbilical = adenopatías o tumor mesentérico.\n'
    'Vejiga palpable = retención urinaria.\n'
    'Matidez desplazable y onda ascítica positivas = ≥1500 mL ascitis.',
    [
        "Hepatomegalia DOLOROSA: hepatitis aguda, IC derecha (congestiva), absceso, Budd-Chiari.",
        "Hepatomegalia INDOLORA con borde liso: esteatosis, infiltración linfoma; con borde irregular: cirrosis, metástasis.",
        "Bazo palpable SIEMPRE patológico (excepto en niños y delgados con descenso diafragmático).",
        "Esplenomegalia masiva (más allá del ombligo): leucemia mielocítica crónica, mielofibrosis, leishmaniasis visceral, paludismo crónico.",
        "Murphy positivo + colelitiasis sugerente = colecistitis aguda (TG24 grado I-III según severidad).",
        "Onda ascítica requiere ayudante presionando línea media (evita transmisión por TCS); positiva = ≥1500 mL.",
        "Ascitis nueva = paracentesis diagnóstica obligatoria (GASA &gt;1.1 = HTP; &lt;1.1 = no HTP: TB, neoplasia, pancreática).",
    ],
    "verbalizar 'percuto borde superior e inferior hepático' y 'no palpo bazo / palpo bazo a X cm'.",
    "no determinas extensión hepática o no buscas ascitis en paciente con hepatopatía conocida.",
    "AASLD; Tokyo Guidelines 2024; Bates 13ª.",
    "abdomen", "hepatomegalia", "ascitis", "universal",
)

make_card(
    "ABDOMEN AGUDO", "sis-abd",
    "EF12 · Signos peritoneales — Blumberg, Rovsing, McBurney, Murphy, psoas, obturador",
    'Blumberg: presión profunda en FID + liberación brusca → dolor al soltar = positivo.\n'
    'Rovsing: presión FII → dolor referido a FID = positivo.\n'
    'McBurney: dolor a la presión en punto McBurney (1/3 externo línea ombligo-EIAS derecha).\n'
    'Murphy: presión bajo reborde costal derecho mientras paciente inspira profundo → detención inspiratoria por dolor = positivo.\n'
    'Psoas: decúbito lateral izq, extensión pasiva de cadera derecha → dolor = positivo.\n'
    'Obturador: decúbito dorsal, flexión cadera 90° + rotación interna → dolor pélvico = positivo.\n'
    'Buscar también: defensa muscular, contractura involuntaria, abdomen en tabla.',
    'Blumberg + Rovsing + McBurney + psoas/obturador positivos → apendicitis aguda (Alvarado ≥7).\n'
    'Murphy positivo → colecistitis aguda (TG24 grado I-III).\n'
    'Abdomen en tabla + defensa difusa = peritonitis generalizada (perforación de víscera hueca).\n'
    'Signo del psoas positivo aislado → absceso de psoas, apendicitis retrocecal.\n'
    'Signo del obturador positivo → apendicitis pélvica o absceso pélvico.\n'
    'Cullen + Grey-Turner = hemorragia retroperitoneal (pancreatitis hemorrágica, ectópico roto).',
    [
        "Discriminar abdomen quirúrgico vs médico cambia conducta a quirófano en horas.",
        "Alvarado ≥7 + clínica = apendicitis probable → cirugía o imagen (USG/TC); ≤3 = baja probabilidad.",
        "Murphy ecográfico = mejor sens/esp que Murphy clínico para colecistitis (TG24 lo incluye).",
        "Peritonitis generalizada + sepsis = laparotomía emergente (lavado, control del foco, drenaje).",
        "Signo de Carnett (dolor que persiste al contraer abdomen) = origen parietal, no visceral.",
        "Cullen y Grey-Turner aparecen 24-72 h tras inicio; ausencia no descarta.",
        "Mujer fértil con dolor pélvico + Blumberg positivo + amenorrea = ectópico roto hasta descartar (β-hCG urgente).",
    ],
    "nombrar cada signo por nombre propio (Blumberg, Murphy, etc.).",
    "no exploras los 6 signos cuando hay dolor abdominal o no pides al paciente que se relaje.",
    "Tokyo Guidelines 2024; Alvarado 1986; ATLS 10ª; Bates 13ª.",
    "abdomen", "peritonismo", "apendicitis", "colecistitis", "universal",
)

make_card(
    "URINARIO / RECTAL", "sis-uro",
    "EF13 · Puño-percusión renal + tacto rectal + hernias inguinales",
    'Puño-percusión renal (Giordano): paciente sentado, percusión cerrada sobre ángulo costovertebral bilateral.\n'
    'Hernias inguinales: paciente de pie, inspección + palpación de canal inguinal con dedo introducido por anillo inguinal superficial; pedir Valsalva o tos.\n'
    'Tacto rectal: paciente decúbito lateral izq con rodillas flexionadas; inspección externa (hemorroides, fisuras, fístulas), introducción dedo lubricado, evaluar tono esfínter, próstata (H), Douglas y pared posterior vaginal (M), masa, sangre o moco en guante.',
    'Giordano positivo unilateral = pielonefritis, litiasis ureteral, absceso perirrenal.\n'
    'Hernia inguinal indirecta = pasa por anillo profundo, baja al escroto; directa = sale por triángulo de Hesselbach.\n'
    'Tono esfínter ↓ = lesión medular, prolapso rectal; ↑ = fisura, estenosis.\n'
    'Próstata: tamaño (I-IV), simetría, consistencia, nódulos, dolor.\n'
    'Sangre fresca = sangrado bajo (hemorroides, fisura, divertículos, neoplasia).\n'
    'Melena = sangrado alto (úlcera, varices, neoplasia gástrica).',
    [
        "Giordano + leucocituria + fiebre = pielonefritis (urocultivo + antibiótico, evaluar ingreso si embarazo, DM, sepsis).",
        "Hernia inguinal incarcerada (no reductible + dolor) = riesgo de estrangulación → cirugía urgente.",
        "Hernia crural (debajo del ligamento inguinal) tiene MAYOR riesgo de estrangulación que inguinal.",
        "Tacto rectal es OBLIGATORIO en: rectorragia, dolor abdominal agudo, alteración hábito intestinal, sospecha ca próstata, retención urinaria, fecaloma.",
        "Próstata nodular, pétrea, asimétrica = ca próstata hasta descartar (PSA + biopsia).",
        "Próstata aumentada simétrica, elástica, surcos preservados = HBP.",
        "Tacto rectal con sangre fresca + cambio hábito intestinal &gt;50 a = ca colorrectal hasta descartar (colonoscopia).",
        "Saco de Douglas doloroso o abombado = absceso, ectópico roto, EPI, ascitis tabicada.",
    ],
    "verbalizar 'puño-percusión renal negativa bilateral' y 'no palpo hernias inguinales con Valsalva'.",
    "no haces tacto rectal en rectorragia, dolor abdominal agudo o cambio del hábito intestinal &gt;50 a.",
    "AUA HBP 2023; ASCRS; Bates 13ª; UpToDate 'Digital rectal examination'.",
    "urinario", "rectal", "hernias", "universal",
)

make_card(
    "NEUROLÓGICO", "sis-neuro",
    "EF14 · Estado de consciencia + Glasgow + pupilas + signos meníngeos",
    'Estado de alerta: alerta, somnoliento, estuporoso, comatoso.\n'
    'Glasgow Coma Scale (GCS): ocular 1-4, verbal 1-5, motor 1-6 (rango 3-15).\n'
    'Pupilas: tamaño en mm, simetría, reactividad (directa y consensuada).\n'
    'Reflejo corneal, reflejo nauseoso, reflejo oculocefálico (ojos de muñeca).\n'
    'Signos meníngeos: rigidez de nuca, Kernig (flexión cadera 90° + extensión rodilla → dolor/resistencia), Brudzinski (flexión pasiva cuello → flexión refleja caderas).',
    'GCS ≤8 = coma + indicación de intubación (riesgo broncoaspiración).\n'
    'Pupila midriática unilateral arreactiva (Hutchinson) = herniación uncal por hipertensión intracraneal.\n'
    'Pupilas puntiformes reactivas = opioides, lesión pontina (hemorragia).\n'
    'Pupilas midriáticas bilaterales fijas = muerte cerebral, anoxia severa, anticolinérgico.\n'
    'Rigidez de nuca + Kernig + Brudzinski + fiebre + cefalea = meningitis (PL urgente).\n'
    'Rigidez de nuca + cefalea trueno + alteración consciencia = HSA.',
    [
        "GCS ≤8 + cualquier deterioro = intubación inmediata + neuroimagen + traslado a UCI.",
        "Pupilas asimétricas con paciente en coma = herniación inminente — manitol 1 g/kg, hiperventilación leve, neurocirugía.",
        "Síndrome confusional agudo en mayor + cambio cognitivo súbito = DELIRIUM (no demencia); investigar causa (infección, fármacos, dolor, deshidratación).",
        "Cushing (HTA + bradicardia + respiración irregular) = HTIC con riesgo de herniación inminente.",
        "Signos meníngeos pueden ser negativos en niños, ancianos, inmunosuprimidos — bajo umbral para PL.",
        "PL contraindicada si: papiledema, signos focales, GCS ≤8, infección zona de punción, coagulopatía no corregida.",
        "PL en HSA: xantocromía (LCR amarillo &gt;12 h post inicio); TC sin contraste pierde sensibilidad &gt;6 h.",
    ],
    "documentar GCS desglosado (O/V/M) y reactividad pupilar siempre en paciente con alteración del nivel de conciencia.",
    "registras 'consciente y orientado' sin especificar GCS u olvidas el reflejo pupilar en TCE.",
    "Glasgow Teasdale 1974; Brain Trauma Foundation 2017; IDSA meningitis 2017.",
    "neurologico", "consciencia", "glasgow", "meningismo", "universal",
)

make_card(
    "NEUROLÓGICO", "sis-neuro",
    "EF15 · Pares craneales I-XII completos",
    'I Olfato: identificar olor familiar (café, vainilla) cada fosa.\n'
    'II Visión: agudeza (Snellen), campos por confrontación, fondo de ojo (papila, vasos, retina).\n'
    'III, IV, VI: motilidad ocular extrínseca (H del diplopía), pupila intrínseca (III).\n'
    'V: sensibilidad facial 3 ramas + reflejo corneal + función motora (cerrar mandíbula contra resistencia).\n'
    'VII: motilidad facial (frente, ojos, sonrisa), Bell, gusto en 2/3 anteriores lengua.\n'
    'VIII: agudeza auditiva, Rinne (CO &gt; CA si neurosensorial), Weber (lateraliza a oído afectado en conductiva, al sano en neurosensorial).\n'
    'IX, X: úvula central, reflejo nauseoso, voz, deglución.\n'
    'XI: rotación cefálica contra resistencia (ECM) + elevación hombros (trapecio).\n'
    'XII: lengua centrada, movilidad, fasciculaciones.',
    'Anosmia: trauma craneal, meningioma surco olfatorio, COVID, Parkinson, Alzheimer precoz.\n'
    'Defecto campo visual: hemianopsia homónima (lesión retroquiasmática), bitemporal (lesión quiasma, adenoma hipofisario).\n'
    'Diplopía con III: ptosis + midriasis + ojo "abajo y afuera" = aneurisma comunicante posterior hasta descartar.\n'
    'Parálisis facial periférica (toda la hemicara) = Bell, herpes zóster, ictus pontino.\n'
    'Parálisis facial central (preserva frente) = ictus cortical.\n'
    'Disartria + disfagia + ↓ reflejo nauseoso + úvula desviada = lesión bulbar (IX, X).\n'
    'Desviación lengua hacia lado lesión = parálisis hipogloso ipsilateral.',
    [
        "Pares craneales orientan altura de la lesión: I-II = cortical/sensorial; III-IV-VI = mesencéfalo; V-VII = puente; VIII = puente/cerebelo; IX-XII = bulbo.",
        "Parálisis facial periférica completa + dolor retroauricular + alteración gusto = parálisis de Bell (predisponente: HSV, frío); tratar con prednisolona si &lt;72 h.",
        "III par + midriasis = aneurisma comunicante posterior (compresión externa); III par sin midriasis = microvascular (DM, HTA).",
        "Diplopía vertical al mirar abajo y nasal = IV par (típico tortícolis compensatorio).",
        "Diplopía horizontal a un lado = VI par; común en HTIC (no localizadora).",
        "Disfagia + disartria + lateralización lengua = lesión bulbar o suprabulbar (ictus, ELA).",
        "Hemianopsia bitemporal en mujer joven + galactorrea/amenorrea = prolactinoma → IRM + prolactina.",
    ],
    "explorar TODOS los pares al menos brevemente; verbalizar 'pares craneales sin alteraciones, OCM completos'.",
    "no exploras campos visuales, reflejo corneal o función motora del V.",
    "Bates 13ª; UpToDate 'Cranial nerves examination'.",
    "neurologico", "pares_craneales", "universal",
)

make_card(
    "NEUROLÓGICO", "sis-neuro",
    "EF16 · Motor: tono + trofismo + fuerza (MRC 0-5)",
    'Trofismo: inspección y palpación masas musculares — comparativo bilateral, medir perímetros si asimetría.\n'
    'Tono: movilización pasiva de extremidades (flexo-extensión codo, muñeca, rodilla).\n'
    'Fuerza por grupos musculares (MRC 0-5): 0 ninguna; 1 esbozo; 2 movimiento sin gravedad; 3 contra gravedad; 4 contra resistencia parcial; 5 normal.\n'
    'Maniobras de Barré (MS extendidos, palmas arriba con ojos cerrados) y Mingazzini (MMII flexión cadera y rodilla 90°): claudicación = paresia incipiente.\n'
    'Movimientos anormales: temblor, corea, mioclonías, fasciculaciones, distonía.',
    'Atrofia: lesión nervio periférico, denervación crónica, desuso, miopatía.\n'
    'Hipertonía espástica (signo navaja) + hiperreflexia + Babinski = lesión motora superior (córtico-espinal).\n'
    'Hipertonía plástica (rueda dentada) + bradicinesia + temblor reposo = parkinsonismo.\n'
    'Hipotonía + arreflexia + atrofia + fasciculaciones = lesión motora inferior (asta anterior, raíz, plexo, nervio).\n'
    'Hemiparesia con Barré claudicante = ictus contralateral.\n'
    'Paraparesia + nivel sensitivo = lesión medular.\n'
    'Tetraparesia ascendente progresiva días = Guillain-Barré.',
    [
        "Diferenciar LMS (espasticidad + hiperreflexia + Babinski) de LMI (atrofia + fasciculaciones + arreflexia) localiza la lesión.",
        "Síndrome piramidal puro = ictus, EM, mielopatía cervical; atrofia + fasciculaciones + LMS combinado = ELA.",
        "MRC ≤3 = pérdida funcional significativa; déficit súbito = ictus hasta descartar (activar código ictus).",
        "Síndrome cerebeloso ≠ síndrome piramidal (cerebelo: dismetría, disdiadococinesia, ataxia; piramidal: fuerza ↓, espasticidad).",
        "Temblor de reposo (4-6 Hz, cesa con acción) = Parkinson; temblor postural/de acción = esencial, hipertiroideo, fármaco.",
        "Distonía focal (cervical, escribano) puede ser primaria o secundaria a antipsicóticos (síndrome extrapiramidal).",
        "Miastenia gravis = fatigabilidad (debilidad que empeora con esfuerzo); ptosis vespertina + diplopía + edrofonio o test del hielo positivos.",
    ],
    "graduar fuerza con MRC 0-5 en cada grupo muscular evaluado y comparar bilateral.",
    "registras 'fuerza conservada' sin especificar MRC o no haces Barré/Mingazzini.",
    "MRC scale (1981); Bates 13ª; UpToDate 'Motor examination'.",
    "neurologico", "motor", "fuerza", "universal",
)

make_card(
    "NEUROLÓGICO", "sis-neuro",
    "EF17 · Sensitivo + ROTs + reflejos patológicos",
    'Sensibilidad superficial: tacto (algodón), dolor (punta roma), temperatura (tubos fríos/calientes) — comparar bilateral y por dermatomas.\n'
    'Sensibilidad profunda: vibración (diapasón 128 Hz en maléolo), propiocepción (movilización pasiva de dedo con ojos cerrados), grafestesia, estereognosia.\n'
    'Reflejos osteotendinosos (ROT, escala 0-4+): bicipital (C5-C6), tricipital (C7), estilo-radial (C6), patelar (L3-L4), aquíleo (S1).\n'
    'Reflejos cutáneos: abdominales, cremasterianos, plantar.\n'
    'Reflejos patológicos: Babinski (extensión del 1er dedo + abanico), Hoffmann (flexión 2°-3° dedos al pellizcar 3°), clonus aquíleo.',
    'Hipoestesia en guante y calcetín = polineuropatía (DM, OH, B12).\n'
    'Hipoestesia con nivel = lesión medular transversal.\n'
    'Hipoestesia con distribución dermatómica = lesión radicular.\n'
    'Hemihipoestesia = lesión hemisférica contralateral.\n'
    'ROT 0 = arreflexia (lesión LMI, neuropatía); 4+ = hiperreflexia (LMS, hipertiroidismo, ansiedad).\n'
    'Babinski positivo + hiperreflexia + espasticidad = lesión motora superior.\n'
    'Vibración ↓ + propiocepción ↓ + Romberg+ = ataxia sensitiva (cordón posterior, B12, tabes).',
    [
        "Sensibilidad por dermatomas localiza la raíz: pezón = T4; ombligo = T10; ingle = L1; rodilla = L3-L4; maléolo lateral = S1.",
        "Patrón en guante y calcetín simétrico distal sugiere polineuropatía (DM #1, también OH, B12, fármacos, urémica).",
        "Lhermitte (descarga eléctrica al flexionar cuello) = lesión cervical (EM, espondilosis, B12).",
        "Babinski POSITIVO en mayor &gt;1 año = lesión motora superior (ictus, EM, tumor, mielopatía).",
        "Hoffmann positivo bilateral = sospecha mielopatía cervical (ojo en pacientes con dolor cervical y debilidad).",
        "Clonus aquíleo sostenido (&gt;6 batidas) = lesión LMS clara.",
        "Pérdida sensibilidad disociada (térmico-algésica conservada, propio-vibratoria abolida) = lesión cordones posteriores (B12, tabes, EM).",
        "Pérdida térmica-algésica con táctil conservada = lesión espinotalámica (siringomielia, infarto medular anterior).",
    ],
    "explorar dermatomas + ROTs + Babinski en todo paciente con déficit neurológico.",
    "no exploras vibración y propiocepción en sospecha de B12 o tabes; omites Babinski.",
    "Bates 13ª; UpToDate 'Sensory examination' y 'Reflexes'.",
    "neurologico", "sensibilidad", "reflejos", "universal",
)

make_card(
    "NEUROLÓGICO", "sis-neuro",
    "EF18 · Cerebelo + coordinación + marcha + Romberg",
    'Coordinación apendicular: dedo-nariz, talón-rodilla, movimientos alternos rápidos (prono-supinación) = disdiadococinesia.\n'
    'Equilibrio estático: Romberg (pies juntos, brazos extendidos, ojos abiertos y luego cerrados — registrar caída).\n'
    'Marcha: marcha normal, marcha en tándem (talón-punta en línea), marcha de puntillas (S1) y talones (L4-L5), giros.\n'
    'Observar: base de sustentación, lateralización, balanceo de brazos, postura, dificultades específicas.',
    'Dismetría (sobrepasa el blanco), descomposición del movimiento, temblor de intención = lesión cerebelosa ipsilateral.\n'
    'Disdiadococinesia = cerebelo.\n'
    'Romberg POSITIVO (cae con ojos cerrados) = ataxia sensitiva o vestibular (NO cerebelosa — el cerebelo cae con ojos abiertos también).\n'
    'Marcha cerebelosa: ebria, ampliada, lateralizada.\n'
    'Marcha parkinsoniana: pequeña, festinante, sin balanceo brazos, dificultad para girar.\n'
    'Marcha en estepaje: caída pie por debilidad dorsiflexor (peroneo común, L4-L5).\n'
    'Marcha hemiparética: pierna espástica en hoz, brazo flexionado.\n'
    'Marcha apráxica (magnética): pies pegados al suelo (hidrocefalia normotensiva, lesión frontal).',
    [
        "Lesión hemisferio cerebeloso = signos IPSILATERALES (clave diagnóstica vs hemisferio cerebral que da contralaterales).",
        "Lesión cerebelo vermiano (medio) = ataxia troncular, marcha ebria, sin dismetría apendicular.",
        "Romberg requiere INTEGRIDAD CEREBELOSA; si cerebelo está lesionado, cae con ojos abiertos también (no es 'Romberg').",
        "Hidrocefalia normotensiva (Hakim-Adams): tríada marcha apráxica + incontinencia + demencia → derivación VP cuando se confirma.",
        "Marcha de pato = miopatía proximal (debilidad glúteos): Duchenne, polimiositis, hipotiroidismo, esteroide.",
        "Marcha en estepaje unilateral = lesión peroneo común; bilateral = polineuropatía severa (CMT, DM).",
        "Test de los 4 stages of dual task = riesgo de caídas en mayor; Timed Up and Go &gt;12 s = ↑ riesgo de caídas.",
    ],
    "siempre evaluar MARCHA antes de cerrar el exámen neurológico — discrimina mucha patología.",
    "no exploras marcha o no realizas Romberg en paciente con ataxia o vértigo.",
    "Bates 13ª; MDS Parkinson 2015; UpToDate 'Gait disorders'.",
    "neurologico", "cerebelo", "marcha", "universal",
)

make_card(
    "MSK", "sis-msk",
    "EF19 · GALS rápido + maniobras articulares clave",
    'GALS screening (Gait-Arms-Legs-Spine, Doherty 1992):\n'
    ' • Gait (marcha): caminar, girar, regresar.\n'
    ' • Arms: brazos extendidos, manos en nuca, prono-supinación, abrir-cerrar puños.\n'
    ' • Legs: paciente decúbito, flexión cadera, rotación interna, tumefacción rodilla, palpación.\n'
    ' • Spine: paciente parado, "tóquese los dedos de los pies", Schober (≥5 cm flexión lumbar).\n'
    'Maniobras articulares:\n'
    ' • Hombro: Hawkins, Neer (pinzamiento subacromial); Jobe (supraespinoso).\n'
    ' • Rodilla: Lachman, cajón anterior (LCA), McMurray (menisco), Apley.\n'
    ' • Cadera: FABER (sacroilíaca), FADIR (pinzamiento femoroacetabular).\n'
    ' • Muñeca: Finkelstein (De Quervain), Phalen y Tinel (túnel del carpo).',
    'Restricción de rotación interna cadera = coxartrosis o sinovitis.\n'
    'Schober &lt;5 cm = espondilitis anquilosante.\n'
    'Lachman + cajón anterior = ruptura LCA.\n'
    'McMurray positivo = lesión meniscal.\n'
    'Phalen + Tinel + atrofia tenar = STC.\n'
    'Sinovitis (tumefacción + calor + dolor + limitación) en pequeñas articulaciones simétricas = AR.\n'
    'Monoartritis aguda con calor + eritema severo = artritis séptica o gota hasta descartar (artrocentesis).\n'
    'Dolor punto medio inguinal con FABER = patología cadera/sacroilíaca.',
    [
        "GALS es screening; identifica articulación afectada en &lt;3 min para profundizar.",
        "Monoartritis aguda CALIENTE + fiebre + ↑ reactantes = artritis séptica HASTA descartar (artrocentesis urgente, cultivo, líquido sinovial).",
        "AR temprana: sinovitis simétrica de muñecas, MCF, IFP &gt;6 sem + factor reumatoide / anti-CCP → reumatología (DMARDs).",
        "Schober disminuido + dolor inflamatorio (matutino, mejora con ejercicio) + HLA-B27 + sacroileítis radiológica = espondiloartritis.",
        "Lachman es el test más sensible para LCA aguda (especialmente con derrame, donde cajón anterior pierde sensibilidad).",
        "STC + síndrome del túnel cubital + Raynaud + atrofia tenar = pensar en enfermedades sistémicas (hipotiroidismo, AR, amiloidosis).",
        "Hombro doloroso nocturno + Hawkins/Neer positivos + Jobe positivo = pinzamiento + lesión manguito rotador.",
        "Dolor lumbar con red flags (sx neurológicos, baja peso, fiebre, traumatismo, &lt;20 o &gt;55 a, esteroides) = NEUROIMAGEN urgente.",
    ],
    "iniciar SIEMPRE por GALS y luego profundizar en la articulación afectada con maniobras específicas.",
    "evalúas una articulación sin GALS previo o no usas Lachman/Schober/Phalen cuando corresponde.",
    "Doherty Ann Rheum Dis 1992 (GALS); ACR 2020; EULAR 2023; Bates 13ª.",
    "msk", "gals", "articular", "universal",
)

make_card(
    "PIEL / METABÓLICO", "sis-piel",
    "EF20 · Piel + faneras + pie diabético",
    'Inspección general: color, hidratación, temperatura, lesiones primarias (mácula, pápula, vesícula, pústula, nódulo) y secundarias (escama, costra, úlcera, cicatriz).\n'
    'Distribución: localizada, generalizada, simétrica, fotodistribución, dermatomas.\n'
    'Lunares: ABCDE (Asimetría, Bordes irregulares, Color heterogéneo, Diámetro &gt;6 mm, Evolución).\n'
    'Faneras: uñas (acropaquia, coiloniquia, manchas), pelo (alopecia, hirsutismo).\n'
    'Pie diabético: inspección (puntos de presión, callos, úlceras, color, pulsos), monofilamento Semmes-Weinstein 10 g en 10 puntos plantares, diapasón 128 Hz en hallux, ITB.',
    'Acropaquia ("dedos en palillo de tambor") = hipoxemia crónica, neoplasia pulmonar, EII, cardiopatía cianógena.\n'
    'Coiloniquia (uña en cuchara) = anemia ferropénica.\n'
    'Eritema palmar + telangiectasias + ictericia = hepatopatía crónica.\n'
    'Petequias + equimosis + sangrado mucoso = trombocitopenia.\n'
    'Acantosis nigricans (axilas, cuello aterciopelado oscuro) = resistencia a insulina, malignidad oculta.\n'
    'Lesión ABCDE positiva = melanoma sospechoso → biopsia escisional.\n'
    'Pie diabético: ulcera plantar (presión), úlcera por arteriopatía (distal, dolorosa), neuropatía (insensible al monofilamento).',
    [
        "Acropaquia adquirida + tos + ↓ peso + hemoptisis = cáncer de pulmón hasta descartar.",
        "ABCDE en lunar y/o crecimiento rápido = melanoma → biopsia escisional con márgenes, NO afeitada (subestima profundidad Breslow).",
        "Acantosis nigricans en adulto con cambio rápido + delgadez = paraneoplásico (gástrico, pulmonar) — diferenciar de la asociada a resistencia a insulina.",
        "Pie diabético + monofilamento ausente en ≥4 puntos = neuropatía sensitiva = riesgo de úlcera neuropática (educación + calzado + revisión c/3-6 m).",
        "Úlcera plantar redonda indolora con callo perilesional = neuropática; úlcera dolorosa distal pálida con pulsos ausentes = arteriopática.",
        "Charcot del pie diabético: edema + calor + deformidad sin trauma + insensibilidad → inmovilización + descarga + valoración multidisciplinaria.",
        "Lesiones cutáneas en alas de mariposa fotosensibles + artritis + serositis = LES (ANA + criterios SLICC/EULAR).",
        "Eritema migratorio + diana = enfermedad de Lyme (zona endémica + picadura garrapata).",
    ],
    "incluir SIEMPRE monofilamento y pulsos pedios en DM &gt;10 años o con neuropatía sospechosa.",
    "examinas DM sin valorar pie diabético o pasas por alto pulsos pedios.",
    "ADA 2025 'Diabetes care: foot exam'; AAD 2024; Bates 13ª.",
    "piel", "pie_diabetico", "universal",
)


# ============================================================
# B · ESPECIALES POR ESTACIÓN — 5 cards
# ============================================================

make_card(
    "CIRUGÍA / ATLS", "sis-cx",
    "ESP1 · ABCDE de ATLS verbalizado (politraumatizado)",
    'A — Airway con control cervical: hablar al paciente (si responde, vía permeable). Si compromiso: maniobra frente-mentón (no en trauma) o tracción mandibular, aspiración, cánula orofaríngea/nasofaríngea, vía aérea definitiva si GCS ≤8.\n'
    'B — Breathing: inspección, palpación tórax (enfisema, dolor), percusión, auscultación bilateral. Identificar y tratar las 4 letales: neumotórax a tensión, neumotórax abierto, hemotórax masivo, tórax inestable.\n'
    'C — Circulation: pulso, llenado capilar, color piel, PA, FC. Acceso vascular ×2 calibre grueso. Identificar 5 sitios sangrado (tórax, abdomen, pelvis, retroperitoneo, huesos largos).\n'
    'D — Disability: AVPU o GCS, pupilas, déficit motor.\n'
    'E — Exposure: desvestir + voltear con control cervical (log-roll), evitar hipotermia.\n'
    'Anexos: monitorización, SV, SNG, sonda Foley (si no contraindicación: sangre en meato, equimosis perineal, próstata alta), RX tórax/pelvis, FAST.',
    'A: estridor + ronquido + sangre/secreciones = obstrucción → intubación.\n'
    'B: timpanismo + ↓ ruidos + IVY + desplazamiento traqueal = neumotórax a tensión.\n'
    'B: matidez + ↓ ruidos = hemotórax (masivo si &gt;1500 mL inicial o &gt;200 mL/h × 4 h).\n'
    'C: pulso filiforme + frialdad + llenado capilar &gt;3 s + alteración mental = shock; clasificación I-IV ATLS.\n'
    'D: GCS &lt;8 = intubar; anisocoria = herniación.\n'
    'E: lesiones ocultas en espalda/perineo/axilas; hipotermia agrava coagulopatía.',
    [
        "ABCDE es SECUENCIAL — no avanzar hasta resolver el problema actual (concepto 'kills first').",
        "Neumotórax a tensión = clínico, NO esperar Rx → toracocentesis 2EIC LMC o 4-5 EIC LMA con angiocath ≥14G.",
        "Hemotórax masivo = toracotomía si débito inicial &gt;1500 mL o sangrado persistente &gt;200 mL/h × 4 h.",
        "Tríada de la muerte: hipotermia + acidosis + coagulopatía → control de daños quirúrgico, NO cirugía definitiva.",
        "Shock clase III-IV (pérdida &gt;30%) = transfusión masiva (proporción 1:1:1 plasma:plaquetas:eritrocitos).",
        "Pelvic binder + ácido tranexámico (&lt;3 h) reduce mortalidad en politraumatizado con sangrado significativo (CRASH-2).",
        "FAST positivo + paciente inestable = laparotomía exploradora; FAST negativo no descarta lesión retroperitoneal.",
        "Sondaje vesical contraindicado si: sangre en meato, equimosis perineal, próstata alta, fractura pélvica con sospecha de lesión uretral.",
    ],
    "verbalizar en voz alta CADA letra (A, B, C, D, E) y los hallazgos que justificas en cada paso.",
    "saltas pasos, no controlas cervical en A, no buscas las 4 letales de B.",
    "ATLS 10ª (ACS); CRASH-2 Lancet 2010; STARS pelvic binder; Brain Trauma Foundation 2017.",
    "cirugia", "atls", "trauma",
)

make_card(
    "GYO / MF", "sis-gyo",
    "ESP2 · Exploración mamaria + axilar",
    'Inspección con paciente sentada, brazos al lado, después en jarra, después manos en nuca, después inclinada hacia adelante:\n'
    ' • Simetría, contorno, piel (eritema, piel de naranja, retracción), pezón (inversión nueva, secreción), surco inframamario.\n'
    'Palpación con paciente decúbito dorsal + brazo bajo la cabeza del lado a explorar:\n'
    ' • Recorrer 4 cuadrantes en espiral o líneas paralelas con pulpejos de 3 dedos en presión leve-media-profunda.\n'
    ' • Cola axilar (de Spence), región subareolar.\n'
    ' • Pezón: comprimir levemente para evaluar secreción.\n'
    'Axila: paciente sentada con brazo apoyado relajado; palpación 5 grupos (apical, central, lateral, pectoral, subescapular).',
    'Nódulo dominante: tamaño, forma, consistencia, movilidad, dolor, bordes, fijación a piel o pectoral.\n'
    'Maligno sugerente: duro, irregular, fijo, indoloro, &gt;2 cm.\n'
    'Benigno sugerente: blando, móvil, redondeado, regular (fibroadenoma joven; quiste palpable y doloroso premenstrual).\n'
    'Piel de naranja + induración + eritema + calor = mastitis carcinomatosa.\n'
    'Pezón con retracción nueva, eccema unilateral persistente, secreción serosanguinolenta unilateral espontánea = sospecha de neoplasia.\n'
    'Adenopatía axilar firme o pétrea + masa mamaria = ca mama (BIRADS) hasta descartar.',
    [
        "Examen clínico mamario óptimo: 7-10 días postmenstrual (menor congestión).",
        "Maniobra con manos en nuca y luego inclinada hacia adelante detecta retracciones sutiles por fijación a piel.",
        "Secreción patológica: unilateral, uniductal, espontánea, sanguinolenta, asociada a masa = papiloma intraductal o ca; ductografía o resección.",
        "Eccema unilateral del pezón que no responde a tópico = enfermedad de Paget hasta descartar (biopsia).",
        "Masa palpable + USG + mamografía + biopsia = triple test (gold standard diagnóstico).",
        "Cualquier masa nueva en mujer &gt;30 años = imagen + biopsia, no observación.",
        "BIRADS 4-5 obliga biopsia (preferentemente core); BIRADS 3 control en 6 meses.",
        "Ca mama inflamatorio (mastitis carcinomatosa) = piel de naranja + eritema difuso = T4d, pronóstico agresivo → biopsia urgente.",
    ],
    "verbalizar las posiciones de inspección (4) y describir nódulo por tamaño + consistencia + movilidad.",
    "exploras mama sin las 4 posiciones de inspección u olvidas la cola axilar.",
    "ACOG; ACS Screening; BIRADS 5ª ed (ACR); Williams Gynecology 4ª.",
    "mama", "axila", "gineco",
)

make_card(
    "GYO RESUMEN", "sis-gyo",
    "ESP3 · Exploración gineco-obstétrica — 5 momentos clave (cross-link a Gineco Capa 2)",
    'Los 5 momentos del examen gineco-obstétrico:\n'
    '1. Inspección general + abdomen obstétrico (altura uterina, contorno, cicatrices).\n'
    '2. Maniobras de Leopold (1ª situación, 2ª posición, 3ª presentación, 4ª encajamiento) + FCF con Doppler.\n'
    '3. Exploración mamaria (ver ESP2).\n'
    '4. Vulvoperineoscopia + especuloscopia (visualización cuello, toma citología/cultivos).\n'
    '5. Tacto bimanual: útero (tamaño, posición, consistencia), anexos, fondos de saco (Douglas).\n'
    '(Versión detallada de cada paso → deck "Gineco-Obstetricia Adulto::Capa 2 - Exploracion Verbalizada".)',
    'Altura uterina (cm) ≈ SDG entre 20-32 SDG.\n'
    'Leopold 4ª maniobra: cabeza encajada cuando los dedos no logran rodear el polo cefálico.\n'
    'FCF normal 110-160 lpm; bradicardia &lt;110 prolongada = sufrimiento fetal.\n'
    'Cuello cerrado + posterior + duro = no en trabajo de parto; abierto, central, blando = trabajo de parto activo.\n'
    'Sangrado vaginal sin dolor &gt;20 SDG = placenta previa (NO TACTO hasta descartar con USG); con dolor + hipertonía = DPPNI.\n'
    'Fondo de saco abombado y doloroso = ectópico, absceso, EPI; masa anexial = quiste, embarazo ectópico, tumor.',
    [
        "Maniobras de Leopold se hacen ≥28 SDG; antes no son confiables (feto pequeño se moviliza).",
        "Sangrado del 3er trimestre + paciente estable + sin contracciones = NO TACTO hasta excluir placenta previa (USG primero).",
        "Especuloscopia se hace ANTES del tacto bimanual (evita arrastrar células del canal y contaminar muestras).",
        "Tacto bimanual obligatorio en dolor pélvico, sangrado anormal, dispareunia, sospecha EPI, masa anexial.",
        "Saco de Douglas doloroso + amenorrea + ginecorragia escasa = ectópico hasta descartar (β-hCG + USG TV).",
        "Útero retroverso retrovertido es normal en 25% mujeres; útero fijo, doloroso y nodular = endometriosis o EPI crónica.",
        "Cervicitis mucopurulenta + cuello friable = clamidia/gonorrea (PCR + tratamiento empírico CDC 2024).",
        "Para detalle exhaustivo de cada maniobra y maniobra → ver deck Gineco-Obstetricia Adulto Capa 2 ya en repo.",
    ],
    "verbalizar el orden CORRECTO de los 5 momentos; nombrar las 4 maniobras de Leopold.",
    "tactas antes de espéculo, o haces tacto sin haber descartado placenta previa en sangrado 3T.",
    "ACOG; Williams Obstetrics 26ª; FIGO; deck propio Gineco-Obstetricia Capa 2.",
    "gineco", "obstetrico", "leopold", "tacto",
)

make_card(
    "PEDIATRÍA LACTANTE", "sis-ped",
    "ESP4 · Fontanela + perímetro cefálico + Ortolani-Barlow + reflejos arcaicos",
    'Fontanela anterior: palpación con paciente sentado/quieto; tamaño (rombo, 1-3 cm), consistencia (plana, deprimida, abombada), pulso, cierre (12-18 m).\n'
    'Fontanela posterior: cierra a los 2-3 meses; anterior 9-18 m.\n'
    'Perímetro cefálico: cinta sobre occipucio + glabela; comparar con percentiles OMS por edad y sexo.\n'
    'Ortolani: lactante decúbito dorsal, caderas y rodillas flexionadas 90°, abducción suave de cadera con presión hacia adelante → "clunk" si reduce cadera luxada.\n'
    'Barlow: misma posición, aducción + presión posterior → "clunk" si cadera luxable.\n'
    'Reflejos arcaicos: Moro, prensión palmar, prensión plantar, búsqueda, succión, marcha automática, tónico cervical asimétrico, Galant.',
    'Fontanela ABOMBADA = HTIC (meningitis, hidrocefalia, hemorragia, masa); DEPRIMIDA = deshidratación.\n'
    'Cierre tardío (&gt;18 m): hipotiroidismo, hidrocefalia, raquitismo, acondroplasia, síndromes genéticos.\n'
    'Cierre precoz: craneosinostosis (escafocefalia, plagiocefalia) — derivar neurocirugía si afecta forma o crecimiento.\n'
    'Macrocefalia (PC &gt;p97): hidrocefalia, macrosomía, megalencefalia familiar.\n'
    'Microcefalia (PC &lt;p3): TORCH, hipoxia perinatal, genético, Zika.\n'
    'Ortolani/Barlow positivos: displasia evolutiva de cadera → USG inmediato (&lt;6 m) o Rx (&gt;6 m).\n'
    'Reflejos arcaicos persistentes &gt;6 m o ausentes en RN = lesión neurológica.',
    [
        "Fontanela anterior abombada en lactante febril = MENINGITIS hasta descartar (PL).",
        "Perímetro cefálico ↑↑ con percentil cruzando bandas = hidrocefalia (USG transfontanelar si &lt;1 año, IRM después).",
        "DEC (displasia evolutiva de cadera) factores de riesgo: niñas, primogénita, presentación pélvica, AHF, oligohidramnios → screen rutinario.",
        "Ortolani sale negativo después de 3-4 m (cadera ya organizada); evaluar con limitación de abducción, asimetría de pliegues, signo de Galeazzi.",
        "Reflejo de Moro asimétrico = lesión clavicular, plexo braquial (Erb-Duchenne), hemiparesia.",
        "Reflejo tónico cervical asimétrico persistente &gt;6 m = PCI.",
        "Macrocefalia rápidamente progresiva + vómitos + somnolencia = HTIC → URGENCIA.",
        "Tortícolis congénita + plagiocefalia posicional = derivar a fisioterapia + casco si severo.",
    ],
    "verbalizar 'fontanelas normotensas, PC en p50, Ortolani/Barlow negativos, reflejos arcaicos presentes simétricos'.",
    "no exploras Ortolani/Barlow en lactante o no documentas PC.",
    "AAP Bright Futures 2022; AAOS DEC; NICE NG143.",
    "pediatria", "lactante", "fontanela", "cadera",
)

make_card(
    "PEDIATRÍA ADOLESCENTE", "sis-ped",
    "ESP5 · Tanner + Adams (escoliosis) + valoración puberal",
    'Tanner mamario y vello púbico (mujeres) — 5 estadios:\n'
    ' • Mama 1 prepuberal · 2 botón mamario · 3 elevación mama y areola · 4 areola sobreelevada · 5 adulto.\n'
    ' • Vello púbico 1 ausente · 2 ralo lacio · 3 oscuro rizado · 4 abundante triangular · 5 adulto extensión muslos.\n'
    'Tanner genitales y vello púbico (hombres) — 5 estadios:\n'
    ' • Genitales 1 prepuberal · 2 aumento testículo (&gt;3 mL, Prader) · 3 alargamiento pene · 4 oscurecimiento + ↑ glande · 5 adulto.\n'
    'Maniobra de Adams: paciente flexiona tronco con brazos colgando, ojos del examinador a nivel de la espalda; observar giba.\n'
    'Medir auxológica: talla, peso, IMC, velocidad de crecimiento.',
    'Pubertad precoz: caracteres sexuales &lt;8 a niñas, &lt;9 a niños — derivar endocrino (estudio causa: idiopática vs SNC vs gonadal).\n'
    'Pubertad tardía: ausencia caracteres &gt;13 a niñas, &gt;14 a niños — descartar Turner, Klinefelter, hipogonadismo hipogonadotrópico.\n'
    'Menarquia: en promedio Tanner 4 mamario (2-2.5 años post telarquia); ciclo irregular primeros 2-3 años es normal.\n'
    'Adams positivo (giba ≥7° escoliómetro Bunnell o &gt;5°) = escoliosis idiopática → Rx PA columna completa.\n'
    'Escoliosis: ángulo Cobb &lt;25° observación; 25-40° corsé; &gt;40° o progresión rápida = cirugía.',
    [
        "Tanner es la valoración objetiva del desarrollo puberal — más útil que sólo edad cronológica.",
        "Pubertad precoz central (LHRH activa) vs periférica (hiperandrogenismo, McCune-Albright) tiene manejo diferente.",
        "Menarquia &lt;9 a o ausencia &gt;15 a = amenorrea primaria → estudio (cariotipo, GnRH, USG pélvico).",
        "Escoliosis idiopática del adolescente: prevalencia ~3%, predomina niñas, mayoría se detecta entre 10-14 a.",
        "Escoliosis dolorosa = patológica (osteoblastoma, osteoma osteoide, infección, neoplasia) → IRM.",
        "IMC ≥p85 = sobrepeso; ≥p95 = obesidad (CDC y OMS pediátrica).",
        "Trastorno de la conducta alimentaria: descenso percentil súbito + obsesión con peso/imagen + restricción alimentaria → tamizar SCOFF.",
        "Adolescente embarazada o con ITS = consulta confidencial; ofrecer anticoncepción y prevención secundaria.",
    ],
    "explorar Tanner respetando intimidad, presencia de chaperona/cuidador, lenguaje claro y no juzgador.",
    "no estadificas Tanner o no realizas Adams en adolescente en consulta preventiva.",
    "AAP Bright Futures 2022; SRS escoliosis 2021; Marshall & Tanner 1969-1970.",
    "pediatria", "adolescente", "tanner", "escoliosis",
)


# ============================================================
# GENERAR .APKG
# ============================================================
if __name__ == "__main__":
    output_path = os.path.join(
        OUTPUT_DIR,
        "Preparacion_Verbalizada_Deck2_Exploracion_Basica.apkg",
    )
    genanki.Package(deck).write_to_file(output_path)
    print(f"✓ Generado: {output_path}")
    print(f"  Total notas: {len(deck.notes)}")
    print(f"  Deck ID: {DECK_ID}")
    print(f"  Deck name: {DECK_NAME}")
