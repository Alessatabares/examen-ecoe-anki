# -*- coding: utf-8 -*-
"""Deck 1 — Interrogatorio Universal por estación ECOE.

Formato Q&A con FLIP pedagógico:
- Front: QUÉ verbalizar (guion listo para el sinodal).
- Back: POR QUÉ se pregunta cada cosa (razonamiento clínico defendible).

Cobertura:
- 9 cards Marco Universal (aplican a todas las estaciones).
- 31 cards Variantes específicas por estación (MF, MI, Cx, Ped, Psiq, GyO).
- 1 card Transversal mujer fértil (recordatorio antes de Rx/fármaco/cx).
- Total: 41 cards.

Tags por estación → filtrar con "Custom Study by tag" en Anki.

Guías: Bates 13ª + Calgary-Cambridge + UpToDate + USPSTF 2025 + ACIP 2025 +
ACOG + Williams 26ª + ATLS 10ª + DSM-5-TR + Columbia C-SSRS + AAP Bright
Futures + AUDIT/CAGE + NOM-004-SSA3.
"""
import os
import genanki

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "output")
os.makedirs(OUTPUT_DIR, exist_ok=True)

MODEL_QA_ID = 1607392320  # reusable Q&A (mismo que C5-C7)
DECK_ID = 1647829513      # nuevo, único — registrar en ids.json
DECK_NAME = "Preparación Verbalizada::Deck 1 - Interrogatorio Universal"

