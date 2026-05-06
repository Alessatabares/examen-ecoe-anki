"""
Otoscopia Adulto — Capa 1 (Flujo Macro)
Guías: AAO-HNS (otitis externa 2014; OME 2016) + AAP/AAO-HNS OMA 2013 (reaff.)
Output: output/Otoscopia_Adulto_Capa1.apkg
"""
import os
import json
import genanki

TEMA_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPO_ROOT = os.path.dirname(TEMA_ROOT)
OUTPUT = os.path.join(TEMA_ROOT, "output", "Otoscopia_Adulto_Capa1.apkg")
IDS_PATH = os.path.join(REPO_ROOT, "ids.json")

DECK_ID = 1567432891
DECK_NAME = "Otoscopia Adulto::Capa 1 - Flujo Macro"

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

BASE_TAGS = ["capa1", "otoscopia_adulto", "aao_hns", "ecoe"]

CARDS = [
    # Bloque A — ¿Qué exploro?
    {
        "text": "La otoscopia evalúa en orden: primero {{c1::el conducto auditivo externo (CAE)}} y después {{c2::la membrana timpánica}}.",
        "extra": "Si encuentras patología en el CAE (cerumen, edema, detritus) puede impedir ver la membrana — anótalo y descríbelo, no fuerces.",
        "tags": ["anatomia"],
    },
    {
        "text": "Antes de introducir el otoscopio, debo inspeccionar {{c1::pabellón auricular y región mastoidea}} y palpar {{c2::trago y mastoides}} buscando dolor o signos inflamatorios.",
        "extra": '🗣️ ECOE: "Inspecciono pabellón y región mastoidea, palpo trago y mastoides — sin dolor, sin signos inflamatorios."',
        "tags": ["tecnica"],
    },

    # Bloque B — Técnica esqueleto
    {
        "text": "El otoscopio se sostiene como {{c1::un lápiz}}, apoyando el {{c2::meñique sobre la mejilla del paciente}} para amortiguar movimientos bruscos y no lesionar el CAE.",
        "extra": '🗣️ ECOE: "Sostengo el otoscopio como un lápiz y apoyo el meñique en la mejilla del paciente."',
        "tags": ["tecnica"],
    },
    {
        "text": "Para rectificar el CAE en el adulto, se tracciona el pabellón auricular {{c1::hacia arriba y hacia atrás}}.",
        "extra": "En niños <3 años se hace al revés (abajo y atrás) porque el CAE infantil es más horizontal y corto. Capa 1: solo el concepto del adulto; los matices pediátricos van en Capa 2.",
        "tags": ["tecnica"],
    },
    {
        "text": "Regla ECOE: siempre se explora primero {{c1::el oído sano}} y después el sintomático, para no contaminar el espéculo ni perder la referencia normal.",
        "extra": '🗣️ ECOE: "Comienzo por el oído asintomático para usarlo como referencia."',
        "tags": ["tecnica"],
    },

    # Bloque C — Tímpano normal anchor
    {
        "text": "Tímpano normal: color {{c1::gris perlado}}, aspecto {{c2::translúcido}}, con {{c3::cono de luz en el cuadrante anteroinferior}} y {{c4::umbo y mango del martillo visibles}} en el centro.",
        "extra": "Anchor visual obligatorio. Cualquier desviación (color, transparencia, posición del cono de luz, abombamiento o retracción) orienta a patología.",
        "tags": ["timpano_normal", "patrones_visuales"],
    },

    # Bloque D — 7 patologías, patrón en una frase
    {
        "text": "OMA — patrón otoscópico anchor: tímpano {{c1::abombado}}, {{c2::eritematoso}}, {{c3::con pérdida del cono de luz}}; clínica: {{c4::otalgia + fiebre}}.",
        "extra": "Anchor de OMA. Recuerda: el dato más específico es el ABOMBAMIENTO, no el eritema (un tímpano puede estar rojo solo por llanto o fiebre alta sin OMA).",
        "tags": ["oma", "patrones_visuales"],
    },
    {
        "text": "OME — patrón otoscópico contrast: tímpano {{c1::retraído o en posición neutra}}, {{c2::opaco}}, con {{c3::nivel hidroaéreo o burbujas detrás de la membrana}}, {{c4::sin eritema y sin fiebre}}.",
        "extra": "OME = otitis media con efusión = serosa. Contraste clave con OMA: SIN abombamiento, SIN eritema, SIN fiebre, SIN dolor agudo. Hipoacusia conductiva como síntoma principal.",
        "tags": ["ome", "patrones_visuales"],
    },
    {
        "text": "Otitis externa — patrón anchor: CAE {{c1::eritematoso, edematoso, con detritus o exudado}}; tímpano normal o no visible. Síntoma diferenciador: {{c2::dolor intenso a la tracción del trago o pabellón}}.",
        "extra": '🗣️ ECOE: "Dolor exquisito a la tracción del pabellón y a la presión del trago — orienta a otitis externa."',
        "tags": ["otitis_externa", "patrones_visuales"],
    },
    {
        "text": "Perforación timpánica: {{c1::solución de continuidad en la membrana}}; bordes {{c2::netos y regulares}} si es traumática, {{c3::irregulares}} si es post-OMA.",
        "extra": "Capa 2 verá la localización (central vs marginal) y su importancia pronóstica para colesteatoma.",
        "tags": ["perforacion_timpanica", "patrones_visuales"],
    },
    {
        "text": "Tapón de cerumen: masa {{c1::marrón, amarillenta o negruzca}} que {{c2::ocupa el CAE e impide visualizar la membrana timpánica}}.",
        "extra": "No es 'patología' en sí, pero es la causa #1 de otoscopia no concluyente. Antes de etiquetar como 'tímpano normal' asegúrate de que lo estás viendo.",
        "tags": ["cerumen", "patrones_visuales"],
    },
    {
        "text": "Colesteatoma — patrón anchor: masa {{c1::blanca, perlada, escamosa}} situada típicamente en {{c2::la pars flácida (ático, cuadrante superior)}}, asociada a {{c3::otorrea fétida crónica}} y {{c4::hipoacusia conductiva progresiva}}.",
        "extra": "Bandera roja. Es destructivo: erosiona huesecillos, mastoides, puede dar parálisis facial o complicación intracraneal. Siempre → ORL.",
        "tags": ["colesteatoma", "patrones_visuales", "banderas_rojas"],
    },
    {
        "text": "Miringitis bullosa (variante viral de OMA): {{c1::vesículas o ampollas hemorrágicas sobre la membrana timpánica}}, dolor intenso desproporcionado.",
        "extra": "Frecuentemente asociada a infección por Mycoplasma o virus. Manejo: analgesia ± antibiótico si hay datos de OMA bacteriana.",
        "tags": ["oma", "patrones_visuales"],
    },

    # Bloque E — Bifurcación rectora
    {
        "text": "Bifurcación 1 — ¿hay dolor a la tracción del trago o pabellón? Sí → {{c1::otitis externa}}. No → {{c2::otitis media o tímpano normal}}.",
        "extra": '🗣️ ECOE: "Pruebo el signo del trago — si es positivo, oriento a otitis externa antes de mirar el tímpano."',
        "tags": ["bifurcacion"],
    },
    {
        "text": "Bifurcación 2 (si no hay dolor con tracción) — ¿tímpano abombado, eritematoso y con fiebre? → {{c1::OMA}}. ¿Tímpano plano o retraído, con nivel hidroaéreo y sin fiebre? → {{c2::OME}}.",
        "extra": "El abombamiento es el signo cardinal de OMA según AAP 2013. Sin abombamiento, NO etiquetar como OMA aunque haya eritema.",
        "tags": ["bifurcacion", "oma", "ome"],
    },
    {
        "text": "Bifurcación 3 — paciente con hipoacusia y tímpano de aspecto normal → sospechar {{c1::hipoacusia neurosensorial}} y solicitar {{c2::audiometría}} (no es problema otoscópico).",
        "extra": "El tímpano normal no descarta hipoacusia. La pista es el patrón audiométrico, no la otoscopia.",
        "tags": ["bifurcacion", "audiometria"],
    },
    {
        "text": "Bifurcación 4 — otorrea fétida crónica + masa blanca-perlada en pars flácida → {{c1::colesteatoma}} → {{c2::derivación a ORL}} (no manejar en primer nivel).",
        "extra": '🗣️ ECOE: "Patrón compatible con colesteatoma — derivo a ORL para evaluación quirúrgica."',
        "tags": ["bifurcacion", "colesteatoma", "banderas_rojas"],
    },

    # Bloque F — Banderas rojas → ORL
    {
        "text": "Bandera roja: parálisis facial periférica + otitis activa → {{c1::derivación urgente a ORL}} (sospecha de mastoiditis aguda o colesteatoma complicado).",
        "extra": '🗣️ ECOE: "La parálisis facial cambia la urgencia — derivación inmediata a ORL."',
        "tags": ["banderas_rojas"],
    },
    {
        "text": "Bandera roja: vértigo + nistagmo + otorrea → sospechar {{c1::fístula laberíntica}} (erosión del laberinto óseo, típicamente por colesteatoma) → ORL urgente.",
        "extra": "Signo de fístula positivo: vértigo y nistagmo provocados al presionar el trago.",
        "tags": ["banderas_rojas"],
    },
    {
        "text": "Bandera roja: cefalea persistente + fiebre tras OMA → sospechar {{c1::mastoiditis aguda}} o {{c2::complicación intracraneal (absceso, meningitis, trombosis del seno lateral)}}.",
        "extra": "Datos clínicos añadidos: dolor y eritema retroauriculares, pabellón desplazado hacia adelante, abombamiento del surco retroauricular.",
        "tags": ["banderas_rojas", "oma"],
    },

    # Bloque G — Trampas ECOE
    {
        "text": "Trampa ECOE clásica: NO confundir OME (sin fiebre, sin dolor agudo, nivel hidroaéreo) con OMA — el antibiótico oral está indicado en {{c1::OMA}}; en OME el manejo inicial es {{c2::observación 3 meses}} y reevaluación auditiva.",
        "extra": "Dar antibiótico a una OME no la resuelve y selecciona resistencias. Es una trampa frecuente en estaciones ECOE.",
        "tags": ["trampas", "oma", "ome"],
    },
    {
        "text": "Trampa ECOE clásica: NO dar antibiótico oral en otitis externa no complicada — el tratamiento estándar es {{c1::gotas tópicas con antibiótico (quinolona) ± corticoide}}, durante 7-10 días.",
        "extra": "Antibiótico oral solo si hay celulitis perilesional, otitis externa maligna (diabético/inmunodeprimido) o paciente febril/séptico.",
        "tags": ["trampas", "otitis_externa"],
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
