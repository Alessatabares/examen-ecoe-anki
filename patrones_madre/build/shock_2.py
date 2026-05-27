"""Patron Madre: Shock 2 - Septico / Distributivo.

Segundo subdeck del patron madre "shock / mala perfusion".
Cubre la rama septica/distributiva (shock 1 = hipovolemico,
shock 3 = cardiogenico, shock 4 = obstructivo).

Formato de embudo Q&A en 4 niveles (ver patrones_madre/README.md):
- N1 (1 card): identificar el patron madre.
- N2 (6 cards): imagen mental -> nombre formal de la subcausa.
- N3 (6 cards): mecanismo fisiopatologico (imagen del fallo) -> signo clinico.
- N4 (6 cards): escena clinica + problemas visualizados -> acciones de manejo.

Subcausas: neumonia, pielonefritis, colangitis, peritonitis, endometritis, sepsis neonatal.
Total: 19 cards.
"""
import os
import genanki

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "output")
os.makedirs(OUTPUT_DIR, exist_ok=True)

MODEL_QA_ID = 1607392320  # reusable Q&A (mismo que shock_1 y gineco capa 5)
DECK_ID = 1135155371
DECK_NAME = "Patrones Madre::Shock 2"

CSS = """
.card {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  font-size: 19px; text-align: left; color: #1a1a1a;
  background-color: #fafafa; padding: 20px; line-height: 1.55;
}
.nivel {
  display: inline-block; padding: 4px 12px; margin-bottom: 14px;
  background: #991b1b; color: #fff; border-radius: 6px;
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

BASE_TAGS = ["patrones_madre", "ecoe", "shock_septico"]


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
        '<div>Choque donde lo que falla es <b>la distribucion del flujo</b>: '
        'los vasos se dilatan, fugan plasma al intersticio y la celula deja de usar bien el O&#8322;. '
        'La infeccion (u otra causa distributiva) es el disparador.</div>'
        '<div class="prompt">&iquest;Que tipo de shock es?</div>'
    ),
    back=(
        '<div class="respuesta">Shock septico / distributivo</div>'
        '<div class="metafora">Metafora: las tuberias se hicieron mangueras flojas y agujereadas por inflamacion. '
        'La sangre existe, pero los vasos estan dilatados, parte del liquido se fuga a tejidos y '
        'la distribucion se vuelve caotica.</div>'
        '<div class="metafora"><b>Frase madre:</b> sepsis = infeccion local que se volvio problema circulatorio sistemico. '
        'Manejo = antibiotico temprano + liquidos + control de foco.</div>'
    ),
    tags=["n1"],
)


# ============================================================
# NIVEL 2 — Imagen mental -> nombre formal (6 cards)
# ============================================================
N2 = '<div class="nivel">NIVEL 2 — IMAGEN MENTAL &rarr; NOMBRE</div>'

add_note(
    front=(
        N2 +
        '<div>Una esponja pulmonar que se llena de pus y liquido inflamatorio. '
        'El oxigeno entra peor y, al mismo tiempo, la infeccion activa inflamacion en todo el cuerpo.</div>'
        '<div class="prompt">&iquest;Que subcausa de shock septico es?</div>'
    ),
    back=(
        '<div class="respuesta">Sepsis por neumonia</div>'
    ),
    tags=["n2", "neumonia"],
)

add_note(
    front=(
        N2 +
        '<div>Una infeccion que subio desde la vejiga hasta un organo muy vascularizado. '
        'Como ese organo esta lleno de sangre, las bacterias saltan a la circulacion con facilidad.</div>'
        '<div class="prompt">&iquest;Que subcausa de shock septico es?</div>'
    ),
    back=(
        '<div class="respuesta">Pielonefritis complicada / urosepsis</div>'
    ),
    tags=["n2", "pielonefritis"],
)

add_note(
    front=(
        N2 +
        '<div>Una tuberia de drenaje tapada: la bilis se estanca, las bacterias proliferan '
        'bajo presion y terminan pasando a la sangre. Aparece ictericia porque la bilis no drena.</div>'
        '<div class="prompt">&iquest;Que subcausa de shock septico es?</div>'
    ),
    back=(
        '<div class="respuesta">Colangitis aguda</div>'
        '<div class="metafora">Triada de Charcot: fiebre + dolor HD + ictericia. '
        'Pentada de Reynolds: triada + hipotension + alteracion mental.</div>'
    ),
    tags=["n2", "colangitis"],
)

add_note(
    front=(
        N2 +
        '<div>Una alarma inflamatoria gigante se contamina con contenido intestinal, pus o bilis '
        '(perforacion, apendicitis rota, fuga). Toda la cavidad se inflama y se activa sepsis.</div>'
        '<div class="prompt">&iquest;Que subcausa de shock septico es?</div>'
    ),
    back=(
        '<div class="respuesta">Peritonitis / abdomen septico</div>'
    ),
    tags=["n2", "peritonitis"],
)

add_note(
    front=(
        N2 +
        '<div>Despues del parto el utero queda como una herida interna grande. '
        'Las bacterias ascienden, infectan endometrio y miometrio, y aparecen fiebre + loquios fetidos.</div>'
        '<div class="prompt">&iquest;Que subcausa de shock septico es?</div>'
    ),
    back=(
        '<div class="respuesta">Endometritis puerperal</div>'
    ),
    tags=["n2", "endometritis"],
)

add_note(
    front=(
        N2 +
        '<div>Una ciudad con defensas inmaduras. No siempre hace fiebre; su forma de avisar es '
        'dejar de comer, ponerse letargico, hipotermico o presentar dificultad respiratoria.</div>'
        '<div class="prompt">&iquest;Que subcausa de shock septico es?</div>'
    ),
    back=(
        '<div class="respuesta">Sepsis neonatal</div>'
    ),
    tags=["n2", "sepsis_neonatal"],
)


# ============================================================
# NIVEL 3 — Mecanismo fisiopatologico (imagen del fallo) -> signo (6 cards)
# ============================================================
N3 = '<div class="nivel">NIVEL 3 — MECANISMO &rarr; SIGNO</div>'

# Neumonia
add_note(
    front=(
        N3 +
        '<div class="header">Sepsis por neumonia</div>'
        '<div>Por cada imagen del fallo, &iquest;que signo o sintoma produce?</div>' +
        items([
            "Alveolos llenos de pus y liquido inflamatorio",
            "Aire intentando entrar a alveolos ocupados",
            "Hipotalamo bombardeado por citocinas",
            "Bulbo detecta hipoxemia y acidosis",
            "Pulmon no intercambia O&#8322; por el exudado",
            "Citocinas dilatan vasos sistemicos",
            "Cerebro mal perfundido + hipoxemico",
        ])
    ),
    back=items([
        "Tos + expectoracion purulenta",
        "Crepitantes",
        "Fiebre + escalofrios",
        "Taquipnea",
        "Saturacion baja",
        "Hipotension + taquicardia",
        "Confusion",
    ]),
    tags=["n3", "neumonia"],
)

# Pielonefritis
add_note(
    front=(
        N3 +
        '<div class="header">Pielonefritis / urosepsis</div>'
        '<div>Por cada imagen del fallo, &iquest;que signo o sintoma produce?</div>' +
        items([
            "Inflamacion de vejiga y uretra",
            "Capsula renal distendida e inflamada",
            "Rinon inflamado al golpearlo",
            "Bacterias liberadas a sangre + pirogenos",
            "Estimulo autonomico inflamatorio",
            "Vasodilatacion septica + hipoperfusion",
        ])
    ),
    back=items([
        "Disuria, urgencia, polaquiuria",
        "Dolor lumbar",
        "Punopercusion positiva",
        "Fiebre alta + escalofrios",
        "Nausea / vomito",
        "Hipotension + confusion",
    ]),
    tags=["n3", "pielonefritis"],
)

# Colangitis
add_note(
    front=(
        N3 +
        '<div class="header">Colangitis aguda</div>'
        '<div>Por cada imagen del fallo, &iquest;que signo o sintoma produce?</div>' +
        items([
            "Via biliar distendida por obstruccion",
            "Bilis no drena al intestino y se acumula en sangre",
            "Bacterias proliferan en bilis estancada &rarr; pirogenos",
            "Vasodilatacion septica",
            "Hipoperfusion cerebral",
        ])
    ),
    back=items([
        "Dolor en hipocondrio derecho",
        "Ictericia",
        "Fiebre + escalofrios",
        "Hipotension",
        "Alteracion mental (pentada de Reynolds)",
    ]),
    tags=["n3", "colangitis"],
)

# Peritonitis
add_note(
    front=(
        N3 +
        '<div class="header">Peritonitis / abdomen septico</div>'
        '<div>Por cada imagen del fallo, &iquest;que signo o sintoma produce?</div>' +
        items([
            "Peritoneo inflamado, duele al moverlo",
            "Contraccion refleja para proteger",
            "Intestino inflamado se paraliza",
            "Citocinas peritoneales sistemicas",
            "Fuga capilar al tercer espacio abdominal",
        ])
    ),
    back=items([
        "Dolor intenso + rebote / defensa",
        "Abdomen rigido (\"en tabla\")",
        "Ileo: distension + vomito + ausencia de ruidos",
        "Fiebre + taquicardia",
        "Hipotension",
    ]),
    tags=["n3", "peritonitis"],
)

# Endometritis
add_note(
    front=(
        N3 +
        '<div class="header">Endometritis puerperal</div>'
        '<div>Por cada imagen del fallo, &iquest;que signo o sintoma produce?</div>' +
        items([
            "Endometrio infectado posparto",
            "Miometrio inflamado, no contrae bien",
            "Flora mixta anaerobia proliferando",
            "Citocinas sistemicas",
            "Sepsis con vasodilatacion",
        ])
    ),
    back=items([
        "Dolor uterino a la palpacion",
        "Utero subinvolucionado",
        "Loquios fetidos",
        "Fiebre posparto",
        "Taquicardia + hipotension",
    ]),
    tags=["n3", "endometritis"],
)

# Sepsis neonatal
add_note(
    front=(
        N3 +
        '<div class="header">Sepsis neonatal</div>'
        '<div>Por cada imagen del fallo, &iquest;que signo o sintoma produce?</div>' +
        items([
            "Termorregulacion inmadura ante infeccion",
            "Cerebro inflamado / hipoperfundido",
            "Bajo gasto y encefalopatia &rarr; no traga",
            "Acidosis metabolica + sepsis pulmonar",
            "Inmadurez del centro respiratorio + infeccion",
            "Mala perfusion periferica",
        ])
    ),
    back=items([
        "Hipotermia (a veces fiebre)",
        "Letargo o irritabilidad",
        "Mala alimentacion / rechazo al alimento",
        "Dificultad respiratoria",
        "Apneas",
        "Llenado capilar lento, piel moteada",
    ]),
    tags=["n3", "sepsis_neonatal"],
)


# ============================================================
# NIVEL 4 — Escena clinica + problemas -> acciones (6 cards)
# ============================================================
N4 = '<div class="nivel">NIVEL 4 — ESCENA &rarr; MANEJO</div>'

# Neumonia
add_note(
    front=(
        N4 +
        '<div class="escena">Adulto febril, tos productiva, disnea, taquipnea, Sat 86%, '
        'hipotenso y confuso. Sospechas sepsis por neumonia.</div>'
        '<div>Para cada problema visualizado, &iquest;que accion tomas?</div>' +
        items([
            "Llega inestable y septico &mdash; necesitas mapa rapido",
            "Alveolos ocupados &mdash; no oxigena",
            "Hay que saber que pulmon y cuanto esta tomado",
            "La infeccion es el disparador de toda la cascada",
            "Antes de empezar antibiotico, captura el bicho",
            "Vasodilatacion septica &mdash; presion cayendo",
            "Quieres medir si la celula ya sufre",
        ])
    ),
    back=items([
        "ABCDE + monitorizacion + 2 vias IV",
        "Oxigeno (mascarilla / VMNI / IOT si falla)",
        "Rx torax + gasometria",
        "<b>Ceftriaxona + azitromicina</b> IV temprano",
        "Hemocultivos + cultivo de esputo (si no retrasan)",
        "Cristaloides IV",
        "Lactato + BH",
    ]),
    tags=["n4", "neumonia"],
)

# Pielonefritis
add_note(
    front=(
        N4 +
        '<div class="escena">Mujer joven, fiebre 39&deg;, dolor lumbar, punopercusion positiva, '
        'taquicardica e hipotensa.</div>'
        '<div>Para cada problema visualizado, &iquest;que accion tomas?</div>' +
        items([
            "Septica &mdash; estabilizacion inicial",
            "Necesitas confirmar foco urinario",
            "Hay que identificar el germen",
            "El rinon infectado puede pasar bacterias a sangre",
            "Vasodilatacion + posible deshidratacion",
            "&iquest;Y si ademas hay una piedra tapando arriba?",
            "Si hay obstruccion, el antibiotico solo no basta",
        ])
    ),
    back=items([
        "ABCDE + monitor + 2 vias IV",
        "EGO",
        "Urocultivo + hemocultivos",
        "<b>Ceftriaxona IV</b> empirica",
        "Cristaloides IV",
        "USG / TAC si dolor colico o mala evolucion",
        "Urologia &rarr; drenaje urgente (control de foco)",
    ]),
    tags=["n4", "pielonefritis"],
)

# Colangitis
add_note(
    front=(
        N4 +
        '<div class="escena">Adulto con triada de Charcot (fiebre + dolor HD + ictericia), '
        'hipotenso y confuso (pentada de Reynolds).</div>'
        '<div>Para cada problema visualizado, &iquest;que accion tomas?</div>' +
        items([
            "Septico grave &mdash; estabilizacion primero",
            "Confirmar patron obstructivo biliar",
            "Ver donde esta el lito y cuanto dilatado esta el conducto",
            "Bacteriemia frecuente, quiero el germen",
            "Bilis estancada con bacterias &mdash; apagar el incendio",
            "Vasodilatacion septica + posible ayuno",
            "Mientras la tuberia siga tapada, la infeccion sigue bajo presion",
        ])
    ),
    back=items([
        "ABCDE + ayuno + monitor + 2 vias IV",
        "PFH + bilirrubinas + BH",
        "USG hepatobiliar (&plusmn; colangio-RM)",
        "Hemocultivos",
        "<b>Piperacilina-tazobactam</b> IV",
        "Cristaloides IV",
        "CPRE / descompresion biliar urgente",
    ]),
    tags=["n4", "colangitis"],
)

# Peritonitis
add_note(
    front=(
        N4 +
        '<div class="escena">Abdomen en tabla, rebote positivo, fiebre, taquicardia, hipotension; '
        'sospecha de perforacion.</div>'
        '<div>Para cada problema visualizado, &iquest;que accion tomas?</div>' +
        items([
            "Abdomen agudo + sepsis &mdash; estabilizacion",
            "Intestino paralizado + vomito + posible quirofano",
            "Quiero localizar la fuga / perforacion / absceso",
            "Flora mixta (gram negativos + anaerobios)",
            "Tercer espacio abdominal &mdash; volumen efectivo bajo",
            "Dolor intenso",
            "Si va a cirugia, anticipa transfusion",
            "Antibiotico no cierra una perforacion",
        ])
    ),
    back=items([
        "ABCDE + 2 vias + monitor",
        "Ayuno + SNG",
        "TAC abdomen con contraste (si estable) &plusmn; Rx (aire libre)",
        "<b>Piperacilina-tazobactam</b> IV",
        "Cristaloides IV + lactato",
        "Analgesia IV",
        "BH, grupo y pruebas cruzadas",
        "Cirugia urgente &mdash; control de foco",
    ]),
    tags=["n4", "peritonitis"],
)

# Endometritis
add_note(
    front=(
        N4 +
        '<div class="escena">Puerpera al 3er dia, fiebre 38.8&deg;, utero doloroso, '
        'loquios fetidos, taquicardica.</div>'
        '<div>Para cada problema visualizado, &iquest;que accion tomas?</div>' +
        items([
            "Sepsis posparto &mdash; estabilizacion",
            "Confirmar respuesta inflamatoria",
            "Utero infectado polimicrobiano",
            "Vasodilatacion septica si avanza",
            "&iquest;Hay restos retenidos manteniendo el foco?",
            "Si hay restos, el antibiotico no basta",
            "Descartar otra fuente (IVU posparto)",
        ])
    ),
    back=items([
        "ABCDE + monitor + via IV",
        "BH + hemocultivos si fiebre alta",
        "<b>Clindamicina + gentamicina</b> IV",
        "Cristaloides si hipoperfusion",
        "USG pelvico",
        "Evacuacion / legrado uterino (control de foco)",
        "EGO + urocultivo",
    ]),
    tags=["n4", "endometritis"],
)

# Sepsis neonatal
add_note(
    front=(
        N4 +
        '<div class="escena">RN de 5 dias, no come, letargico, hipotermico (35.6&deg;), '
        'llenado capilar 4 segundos.</div>'
        '<div>Para cada problema visualizado, &iquest;que accion tomas?</div>' +
        items([
            "RN se descompensa rapido",
            "El frio consume glucosa y O&#8322; &mdash; empeora todo",
            "Hipoglucemia simula sepsis y dana neuronas",
            "Venas colapsadas &mdash; no esperes minutos buscando",
            "Captura el bicho antes de tratar (si no retrasa)",
            "Riesgo alto de bacteriemia + meningitis",
            "Posible meningitis coexistente",
            "Necesita perfusion, pero exceso de liquido dana",
            "Puede hacer apnea / dificultad respiratoria",
            "Manejo estrecho, no es para piso",
        ])
    ),
    back=items([
        "ABCDE",
        "Control termico (incubadora / contacto piel)",
        "Glucosa capilar + corregir si baja",
        "Acceso IV o intraoseo",
        "Hemocultivo + BH + PCR / procalcitonina",
        "<b>Ampicilina + gentamicina</b> IV urgente",
        "Puncion lumbar si estable",
        "Bolos pequenos de cristaloide + reevaluar",
        "Oxigeno / soporte ventilatorio",
        "UCIN",
    ]),
    tags=["n4", "sepsis_neonatal"],
)


# ============================================================
# Build
# ============================================================
def build():
    out_path = os.path.join(OUTPUT_DIR, "Patrones_Madre_Shock_2.apkg")
    genanki.Package(deck).write_to_file(out_path)
    print(f"OK: {out_path}  ({len(deck.notes)} notas)")


if __name__ == "__main__":
    build()
