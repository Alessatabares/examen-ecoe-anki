"""Patron Madre: Shock 3 - Cardiogenico.

Tercer subdeck del patron madre "shock / mala perfusion".
Cubre la rama cardiogenica (shock 1 = hipovolemico, shock 2 = septico/distributivo,
shock 4 = obstructivo).

Formato de embudo Q&A en 4 niveles (ver patrones_madre/README.md):
- N1 (1 card): identificar el patron madre.
- N2 (3 cards): imagen mental -> nombre formal de la subcausa.
- N3 (3 cards): mecanismo fisiopatologico -> signo clinico (listas correlacionadas).
- N4 (3 cards): escena clinica -> accion de manejo justificada.

Subcausas: IAM complicado, arritmia grave, insuficiencia cardiaca aguda.
Total: 10 cards.
"""
import os
import genanki

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "output")
os.makedirs(OUTPUT_DIR, exist_ok=True)

MODEL_QA_ID = 1607392320  # reusable Q&A (mismo que shock_1, shock_2 y gineco capa 5)
DECK_ID = 1734892056
DECK_NAME = "Patrones Madre::Shock 3"

CSS = """
.card {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  font-size: 19px; text-align: left; color: #1a1a1a;
  background-color: #fafafa; padding: 20px; line-height: 1.55;
}
.nivel {
  display: inline-block; padding: 4px 12px; margin-bottom: 14px;
  background: #1e40af; color: #fff; border-radius: 6px;
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

BASE_TAGS = ["patrones_madre", "ecoe", "shock_cardiogenico"]


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
        '<div>Choque donde lo que falla es <b>la bomba</b>: el corazon no puede empujar la sangre hacia adelante. '
        'El tanque NO esta vacio y los vasos NO estan dilatados &mdash; la bomba esta danada, fuera de ritmo o agotada.</div>'
        '<div class="prompt">&iquest;Que tipo de shock es?</div>'
    ),
    back=(
        '<div class="respuesta">Shock cardiogenico</div>'
        '<div class="metafora">Metafora: una bomba debil conectada a una tuberia llena. '
        'Sale poca sangre hacia adelante (baja perfusion) y se acumula hacia atras '
        '(congestion pulmonar / venosa).</div>'
        '<div class="metafora"><b>Frase madre:</b> no pienses "le falta liquido". Piensa: '
        '"la bomba no puede mover lo que ya tiene". Por eso NO lo llenas a ciegas &mdash; '
        'buscas ECG, causa cardiaca, congestion y reperfusion / reversion urgente.</div>'
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
        '<div>La bomba tiene una <b>pared muerta</b>: una arteria coronaria se tapo y una zona '
        'del musculo dejo de apretar. El resto intenta compensar, pero el gasto cae y la sangre '
        'se regresa al pulmon.</div>'
        '<div class="prompt">&iquest;Que subcausa de shock cardiogenico es?</div>'
    ),
    back=(
        '<div class="respuesta">IAM complicado con shock cardiogenico</div>'
        '<div class="metafora">Causa mas frecuente de shock cardiogenico. '
        'El tratamiento causal es <b>abrir la arteria</b> (reperfusion temprana).</div>'
    ),
    tags=["n2", "iam"],
)

add_note(
    front=(
        N2 +
        '<div>La bomba no esta rota &mdash; esta <b>golpeando fuera de ritmo</b>. '
        'Puede latir tan rapido que no se llena, tan lento que no alcanza, '
        'o tan caotico que no contrae utilmente.</div>'
        '<div class="prompt">&iquest;Que subcausa de shock cardiogenico es?</div>'
    ),
    back=(
        '<div class="respuesta">Arritmia grave inestable</div>'
        '<div class="metafora">Tres formas: taquiarritmia (no se llena), bradiarritmia '
        '(no bombea suficientes veces) o ritmo caotico (contraccion inefectiva). '
        'La pregunta clave en ECOE: &iquest;estable o inestable?</div>'
    ),
    tags=["n2", "arritmia"],
)

add_note(
    front=(
        N2 +
        '<div>Una <b>bomba cansada con trafico acumulado detras</b>: no logra manejar la carga '
        'de volumen / presion y la sangre se atasca en pulmon (izquierda), '
        'venas sistemicas (derecha) o ambas (global).</div>'
        '<div class="prompt">&iquest;Que subcausa de shock cardiogenico es?</div>'
    ),
    back=(
        '<div class="respuesta">Insuficiencia cardiaca aguda descompensada</div>'
        '<div class="metafora">Falla izquierda &rarr; congestion pulmonar. '
        'Falla derecha &rarr; congestion venosa sistemica. '
        'Si progresa: hipotension, piel fria, oliguria, confusion (bajo gasto).</div>'
    ),
    tags=["n2", "ic_aguda"],
)


# ============================================================
# NIVEL 3 — Mecanismo fisiopatologico -> signo clinico (3 cards)
# ============================================================
N3 = '<div class="nivel">NIVEL 3 — MECANISMO &rarr; SIGNO</div>'

# IAM complicado
add_note(
    front=(
        N3 +
        '<div class="header">IAM complicado con shock cardiogenico</div>'
        '<div>Por cada mecanismo, &iquest;que signo o sintoma produce?</div>' +
        items([
            "Miocardio isquemico libera senales de dolor",
            "Descarga simpatica por estres / isquemia",
            "Reflejo vagal (sobre todo IAM inferior)",
            "Ventriculo no expulsa suficiente sangre",
            "Vasoconstriccion compensatoria",
            "Congestion retrograda al pulmon",
            "Liquido en intersticio / alveolos",
            "Bajo flujo renal y cerebral",
        ])
    ),
    back=items([
        "Dolor toracico opresivo irradiado",
        "Diaforesis",
        "Nausea / vomito",
        "Hipotension",
        "Piel fria, palidez",
        "Disnea",
        "Estertores",
        "Oliguria, confusion",
    ]),
    tags=["n3", "iam"],
)

# Arritmia grave
add_note(
    front=(
        N3 +
        '<div class="header">Arritmia grave inestable</div>'
        '<div>Por cada mecanismo, &iquest;que signo o sintoma produce?</div>' +
        items([
            "Ritmo rapido / irregular percibido",
            "Bajo flujo cerebral transitorio",
            "Corazon con mayor demanda o baja perfusion coronaria",
            "Ritmo no genera gasto efectivo",
            "Hipoperfusion cerebral sostenida",
            "Pocas contracciones por minuto",
            "No hay tiempo de llenado ventricular",
            "Activacion electrica desorganizada",
        ])
    ),
    back=items([
        "Palpitaciones",
        "Mareo / sincope",
        "Dolor toracico",
        "Hipotension",
        "Confusion",
        "Pulso muy lento (bradi)",
        "Pulso muy rapido sin pulsos llenos (taqui)",
        "Pulso irregular",
    ]),
    tags=["n3", "arritmia"],
)

# IC aguda
add_note(
    front=(
        N3 +
        '<div class="header">Insuficiencia cardiaca aguda</div>'
        '<div>Por cada mecanismo, &iquest;que signo o sintoma produce?</div>' +
        items([
            "Pulmon congestionado, peor intercambio gaseoso",
            "Al acostarse aumenta retorno venoso",
            "Liquido en intersticio / alveolos",
            "Alveolos con liquido intercambian peor O&#8322;",
            "Edema alveolar franco",
            "Presion venosa central elevada",
            "Congestion venosa + retencion renal de sodio / agua",
            "Congestion hepatica",
            "Bajo flujo renal activa retencion",
            "Bajo gasto avanzado",
        ])
    ),
    back=items([
        "Disnea",
        "Ortopnea / disnea paroxistica nocturna",
        "Estertores",
        "Saturacion baja",
        "Tos espumosa rosada",
        "Ingurgitacion yugular",
        "Edema periferico",
        "Hepatomegalia dolorosa",
        "Oliguria",
        "Hipotension, confusion, piel fria",
    ]),
    tags=["n3", "ic_aguda"],
)


# ============================================================
# NIVEL 4 — Escena clinica -> accion de manejo (3 cards)
# ============================================================
N4 = '<div class="nivel">NIVEL 4 — ESCENA &rarr; MANEJO</div>'

# IAM complicado
add_note(
    front=(
        N4 +
        '<div class="escena">Adulto con dolor toracico opresivo irradiado, diaforetico, palido, '
        'hipotenso, estertores bibasales, Sat 88%. Sospechas IAM complicado con shock cardiogenico.</div>'
        '<div>Para cada problema visualizado, &iquest;que accion tomas?</div>' +
        items([
            "Llega inestable e isquemico &mdash; necesitas mapa rapido y aviso a hemodinamia",
            "Hay que saber si es STEMI y que territorio",
            "Confirmar dano miocardico",
            "Si esta hipoxemico, la celula sufre mas",
            "El trombo coronario sigue creciendo",
            "Bomba danada + tuberia llena &mdash; no la inundes",
            "Si la presion sigue cayendo, el corazon no se perfunde a si mismo",
            "El tratamiento causal es abrir la arteria",
        ])
    ),
    back=items([
        "ABCDE + monitor con desfibrilador cerca + 2 vias IV",
        "ECG de 12 derivaciones &lt; 10 min",
        "Troponinas seriadas",
        "Oxigeno <b>solo si hipoxemia</b>",
        "AAS + segundo antiagregante segun protocolo",
        "<b>Evitar bolos de liquido</b> salvo IAM de VD",
        "Vasopresor / inotropico (noradrenalina &plusmn; dobutamina) si shock",
        "<b>Reperfusion urgente</b> (ICP primaria &lt;90 min; fibrinolisis si no disponible) + UCC / hemodinamia",
    ]),
    tags=["n4", "iam"],
)

# Arritmia grave
add_note(
    front=(
        N4 +
        '<div class="escena">Paciente con palpitaciones subitas, mareo, dolor toracico, '
        'TA 75/40, alteracion mental. Pulso 180 irregular (o 35 lento). Inestable.</div>'
        '<div>Para cada problema visualizado, &iquest;que accion tomas?</div>' +
        items([
            "Inestable &mdash; la pregunta clave es estable vs inestable",
            "Sin ECG no sabes que arritmia tratas",
            "Si la taqui no deja llenar el ventriculo, hay que resetear el ritmo ya",
            "Si late muy lento, hay que acelerarlo de inmediato",
            "Si la atropina no basta, necesitas un marcapasos",
            "Algunas arritmias son por electrolitos o farmacos",
            "Buscar causa subyacente reversible (isquemia, TEP, hiperK, intoxicacion)",
            "Manejo avanzado, no es para piso",
        ])
    ),
    back=items([
        "ABCDE + monitor + 2 vias IV + O&#8322; si hipoxemia",
        "ECG de 12 derivaciones + tira de ritmo",
        "<b>Taqui inestable &rarr; cardioversion sincronizada</b> (sedacion previa si consciente)",
        "<b>Bradi inestable &rarr; atropina 1 mg IV</b> (repetir hasta 3 mg)",
        "Si atropina falla &rarr; <b>marcapasos transcutaneo</b> o infusion de dopamina / adrenalina",
        "K, Mg, Ca, digoxinemia",
        "Troponina + buscar causa reversible",
        "UCC + cardiologia",
    ]),
    tags=["n4", "arritmia"],
)

# IC aguda
add_note(
    front=(
        N4 +
        '<div class="escena">Paciente disneico, ortopneico, con estertores bibasales, '
        'ingurgitacion yugular marcada, edema en miembros, Sat 84%, TA 90/60 y oliguria.</div>'
        '<div>Para cada problema visualizado, &iquest;que accion tomas?</div>' +
        items([
            "Llega congestivo y mal perfundido &mdash; necesitas mapa rapido",
            "Acostado, la sangre se le va al pulmon",
            "Esta hipoxemico por edema alveolar",
            "Si los alveolos estan colapsados, el trabajo respiratorio agota",
            "Hay volumen excesivo regresandose al pulmon",
            "Si la TA lo permite, baja precarga y poscarga",
            "&iquest;Hay IAM como causa de la descompensacion?",
            "Ver edema pulmonar y silueta cardiaca",
            "<b>No le des liquidos a ciegas &mdash; empeoras la congestion</b>",
            "Si la bomba ya no sostiene presion, necesita soporte",
        ])
    ),
    back=items([
        "ABCDE + monitor + 2 vias IV",
        "<b>Sentar al paciente</b> (piernas colgando)",
        "Oxigeno si Sat &lt; 90%",
        "<b>VMNI (CPAP / BiPAP)</b> si edema pulmonar grave",
        "<b>Furosemida IV</b> si sobrecarga",
        "<b>Nitratos IV</b> si TAS &gt; 110",
        "ECG + troponina",
        "Rx torax + BNP + eco a pie de cama",
        "Restriccion hidrica + balance estricto",
        "Inotropico (dobutamina) &plusmn; vasopresor si shock; UCI",
    ]),
    tags=["n4", "ic_aguda"],
)


# ============================================================
# Build
# ============================================================
def build():
    out_path = os.path.join(OUTPUT_DIR, "Patrones_Madre_Shock_3.apkg")
    genanki.Package(deck).write_to_file(out_path)
    print(f"OK: {out_path}  ({len(deck.notes)} notas)")


if __name__ == "__main__":
    build()
