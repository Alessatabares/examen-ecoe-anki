"""
Ruidos Cardiacos Pediátrico — Capa 2 (Componentes)
Guías: AHA scientific statements (cardiopatías congénitas, Jones 2015, screening neonatal)
Output: output/Ruidos_Cardiacos_Pediatrico_Capa2.apkg
"""
import os
import json
import genanki

TEMA_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPO_ROOT = os.path.dirname(TEMA_ROOT)
OUTPUT = os.path.join(TEMA_ROOT, "output", "Ruidos_Cardiacos_Pediatrico_Capa2.apkg")
IDS_PATH = os.path.join(REPO_ROOT, "ids.json")

DECK_ID = 1577267608
DECK_NAME = "Ruidos Cardiacos Pediátrico::Capa 2 - Componentes"

with open(IDS_PATH) as f:
    MODEL_ID = json.load(f)["models"]["cloze_estandar"]

CSS = """
.card {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  font-size: 19px; text-align: left; color: #1a1a1a;
  background-color: #fafafa; padding: 20px; line-height: 1.5;
}
.cloze { font-weight: 600; color: #2563eb; }
#extra { margin-top: 16px; border: none; border-top: 1px solid #d4d4d4; }
"""

model = genanki.Model(
    MODEL_ID,
    "Estudio Médico Cloze",
    fields=[{"name": "Text"}, {"name": "Extra"}],
    templates=[{
        "name": "Cloze",
        "qfmt": "{{cloze:Text}}",
        "afmt": '{{cloze:Text}}<hr id="extra">{{Extra}}',
    }],
    css=CSS,
    model_type=genanki.Model.CLOZE,
)

BASE_TAGS = ["capa2", "ruidos_cardiacos_pediatrico", "aha", "ecoe"]

