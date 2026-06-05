"""No hay tiempo / Medicina Familiar — PILAR MANEJO (ejes/patrones madre + core + menos).

Carta de manejo (Back): VERBALIZO (al sinodal) / CONDUCTA-CONSEJERIA / CIERRE (red flag).
Carta de eje (Back): REGLA MADRE / BIFURCACION / TRAMPA.
Enfoque de primer contacto: ambulatorio vs referir, prevencion, uso racional de antibiotico.
Guia: GPC MX, GINA, GOLD, ADA, AHA/ACC, ESC, IDSA, USPSTF, CENETEC.
"""
import os
import genanki

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "output")
os.makedirs(OUTPUT_DIR, exist_ok=True)

MODEL_QA_ID = 1990009901
DECK_ID_E, DECK_ID_C, DECK_ID_M = 1990009001, 1990009002, 1990009003
DECK_NAME_E = "No hay tiempo::Medicina Familiar::1 - Ejes / patrones madre"
DECK_NAME_C = "No hay tiempo::Medicina Familiar::2 - Manejos comunes (core)"
DECK_NAME_M = "No hay tiempo::Medicina Familiar::3 - Menos comunes"

CSS_BASE = """
.card { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  font-size: 19px; text-align: left; color: #1a1a1a; background-color: #fafafa;
  padding: 20px; line-height: 1.55; }
.caso { font-size: 21px; font-weight: 700; color: #1e3a8a; }
#extra { margin-top: 16px; border: none; border-top: 1px solid #d4d4d4; padding-top: 12px; }
.bloque { display: block; margin: 12px 0; padding: 10px 14px; border-radius: 8px; }
.lab { display: block; font-size: 13px; font-weight: 700; letter-spacing: .5px;
  text-transform: uppercase; margin-bottom: 4px; }
.verbalizo { background: #eef2ff; border-left: 4px solid #1e3a8a; }
.conducta { background: #ecfdf5; border-left: 4px solid #047857; }
.cierre { background: #fef2f2; border-left: 4px solid #b91c1c; }
.verbalizo .lab { color: #1e3a8a; } .conducta .lab { color: #047857; } .cierre .lab { color: #b91c1c; }
.regla { background: #eef2ff; border-left: 4px solid #1e3a8a; }
.bif { background: #f5f3ff; border-left: 4px solid #6d28d9; }
.trampa { background: #fef2f2; border-left: 4px solid #b91c1c; }
.regla .lab { color: #1e3a8a; } .bif .lab { color: #6d28d9; } .trampa .lab { color: #b91c1c; }
b { color: #111; }
"""
model_qa = genanki.Model(MODEL_QA_ID, "NHT MF Manejo QA",
    fields=[{"name": "Front"}, {"name": "Back"}],
    templates=[{"name": "QA", "qfmt": "{{Front}}", "afmt": '{{Front}}<hr id="extra">{{Back}}'}],
    css=CSS_BASE)

deck_e = genanki.Deck(DECK_ID_E, DECK_NAME_E)
deck_c = genanki.Deck(DECK_ID_C, DECK_NAME_C)
deck_m = genanki.Deck(DECK_ID_M, DECK_NAME_M)
BASE_TAGS = ["medicina_familiar", "ecoe", "no_hay_tiempo"]


def add(deck, front, back, tags):
    deck.add_note(genanki.Note(model=model_qa, fields=[front, back], tags=BASE_TAGS + tags))

def caso(t): return f'<span class="caso">{t}</span>'

def manejo(v, c, ci):
    return (f'<span class="bloque verbalizo"><span class="lab">Verbalizo (al sinodal)</span>{v}</span>'
            f'<span class="bloque conducta"><span class="lab">Conducta / consejeria</span>{c}</span>'
            f'<span class="bloque cierre"><span class="lab">Red flag / cierre</span>{ci}</span>')

def eje(r, b, t):
    return (f'<span class="bloque regla"><span class="lab">Regla madre</span>{r}</span>'
            f'<span class="bloque bif"><span class="lab">Bifurcacion</span>{b}</span>'
            f'<span class="bloque trampa"><span class="lab">Trampa ECOE</span>{t}</span>')

def core(deck, t, v, c, ci, tags):
    add(deck, caso(t), manejo(v, c, ci), ["core"] + tags)

def menos(deck, t, v, c, ci, tags):
    add(deck, caso(t), manejo(v, c, ci), ["menos_comun"] + tags)


# ===================== EJES / PATRONES MADRE (8) =====================
E = ["eje"]
add(deck_e, caso("EJE 1 — Primero descarto LO URGENTE; recien luego trato como banal"),
    eje("Imagen: el portero que revisa banderas rojas antes de dejar pasar. En primer contacto, ante cualquier "
        "sintoma comun (cefalea, lumbalgia, dolor toracico, sincope, fiebre) <b>cribo red flags y signos vitales "
        "ANTES</b> de etiquetarlo como benigno.",
        "<b>Sin banderas</b> &rarr; manejo ambulatorio sintomatico + cita de control. "
        "<b>Con banderas</b> &rarr; estudio dirigido o referencia/urgencias.",
        "El error de medicina familiar es tratar como banal un debut grave (cefalea trueno, lumbalgia con cauda "
        "equina, dolor toracico = SCA). La seguridad esta en el cribado, no en el tratamiento."),
    E + ["red_flags"])

add(deck_e, caso("EJE 2 — La pregunta de fondo: AMBULATORIO vs REFERIR/URGENCIAS"),
    eje("Imagen: una bifurcacion del camino en cada consulta. Defino el <b>nivel de atencion</b> segun gravedad, "
        "comorbilidad, estabilidad y recursos.",
        "<b>Manejo aqui</b>: estable, sin dato de alarma, diagnostico claro de 1er nivel. "
        "<b>Refiero a 2o/3er nivel</b>: duda diagnostica, falla al tratamiento, criterio de especialidad "
        "(p.ej. nodulo tiroideo sospechoso, CA prostata, valvulopatia). "
        "<b>Urgencias</b>: inestable o emergencia (SCA, EVC, sepsis, cauda equina, emergencia HTA).",
        "Verbaliza SIEMPRE el plan de seguridad: 'si aparece X, acude a urgencias'. La consulta no termina sin "
        "criterios de retorno."),
    E + ["nivel_atencion"])

add(deck_e, caso("EJE 3 — Antibiotico SOLO cuando cambia el desenlace"),
    eje("Imagen: guardar la bala para cuando importa. La mayoria de las infecciones respiratorias altas y la "
        "bronquitis aguda son <b>virales</b>: el antibiotico no ayuda y dana (resistencia, efectos adversos).",
        "<b>Viral</b> (resfriado, bronquitis, faringitis viral, influenza) &rarr; sintomatico + educacion. "
        "<b>Bacteriano probable</b> (faringitis con Centor alto, OMA que no mejora, sinusitis &gt;10 dias o que "
        "empeora, NAC, ITU) &rarr; antibiotico dirigido.",
        "Recetar antibiotico 'por si acaso' en cuadro viral es la trampa clasica. Explica por que NO lo necesita y "
        "da banderas de alarma."),
    E + ["antibiotico"])

