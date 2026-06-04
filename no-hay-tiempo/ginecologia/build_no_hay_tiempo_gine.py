"""Generador de 3 subdecks Anki — "No hay tiempo" / Ginecología (ECOE).

Filosofía: cuando queda poco para el examen, no estudias 25 manejos sueltos.
Estudias PRIMERO los 7 ejes de decisión (andamiaje) y luego los manejos
colgados de ese árbol, verbalizados como se hablan en la estación.

Subdecks:
  1 - Ejes (madre)          ->  7 cartas (la pregunta que decide el manejo)
  2 - Manejos trampa (core) -> 18 cartas (lo más puntuable, formato hablado)
  3 - Menos preguntados     -> 17 cartas (segunda pasada si sobra tiempo)

Formato carta de manejo (campo Back, 3 bloques):
  VERBALIZO  -> al sinodal, técnico (qué indico/solicito)
  CONSEJERÍA -> a la paciente, lenguaje llano + empatía
  CIERRE     -> seguridad: datos de alarma + seguimiento + pareja/lactancia

Guía: GPC mexicanas + ACOG + Williams (misma base que las Capas 1-6).
"""
import os
import genanki

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "output")
os.makedirs(OUTPUT_DIR, exist_ok=True)

MODEL_QA_ID = 1990002001

DECK_ID_EJES = 1990001001
DECK_ID_CORE = 1990001002
DECK_ID_MENOS = 1990001003

DECK_NAME_EJES = "No hay tiempo::Ginecologia::1 - Ejes (madre)"
DECK_NAME_CORE = "No hay tiempo::Ginecologia::2 - Manejos trampa (core)"
DECK_NAME_MENOS = "No hay tiempo::Ginecologia::3 - Menos preguntados"

CSS_BASE = """
.card {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  font-size: 19px; text-align: left; color: #1a1a1a;
  background-color: #fafafa; padding: 20px; line-height: 1.55;
}
.caso { font-size: 21px; font-weight: 700; color: #1e3a8a; }
.eje-q { font-size: 20px; font-weight: 700; color: #1e3a8a; }
#extra { margin-top: 16px; border: none; border-top: 1px solid #d4d4d4; padding-top: 12px; }

.bloque { display: block; margin: 12px 0; padding: 10px 14px; border-radius: 8px; }
.verbalizo { background: #eef2ff; border-left: 4px solid #1e3a8a; }
.consejeria { background: #ecfdf5; border-left: 4px solid #047857; }
.cierre { background: #fff7ed; border-left: 4px solid #b45309; }
.lab { display: block; font-size: 13px; font-weight: 700; letter-spacing: .5px;
       text-transform: uppercase; margin-bottom: 4px; }
.verbalizo .lab { color: #1e3a8a; }
.consejeria .lab { color: #047857; }
.cierre .lab { color: #b45309; }
.consejeria em, .consejeria i { color: #065f46; font-style: italic; }

.regla { background: #eef2ff; border-left: 4px solid #1e3a8a; }
.bif { background: #f5f3ff; border-left: 4px solid #6d28d9; }
.trampa { background: #fef2f2; border-left: 4px solid #b91c1c; }
.regla .lab { color: #1e3a8a; }
.bif .lab { color: #6d28d9; }
.trampa .lab { color: #b91c1c; }
b { color: #111; }
"""

model_qa = genanki.Model(
    MODEL_QA_ID,
    "No Hay Tiempo QA",
    fields=[{"name": "Front"}, {"name": "Back"}],
    templates=[{
        "name": "QA",
        "qfmt": "{{Front}}",
        "afmt": '{{Front}}<hr id="extra">{{Back}}',
    }],
    css=CSS_BASE,
)

deck_ejes = genanki.Deck(DECK_ID_EJES, DECK_NAME_EJES)
deck_core = genanki.Deck(DECK_ID_CORE, DECK_NAME_CORE)
deck_menos = genanki.Deck(DECK_ID_MENOS, DECK_NAME_MENOS)

BASE_TAGS = ["gineco", "ecoe", "no_hay_tiempo"]


def add(deck, front, back, tags):
    note = genanki.Note(model=model_qa, fields=[front, back], tags=BASE_TAGS + tags)
    deck.add_note(note)


def caso(txt):
    return f'<span class="caso">{txt}</span>'


def manejo(verbalizo, consejeria, cierre):
    """Arma el Back de 3 bloques de un manejo hablado."""
    return (
        f'<span class="bloque verbalizo"><span class="lab">Verbalizo (al sinodal)</span>{verbalizo}</span>'
        f'<span class="bloque consejeria"><span class="lab">Consejeria (a la paciente)</span><em>{consejeria}</em></span>'
        f'<span class="bloque cierre"><span class="lab">Cierre (seguridad)</span><em>{cierre}</em></span>'
    )


def eje(regla, bifurcacion, trampa):
    return (
        f'<span class="bloque regla"><span class="lab">Regla madre</span>{regla}</span>'
        f'<span class="bloque bif"><span class="lab">Bifurcacion</span>{bifurcacion}</span>'
        f'<span class="bloque trampa"><span class="lab">Trampa ECOE</span>{trampa}</span>'
    )


