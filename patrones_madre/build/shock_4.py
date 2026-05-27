"""Patron Madre: Shock 4 - Obstructivo.

Cuarto subdeck del patron madre "shock / mala perfusion".
Cierra la serie (shock 1 = hipovolemico, shock 2 = septico/distributivo,
shock 3 = cardiogenico, shock 4 = obstructivo).

Formato de embudo Q&A en 4 niveles (ver patrones_madre/README.md):
- N1 (1 card): identificar el patron madre.
- N2 (3 cards): imagen mental -> nombre formal de la subcausa.
- N3 (3 cards): mecanismo fisiopatologico -> signo clinico (listas correlacionadas).
- N4 (3 cards): escena clinica -> accion de manejo justificada.

Subcausas: TEP masivo, neumotorax a tension, taponamiento cardiaco.
Total: 10 cards.
"""
import os
import genanki

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "output")
os.makedirs(OUTPUT_DIR, exist_ok=True)

MODEL_QA_ID = 1607392320  # reusable Q&A (mismo que shock_1, shock_2, shock_3 y gineco capa 5)
DECK_ID = 1428675319
DECK_NAME = "Patrones Madre::Shock 4"

CSS = """
.card {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  font-size: 19px; text-align: left; color: #1a1a1a;
  background-color: #fafafa; padding: 20px; line-height: 1.55;
}
.nivel {
  display: inline-block; padding: 4px 12px; margin-bottom: 14px;
  background: #581c87; color: #fff; border-radius: 6px;
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

BASE_TAGS = ["patrones_madre", "ecoe", "shock_obstructivo"]


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
        '<div>Choque donde <b>algo bloquea fisicamente el flujo sanguineo</b>. '
        'El tanque NO esta vacio, la bomba puede estar funcional y los vasos no son el problema &mdash; '
        'la sangre quiere pasar, pero algo la estrangula al llenar o salir del corazon.</div>'
        '<div class="prompt">&iquest;Que tipo de shock es?</div>'
    ),
    back=(
        '<div class="respuesta">Shock obstructivo</div>'
        '<div class="metafora">Metafora: el sistema circulatorio es una carretera con un '
        'obstaculo mecanico. Por eso suele verse: disnea subita + hipotension + '
        '<b>ingurgitacion yugular</b> + hipoxia (la sangre se acumula antes del corazon).</div>'
        '<div class="metafora"><b>Frase madre:</b> en obstructivo NO se resuelve "llenando" &mdash; '
        'hay que <b>quitar la obstruccion</b>. TEP = destapar coagulo. '
        'Neumotorax tension = sacar aire. Taponamiento = sacar liquido del pericardio.</div>'
    ),
    tags=["n1"],
)


# ============================================================
# NIVEL 2 — Imagen mental -> nombre formal (3 cards)
# ============================================================
N2 = '<div class="nivel">NIVEL 2 — IMAGEN MENTAL &rarr; NOMBRE</div>'

add_note(
    front=(
        N2 +
        '<div>Un <b>coagulo viaja</b> hasta la arteria pulmonar y choca como una pared subita. '
        'El ventriculo derecho intenta empujar contra ese muro, se dilata y falla; '
        'al pulmon izquierdo le llega poca sangre y el VI se queda vacio.</div>'
        '<div class="prompt">&iquest;Que subcausa de shock obstructivo es?</div>'
    ),
    back=(
        '<div class="respuesta">TEP masivo (tromboembolia pulmonar)</div>'
        '<div class="metafora">Pistas ECOE: cirugia reciente, inmovilizacion, cancer, '
        'TVP previa, puerperio, anticonceptivos.</div>'
    ),
    tags=["n2", "tep"],
)

add_note(
    front=(
        N2 +
        '<div><b>Aire entra al torax y no puede salir</b>. El hemitorax se vuelve una camara '
        'de presion: el pulmon colapsa, el mediastino se desplaza y las venas cavas quedan '
        'aplastadas &mdash; el corazon ya no se llena.</div>'
        '<div class="prompt">&iquest;Que subcausa de shock obstructivo es?</div>'
    ),
    back=(
        '<div class="respuesta">Neumotorax a tension</div>'
        '<div class="metafora">Pistas: trauma, ventilacion mecanica, paciente alto / delgado '
        'con dolor subito.</div>'
    ),
    tags=["n2", "neumotorax_tension"],
)

add_note(
    front=(
        N2 +
        '<div><b>Liquido o sangre se acumula en el pericardio</b> rigido. El corazon queda '
        '"ahorcado" dentro de una bolsa que no se expande &mdash; las camaras no se llenan '
        'y el gasto cae.</div>'
        '<div class="prompt">&iquest;Que subcausa de shock obstructivo es?</div>'
    ),
    back=(
        '<div class="respuesta">Taponamiento cardiaco</div>'
        '<div class="metafora"><b>Triada de Beck:</b> hipotension + yugulares ingurgitadas + '
        'ruidos cardiacos velados.</div>'
    ),
    tags=["n2", "taponamiento"],
)


# ============================================================
# NIVEL 3 — Mecanismo fisiopatologico -> signo clinico (3 cards)
# ============================================================
N3 = '<div class="nivel">NIVEL 3 — MECANISMO &rarr; SIGNO</div>'

# TEP masivo
add_note(
    front=(
        N3 +
        '<div class="header">TEP masivo</div>'
        '<div>Por cada mecanismo, &iquest;que signo o sintoma produce?</div>' +
        items([
            "Pulmon ventilado pero subitamente mal perfundido",
            "Areas ventiladas sin perfusion (V/Q alterado)",
            "Compensacion por hipoxia y bajo gasto",
            "Irritacion pleural / infarto pulmonar",
            "VD sobrecargado, no puede vaciarse",
            "Al VI le llega poca sangre",
            "Caida brusca del gasto cardiaco",
            "Hipoxia + descarga simpatica",
        ])
    ),
    back=items([
        "Disnea subita",
        "Hipoxia",
        "Taquicardia",
        "Dolor toracico pleuritico",
        "Ingurgitacion yugular",
        "Hipotension",
        "Sincope",
        "Ansiedad intensa",
    ]),
    tags=["n3", "tep"],
)

# Neumotorax a tension
add_note(
    front=(
        N3 +
        '<div class="header">Neumotorax a tension</div>'
        '<div>Por cada mecanismo, &iquest;que signo o sintoma produce?</div>' +
        items([
            "Pulmon colapsado por aire bajo presion",
            "Pleura irritada por aire subito",
            "Menos superficie ventilada",
            "Aire libre bajo presion en hemitorax",
            "Pulmon ausente bajo el estetoscopio",
            "Presion intratoracica aplasta venas cavas",
            "Sangre atorada antes del corazon",
            "Presion desplaza mediastino (signo tardio)",
            "Compensacion por hipoxia y shock",
        ])
    ),
    back=items([
        "Disnea subita",
        "Dolor toracico subito",
        "Hipoxia",
        "Hemitorax hiperresonante",
        "Ausencia de murmullo vesicular",
        "Hipotension",
        "Ingurgitacion yugular",
        "Desviacion traqueal contralateral",
        "Taquicardia",
    ]),
    tags=["n3", "neumotorax_tension"],
)

# Taponamiento cardiaco
add_note(
    front=(
        N3 +
        '<div class="header">Taponamiento cardiaco</div>'
        '<div>Por cada mecanismo, &iquest;que signo o sintoma produce?</div>' +
        items([
            "Cavidades no se llenan &rarr; bajo volumen sistolico",
            "Sangre no puede entrar al corazon",
            "Liquido pericardico amortigua el sonido",
            "Compensacion por bajo gasto",
            "Bajo gasto + congestion retrograda",
            "Inspiracion empeora llenado izquierdo",
            "Hipoperfusion sistemica",
            "Origen inflamatorio (pericarditis) o hemorragico (trauma)",
        ])
    ),
    back=items([
        "Hipotension",
        "Ingurgitacion yugular",
        "Ruidos cardiacos velados / apagados",
        "Taquicardia",
        "Disnea",
        "Pulso paradojico (&gt;10 mmHg)",
        "Piel fria, confusion, agitacion",
        "Dolor toracico",
    ]),
    tags=["n3", "taponamiento"],
)


# ============================================================
# NIVEL 4 — Escena clinica -> accion de manejo (3 cards)
# ============================================================
N4 = '<div class="nivel">NIVEL 4 — ESCENA &rarr; MANEJO</div>'

# TEP masivo
add_note(
    front=(
        N4 +
        '<div class="escena">Mujer postquirurgica de cadera, dia 4. Subitamente disneica, '
        'taquicardica 130, TA 80/50, Sat 84%, yugulares ingurgitadas, ansiosa. '
        'Pierna derecha edematizada.</div>'
        '<div>Para cada problema visualizado, &iquest;que accion tomas?</div>' +
        items([
            "Inestable e hipoxemica &mdash; mapa rapido",
            "Necesita oxigeno ya",
            "Sin ECG no descartas IAM ni ves sobrecarga derecha",
            "Hay que confirmar / intuir el TEP",
            "Si esta estable, lo confirmas con imagen",
            "Si esta en shock, no la mandes a la TAC sin verla primero",
            "Buscar la fuente del embolo",
            "El coagulo sigue creciendo si no haces nada",
            "La presion no aguanta &mdash; necesita soporte",
            "Bloqueo masivo del flujo pulmonar &mdash; hay que destaparlo",
        ])
    ),
    back=items([
        "ABCDE + monitor + 2 vias IV",
        "<b>Oxigeno</b> (mascarilla / VMNI / IOT si falla)",
        "ECG + troponina",
        "Gasometria + dimero D (util si baja / intermedia sospecha)",
        "<b>AngioTAC pulmonar</b> si estable",
        "<b>Eco bedside</b> si inestable (busca dilatacion de VD)",
        "USG Doppler de piernas",
        "<b>Anticoagulacion</b> (HNF IV) si no hay contraindicacion",
        "Noradrenalina si hipotensa; <b>evitar bolos grandes</b> (sobrecarga VD)",
        "<b>Trombolisis sistemica</b> si TEP masivo con shock + UCI",
    ]),
    tags=["n4", "tep"],
)

# Neumotorax a tension
add_note(
    front=(
        N4 +
        '<div class="escena">Joven politraumatizado, dolor toracico derecho subito, disnea '
        'extrema, TA 70/40, yugulares ingurgitadas, hemitorax derecho hiperresonante, '
        'sin murmullo, traquea desviada a la izquierda.</div>'
        '<div>Para cada problema visualizado, &iquest;que accion tomas?</div>' +
        items([
            "Inestable extremo &mdash; la clinica es el diagnostico",
            "<b>NO esperes radiografia &mdash; esto es clinico</b>",
            "El aire bajo presion esta aplastando el retorno venoso",
            "Despues de descomprimir, el pulmon necesita drenaje continuo",
            "Mejora hipoxia y ayuda a reabsorcion",
            "Hay que confirmar lo que ya trataste",
            "Si fue trauma, hay mas cosas que buscar",
        ])
    ),
    back=items([
        "ABCDE + monitor + 2 vias IV",
        "<b>Descompresion inmediata con aguja</b> (2&deg; EIC linea medioclavicular o 4-5&deg; EIC linea axilar anterior)",
        "(justifica la descompresion sin esperar)",
        "<b>Tubo de torax</b> despues de la descompresion",
        "Oxigeno alto flujo",
        "Rx torax post-procedimiento (USG pulmonar si disponible)",
        "Evaluacion ATLS completa por trauma",
    ]),
    tags=["n4", "neumotorax_tension"],
)

# Taponamiento cardiaco
add_note(
    front=(
        N4 +
        '<div class="escena">Paciente con herida penetrante precordial (o pericarditis previa). '
        'Hipotenso, taquicardico, yugulares ingurgitadas marcadas, ruidos cardiacos velados, '
        'pulso paradojico de 18 mmHg, agitado.</div>'
        '<div>Para cada problema visualizado, &iquest;que accion tomas?</div>' +
        items([
            "Triada de Beck + inestable &mdash; sospecha clara",
            "Confirma rapido con imagen a pie de cama",
            "Voltaje bajo o alternancia electrica orientan",
            "En trauma, busca liquido pericardico con USG dirigida",
            "El pericardio aprieta &mdash; hay que quitarle presion ya",
            "Pequeno bolo puede ayudar mientras drenas (precarga)",
            "Si es trauma penetrante con inestabilidad extrema, la aguja no basta",
            "Buscar y tratar la causa de fondo",
        ])
    ),
    back=items([
        "ABCDE + monitor + 2 vias IV + O&#8322;",
        "<b>Eco bedside</b> (confirma liquido + colapso de cavidades)",
        "ECG",
        "<b>FAST extendido</b> si trauma",
        "<b>Pericardiocentesis urgente</b> (subxifoidea guiada por eco)",
        "Cristaloides en bolo pequeno como puente",
        "<b>Toracotomia</b> si trauma penetrante e inestabilidad extrema",
        "Tratar causa (pericarditis, uremica, neoplasica, diseccion)",
    ]),
    tags=["n4", "taponamiento"],
)


# ============================================================
# Build
# ============================================================
def build():
    out_path = os.path.join(OUTPUT_DIR, "Patrones_Madre_Shock_4.apkg")
    genanki.Package(deck).write_to_file(out_path)
    print(f"OK: {out_path}  ({len(deck.notes)} notas)")


if __name__ == "__main__":
    build()