add(deck_e, caso("EJE 4 — El cronico se maneja por RIESGO GLOBAL + metas + adherencia + prevencion"),
    eje("Imagen: el tablero de control del paciente cronico. No trato cifras aisladas: integro <b>HTA, DM, lipidos, "
        "tabaco, peso, renal</b> en un riesgo CV total y fijo metas.",
        "<b>Alto riesgo / dano de organo</b> &rarr; metas estrictas (estatina, TA &lt;130/80, iSGLT2/GLP-1 si DM con "
        "riesgo). <b>Cada visita</b>: refuerzo de adherencia, estilo de vida, tamizaje y vacunas.",
        "Tratar un solo factor e ignorar los demas (o no reforzar adherencia) deja el riesgo casi intacto. La "
        "prevencion es parte del manejo, no un extra."),
    E + ["riesgo_cv"])

add(deck_e, caso("EJE 5 — Dolor toracico / disnea: descarto primero LO QUE MATA"),
    eje("Imagen: las 'que matan' antes de la causa benigna. ECG + signos vitales + SatO2 de inmediato.",
        "Letales: <b>SCA</b>, <b>TEP</b>, <b>diseccion aortica</b>, <b>neumotorax a tension</b>, "
        "<b>taponamiento</b>. Benignas (costocondritis, ansiedad, ERGE) son diagnostico de exclusion.",
        "Un ECG normal NO descarta SCA. En 1er contacto, ante dolor toracico de caracteristicas isquemicas, "
        "traslado a urgencias (no 'observar en casa')."),
    E + ["dolor_toracico"])

add(deck_e, caso("EJE 6 — Crisis metabolica/endocrina: glucemia primero; luego liquidos + deficit + gatillo"),
    eje("Imagen: el glucometro antes que nada en el paciente alterado. Casi toda urgencia endocrina comparte: "
        "<b>reanimacion con liquidos + correccion del eje + tratar el desencadenante</b>.",
        "<b>Hipoglucemia</b> (siempre primero, es reversible al instante) &rarr; glucosa. "
        "CAD/EHH &rarr; liquidos + insulina + K. Crisis suprarrenal &rarr; liquidos + hidrocortisona. "
        "Tormenta tiroidea &rarr; BB + tionamida + yodo + esteroide.",
        "En crisis suprarrenal y mixedema da <b>hidrocortisona ANTES</b> de la hormona tiroidea. No esperes la "
        "confirmacion hormonal para tratar la emergencia."),
    E + ["crisis_endocrina"])

add(deck_e, caso("EJE 7 — Toda cefalea, lumbalgia y sincope: buscar RED FLAGS antes de etiquetar benigno"),
    eje("Imagen: tres sintomas 'banales' con una version mortal escondida. El 95% es benigno; mi trabajo es "
        "atrapar el 5% peligroso.",
        "<b>Cefalea</b>: SNNOOP (trueno, focal, fiebre+rigidez, &gt;50 nueva, inmunodeprimido, papiledema). "
        "<b>Lumbalgia</b>: cauda equina, fractura, infeccion, cancer (perdida de peso, fiebre, deficit, nocturno). "
        "<b>Sincope</b>: de esfuerzo, en supino, palpitaciones, cardiopatia, ECG anormal.",
        "Sin banderas: manejo conservador y educacion, <b>sin imagen de rutina</b>. Con banderas: estudio urgente."),
    E + ["red_flags_sintomas"])

add(deck_e, caso("EJE 8 — PREVENCION en cada consulta: tamizaje + vacunas + consejo (oportunidad)"),
    eje("Imagen: aprovechar que el paciente ya esta enfrente. En medicina familiar cada visita es ventana para "
        "<b>prevenir</b>, no solo para tratar el motivo de consulta.",
        "<b>Tamizaje por edad/riesgo</b> (TA, glucosa, lipidos, cancer cervico/mama/colon, VIH). "
        "<b>Vacunas</b> segun esquema del adulto. <b>Consejo breve</b>: tabaco (5 A), alcohol, actividad, dieta.",
        "Olvidar la prevencion (no preguntar por tabaco, no ofrecer tamizaje/vacuna) es perder el rol central de "
        "la medicina familiar. Documenta y ofrece siempre."),
    E + ["prevencion"])


# ===================== CORE / COMUNES (24) =====================
C = ["core"]
core(deck_c, "Hipertension arterial",
     "Estilo de vida + farmaco: <b>IECA/ARA-II + calcioantagonista + tiazida</b> (combinar pronto). Meta general "
     "<b>&lt;130/80</b>. Busco dano a organo blanco y descarto causa 2aria si datos atipicos.",
     "Tiene la presion alta cronica; el objetivo es mantenerla controlada con medicamento diario y habitos (sal, "
     "peso, ejercicio) para evitar infarto, EVC y dano renal.",
     "No combines IECA + ARA-II. Vigila K/creatinina al iniciar IECA/ARA-II. Confirma con tomas repetidas/AMPA "
     "(bata blanca).", C + ["htas"])

core(deck_c, "Diabetes mellitus tipo 2",
     "Estilo de vida + <b>metformina</b> de base; anado <b>iSGLT2/GLP-1</b> si riesgo CV/renal. Meta <b>HbA1c "
     "&lt;7%</b> (individualizada). Trato TA, LDL (estatina) y tabaco; tamizo pie, retina, rinon.",
     "Tiene diabetes; el control combina alimentacion, ejercicio y medicamento. Cuidamos tambien presion, "
     "colesterol y rinon porque eso evita las complicaciones.",
     "El iSGLT2/GLP-1 se eligen por proteccion CV/renal. Educacion en hipoglucemia y pie diabetico es parte del "
     "manejo.", C + ["dm2"])

core(deck_c, "Dislipidemia",
     "Calculo <b>riesgo CV</b> y trato con <b>estatina</b> segun riesgo (alta intensidad en alto riesgo/ECV "
     "establecida) + estilo de vida. Meta de LDL mas baja a mayor riesgo; anado ezetimibe/iPCSK9 si no llega.",
     "El colesterol alto tapa las arterias con los anos. Bajamos el LDL con dieta y una estatina; la meta depende "
     "de su riesgo total de infarto/EVC.",
     "La decision es por riesgo global, no solo por la cifra de LDL. Vigila adherencia y mialgias; descarta "
     "hipotiroidismo como causa 2aria.", C + ["dislipidemia"])