# ============================================================
# SUBDECK 1 - EJES (madre): 7 cartas
# ============================================================
EJE = ["eje"]

add(deck_ejes,
    caso("EJE 1 — &iquest;Es ITS de transmision real? &rarr; decide si tratas a la pareja"),
    eje(
        "Imagen: dos cuerpos vs uno. Si el bicho salta de persona a persona &rarr; "
        "<b>pareja + abstinencia</b>. Si nace de su propia flora &rarr; <b>solo ella</b>.",
        "<b>Tratar pareja (ITS real):</b> sifilis, tricomoniasis, chancroide, cervicitis (GC/clamidia), EIP.<br>"
        "<b>NO tratar pareja (disbiosis propia):</b> vaginosis bacteriana, candidiasis.",
        "VB y candida <b>NO</b> se tratan a la pareja: ese es el discriminador que buscan. "
        "En embarazo: candida/VB <b>solo topico</b>; sifilis alergica &rarr; <b>desensibilizar</b>.",
    ),
    EJE + ["its"])

add(deck_ejes,
    caso("EJE 2 — Virus: no se cura, se controla"),
    eje(
        "Imagen: un bicho que se queda a vivir. No erradicas: apagas brotes y reduces transmision.",
        "<b>Herpes:</b> aciclovir. Primario 7-10 d &rarr; recurrente 5 d &rarr; <b>supresor diario si &ge;6 brotes/ano</b>.<br>"
        "<b>VPH:</b> no hay antiviral. Verrugas &rarr; topico/crioterapia; lesion de cuello &rarr; se trata la LESION (Eje 3).",
        "El antiviral del herpes <b>no cura</b>: el virus queda latente. Contagia incluso sin lesiones &rarr; preservativo.",
    ),
    EJE + ["herpes", "vph"])

add(deck_ejes,
    caso("EJE 3 — Lesion de cuello: el GRADO decide vigilar / cortar / referir"),
    eje(
        "Imagen: una escalera. Cada escalon sube la agresividad de la conducta.",
        "<b>NIC 1</b> &rarr; vigilar (regresa hasta 60%).<br>"
        "<b>NIC 2-3</b> &rarr; escindir: <b>cono LEEP</b>.<br>"
        "<b>Ca invasor</b> &rarr; <b>referir a oncologia</b> (estadificacion FIGO).",
        "Lo unico que TU manejas es NIC. De ca invasor la respuesta correcta es <b>&laquo;refiero&raquo;</b>, "
        "no inventar quimio. Los demas Ca (endometrio, ovario) tambien terminan en referencia.",
    ),
    EJE + ["nic", "cancer"])

add(deck_ejes,
    caso("EJE 4 — Mama: el patron decide observar / drenar / biopsiar"),
    eje(
        "Imagen: un semaforo sobre la mama. Patron benigno &rarr; observo; coleccion &rarr; dreno; "
        "patron sospechoso &rarr; biopsio.",
        "<b>Observar:</b> fibroadenoma joven &lt;3 cm, quiste simple.<br>"
        "<b>Biopsia core:</b> BI-RADS 4-5, Paget, telorrea patologica.<br>"
        "<b>Infeccion (mastitis/absceso):</b> dicloxacilina + vaciar + <b>NO suspender lactancia</b>; si hay coleccion, drenar.",
        "BI-RADS 4-5 &rarr; <b>biopsia core, nunca FNAC</b> como unico estudio. "
        "Mastitis y absceso son el mismo manejo; el absceso solo anade el drenaje.",
    ),
    EJE + ["mama"])

add(deck_ejes,
    caso("EJE 5 — &iquest;Desea embarazo? &rarr; bifurca TODA la gine funcional"),
    eje(
        "Imagen: una sola pregunta partiendo el arbol en dos. Es la key de interrogatorio mas rentable.",
        "<b>SOP:</b> desea &rarr; <b>letrozol</b>; no desea &rarr; ACO.<br>"
        "<b>Endometriosis:</b> desea/infertil &rarr; <b>laparoscopia</b>; dolor &rarr; AINE + ACO continuo.<br>"
        "<b>Miomatosis:</b> desea &rarr; <b>miomectomia</b>; paridad satisfecha &rarr; histerectomia.<br>"
        "<b>Adenomiosis:</b> sintomatica &rarr; DIU-LNG; definitivo &rarr; histerectomia (unico curativo).",
        "SOP: el inductor de ovulacion es <b>letrozol</b>, ya NO citrato de clomifeno. Lo buscan siempre.",
    ),
    EJE + ["sop", "endometriosis", "miomatosis"])

add(deck_ejes,
    caso("EJE 6 — Drenar y dejar abierto a epitelizar"),
    eje(
        "Imagen: abrir una bolsa y coser los bordes para que no se vuelva a cerrar.",
        "<b>Absceso de Bartholino:</b> <b>cateter de Word</b> o marsupializacion. "
        "No basta con incidir (se recierra).",
        "Antibiotico <b>solo</b> si celulitis perilesional, inmunocompromiso o sospecha de ITS. "
        "El drenaje es el tratamiento, no el antibiotico.",
    ),
    EJE + ["bartholino"])

