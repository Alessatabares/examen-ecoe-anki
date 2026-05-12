"""
Ruidos Cardiacos Pediátrico — Capa 1 (Flujo Macro)
Guía: AHA scientific statements (cardiopatías congénitas y soplos pediátricos)
Output: output/Ruidos_Cardiacos_Pediatrico_Capa1.apkg
"""
import os
import json
import genanki

TEMA_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPO_ROOT = os.path.dirname(TEMA_ROOT)
OUTPUT = os.path.join(TEMA_ROOT, "output", "Ruidos_Cardiacos_Pediatrico_Capa1.apkg")
MEDIA_DIR = os.path.join(TEMA_ROOT, "media")
IDS_PATH = os.path.join(REPO_ROOT, "ids.json")

DECK_ID = 1404571352
DECK_NAME = "Ruidos Cardiacos Pediátrico::Capa 1 - Flujo Macro"

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

BASE_TAGS = ["capa1", "ruidos_cardiacos_pediatrico", "aha", "ecoe"]

MEDIA_FILES = [
    os.path.join(MEDIA_DIR, "soplo_inocente_still.ogg"),
    os.path.join(MEDIA_DIR, "civ_holosistolico.wav"),
    os.path.join(MEDIA_DIR, "soplo_funcional.wav"),
]