core(deck_c, "Asma (manejo y crisis)",
     "<b>Control</b>: terapia escalonada basada en <b>corticoide inhalado</b> (GINA: ICS-formoterol de rescate). "
     "<b>Crisis</b>: SABA + O2 + <b>esteroide sistemico precoz</b> + ipratropio/magnesio si grave.",
     "El asma se controla con un inhalador con cortisona que desinflama; el de rescate alivia. Identificamos y "
     "evitamos los gatillos y revisamos la tecnica del inhalador.",
     "No uses SABA solo como mantenimiento. En crisis grave, PCO2 'normal' (deberia estar baja) anuncia paro.",
     C + ["asma"])

core(deck_c, "EPOC (manejo y exacerbacion)",
     "<b>Cronico</b>: broncodilatadores de larga (LABA/LAMA) + dejar de fumar + vacunas + rehabilitacion. "
     "<b>Exacerbacion</b>: SABA/SAMA + <b>esteroide</b> + ATB si purulencia + O2 meta 88-92% + VMNI si acidosis.",
     "El EPOC dana los pulmones por el tabaco. El pilar que cambia el curso es <b>dejar de fumar</b>; los "
     "inhaladores y vacunas reducen las crisis.",
     "Meta de O2 88-92% (riesgo de narcosis). Dejar de fumar es la unica medida que modifica la historia natural.",
     C + ["epoc"])

core(deck_c, "Neumonia adquirida en la comunidad (NAC)",
     "Evaluo gravedad (<b>CURB-65</b>) para decidir ambulatorio vs hospital. <b>Antibiotico empirico</b> segun el "
     "sitio (ambulatorio: amoxicilina/macrolido; hospital: betalactamico + macrolido). O2 y liquidos.",
     "Tiene neumonia. Segun la gravedad decidimos si se trata en casa o ingresado; el pilar es el antibiotico mas "
     "soporte.",
     "CURB-65 guia el sitio. Reevalua si no mejora en 48-72 h (derrame/empiema, resistencia).", C + ["nac"])

core(deck_c, "IVAS / resfriado comun",
     "<b>Sintomatico</b>: analgesico/antipiretico, hidratacion, lavados nasales. <b>NO antibiotico</b> (es viral). "
     "Educacion e higiene respiratoria.",
     "Es una infeccion viral de las vias respiratorias altas; se cura sola en pocos dias. No necesita antibiotico; "
     "tratamos los sintomas y cuidamos la hidratacion.",
     "Sintomas &gt;10 dias o que empeoran tras mejorar &rarr; sospecha sinusitis bacteriana. Da banderas de alarma "
     "(disnea, fiebre alta persistente).", C + ["ivas"])

core(deck_c, "Influenza",
     "<b>Sintomatico</b>; <b>oseltamivir</b> si &lt;48 h del inicio y alto riesgo (embarazo, &gt;65, comorbilidad) "
     "o cuadro grave. Aislamiento y reposo. <b>Prevencion = vacuna anual</b>.",
     "Es gripe por virus de influenza. La mayoria mejora con reposo e hidratacion; si esta en riesgo y es "
     "temprano, un antiviral acorta el cuadro. Lo clave es vacunarse cada ano.",
     "Vigila complicacion (neumonia, descompensacion de cronico). El antiviral sirve solo temprano (&lt;48 h).",
     C + ["influenza"])

core(deck_c, "Faringitis aguda",
     "Aplico <b>Centor/McIsaac</b>: bajo &rarr; sintomatico (probable viral). Alto/estreptococo confirmado &rarr; "
     "<b>penicilina o amoxicilina</b> (alergia: macrolido). Analgesia siempre.",
     "Es dolor de garganta; la mayoria es viral y mejora sola. Si los datos apuntan a bacteria (estreptococo), "
     "damos antibiotico para prevenir complicaciones.",
     "El antibiotico previene fiebre reumatica en la estreptococica. No lo des de rutina a todo dolor de garganta "
     "(la mayoria es viral).", C + ["faringitis"])

core(deck_c, "Otitis media aguda (OMA)",
     "<b>Analgesia</b> siempre. <b>Antibiotico (amoxicilina alta dosis)</b> si &lt;2 anos bilateral, otorrea, o "
     "grave; <b>observacion 48-72 h</b> en seleccionados leves. Amoxi-clavulanico si falla/factores.",
     "Es una infeccion del oido medio. Lo primero es calmar el dolor; segun la edad y la gravedad damos antibiotico "
     "o esperamos 2-3 dias vigilando.",
     "Otorrea con membrana perforada o mastoiditis (oido protruido, fiebre) = referir. No confundir con otitis "
     "externa (dolor al traccionar el pabellon).", C + ["oma"])

core(deck_c, "Sinusitis aguda",
     "La mayoria es <b>viral</b> &rarr; sintomatico (analgesia, lavados, descongestivo corto). <b>Antibiotico "
     "(amoxi-clavulanico)</b> solo si &gt;10 dias sin mejorar, empeora tras mejorar, o cuadro grave (fiebre alta, "
     "dolor facial intenso).",
     "Es inflamacion de los senos paranasales, casi siempre viral. Mejora con lavados y analgesico; solo si dura "
     "mucho o empeora damos antibiotico.",
     "Datos de alarma (complicacion orbitaria/intracraneal): edema/eritema periorbitario, diplopia, alteracion "
     "visual o neurologica &rarr; urgencia.", C + ["sinusitis"])

core(deck_c, "Rinitis alergica",
     "<b>Evitar el alergeno</b> + <b>corticoide nasal</b> (mas eficaz) y/o <b>antihistaminico</b> no sedante. "
     "Considerar inmunoterapia si refractaria.",
     "Es una alergia de la nariz (estornudos, moco claro, comezon). El spray nasal con cortisona es lo que mejor "
     "funciona; ayuda evitar el polvo/polen y un antihistaminico.",
     "Diferencia de la viral: sintomas recurrentes/estacionales, prurito, sin fiebre. El abuso de descongestivos "
     "nasales causa rinitis medicamentosa.", C + ["rinitis"])

core(deck_c, "Insuficiencia cardiaca cronica (ICC)",
     "Segun FEVI: <b>FEr</b> &rarr; 4 pilares (ARNI/IECA, BB, ARM, iSGLT2) + diuretico para congestion; "
     "<b>FEp</b> &rarr; iSGLT2 + diuretico + tratar comorbilidades. Educacion: sal, peso diario, adherencia.",
     "El corazon bombea/llena mal y se acumula liquido. Hay medicamentos que alargan la vida y un diuretico que "
     "quita el liquido; cuidar la sal y pesarse a diario detecta descompensaciones.",
     "El BB no se inicia en descompensacion congestiva aguda. Subida brusca de peso/disnea = descompensacion (busca "
     "el gatillo).", C + ["icc"])