add(deck_ejes,
    caso("EJE 7 — Estrogeno-dependiente / estructural: ventana + topicos"),
    eje(
        "Imagen: una ventana de tiempo que se cierra, y problemas de &laquo;estructura&raquo; que se sostienen o se cortan.",
        "<b>Climaterio:</b> TRH si <b>&lt;60 anos o &lt;10 anos de menopausia</b>, sin contraindicaciones.<br>"
        "<b>Liquen escleroso:</b> <b>clobetasol</b> topico + vigilar (riesgo ca vulvar).<br>"
        "<b>Prolapso:</b> Kegel si leve &rarr; pesario &rarr; cirugia.<br>"
        "<b>Infertilidad:</b> primero ESTUDIO de pareja, no tratamiento a ciegas.",
        "TRH: con utero &rarr; estrogeno + progestina; sin utero &rarr; estrogeno solo. "
        "Contraindicada con Ca mama, ETV, EVC, IAM, sangrado sin dx o hepatopatia.",
    ),
    EJE + ["climaterio", "liquen", "prolapso", "infertilidad"])


# ============================================================
# SUBDECK 2 - MANEJOS TRAMPA (core): 18 cartas
# ============================================================
CORE = ["core"]

add(deck_core,
    caso("Sifilis temprana (primaria/secundaria/latente temprana)"),
    manejo(
        "Indico <b>penicilina G benzatinica 2.4 millones IM en dosis unica</b>. Solicito control "
        "serologico (VDRL/RPR) a los 3, 6 y 12 meses. Notifico y trato a la pareja y tamizo otras "
        "ITS (VIH, hepatitis B y C). Si alergica: doxiciclina 100 mg c/12 h 14 d; si embarazada alergica, "
        "<b>desensibilizo</b> y doy penicilina.",
        "Su prueba confirma una sifilis en etapa temprana. La buena noticia es que se cura por completo "
        "con una sola inyeccion. Es muy importante que su pareja tambien reciba tratamiento aunque no "
        "tenga sintomas; si no, se reinfectan entre ustedes.",
        "Puede tener fiebre o malestar en las primeras horas: es una reaccion esperada, no alergia. "
        "Evite relaciones hasta una semana despues de que ambos esten tratados. La cito para repetir el examen de sangre.",
    ),
    CORE + ["its", "sifilis"])

add(deck_core,
    caso("Candidiasis vulvovaginal no complicada"),
    manejo(
        "Indico <b>fluconazol 150 mg VO dosis unica</b> (o clotrimazol vaginal 7 d). "
        "<b>No trato a la pareja</b> por no ser ITS. En embarazo: <b>solo topico</b> (clotrimazol/miconazol).",
        "Es una infeccion por un hongo que vive normalmente en la zona y se sobrecrecio; no es de "
        "transmision sexual, asi que su pareja no necesita tratamiento. Con una sola pastilla mejora.",
        "Para que no vuelva: ropa interior de algodon, evitar duchas vaginales y jabones perfumados. "
        "Si le pasa mas de 3-4 veces al ano, vuelva para estudiar por que se repite.",
    ),
    CORE + ["candidiasis"])

add(deck_core,
    caso("Tricomoniasis"),
    manejo(
        "Indico <b>metronidazol 2 g VO dosis unica</b> (o 500 mg c/12 h 7 d). "
        "<b>Trato a la pareja</b> y abstinencia 7 dias. Tamizo otras ITS.",
        "Es una infeccion de transmision sexual por un parasito. Su pareja debe tratarse al mismo tiempo "
        "aunque no tenga sintomas, o se la vuelve a pasar.",
        "Nada de alcohol durante el tratamiento y hasta 24-48 h despues (da nauseas y vomito con el metronidazol). "
        "Eviten relaciones por una semana hasta que ambos terminen.",
    ),
    CORE + ["its", "tricomoniasis"])

add(deck_core,
    caso("EIP ambulatoria (leve-moderada)"),
    manejo(
        "Indico <b>ceftriaxona 500 mg IM dosis unica + doxiciclina 100 mg c/12 h 14 d + "
        "metronidazol 500 mg c/12 h 14 d</b>. Hospitalizo si: embarazo, fiebre alta, intolerancia oral, "
        "absceso tubo-ovarico o no mejora en 72 h.",
        "Tiene una infeccion que subio al utero y las trompas. Es importante tratarla bien para proteger "
        "su fertilidad. Debe completar los 14 dias de antibiotico aunque se sienta mejor antes.",
        "Su pareja tambien necesita tratamiento. Si en 72 horas no mejora, o aparece fiebre alta o dolor "
        "intenso, vuelva: puede necesitar hospitalizacion. El DIU se retira solo si no mejora.",
    ),
    CORE + ["its", "eip"])

add(deck_core,
    caso("Herpes genital (primario y recurrente)"),
    manejo(
        "<b>Primario:</b> aciclovir 400 mg c/8 h 7-10 d + analgesia + lidocaina topica. "
        "<b>Recurrente:</b> aciclovir 800 mg c/12 h 5 d. <b>Supresor</b> diario (400 mg c/12 h) si &ge;6 brotes/ano.",
        "Tiene herpes genital. Sere honesta: el medicamento controla este brote y lo acorta, pero el virus "
        "se queda en el cuerpo y puede dar brotes futuros, generalmente mas leves. Es muy frecuente, no es para avergonzarse.",
        "Puede contagiar incluso sin heridas visibles, por eso el preservativo importa. "
        "Si los brotes se vuelven muy frecuentes (mas de seis al ano) hay tratamiento diario que los previene.",
    ),
    CORE + ["its", "herpes"])