CARDS = [
    # Bloque A — Escala de Levine + criterios de inocencia
    {
        "text": "Escala de Levine: **1/6** muy suave, requiere concentración. **2/6** suave pero {{c1::audible al instante}}. **3/6** moderadamente alto, {{c2::sin frémito}}. **4/6** alto, {{c3::con frémito palpable}}.",
        "extra": "El umbral del frémito (vibración palpable) está entre 3/6 y 4/6. Frémito = soplo patológico, descarta inocente.",
        "tags": ["levine", "intensidad"],
    },
    {
        "text": "Escala de Levine: **5/6** audible con el estetoscopio {{c1::apenas tocando la piel}}. **6/6** audible con el estetoscopio {{c2::separado de la piel}}.",
        "extra": "Soplos 5-6/6 son siempre patológicos y de alta severidad. En la práctica clínica reales son raros — la mayoría de soplos están entre 2/6 y 4/6.",
        "tags": ["levine", "intensidad"],
    },
    {
        "text": "Criterios de soplo inocente (todos deben cumplirse): intensidad {{c1::≤2/6}}, {{c2::sistólico}} (nunca diastólico ni continuo), sin frémito, sin irradiación amplia, {{c3::cambia con la postura}}, S2 normal, niño asintomático.",
        "extra": "Basta con que falle UN criterio para descartar la etiqueta de inocente. Cualquier soplo diastólico o ≥3/6 = ecocardiograma obligatorio.",
        "tags": ["inocente", "criterios"],
    },

    # Bloque B — CIV por tamaño y Qp/Qs
    {
        "text": "CIV **pequeña (restrictiva)**: diámetro {{c1::&lt;1/3 del anillo aórtico}}, Qp/Qs {{c2::&lt;1.5}}, asintomática, alto índice de cierre espontáneo; manejo: {{c3::observación con ecocardiogramas periódicos}}.",
        "extra": "La mayoría de CIVs musculares pequeñas cierran espontáneamente antes de los 5 años. No requieren restricción de actividad ni profilaxis de endocarditis salvo antecedente previo.",
        "tags": ["civ", "tamaño"],
    },
    {
        "text": "CIV **mediana** (Qp/Qs {{c1::1.5-2.2}}) o **grande/no restrictiva** (&gt;1/2 del anillo aórtico, Qp/Qs {{c2::&gt;2.2}}) → indicación de {{c3::cierre quirúrgico o percutáneo}}; sin cierre, riesgo de hipertensión pulmonar y {{c4::síndrome de Eisenmenger}}.",
        "extra": "Eisenmenger = inversión del shunt (D→I) por hipertensión pulmonar irreversible. A partir de ahí el cierre quirúrgico está contraindicado.",
        "tags": ["civ", "tamaño", "manejo"],
    },

    # Bloque C — PCA Qp/Qs y manejo
    {
        "text": "PCA por Qp/Qs: silente/pequeño {{c1::&lt;1.5}} → seguimiento; moderado {{c2::1.5-2.2}} → cierre; grande {{c3::&gt;2.2}} o sintomático → cierre indicación clase I.",
        "extra": "El umbral de cierre considera Qp/Qs + presencia de dilatación de cavidades izquierdas + síntomas (falla cardiaca, retraso pondoestatural, hipertensión pulmonar).",
        "tags": ["pca", "qps"],
    },
    {
        "text": "PCA en **prematuro**: cierre farmacológico con {{c1::indometacina o ibuprofeno}} (inhiben prostaglandinas). Si falla → cierre quirúrgico. En **niño/adulto**: cierre {{c2::percutáneo}} con dispositivo (Amplatzer).",
        "extra": "Contraindicaciones a indometacina/ibuprofeno: enterocolitis necrotizante, hemorragia activa, insuficiencia renal. Paracetamol es alternativa emergente.",
        "tags": ["pca", "manejo"],
    },

    # Bloque D — EP gradientes
    {
        "text": "Estenosis pulmonar — gradiente pico transvalvular: **leve** {{c1::&lt;36 mmHg}} (velocidad &lt;3 m/s), **moderada** {{c2::36-64 mmHg}} (velocidad 3-4 m/s), **severa** {{c3::&gt;64 mmHg}} (velocidad &gt;4 m/s).",
        "extra": "El gradiente Doppler se estima por la ecuación de Bernoulli simplificada: ΔP = 4 × v². Una velocidad de 4 m/s = gradiente de 64 mmHg.",
        "tags": ["estenosis_pulmonar", "gradiente"],
    },
    {
        "text": "Indicación de **valvuloplastia pulmonar con balón**: gradiente pico {{c1::&gt;40 mmHg}} en paciente sintomático, o {{c2::&gt;60 mmHg}} en asintomático.",
        "extra": "Procedimiento de elección en EP valvular pediátrica. Tasa de éxito &gt;90%. Complicaciones raras (insuficiencia pulmonar residual leve es esperable).",
        "tags": ["estenosis_pulmonar", "manejo"],
    },

    # Bloque E — Jones 2015
    {
        "text": "Criterios de Jones revisados 2015 — **mayores** (5): {{c1::carditis}} (clínica o subclínica por ecocardiograma), {{c2::poliartritis migratoria}}, {{c3::corea de Sydenham}}, {{c4::eritema marginado}}, {{c5::nódulos subcutáneos}}.",
        "extra": "Novedad 2015: carditis subclínica (solo por eco) cuenta como criterio mayor. En poblaciones de alto riesgo, monoartritis o poliartralgia también cuentan.",
        "tags": ["fiebre_reumatica", "jones"],
    },
    {
        "text": "Criterios de Jones **menores**: artralgia (si no se contó poliartritis), {{c1::fiebre ≥38.5°C}}, {{c2::VES ≥60 o PCR ≥3 mg/dL}}, {{c3::PR prolongado en ECG}}.",
        "extra": "Los menores son inespecíficos: por eso siempre exigen acompañamiento de mayores y evidencia de infección estreptocócica.",
        "tags": ["fiebre_reumatica", "jones"],
    },
    {
        "text": "Diagnóstico de fiebre reumática: {{c1::2 mayores}} o {{c2::1 mayor + 2 menores}}, **más** {{c3::evidencia de infección estreptocócica reciente}} (ASLO o anti-DNAsa B elevados, cultivo o antígeno positivo).",
        "extra": "Sin evidencia de infección estreptocócica reciente no se diagnostica fiebre reumática aunque haya criterios clínicos — único excepción: corea de Sydenham aislada.",
        "tags": ["fiebre_reumatica", "jones", "diagnostico"],
    },

    # Bloque F — MCH pediátrica
    {
        "text": "Criterio diagnóstico de MCH pediátrica por ecocardiograma: grosor parietal del VI {{c1::&gt;2 desviaciones estándar (z-score &gt;2)}} del esperado para edad y superficie corporal, sin causa secundaria.",
        "extra": "El criterio adulto (≥15 mm) no aplica en niño porque el grosor normal varía con el crecimiento. Se usa z-score.",
        "tags": ["mch", "diagnostico"],
    },
    {
        "text": "Screening de MCH en deportista joven o familiar de primer grado de paciente con MCH: {{c1::ECG + ecocardiograma}}. Antecedente familiar de muerte súbita en &lt;50 años obliga a {{c2::evaluación cardiológica antes de actividad competitiva}}.",
        "extra": "AHA recomienda screening preparticipación con historia + examen físico. El ECG sistemático es debate, pero en familiares de MCH es obligado.",
        "tags": ["mch", "screening"],
    },

    # Bloque G — Tetralogía de Fallot
    {
        "text": "Tetralogía de Fallot — los 4 componentes anatómicos: {{c1::CIV grande malalineada}}, {{c2::cabalgamiento aórtico}}, {{c3::obstrucción al tracto de salida del VD (estenosis pulmonar/infundibular)}}, {{c4::hipertrofia del VD}}.",
        "extra": "El cabalgamiento aórtico significa que la aorta nace 'a caballo' sobre el septum, parcialmente sobre el VD. El grado de obstrucción RVOT determina la severidad de la cianosis.",
        "tags": ["fallot", "anatomia"],
    },
    {
        "text": "RX tórax clásica en Fallot: silueta cardiaca en {{c1::\"bota\" (coeur en sabot)}} por hipertrofia del VD y arco pulmonar cóncavo. Cianosis aparece típicamente entre {{c2::2-6 meses}} cuando la obstrucción RVOT progresa.",
        "extra": "Crisis hipoxémicas ('tet spells'): cianosis aguda con llanto/esfuerzo. Manejo agudo: posición genupectoral, oxígeno, morfina, betabloqueador, fenilefrina si refractario.",
        "tags": ["fallot", "imagen"],
    },

    # Bloque H — CIA
    {
        "text": "CIA — anchor auscultatorio: {{c1::S2 desdoblado fijo}} (no varía con la respiración) + soplo sistólico de hiperflujo en {{c2::foco pulmonar}}.",
        "extra": "El desdoblamiento fijo se explica porque el shunt I→D iguala el volumen del VD en inspiración y espiración. Es patognomónico de CIA.",
        "tags": ["cia", "auscultacion"],
    },
    {
        "text": "CIA — indicación de cierre: Qp/Qs {{c1::&gt;1.5}} con dilatación de cavidades derechas. Presentación típica: {{c2::tardía (4-5 años o adulto joven)}}, frecuentemente asintomática hasta entonces.",
        "extra": "Cierre percutáneo (Amplatzer) es de elección en CIA ostium secundum con bordes adecuados. CIA ostium primum y seno venoso requieren cirugía.",
        "tags": ["cia", "manejo"],
    },

    # Bloque I — Screening neonatal saturometría
    {
        "text": "Saturometría neonatal de screening — sitios de medición: {{c1::pre-ductal (mano derecha)}} y {{c2::post-ductal (pie)}}. Momento óptimo: entre {{c3::24-48 horas de vida}}.",
        "extra": "El conducto arterioso aún permeable en las primeras horas puede enmascarar diferencias pre/post-ductales. Por eso se espera a las 24-48h.",
        "tags": ["screening_neonatal"],
    },
    {
        "text": "Saturometría positiva para sospecha de cardiopatía congénita crítica: SpO2 {{c1::&lt;90%}} en cualquier extremidad, **o** SpO2 {{c2::&lt;95%}} en ambas, **o** diferencia pre/post-ductal {{c3::&gt;3%}}. Conducta: {{c4::ecocardiograma}}.",
        "extra": "Cardiopatías que detecta este screening: transposición de grandes arterias, atresia pulmonar, Fallot, drenaje venoso anómalo total, atresia tricuspídea, ventrículo único, tronco arterioso, síndrome de corazón izquierdo hipoplásico.",
        "tags": ["screening_neonatal", "cardiopatias_criticas"],
    },
]

deck = genanki.Deck(DECK_ID, DECK_NAME)

for card in CARDS:
    note = genanki.Note(
        model=model,
        fields=[card["text"], card["extra"]],
        tags=BASE_TAGS + card["tags"],
    )
    deck.add_note(note)

os.makedirs(os.path.dirname(OUTPUT), exist_ok=True)
genanki.Package(deck).write_to_file(OUTPUT)

print(f"Notas: {len(CARDS)}")
print(f"DECK_ID: {DECK_ID}")
print(f"Output: {OUTPUT}")