core(deck_c, "Gastroenteritis aguda",
     "<b>Hidratacion oral</b> (pilar) + dieta segun tolerancia. Antiemetico/antidiarreico segun caso. "
     "<b>Antibiotico solo</b> en disenteria/sospecha bacteriana especifica o paciente de riesgo. Educacion e higiene.",
     "Es una infeccion del tubo digestivo, casi siempre viral y autolimitada. Lo principal es reponer liquidos con "
     "suero oral; la mayoria no necesita antibiotico.",
     "Datos de alarma: deshidratacion, sangre en heces, fiebre alta, intolerancia oral &rarr; valorar IV/estudio. "
     "Evita antibiotico de rutina (riesgo SHU en E. coli O157).", C + ["gastroenteritis"])

core(deck_c, "Migrana",
     "<b>Agudo</b>: AINE o <b>triptan</b> + antiemetico, temprano, en ambiente oscuro. <b>Profilaxis</b> "
     "(betabloqueante, topiramato, amitriptilina) si &ge;4 dias/mes o gran impacto. Identificar gatillos.",
     "Es una migrana: dolor pulsatil, con nausea y molestia a luz/ruido. La tratamos pronto con un analgesico "
     "especifico; si es frecuente, damos un medicamento diario para prevenir.",
     "Cefalea NUEVA, en trueno, con focalidad o &gt;50 anos = estudio (no es migrana). Cuidado con abuso de "
     "analgesicos (cefalea de rebote).", C + ["migrana"])

core(deck_c, "Cefalea tensional",
     "<b>Analgesico simple</b> (paracetamol/AINE) para el episodio + manejo de <b>estres, sueno, postura</b>. "
     "Amitriptilina si cronica/frecuente. Limitar analgesicos para evitar rebote.",
     "Es la cefalea por tension: opresiva, 'en banda', sin nausea ni foto/fonofobia marcadas. Mejora con un "
     "analgesico y, sobre todo, controlando estres y descanso.",
     "Si cambia de patron, aparecen banderas o aumenta de frecuencia, reevalua. El uso excesivo de analgesicos "
     "perpetua la cefalea.", C + ["cefalea_tensional"])

core(deck_c, "Vertigo posicional benigno (VPPB)",
     "<b>Dix-Hallpike</b> para confirmar &rarr; <b>maniobra de reposicion (Epley)</b>. Sedantes vestibulares solo "
     "breve para el sintoma agudo. Educacion (es benigno y autolimitado).",
     "Es vertigo por cristales en el oido interno; aparece con los cambios de posicion de la cabeza y dura "
     "segundos. Una maniobra para recolocarlos lo resuelve en la mayoria.",
     "Banderas de <b>vertigo central</b> (referir/urgencia): deficit neurologico, cefalea, nistagmo que no fatiga, "
     "HINTS patologico, no posicional.", C + ["vppb"])

core(deck_c, "Lumbalgia inespecifica (aguda)",
     "<b>Analgesia (paracetamol/AINE)</b> + <b>mantener actividad</b> (evitar reposo prolongado) + educacion de "
     "buen pronostico. <b>NO imagen de rutina</b> sin banderas. Calor/ejercicio segun tolerancia.",
     "Es un dolor de espalda mecanico, muy comun y de buen pronostico. Lo mejor es seguir activo dentro de lo "
     "tolerable y usar analgesico; casi siempre mejora en pocas semanas.",
     "Banderas rojas (estudio/referir): deficit neurologico, cauda equina, fiebre, perdida de peso, cancer, trauma, "
     "dolor nocturno. Sin banderas, NO pidas Rx/RM.", C + ["lumbalgia"])

core(deck_c, "Cistitis no complicada (mujer)",
     "<b>Antibiotico corto empirico</b>: nitrofurantoina, fosfomicina o TMP-SMX (segun resistencia local) + "
     "analgesia/hidratacion. Urocultivo si recurrente/duda.",
     "Es una infeccion de la vejiga. Un antibiotico corto la resuelve; ademas tomar liquidos y un analgesico "
     "urinario ayuda con la molestia.",
     "Fiebre + dolor lumbar/punopercusion = pielonefritis (no es cistitis simple). En varon, embarazo, sonda o "
     "anomalia = ITU complicada (manejo distinto).", C + ["cistitis"])

core(deck_c, "Hipotiroidismo",
     "<b>Levotiroxina</b> ajustada por TSH (control en 6-8 semanas). Dosis menor e incremento lento en ancianos/"
     "cardiopatas. Tomar en ayuno.",
     "La tiroides produce poca hormona y todo se enlentece (cansancio, frio, peso, estrenimiento). Se repone con "
     "una pastilla diaria de hormona tiroidea, ajustando la dosis con analisis.",
     "Subclinico (TSH alta, T4 normal): tratar si TSH alta significativa, sintomas, embarazo o anticuerpos. "
     "Levotiroxina en exceso = hipertiroidismo iatrogenico (FA, osteoporosis).", C + ["hipotiroidismo"])

core(deck_c, "Anemia (enfoque en 1er contacto)",
     "Clasifico por <b>VCM</b>: micro (ferropenica &rarr; buscar sangrado/dieta), normo (enfermedad cronica), "
     "macro (B12/folato). Trato la causa + repongo el deficit. Referir si severa o causa no clara.",
     "La anemia es tener pocos globulos rojos; cansa y da palidez. Primero vemos el tamano del globulo para saber "
     "la causa (falta de hierro, vitamina o enfermedad de fondo) y la corregimos.",
     "Anemia ferropenica en varon o posmenopausica = <b>descartar sangrado digestivo</b> (endoscopia/colonoscopia). "
     "Repon B12 antes/junto con folato si hay deficit de B12.", C + ["anemia"])

core(deck_c, "Vacunacion del adulto (prevencion)",
     "Reviso y completo esquema: <b>influenza anual</b>, <b>neumococo</b> (&ge;65 o riesgo), <b>Td/Tdap</b> "
     "(refuerzo c/10 a), hepatitis B, <b>VPH</b>, <b>herpes zoster</b> (&ge;50), COVID, segun edad/riesgo/embarazo.",
     "Aprovecho la consulta para revisar sus vacunas. Las vacunas previenen enfermedades graves; le pongo o "
     "programo las que le faltan segun su edad y condiciones.",
     "Embarazo: Tdap e influenza SI; vacunas de virus vivos (SRP, varicela) NO. Inmunodepresion: evitar vivas. "
     "Aprovecha toda visita para actualizar.", C + ["vacunas"])

