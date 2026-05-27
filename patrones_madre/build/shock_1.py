"""Patron Madre: Shock 1 - Hipovolemico.

Primer subdeck del patron madre "shock / mala perfusion".
Cubre la rama hipovolemica (los proximos shocks tendran su propio numero:
shock 2 = septico, shock 3 = cardiogenico, shock 4 = obstructivo).

Formato de embudo Q&A en 4 niveles (ver patrones_madre/README.md):
- N1 (1 card): identificar el patron madre.
- N2 (4 cards): imagen mental -> nombre formal de la subcausa.
- N3 (4 cards): mecanismo fisiopatologico -> signo clinico (listas correlacionadas).
- N4 (4 cards): escena clinica -> accion de manejo justificada.

Subcausas: GI, hemorragico, quemaduras, pediatrico.
Total: 13 cards.
"""
import os
import genanki

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "output")
os.makedirs(OUTPUT_DIR, exist_ok=True)

MODEL_QA_ID = 1607392320  # reusable Q&A (mismo que gineco capa 5)
DECK_ID = 2096096757
DECK_NAME = "Patrones Madre::Shock 1"

CSS = """
.card {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  font-size: 19px; text-align: left; color: #1a1a1a;
  background-color: #fafafa; padding: 20px; line-height: 1.55;
}
.nivel {
  display: inline-block; padding: 4px 12px; margin-bottom: 14px;
  background: #7c2d12; color: #fff; border-radius: 6px;
  font-size: 13px; letter-spacing: 0.5px; font-weight: 600;
}
.header {
  font-weight: 700; margin-bottom: 10px; color: #1e3a8a;
}
.escena {
  font-style: italic; margin-bottom: 12px; color: #374151;
  background: #fef3c7; padding: 10px 14px; border-radius: 6px;
}
ol.items { margin: 8px 0 14px 0; padding-left: 24px; }
ol.items li { margin: 6px 0; }
.prompt { color: #2563eb; font-weight: 600; margin-top: 10px; }
.respuesta { font-size: 21px; font-weight: 700; color: #047857; margin-top: 4px; }
.metafora { color: #6b21a8; margin-top: 6px; }
#extra { margin-top: 16px; border: none; border-top: 1px solid #d4d4d4; padding-top: 12px; }
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

BASE_TAGS = ["patrones_madre", "ecoe", "shock_hipovolemico"]


def add_note(front, back, tags):
    deck.add_note(genanki.Note(
        model=model_qa,
        fields=[front, back],
        tags=BASE_TAGS + tags,
    ))


def items(lst):
    return "<ol class='items'>" + "".join(f"<li>{x}</li>" for x in lst) + "</ol>"


# ============================================================
# NIVEL 1 — Identificar el patron madre (1 card)
# ============================================================
add_note(
    front=(
        '<div class="nivel">NIVEL 1 — PATRON MADRE</div>'
        '<div>Choque donde lo que falla es <b>el liquido en el sistema circulatorio</b>.</div>'
        '<div class="prompt">&iquest;Que tipo de shock es?</div>'
    ),
    back=(
        '<div class="respuesta">Shock hipovolemico</div>'
        '<div class="metafora">Metafora: tanque vacio. '
        'Menos volumen &rarr; menos retorno venoso &rarr; menos gasto cardiaco &rarr; menos perfusion tisular.</div>'
    ),
    tags=["n1"],
)


# ============================================================
# NIVEL 2 — Imagen mental -> nombre formal (4 cards)
# ============================================================
N2 = '<div class="nivel">NIVEL 2 — IMAGEN MENTAL &rarr; NOMBRE</div>'

add_note(
    front=(
        N2 +
        '<div>El cuerpo es una planta perdiendo agua por arriba y por abajo. '
        'No pierde sangre &mdash; pierde agua, sodio, potasio y bicarbonato.</div>'
        '<div class="prompt">&iquest;Que subcausa de shock hipovolemico es?</div>'
    ),
    back=(
        '<div class="respuesta">Hipovolemico por vomito / diarrea / deshidratacion</div>'
    ),
    tags=["n2", "gi"],
)

add_note(
    front=(
        N2 +
        '<div>Ademas del liquido pierdes globulos rojos y los "camiones de oxigeno" (Hb). '
        'El tanque se vacia y los transportadores tambien.</div>'
        '<div class="prompt">&iquest;Que subcausa de shock hipovolemico es?</div>'
    ),
    back=(
        '<div class="respuesta">Hipovolemico hemorragico</div>'
        '<div class="metafora">Escenarios: HDA, trauma, ectopico roto, hemorragia obstetrica.</div>'
    ),
    tags=["n2", "hemorragico"],
)

add_note(
    front=(
        N2 +
        '<div>La piel deja de ser barrera. Los capilares se vuelven permeables '
        'y el plasma "se fuga" hacia los tejidos aunque no veas sangrar.</div>'
        '<div class="prompt">&iquest;Que subcausa de shock hipovolemico es?</div>'
    ),
    back=(
        '<div class="respuesta">Hipovolemico por quemaduras extensas</div>'
    ),
    tags=["n2", "quemaduras"],
)

add_note(
    front=(
        N2 +
        '<div>Tanque pequeno con poca reserva: pequenas perdidas producen gran impacto circulatorio. '
        'Mas superficie corporal por kilo, menos margen.</div>'
        '<div class="prompt">&iquest;Que subcausa de shock hipovolemico es?</div>'
    ),
    back=(
        '<div class="respuesta">Hipovolemico pediatrico por gastroenteritis</div>'
    ),
    tags=["n2", "pediatrico"],
)


# ============================================================
# NIVEL 3 — Mecanismo fisiopatologico -> signo clinico (4 cards)
# ============================================================
N3 = '<div class="nivel">NIVEL 3 — MECANISMO &rarr; SIGNO</div>'

# 6. GI
add_note(
    front=(
        N3 +
        '<div class="header">Hipovolemico por vomito / diarrea</div>'
        '<div>Por cada mecanismo, &iquest;que signo o sintoma produce?</div>' +
        items([
            "Perdida de agua intravascular",
            "&darr; volumen circulante",
            "Vasoconstriccion periferica compensatoria",
            "&darr; retorno venoso al pararse",
            "Rinon retiene agua",
            "&darr; volumen intersticial",
        ])
    ),
    back=items([
        "Mucosas secas, sed",
        "Taquicardia, hipotension",
        "Piel fria, palidez, llenado capilar lento",
        "Hipotension ortostatica",
        "Oliguria",
        "Ojos hundidos",
    ]),
    tags=["n3", "gi"],
)

# 7. Hemorragico
add_note(
    front=(
        N3 +
        '<div class="header">Hipovolemico hemorragico</div>'
        '<div>Por cada mecanismo, &iquest;que signo o sintoma produce?</div>' +
        items([
            "&darr; volumen + &darr; Hb (transporte de O&#8322;)",
            "Vasoconstriccion periferica",
            "Descarga adrenergica",
            "Volumen circulante critico",
            "Hipoperfusion cerebral",
        ])
    ),
    back=items([
        "Palidez, debilidad, mareo",
        "Piel fria, taquicardia",
        "Diaforesis",
        "Hipotension",
        "Sincope, confusion",
    ]),
    tags=["n3", "hemorragico"],
)

# 8. Quemaduras
add_note(
    front=(
        N3 +
        '<div class="header">Hipovolemico por quemadura</div>'
        '<div>Por cada mecanismo, &iquest;que signo o sintoma produce?</div>' +
        items([
            "Plasma fuga al intersticio (capilares permeables)",
            "&darr; volumen efectivo",
            "Perdida de barrera cutanea",
            "Dano termico tisular",
        ])
    ),
    back=items([
        "Edema",
        "Taquicardia, hipotension",
        "Quemadura extensa con piel destruida",
        "Dolor, sed",
    ]),
    tags=["n3", "quemaduras"],
)

# 9. Pediatrico
add_note(
    front=(
        N3 +
        '<div class="header">Hipovolemico pediatrico</div>'
        '<div>Por cada mecanismo, &iquest;que signo o sintoma produce?</div>' +
        items([
            "Perdida de agua intravascular",
            "&darr; volumen intersticial",
            "Perdida de liquido en lactante con fontanela abierta",
            "Vasoconstriccion periferica",
            "Hipoperfusion cerebral",
            "Hipotension tardia (compensa hasta el final)",
        ])
    ),
    back=items([
        "Mucosas secas, llanto sin lagrimas",
        "Ojos hundidos",
        "Fontanela hundida",
        "Llenado capilar lento, extremidades frias",
        "Irritabilidad &rarr; letargo",
        "Pulso debil, hipotension grave",
    ]),
    tags=["n3", "pediatrico"],
)


# ============================================================
# NIVEL 4 — Escena clinica -> accion de manejo (4 cards)
# ============================================================
N4 = '<div class="nivel">NIVEL 4 — ESCENA &rarr; MANEJO</div>'

# 10. GI
add_note(
    front=(
        N4 +
        '<div class="escena">Adulto con vomito y diarrea de varios dias, mucosas secas, '
        'taquicardia, hipotension ortostatica. Llega inestable a urgencias.</div>'
        '<div>Para cada problema visualizado, &iquest;que accion tomas?</div>' +
        items([
            "Llega inestable &mdash; necesitas mapa rapido del estado",
            "El tanque esta vacio y hay que rellenarlo ya",
            "Perdio no solo agua, tambien las sales que regulan ritmo cardiaco y funcion celular",
            "Los rinones llevan horas sin recibir flujo",
            "Si rellenas sin medir, vuelas a ciegas",
            "Dias vomitando &rarr; el pH puede estar fuera de rango",
        ])
    ),
    back=items([
        "ABCDE + monitorizacion",
        "Dos vias perifericas + cristaloides IV",
        "Electrolitos sericos (Na / K / HCO&#8323;)",
        "Urea / creatinina",
        "Vigilar diuresis",
        "Gasometria + lactato",
    ]),
    tags=["n4", "gi"],
)

# 11. Hemorragico
add_note(
    front=(
        N4 +
        '<div class="escena">Paciente sangrante (HDA, trauma, ectopico roto, posparto) '
        'palido, taquicardico, hipotenso, diaforetico.</div>'
        '<div>Para cada problema visualizado, &iquest;que accion tomas?</div>' +
        items([
            "Sangrante e inestable &mdash; no es momento de estar solo",
            "Si el liquido entra lento, se va antes de llegar al sistema",
            "Va a necesitar sangre &mdash; pidela antes de necesitarla",
            "Aunque le entres litros, no llevan oxigeno como la sangre",
            "La hemorragia sigue corriendo hasta que cierres la llave",
        ])
    ),
    back=items([
        "ABCDE + pedir ayuda + monitorizacion",
        "Dos vias gruesas + cristaloide inicial",
        "BH, grupo y pruebas cruzadas, tiempos de coagulacion",
        "Protocolo de transfusion si inestable",
        "FAST / endoscopia / cirugia / USG segun contexto",
    ]),
    tags=["n4", "hemorragico"],
)

# 12. Quemaduras
add_note(
    front=(
        N4 +
        '<div class="escena">Gran quemado, posiblemente con humo, dolor extremo, '
        'edema progresivo, hollin en cara.</div>'
        '<div>Para cada problema visualizado, &iquest;que accion tomas?</div>' +
        items([
            "Quemadura facial / sibilancias / hollin &mdash; la via aerea se esta cerrando por edema",
            "La quemadura sigue danando tejido si no la detienes",
            "La piel ya no es barrera &mdash; frio, infeccion y evaporacion entran libres",
            "Quemaduras duelen como pocas cosas",
            "El plasma se fuga del vaso a los tejidos &mdash; el tanque se vacia por dentro",
            "Necesitas saber si el liquido que entra esta llegando al rinon",
            "Si fue incendio cerrado el CO lo mata en silencio; si fue electrica el corazon puede estar arritmizado",
        ])
    ),
    back=items([
        "ABCDE + evaluar inhalacion temprano",
        "Retirar ropa, enfriar si reciente",
        "Cubrir quemadura con apositos limpios",
        "Analgesia",
        "Via IV + reanimacion con formula de Parkland",
        "Sonda Foley + diuresis horaria",
        "Carboxihemoglobina si humo / EKG si electrica",
    ]),
    tags=["n4", "quemaduras"],
)

# 13. Pediatrico
add_note(
    front=(
        N4 +
        '<div class="escena">Nino con gastroenteritis, ojos hundidos, irritable, '
        'mucosas secas, llenado capilar lento.</div>'
        '<div>Para cada problema visualizado, &iquest;que accion tomas?</div>' +
        items([
            "Mucosas secas pero todavia toma agua",
            "El intestino del nino aun absorbe &mdash; aprovecha esa puerta",
            "Los ninos se ven \"bien\" hasta que se descompensan de golpe",
            "Nino en shock o que ya no traga &mdash; los signos hablan de emergencia",
            "Nino confuso o letargico &mdash; el azucar tambien puede estar bajo",
            "En shock las venas se colapsan &mdash; no esperes 20 minutos buscando una",
            "Cuerpo pequeno se rellena rapido pero tambien se desborda rapido",
        ])
    ),
    back=items([
        "Vida suero oral en tomas pequenas frecuentes",
        "(justifica la via oral)",
        "Revalorar perfusion seguido",
        "ABCDE",
        "Glucosa capilar",
        "Via IV o intraosea",
        "Bolo de cristaloide + reevaluar + corregir electrolitos",
    ]),
    tags=["n4", "pediatrico"],
)


# ============================================================
# Build
# ============================================================
def build():
    out_path = os.path.join(OUTPUT_DIR, "Patrones_Madre_Shock_1.apkg")
    genanki.Package(deck).write_to_file(out_path)
    print(f"OK: {out_path}  ({len(deck.notes)} notas)")


if __name__ == "__main__":
    build()