add(deck_core,
    caso("NIC 1 confirmado por biopsia"),
    manejo(
        "Es lesion de bajo grado con alta regresion espontanea (hasta 60%). Indico <b>vigilancia con "
        "citologia/colposcopia cada 6-12 meses</b>, sin tratamiento ablativo inicial. Trato solo si persiste &gt;2 anos o progresa.",
        "El resultado muestra una lesion de BAJO grado en el cuello de la matriz. Entiendo que asusta, pero "
        "esto NO es cancer y en la mayoria de las mujeres el cuerpo lo resuelve solo. Por eso lo mas seguro "
        "es vigilarlo de cerca en vez de un procedimiento ahora.",
        "Es clave que no falte a sus controles cada 6 meses: ahi confirmamos que esta desapareciendo. "
        "Si necesita algo entre controles, vuelva.",
    ),
    CORE + ["nic"])

add(deck_core,
    caso("NIC 2-3 confirmado"),
    manejo(
        "Indico <b>tratamiento escisional: cono LEEP/LLETZ</b> (de eleccion). Alternativa ablativa "
        "(crio/laser) solo si la lesion es totalmente visible. Control con co-test posterior.",
        "Es una lesion de ALTO grado: todavia no es cancer, pero tiene mas riesgo de progresar, asi que "
        "esta vez si conviene tratarla. Se hace un corte pequeno del cuello de la matriz que quita la lesion "
        "y permite analizarla.",
        "Puede tener un poco de sangrado o flujo unos dias. Importante para futuros embarazos saber que se "
        "hizo este procedimiento. Seguira en controles para confirmar que quedo limpio.",
    ),
    CORE + ["nic"])

add(deck_core,
    caso("Ca cervix invasor"),
    manejo(
        "<b>Refiero a oncologia ginecologica</b> para estadificacion FIGO y tratamiento (Wertheim, "
        "RT-QT concomitante o ambos segun etapa). No inicio quimio yo.",
        "Los estudios muestran un cancer de cuello de matriz. Voy a referirla con el equipo de oncologia, "
        "que son los especialistas que definiran el mejor tratamiento segun la etapa. No esta sola en esto, "
        "la acompano en el proceso.",
        "La referencia es prioritaria; me aseguro de que tenga la cita y los estudios completos. "
        "Cualquier sangrado abundante o dolor, consulte sin esperar.",
    ),
    CORE + ["cancer_cervix"])

add(deck_core,
    caso("Mama con BI-RADS 4 o 5"),
    manejo(
        "Indico <b>biopsia con aguja gruesa (core) guiada por imagen</b> &rarr; histologia. "
        "Si maligno, refiero a oncologia para etapa clinica/imagen y tratamiento multimodal. "
        "<b>No</b> uso FNAC como unico estudio.",
        "La mamografia muestra un hallazgo que necesitamos analizar. Para saber con certeza que es, hay que "
        "tomar una muestra con una aguja, guiada por imagen. Es un procedimiento sencillo, con anestesia local.",
        "El resultado tarda unos dias; la cito para darselo en persona. Que sea sospechoso en imagen no "
        "significa que sea cancer; por eso confirmamos con la biopsia antes de decidir nada.",
    ),
    CORE + ["mama", "birads"])

add(deck_core,
    caso("Mastitis puerperal"),
    manejo(
        "Indico <b>dicloxacilina 500 mg c/6 h 10-14 d</b> (o cefalexina) + analgesia + compresas tibias + "
        "<b>vaciamiento mamario continuo</b>. <b>NO suspender lactancia</b> (es protectora).",
        "Tiene una infeccion en el pecho por la lactancia. Se que duele y da miedo seguir, pero es al reves: "
        "tiene que seguir dando pecho o extraer leche de ese lado. Vaciar el pecho es parte del tratamiento; "
        "si lo deja lleno, empeora. El antibiotico es seguro para el bebe.",
        "Si en 48-72 horas no mejora, o siente una bolita que fluctua, vuelva: podria haberse formado un "
        "absceso que hay que drenar.",
    ),
    CORE + ["mama", "mastitis"])

add(deck_core,
    caso("Absceso mamario"),
    manejo(
        "Indico <b>drenaje</b>: aspiracion con aguja guiada por USG (1ra eleccion en abscesos pequenos) o "
        "drenaje quirurgico si grande/multilocular. Anado dicloxacilina + analgesia y <b>continuo lactancia</b>.",
        "La infeccion formo una bolsa de pus que el antibiotico solo no resuelve; hay que drenarla. "
        "Se hace con una aguja guiada por ecografia, no siempre requiere cirugia. Puede seguir amamantando.",
        "Mantenga el pecho vaciado. Si vuelve a acumularse o aparece fiebre, regrese para revalorar el drenaje.",
    ),
    CORE + ["mama", "absceso"])