core(deck_c, "Cese de tabaquismo (consejo breve)",
     "Aplico las <b>5 A</b>: Averiguar, Aconsejar (claro y personalizado), Apreciar disposicion, Asistir "
     "(farmacoterapia: <b>terapia de reemplazo de nicotina, bupropion, vareniclina</b> + apoyo conductual), "
     "Acordar seguimiento.",
     "Dejar de fumar es lo que mas mejora su salud. Le ofrezco ayuda: parches/chicles o pastillas que reducen el "
     "deseo, y lo acompano con seguimiento; recaer es parte del proceso.",
     "Aun el consejo breve aumenta el cese; ofrecelo SIEMPRE. La combinacion farmaco + conductual es mas efectiva "
     "que la fuerza de voluntad sola.", C + ["tabaquismo"])

core(deck_c, "Tamizaje (deteccion oportuna por edad/riesgo)",
     "Ofrezco segun edad/riesgo: <b>TA, glucosa/HbA1c, lipidos</b>; cancer <b>cervicouterino</b> (citologia/VPH), "
     "<b>mama</b> (mastografia), <b>colon</b> (sangre oculta/colonoscopia), prostata individualizado; <b>VIH</b> al "
     "menos una vez; agudeza visual, salud mental.",
     "Aprovecho para buscar enfermedades antes de que den sintomas (presion, azucar, colesterol, algunos canceres, "
     "VIH). Detectarlas temprano salva vidas; le explico cuales le tocan.",
     "El tamizaje es por edad/riesgo, no 'a todos todo'. Cervico: 21-65 a (citologia/co-test); mama y colon segun "
     "guia local. Individualiza prostata (consentimiento informado).", C + ["tamizaje"])


# ===================== MENOS COMUNES (37) =====================
menos(deck_m, "Bronquitis aguda",
      "<b>Sintomatico</b> (analgesico, hidratacion, antitusivo si molesta). <b>NO antibiotico</b> de rutina (es "
      "viral), aunque la tos dure 2-3 semanas.",
      "Es una infeccion viral de los bronquios; la tos puede durar semanas pero se cura sola. No necesita "
      "antibiotico; tratamos la molestia.",
      "Tos &gt;3 semanas, fiebre alta, disnea o foco en la auscultacion &rarr; descarta neumonia (Rx).", ["bronquitis"])

menos(deck_m, "Derrame pleural",
      "<b>Identificar la causa</b> (IC, neumonia/empiema, neoplasia, TB) y referir para <b>toracocentesis</b> "
      "diagnostica (criterios de Light: trasudado vs exudado). Tratar la enfermedad de base; drenar si empiema.",
      "Es liquido acumulado alrededor del pulmon. Hay que sacar una muestra para saber por que se acumulo y tratar "
      "la causa; si es pus, hay que drenarlo.",
      "Disnea con matidez + abolicion del murmullo de un lado. Empiema/derrame paraneumonico complicado = drenaje "
      "urgente (referir).", ["derrame_pleural"])

menos(deck_m, "Neumotorax",
      "<b>Pequeno y estable</b> &rarr; O2 + observacion. <b>Grande/sintomatico</b> &rarr; aspiracion o tubo "
      "pleural. <b>A tension</b> (hipotension, desviacion traqueal) &rarr; <b>descompresion con aguja YA</b> (dx "
      "clinico).",
      "Es aire entre el pulmon y la pared del torax que colapsa el pulmon. Segun el tamano se vigila o se drena con "
      "un tubo; si comprime el corazon es una urgencia inmediata.",
      "Neumotorax a tension NO espera Rx: descomprime de inmediato. Alto delgado fumador (espontaneo) o trauma.",
      ["neumotorax"])

menos(deck_m, "Otitis externa",
      "<b>Gotas topicas</b> (antibiotico &plusmn; esteroide) + analgesia + <b>mantener el oido seco</b>. Limpieza "
      "del conducto. Evitar hisopos.",
      "Es una infeccion del conducto del oido ('oido de nadador'). Se trata con gotas; hay que mantener el oido "
      "seco y no meter hisopos.",
      "Dolor al traccionar el pabellon/tragus (vs OMA). En diabetico/inmunodeprimido vigila <b>otitis externa "
      "maligna</b> (dolor intenso, parálisis facial) &rarr; urgencia.", ["otitis_externa"])

menos(deck_m, "Laringitis aguda",
      "<b>Sintomatico</b>: reposo vocal, hidratacion, humidificacion. Casi siempre viral; <b>NO antibiotico</b>. "
      "Educacion.",
      "Es inflamacion de la laringe, casi siempre viral; da ronquera. Se cura sola con reposo de la voz e "
      "hidratacion.",
      "Disfonia &gt;2-3 semanas (sobre todo fumador) = referir ORL (descartar cancer laringeo). Estridor/disnea = "
      "urgencia de via aerea.", ["laringitis"])

menos(deck_m, "Nodulo tiroideo",
      "Pido <b>TSH</b> + <b>USG tiroideo</b> (estratifica riesgo, p.ej. TIRADS). <b>BAAF</b> segun tamano/riesgo "
      "ecografico. Referir a endocrino/cirugia si sospecha. La mayoria son benignos.",
      "Encontramos un nodulo en la tiroides. Pedimos un analisis y un ultrasonido; si tiene caracteristicas de "
      "riesgo, se toma una muestra con aguja. La mayoria son benignos.",
      "Banderas de malignidad: duro, fijo, crecimiento rapido, adenopatia, disfonia, antecedente de radiacion. "
      "TSH baja &rarr; gammagrafia (nodulo caliente, casi siempre benigno).", ["nodulo_tiroideo"])

menos(deck_m, "Sindrome coronario agudo (SCA)",
      "<b>Urgencia</b>: ECG + traslado. <b>MONA-B</b> sintomatico + antiagregacion (AAS) inicial. "
      "<b>CEST</b> &rarr; reperfusion (ICP/fibrinolisis); <b>SEST</b> &rarr; antitrombotico + estratificar. "
      "Estabilizar y referir a 3er nivel.",
      "(urgencia) Es un infarto/angina: una arteria del corazon esta comprometida. Activamos el traslado "
      "inmediato; cada minuto cuenta para salvar musculo cardiaco.",
      "ECG normal NO descarta SCA. En 1er contacto: AAS + traslado urgente, no 'observar'.", ["sca"])

menos(deck_m, "Pericarditis aguda",
      "<b>AINE (alta dosis) + colchicina</b> + restriccion de ejercicio. Buscar derrame; <b>taponamiento</b> &rarr; "
      "pericardiocentesis (urgencia). Tratar causa si se identifica.",
      "Es inflamacion de la bolsa del corazon; el dolor mejora con antiinflamatorios y agregamos colchicina para "
      "que no recaiga.",
      "ECG: <b>elevacion del ST difusa + descenso del PR</b>. Vigila taponamiento (Beck, pulso paradojico).",
      ["pericarditis"])

