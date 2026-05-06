"""
Otoscopia Adulto — Capa 2 (Componentes)
Guías: AAO-HNS (otitis externa 2014; OME 2016) + AAP/AAO-HNS OMA 2013 (reaff.)
Output: output/Otoscopia_Adulto_Capa2.apkg
"""
import os
import json
import genanki

TEMA_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPO_ROOT = os.path.dirname(TEMA_ROOT)
OUTPUT = os.path.join(TEMA_ROOT, "output", "Otoscopia_Adulto_Capa2.apkg")
IDS_PATH = os.path.join(REPO_ROOT, "ids.json")

DECK_ID = 1729384650
DECK_NAME = "Otoscopia Adulto::Capa 2 - Componentes"

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

BASE_TAGS = ["capa2", "otoscopia_adulto", "aao_hns", "ecoe"]

CARDS = [
    # Bloque A — Anatomía timpánica detallada
    {
        "text": "La membrana timpánica se divide en {{c1::pars tensa}} (la mayor parte, fibrosa y resistente) y {{c2::pars flácida (membrana de Shrapnell)}} situada en {{c3::el ático (cuadrante superior, sobre la apófisis corta del martillo)}}; la pars flácida es el sitio típico de inicio del {{c4::colesteatoma adquirido}}.",
        "extra": "La pars flácida tiene menos capa fibrosa → se retrae más fácil → forma la bolsa epitelial inicial del colesteatoma. Por eso siempre hay que mirarla explícitamente, no solo el centro del tímpano.",
        "tags": ["anatomia"],
    },
    {
        "text": "Para describir hallazgos otoscópicos, la membrana se divide en {{c1::4 cuadrantes}} usando dos referencias: una vertical (el {{c2::mango del martillo}}) y una horizontal (el {{c3::umbo}}).",
        "extra": "Cuadrantes: anterosuperior (AS), anteroinferior (AI), posterosuperior (PS), posteroinferior (PI). Permite localizar perforaciones, abombamientos focales o efusiones loculadas.",
        "tags": ["anatomia"],
    },
    {
        "text": "El cono de luz se localiza normalmente en el cuadrante {{c1::anteroinferior}}. El cuadrante {{c2::posterosuperior}} es la 'zona crítica' porque detrás están los huesecillos (yunque y articulación incudo-estapedial); las perforaciones en esta zona son las de {{c3::peor pronóstico}}.",
        "extra": "Una perforación marginal posterosuperior es señal de alarma para colesteatoma adquirido — siempre derivar.",
        "tags": ["anatomia", "patrones_visuales"],
    },
    {
        "text": "Landmarks visibles en el tímpano normal: {{c1::umbo}} (centro, donde se inserta la punta del manubrio del martillo), {{c2::mango del martillo}} (estría blanca vertical), {{c3::apófisis corta del martillo}} (proyección lateral arriba) y {{c4::pliegues maleolares anterior y posterior}}.",
        "extra": "Si no identificas estos landmarks no estás viendo bien el tímpano: replantea técnica (espéculo, tracción, iluminación) antes de etiquetar 'normal'.",
        "tags": ["anatomia", "patrones_visuales"],
    },
    {
        "text": "Pars tensa vs pars flácida visualmente: la pars tensa es {{c1::translúcida y tensa}}, ocupa la mayor parte de la membrana; la pars flácida es {{c2::pequeña, situada por encima de la apófisis corta del martillo, más laxa y opaca}}.",
        "extra": "La pars flácida es la que primero se retrae cuando hay disfunción tubárica crónica — y donde aparece el colesteatoma.",
        "tags": ["anatomia", "colesteatoma"],
    },

    # Bloque B — Técnica precisa
    {
        "text": "Tamaño del espéculo en adulto: {{c1::4-5 mm}} (el más grande que entre cómodamente). Espéculos pequeños limitan el campo visual; demasiado grandes lesionan la piel del CAE.",
        "extra": "Niño/lactante: 2.5-3 mm. Es importante porque para otoscopia neumática el sello depende del calibre.",
        "tags": ["tecnica"],
    },
    {
        "text": "Profundidad de inserción del otoscopio: solo lo necesario para visualizar la membrana. {{c1::No avanzar al CAE óseo (los 2/3 internos)}}, porque ahí la piel es muy fina, sensible al dolor y se lesiona fácilmente.",
        "extra": "El CAE tiene 1/3 cartilaginoso externo (tolerable) + 2/3 óseo interno (extremadamente sensible). Avanzar más de la cuenta provoca dolor reflejo y reflejo tusígeno por el nervio de Arnold.",
        "tags": ["tecnica"],
    },
    {
        "text": "Tracción del pabellón en adulto: {{c1::arriba y atrás}}. En niños <3 años: {{c2::abajo y atrás}}. Razón anatómica: el CAE infantil es más {{c3::horizontal y corto}}, y el tímpano está más oblicuo.",
        "extra": "Esta maniobra rectifica la curvatura del CAE para alinear visualmente el espéculo con la membrana timpánica.",
        "tags": ["tecnica"],
    },
    {
        "text": "El otoscopio neumático sirve para evaluar {{c1::la movilidad de la membrana timpánica}} mediante una pera de aire integrada; junto con la timpanometría es el {{c2::estándar de oro para diagnosticar OME}}.",
        "extra": "Membrana inmóvil = efusión o perforación. Membrana móvil normal = aireación intacta del oído medio. En OMA la movilidad también está reducida pero predomina el abombamiento clínico.",
        "tags": ["tecnica", "ome"],
    },
    {
        "text": "Para que la otoscopia neumática sea válida, el espéculo debe {{c1::sellar el CAE}}; sin sello no se genera el cambio de presión y la prueba no informa.",
        "extra": "Por eso el tamaño del espéculo importa también para neumática: si queda holgado, el aire escapa y la maniobra es inútil.",
        "tags": ["tecnica"],
    },

    # Bloque C — Criterios y números
    {
        "text": "Criterio diagnóstico AAP 2013 para OMA, presente cualquiera de: (a) {{c1::abombamiento moderado o severo de la membrana}}; (b) abombamiento leve + otalgia o eritema marcado; (c) {{c2::nueva otorrea no atribuible a otitis externa}}.",
        "extra": "El criterio cardinal es el abombamiento — sin abombamiento no se diagnostica OMA aunque haya eritema o fiebre.",
        "tags": ["oma", "criterios"],
    },
    {
        "text": "Estrategia 'observar vs antibiótico' en OMA: en {{c1::adultos}} → antibiótico de entrada. La opción de observación 48-72 h es {{c2::pediátrica}}, restringida a edad ≥6m (mejor ≥2a), enfermedad no severa, no bilateral y sin otorrea.",
        "extra": "Capa 1 dijo 'antibiótico en OMA' como esqueleto; Capa 2 precisa que la observación NO aplica al adulto típico de ECOE.",
        "tags": ["oma", "manejo"],
    },
    {
        "text": "Antibiótico de elección en OMA del adulto: {{c1::amoxicilina 500-875 mg c/8-12 h × 7-10 días}}. Cambiar a {{c2::amoxicilina-clavulánico}} si: antibiótico en últimos 30 días, conjuntivitis purulenta concomitante, falla a amoxicilina o OMA recurrente.",
        "extra": "El clavulánico cubre H. influenzae y M. catarrhalis productoras de betalactamasa. Alergia a penicilina: macrólido o cefalosporina de 2ª–3ª generación.",
        "tags": ["oma", "manejo"],
    },
    {
        "text": "Otitis externa aguda — tratamiento estándar: {{c1::gotas tópicas de quinolona (ciprofloxacino) ± corticoide (dexametasona)}} durante {{c2::7-10 días}}. {{c3::No usar aminoglucósidos}} si se sospecha perforación timpánica (riesgo de ototoxicidad).",
        "extra": "Limpieza previa del CAE (aspiración o irrigación suave si hay membrana íntegra) mejora la penetración del fármaco. Mantener oído seco durante todo el tratamiento.",
        "tags": ["otitis_externa", "manejo"],
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