add(deck_core,
    caso("SOP con deseo de embarazo"),
    manejo(
        "1) <b>Perdida de peso 5-10%</b> (1ra linea no farmacologica). "
        "2) <b>Letrozol 2.5-5 mg/dia x 5 dias</b> para inducir ovulacion (NO citrato de clomifeno). "
        "3) Metformina si resistencia a insulina. 4) Gonadotropinas/reproduccion asistida si falla.",
        "Sus ovarios no liberan ovulos con regularidad, por eso cuesta el embarazo. Lo primero y mas "
        "poderoso es bajar algo de peso: incluso un 5-10% puede hacer que vuelva a ovular sola. Ademas le "
        "dare una pastilla, el letrozol, unos dias al mes para estimular la ovulacion.",
        "Vamos a monitorear si ovula. Es un proceso por pasos; si no logramos embarazo en unos meses, la "
        "derivo a fertilidad.",
    ),
    CORE + ["sop"])

add(deck_core,
    caso("SOP sin deseo de embarazo"),
    manejo(
        "Indico <b>ACO combinados</b> (regulan ciclo + manejan hiperandrogenismo) + estilo de vida + "
        "<b>metformina</b> si resistencia/intolerancia. Espironolactona para hirsutismo refractario "
        "(siempre con anticoncepcion).",
        "El sindrome de ovario poliquistico desordena sus reglas y sube hormonas masculinas (acne, vello). "
        "La pastilla anticonceptiva regula el ciclo y mejora esos sintomas, y el estilo de vida es la base "
        "del tratamiento.",
        "Reglas regulares tambien protegen su utero a largo plazo. La espironolactona para el vello nunca va "
        "sola sin anticoncepcion, porque no debe usarse buscando embarazo.",
    ),
    CORE + ["sop"])

add(deck_core,
    caso("Endometriosis sintomatica"),
    manejo(
        "1) AINEs + <b>ACO continuos</b> o progestinas (1ra linea). "
        "2) Analogos de GnRH con add-back si refractario. "
        "3) <b>Laparoscopia</b> con reseccion si falla manejo medico o hay infertilidad.",
        "El tejido del endometrio crece fuera del utero y por eso duele tanto, sobre todo con la regla. "
        "Empezamos con antiinflamatorios y anticonceptivo tomado de forma continua para que no menstrue y "
        "duela menos.",
        "Si el dolor no cede con el tratamiento, o si busca embarazo y no llega, valoramos una cirugia por "
        "laparoscopia. Cualquier dolor incapacitante, consulte.",
    ),
    CORE + ["endometriosis"])

add(deck_core,
    caso("Miomatosis uterina sintomatica"),
    manejo(
        "<b>Sangrado:</b> ACO/DIU-LNG, acido tranexamico, AINEs. <b>Masa/dolor:</b> anti-GnRH preoperatorio. "
        "<b>Quirurgico:</b> miomectomia si desea fertilidad, histerectomia si paridad satisfecha o sintomas severos.",
        "Tiene miomas, que son tumores benignos (no cancer) del musculo del utero. El tratamiento depende de "
        "si desea tener hijos: si los desea, podemos quitar solo los miomas; si ya no, la histerectomia "
        "resuelve definitivamente.",
        "Mientras decidimos, controlamos el sangrado para evitar anemia. Si sangra muy abundante o se marea, "
        "consulte y revisamos su hemoglobina.",
    ),
    CORE + ["miomatosis"])

add(deck_core,
    caso("Climaterio sintomatico"),
    manejo(
        "Candidata a <b>terapia hormonal</b> por <b>&lt;60 anos / &lt;10 anos de menopausia</b> sin "
        "contraindicaciones. Con utero: <b>estrogeno + progestina</b>; sin utero: estrogeno solo. "
        "Contraindicada: Ca mama, ETV, EVC, IAM, sangrado sin dx, hepatopatia grave.",
        "Los bochornos y molestias son por la baja de estrogenos de la menopausia. Como esta dentro de la "
        "ventana segura (menos de 60 anos y poco tiempo desde su ultima regla), los beneficios de las "
        "hormonas superan los riesgos. Le sumo una segunda hormona porque conserva su matriz, para protegerla.",
        "Cualquier sangrado nuevo me lo avisa de inmediato. Revisaremos cada ano si conviene continuar.",
    ),
    CORE + ["climaterio"])

add(deck_core,
    caso("Absceso de Bartholino"),
    manejo(
        "Indico <b>drenaje con cateter de Word</b> (se deja 4-6 semanas para epitelizar) o marsupializacion. "
        "Antibiotico <b>solo</b> si celulitis perilesional, inmunocompromiso o sospecha de ITS.",
        "Tiene un absceso en una glandula de la entrada vaginal. Hay que drenarlo; ademas se deja un pequeno "
        "cateter unas semanas para que el conducto quede abierto y no se vuelva a tapar. Si solo lo abrieramos, "
        "se cerraria y volveria.",
        "Puede tener molestia y algo de secrecion mientras esta el cateter, es normal. Si vuelve fiebre o "
        "dolor intenso, consulte.",
    ),
    CORE + ["bartholino"])