menos(deck_m, "Estenosis aortica",
      "Vigilancia si asintomatica. <b>Sintomatica/severa</b> (angina, sincope, disnea) &rarr; referir para "
      "<b>reemplazo valvular (RVAo/TAVI)</b>. Cuidado con vasodilatadores/diureticos potentes.",
      "La valvula aortica esta estrecha y el corazon batalla. Cuando da sintomas, el tratamiento que sirve es "
      "cambiar la valvula; mientras, evitamos medicamentos que bajen mucho la presion.",
      "Triada: <b>angina, sincope, disnea</b>. El sincope de esfuerzo es bandera roja. Evita nitratos en severa.",
      ["estenosis_aortica"])

menos(deck_m, "Trombosis venosa profunda (TVP)",
      "<b>Probabilidad (Wells) + dimero D / USG Doppler</b>. Confirmada &rarr; <b>anticoagulacion</b> (HBPM/ACOD). "
      "Buscar datos de TEP. Medias de compresion para sintomas.",
      "Es un coagulo en una vena profunda de la pierna (hinchada, dolorosa, caliente). Se trata con anticoagulante "
      "para evitar que crezca o viaje al pulmon.",
      "Disnea/dolor toracico = sospecha de TEP (urgencia). Investiga causa (cancer, inmovilidad, trombofilia) si no "
      "provocada.", ["tvp"])

menos(deck_m, "Sincope (enfoque)",
      "Distingo <b>vasovagal/ortostatico</b> (benigno) de <b>cardiogenico</b> (peligroso). <b>ECG</b> a todos + "
      "TA en bipedestacion. Educacion y maniobras en el vasovagal; referir cardiologia el cardiogenico.",
      "Es un desmayo por baja momentanea de sangre al cerebro. La mayoria es benigno (por calor, dolor, "
      "levantarse rapido); revisamos el corazon para descartar una causa peligrosa.",
      "Banderas cardiacas (referir/urgencia): de <b>esfuerzo</b>, en supino, sin prodromos, palpitaciones, "
      "cardiopatia, ECG anormal, muerte subita familiar.", ["sincope"])

menos(deck_m, "Apendicitis aguda",
      "<b>Referir a cirugia</b> (urgencia). Analgesia + NPO + liquidos + antibiotico mientras. Dx clinico "
      "(migracion del dolor a FID) + laboratorio/USG/TAC.",
      "(urgencia) Es una inflamacion del apendice que requiere cirugia. Lo enviamos al hospital; mientras, ayuno, "
      "suero y algo para el dolor.",
      "Dolor que migra a fosa iliaca derecha + Blumberg/McBurney. No retrasar (riesgo de perforacion). En mujer "
      "fertil descarta embarazo/ectopico.", ["apendicitis"])

menos(deck_m, "Colecistitis aguda",
      "<b>Referir</b>: NPO + liquidos + analgesia + <b>antibiotico</b>; <b>colecistectomia temprana</b>. USG "
      "(pared engrosada, litos, Murphy ecografico).",
      "Es una inflamacion de la vesicula por una piedra. El tratamiento es retirarla con cirugia, pronto; mientras, "
      "antibiotico y ayuno.",
      "Murphy +. Si aparece ictericia + fiebre con escalofrios &rarr; sospecha <b>colangitis</b> (urgencia mayor).",
      ["colecistitis"])

menos(deck_m, "Pancreatitis aguda",
      "<b>Referir/hospital</b>: <b>reanimacion con liquidos</b>, analgesia, NPO con reinicio precoz, tratar causa "
      "(biliar/alcohol). <b>No antibiotico de rutina</b>.",
      "Es una inflamacion del pancreas, casi siempre por piedras o alcohol. El tratamiento es hidratacion, control "
      "del dolor y reposo intestinal, vigilando la gravedad.",
      "Dx: 2 de 3 (dolor en barra + <b>lipasa &gt;3x</b> + imagen). Vigila falla organica las primeras 48 h.",
      ["pancreatitis"])

menos(deck_m, "Diverticulitis aguda",
      "<b>No complicada</b>: reposo intestinal + analgesia &plusmn; antibiotico (ambulatorio en leves). "
      "<b>Complicada</b> (absceso/perforacion) &rarr; referir (drenaje/cirugia). TAC para estadificar.",
      "Es inflamacion de pequenas bolsas del colon (dolor en fosa iliaca izquierda). Si es leve se maneja con "
      "reposo del intestino; si hay absceso o perforacion, se refiere.",
      "Colonoscopia <b>tras resolver</b> (no en agudo). Peritonismo/sepsis = urgencia quirurgica.", ["diverticulitis"])

menos(deck_m, "Obstruccion intestinal",
      "<b>Referir (urgencia)</b>: NPO + SNG (descompresion) + liquidos + corregir electrolitos. Cirugia si "
      "estrangulacion/asa cerrada/hernia incarcerada.",
      "(urgencia) El intestino esta obstruido (dolor colico, distension, vomito, no canaliza gases). Lo enviamos al "
      "hospital para descomprimir y valorar cirugia.",
      "Dolor continuo + fiebre + lactato = estrangulacion (urgencia). Pregunta por cirugias previas (bridas) y "
      "hernias.", ["obstruccion"])

menos(deck_m, "Enfermedad vascular cerebral (EVC)",
      "(urgencia) <b>Activar codigo ictus + traslado inmediato</b> (ventana de trombolisis/trombectomia). "
      "Glucemia, ECG, NO bajar TA agresivamente salvo limites. Tiempo es cerebro.",
      "(urgencia) Es una embolia/derrame cerebral. Cada minuto cuenta para salvar cerebro; activamos el traslado "
      "inmediato a un hospital con imagen.",
      "FAST (cara, brazo, habla, tiempo). NO des AAS hasta TAC (descartar hemorragico). No retrasar el traslado.",
      ["evc"])

menos(deck_m, "Cefalea con banderas rojas (secundaria)",
      "<b>Estudio urgente</b> (TAC/RM, puncion lumbar segun caso) y referir. No tratar como primaria hasta "
      "descartar causa grave.",
      "(alarma) Esta cefalea tiene datos que obligan a estudiarla a fondo de inmediato, porque podria deberse a una "
      "causa peligrosa.",
      "<b>SNNOOP</b>: en trueno (HSA), focalidad, fiebre + rigidez (meningitis), &gt;50 a de novo (arteritis), "
      "inmunodeprimido/cancer, papiledema/cambio postural, embarazo/posparto.", ["cefalea_red_flag"])

menos(deck_m, "Vertigo central",
      "<b>Referir/urgencia</b> (sospecha de EVC de fosa posterior). Neuroimagen. No es maniobra de Epley.",
      "(alarma) Este vertigo tiene datos de que el origen esta en el cerebro, no en el oido; requiere estudio "
      "urgente.",
      "Banderas: deficit neurologico, cefalea/cervicalgia, nistagmo que <b>no fatiga</b>/vertical, no posicional, "
      "<b>HINTS</b> central (skew, nistagmo cambiante, impulso cefalico normal).", ["vertigo_central"])

