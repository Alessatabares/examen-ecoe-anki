#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Conectores verbalizados ECOE — frases puente que dices en voz alta para hacer
EXPLÍCITO cada bloque de la rúbrica ante el sinodal y asegurar el punto.
Una tarjeta por transición. El cloze esconde el conector clave; el Extra dice
qué bloque asegura y el truco. (Este deck ES verbalización, como los decks
'Verbalización ECOE' / 'Preparación Verbalizada' del repo.)
"""
import os
import genanki

MODEL_ID = 1607392319  # cloze_estandar
DECK_ID = 1990012005
OUT = os.path.join(os.path.dirname(__file__), "output")

model = genanki.Model(
    MODEL_ID,
    "Estudio Médico Cloze",
    fields=[{"name": "Text"}, {"name": "Extra"}],
    templates=[{
        "name": "Cloze",
        "qfmt": "{{cloze:Text}}",
        "afmt": '{{cloze:Text}}<hr id="extra">{{Extra}}',
    }],
    css="""
    .card {
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      font-size: 19px; text-align: left; color: #1a1a1a;
      background-color: #fafafa; padding: 20px; line-height: 1.5;
    }
    .cloze { font-weight: 600; color: #2563eb; }
    #extra { margin-top: 16px; border: none; border-top: 1px solid #d4d4d4; }
    """,
    model_type=genanki.Model.CLOZE,
)
TAGS = ["ecoe", "verbalizacion", "conectores", "rubrica"]
deck = genanki.Deck(DECK_ID, "Conectores Verbalizados ECOE::Frases de transicion por bloque")


def note(text, extra):
    deck.add_note(genanki.Note(model=model, fields=[text.strip(), extra.strip()], tags=TAGS))


note(
    "🎬 [Apertura · Comunicación] «Buenos días, soy [nombre], estudiante de medicina. "
    "¿Me confirma su nombre y edad? "
    "{{c1::Le voy a hacer unas preguntas, después le exploraré y al final le explicaré qué pienso y qué haremos}}. "
    "¿Está de acuerdo?»",
    "Asegura: presentación + CONSENTIMIENTO (Comunicación 10%). "
    "Anunciar el plan completo hace que el evaluador vea estructura desde el segundo 0.",
)
note(
    "🎬 [Inicio del interrogatorio · Información] "
    "«Voy a empezar preguntándole por su molestia principal "
    "{{c1::para orientarme y poder enfocar el resto de la consulta}}.»",
    "Asegura: Obtención de información (15%). Decir el PORQUÉ muestra un interrogatorio "
    "dirigido, no al azar — ese es el matiz que da el 3–4.",
)
note(
    "🎬 [Profundizar el síntoma · Información] «Para entender bien su [síntoma], le voy a preguntar "
    "{{c1::desde cuándo, cómo es, a dónde se corre y qué lo mejora o empeora}}, "
    "y qué otros síntomas lo acompañan.»",
    "Es ALICIA en lenguaje de paciente. «Síntomas que lo acompañan» es la puerta a las banderas rojas.",
)
note(
    "🎬 [Descartar gravedad · Información + Errores críticos] "
    "«Ahora le haré unas preguntas específicas "
    "{{c1::para descartar datos de alarma o causas graves}}.»",
    "Verbalizar que BUSCAS lo grave te blinda contra el error crítico «no identificar datos de alarma».",
)
note(
    "🎬 [Puente a la exploración · Información → Exploración] "
    "«Con lo que me cuenta ya tengo una sospecha; ahora "
    "{{c1::lo/la voy a explorar para confirmar o descartar lo que pienso}}. "
    "Me lavo las manos y cuido su privacidad.»",
    "Conecta razonamiento con exploración. Lavado de manos + privacidad = profesionalismo "
    "(evita la falta ética).",
)
note(
    "🎬 [Exploración] «Empiezo por {{c1::los signos vitales y el estado general}}, "
    "y luego exploro [región] de forma ordenada.» "
    "Al terminar: «Encuentro [positivos] y {{c2::NO encuentro [negativos relevantes]}}.»",
    "Vitales primero saca del 1–2. Decir hallazgos positivos Y negativos sube de 3 a 4 en Exploración (15%).",
)
note(
    "🎬 [Diagnóstico · Reconocimiento 25%] «Integrando todo, mi diagnóstico principal es [entidad], "
    "{{c1::porque presenta [hallazgo 1, 2 y 3]}}.»",
    "Nombrar + JUSTIFICAR con hallazgos = 4 en el bloque que más pesa (25%). Solo nombrar = 3.",
)
note(
    "🎬 [Diferenciales · Razonamiento 15%] «Considero como diferenciales, en orden: "
    "primero [X] {{c1::porque [evidencia]}}, luego [Y] porque...; y {{c2::descarto [Z] porque [falta tal dato]}}.»",
    "Mínimo 2 diferenciales JERARQUIZADOS y justificados. El «descarto X porque» es lo que demuestra razonamiento.",
)
note(
    "🎬 [Estudios · 10%] «Para confirmar mi sospecha y descartar los diferenciales, "
    "solicito de forma dirigida [estudio]; "
    "{{c1::sería anormal si [umbral], lo que apoyaría [diagnóstico]}}.»",
    "Pedir dirigido + INTERPRETAR el umbral = costo-efectivo (sube a 4). Pedir «de escopeta» baja a 1.",
)
note(
    "🎬 [Plan · 15%] «Mi plan es: "
    "{{c1::tratamiento [X], seguimiento (cuándo revaloro) y datos de alarma para regresar}}.»",
    "Las 3 partes (tratamiento + seguimiento + alarmas) = manejo integral (4). "
    "Omitir las alarmas roza el error crítico.",
)
note(
    "🎬 [Cierre · Comunicación + Errores críticos] "
    "«Le explico en palabras simples qué tiene y qué haremos. "
    "{{c1::¿Tiene alguna duda?}} Y si presenta [datos de alarma], {{c2::acuda de inmediato a urgencias}}.»",
    "Cerrar con dudas + red de seguridad = comunicación centrada en el paciente y referencia oportuna.",
)

os.makedirs(OUT, exist_ok=True)
out_path = os.path.join(OUT, "Conectores_Verbalizados_ECOE.apkg")
genanki.Package([deck]).write_to_file(out_path)
print(f"OK -> {out_path}")
print(f"  Conectores: {len(deck.notes)} notas (deck {DECK_ID})")
