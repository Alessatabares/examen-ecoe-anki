"""
Ruidos Cardiacos Adulto — Capa 2 (Componentes)
Guías: AHA/ACC 2020 Valvular Heart Disease + Duke modificados + AHA endocarditis prophylaxis
Output: output/Ruidos_Cardiacos_Adulto_Capa2.apkg
"""
import os
import json
import genanki

TEMA_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPO_ROOT = os.path.dirname(TEMA_ROOT)
OUTPUT = os.path.join(TEMA_ROOT, "output", "Ruidos_Cardiacos_Adulto_Capa2.apkg")
IDS_PATH = os.path.join(REPO_ROOT, "ids.json")

DECK_ID = 1695400845
DECK_NAME = "Ruidos Cardiacos Adulto::Capa 2 - Componentes"

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

BASE_TAGS = ["capa2", "ruidos_cardiacos_adulto", "aha", "ecoe"]

# Note: &lt; y &gt; usados desde el inicio para evitar que Anki interprete <X o >X como tags HTML.
CARDS = [
    # Bloque A — Levine + técnica
    {
        "text": "Recordatorio Levine: frémito palpable empieza en grado {{c1::4/6}}. Soplos {{c2::5-6/6}} son siempre severos y patológicos.",
        "extra": "Grado 5/6: audible con el estetoscopio apenas tocando la piel. Grado 6/6: audible con el estetoscopio separado de la piel.",
        "tags": ["levine", "intensidad"],
    },
    {
        "text": "Auscultación — **campana** para tonos {{c1::bajos (S3, S4, retumbo de EM)}}; **diafragma** para tonos {{c2::altos (soplos de IAo, IM, EA)}}.",
        "extra": "Truco ECOE: si buscas EM (retumbo diastólico), pon al paciente en decúbito lateral izquierdo y usa la campana en ápex.",
        "tags": ["tecnica"],
    },

    # Bloque B — EA
    {
        "text": "EA severa (estadio C, asintomática) — criterios eco: Vmax {{c1::≥4 m/s}}, gradiente medio {{c2::≥40 mmHg}}, área valvular {{c3::≤1.0 cm²}} (o ≤0.6 cm²/m²).",
        "extra": "Etapas AHA/ACC 2020: A (en riesgo), B (progresiva), C (severa asintomática), D (severa sintomática). El estadio decide el tratamiento.",
        "tags": ["ea", "severidad"],
    },
    {
        "text": "EA **muy severa**: Vmax {{c1::≥5 m/s}} o gradiente medio {{c2::≥60 mmHg}}.",
        "extra": "EA muy severa asintomática es indicación clase IIa de reemplazo valvular incluso sin síntomas, por alto riesgo de muerte súbita.",
        "tags": ["ea", "severidad"],
    },
    {
        "text": "Indicación de TAVR/SAVR: EA severa **sintomática** (estadio D1), o EA severa asintomática con {{c1::FE &lt;50%}}, o {{c2::test de ejercicio positivo}}.",
        "extra": "Tríada clásica de EA sintomática severa: angina, síncope, disnea. Cualquiera de los tres con EA severa es indicación quirúrgica.",
        "tags": ["ea", "manejo"],
    },

    # Bloque C — IM
    {
        "text": "IM **primaria** (estructural): {{c1::prolapso valvular, ruptura cordal, endocarditis}}. IM **secundaria** (funcional): por {{c2::dilatación del VI / miocardiopatía}} sin defecto valvular intrínseco.",
        "extra": "La distinción primaria/secundaria es crítica para el manejo: primaria se beneficia de cirugía reparadora; secundaria responde primero a tratamiento de la causa de fondo (insuficiencia cardiaca, isquemia).",
        "tags": ["im", "clasificacion"],
    },
    {
        "text": "IM severa por eco: ERO (orificio regurgitante efectivo) {{c1::≥40 mm²}}, volumen regurgitante {{c2::≥60 mL/latido}}, fracción regurgitante {{c3::≥50%}}, vena contracta {{c4::≥7 mm}}.",
        "extra": "ERO se calcula por método PISA. Indicación de cirugía: IM severa sintomática, o asintomática con FE ≤60% o diámetro telesistólico VI ≥40 mm.",
        "tags": ["im", "severidad"],
    },

    # Bloque D — IAo
    {
        "text": "IAo severa por eco: vena contracta {{c1::&gt;6 mm}}, fracción regurgitante {{c2::≥50%}}, volumen regurgitante {{c3::≥60 mL/latido}}, ERO {{c4::≥30 mm²}}.",
        "extra": "Ojo: los umbrales numéricos de IAo y IM severas son similares pero NO idénticos (vena contracta IM ≥7 mm vs IAo &gt;6 mm; ERO IM ≥40 mm² vs IAo ≥30 mm²).",
        "tags": ["iao", "severidad"],
    },
    {
        "text": "Indicación de cirugía en IAo severa: paciente {{c1::sintomático}}, o asintomático con {{c2::FE ≤55%}}, o {{c3::diámetro telesistólico VI &gt;50 mm}}.",
        "extra": "IAo crónica permite años asintomáticos por adaptación del VI (dilatación + hipertrofia excéntrica). La aparición de síntomas o de disfunción ventricular es 'tarde' fisiopatológicamente.",
        "tags": ["iao", "manejo"],
    },

    # Bloque E — EM
    {
        "text": "Estenosis mitral por área valvular: significativa {{c1::≤1.5 cm²}}; severa {{c2::≤1.0 cm²}}.",
        "extra": "Mitral normal: 4-6 cm². Síntomas (disnea de esfuerzo) suelen aparecer cuando el área baja de 2 cm². Etiología #1: fiebre reumática.",
        "tags": ["em", "severidad"],
    },
    {
        "text": "Indicación de **comisurotomía percutánea con balón** en EM severa sintomática: anatomía favorable (score de Wilkins {{c1::≤8}}), sin {{c2::trombo en aurícula izquierda}} ni IM moderada/severa.",
        "extra": "Score de Wilkins evalúa: movilidad valvular, engrosamiento valvular, engrosamiento subvalvular y calcificación (cada uno de 1 a 4 puntos). Score ≥9 → cirugía abierta preferible.",
        "tags": ["em", "manejo"],
    },

    # Bloque F — PVM
    {
        "text": "Criterio diagnóstico ecocardiográfico de prolapso mitral: desplazamiento {{c1::&gt;2 mm}} de los velos mitrales por encima del plano anular en vista paraesternal eje largo. Engrosamiento de velos {{c2::&gt;5 mm}} = prolapso **clásico** (mayor riesgo de complicaciones).",
        "extra": "Complicaciones del PVM: insuficiencia mitral progresiva, endocarditis, arritmias auriculares/ventriculares, muerte súbita (rara). PVM clásico tiene 5× más riesgo de eventos que no-clásico.",
        "tags": ["pvm", "diagnostico"],
    },

    # Bloque G — MCH adulto
    {
        "text": "Criterio diagnóstico de MCH adulto por eco: grosor parietal máximo del VI {{c1::≥15 mm}}, o {{c2::≥13 mm}} si antecedente familiar de primer grado, sin causa secundaria (HTA severa, EA, atleta).",
        "extra": "Diagnóstico diferencial crítico: corazón de atleta (grosor 12-15 mm, regresa con desentrenamiento, función diastólica normal) vs MCH (grosor ≥15 mm, función diastólica alterada, no regresa).",
        "tags": ["mch", "diagnostico"],
    },
    {
        "text": "MCH **obstructiva**: gradiente en el tracto de salida del VI {{c1::≥30 mmHg}} en reposo, o {{c2::≥50 mmHg}} con provocación (Valsalva, ejercicio).",
        "extra": "El gradiente dinámico es la clave de MCH: cambia con la precarga y la contractilidad. Por eso Valsalva (↓ precarga) lo aumenta — distintivo vs EA, cuyo gradiente es fijo.",
        "tags": ["mch", "obstruccion"],
    },

    # Bloque H — Endocarditis (Duke modificados)
    {
        "text": "Criterios de Duke — **mayores** (2): {{c1::hemocultivos positivos para microorganismo típico (2 separados, persistentes, o Coxiella burnetii)}}; evidencia ecocardiográfica de {{c2::vegetación, absceso, dehiscencia protésica nueva, o nueva regurgitación valvular}}.",
        "extra": "Microorganismos típicos: estreptococos del grupo viridans, S. aureus, S. bovis, grupo HACEK, enterococo adquirido en comunidad sin foco primario.",
        "tags": ["endocarditis", "duke"],
    },
    {
        "text": "Criterios de Duke — **menores** (5): {{c1::predisposición (cardiopatía o uso de drogas IV)}}, {{c2::fiebre ≥38°C}}, {{c3::fenómenos vasculares (émbolos, Janeway, hemorragias conjuntivales)}}, {{c4::fenómenos inmunológicos (glomerulonefritis, Osler, Roth, FR+)}}, evidencia microbiológica que no cumple mayor.",
        "extra": "Mnemonia: FIVE = Fiebre, Inmunológicos, Vasculares, Eco/microbiológicos menores, Predisposición.",
        "tags": ["endocarditis", "duke"],
    },
    {
        "text": "Diagnóstico de endocarditis **definitiva**: {{c1::2 mayores}}, o {{c2::1 mayor + 3 menores}}, o {{c3::5 menores}}. **Posible**: 1 mayor + 1 menor, o 3 menores.",
        "extra": '🗣️ ECOE: "Ante sospecha clínica de endocarditis: hemocultivos x3 antes de antibiótico + ecocardiograma transtorácico; si dudas, transesofágico."',
        "tags": ["endocarditis", "duke", "diagnostico"],
    },

    # Bloque I — Profilaxis
    {
        "text": "Profilaxis de endocarditis indicada SOLO en alto riesgo: {{c1::válvula protésica o material protésico en reparación valvular}}, {{c2::endocarditis previa}}, {{c3::cardiopatía congénita cianótica no reparada o con defecto residual}}, {{c4::trasplante cardíaco con valvulopatía}}.",
        "extra": "La AHA restringió la profilaxis en 2007: el prolapso mitral, soplos inocentes, valvulopatía reumática sin prótesis, EM/IM sin prótesis YA NO requieren profilaxis rutinaria.",
        "tags": ["endocarditis", "profilaxis"],
    },
    {
        "text": "Procedimientos que requieren profilaxis (en pacientes de alto riesgo): {{c1::dentales con manipulación gingival o periapical, o de mucosa oral perforada}}. Régimen estándar: {{c2::amoxicilina 2 g VO}} 30-60 min antes del procedimiento.",
        "extra": "Alternativas si alergia a penicilina: cefalexina 2 g, clindamicina 600 mg, azitromicina 500 mg. NO se recomienda profilaxis para procedimientos GI/GU rutinarios.",
        "tags": ["endocarditis", "profilaxis"],
    },

    # Bloque J — Maniobras
    {
        "text": "Valsalva (fase de esfuerzo): ↓ retorno venoso → ↓ casi todos los soplos. **MCH y PVM** pueden {{c1::duplicar (&gt;100%)}} su intensidad. Handgrip: ↑ postcarga → ↑ {{c2::IM, IAo, CIV}}.",
        "extra": "Truco ECOE: Valsalva amplifica obstrucción dinámica (MCH) y desplazamiento valvular (PVM); handgrip amplifica regurgitación contra la circulación sistémica.",
        "tags": ["maniobras"],
    },

    # Bloque K — Cuándo pedir eco
    {
        "text": "Indicaciones absolutas de ecocardiograma ante un soplo: {{c1::soplo diastólico (cualquiera)}}, {{c2::soplo sistólico ≥3/6}}, soplo + síntomas (síncope, angina, disnea, falla), soplo nuevo + fiebre, {{c3::antecedente familiar de cardiopatía estructural}}.",
        "extra": '🗣️ ECOE: "Justifico solicitar ecocardiograma porque el soplo es diastólico (siempre patológico) / es ≥3/6 / se acompaña de síntomas / o cambió de aspecto reciente."',
        "tags": ["indicaciones_eco"],
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
