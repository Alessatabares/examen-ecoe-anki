"""
Ruidos Cardiacos Adulto — Capa 1 (Flujo Macro)
Guía: AHA/ACC 2020 Valvular Heart Disease
Output: output/Ruidos_Cardiacos_Adulto_Capa1.apkg
"""
import os
import json
import genanki

TEMA_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPO_ROOT = os.path.dirname(TEMA_ROOT)
OUTPUT = os.path.join(TEMA_ROOT, "output", "Ruidos_Cardiacos_Adulto_Capa1.apkg")
MEDIA_DIR = os.path.join(TEMA_ROOT, "media")
IDS_PATH = os.path.join(REPO_ROOT, "ids.json")

DECK_ID = 1813889052
DECK_NAME = "Ruidos Cardiacos Adulto::Capa 1 - Flujo Macro"

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

BASE_TAGS = ["capa1", "ruidos_cardiacos_adulto", "aha", "ecoe"]

MEDIA_FILES = [
    os.path.join(MEDIA_DIR, "civ_holosistolico.wav"),
    os.path.join(MEDIA_DIR, "prolapso_mitral.wav"),
    os.path.join(MEDIA_DIR, "soplo_funcional.wav"),
]

CARDS = [
    # Bloque A — Cronología
    {
        "text": "S1 marca el inicio de la {{c1::sístole}} (cierre de mitral y tricúspide). S2 marca el inicio de la {{c2::diástole}} (cierre de aórtica y pulmonar).",
        "extra": "Anchor cronológico: todo el razonamiento auscultatorio cuelga de aquí. Sin S1/S2 ubicados, no se interpreta nada.",
        "tags": ["cronologia"],
    },
    {
        "text": "Soplo entre S1 y S2 → {{c1::sistólico}}. Soplo después de S2 hasta el siguiente S1 → {{c2::diastólico}}. Soplo que cruza S2 sin interrumpirse → {{c3::continuo}}.",
        "extra": '🗣️ ECOE: "Primero ubico S1 y S2, después determino si el soplo está en sístole, en diástole, o atraviesa S2."',
        "tags": ["cronologia", "bifurcacion"],
    },
    {
        "text": "Regla anchor: si no puedes ubicar el soplo en el ciclo cardíaco, no puedes interpretarlo. {{c1::Cronología}} antes que nombre.",
        "extra": "Trampa ECOE clásica: nombrar un soplo (EA, IM) sin haber demostrado primero su timing.",
        "tags": ["cronologia"],
    },

    # Bloque B — Forma del soplo dice el mecanismo
    {
        "text": "Forma holosistólica (plano, intensidad constante) → gradiente constante toda la sístole → mecanismo: {{c1::regurgitación AV (IM, IT)}} o {{c2::shunt VI→VD}}.",
        "extra": "Si la presión a un lado es siempre mayor que la del otro durante toda la sístole, el flujo es continuo y el soplo es plano.",
        "tags": ["forma_soplo", "mecanismo"],
    },
    {
        "text": "Forma crescendo-decrescendo (romboidal) → flujo turbulento al pasar por orificio estrecho → mecanismo: {{c1::estenosis valvular (EA, EP)}}.",
        "extra": "Sube cuando el ventrículo expulsa con más fuerza y baja cuando la eyección se agota. Por eso es más fuerte en mesosístole.",
        "tags": ["forma_soplo", "mecanismo"],
    },
    {
        "text": "Forma decrescendo en diástole → válvula semilunar que no cierra y deja escapar sangre hacia atrás → mecanismo: {{c1::insuficiencia aórtica o pulmonar}}.",
        "extra": "Gradiente máximo al inicio (justo después de S2) y va cayendo conforme se igualan las presiones.",
        "tags": ["forma_soplo", "mecanismo"],
    },
    {
        "text": "Forma continua en maquinaria en adulto → raro. Anchors posibles: {{c1::PCA persistente}} o {{c2::fístula arteriovenosa}}.",
        "extra": "El soplo continuo de adulto siempre es bandera de derivación cardiológica. No existe 'soplo continuo benigno del adulto' fuera del zumbido venoso cervical.",
        "tags": ["forma_soplo"],
    },

    # Bloque C — Focos clásicos
    {
        "text": "Foco aórtico → {{c1::2º espacio intercostal derecho}}, paraesternal. Foco pulmonar → {{c2::2º espacio intercostal izquierdo}}, paraesternal.",
        "extra": "Los focos altos son las válvulas semilunares (eyección hacia las grandes arterias).",
        "tags": ["focos"],
    },
    {
        "text": "Foco tricúspide → {{c1::borde esternal inferior izquierdo}} (4º-5º EIC). Foco mitral → {{c2::ápex, 5º EIC línea medio-clavicular}}.",
        "extra": "Los focos bajos son las válvulas AV. La regla útil: en el foco se oye mejor la válvula que produce ese sonido.",
        "tags": ["focos"],
    },

    # Bloque D — Mecanismos
    {
        "text": "Cinco mecanismos posibles de soplo: {{c1::estenosis}}, {{c2::insuficiencia/regurgitación}}, {{c3::shunt}}, {{c4::hiperflujo o alto gasto}}, {{c5::turbulencia funcional}}.",
        "extra": "Antes de pensar en una enfermedad, pregúntate cuál mecanismo explica el sonido. Filtra el 90% del DDx.",
        "tags": ["mecanismo"],
    },
    {
        "text": "En adulto, soplo nuevo o cambiante → {{c1::casi siempre patológico}}. 'Soplo inocente del adulto' solo existe en contextos de alto gasto: {{c2::anemia, embarazo, hipertiroidismo, fiebre, atleta entrenado}}.",
        "extra": "A diferencia del niño, en adulto la sospecha basal de patología es alta. Cualquier soplo nuevo merece ecocardiograma salvo justificación clínica clara.",
        "tags": ["mecanismo"],
    },

    # Bloque E — Anchors adulto
    {
        "text": "Estenosis aórtica — anchor: soplo {{c1::crescendo-decrescendo}} en foco aórtico, irradia a {{c2::carótidas}}, {{c3::pulso parvus et tardus}}, S2 disminuido o ausente en severas.",
        "extra": "Tríada clínica de EA severa: angina, síncope, disnea. Cualquiera de los tres con soplo aórtico → urgencia, riesgo de muerte súbita.",
        "tags": ["ea", "anchor"],
    },
    {
        "text": "Insuficiencia mitral — anchor: soplo {{c1::holosistólico}} en {{c2::ápex}}, irradia a {{c3::axila}}.",
        "extra": "Mecanismo: el VI eyecta contra una válvula incompetente → la sangre regresa a la AI durante toda la sístole → soplo plano. En IM crónica severa aparece S3 por sobrecarga de volumen.",
        "tags": ["im", "anchor"],
    },
    {
        "text": "Insuficiencia aórtica — anchor: soplo {{c1::decrescendo diastólico}} en borde paraesternal izquierdo (foco de Erb), {{c2::pulso saltón (Corrigan)}}, presión de pulso amplia.",
        "extra": "Signos periféricos clásicos: Musset (cabeza pulsátil), Quincke (pulso ungueal), Traube (sonido de pistola femoral). Todos derivan de la presión de pulso aumentada.",
        "tags": ["iao", "anchor"],
    },
    {
        "text": "Estenosis mitral — anchor: {{c1::chasquido de apertura}} + {{c2::retumbo diastólico}} en ápex, mejor con paciente en {{c3::decúbito lateral izquierdo}} con campana del estetoscopio.",
        "extra": "Etiología #1: fiebre reumática. Cuanto más cerca esté el chasquido de S2, más severa la estenosis (mayor presión en AI). Refuerzo presistólico en ritmo sinusal.",
        "tags": ["em", "anchor"],
    },
    {
        "text": "Prolapso mitral — anchor: {{c1::click mesosistólico}} + {{c2::soplo telesistólico}} en ápex, frecuente en joven asintomático.",
        "extra": "Con Valsalva el click se adelanta y el soplo se alarga (el ventrículo más vacío permite que el velo prolapse antes). Es un truco ECOE de diferenciación dinámica.",
        "tags": ["pvm", "anchor"],
    },
    {
        "text": "Miocardiopatía hipertrófica (MCH) — anchor: soplo {{c1::sistólico eyectivo}} en borde esternal izquierdo, {{c2::aumenta con Valsalva}} (obstrucción dinámica); sospecha alta si antecedente familiar de {{c3::muerte súbita}}.",
        "extra": "Causa #1 de muerte súbita cardiaca en deportistas jóvenes. A diferencia de EA, el soplo NO irradia a carótidas y los pulsos son normales o bisferiens.",
        "tags": ["mch", "anchor", "banderas_rojas"],
    },
    {
        "text": "Insuficiencia tricuspídea por endocarditis (uso de drogas IV) — anchor: soplo {{c1::holosistólico}} en {{c2::borde esternal inferior izquierdo}}, {{c3::aumenta con la inspiración (Rivero-Carvallo positivo)}}.",
        "extra": "Microorganismo clásico: Staphylococcus aureus. Buscar signos de embolia séptica pulmonar (nódulos cavitados en RX). Hemocultivos x3 antes de antibiótico empírico.",
        "tags": ["it", "endocarditis", "anchor"],
    },

    # Bloque F — Maniobras dinámicas
    {
        "text": "Valsalva y posición de pie → {{c1::disminuyen}} el retorno venoso → casi todos los soplos {{c2::disminuyen}}, excepto los de {{c3::MCH y prolapso mitral}}, que aumentan.",
        "extra": "MCH y prolapso aumentan porque el ventrículo se vacía más → la obstrucción dinámica empeora (MCH) o el velo prolapsa antes (PVM).",
        "tags": ["maniobras"],
    },
    {
        "text": "Sentadilla y handgrip → {{c1::aumentan}} el retorno venoso y/o la postcarga → {{c2::aumentan}} los soplos de regurgitación izquierda (IM, IAo).",
        "extra": '🗣️ ECOE: "Pediré handgrip al paciente para amplificar el soplo de insuficiencia aórtica — el aumento confirma la hipótesis."',
        "tags": ["maniobras"],
    },
    {
        "text": "Signo de Rivero-Carvallo: los soplos del lado derecho (IT, EP) {{c1::aumentan con la inspiración}} porque entra más sangre al ventrículo derecho.",
        "extra": "Truco ECOE: si un soplo en BEI bajo cambia con la respiración, es del lado derecho. Si no cambia, es izquierdo aunque suene en el mismo punto.",
        "tags": ["maniobras", "rivero_carvallo"],
    },

    # Bloque G — Bifurcaciones rectoras
    {
        "text": "Bifurcación 1 — ¿cronología del soplo? Sistólico = pensar EA, IM, MCH, IT. Diastólico = {{c1::siempre patológico}} (IAo, EM). Continuo = raro, derivar.",
        "extra": "Anchor mental para adulto: 'soplo diastólico = siempre patológico, ecocardiograma'.",
        "tags": ["bifurcacion"],
    },
    {
        "text": "Bifurcación 2 — sistólico aórtico que irradia a {{c1::carótidas}} con pulso pequeño y lento → {{c2::EA}}. Sistólico en ápex que irradia a {{c3::axila}} → {{c4::IM}}.",
        "extra": "La irradiación es la huella dactilar del soplo sistólico en adulto: carótidas = EA; axila = IM; espalda = EP o coartación.",
        "tags": ["bifurcacion", "ea", "im"],
    },
    {
        "text": "Bifurcación 3 — soplo nuevo + fiebre persistente + uso de drogas IV → sospechar {{c1::endocarditis tricuspídea}} → {{c2::hemocultivos x3 + ecocardiograma}} urgente.",
        "extra": '🗣️ ECOE: "Soplo nuevo en paciente febril es endocarditis hasta que se demuestre lo contrario — hemocultivos antes de antibiótico."',
        "tags": ["bifurcacion", "endocarditis"],
    },

    # Bloque H — Banderas rojas adulto
    {
        "text": "Banderas rojas en adulto: {{c1::síncope, angina o disnea}} con soplo aórtico eyectivo → EA severa, urgencia quirúrgica. Soplo nuevo + {{c2::fiebre persistente}} → endocarditis. Soplo + {{c3::hemoptisis}} → EM con congestión pulmonar.",
        "extra": "Estas tres asociaciones (EA + síntomas, soplo + fiebre, soplo + hemoptisis) son las que más se preguntan en ECOE adulto.",
        "tags": ["banderas_rojas"],
    },

    # Bloque I — Audio
    {
        "text": '[sound:civ_holosistolico.wav]<br>Patrón auscultatorio: {{c1::holosistólico}}, intensidad constante toda la sístole. En adulto, si se oye máximo en {{c2::ápex con irradiación a axila}} → diagnóstico más probable: {{c3::insuficiencia mitral}}.',
        "extra": "El mismo patrón holosistólico en BEI bajo que aumenta con inspiración orienta a IT (endocarditis). El patrón temporal es idéntico — la localización y el comportamiento con la respiración diferencian.",
        "tags": ["audio", "im"],
    },
    {
        "text": '[sound:prolapso_mitral.wav]<br>Secuencia auscultatoria: {{c1::click mesosistólico}} seguido de {{c2::soplo telesistólico}} en ápex → diagnóstico: {{c3::prolapso mitral}}.',
        "extra": '🗣️ ECOE: "Con Valsalva el click se adelanta y el soplo se alarga — confirma prolapso mitral por mecanismo dinámico."',
        "tags": ["audio", "pvm"],
    },
    {
        "text": '[sound:soplo_funcional.wav]<br>Soplo sistólico suave en adulto joven sin cardiopatía estructural. Contextos en los que sería esperable: {{c1::embarazo, anemia, hipertiroidismo, fiebre, atleta entrenado}}.',
        "extra": "En adulto el soplo funcional es de exclusión: requiere ecocardiograma normal y un contexto de hiperdinámia documentado. Sin contexto claro → estudiar.",
        "tags": ["audio", "funcional"],
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