menos(deck_m, "Cauda equina",
      "<b>URGENCIA neuroquirurgica</b>: <b>RM urgente + referir YA</b>. No demorar.",
      "(urgencia) Es una compresion de los nervios de la parte baja de la columna; si no se descomprime pronto, "
      "deja secuelas (control de esfinteres, fuerza). Traslado inmediato.",
      "Triada: <b>retencion/incontinencia urinaria o fecal, anestesia en silla de montar, deficit motor "
      "bilateral</b>. Lumbalgia con esto = quirofano, no analgesia.", ["cauda_equina"])

menos(deck_m, "Ciatica / radiculopatia lumbar",
      "<b>Analgesia + mantener actividad</b> (igual que lumbalgia) + educacion (buen pronostico). Imagen/referir "
      "solo si deficit progresivo, refractario &gt;6 semanas o banderas.",
      "Es dolor que baja por la pierna por irritacion de una raiz nerviosa (hernia de disco). La mayoria mejora "
      "sola; usamos analgesico y mantenemos actividad.",
      "Lasegue +. Deficit motor progresivo o cauda equina = referir urgente. Sin banderas, NO imagen temprana.",
      ["ciatica"])

menos(deck_m, "Cervicalgia",
      "<b>Analgesia + movilizacion temprana</b> + educacion postural/ergonomia. Evitar collarin prolongado. "
      "Imagen/referir si trauma, deficit neurologico o banderas.",
      "Es dolor de cuello mecanico, muy comun y de buen pronostico. Mejor moverse dentro de lo tolerable y usar "
      "analgesico; el collarin rigido prolongado no ayuda.",
      "Banderas: trauma, deficit neurologico, fiebre, cancer, mielopatia (torpeza de manos, marcha). Trauma = "
      "inmovilizar y estudiar.", ["cervicalgia"])

menos(deck_m, "Pielonefritis aguda",
      "<b>Antibiotico</b> (ambulatorio si leve y tolera VO; <b>IV/hospital</b> si grave, vomito, embarazo, "
      "comorbilidad) + hidratacion. <b>Urocultivo</b> siempre. Imagen si no mejora en 48-72 h.",
      "Es una infeccion del rinon. Damos antibiotico (en vena si esta grave) y liquidos; si no mejora pronto, "
      "buscamos una obstruccion o absceso.",
      "ITU + obstruccion (litiasis) = <b>pionefrosis</b> &rarr; urgencia para drenar. Embarazada = ingreso/manejo "
      "estrecho.", ["pielonefritis"])

menos(deck_m, "Colico renal / litiasis ureteral",
      "<b>Analgesia (AINE de eleccion)</b> + hidratacion + antiemetico. <b>Alfa-bloqueante</b> (tamsulosina) para "
      "calculo distal &lt;10 mm (terapia expulsiva). TAC sin contraste confirma.",
      "Es una piedra en el rinon/ureter; el dolor es muy intenso. Damos un antiinflamatorio potente y, si la piedra "
      "es pequena, un medicamento que ayuda a expulsarla.",
      "<b>Urgencia</b> (referir): calculo + <b>fiebre/infeccion</b> (sepsis obstructiva), rinon unico, AKI, dolor "
      "incontrolable, calculo grande &rarr; drenaje urologico.", ["colico_renal"])

menos(deck_m, "ITU en el embarazo",
      "<b>Tratar SIEMPRE</b>, incluida la <b>bacteriuria asintomatica</b> (tamizar con urocultivo). Antibiotico "
      "seguro segun trimestre (cefalexina, fosfomicina; nitrofurantoina evitar cerca del termino; <b>NO "
      "fluoroquinolonas ni TMP en 1er trimestre</b>). Urocultivo de control.",
      "En el embarazo, hasta una infeccion urinaria sin sintomas hay que tratarla, porque puede causar pielonefritis "
      "y parto prematuro. Usamos un antibiotico seguro para el bebe.",
      "La bacteriuria asintomatica en embarazo SI se trata (a diferencia de la no embarazada). Pielonefritis en "
      "embarazo = ingreso.", ["itu_embarazo"])

menos(deck_m, "Hiperplasia prostatica benigna (HPB)",
      "Sintomas leves &rarr; vigilancia + medidas conductuales. Moderados/graves &rarr; <b>alfa-bloqueante</b> "
      "(tamsulosina) &plusmn; <b>5-alfa-reductasa</b> (prostata grande). Referir si retencion, hematuria, litiasis "
      "o falla.",
      "Es el crecimiento benigno de la prostata que dificulta orinar. Damos un medicamento que relaja el cuello de "
      "la vejiga; si la prostata es grande, otro que la reduce.",
      "Tacto rectal + PSA para descartar cancer. <b>Retencion aguda de orina</b> = sondar (urgencia). Evita "
      "anticolinergicos/descongestivos (precipitan retencion).", ["hpb"])

menos(deck_m, "Cancer de prostata (sospecha/tamizaje)",
      "<b>PSA + tacto rectal</b>; decision de tamizar <b>individualizada</b> (consentimiento informado, 50-70 a). "
      "Sospecha (PSA alto/nodulo duro) &rarr; <b>referir urologia</b> (RM/biopsia).",
      "Buscamos cancer de prostata con un analisis de sangre (PSA) y un tacto; le explico pros y contras antes de "
      "hacerlo. Si algo sale anormal, lo refiero al urologo.",
      "Tacto con <b>nodulo duro/irregular</b> o PSA elevado/creciente &rarr; referir. Tamizaje compartido (no "
      "universal): valora expectativa de vida y preferencias.", ["ca_prostata"])

menos(deck_m, "Hipertiroidismo / Graves",
      "<b>Betabloqueante</b> para sintomas + <b>tionamida (metimazol)</b>; definitivo: <b>yodo radiactivo o "
      "cirugia</b>. Referir endocrino. PTU en 1er trimestre del embarazo.",
      "La tiroides produce hormona de mas y acelera el cuerpo (palpitaciones, perdida de peso, temblor). Damos "
      "medicamento para frenarla y otro para los sintomas; a veces tratamiento definitivo.",
      "Vigila <b>agranulocitosis</b> con tionamida (fiebre/odinofagia &rarr; suspender + hemograma). Tormenta "
      "tiroidea = urgencia.", ["hipertiroidismo"])

menos(deck_m, "Sindrome de Cushing",
      "<b>Sospecha clinica</b> (obesidad central, estrias violaceas, giba, cara de luna, HTA, DM, equimosis) &rarr; "
      "<b>cribado</b> (cortisol libre urinario 24 h, supresion con dexametasona, cortisol salival nocturno) &rarr; "
      "<b>referir endocrino</b>.",
      "Es un exceso de cortisol (la hormona del estres). Sospechamos por el aspecto y la presion/azucar altas; "
      "confirmamos con analisis y lo enviamos al endocrinologo.",
      "Causa exogena (esteroides) es la mas frecuente: pregunta por uso cronico de corticoides antes de buscar "
      "tumor.", ["cushing"])