# ============================================================
# CSS — badge por estación, secciones marcadas en back
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
  font-size: 12px; letter-spacing: 0.8px; font-weight: 700;
  text-transform: uppercase;
}
.est-universal { background: #4338ca; }
.est-mf        { background: #047857; }
.est-mi        { background: #0e7490; }
.est-cx        { background: #b91c1c; }
.est-ped       { background: #c2410c; }
.est-psiq      { background: #7e22ce; }
.est-gyo       { background: #be185d; }
.est-transv    { background: #b45309; }

.titulo { font-size: 16px; font-weight: 700; color: #111;
          margin: 0 0 10px 0; }
.guion  { color: #2563eb; font-weight: 500;
          background: #eff6ff; border-left: 3px solid #2563eb;
          padding: 10px 14px; margin: 8px 0; border-radius: 3px;
          white-space: pre-line; }

.seccion { margin-top: 14px; font-weight: 700; font-size: 13px;
           letter-spacing: 0.5px; text-transform: uppercase;
           color: #374151; }
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
BASE_TAGS = ["interrogatorio", "ecoe", "preparacion_verbalizada"]


def make_card(badge_text, badge_class, titulo, preguntas, porque,
              ecoe_tip, penaliza, fuente, *extra_tags):
    """Genera una nota Q&A con front=guion, back=razonamiento."""
    front = (
        f'<div class="badge {badge_class}">{badge_text}</div>'
        f'<div class="titulo">{titulo}</div>'
        f'<div class="guion">{preguntas}</div>'
    )
    porque_html = "".join(f"<li>{p}</li>" for p in porque)
    back = (
        f'<div class="seccion">¿Por qué se pregunta cada cosa?</div>'
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
# MARCO UNIVERSAL — 9 cards (aplican a todas las estaciones)
# ============================================================

make_card(
    "UNIVERSAL", "est-universal",
    "U1 · Presentación + consentimiento + privacidad",
    'Buenos días, soy [nombre], médico/a en formación.\n'
    '¿Me permite hacerle algunas preguntas y revisarlo/a?\n'
    'Si lo prefiere, podemos hablar a solas o con su acompañante.\n'
    'Todo lo que me comparta es confidencial.',
    [
        "Saludo + identificación construye alianza terapéutica (Calgary-Cambridge); reduce ansiedad y mejora información obtenida.",
        "Consentimiento verbal es obligación ética y legal (NOM-004-SSA3-2012 expediente clínico).",
        "Ofrecer privacidad permite que aflore violencia, abuso, dudas sexuales; en gineco SIEMPRE ofrecer chaperona.",
        "Nombrar la confidencialidad explícitamente aumenta la sinceridad del paciente.",
    ],
    "esto SIEMPRE abre la estación; el sinodal cronometra los primeros 30 s.",
    "empiezas a preguntar sin presentarte o sin pedir permiso para revisarlo.",
    "NOM-004-SSA3-2012; Calgary-Cambridge framework (Silverman & Kurtz).",
    "universal", "marco_universal", "comunicacion",
)

make_card(
    "UNIVERSAL", "est-universal",
    "U2 · Apertura del motivo de consulta + parafraseo",
    '¿Qué le trae hoy a la consulta?\n'
    '[escuchar sin interrumpir ≥ 60 s, contacto visual]\n'
    'Si entendí bien, usted me dice que [parafrasear con sus palabras]. ¿Es correcto?',
    [
        "Pregunta abierta no sesga (¿le duele el pecho? induce respuesta afirmativa por sugestión).",
        "'Golden minute': el paciente da el 80% del dx si lo dejas 60 s; estudios muestran que el médico interrumpe a los 18 s (Beckman & Frankel 1984).",
        "Parafraseo valida comprensión + el paciente se siente escuchado → mejor alianza, mejor adherencia.",
        "Reformular con sus palabras reduce error de interpretación y captura matices clínicos.",
    ],
    "lenguaje corporal abierto, sin interrumpir, parafraseo literal.",
    "abres con preguntas cerradas SÍ/NO o interrumpes en los primeros 60 s.",
    "Calgary-Cambridge; Beckman & Frankel JAMA 1984.",
    "universal", "marco_universal", "comunicacion",
)

make_card(
    "UNIVERSAL", "est-universal",
    "U3 · Inicio y evolución cronológica",
    '¿Cuándo comenzó este [síntoma]?\n'
    '¿Fue de pronto o poco a poco?\n'
    '¿Desde entonces ha mejorado, empeorado o sigue igual?\n'
    '¿Es la primera vez o ha tenido episodios similares antes?\n'
    '¿Qué estaba haciendo cuando empezó?',
    [
        "Inicio súbito (segundos-minutos) → vascular/mecánico: IAM, TEP, HSA, disección aórtica, torsión, neumotórax, perforación visceral.",
        "Inicio gradual (días-semanas) → inflamatorio/infeccioso/tumoral.",
        "Curso progresivo → neoplásico, fibrótico, degenerativo.",
        "Curso fluctuante → autoinmune o episódico (asma, migraña, epilepsia, lupus).",
        "Episodios previos similares → recurrencia conocida (litiasis, cefalea primaria, asma) — orienta al dx ya estudiado.",
        "Detonante (esfuerzo, ingesta, fármaco, trauma) → fisiopatología y prevención.",
    ],
    "registrar fecha de inicio EXACTA + modo + curso en la nota.",
    "no precisas 'súbito vs gradual' — son las dos grandes ramas del DDx.",
    "Bates 13ª; UpToDate 'Approach to the patient with new symptoms'.",
    "universal", "marco_universal",
)

make_card(
    "UNIVERSAL", "est-universal",
    "U4 · Caracterizar el síntoma principal — OLDCARTS",
    'Cuénteme cómo es ese [síntoma]:\n'
    'O — ¿Cuándo empezó? ¿De pronto o poco a poco?\n'
    'L — ¿Dónde lo siente exactamente?\n'
    'D — ¿Cuánto dura? ¿Es continuo o por episodios?\n'
    'C — ¿Cómo lo describiría? (punzante, opresivo, ardoroso, cólico…)\n'
    'A — ¿Qué lo empeora o lo mejora?\n'
    'R — ¿Se va hacia algún otro lado?\n'
    'T — ¿A qué hora del día? ¿Con qué actividad?\n'
    'S — Del 0 al 10, ¿qué tan fuerte?',
    [
        "O (Onset): súbito = vascular (IAM, TEP, HSA, disección, torsión, perforación); gradual = inflamatorio/infeccioso/tumoral.",
        "L (Location): irradiación a mandíbula/brazo izq = IAM; flanco→ingle = cólico renal; escápula derecha = biliar; epigastrio→espalda = pancreatitis o aorta.",
        "D (Duration): dolor torácico >20-30 min con FRCV = SICA hasta demostrar lo contrario. Cólico (va y viene) = obstrucción (renal, biliar, intestinal).",
        "C (Character): opresivo retroesternal = isquemia; ardoroso = GERD/úlcera; pulsátil = vascular o migraña; 'tipo desgarro' = disección aórtica.",
        "A: cede con nitratos = angina; cede con AINE = MSK; empeora inspirar = pleurítico (TEP, neumonía, pericarditis).",
        "R: dolor referido orienta (Kehr = irritación diafragmática; cólico renal a ingle; biliar a escápula derecha).",
        "T: dolor nocturno + cede con comida = úlcera duodenal; matutino + rigidez >30 min = inflamatorio (AR, espondiloartritis).",
        "S: 10/10 'thunderclap' = HSA hasta descartar. Escala 0-10 OBLIGATORIA en nota ECOE.",
    ],
    "SIEMPRE abrir con pregunta abierta antes de OLDCARTS.",
    "omites escala 0-10 o saltas directo a '¿le duele aquí?'.",
    "Bates 13ª; UpToDate 'Approach to the patient with chest pain'.",
    "universal", "marco_universal", "dolor",
)

make_card(
    "UNIVERSAL", "est-universal",
    "U5 · Síntomas asociados — revisión dirigida al sistema sospechoso",
    'Junto con [síntoma principal], ¿ha notado…?\n'
    '• Cardio: dolor torácico, disnea, palpitaciones, síncope, edema, ortopnea, DPN.\n'
    '• Respi: tos, expectoración, hemoptisis, sibilancias, fiebre.\n'
    '• GI: náusea, vómito, diarrea/estreñimiento, sangrado (hematemesis/melena/hematoquecia), ictericia.\n'
    '• GU: disuria, polaquiuria, hematuria, urgencia, dolor lumbar.\n'
    '• Neuro: cefalea, déficit motor/sensitivo, alteración consciencia, convulsiones, vértigo, alteración visual.\n'
    '• Constitucionales: fiebre, pérdida de peso, sudoración nocturna, astenia.',
    [
        "Revisión DIRIGIDA al sistema sospechoso, no cuestionario universal — confirma o refuta hipótesis del MC.",
        "Síntomas B (fiebre + pérdida peso >5% en 6m + sudoración nocturna) → bandera infecciosa (TB, endocarditis) u oncológica (linfoma).",
        "Ortopnea + DPN + edema bilateral = IC izquierda; claudicación intermitente = EAP.",
        "Hemoptisis = TB, ca pulmón, TEP, bronquiectasias, vasculitis (Wegener).",
        "Melena = sangrado alto (Treitz arriba); hematoquecia = bajo. Ictericia + dolor cólico HD + fiebre = colangitis (tríada de Charcot).",
        "Déficit neuro focal súbito = ictus; cefalea súbita 10/10 = HSA; cefalea + papiledema = HTIC.",
    ],
    "el sinodal espera ≥3 síntomas asociados pertinentes al sistema sospechoso.",
    "haces 'revisión por sistemas' tipo cuestionario sin filtrar por hipótesis.",
    "Bates 13ª; UpToDate 'Review of systems'.",
    "universal", "marco_universal",
)

make_card(
    "UNIVERSAL", "est-universal",
    "U6 · Red flags universales — banderas rojas",
    '¿Ha tenido alguno de estos?\n'
    '• Fiebre persistente sin causa clara.\n'
    '• Pérdida de peso involuntaria.\n'
    '• Sudoración nocturna que empapa.\n'
    '• Sangrado por cualquier sitio.\n'
    '• Dolor que lo despierta por la noche.\n'
    '• Cefalea diferente / peor de su vida.\n'
    '• Cambio reciente en hábito intestinal o urinario.\n'
    '• Bultos o masas nuevas.\n'
    '• Cansancio extremo que no cede con descanso.\n'
    '• Dolor de pecho, desmayo o falta de aire.',
    [
        "Síntomas B (fiebre + ↓peso + sudoración nocturna) → linfoma, TB, endocarditis, neoplasia oculta.",
        "Sangrado oculto + astenia + ↓peso >50 años → ca colorrectal, gástrico hasta descartar (colonoscopia/endoscopia).",
        "Dolor nocturno (despierta) → tumor óseo, metástasis, espondiloartritis axial, dolor neuropático.",
        "Cefalea 'thunderclap' (10/10 en <1 min) → HSA hasta descartar (TC simple + PL si negativa).",
        "Cefalea + déficit neurológico nuevo / papiledema → masa ocupante o HTIC.",
        "Cambio reciente en hábito intestinal/urinario >50 años → ca colorrectal o de vejiga.",
        "Síncope durante esfuerzo → cardio estructural (estenosis aórtica, MCH, anomalía coronaria).",
        "Dolor torácico + disnea + diaforesis + irradiación = SICA hasta descartar.",
    ],
    "siempre preguntar 3-4 red flags universales antes de cerrar el interrogatorio.",
    "cierras la anamnesis sin descartar lo que mata o discapacita.",
    "NICE referral guidelines; USPSTF; UpToDate 'Red flags by symptom'.",
    "universal", "marco_universal", "red_flags",
)

make_card(
    "UNIVERSAL", "est-universal",
    "U7 · Antecedentes (AHF · APP · APNP · alergias · fármacos · vacunas)",
    'AHF: ¿alguien en la familia con diabetes, hipertensión, infarto, cáncer (cuál y a qué edad), enfermedad mental, muerte súbita?\n'
    'APP: ¿qué enfermedades crónicas tiene o ha tenido?\n'
    'APNP: ¿cirugías previas? ¿hospitalizaciones? ¿transfusiones?\n'
    'Alergias: ¿medicamentos, alimentos, látex, contraste?\n'
    'Fármacos: ¿qué toma, dosis, desde cuándo? ¿suplementos o herbolaria?\n'
    'Vacunación: ¿al día con influenza, COVID, Td/Tdap, neumo, herpes zóster, VPH?',
    [
        "AHF de cáncer en 1er grado <50 a → criterios genéticos (Lynch, BRCA, Amsterdam); orienta a tamizaje temprano.",
        "AHF de muerte súbita <40 a → cardiopatía hereditaria (QT largo, Brugada, MCH); pedir ECG basal.",
        "AHF de DM2 1er grado = ↑3× riesgo; tamizar antes de 35 a (ADA 2025).",
        "APP cardiopatía/EPOC/ERC → ajusta fármacos, contraste y anestesia (RCRI, ARISCAT).",
        "Cirugías abdominales previas → bridas (oclusión); colecistectomía cambia motilidad GI.",
        "Transfusiones pre-1992 → riesgo VHC/VHB; aloinmunización RhD en mujer fértil.",
        "Alergia a penicilina: preguntar TIPO (rash vs anafilaxia) — 90% no son alergia verdadera, restringe espectro innecesariamente.",
        "Polifarmacia ≥5 fármacos → interacciones, deprescribir, revisar Beers en >65 a.",
        "Vacunas adulto (ACIP 2025): influenza anual; Td c/10 a; Tdap 1×+cada embarazo; Shingrix 50+; PCV20 65+; VPH ≤26 (extendible a ≤45); COVID anual.",
    ],
    "estructurar AHF → APP → APNP → alergias → fármacos → vacunas (mnemotécnico ordenado).",
    "olvidas automedicación, herbolaria, alergias o vacunación adulto.",
    "Bates 13ª; ACIP 2025 (CDC); USPSTF 2025; ADA 2025.",
    "universal", "marco_universal", "antecedentes",
)

make_card(
    "UNIVERSAL", "est-universal",
    "U8 · Hábitos y contexto",
    'Tabaco: ¿fuma? ¿cuántos al día? ¿desde qué edad? (paquetes-año)\n'
    'Alcohol: ¿qué cantidad y frecuencia? (AUDIT-C)\n'
    'Otras sustancias: ¿marihuana, cocaína, opioides, otras?\n'
    'Dieta: ¿cuántas comidas? ¿frutas/verduras? ¿procesados, refresco?\n'
    'Ejercicio: ¿tipo, frecuencia, intensidad?\n'
    'Sueño: ¿cuántas horas? ¿reparador? ¿ronca? ¿se despierta cansado?\n'
    'Sexual: ¿activo/a? ¿hombres/mujeres/ambos? ¿uso de protección?\n'
    'Ocupación: ¿polvos, químicos, ruido?\n'
    'Viajes / exposiciones / mascotas.',
    [
        "Paquetes-año = (cigarros/día × años)/20. ≥20 paq-año en 50-80 a + activo o que dejó <15 a → LDCT anual (USPSTF 2025 grado B).",
        "AUDIT-C ≥4 H / ≥3 M = consumo de riesgo; intervención breve indicada.",
        "Sustancias: detecta intoxicación/abstinencia, riesgo perioperatorio, conducta hospitalaria, ITS asociadas.",
        "Dieta orienta déficits (Fe, B12, D), excesos (HTA, DM, dislipidemia) y consejo dirigido (DASH/Mediterránea).",
        "Sedentarismo <150 min/sem moderado = FRCV modificable.",
        "Ronquido + apneas observadas + Epworth >10 → STOP-BANG, polisomnografía (SAOS).",
        "Historia sexual orienta tamizaje ITS (CDC: VIH 13-64 anual + ITS según riesgo); confidencialidad indispensable.",
        "Exposición ocupacional: asbesto (mesotelioma), sílice (silicosis), benceno (LMA), turnos (CV/metabólico).",
        "Viajes a zona endémica: dengue, malaria, Zika, tifoidea; contacto TB; toxoplasma en embarazada con gato.",
    ],
    "tabaco-alcohol-drogas-sexual es OBLIGATORIO; resto según pertinencia clínica.",
    "no preguntas consumo de sustancias por pudor o juzgas al paciente.",
    "USPSTF 2025 (tamizaje LDCT); CDC STI 2024; AUDIT-C OMS; ASSIST 2.0.",
    "universal", "marco_universal", "habitos",
)

make_card(
    "UNIVERSAL", "est-universal",
    "U9 · Resumen + cierre + plan compartido",
    'Recapitulando: usted me cuenta que [resumir MC + datos clave + tiempo].\n'
    'Para entender mejor lo que le sucede, le voy a:\n'
    '• Realizar una exploración física dirigida.\n'
    '• Solicitar [estudios pertinentes].\n'
    'Mi impresión inicial es [DDx prudente, en plural].\n'
    '¿Tiene alguna duda o algo que le preocupe que no le haya preguntado?\n'
    'Gracias por su confianza.',
    [
        "Resumen final = 'closing the loop' (Calgary-Cambridge): reduce errores de información, evidencia escucha.",
        "Plan compartido = shared decision-making → mejor adherencia y satisfacción.",
        "Pregunta de cierre ('¿algo más?') captura 20-30% de información oculta en estudios reales.",
        "DDx prudente en plural ('estamos descartando…') evita cerrarse a un dx único antes de exploración/estudios.",
        "Despedida cálida = efecto recencia → última impresión sesga el puntaje ECOE final.",
    ],
    "el sinodal escucha el cierre como termómetro de comunicación; no improvises.",
    "terminas sin resumen, sin invitar a preguntar, o anuncias dx único antes de explorar.",
    "Calgary-Cambridge; UpToDate 'Patient-clinician communication'.",
    "universal", "marco_universal", "comunicacion", "cierre",
)


# ============================================================
# 01 MEDICINA FAMILIAR — 4 cards
# ============================================================

make_card(
    "MEDICINA FAMILIAR", "est-mf",
    "MF1 · Tamizajes USPSTF por edad y sexo",
    '¿Le han realizado los siguientes estudios de prevención?\n'
    '• Mujer 21-65: papanicolaou (c/3 a) o co-test VPH (c/5 a) ≥30.\n'
    '• Mujer 40-74: mastografía bienal.\n'
    '• Mujer/hombre 45-75: colonoscopia c/10 a o SOH anual.\n'
    '• Mujer ≥65 (o ≥50 con FR): DEXA para osteoporosis.\n'
    '• Hombre 65-75 fumador: USG abdominal (AAA, 1×).\n'
    '• 13-64 a: VIH al menos 1×; ITS según conducta sexual.\n'
    '• Adulto: depresión, ansiedad, consumo OH/tabaco, HTA, lípidos, DM (≥35 a o IMC ≥25 + FR).',
    [
        "Citología cervical 21-65 a — USPSTF grado A; ≥30 a co-test VPH c/5 a es opción aceptada (sensibilidad mayor).",
        "Mastografía 40-74 a bienal — USPSTF 2024 actualizó inicio de 50 a a 40 a (grado B).",
        "Colon 45-75 — USPSTF 2021 bajó inicio a 45 a por ↑incidencia en adultos jóvenes. Modalidad: colonoscopia c/10 a o SOH anual.",
        "DEXA: mujer ≥65 (grado B); <65 con riesgo equivalente (FRAX ≥9.3%).",
        "AAA: USG 1× en H 65-75 fumadores (grado B); no en mujeres.",
        "VIH 1× en 13-64 a (grado A); embarazadas en cada gestación.",
        "DM2: tamizar 35-70 a con sobrepeso/obesidad (HbA1c o glucemia ayuno); ADA 2025 baja inicio a 35 a.",
        "Depresión + alcohol + tabaco = tamizaje universal en adultos (grado B); usar PHQ-2, AUDIT-C, ASSIST.",
    ],
    "vincular tamizaje a edad y sexo del paciente concreto; no enumerar todo a todos.",
    "no preguntar tamizajes en consulta de prevención o consulta de control.",
    "USPSTF 2024-2025 (uspreventiveservicestaskforce.org); ADA 2025.",
    "medicina_familiar", "tamizaje", "prevencion",
)

make_card(
    "MEDICINA FAMILIAR", "est-mf",
    "MF2 · Vacunación del adulto (ACIP 2025)",
    '¿Está al día con sus vacunas?\n'
    '• Influenza inactivada anual (todos los ≥6 meses).\n'
    '• COVID-19 actualizada anual.\n'
    '• Td c/10 años; Tdap 1× + en cada embarazo (27-36 SDG).\n'
    '• VPH ≤26 a (extender ≤45 a previa toma decisión compartida).\n'
    '• Herpes zóster (Shingrix) 2 dosis ≥50 a (y ≥19 a inmunocomprometido).\n'
    '• Neumococo: PCV20 1× o PCV15+PPSV23 a ≥65 a (o 19-64 con FR).\n'
    '• VHB en adultos 19-59 a (universal desde ACIP 2022).\n'
    '• VSR 1× a ≥75 a y 60-74 a con FR.',
    [
        "Influenza anual — única que se administra cada año en todos los adultos; ↓ hospitalización y muerte.",
        "Td booster c/10 a + Tdap 1× para reemplazar uno de los Td (control de pertussis en adultos).",
        "Tdap en cada embarazo 27-36 SDG = protección pasiva del lactante en primeros 2 meses pre-vacuna.",
        "VPH: indicación rutinaria ≤26 a; ACIP permite ≤45 a con shared decision (menor beneficio).",
        "Shingrix 50+ → reduce zóster 97% y NPH 91%; preferida sobre Zostavax (descontinuada).",
        "Neumococo cambió 2024-2025: PCV20 reemplaza esquema PCV13+PPSV23 en mayoría; PCV15+PPSV23 alternativo.",
        "VHB universal 19-59 a desde 2022 (carga oculta + erradicación a largo plazo).",
        "VSR adultos 75+ y 60-74 con FR (EPOC, IC, ERC, DM, inmunocompromiso) — desde 2023-2024.",
    ],
    "preguntar cartilla / comprobante; no asumir. Verbalizar grupos de riesgo concretos.",
    "no preguntas vacunación o recomiendas esquema desactualizado.",
    "ACIP 2025 (CDC Adult Immunization Schedule).",
    "medicina_familiar", "vacunacion", "prevencion",
)

make_card(
    "MEDICINA FAMILIAR", "est-mf",
    "MF3 · Salud mental breve — PHQ-2, GAD-2, AUDIT-C",
    'PHQ-2 (depresión):\n'
    '1. En las últimas 2 semanas, ¿se ha sentido decaído/a, deprimido/a o sin esperanza?\n'
    '2. ¿Ha sentido poco interés o placer en hacer las cosas?\n'
    'GAD-2 (ansiedad):\n'
    '1. ¿Se ha sentido nervioso/a, ansioso/a o muy tenso/a?\n'
    '2. ¿No ha podido dejar de preocuparse o controlar la preocupación?\n'
    'AUDIT-C (alcohol):\n'
    '1. ¿Con qué frecuencia consume alcohol?\n'
    '2. ¿Cuántas bebidas un día típico que toma?\n'
    '3. ¿Con qué frecuencia toma ≥6 en una sola ocasión?',
    [
        "PHQ-2 ≥3 (escala 0-6) → sensibilidad 83%, especificidad 92% para depresión mayor; aplicar PHQ-9 completo si positivo.",
        "GAD-2 ≥3 → tamizaje positivo de TAG; aplicar GAD-7 (≥10 = clínicamente significativo).",
        "AUDIT-C ≥4 H / ≥3 M = consumo de riesgo; intervención breve (5-15 min) reduce consumo 13-34%.",
        "USPSTF 2023: tamizaje universal de ansiedad en adultos <65 a (grado B); depresión y suicidalidad en todos los adultos (grado B).",
        "PHQ-9 #9 (ideación suicida) → evaluación inmediata si ≥1; aplicar Columbia C-SSRS si positiva.",
        "Comorbilidad ansiedad+depresión = 50% — siempre tamizar ambas.",
    ],
    "verbalizar SIEMPRE PHQ-2 + GAD-2 + AUDIT-C en estación de medicina familiar adulto.",
    "no tamizar salud mental o asumir que el paciente lo diría espontáneamente.",
    "USPSTF 2023; PHQ-9 (Kroenke 2001); GAD-7 (Spitzer 2006); AUDIT-C OMS.",
    "medicina_familiar", "salud_mental", "tamizaje",
)

make_card(
    "MEDICINA FAMILIAR", "est-mf",
    "MF4 · Contexto social, violencia y red de apoyo",
    '¿Vive con alguien? ¿quién está al pendiente de usted?\n'
    '¿Cómo es su situación económica y de vivienda? ¿alimentos suficientes?\n'
    '¿Ha vivido violencia (física, psicológica, sexual, económica) por parte de alguien cercano?\n'
    '¿Se siente seguro/a en su casa?\n'
    '¿Tiene quién lo lleve al hospital si lo necesita?\n'
    '¿Tiene mascota o cuidador a su cargo?\n'
    '¿Acceso a servicios (transporte, internet, medicamentos)?',
    [
        "Determinantes sociales de la salud (vivienda, alimentos, ingresos, educación, transporte) predicen mortalidad mejor que muchos factores biomédicos.",
        "USPSTF 2018 grado B: tamizaje de violencia de pareja en mujer en edad fértil + canalización a recursos.",
        "Aislamiento social = ↑ mortalidad equivalente a fumar 15 cig/día (Holt-Lunstad 2015).",
        "Inseguridad alimentaria = ↑ HbA1c, ↑ hospitalizaciones, ↓ adherencia.",
        "Acceso a transporte y medicamentos = barrera #1 de adherencia en ERC/IC/DM.",
        "Cuidador primario con burnout = ↑ riesgo de claudicación familiar; identificar para apoyo.",
    ],
    "preguntar de forma respetuosa y sin emitir juicio; ofrecer ayuda o canalización.",
    "asumes que el paciente vive en condiciones óptimas o no abordas violencia.",
    "USPSTF 2018 IPV; Holt-Lunstad 2015 PLoS Med; CDC SDOH.",
    "medicina_familiar", "social", "violencia",
)


# ============================================================
# 02 MEDICINA INTERNA — 4 cards
# ============================================================

make_card(
    "MEDICINA INTERNA", "est-mi",
    "MI1 · Enfermedad actual multisistémica detallada",
    'Cuénteme cronológicamente cómo ha evolucionado este cuadro.\n'
    'Aparte de [síntoma principal], ¿qué otros síntomas se han ido sumando?\n'
    'Para cada órgano sospechoso:\n'
    '• Cardio: dolor torácico, disnea de esfuerzo (NYHA), ortopnea, DPN, edema, palpitaciones, síncope.\n'
    '• Pulmón: tos, expectoración, hemoptisis, sibilancias, disnea (mMRC).\n'
    '• Riñón: oliguria/poliuria, espuma, edema, dolor lumbar, hematuria.\n'
    '• Hígado: ictericia, prurito, ascitis, hematemesis, alteración estado mental, equimosis.\n'
    '• Endocrino: polidipsia/poliuria, ↑/↓ peso, intolerancia al frío/calor, tremor.',
    [
        "Internista busca la 'enfermedad sistémica oculta' que conecta síntomas aparentemente dispares (autoinmune, infeccioso, neoplásico, endocrino).",
        "Disnea NYHA I-IV (limitación funcional CV) y mMRC 0-4 (respiratoria) son obligatorias para estratificar IC y EPOC.",
        "Síndrome anémico (palidez, fatiga, taquicardia, disnea) → buscar sangrado oculto digestivo o ginecológico.",
        "Edema bilateral + ortopnea = IC; unilateral + dolor pantorrilla = TVP; periorbitario matutino + proteinuria = nefrótico.",
        "Ictericia + coluria + acolia = obstructiva; ictericia + dolor cólico HD + fiebre = colangitis (Charcot).",
        "Triada poliuria + polidipsia + ↓peso = DM descompensada; cetoacidosis si hiperventilación o aliento cetónico.",
    ],
    "ir órgano por órgano cuando el cuadro es multisistémico — NO desorganizar.",
    "te quedas en el síntoma principal sin explorar comorbilidad sistémica.",
    "Bates 13ª; UpToDate 'Approach to the patient with multisystem disease'.",
    "medicina_interna", "enfermedad_actual",
)

make_card(
    "MEDICINA INTERNA", "est-mi",
    "MI2 · Polifarmacia + adherencia + automedicación",
    '¿Qué medicamentos toma actualmente?\n'
    'Para cada uno: nombre, dosis, frecuencia, desde cuándo, indicación.\n'
    '¿Los toma todos los días? ¿se le olvida alguno?\n'
    '¿Suspendió algún medicamento por su cuenta? ¿por qué?\n'
    '¿Toma algo sin receta: AINE, antiácidos, laxantes, somníferos, herbolaria, suplementos?\n'
    '¿Algún medicamento le ha sentado mal (reacción adversa)?',
    [
        "Polifarmacia ≥5 fármacos → ↑ riesgo interacciones, hospitalización por RAM, caídas, deterioro cognitivo.",
        "Adherencia: solo 50% toma sus medicamentos como se le indicó — preguntar abiertamente (no juzgar) revela el 40% real.",
        "AINE de venta libre = causa #1 de IRA en paciente con ERC/anciano; ↑ HTA, ↑ sangrado GI.",
        "Herbolaria (hierba de San Juan ↓ ACO/antidepresivos; ginkgo ↑ sangrado; toronja ↑ estatinas).",
        "Beers Criteria 2023: lista AGS de fármacos inapropiados en ≥65 a (benzo, anticolinérgicos, AINE crónico).",
        "RAM previa = elimina opción terapéutica; documentar TIPO de reacción (rash, anafilaxia, GI).",
    ],
    "preguntar nombre + dosis + frecuencia + ADHERENCIA; ojo a herbolaria y automedicación.",
    "anotas 'misma medicación' sin verificar adherencia ni herbolaria.",
    "AGS Beers Criteria 2023; UpToDate 'Drug interactions'.",
    "medicina_interna", "farmacos", "polifarmacia",
)

make_card(
    "MEDICINA INTERNA", "est-mi",
    "MI3 · Funcionalidad basal previa",
    '¿Cómo era usted antes de este cuadro?\n'
    '• Actividades básicas (ABVD): comer, vestirse, bañarse, ir al baño, moverse en cama.\n'
    '• Actividades instrumentales (AIVD): cocinar, comprar, transporte, manejar dinero, medicamentos, teléfono.\n'
    '• Marcha y caídas: ¿caminaba solo? ¿ayuda? ¿caídas último año?\n'
    '• Cognición: ¿memoria, orientación, decisiones?\n'
    '• Estado de ánimo y soporte social.\n'
    '• Capacidad funcional cardiovascular: ¿podía subir 2 pisos sin detenerse? (≥4 MET)',
    [
        "Estado basal predice mortalidad y plan de cuidados mejor que dx individual; cambio funcional reciente = alerta.",
        "Katz (ABVD) y Lawton (AIVD) son escalas validadas; dependencia parcial = comorbilidad oculta o demencia.",
        "Historia de ≥2 caídas/año o caída con lesión = evaluación geriátrica multidimensional + valoración de marcha (Timed Up & Go ≥12 s).",
        "Capacidad funcional <4 MET = riesgo cardiovascular perioperatorio elevado (ACC/AHA).",
        "Deterioro cognitivo agudo (≤horas-días) = delirium hasta demostrar lo contrario; subagudo = demencia, depresión.",
        "Aislamiento + dependencia + cuidador único = riesgo de claudicación; canalizar trabajo social.",
    ],
    "siempre evaluar funcionalidad basal en >65 a; lo usa el sinodal para estratificar caso.",
    "no documentas estado funcional previo en paciente crónico u hospitalizado.",
    "Katz JAMA 1963; Lawton 1969; ACC/AHA perioperative 2024; UpToDate 'Geriatric assessment'.",
    "medicina_interna", "geriatria", "funcionalidad",
)

make_card(
    "MEDICINA INTERNA", "est-mi",
    "MI4 · Descompensación — ¿qué cambió antes de empeorar?",
    'Antes de que empeorara, ¿cambió algo?\n'
    '• ¿Dejó de tomar algún medicamento? ¿se le terminó?\n'
    '• ¿Comenzó algún medicamento nuevo (AINE, esteroide, antibiótico)?\n'
    '• ¿Infección reciente (vías urinarias, respiratoria, dental, piel)?\n'
    '• ¿Cambio en la dieta o exceso de sal/líquidos?\n'
    '• ¿Esfuerzo, estrés, viaje, exposición?\n'
    '• ¿Cambio en su nivel de actividad?\n'
    '• ¿Algún procedimiento o cirugía reciente?',
    [
        "Identificar TRIGGER de descompensación es la pregunta clave del internista — modificable y prevenible.",
        "IC descompensada: causas FAILURE (Forgot meds, Anemia/Arrhythmia, Ischemia, Lifestyle salt/fluid, Upregulation thyroid, Renal failure, Embolia/Endocarditis).",
        "EPOC reagudizada: 70% infección viral/bacteriana; resto contaminación, no adherencia, embolismo.",
        "Cetoacidosis DM: las 5 I (Infección, Infarto, Iatrogenia, Insulina omitida, Intoxicación).",
        "Cirrosis descompensada (encefalopatía): infección (PBE), sangrado variceal, dieta rica en proteína, deshidratación, sedantes.",
        "AINE en ERC/IC = causa común de descompensación; preguntar TODO lo nuevo en las últimas 2-4 semanas.",
    ],
    "siempre preguntar 'qué cambió antes' — orienta plan de prevención secundaria.",
    "anotas que el paciente 'se descompensó' sin investigar el detonante.",
    "UpToDate 'Acute decompensated heart failure precipitants'; GOLD 2024.",
    "medicina_interna", "descompensacion",
)


# ============================================================
# 03 CIRUGIA GENERAL — 5 cards
# ============================================================

make_card(
    "CIRUGÍA GENERAL", "est-cx",
    "Cx1 · ALICIA del dolor abdominal",
    'A — Aparición: ¿cuándo empezó? ¿de pronto o gradual?\n'
    'L — Localización inicial y actual (señale con un dedo).\n'
    'I — Irradiación: ¿hacia dónde se va?\n'
    'C — Carácter: ¿punzante, cólico, ardoroso, opresivo, sordo?\n'
    'I — Intensidad: del 0 al 10.\n'
    'A — Atenuantes / agravantes: ¿qué lo mejora o empeora?\n'
    'Adicional: ¿migra? ¿con vómito? ¿alivia con la defecación?',
    [
        "Inicio súbito + irradiado a espalda = aorta, pancreatitis severa, perforación; síncope asociado = ruptura AAA.",
        "Migración periumbilical → FID en 4-12 h = apendicitis (Murphy 1904) — patognomónico.",
        "Dolor en epigastrio que migra a HD + fiebre + ictericia = colangitis (Charcot); + alteración conciencia y shock = Reynolds (pentada).",
        "Cólico (va y viene cada 5-15 min) = obstructivo: renal (flanco→ingle), biliar (HD→escápula derecha), intestinal (con vómito y distensión).",
        "Dolor 'desproporcionado al examen' = isquemia mesentérica hasta descartar (paciente mayor con FA o vasculopatía).",
        "Dolor pélvico mujer fértil + amenorrea + síncope = embarazo ectópico roto — β-hCG urgente, USG, quirófano.",
        "Atenuantes: AINE alivia MSK; postura genupectoral alivia pancreatitis; alimentos alivian úlcera duodenal y agravan biliar.",
    ],
    "incluir 'migración' y 'señale con un dedo' — son discriminadores poderosos.",
    "no pides al paciente que señale con un dedo o no preguntas irradiación.",
    "ATLS 10ª; UpToDate 'Evaluation of adult with abdominal pain'; SAGES.",
    "cirugia", "dolor_abdominal",
)

make_card(
    "CIRUGÍA GENERAL", "est-cx",
    "Cx2 · AMPLE en urgencia / preoperatorio",
    'A — Alergias: medicamentos, látex, contraste.\n'
    'M — Medicación actual: anticoagulantes, antiagregantes, esteroides, antiHTA, insulina, AINE.\n'
    'P — Patología previa relevante: cardio/EPOC/ERC/DM/diátesis hemorrágica, anestesia previa.\n'
    'L — Last meal: ¿hace cuánto comió o tomó líquidos por última vez?\n'
    'E — Eventos previos al cuadro: mecanismo de lesión, ingesta, fármaco nuevo, esfuerzo.',
    [
        "Alergia a contraste o látex cambia protocolo de quirófano; reacción a anestésico previo = bandera anestésica mayor.",
        "Anticoagulantes/antiagregantes determinan necesidad de reversión: warfarina → vitK + PCC; rivaroxabán/apixabán → andexanet; dabigatrán → idarucizumab.",
        "Esteroides crónicos → riesgo de insuficiencia suprarrenal perioperatoria; requiere dosis de stress (hidrocortisona 100 mg IV).",
        "Antihipertensivos: continuar β-bloq y clonidina; suspender IECA/ARA II la mañana (hipotensión en inducción).",
        "ERC + contraste → riesgo NIC; valorar hidratación, suspender metformina, considerar alternativa diagnóstica.",
        "Ayuno: <6 h sólidos / <2 h líquidos claros = riesgo broncoaspiración → intubación de secuencia rápida (ISR) si emergencia.",
        "Mecanismo de lesión orienta: cinturón mal puesto → estallido vesical/páncreas; volante → trauma cardíaco; cinemática alta → trauma oculto.",
    ],
    "AMPLE va INMEDIATAMENTE después del ABCDE en politraumatizado.",
    "olvidas anticoagulantes/antiagregantes o última ingesta (define conducta).",
    "ATLS 10ª (ACS); UpToDate 'Anticoagulant reversal'.",
    "cirugia", "ample", "urgencia",
)

make_card(
    "CIRUGÍA GENERAL", "est-cx",
    "Cx3 · Antecedentes quirúrgicos + anestésicos",
    '¿Ha tenido cirugías previas? ¿de qué y cuándo?\n'
    '¿Cómo fue la anestesia: general, regional, local? ¿algún problema?\n'
    '¿Despertar normal? ¿náusea/vómito postoperatorio severo?\n'
    '¿Familiar con problema anestésico (hipertermia maligna)?\n'
    '¿Cicatrización normal? ¿queloides? ¿infección de herida?\n'
    '¿Complicación reciente (sangrado, dehiscencia, eventración)?',
    [
        "Cirugía abdominal previa → bridas (causa #1 obstrucción intestinal mecánica en adulto).",
        "Colecistectomía previa cambia DDx de dolor HD (descartar coledocolitiasis residual, estenosis biliar).",
        "Náusea/vómito postoperatorio severo → riesgo Apfel ≥3 → profilaxis multimodal (dexa + ondansetrón).",
        "Hipertermia maligna familiar = contraindica halotano/succinilcolina; usar TIVA con propofol/rocuronio.",
        "Queloide previo = riesgo de queloide en nueva cicatriz; informar al paciente.",
        "Eventración previa = considerar plastia con malla; valorar IMC y técnica quirúrgica.",
        "Anestesia raquídea previa con cefalea post-punción → preferir aguja punta de lápiz (Whitacre) si se repite.",
    ],
    "preguntar anestesia previa + complicaciones específicamente, no solo 'cirugías'.",
    "anotas 'colecistectomía previa' sin preguntar técnica, complicación, anestesia.",
    "UpToDate 'Preoperative evaluation'; MHAUS hipertermia maligna.",
    "cirugia", "preoperatorio",
)

make_card(
    "CIRUGÍA GENERAL", "est-cx",
    "Cx4 · Transfusional · sangrado · coagulación",
    '¿Le han transfundido sangre o derivados alguna vez?\n'
    '¿Reacción transfusional previa (fiebre, urticaria, hemólisis)?\n'
    '¿Sangrado fácil con cepillo de dientes, encías, nariz?\n'
    '¿Hematomas espontáneos o desproporcionados al trauma?\n'
    '¿Sangrado prolongado tras cirugía dental o cirugía menor?\n'
    '¿Familia con hemofilia o trastorno de coagulación?\n'
    '¿Toma aspirina, clopidogrel, anticoagulante? ¿última dosis?',
    [
        "Aloinmunización post-transfusional (Rh, Kell, Duffy) → mujer fértil con anticuerpos = riesgo de EHRN en próximo embarazo.",
        "Reacción hemolítica previa = ABO incompatible; pre-medicar + producto lavado en futura transfusión.",
        "Sangrado mucocutáneo (encías, epistaxis, equimosis) = defecto plaquetario o vWF.",
        "Sangrado articular/muscular = defecto factor de coagulación (hemofilia A/B).",
        "Sangrado post-quirúrgico tardío (≥24 h) = trastorno de factor o uso de antiagregante.",
        "Antiagregantes: suspender clopidogrel 5-7 d antes de cirugía; AAS según riesgo (continuar en mayoría salvo SNC/posterior).",
        "ACO: warfarina → puente con HBPM si alto riesgo trombótico; DOAC → suspender 24-72 h según TFG y cirugía.",
    ],
    "preguntar SANGRADO antes de quirófano y antes de procedimiento invasivo (PL, vía central).",
    "operas sin preguntar antiagregantes, anticoagulantes o historia de sangrado.",
    "ASA preoperative 2024; UpToDate 'Perioperative management of antithrombotic therapy'.",
    "cirugia", "sangrado", "coagulacion",
)

make_card(
    "CIRUGÍA GENERAL", "est-cx",
    "Cx5 · Síntomas peritoneales + obstructivos",
    '¿El dolor le impide moverse? ¿caminar empeora?\n'
    '¿Ha tenido vómito? ¿cuántas veces? ¿con qué características (bilioso, fecaloide, sanguinolento)?\n'
    '¿Cuándo fue su última evacuación? ¿ha canalizado gases?\n'
    '¿Distensión abdominal? ¿desde cuándo?\n'
    '¿Fiebre o escalofríos?\n'
    '¿Anorexia o rechazo al alimento?\n'
    '¿En mujer: FUM y posibilidad de embarazo?',
    [
        "Dolor que impide moverse + alivio con flexión de cadera = irritación peritoneal (abdomen agudo).",
        "Vómito fecaloide = obstrucción intestinal distal (íleon distal-colon).",
        "Vómito bilioso = obstrucción distal a ampolla de Vater (yeyuno-íleon).",
        "Hematemesis 'pozos de café' = sangrado de tubo digestivo alto; rojo brillante = activo, masivo.",
        "No canaliza gases + distensión + dolor cólico + vómito = obstrucción intestinal mecánica.",
        "Fiebre + dolor RIQ = apendicitis o absceso; fiebre + ictericia + dolor HD = colangitis.",
        "Anorexia + náusea + dolor migratorio FID = clásico de apendicitis (más sensible que fiebre).",
        "Mujer fértil con dolor pélvico + amenorrea = ectópico hasta descartar (β-hCG cuantitativa).",
    ],
    "siempre preguntar canalización de gases y características del vómito en abdomen agudo.",
    "anotas 'abdomen agudo' sin caracterizar peritonismo ni obstrucción.",
    "Tokyo Guidelines 2024 (TG24); UpToDate 'Acute abdomen approach'.",
    "cirugia", "peritonismo", "obstruccion",
)


# ============================================================
# 04 PEDIATRIA — 6 cards
# ============================================================

make_card(
    "PEDIATRÍA", "est-ped",
    "Ped1 · Antecedentes perinatales completos",
    'Embarazo: ¿planeado? ¿controlado? ¿cuántos USG? ¿infecciones? ¿alcohol/tabaco/drogas? ¿diabetes/HTA/preeclampsia?\n'
    'Parto: ¿vaginal o cesárea? ¿a término o pretérmino (SDG)? ¿peso al nacer? ¿APGAR 1 y 5 min?\n'
    'Neonatal: ¿lloró al nacer? ¿necesitó reanimación, oxígeno, UCIN?\n'
    'Tamiz neonatal metabólico y auditivo: ¿se realizó? ¿resultado?\n'
    'Ictericia, hipoglucemia, sepsis, ventilación, ictericia tratada con fototerapia.',
    [
        "Pretérmino <37 SDG y/o bajo peso <2500 g = factor de riesgo para todo (DPM, infección, neumopatía crónica, retinopatía).",
        "Diabetes gestacional materna → macrosomía, hipoglucemia neonatal, ↑ riesgo obesidad/DM2 en hijo.",
        "Preeclampsia → RCIU, prematurez, ↑ riesgo CV en adulto.",
        "APGAR 5 min <7 = riesgo neurológico; <4 = encefalopatía hipóxico-isquémica posible.",
        "Tamiz metabólico ampliado (México: hipotiroidismo, fenilcetonuria, hiperplasia suprarrenal, fibrosis quística, etc.) — la falta o negativa cambia DDx.",
        "UCIN previa → riesgo ventilación → displasia broncopulmonar, retinopatía del prematuro.",
        "Ictericia patológica (<24 h, >12 mg/dL en RN término, persistente >2 sem) = obligatorio investigar.",
    ],
    "antecedentes perinatales son OBLIGATORIOS en TODO niño <5 años — son el factor #1 de riesgo.",
    "anotas 'sin antecedentes perinatales relevantes' sin haber preguntado.",
    "AAP Bright Futures 4ª ed; NOM-007-SSA2-2016; SEGO/SMFM.",
    "pediatria", "perinatales",
)

make_card(
    "PEDIATRÍA", "est-ped",
    "Ped2 · Alimentación y lactancia",
    '¿Cómo se alimenta: pecho exclusivo, fórmula o mixta? ¿desde cuándo?\n'
    'Si pecho: ¿libre demanda? ¿técnica? ¿problemas (grietas, mastitis, baja producción)?\n'
    'Si fórmula: ¿cuál? ¿cuántas onzas y cada cuántas horas?\n'
    'Ablactación: ¿a qué edad inició? ¿qué alimentos?\n'
    '¿Cuántas comidas y colaciones al día?\n'
    '¿Apetito normal o disminuido?\n'
    '¿Aversiones alimentarias? ¿alergias?',
    [
        "Lactancia materna exclusiva (LME) hasta 6 meses recomendación OMS/UNICEF → ↓ infecciones, ↓ obesidad, ↓ DM, ↑ vínculo.",
        "Ablactación 6 meses; <4 meses ↑ alergia alimentaria, sobrepeso; >7 meses ↑ aversión y déficit nutricional.",
        "Fórmula: <1 año NO leche de vaca entera (anemia ferropénica, microsangrado intestinal).",
        "Cambio reciente de leche/fórmula + síntomas GI = alergia a proteína de leche de vaca (APLV).",
        "Apetito disminuido + ↓ peso percentil + fatiga = anemia, infección crónica, celíaca, depresión infantil.",
        "Adolescentes: tamizaje TCA (SCOFF), imagen corporal, dietas restrictivas.",
        "Rechazo a sólidos persistente = disfunción oromotora, reflujo, alergia, autismo.",
    ],
    "verbalizar tipo de alimentación + frecuencia + percentil de peso/talla en cada estación pediátrica.",
    "no preguntas lactancia o ablactación en niño <2 años.",
    "OMS lactancia 2024; AAP Bright Futures 4ª; ESPGHAN guidelines.",
    "pediatria", "alimentacion",
)

make_card(
    "PEDIATRÍA", "est-ped",
    "Ped3 · Desarrollo psicomotor (DPM) por hitos clave",
    '¿A qué edad: sostuvo la cabeza, se sentó, gateó, caminó?\n'
    '¿A qué edad: balbuceó, dijo primera palabra, frases de 2 palabras?\n'
    '¿Sigue instrucciones simples? ¿señala lo que quiere?\n'
    '¿Control de esfínteres diurno y nocturno: a qué edad?\n'
    '¿Sonríe socialmente, juega imitando, juego simbólico?\n'
    '¿Lateralidad establecida (sólo si >4 años)?',
    [
        "Hitos motores (referencia AAP/Bright Futures 2022): sostén cefálico 2-4 m, sentado 6-8 m, gateo 9 m, marcha 12-15 m. Retraso significativo si >2 desviaciones.",
        "Hitos lenguaje: balbuceo 6 m, 1ª palabra 12 m, 2 palabras 18 m, frases 24 m, oración 36 m.",
        "Hitos socioemocionales: sonrisa social 6 sem, ansiedad del extraño 8-9 m, juego paralelo 2 a, simbólico 3 a.",
        "Regresión de hitos = NEUROLÓGICO grave (autismo, leucodistrofia, Rett, mitocondrial).",
        "Lateralidad antes de 18 m = sospechar hemiparesia contralateral (PCI).",
        "Marcha en puntas + retraso lenguaje + comportamiento estereotipado = TEA hasta descartar.",
        "Control de esfínteres diurno 2-4 a, nocturno 3-5 a; enuresis primaria >5 a indica evaluación.",
    ],
    "preguntar hitos por dominios (motor + lenguaje + social) — no sólo 'desarrollo normal'.",
    "afirmas 'DPM normal' sin haber preguntado hitos específicos por edad.",
    "AAP Bright Futures 2022; CDC Developmental Milestones revisadas 2022.",
    "pediatria", "desarrollo", "dpm",
)

make_card(
    "PEDIATRÍA", "est-ped",
    "Ped4 · Esquema de vacunación + cartilla",
    '¿Trae la cartilla nacional de vacunación?\n'
    'Verificar dosis y edades:\n'
    '• RN: BCG, hepatitis B.\n'
    '• 2-4-6 m: pentavalente acelular, rotavirus, neumo conjugada.\n'
    '• 6 m: influenza anual.\n'
    '• 12 m: SRP (triple viral), neumo.\n'
    '• 18 m: pentavalente refuerzo, hepatitis A (zonas riesgo).\n'
    '• 4 a: DPT, SRP, OPV.\n'
    '• 11 a: VPH (niñas/niños).\n'
    '¿Reacción vacunal previa (fiebre, urticaria, llanto incoercible)?',
    [
        "BCG al nacer (zona endémica TB) protege de meningitis tuberculosa y formas diseminadas, NO de TB pulmonar.",
        "Pentavalente acelular cubre DTPa-Hib-VPI; OPV se usa en campañas (no rutinaria).",
        "Rotavirus oral 2-6 m (no iniciar >15 sem por intususcepción si tardía).",
        "Neumo conjugada → ↓ otitis recurrente, neumonía bacteriana, meningitis.",
        "SRP 12 m → protege contra sarampión (brotes 2024-2025); 2ª dosis a los 4 a.",
        "VPH 11 a (niños y niñas) — 2 dosis si <15 a; 3 si ≥15 a o inmunocomprometido.",
        "Reacción adversa documentada → reportar VAERS/Cofepris; no contraindica futuras dosis salvo anafilaxia.",
        "Esquema México: cartilla nacional vigente 2024-2025 (CONAVA).",
    ],
    "revisar la cartilla físicamente; verbalizar las dosis pendientes por edad.",
    "anotas 'esquema completo' sin haber revisado la cartilla.",
    "CONAVA Esquema México 2024-2025; ACIP 2025; Red Book AAP 2024.",
    "pediatria", "vacunacion",
)

make_card(
    "PEDIATRÍA", "est-ped",
    "Ped5 · Escolaridad · conducta · sueño · interacción",
    '¿Asiste a guardería/escuela? ¿qué grado? ¿cómo va en aprovechamiento?\n'
    '¿Lo describen como tranquilo, inquieto, distraído?\n'
    '¿Cuántas horas duerme? ¿siesta? ¿ronca? ¿pesadillas o sonambulismo?\n'
    '¿Cómo se lleva con otros niños? ¿amigos?\n'
    '¿Tiempo de pantallas al día?\n'
    '¿Conductas repetitivas, intereses restringidos, contacto visual?\n'
    '¿Disciplina en casa? ¿castigo físico?',
    [
        "Bajo aprovechamiento + inquietud + distractibilidad + impulsividad ≥6 m en ≥2 ambientes = sospecha TDAH; aplicar Conners/Vanderbilt.",
        "Sueño: 0-3 m 14-17 h, 4-11 m 12-15 h, 1-2 a 11-14 h, 3-5 a 10-13 h, 6-13 a 9-11 h, 14-17 a 8-10 h (AASM).",
        "Ronquido habitual + apneas + somnolencia diurna → SAOS pediátrico → hipertrofia amigdalar (consulta ORL).",
        "Aislamiento social + intereses restringidos + déficit de comunicación = TEA hasta descartar (M-CHAT 18-30 m).",
        "Pantallas: 0 antes de 18 m; <1 h/día 2-5 a (AAP); ↑ pantallas = ↓ lenguaje, ↓ sueño, ↑ obesidad.",
        "Castigo físico = factor de riesgo para conducta agresiva, baja autoestima, trastornos mentales adultos.",
        "Maltrato (físico, sexual, emocional, negligencia) = obligación de denuncia legal en México (Ley de los Derechos NNA).",
    ],
    "preguntar conducta + sueño + escolar en TODA consulta pediátrica preventiva.",
    "no preguntas escolaridad, sueño o tiempo de pantallas.",
    "AAP Bright Futures 2022; AASM sleep duration; CDC ACEs.",
    "pediatria", "conducta", "sueño",
)

make_card(
    "PEDIATRÍA", "est-ped",
    "Ped6 · Signos de alarma por edad",
    'Lactante (&lt;1 a):\n'
    '• Rechazo al pecho, llanto débil, hipoactividad.\n'
    '• Fiebre &lt;3 meses → urgencia.\n'
    '• Cianosis, dificultad respiratoria, apneas.\n'
    '• Convulsiones, fontanela abombada.\n'
    'Preescolar/escolar:\n'
    '• Dolor abdominal recurrente con baja peso.\n'
    '• Cefalea matutina + vómito.\n'
    '• Cojera persistente, dolor óseo nocturno.\n'
    'Adolescente:\n'
    '• Ideación suicida, autolesiones.\n'
    '• Consumo de sustancias.\n'
    '• Pérdida o ganancia de peso súbita.\n'
    '• Embarazo o ITS.',
    [
        "Fiebre <3 meses = urgencia infectológica (sepsis neonatal, ITU, meningitis); evaluación completa + cultivos + ingreso si <28 d.",
        "Llanto inconsolable + irritabilidad + fontanela abombada = meningitis o trauma craneoencefálico (no obstrucción intestinal).",
        "Dolor abdominal recurrente + baja peso + sangre en heces = EII pediátrica (Crohn, CUCI) hasta descartar.",
        "Cefalea matutina + vómito en proyectil + papiledema = tumor cerebral (especialmente fosa posterior).",
        "Cojera + dolor óseo nocturno + fiebre = osteomielitis, leucemia, osteosarcoma.",
        "Ideación suicida en adolescente = preguntar DIRECTAMENTE (no induce conducta; sí salva vidas).",
        "Embarazo en adolescente = canalizar a control prenatal y orientación social; ITS = tratar + tamizar pareja.",
        "Maltrato físico: lesiones inexplicables, en distintas etapas, fracturas costales en lactante, hematoma retiniano (síndrome del niño sacudido).",
    ],
    "verbalizar las red flags pertinentes a la EDAD del paciente.",
    "no consideras edad al evaluar red flags pediátricas (no es lo mismo lactante que adolescente).",
    "AAP/CDC; UpToDate 'Red flags in pediatrics'; NICE NG143.",
    "pediatria", "red_flags",
)


# ============================================================
# 05 PSIQUIATRIA — 6 cards
# ============================================================

make_card(
    "PSIQUIATRÍA", "est-psiq",
    "Psiq1 · Examen mental (MSE) verbalizado",
    'Apariencia: aseo, vestido, edad aparente, postura.\n'
    'Actitud: cooperador, suspicaz, evasivo, hostil.\n'
    'Conducta motora: agitación, retardo, tics, manierismos, catatonia.\n'
    'Lenguaje: fluencia, latencia, volumen, prosodia.\n'
    'Afecto y ánimo: ánimo subjetivo + afecto observado (congruente/incongruente, amplio/aplanado).\n'
    'Pensamiento: curso (taquipsiquia/bradipsiquia/bloqueo) + contenido (delirios, ideación, obsesiones).\n'
    'Sensopercepción: alucinaciones (auditivas/visuales/táctiles), ilusiones, despersonalización.\n'
    'Cognición: orientación, atención, memoria, función ejecutiva (MoCA si sospecha).\n'
    'Juicio + introspección (insight).',
    [
        "MSE es el 'examen físico' del psiquiatra: documentar paso a paso (10 dominios estándar).",
        "Apariencia descuidada en paciente previamente cuidado → depresión, psicosis, deterioro cognitivo.",
        "Bradipsiquia + bradicinesia + ánimo bajo = depresión melancólica o hipotiroidismo.",
        "Fuga de ideas + taquilalia + grandiosidad = manía hasta descartar.",
        "Alucinaciones AUDITIVAS = típicas de esquizofrenia; VISUALES = orgánica/delirium/intoxicación.",
        "Pensamiento mágico, ideas referenciales, delirios = considerar esquizofrenia, manía psicótica, depresión psicótica.",
        "Desorientación reciente + atención fluctuante + curso agudo = DELIRIUM (no demencia).",
        "Juicio alterado en presencia de cognición preservada = trastorno psicótico o intoxicación.",
        "Insight ausente = peor pronóstico, peor adherencia al tratamiento.",
    ],
    "MSE se verbaliza durante la entrevista, no se hace 'aparte'; observas mientras hablas.",
    "no documentas MSE estructurado o lo confundes con DSM-5.",
    "DSM-5-TR; Bates 13ª; APA Practice Guideline on Psychiatric Evaluation.",
    "psiquiatria", "mse",
)

make_card(
    "PSIQUIATRÍA", "est-psiq",
    "Psiq2 · Ideación suicida — Columbia C-SSRS",
    'Voy a hacerle preguntas importantes:\n'
    '1. En el último mes, ¿ha tenido el deseo de estar muerto/a o no despertar?\n'
    '2. ¿Ha tenido pensamientos de hacerse daño o quitarse la vida?\n'
    '3. ¿Ha pensado en CÓMO podría hacerlo (método)?\n'
    '4. ¿Tiene un plan concreto?\n'
    '5. ¿Tiene los MEDIOS para hacerlo (acceso a arma, fármacos, etc.)?\n'
    '6. ¿Ha intentado hacerse daño en el pasado? ¿cuándo, cómo, qué pasó?\n'
    '7. ¿Qué le impide hacerlo hoy? (factores protectores)',
    [
        "Preguntar directamente NO INDUCE conducta suicida — múltiples estudios lo confirman (Dazzi 2014, meta-análisis).",
        "C-SSRS escala validada para tamizaje y estratificación de riesgo en urgencias y atención primaria.",
        "Ideación pasiva (querer estar muerto sin plan) = riesgo bajo-moderado; ideación activa con plan + medios = riesgo ALTO.",
        "Intento previo = factor de riesgo #1 para suicidio consumado (RR 5-10x); preguntar SIEMPRE.",
        "Acceso a medios letales (arma de fuego en casa, fármacos peligrosos) = retirar/restringir es intervención efectiva.",
        "Factores protectores: hijos pequeños, religión, miedo al dolor, red de apoyo, tratamiento activo.",
        "Hospitalización indicada si: plan + medios + intención + sin factor protector, o intento reciente.",
        "Contrato 'no suicidio' NO previene ni reduce riesgo (evidencia en contra); plan de seguridad sí (Stanley-Brown).",
    ],
    "preguntar es OBLIGATORIO en cualquier paciente con depresión, trastorno bipolar, esquizofrenia, abuso de sustancias.",
    "evitas preguntar por ideación suicida por miedo a 'sugerirla' o falta de tiempo.",
    "Columbia Lighthouse Project C-SSRS; Dazzi BMJ 2014; APA SMI guideline.",
    "psiquiatria", "suicidio", "urgencia",
)

make_card(
    "PSIQUIATRÍA", "est-psiq",
    "Psiq3 · Consumo de sustancias — CAGE / AUDIT-C",
    'CAGE (alcohol):\n'
    'C — ¿Ha sentido que debería REDUCIR (Cut) su consumo?\n'
    'A — ¿Le ha MOLESTADO (Annoyed) que critiquen su consumo?\n'
    'G — ¿Se ha sentido CULPABLE (Guilty) por beber?\n'
    'E — ¿Ha bebido al despertar para calmar nervios o resaca? (Eye-opener)\n'
    'Para cada sustancia: tabaco, marihuana, cocaína, opioides, anfetaminas, alucinógenos, inhalables, sedantes:\n'
    '• Edad de inicio · Último consumo · Frecuencia · Vía · Cantidad · Abstinencia previa.',
    [
        "CAGE ≥2 = posible trastorno por uso de alcohol; sens 70-90% para dependencia, baja para uso de riesgo.",
        "AUDIT-C es más sensible que CAGE para uso de riesgo (≥4 H / ≥3 M).",
        "Intoxicación aguda alcohol = alteración de juicio, ataxia, nistagmo; >300 mg/dL = riesgo coma.",
        "Abstinencia OH (CIWA): tremor 6-12 h, alucinaciones 12-24 h, convulsiones 24-48 h, delirium tremens 48-96 h.",
        "Cocaína intoxicación = HTA, taquicardia, midriasis, agitación, isquemia coronaria, ictus hemorrágico.",
        "Opioides intoxicación = miosis, depresión respiratoria, sedación; antídoto naloxona.",
        "Opioides abstinencia (COWS): rinorrea, lagrimeo, midriasis, piloerección, mialgias, diarrea.",
        "Benzodiacepinas abstinencia = potencialmente letal (convulsiones, delirium); tapering obligatorio.",
        "Comorbilidad SUD + trastorno mental = diagnóstico DUAL; tratar simultáneamente, no secuencialmente.",
    ],
    "preguntar TODAS las sustancias por separado; CAGE/AUDIT-C aplicado y verbalizado.",
    "preguntas solo 'consume alcohol o drogas' sin cuantificar ni aplicar instrumento.",
    "DSM-5-TR; CAGE Ewing JAMA 1984; AUDIT-C OMS; ASAM/APA SUD guidelines.",
    "psiquiatria", "sustancias",
)

make_card(
    "PSIQUIATRÍA", "est-psiq",
    "Psiq4 · Antecedentes psiquiátricos · personales y familiares",
    '¿Ha tenido antes algún episodio similar?\n'
    '¿Ha estado en tratamiento psicológico o psiquiátrico? ¿con qué dx?\n'
    '¿Ha tomado psicofármacos: antidepresivos, ansiolíticos, antipsicóticos, estabilizadores? ¿cuáles, dosis, respuesta?\n'
    '¿Ha estado hospitalizado/a por motivo psiquiátrico? ¿cuándo, dónde, cuánto tiempo?\n'
    '¿Intentos previos de suicidio? ¿método, lugar, consecuencias?\n'
    '¿Antecedentes familiares de depresión, bipolaridad, esquizofrenia, suicidio, alcoholismo?',
    [
        "Episodios previos definen DIAGNÓSTICO (depresión recurrente vs primer episodio; bipolar I requiere ≥1 episodio maníaco).",
        "Respuesta previa a fármaco específico predice respuesta actual (mismo agente o misma familia).",
        "Polifarmacia psiquiátrica + cambios frecuentes = sugiere refractariedad o dx subóptimo (reevaluar).",
        "Hospitalización previa = mayor severidad; preguntar voluntaria vs involuntaria.",
        "Intentos previos = factor de riesgo #1 para suicidio futuro; método de alta letalidad = riesgo mayor.",
        "AHF de bipolaridad → riesgo 10-15% (vs 1% población); altera DDx en depresión joven (cuidado con antidepresivo en monoterapia).",
        "AHF de suicidio en 1er grado = ↑3-6x riesgo independiente.",
        "AHF de esquizofrenia → 10% si 1 padre, 40% si ambos, 50% en gemelo monocigótico.",
    ],
    "preguntar antecedentes específicos por trastorno y por fármaco, no genéricos.",
    "anotas 'sin antecedentes psiquiátricos' sin haber preguntado por episodios, fármacos y AHF.",
    "DSM-5-TR; APA Practice Guidelines; UpToDate 'Psychiatric history'.",
    "psiquiatria", "antecedentes",
)

make_card(
    "PSIQUIATRÍA", "est-psiq",
    "Psiq5 · Función ocupacional · social · estresores recientes",
    '¿En qué trabaja o estudia? ¿ha cambiado su rendimiento?\n'
    '¿Cómo son sus relaciones: pareja, familia, amigos?\n'
    '¿Tiene alguien con quien hablar de lo que siente?\n'
    '¿Cómo está su vida sexual?\n'
    '¿Cambios recientes: pérdidas, mudanza, divorcio, despido, enfermedad, embarazo?\n'
    '¿Eventos traumáticos previos: accidentes, violencia, abuso, guerra, desastres?\n'
    '¿Estresor actual identificable?',
    [
        "Deterioro funcional ≥2 sem es criterio para episodio depresivo mayor (DSM-5).",
        "Aislamiento social = factor de riesgo independiente para suicidio, depresión, demencia, mortalidad CV.",
        "Pérdidas (duelo, divorcio, despido) son detonantes frecuentes de depresión; duelo no complicado vs trastorno de adaptación vs depresión mayor (DSM-5-TR ya separa los tres).",
        "Trauma previo + síntomas reexperimentación + evitación + hipervigilancia + alteración ánimo ≥1 mes = TEPT.",
        "Violencia de pareja activa → riesgo suicida + homicida en pareja + protección de hijos = canalización urgente.",
        "Abuso sexual previo (en cualquier edad) = factor de riesgo mayor para depresión, TEPT, TLP, somatización, suicidio.",
        "Cambio reciente del puesto laboral con autonomía perdida = estresor crónico, ↑ depresión y CV.",
    ],
    "explorar trauma y violencia con sensibilidad, sin urgir respuesta.",
    "anotas 'sin estresores' sin haber preguntado por trauma, violencia o cambios vitales.",
    "DSM-5-TR; PCL-5 para TEPT; APA Trauma & Stressor-Related Disorders.",
    "psiquiatria", "trauma", "social",
)

make_card(
    "PSIQUIATRÍA", "est-psiq",
    "Psiq6 · Evento desencadenante · duelo · violencia · abuso",
    '¿Hubo algún evento que disparó esto?\n'
    '¿Ha perdido a alguien cercano? ¿cuándo y cómo?\n'
    '¿Ha vivido algún evento muy doloroso (accidente, violencia, abuso)?\n'
    '¿Alguna vez alguien lo/la lastimó física, sexual o emocionalmente?\n'
    '¿Se siente seguro/a en este momento, en su casa, con su pareja?\n'
    '¿Tiene acceso a armas, fármacos peligrosos en casa?',
    [
        "Identificar EVENTO permite intervención dirigida (terapia de duelo, EMDR para trauma, salida de violencia).",
        "Duelo agudo (≤6 m) ≠ depresión mayor: tristeza centrada en el fallecido, en oleadas, capaz de momentos positivos.",
        "Trastorno de duelo prolongado (DSM-5-TR 2022) ≥12 m con anhelo intenso + disfunción = dx propio, tratamiento específico.",
        "Trauma reciente <1 m = trastorno de estrés agudo; ≥1 m = TEPT — manejo cambia.",
        "Pregunta de seguridad ('¿se siente seguro en casa?') es OBLIGATORIA en todo paciente con datos de violencia familiar o pareja.",
        "Acceso a medios letales (arma, fármacos en cantidad) en paciente con ideación = restringir es lifesaving (means restriction).",
        "Abuso en la infancia (ACE score ≥4) = riesgo CV, oncológico, depresión, suicidio, sustancias dramáticamente aumentado en adulto.",
    ],
    "preguntar trauma + violencia + acceso a medios; documentar sin juzgar y ofrecer apoyo.",
    "registras 'sin trauma' sin haber preguntado abierta y directamente.",
    "DSM-5-TR; CDC ACEs study; Means Matter (Harvard).",
    "psiquiatria", "trauma", "violencia",
)


# ============================================================
# 06 GINECO-OBSTETRICIA — 6 cards
# ============================================================

make_card(
    "GINECO-OBSTETRICIA", "est-gyo",
    "GO1 · FUM + ciclos menstruales",
    '¿Cuándo fue su última menstruación (FUM)? ¿día exacto?\n'
    '¿Sus reglas son regulares o irregulares? (intervalo en días)\n'
    '¿Cuántos días dura el sangrado? ¿cantidad de toallas/tampones por día?\n'
    '¿Coágulos? ¿inunda?\n'
    '¿Le duele al menstruar (dismenorrea)? ¿cede con AINE?\n'
    '¿Sangrado intermenstrual, postcoital, postmenopáusico?\n'
    '¿Síntomas premenstruales?',
    [
        "FUM con día exacto = primer dato para calcular semanas de gestación (regla de Naegele) o descartar embarazo.",
        "Ciclo regular = duración constante 21-35 d; irregular en pubertad y perimenopausia es normal, fuera de esos rangos investigar.",
        "Menorragia (>80 mL o >7 d o cambia toalla/h) → considerar SUA-O (ovulación), SUA-E (endometrio), SUA-L (leiomioma), SUA-C (coagulopatía); PALM-COEIN FIGO.",
        "Dismenorrea primaria (inicia con menarquia, cede con AINE) ≠ secundaria (inicia años después, sospecha endometriosis, adenomiosis, EPI).",
        "Sangrado postcoital = cervicitis, pólipo cervical, ca cérvix hasta descartar (citología, colposcopia).",
        "Sangrado postmenopáusico = ca endometrial hasta descartar (USG TV: endometrio >4 mm → biopsia).",
        "Sangrado intermenstrual + DIU → mala posición; + ACO → sangrado de disrupción; sin causa → estudiar.",
        "Síndrome premenstrual severo (TDPM) ≥5 síntomas en fase lútea ≥2 ciclos con disfunción → ISRS o ACO continuo.",
    ],
    "FUM exacta + patrón de ciclo + cantidad SIEMPRE; usar PALM-COEIN para clasificar SUA.",
    "registras 'menstruación normal' sin caracterizar duración, cantidad, dolor.",
    "FIGO PALM-COEIN 2018; ACOG Practice Bulletins; Williams Gynecology 4ª.",
    "gineco_obstetricia", "menstruacion",
)

make_card(
    "GINECO-OBSTETRICIA", "est-gyo",
    "GO2 · Antecedentes obstétricos — G / P / A / C",
    'G — ¿Cuántas veces ha estado embarazada en total?\n'
    'P — ¿Cuántos partos vaginales? ¿a término o pretérmino?\n'
    'A — ¿Pérdidas o abortos? ¿de qué semanas? ¿espontáneos o inducidos?\n'
    'C — ¿Cuántas cesáreas? ¿por qué indicación?\n'
    'Adicionales:\n'
    '• Ectópicos · molas · óbitos · hijos vivos · pesos al nacer.\n'
    '• Preeclampsia · diabetes gestacional · hemorragia obstétrica.\n'
    '• Lactancia previa.',
    [
        "Multípara ≥5 = riesgo de atonía uterina, placenta previa, prolapso.",
        "Parto pretérmino previo = factor #1 para parto pretérmino actual (RR ~2.5).",
        "Aborto recurrente (≥2 consecutivos <20 SDG) = estudiar SAF, trombofilia, anomalías uterinas, cariotipo parental.",
        "≥2 cesáreas previas o cesárea clásica = contraindicación relativa para parto vaginal posterior (TOLAC); riesgo de ruptura uterina.",
        "Acretismo placentario aumenta con número de cesáreas + placenta previa (riesgo 67% con 4 cesáreas previas + previa).",
        "Ectópico previo = recurrencia 10-20%; mola previa = control β-hCG 6-12 meses + anticoncepción.",
        "Preeclampsia previa = recurrencia 15-20%; AAS 100-150 mg desde 12 SDG en embarazo siguiente (USPSTF).",
        "Diabetes gestacional previa = 50% riesgo DM2 a 10 a; tamizar HbA1c c/3 a; siguiente embarazo glucemia precoz.",
    ],
    "registrar como G_ P_ A_ C_ (ej. G3 P1 A1 C1) + complicaciones obstétricas relevantes.",
    "no preguntas indicación de cesárea o complicaciones obstétricas previas.",
    "ACOG Practice Bulletin VBAC; Williams 26ª; USPSTF preeclampsia 2021.",
    "gineco_obstetricia", "obstetricos",
)

make_card(
    "GINECO-OBSTETRICIA", "est-gyo",
    "GO3 · IVSA · parejas · ITS · dispareunia",
    '¿A qué edad inició relaciones sexuales (IVSA)?\n'
    '¿Cuántas parejas sexuales en total y en el último año?\n'
    '¿Pareja actual: hombre, mujer, ambos?\n'
    '¿Usa protección? ¿siempre, a veces, nunca?\n'
    '¿Antecedente de ITS: tricomonas, clamidia, gonorrea, VPH, herpes, sífilis, VIH, hepatitis B/C?\n'
    '¿Dispareunia (dolor al coito)? ¿superficial o profundo?\n'
    '¿Sangrado postcoital? ¿flujo anormal?\n'
    '¿Violencia o coerción sexual?',
    [
        "IVSA temprana (<18 a) = mayor exposición a VPH = ↑ riesgo ca cervicouterino.",
        "Múltiples parejas o pareja con múltiples parejas = factor de riesgo para todas las ITS.",
        "Conducta sexual orienta tamizaje: VIH anual a todas; clamidia/gonorrea anual ≤25 a o conducta riesgo; VHC 1× ≥18 a (USPSTF).",
        "Embarazada: tamizar VIH, sífilis, hepatitis B, clamidia/gonorrea, urocultivo, VHC.",
        "Dispareunia superficial = vulvovaginitis, vaginismo, atrofia (post-menopausia); profunda = endometriosis, EPI, masa pélvica.",
        "Sangrado postcoital = cervicitis, ectropión, pólipo, ca cervicouterino — colposcopia obligatoria si persiste.",
        "VPH alto riesgo (16, 18) → citología/co-test; vacuna ≤26 a (extendible 27-45 a con shared decision).",
        "Violencia sexual = tamizar en TODA mujer (USPSTF grado B); kit de profilaxis + anticoncepción de emergencia + tamizaje ITS y embarazo.",
    ],
    "preguntar conducta sexual SIEMPRE, sin asumir orientación o número de parejas.",
    "no preguntas conducta sexual por pudor; asumes monogamia o heterosexualidad.",
    "CDC STI Treatment 2024; USPSTF 2024; ACOG Committee Opinions.",
    "gineco_obstetricia", "its", "sexual",
)

make_card(
    "GINECO-OBSTETRICIA", "est-gyo",
    "GO4 · Anticoncepción + deseo genésico",
    '¿Usa algún método anticonceptivo actualmente? ¿cuál?\n'
    '¿Desde cuándo lo usa? ¿está conforme?\n'
    '¿Ha tenido efectos adversos (sangrado, peso, ánimo, libido)?\n'
    '¿Desea embarazarse en los próximos 1-2 años?\n'
    '¿Ha pensado en métodos de larga duración (DIU, implante)?\n'
    '¿Ha usado anticoncepción de emergencia? ¿cuándo?\n'
    '¿Antecedente de TVP/TEP, migraña con aura, HTA no controlada, ca mama? (contraindican estrógenos)',
    [
        "Método ideal = el más efectivo que la paciente esté dispuesta a usar consistentemente.",
        "LARC (DIU, implante) = efectividad >99% (uso típico = uso perfecto); reduce embarazo no planeado drásticamente.",
        "ACO combinado = contraindicado en TVP/TEP previa, migraña con aura, HTA >160/100, lactancia <6 sem, fumadora >35 a, ca mama (CDC US-MEC).",
        "DIU Cu = primera línea para AE hasta 5 d post-coito (más efectivo que píldora).",
        "Levonorgestrel 1.5 mg AE ≤72 h; ulipristal ≤120 h (más efectivo).",
        "Lactancia: progestágeno solo seguro; combinado evitar <6 sem postparto.",
        "Deseo de embarazo en <1 a = preparación pregestacional: ácido fólico 400-800 mcg, tamizar rubéola, varicela, hep B, VIH, tóxicos.",
        "Falta de adherencia a ACO = motivo principal de fallo; ofrecer alternativas (LARC, parche, anillo, inyectable).",
    ],
    "siempre explorar deseo genésico y ofrecer todos los métodos (no solo el más popular).",
    "recomendas un método sin valorar contraindicaciones (TVP, migraña con aura, lactancia).",
    "CDC US-MEC 2024; ACOG Practice Bulletins; FIGO LARC.",
    "gineco_obstetricia", "anticoncepcion",
)

make_card(
    "GINECO-OBSTETRICIA", "est-gyo",
    "GO5 · Tamizaje ginecológico — papanicolaou · colposcopia · mamografía · DMO",
    'Papanicolaou: ¿se lo ha hecho? ¿cuándo el último? ¿resultado?\n'
    'VPH cotest (≥30 a): ¿se ha realizado?\n'
    'Colposcopia: ¿ha tenido lesión cervical, cono, criocirugía?\n'
    'Mamografía: ¿se la ha hecho? ¿desde qué edad y cada cuánto?\n'
    'Autoexploración mamaria: ¿la realiza?\n'
    'Densitometría ósea: ¿se la ha hecho? (≥65 a o &lt;65 con riesgo)\n'
    'Vacunación VPH y hep B.',
    [
        "Papanicolaou 21-65 a c/3 a (USPSTF grado A); ≥30 a co-test VPH c/5 a aceptable.",
        "ASCCP 2019: VPH primario c/5 a opción preferida en algunos contextos.",
        "Citología/HPV anormal → colposcopia + biopsia dirigida; LSIL → vigilancia; HSIL/AGC → cono o LLETZ.",
        "Mamografía 40-74 a bienal (USPSTF 2024 grado B); riesgo alto (BRCA, AHF temprano) → inicio a 30 a + RM.",
        "Autoexploración mamaria: USPSTF NO la recomienda formalmente (evidencia I), pero consciencia mamaria útil.",
        "Examen clínico mamario por médico: USPSTF evidencia I; ACOG sí lo recomienda c/1-3 a 25-39 y anual ≥40.",
        "DMO con DEXA mujer ≥65 a (USPSTF grado B); <65 con FRAX ≥9.3% (osteoporosis posmenopáusica precoz, cortico, esteroide).",
        "Vacuna VPH ≤26 a; AE 27-45 a si no recibió.",
    ],
    "verbalizar tamizaje pertinente a la edad/sexo del caso, no enumerar todo.",
    "no preguntas papanicolaou, mamografía o DMO en mujer de la edad correspondiente.",
    "USPSTF 2024; ASCCP 2019; ACOG; NAMS 2024.",
    "gineco_obstetricia", "tamizaje",
)

make_card(
    "GINECO-OBSTETRICIA", "est-gyo",
    "GO6 · Embarazo actual — FUR, EG, controles, USG, lab",
    'FUR exacta + regla de Naegele: FUR + 7 d − 3 m + 1 a → FPP.\n'
    'EG por FUR vs USG (más confiable USG primer trimestre).\n'
    'Controles prenatales: ¿cuántos? ¿en qué semanas?\n'
    'USG: 1er trimestre (10-13 SDG translucencia nucal), 2do (18-22 anatomía), 3er (28-32 crecimiento).\n'
    'Laboratorios: BH, GS-Rh, glucosa, EGO + urocultivo, VDRL, VIH, HBsAg, AcHbsAg, AcVHC, rubéola IgG, varicela IgG, TORCH si indicado, CTOG 24-28 SDG.\n'
    'Movimientos fetales: ≥10 en 2 h después de 28 SDG.\n'
    'Signos de alarma: cefalea + visión borrosa + epigastralgia + edema + sangrado + LA + contracciones <37 SDG.',
    [
        "FUR confiable solo si ciclos regulares y no usaba ACO en los 3 meses previos; en caso contrario, ajustar con USG de 1er trimestre (más exacto).",
        "Mínimo 8 consultas prenatales (OMS 2016): 12, 20, 26, 30, 34, 36, 38, 40 SDG.",
        "USG 11-14 SDG: translucencia nucal + PAPP-A + β-hCG = tamizaje aneuploidías; >3 mm sospecha.",
        "USG anatómica 18-22 SDG = malformaciones; longitud cervical (riesgo parto pretérmino).",
        "Iso-inmunización Rh: madre Rh− + padre Rh+ → Coombs indirecto; profilaxis con Ig anti-D 28 SDG + postparto.",
        "VIH, sífilis, hepatitis B en TODAS las embarazadas (USPSTF grado A).",
        "CTOG 24-28 SDG (75 g, 1 medición ≥180/153/140) = diabetes gestacional → manejo nutricional + insulina si falla.",
        "Signos de alarma de preeclampsia: cefalea pertinaz, escotomas, epigastralgia (HELLP), edema rápido, oliguria.",
        "Conteo de movimientos fetales (Cardiff o Sadovsky): <10 en 2 h → NST.",
    ],
    "verbalizar TODAS las pertinentes: FUR + EG + USG previas + lab estándar + signos de alarma.",
    "anotas 'control prenatal en curso' sin verificar laboratorios, USG y datos de alarma.",
    "OMS ANC 2016; ACOG; NOM-007-SSA2-2016; USPSTF.",
    "gineco_obstetricia", "embarazo",
)


# ============================================================
# 07 TRANSVERSAL — 1 card (mujer fértil, recordatorio)
# ============================================================

make_card(
    "TRANSVERSAL ♀ FÉRTIL", "est-transv",
    "MF♀ · Antes de Rx / fármaco / cirugía en mujer en edad fértil",
    'Antes de:\n'
    '• Prescribir un fármaco potencialmente teratógeno.\n'
    '• Indicar estudio con radiación ionizante (Rx, TC).\n'
    '• Someter a procedimiento quirúrgico con anestesia.\n'
    'PREGUNTAR:\n'
    '1. ¿Cuál fue su última menstruación (FUM)?\n'
    '2. ¿Está usando anticoncepción? ¿cuál?\n'
    '3. ¿Existe posibilidad de embarazo?\n'
    '4. SI HAY DUDA → solicitar β-hCG cuantitativa antes del procedimiento.',
    [
        "Teratógenos categoría X/D (warfarina, IECA, valproato, isotretinoína, metotrexate, talidomida, estatinas, misoprostol fuera de obstetricia, AINE >30 SDG).",
        "Radiación ionizante: TC abdomen-pelvis ~10-25 mGy fetal — minimizar 1er trimestre (organogénesis); >100 mGy = riesgo determinístico.",
        "RM y USG son seguros en embarazo; contraste gadolinio NO en 1er trimestre (categoría C); contraste yodado evitar si posible (hipotiroidismo neonatal).",
        "Embarazo no diagnosticado al momento de cirugía electiva = posponer; urgencia = proceder con protección uterina, evitar ciertos anestésicos.",
        "Anticoncepción de emergencia (levonorgestrel ≤72 h, ulipristal ≤120 h, DIU Cu ≤5 d) si coito sin protección.",
        "Pre-conceptional: ácido fólico 400-800 mcg desde 1 mes pre-concepción; 4 mg en DM, antiepilépticos, hijo previo con DTN.",
        "Suspender teratógenos antes de embarazo: warfarina → HBPM; IECA → labetalol; isotretinoína → 1 mes pre + dos métodos de anticoncepción.",
    ],
    "esta pregunta SIEMPRE en MF / MI / Cx / Psiquiatría con mujer 12-50 años.",
    "prescribes teratógeno o indicas radiación sin descartar embarazo en mujer fértil.",
    "FDA Pregnancy Categories; ACOG Committee Opinion 723 (Imaging); CDC preconception 2024.",
    "transversal", "mujer_fertil",
)


# ============================================================
# GENERAR .APKG
# ============================================================
if __name__ == "__main__":
    output_path = os.path.join(
        OUTPUT_DIR,
        "Preparacion_Verbalizada_Deck1_Interrogatorio_Universal.apkg",
    )
    genanki.Package(deck).write_to_file(output_path)
    print(f"✓ Generado: {output_path}")
    print(f"  Total notas: {len(deck.notes)}")
    print(f"  Deck ID: {DECK_ID}")
    print(f"  Deck name: {DECK_NAME}")