add(deck_core,
    caso("Liquen escleroso vulvar"),
    manejo(
        "Indico <b>corticoide topico ultrapotente: clobetasol 0.05%</b> (descenso gradual tras control). "
        "Vigilancia periodica por <b>riesgo de carcinoma vulvar</b>; biopsio zonas sospechosas o que no responden.",
        "Es una enfermedad cronica de la piel de la vulva que da picazon, ardor y aclaramiento. No es "
        "contagiosa ni es cancer, pero requiere control. La crema con corticoide potente calma los sintomas "
        "y frena el dano de la piel.",
        "Use la crema como le indico, sin abusar. Revisiones periodicas son importantes porque a largo plazo "
        "hay un pequeno riesgo de cancer en esa piel; cualquier herida o bulto que no sane, avise.",
    ),
    CORE + ["liquen"])


# ============================================================
# SUBDECK 3 - MENOS PREGUNTADOS: 17 cartas
# ============================================================
MENOS = ["menos_preguntado"]

add(deck_menos,
    caso("Sifilis latente tardia o de duracion desconocida"),
    manejo(
        "Indico <b>penicilina G benzatinica 2.4 millones IM SEMANAL x 3 dosis</b> (total 7.2 millones). "
        "Seguimiento serologico. Si alergica no embarazada: doxiciclina 28 dias.",
        "Su sifilis lleva mas tiempo del que podemos precisar, asi que el tratamiento es el mismo "
        "medicamento pero en tres inyecciones, una por semana. Es importante completar las tres.",
        "Si falta una dosis con mas de un par de dias de retraso, reiniciamos el esquema. Controlamos con "
        "examen de sangre que los titulos bajen.",
    ),
    MENOS + ["its", "sifilis"])

add(deck_menos,
    caso("Chancroide (Haemophilus ducreyi)"),
    manejo(
        "Indico <b>azitromicina 1 g VO dosis unica</b> (o ceftriaxona 250 mg IM unica, o ciprofloxacino). "
        "Trato a la pareja, tamizo otras ITS (sobre todo VIH) y aspiro bubones fluctuantes.",
        "Es una ulcera genital dolorosa de transmision sexual. Se cura con una sola dosis de antibiotico. "
        "Su pareja debe tratarse tambien.",
        "Conviene hacer prueba de VIH, porque estas ulceras facilitan su contagio. Eviten relaciones hasta "
        "completar y que cicatrice.",
    ),
    MENOS + ["its", "chancroide"])

add(deck_menos,
    caso("VPH: verrugas genitales (condilomas)"),
    manejo(
        "Indico tratamiento de la lesion: <b>imiquimod</b> o podofilotoxina topicos (autoaplicados) o "
        "<b>crioterapia</b>/acido tricloroacetico en consulta. No hay antiviral. Recomiendo <b>vacuna</b> como prevencion.",
        "Son verrugas causadas por el virus del papiloma. Tratamos las verrugas visibles, pero el virus "
        "puede seguir, asi que pueden reaparecer y a veces hay que repetir. No es lo mismo que el cancer de cuello.",
        "Use preservativo (reduce pero no elimina el contagio). Mantenga su citologia al dia. La vacuna "
        "protege contra otros tipos del virus.",
    ),
    MENOS + ["its", "vph"])

add(deck_menos,
    caso("Vaginosis bacteriana"),
    manejo(
        "Indico <b>metronidazol 500 mg VO c/12 h 7 d</b> (o gel vaginal 0.75% 5 d, o clindamicina crema 2% 7 d). "
        "<b>NO trato a la pareja</b>.",
        "Es un desbalance de las bacterias normales de la vagina, no una infeccion de transmision sexual; "
        "por eso su pareja no necesita tratamiento. El olor a pescado y el flujo gris mejoran con el antibiotico.",
        "Evite duchas vaginales y jabones perfumados, que empeoran el desbalance. Nada de alcohol con el "
        "metronidazol. Si se repite mucho, la reviso.",
    ),
    MENOS + ["vaginosis"])

add(deck_menos,
    caso("Cervicitis (gonococo + clamidia)"),
    manejo(
        "Trato empiricamente ambos: <b>ceftriaxona 500 mg IM dosis unica + doxiciclina 100 mg c/12 h 7 d</b> "
        "(azitromicina 1 g si embarazo). Trato pareja, abstinencia 7 d y tamizo otras ITS.",
        "Tiene una inflamacion del cuello de la matriz por una infeccion de transmision sexual. Tratamos "
        "las dos bacterias mas frecuentes a la vez. Su pareja tambien debe tratarse.",
        "Eviten relaciones por una semana hasta terminar ambos. Conviene prueba de VIH y otras ITS. "
        "Si aparece dolor pelvico o fiebre, podria haber subido a EIP: vuelva.",
    ),
    MENOS + ["its", "cervicitis"])

add(deck_menos,
    caso("Tamizaje cervical: inicio e intervalos"),
    manejo(
        "<b>Citologia desde los 21 anos c/3 anos</b>. <b>25-30 a 65 anos: co-test (citologia + VPH) c/5 anos</b> "
        "o citologia sola c/3 anos. Suspendo a los 65 si tamizaje previo negativo adecuado.",
        "El Papanicolaou busca cambios en el cuello de la matriz antes de que se vuelvan un problema. No hace "
        "falta hacerlo cada ano: con el esquema indicado es suficiente y evita procedimientos innecesarios.",
        "Aunque este vacunada contra el VPH, debe seguir tamizandose. Le anoto su proxima fecha de control.",
    ),
    MENOS + ["tamizaje"])