menos(deck_m, "Pie diabetico",
      "<b>Clasificar</b> (Wagner/IWGDF): valorar <b>infeccion, isquemia (pulsos/ITB) y neuropatia</b>. "
      "Control glucemico + descarga + curacion; <b>antibiotico</b> si infeccion; <b>referir</b> urgente si isquemia "
      "critica, absceso, gangrena u osteomielitis.",
      "Es una ulcera/infeccion del pie por la diabetes (dana nervios y circulacion). Limpiamos y descargamos la "
      "herida, controlamos la glucosa y, si hay infeccion o mala circulacion, referimos.",
      "Eritema ascendente, crepitos, mal estado, isquemia o hueso expuesto = urgencia (amputacion/sepsis). "
      "Exploracion del pie y educacion en TODO diabetico.", ["pie_diabetico"])

menos(deck_m, "Sepsis",
      "<b>Bundle de 1 hora</b>: lactato, hemocultivos antes del antibiotico, <b>antibiotico amplio espectro</b>, "
      "cristaloide 30 mL/kg, vasopresor si TAM &lt;65. <b>Estabilizar + referir/UCI</b>. Control del foco.",
      "(urgencia) Es una infeccion grave que afecta todo el cuerpo. Iniciamos antibiotico y sueros de inmediato y "
      "lo trasladamos; buscamos el origen para controlarlo.",
      "qSOFA &ge;2 (TA &le;100, FR &ge;22, confusion). El antibiotico en la 1a hora salva vidas; no lo retrases.",
      ["sepsis"])

menos(deck_m, "Emergencia hipertensiva",
      "TA muy alta + <b>dano agudo de organo</b> (EVC, SCA, edema pulmonar, diseccion, eclampsia, encefalopatia) "
      "&rarr; <b>IV en monitor</b>, bajar TAM ~10-25% en la 1a hora. <b>Referir/urgencias</b>.",
      "(urgencia) La presion esta tan alta que ya esta danando un organo. Hay que bajarla de forma controlada en el "
      "hospital, no de golpe.",
      "Sin dano de organo es <b>urgencia</b> (no emergencia): VO gradual. Bajar demasiado rapido causa isquemia. "
      "Diseccion y eclampsia SI requieren bajada rapida.", ["emergencia_htas"])

menos(deck_m, "Cetoacidosis diabetica (CAD)",
      "<b>Liquidos IV + insulina IV en infusion + reposicion de potasio</b> + tratar el desencadenante. "
      "<b>Referir/hospital</b>. Monitorizar glucosa, K, brecha y pH.",
      "(urgencia) La diabetes se descompenso con acidos en sangre. Reponemos liquidos, damos insulina en vena y "
      "vigilamos el potasio de cerca.",
      "<b>No inicies insulina si K &lt;3.3</b> (repon K primero). Anade glucosa al suero al bajar de ~200.",
      ["cad"])

menos(deck_m, "Hipoglucemia",
      "<b>Consciente</b>: <b>15 g de glucosa VO</b> (regla del 15) y reevaluar. <b>Inconsciente/no via oral</b>: "
      "<b>glucosa IV</b> (o glucagon IM si no hay acceso). Buscar y corregir la causa (insulina/sulfonilurea, "
      "ayuno, alcohol, sepsis).",
      "El azucar esta peligrosamente bajo. Le doy azucar de absorcion rapida; si no puede tragar o esta "
      "inconsciente, glucosa por vena o una inyeccion de glucagon. Luego ajustamos su tratamiento.",
      "Sulfonilureas dan hipoglucemia prolongada/recurrente (observar/ingresar). Siempre <b>glucemia capilar</b> en "
      "todo paciente con alteracion del estado de alerta.", ["hipoglucemia"])

menos(deck_m, "Tormenta tiroidea",
      "<b>Betabloqueante (propranolol) + tionamida (PTU) + yodo (1 h despues) + hidrocortisona</b> + antitermicos "
      "+ tratar el gatillo. <b>Referir/UCI</b>.",
      "(urgencia) La tiroides esta hiperactiva al extremo y afecta corazon y temperatura. Damos varios "
      "medicamentos en secuencia para frenarla y lo trasladamos.",
      "El <b>orden importa</b>: tionamida ANTES que el yodo. Betabloqueante controla la tormenta simpatica.",
      ["tormenta_tiroidea"])

menos(deck_m, "Crisis suprarrenal (addisoniana)",
      "<b>Hidrocortisona 100 mg IV de inmediato</b> (no esperar confirmacion) + <b>liquidos IV (salino + "
      "glucosa)</b> + tratar el desencadenante. <b>Referir/urgencias</b>.",
      "(urgencia) Las glandulas suprarrenales no producen cortisol y entra en choque. La cortisona en vena y los "
      "sueros son inmediatos y salvan la vida.",
      "Sospecha: hipotension que no responde a liquidos + hiponatremia + hiperkalemia + hipoglucemia. No retrases "
      "la hidrocortisona por estudios.", ["crisis_suprarrenal"])

menos(deck_m, "VIH (tamizaje y abordaje inicial)",
      "<b>Ofrecer prueba</b> (al menos una vez a todo adulto; mas si riesgo) con consentimiento. Reactiva &rarr; "
      "<b>confirmar y referir</b> a inicio de TAR (lo antes posible). Ofrecer <b>PrEP</b> a personas en riesgo.",
      "Le ofrezco la prueba de VIH; es voluntaria y confidencial. Si saliera positiva, hoy hay tratamiento muy "
      "efectivo que permite vivir sano; lo enlazo de inmediato con atencion especializada.",
      "Tamizaje universal al menos una vez (no solo 'grupos de riesgo'). PrEP previene en personas de alto riesgo. "
      "Cribar ITS y tuberculosis al diagnostico.", ["vih"])


def build():
    for d, f in [(deck_e, "Manejo_01_Ejes.apkg"), (deck_c, "Manejo_02_Core.apkg"), (deck_m, "Manejo_03_Menos.apkg")]:
        genanki.Package(d).write_to_file(os.path.join(OUTPUT_DIR, f))
        print(f"  -> {f} ({len(d.notes)} notas)")
    genanki.Package([deck_e, deck_c, deck_m]).write_to_file(
        os.path.join(OUTPUT_DIR, "No_Hay_Tiempo_MF_Manejo_TODOS.apkg"))
    print(f"  -> TODOS ({sum(len(d.notes) for d in [deck_e, deck_c, deck_m])} notas)")


if __name__ == "__main__":
    build()
