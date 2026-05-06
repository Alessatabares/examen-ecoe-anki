"""
Otoscopia Adulto — Capa 3 (Ejes por patología)
Guías: AAO-HNS (otitis externa 2014; OME 2016) + AAP/AAO-HNS OMA 2013 (reaff.)
Output: output/Otoscopia_Adulto_Capa3.apkg

Estructura cuádruple por patología: fisiopatología → presentación →
hallazgo otoscópico diferenciador → manejo.
"""
import os
import json
import genanki

TEMA_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPO_ROOT = os.path.dirname(TEMA_ROOT)
OUTPUT = os.path.join(TEMA_ROOT, "output", "Otoscopia_Adulto_Capa3.apkg")
IDS_PATH = os.path.join(REPO_ROOT, "ids.json")

DECK_ID = 1456789123
DECK_NAME = "Otoscopia Adulto::Capa 3 - Ejes"

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

BASE_TAGS = ["capa3", "otoscopia_adulto", "aao_hns", "ecoe"]

CARDS = [
    # OMA — 4 cards (eje completo)
    {
        "text": "Fisiopatología OMA: disfunción de {{c1::trompa de Eustaquio}} → presión negativa en oído medio → {{c2::trasudado}} → sobreinfección bacteriana. Patógenos típicos: {{c3::S. pneumoniae, H. influenzae no tipificable, M. catarrhalis}}.",
        "extra": "Frecuentemente precedida por una IVRS viral que altera la función tubárica.",
        "tags": ["oma", "fisiopatologia"],
    },
    {
        "text": "Presentación OMA: {{c1::otalgia aguda}} + {{c2::fiebre}} + {{c3::hipoacusia conductiva}} ± otorrea (si la membrana se perfora, suele aliviar el dolor de golpe).",
        "extra": "En niños prelinguales: irritabilidad, tirar/frotar la oreja, alteración del sueño, anorexia.",
        "tags": ["oma", "presentacion"],
    },
    {
        "text": "Hallazgo otoscópico diferenciador OMA: el dato cardinal es el {{c1::abombamiento de la membrana timpánica}}, no el eritema. Sin abombamiento → no etiquetar como OMA aunque haya tímpano rojo.",
        "extra": '🗣️ ECOE: "Tímpano abombado, eritematoso, sin cono de luz visible — patrón compatible con OMA."',
        "tags": ["oma", "patrones_visuales"],
    },
    {
        "text": "Manejo OMA en adulto: {{c1::amoxicilina 500-875 mg c/8-12 h × 7-10 días}} + analgesia (paracetamol/ibuprofeno). Reevaluar a las {{c2::48-72 horas}}; si no mejora → escalar a {{c3::amoxicilina-clavulánico}} y descartar complicación (mastoiditis).",
        "extra": '🗣️ ECOE: "OMA en adulto: amoxicilina 875 mg c/12 h durante 7 días, analgésico, control en 48-72 h; si no mejora, amoxicilina-clavulánico."',
        "tags": ["oma", "manejo"],
    },

    # OME — 3 cards
    {
        "text": "Fisiopatología OME: {{c1::disfunción crónica de trompa de Eustaquio}} → presión negativa persistente → {{c2::efusión serosa estéril}} en oído medio. NO hay infección bacteriana activa.",
        "extra": "Frecuentemente post-OMA (efusión residual), post-IVRS, o asociada a hipertrofia adenoidea, alergia o RGE.",
        "tags": ["ome", "fisiopatologia"],
    },
    {
        "text": "Presentación OME: {{c1::hipoacusia conductiva}} + sensación de oído tapado o autofonía; {{c2::sin dolor agudo, sin fiebre}}. En niños puede manifestarse como {{c3::retraso del lenguaje}} o falta de atención escolar.",
        "extra": "Por eso 'tirón de oreja sin fiebre, lleva 2 meses' apunta a OME, no a OMA. La cronología y la ausencia de fiebre son los discriminadores clínicos.",
        "tags": ["ome", "presentacion"],
    },
    {
        "text": "Manejo OME: {{c1::observación 3 meses}} (la mayoría se resuelve sola). Si persiste >3 meses con hipoacusia significativa → {{c2::derivación a ORL}} para valorar tubos de ventilación. NO antibióticos, NO antihistamínicos sistemáticos, NO descongestionantes (ineficaces y con efectos adversos).",
        "extra": '🗣️ ECOE: "OME asintomática: observación 3 meses con seguimiento; si persiste y compromete audición, derivación a ORL."',
        "tags": ["ome", "manejo"],
    },

    # Otitis externa — 3 cards
    {
        "text": "Fisiopatología otitis externa: {{c1::rotura de la barrera cutánea del CAE}} (humedad mantenida, manipulación con cotonetes, dermatitis) → infección bacteriana. Patógenos: {{c2::Pseudomonas aeruginosa}} y S. aureus.",
        "extra": "Por eso se llama 'oído del nadador' — la humedad mantenida es el factor más importante.",
        "tags": ["otitis_externa", "fisiopatologia"],
    },
    {
        "text": "Presentación otitis externa: {{c1::otalgia intensa}}, prurito previo, {{c2::otorrea}}, hipoacusia si CAE ocluido por edema/detritus. Signo cardinal: {{c3::dolor exquisito a la tracción del trago/pabellón}}.",
        "extra": '🗣️ ECOE: "Dolor intenso a la tracción del trago — patrón de otitis externa."',
        "tags": ["otitis_externa", "presentacion"],
    },
    {
        "text": "Manejo otitis externa: {{c1::limpieza del CAE}} + {{c2::gotas tópicas con quinolona ± corticoide}} 7-10 días. Mantener oído seco. Antibiótico oral solo si {{c3::celulitis perilesional, fiebre, paciente diabético/inmunodeprimido o sospecha de otitis externa maligna}}.",
        "extra": '🗣️ ECOE: "Limpio el CAE, ciprofloxacino-dexametasona en gotas, 7 días, mantener oído seco, control si no mejora en 48-72 h."',
        "tags": ["otitis_externa", "manejo"],
    },

    # Otitis externa maligna — 1 card (bandera roja, contraste)
    {
        "text": "Bandera roja: otitis externa que no responde + {{c1::diabético o inmunodeprimido}} + dolor desproporcionado + {{c2::tejido de granulación en el suelo del CAE}} → sospechar {{c3::otitis externa maligna (necrotizante)}} por Pseudomonas con osteomielitis de base de cráneo. Manejo: {{c4::TC + ORL urgente + antipseudomona IV prolongado}}.",
        "extra": "Mortalidad significativa si no se trata. Puede progresar a parálisis facial, afectación de base de cráneo y complicación intracraneal.",
        "tags": ["otitis_externa", "banderas_rojas"],
    },

    # Perforación timpánica — 3 cards
    {
        "text": "Fisiopatología perforación: {{c1::traumática}} (objeto introducido, barotrauma, blast acústico) o {{c2::post-OMA}} (la presión del exudado purulento necrosa la membrana).",
        "extra": "Las traumáticas suelen tener bordes netos; las post-OMA bordes irregulares y a veces con exudado residual.",
        "tags": ["perforacion_timpanica", "fisiopatologia"],
    },
    {
        "text": "Presentación perforación: {{c1::otalgia que cede bruscamente}} (al perforar baja la presión del oído medio) + {{c2::otorrea}} + hipoacusia conductiva.",
        "extra": "Si era post-OMA: el alivio del dolor coincidiendo con la aparición de otorrea es la pista clave.",
        "tags": ["perforacion_timpanica", "presentacion"],
    },
    {
        "text": "Manejo perforación: {{c1::mantener oído seco}}, NO meter agua ni gotas con {{c2::aminoglucósidos (ototóxicos)}}. La mayoría cierra espontáneamente en {{c3::4-8 semanas}}; si persiste >3 meses → {{c4::timpanoplastia}} por ORL.",
        "extra": "Si era post-OMA y persiste con otorrea fétida → descartar colesteatoma residual.",
        "tags": ["perforacion_timpanica", "manejo"],
    },

    # Tapón cerumen — 2 cards
    {
        "text": "Fisiopatología tapón de cerumen: {{c1::alteración de la migración natural del cerumen}} hacia el exterior, hipersecreción, o (la causa más frecuente) {{c2::manipulación con cotonete que empuja la cera al CAE óseo}}.",
        "extra": "El cerumen normalmente migra hacia afuera por el movimiento mandibular y el desplazamiento epitelial. Los cotonetes invierten ese flujo.",
        "tags": ["cerumen", "fisiopatologia"],
    },
    {
        "text": "Manejo tapón de cerumen: {{c1::cerumenolíticos}} (peróxido de hidrógeno, docusato, aceite mineral) 3-5 días, después {{c2::irrigación con agua tibia}} o extracción instrumental bajo visión. {{c3::NO irrigar si: perforación, cirugía otológica previa o antecedente de OMA recurrente}}.",
        "extra": "Si hay duda sobre la integridad del tímpano → no irrigar, derivar a ORL para extracción bajo microscopio.",
        "tags": ["cerumen", "manejo"],
    },

    # Colesteatoma — 3 cards
    {
        "text": "Fisiopatología colesteatoma: {{c1::epitelio escamoso queratinizante migrando al oído medio}} (típicamente desde una bolsa de retracción de la pars flácida) → {{c2::produce queratina que se acumula}} → erosión enzimática de huesecillos, mastoides y, eventualmente, base de cráneo.",
        "extra": "No es un tumor verdadero — es epitelio normal en sitio anormal, comportándose como pseudotumor destructivo.",
        "tags": ["colesteatoma", "fisiopatologia"],
    },
    {
        "text": "Presentación colesteatoma: {{c1::otorrea fétida crónica}} (resistente a tratamiento habitual) + {{c2::hipoacusia conductiva progresiva}} + {{c3::masa blanca-perlada en pars flácida (ático)}}; banderas rojas de complicación: {{c4::parálisis facial, vértigo, complicación intracraneal}}.",
        "extra": "La fetidez de la otorrea es muy característica — la otitis externa o la OMA simple no producen ese olor.",
        "tags": ["colesteatoma", "presentacion", "banderas_rojas"],
    },
    {
        "text": "Manejo colesteatoma: {{c1::SIEMPRE quirúrgico}} ({{c2::mastoidectomía + timpanoplastia}}). Los antibióticos solo controlan transitoriamente la sobreinfección de la otorrea pero NO son tratamiento definitivo. {{c3::Derivación a ORL}}.",
        "extra": '🗣️ ECOE: "Patrón compatible con colesteatoma — no es manejo de primer nivel, derivo a ORL para tratamiento quirúrgico."',
        "tags": ["colesteatoma", "manejo"],
    },

    # Disfunción trompa de Eustaquio — 2 cards
    {
        "text": "Fisiopatología disfunción tubárica: la trompa de Eustaquio no se abre adecuadamente al deglutir/bostezar → {{c1::no equilibra la presión del oído medio con la atmósfera}} → presión negativa → {{c2::tímpano retraído}} → con el tiempo trasudado y OME.",
        "extra": "Causas frecuentes: alergia, hipertrofia adenoidea, infección viral reciente, RGE, secuela de paladar hendido.",
        "tags": ["disfuncion_tubarica", "fisiopatologia"],
    },
    {
        "text": "Manejo disfunción tubárica: {{c1::maniobras de Valsalva o Toynbee}}; tratar la causa base ({{c2::antihistamínicos en alérgico, IBP en RGE, adenoidectomía si hipertrofia}}). Descongestionantes: utilidad limitada y solo en agudo.",
        "extra": "Si evoluciona a OME persistente con hipoacusia → tubos de ventilación.",
        "tags": ["disfuncion_tubarica", "manejo"],
    },

    # Cuándo referir / banderas rojas — 2 cards
    {
        "text": "Indicaciones de derivación a ORL: {{c1::parálisis facial}} + otitis activa, {{c2::vértigo + nistagmo + otorrea}}, {{c3::masa blanca en ático (colesteatoma)}}, {{c4::OMA recurrente (≥3 episodios/6 meses o ≥4/12 meses)}}, OME persistente >3 meses con hipoacusia y {{c5::hipoacusia neurosensorial súbita}}.",
        "extra": "Esta lista responde a la pregunta '¿cuándo refieres?' clásica de ECOE — memorízala como bloque.",
        "tags": ["banderas_rojas"],
    },
    {
        "text": "Hipoacusia neurosensorial súbita: pérdida {{c1::≥30 dB en ≥3 frecuencias contiguas en <72 horas}}. Es {{c2::URGENCIA ORL}} — corticoides sistémicos en los primeros 7 días pueden recuperar audición; pasadas >2 semanas el rescate es muy bajo.",
        "extra": '🗣️ ECOE: "Hipoacusia neurosensorial súbita es urgencia — inicio corticoide sistémico y derivación inmediata a ORL."',
        "tags": ["banderas_rojas"],
    },

    # Trampas ECOE — 2 cards
    {
        "text": "Trampa ECOE: {{c1::eritema timpánico aislado sin abombamiento ni fiebre}} ≠ OMA. Puede ser por llanto, fiebre alta sistémica de otra causa o manipulación reciente del CAE. NO antibioticar.",
        "extra": "El abombamiento es el criterio cardinal AAP 2013; el eritema solo no basta para etiquetar OMA.",
        "tags": ["trampas", "oma"],
    },
    {
        "text": "Trampa ECOE: mareo aislado sin nistagmo, sin otorrea y sin signos otológicos NO es problema otoscópico. Pensar {{c1::VPPB (Dix-Hallpike), ortostatismo, neuritis vestibular o causa central}}, no manejarlo desde la otitis.",
        "extra": "Vértigo otológico se acompaña de signos otológicos (otorrea, nistagmo, signo de la fístula). Si no los hay, busca otro origen.",
        "tags": ["trampas"],
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