add(deck_menos,
    caso("Papanicolaou anormal: conducta"),
    manejo(
        "<b>ASC-US:</b> prueba de VPH refleja (si + &rarr; colposcopia) o repetir citologia. "
        "<b>LSIL / ASC-H / HSIL:</b> <b>colposcopia + biopsia dirigida</b>. AGC: colposcopia + estudio endometrial.",
        "Su citologia salio alterada. No significa cancer; significa que debemos mirar el cuello de la matriz "
        "mas de cerca con un aparato (colposcopia) y, si hace falta, tomar una pequena muestra.",
        "La colposcopia es ambulatoria y bien tolerada. Con el resultado decidimos si solo vigilar o tratar. "
        "Le agendo la cita.",
    ),
    MENOS + ["papanicolau", "nic"])

add(deck_menos,
    caso("Cancer de endometrio"),
    manejo(
        "Toda <b>metrorragia posmenopausica</b> obliga a descartarlo: USG transvaginal + <b>biopsia "
        "endometrial</b>. Confirmado: <b>histerectomia total + salpingooforectomia bilateral</b> con "
        "estadificacion quirurgica &plusmn; linfadenectomia. Refiero a oncologia.",
        "El sangrado despues de la menopausia siempre hay que estudiarlo. Tomamos una muestra del "
        "endometrio. Si confirma cancer, el tratamiento principal es una cirugia que quita utero y ovarios, "
        "y suele tener buen pronostico cuando se detecta temprano.",
        "Cualquier sangrado posmenopausico, por minimo que sea, debe consultarse: es el sintoma de alarma clave.",
    ),
    MENOS + ["cancer_endometrio"])

add(deck_menos,
    caso("Cancer de ovario"),
    manejo(
        "Sospecha por masa anexial + ascitis + <b>CA-125</b> elevado. <b>Refiero a oncologia ginecologica</b> "
        "para <b>cirugia de citorreduccion + estadificacion</b> y quimioterapia (platino + taxano). "
        "No biopsio percutaneo una masa potencialmente maligna.",
        "Hay una masa en el ovario con caracteristicas que obligan a descartar cancer. La derivo con "
        "oncologia ginecologica: el diagnostico y el tratamiento se hacen en la misma cirugia. La acompano en el proceso.",
        "Es un cancer que suele dar sintomas vagos (hinchazon, saciedad temprana), por eso es importante no "
        "retrasar la valoracion. Le aseguro la referencia prioritaria.",
    ),
    MENOS + ["cancer_ovario"])

add(deck_menos,
    caso("Fibroadenoma (mujer joven, &lt;2-3 cm)"),
    manejo(
        "Indico <b>observacion con USG de control en 6 meses</b>. Escision si: crece &gt;20% en 6 meses, "
        "&gt;3 cm, sintomatico, diagnostico incierto o preferencia de la paciente.",
        "Es un nodulo benigno muy frecuente en mujeres jovenes, no es cancer y no aumenta el riesgo de "
        "tenerlo. Lo mas seguro es vigilarlo con una ecografia de control, sin operar.",
        "Si nota que crece rapido, duele o cambia, vuelva antes del control. Si usted prefiere quitarlo o el "
        "diagnostico no es claro, lo valoramos.",
    ),
    MENOS + ["mama", "fibroadenoma"])

add(deck_menos,
    caso("Quiste mamario simple"),
    manejo(
        "Quiste simple en USG (anecoico, pared fina): <b>benigno, no requiere tratamiento</b>. "
        "Aspiro solo si es sintomatico/doloroso. Si el liquido es hematico o queda masa residual: estudio citologico/biopsia.",
        "Es una bolsita con liquido, completamente benigna y muy comun. Si no le molesta, no hay que hacer "
        "nada. Si duele, podemos vaciarla con una aguja y la molestia cede.",
        "Si vuelve a llenarse y molestar, se puede repetir la aspiracion. Si el liquido saliera con sangre, "
        "lo estudiamos mas a fondo.",
    ),
    MENOS + ["mama", "quiste"])

add(deck_menos,
    caso("Enfermedad de Paget del pezon"),
    manejo(
        "Eccema/erosion cronica del pezon que no responde a topicos: indico <b>biopsia de piel del pezon</b> + "
        "<b>mamografia bilateral</b>. <b>Casi siempre hay carcinoma subyacente</b> (in situ o invasor) &rarr; "
        "manejo oncologico segun hallazgos.",
        "Esa lesion del pezon que no cura con cremas necesita una biopsia, porque puede asociarse a un cancer "
        "debajo. Por eso tambien pedimos una mamografia completa. Es importante estudiarlo bien, no tratarlo "
        "como una simple irritacion.",
        "No use mas cremas a ciegas: eso retrasa el diagnostico. La cito pronto con los resultados.",
    ),
    MENOS + ["mama", "paget"])