CARDS = [
    # Bloque A — Cronología (bifurcación cardinal)
    {
        "text": "S1 marca el inicio de la {{c1::sístole}} (cierre de mitral y tricúspide). S2 marca el inicio de la {{c2::diástole}} (cierre de aórtica y pulmonar).",
        "extra": "Anchor cronológico: si no tienes ubicados S1 y S2, no puedes ubicar nada más. Todo el razonamiento auscultatorio cuelga de aquí.",
        "tags": ["cronologia"],
    },
    {
        "text": "Soplo entre S1 y S2 → {{c1::sistólico}}. Soplo después de S2 hasta el siguiente S1 → {{c2::diastólico}}. Soplo que cruza S2 sin interrumpirse → {{c3::continuo}}.",
        "extra": '🗣️ ECOE: "Primero ubico S1 y S2, después determino si el soplo está en sístole, en diástole o atraviesa S2 — esa es la primera decisión."',
        "tags": ["cronologia", "bifurcacion"],
    },
    {
        "text": "Regla anchor: si no puedes ubicar el soplo en el ciclo cardíaco, no puedes interpretarlo. {{c1::Cronología}} antes que nombre.",
        "extra": "Trampa ECOE clásica: nombrar un soplo (CIV, IM) sin haber demostrado primero su timing. El sinodal te corta.",
        "tags": ["cronologia"],
    },

    # Bloque B — Forma del soplo dice el mecanismo
    {
        "text": "Forma holosistólica (plano, intensidad constante) → gradiente constante toda la sístole → mecanismo: {{c1::regurgitación valvular AV}} o {{c2::shunt VI→VD (CIV)}}.",
        "extra": "Anchor mecánico: si la presión a un lado es siempre mayor que la del otro durante toda la sístole, el flujo es continuo y el soplo es plano.",
        "tags": ["forma_soplo", "mecanismo"],
    },
    {
        "text": "Forma crescendo-decrescendo (romboidal) → flujo turbulento al pasar por un orificio estrecho → mecanismo: {{c1::estenosis valvular}}.",
        "extra": "Sube cuando el ventrículo expulsa con más fuerza y baja cuando la eyección se agota. Por eso es más fuerte en mesosístole.",
        "tags": ["forma_soplo", "mecanismo"],
    },
    {
        "text": "Forma decrescendo en diástole → válvula que no cierra y deja escapar sangre hacia atrás → mecanismo: {{c1::insuficiencia aórtica o pulmonar}}.",
        "extra": "El gradiente es máximo al inicio (justo cuando cierra S2) y va cayendo conforme se igualan las presiones — por eso decrescendo.",
        "tags": ["forma_soplo", "mecanismo"],
    },
    {
        "text": "Forma continua (en maquinaria) que cruza S2 sin interrupción → comunicación entre dos cámaras con gradiente en todo el ciclo. Anchor pediátrico: {{c1::PCA (persistencia del conducto arterioso)}}.",
        "extra": "Aorta tiene mayor presión que arteria pulmonar tanto en sístole como en diástole → el flujo nunca para → soplo continuo.",
        "tags": ["forma_soplo", "pca"],
    },

    # Bloque C — Focos clásicos
    {
        "text": "Foco aórtico → {{c1::2º espacio intercostal derecho}}, paraesternal. Foco pulmonar → {{c2::2º espacio intercostal izquierdo}}, paraesternal.",
        "extra": "Los focos altos son las válvulas semilunares (eyección hacia las grandes arterias).",
        "tags": ["focos"],
    },
    {
        "text": "Foco tricúspide → {{c1::borde esternal inferior izquierdo}} (4º-5º EIC). Foco mitral → {{c2::ápex, 5º EIC línea medio-clavicular}}.",
        "extra": "Los focos bajos son las válvulas AV. La regla útil: en el foco se oye mejor la válvula que cierra ese sonido, no necesariamente donde está anatómicamente.",
        "tags": ["focos"],
    },

    # Bloque D — Mecanismo antes que nombre
    {
        "text": "Cinco mecanismos posibles de soplo: {{c1::estenosis}}, {{c2::insuficiencia/regurgitación}}, {{c3::shunt}}, {{c4::hiperflujo o alto gasto}}, {{c5::turbulencia funcional (soplo inocente)}}.",
        "extra": "Antes de pensar en una enfermedad, pregúntate cuál de estos 5 mecanismos explica el sonido. Eso filtra el 90% del diagnóstico diferencial.",
        "tags": ["mecanismo"],
    },
    {
        "text": "En pediatría, la mayoría de soplos son {{c1::inocentes (funcionales)}} — turbulencia por flujo en un corazón estructuralmente sano. No requieren tratamiento ni ecocardiograma si cumplen criterios de inocencia.",
        "extra": "Hasta 50-80% de niños presentan soplo inocente en algún momento. Etiquetar todo como patológico genera ansiedad familiar y estudios innecesarios.",
        "tags": ["mecanismo", "inocente"],
    },

    # Bloque E — Anchors pediátricos clave
    {
        "text": "Soplo inocente (Still) — anchor: soplo {{c1::sistólico eyectivo, suave (≤grado 2/6), musical o vibratorio}}, en {{c2::borde esternal izquierdo bajo}}, cambia con la postura, niño asintomático.",
        "extra": "Si lo escuchas como un 'zumbido musical' o tono vibratorio, piensa Still. Característica clave: la intensidad cambia entre acostado y sentado.",
        "tags": ["inocente", "anchor"],
    },
    {
        "text": "CIV (comunicación interventricular) — anchor: soplo {{c1::holosistólico}} en {{c2::borde esternal inferior izquierdo}}, frecuente {{c3::frémito}} palpable.",
        "extra": "Mecanismo: la presión del VI supera la del VD durante toda la sístole → flujo constante VI→VD → soplo plano. Anchor mental: el soplo es 'plano' porque el gradiente es constante.",
        "tags": ["civ", "anchor"],
    },
    {
        "text": "PCA (persistencia del conducto arterioso) — anchor: soplo {{c1::continuo en maquinaria}} en {{c2::2º EIC izquierdo / región infraclavicular}}, con {{c3::pulsos saltones (amplios)}}.",
        "extra": "Los pulsos saltones se explican por el escape diastólico hacia la pulmonar — presión diastólica baja, presión sistólica conservada = presión de pulso amplia.",
        "tags": ["pca", "anchor"],
    },
    {
        "text": "Estenosis pulmonar — anchor: soplo {{c1::crescendo-decrescendo}} en {{c2::foco pulmonar}}, irradia a {{c3::espalda}}, precedido por {{c4::click eyectivo}}.",
        "extra": "El click eyectivo aparece justo antes del soplo, cuando la válvula estenótica se abre bruscamente.",
        "tags": ["estenosis_pulmonar", "anchor"],
    },
    {
        "text": "Fiebre reumática — anchor: soplo nuevo de {{c1::insuficiencia mitral}} (holosistólico en ápex, irradia a axila) en niño con antecedente de {{c2::faringitis estreptocócica}} 2-3 semanas previas.",
        "extra": "La fiebre reumática es la causa #1 de cardiopatía valvular adquirida en niños en países con acceso limitado a antibióticos. Profilaxis post-episodio con penicilina G benzatínica.",
        "tags": ["fiebre_reumatica", "im", "anchor"],
    },
    {
        "text": "Miocardiopatía hipertrófica (MCH) pediátrica — anchor: soplo {{c1::sistólico eyectivo}} en borde esternal izquierdo, {{c2::aumenta con Valsalva}}, antecedente familiar de {{c3::muerte súbita}}.",
        "extra": "Causa #1 de muerte súbita cardiaca en deportistas jóvenes. La pista anamnésica del familiar muerto súbitamente vale más que cualquier auscultación.",
        "tags": ["mch", "anchor", "banderas_rojas"],
    },

    # Bloque F — Maniobras dinámicas
    {
        "text": "Valsalva y posición de pie → {{c1::disminuyen}} el retorno venoso → casi todos los soplos {{c2::disminuyen}}, excepto los de {{c3::MCH y prolapso mitral}}, que aumentan.",
        "extra": "MCH y prolapso aumentan porque el ventrículo se vacía más → la obstrucción dinámica empeora (MCH) o el velo prolapsa antes (PVM).",
        "tags": ["maniobras"],
    },
    {
        "text": "Sentadilla y handgrip → {{c1::aumentan}} el retorno venoso y/o la postcarga → {{c2::aumentan}} los soplos de regurgitación izquierda (IM, IAo).",
        "extra": '🗣️ ECOE: "Pediré al paciente que haga sentadilla para amplificar el soplo de insuficiencia mitral — el aumento confirma la hipótesis."',
        "tags": ["maniobras"],
    },
    {
        "text": "Signo de Rivero-Carvallo: los soplos del lado derecho (tricúspide, pulmonar) {{c1::aumentan con la inspiración}} porque entra más sangre al ventrículo derecho.",
        "extra": "Truco ECOE: si un soplo en BEI bajo cambia con la respiración, es del lado derecho. Si no cambia, es del izquierdo aunque suene en el mismo punto.",
        "tags": ["maniobras", "rivero_carvallo"],
    },

    # Bloque G — Bifurcaciones rectoras
    {
        "text": "Bifurcación 1 — ¿el soplo está entre S1 y S2? Sí → {{c1::sistólico}} (pensar estenosis aórtica/pulmonar, IM/IT, CIV, o inocente). No → diastólico o continuo, {{c2::siempre patológicos}}.",
        "extra": "Anchor mental: 'soplo diastólico = siempre patológico' es una de las reglas más útiles de la auscultación pediátrica.",
        "tags": ["bifurcacion"],
    },
    {
        "text": "Bifurcación 2 — sistólico en niño asintomático, suave, que cambia con la postura → {{c1::inocente}}. Sistólico que no cambia con la postura, ≥grado 3/6, con frémito o irradiación → {{c2::patológico, ecocardiograma}}.",
        "extra": "Los criterios de inocencia son acumulativos. Basta con que falle uno (intensidad ≥3, frémito, diastólico, irradiación amplia, cianosis, falla para crecer) para perder la etiqueta de inocente.",
        "tags": ["bifurcacion", "inocente"],
    },
    {
        "text": "Bifurcación 3 — holosistólico en niño: ¿dónde se oye más fuerte? Borde esternal inferior izquierdo → {{c1::CIV}}. Ápex con irradiación a axila → {{c2::insuficiencia mitral}}.",
        "extra": '🗣️ ECOE: "Mismo patrón temporal (holosistólico), distinto foco máximo: la localización es lo que diferencia CIV de IM en el niño."',
        "tags": ["bifurcacion", "civ", "im"],
    },

    # Bloque H — Banderas rojas
    {
        "text": "Banderas rojas que descartan soplo inocente y obligan a ecocardiograma: soplo {{c1::diastólico}}, intensidad {{c2::≥grado 3/6}}, {{c3::frémito}}, {{c4::cianosis}}, fatiga al comer o falla para crecer, antecedente familiar de {{c5::muerte súbita}}.",
        "extra": "Mnemonia útil: 'D3FCF' (Diastólico, ≥3/6, Frémito, Cianosis, Familiar muerto). Cualquiera de estos saca al niño de la vía de soplo inocente.",
        "tags": ["banderas_rojas"],
    },

    # Bloque I — Audio (identificación auditiva tipo ECOE)
    {
        "text": '[sound:soplo_inocente_still.ogg]<br>Patrón: {{c1::sistólico eyectivo, suave, musical/vibratorio}}. Niño asintomático, ≤grado 2/6, cambia con la postura → diagnóstico: {{c2::soplo inocente (Still)}}.',
        "extra": '🗣️ ECOE: "Soplo de baja intensidad, sin frémito, que cambia con la postura y sin otros hallazgos — compatible con soplo inocente, no requiere ecocardiograma."',
        "tags": ["audio", "inocente"],
    },
    {
        "text": '[sound:civ_holosistolico.wav]<br>Patrón: {{c1::holosistólico, plano}}, intensidad constante toda la sístole. Localización clásica en niño: {{c2::borde esternal inferior izquierdo}}, frecuente frémito → diagnóstico más probable: {{c3::CIV}}.',
        "extra": "El mismo patrón holosistólico en ápex con irradiación a axila apunta a insuficiencia mitral. El patrón acústico es idéntico — la diferencia la hace la localización.",
        "tags": ["audio", "civ"],
    },
    {
        "text": '[sound:soplo_funcional.wav]<br>Soplo sistólico suave en adolescente sin síntomas. ¿Qué confirma soplo funcional? Que {{c1::cambia o desaparece con cambios posturales}} y no se acompaña de {{c2::frémito, irradiación, cianosis ni fatiga}}.',
        "extra": "Tip ECOE: si el soplo desaparece al sentar al paciente o cambia claramente entre decúbito y sedestación, es muy probablemente funcional.",
        "tags": ["audio", "inocente"],
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
genanki.Package(deck, media_files=MEDIA_FILES).write_to_file(OUTPUT)

print(f"Notas: {len(CARDS)}")
print(f"DECK_ID: {DECK_ID}")
print(f"Media: {len(MEDIA_FILES)} archivos")
print(f"Output: {OUTPUT}")