add(deck_menos,
    caso("Telorrea (secrecion por el pezon)"),
    manejo(
        "<b>Fisiologica</b> (bilateral, multiporo, provocada, lechosa): tranquilizo, descarto galactorrea "
        "(prolactina, TSH, farmacos). <b>Patologica</b> (<b>unilateral, uniporo, espontanea, "
        "serosanguinolenta</b>): mamografia + USG &plusmn; ductografia/biopsia (papiloma intraductal o Ca).",
        "Lo importante es el tipo de secrecion. Si sale de los dos pechos, de varios poros y solo al "
        "apretar, casi siempre es benigna. Si sale de un solo pecho, un solo punto, sola y con sangre, "
        "hay que estudiarla.",
        "Evite estimular o apretar el pezon, eso la perpetua. Si es del tipo que preocupa, le agendo los "
        "estudios de imagen.",
    ),
    MENOS + ["mama", "telorrea"])

add(deck_menos,
    caso("Adenomiosis"),
    manejo(
        "Sintomatica: <b>DIU-LNG</b> (de eleccion), AINEs, ACO/progestinas, acido tranexamico para el "
        "sangrado. <b>Histerectomia = unico tratamiento curativo</b> (si paridad satisfecha y refractaria).",
        "El tejido del endometrio crece dentro del musculo del utero; por eso tiene reglas muy abundantes y "
        "dolorosas, con el utero agrandado. Un dispositivo con hormona (DIU) suele controlar muy bien sangrado y dolor.",
        "Si ya no desea embarazos y nada controla los sintomas, la histerectomia es lo unico que cura "
        "definitivamente. Vamos por el manejo conservador primero.",
    ),
    MENOS + ["adenomiosis"])

add(deck_menos,
    caso("Prolapso de organos pelvicos"),
    manejo(
        "<b>Leve/asintomatico:</b> ejercicios de Kegel + observacion + medidas (peso, estrenimiento). "
        "<b>Sintomatico:</b> <b>pesario</b> (conservador, buena opcion si no desea/no tolera cirugia) o "
        "<b>cirugia reconstructiva</b> (colporrafia, histeropexia).",
        "El piso pelvico se ha debilitado y los organos descienden. Si es leve, los ejercicios de "
        "fortalecimiento ayudan mucho. Si le molesta bastante, un dispositivo de silicona (pesario) sostiene "
        "los organos sin cirugia.",
        "Bajar de peso y evitar el estrenimiento y los esfuerzos protegen el resultado. Si elige cirugia o el "
        "pesario no le acomoda, lo valoramos.",
    ),
    MENOS + ["prolapso"])

add(deck_menos,
    caso("Patologia vulvoperineal (liquen plano / VIN / condiloma)"),
    manejo(
        "Toda lesion vulvar persistente o atipica: <b>biopsia para diagnostico</b>. "
        "<b>Liquen plano:</b> corticoide topico. <b>VIN (neoplasia intraepitelial):</b> escision/imiquimod/laser + "
        "seguimiento. <b>Condiloma:</b> topico/crioterapia.",
        "Las lesiones de la vulva que no se curan o cambian de aspecto hay que biopsiarlas para saber que "
        "son, porque el tratamiento cambia mucho segun el diagnostico. No conviene tratarlas a ciegas.",
        "Cualquier herida, mancha o bulto vulvar que no sane en pocas semanas, avise. El seguimiento es "
        "importante en lesiones premalignas.",
    ),
    MENOS + ["vulvoperineal"])

add(deck_menos,
    caso("Infertilidad (estudio inicial de la pareja)"),
    manejo(
        "Estudio tras <b>12 meses sin lograr embarazo</b> (6 meses si &ge;35 anos): "
        "<b>seminograma</b> (factor masculino), <b>confirmar ovulacion</b> (progesterona dia 21), "
        "<b>permeabilidad tubarica (HSG)</b>, reserva ovarica. Trato la causa; escalo a IIU/FIV si procede.",
        "La infertilidad es de la pareja, no solo de la mujer, asi que estudiamos a ambos. No tratamos a "
        "ciegas: primero buscamos la causa (semen, ovulacion, trompas) y de ahi sale el tratamiento.",
        "El estudio del hombre es sencillo y se hace primero por ser el mas rapido. Segun lo que encontremos "
        "definimos los pasos; muchas causas tienen solucion.",
    ),
    MENOS + ["infertilidad"])


# ============================================================
# Build / empaquetado
# ============================================================
def build():
    decks = [
        (deck_ejes, "01_Ejes_madre.apkg"),
        (deck_core, "02_Manejos_trampa_core.apkg"),
        (deck_menos, "03_Menos_preguntados.apkg"),
    ]
    for d, fname in decks:
        pkg = genanki.Package(d)
        out = os.path.join(OUTPUT_DIR, fname)
        pkg.write_to_file(out)
        print(f"  -> {fname} ({len(d.notes)} notas)")

    combined = genanki.Package([deck_ejes, deck_core, deck_menos])
    combined_out = os.path.join(OUTPUT_DIR, "No_Hay_Tiempo_Gineco_TODOS.apkg")
    combined.write_to_file(combined_out)
    total = sum(len(d.notes) for d in [deck_ejes, deck_core, deck_menos])
    print(f"  -> No_Hay_Tiempo_Gineco_TODOS.apkg ({total} notas totales)")


if __name__ == "__main__":
    build()
