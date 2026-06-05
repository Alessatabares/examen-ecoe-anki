"""No hay tiempo / Pediatria — PILAR MANEJO (ejes/patrones madre + core + menos).

Carta de manejo (Back): VERBALIZO (al sinodal) / CONDUCTA-CONSEJERIA / CIERRE (red flag).
Carta de eje (Back): REGLA MADRE / BIFURCACION / TRAMPA.
Enfoque pediatrico de rescate: TEP, dosis/equipo por peso-edad, fiebre por edad, prevencion.
Guia: AAP, AHA/PALS, GINA, OMS, Nelson, GPC MX.
"""
import os
import genanki

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "output")
os.makedirs(OUTPUT_DIR, exist_ok=True)

MODEL_QA_ID = 1990010901
DECK_ID_E, DECK_ID_C, DECK_ID_M = 1990010001, 1990010002, 1990010003
DECK_NAME_E = "No hay tiempo::Pediatria::1 - Ejes / patrones madre"
DECK_NAME_C = "No hay tiempo::Pediatria::2 - Manejos comunes (core)"
DECK_NAME_M = "No hay tiempo::Pediatria::3 - Menos comunes"

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
model_qa = genanki.Model(MODEL_QA_ID, "NHT Ped Manejo QA",
    fields=[{"name": "Front"}, {"name": "Back"}],
    templates=[{"name": "QA", "qfmt": "{{Front}}", "afmt": '{{Front}}<hr id="extra">{{Back}}'}],
    css=CSS_BASE)

deck_e = genanki.Deck(DECK_ID_E, DECK_NAME_E)
deck_c = genanki.Deck(DECK_ID_C, DECK_NAME_C)
deck_m = genanki.Deck(DECK_ID_M, DECK_NAME_M)
BASE_TAGS = ["pediatria", "ecoe", "no_hay_tiempo"]


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
add(deck_e, caso("EJE 1 — Triangulo de Evaluacion Pediatrica (TEP): primero '&iquest;se ve mal?'"),
    eje("Imagen: un triangulo que miro DESDE LA PUERTA, antes de tocar. <b>Apariencia</b> (tono, interaccion, "
        "consuelo, mirada, llanto), <b>Respiracion</b> (ruidos, tiraje, postura), <b>Circulacion</b> (color: "
        "palidez, cianosis, piel marmorea).",
        "Los 3 normales &rarr; estable (tengo tiempo). <b>Apariencia alterada</b> &rarr; disfuncion del SNC/"
        "metabolico/sepsis. <b>+ Respiracion</b> &rarr; dificultad respiratoria. <b>+ Circulacion</b> &rarr; choque. "
        "Los 3 alterados &rarr; falla cardiopulmonar.",
        "El TEP guia la urgencia ANTES del diagnostico fino. Un nino 'que se ve mal' se estabiliza ya, no se manda "
        "a la sala de espera."),
    E + ["tep"])

add(deck_e, caso("EJE 2 — El lactante FEBRIL se estratifica por EDAD: mas chico = mas estudio"),
    eje("Imagen: una escalera de edad. A menor edad, menor capacidad de localizar la infeccion y mayor riesgo de "
        "infeccion bacteriana grave (IBG), asi que bajo el umbral para estudiar y tratar.",
        "<b>&le;28 dias</b>: estudio completo (sangre, orina, <b>LCR</b>) + antibiotico empirico + ingreso, SIEMPRE. "
        "<b>29-60 d</b>: sangre + orina; PL y manejo segun biomarcadores (PCT/PCR). <b>&gt;3 meses</b>: buscar foco; "
        "manejo segun aspecto.",
        "Un neonato febril <b>nunca</b> es 'observacion en casa': estudio completo y antibiotico aunque se vea bien. "
        "Fiebre relevante = temperatura RECTAL &ge;38 C."),
    E + ["fiebre_edad"])

add(deck_e, caso("EJE 3 — En pediatria TODO es por PESO/EDAD: dosis, equipo, signos vitales"),
    eje("Imagen: no hay 'talla unica'. Calculo dosis en <b>mg/kg</b>, elijo equipo por edad/peso (cinta de "
        "Broselow), e interpreto FC/FR/TA segun la edad. <b>Glucemia capilar</b> en todo nino grave/alterado.",
        "Reanimacion: liquidos en <b>bolos de 10-20 mL/kg</b>; adrenalina, antibioticos, anticonvulsivos: todos por "
        "kg. Signos vitales normales cambian con la edad (el lactante es taquicardico y taquipneico de base).",
        "Aplicar cifras o dosis de adulto al nino es error grave. La <b>hipoglucemia</b> imita y agrava cualquier "
        "cuadro: medila siempre."),
    E + ["por_peso"])

add(deck_e, caso("EJE 4 — Fiebre + exantema: el PRODROMO + la morfologia dan el dx (y separo lo grave)"),
    eje("Imagen: leo el exantema como un texto (tipo de lesion, distribucion, que vino antes). La mayoria son "
        "virales benignos, pero <b>cribo lo que mata</b>.",
        "Maculopapular + Koplik/coriza &rarr; sarampion. Vesiculas en distintos estadios &rarr; varicela. Piel en "
        "lija + lengua aframbuesada &rarr; escarlatina. <b>Fiebre &ge;5 d + criterios</b> &rarr; Kawasaki.",
        "<b>Petequias/purpura que no desaparecen a la presion + mal estado</b> = meningococemia &rarr; antibiotico "
        "YA. No la confundas con un exantema viral."),
    E + ["fiebre_exantema"])

add(deck_e, caso("EJE 5 — Deshidratacion: clasifico el GRADO y elijo plan A/B/C"),
    eje("Imagen: un semaforo de hidratacion. Estimo perdidas por signos clinicos (no por el germen) y elijo la via.",
        "<b>Plan A</b> (sin deshidratacion): liquidos en casa + seguir alimentando. <b>Plan B</b> (leve-moderada): "
        "<b>rehidratacion oral con sales</b> (SRO) ~50-100 mL/kg en 4 h, supervisada. <b>Plan C</b> (grave/choque): "
        "<b>liquidos IV</b> en bolos.",
        "La via oral es de eleccion salvo choque, ileo o intolerancia. Vigila datos de deshidratacion grave: "
        "letargia, ojos hundidos, signo del pliegue lento, anuria, llenado capilar lento."),
    E + ["deshidratacion"])

add(deck_e, caso("EJE 6 — Estridor = obstruccion de via aerea ALTA: y NO agito al nino"),
    eje("Imagen: el aire silba al pasar por un tubo estrecho. El estridor inspiratorio localiza la obstruccion "
        "arriba; mi prioridad es mantener al nino <b>tranquilo</b> (el llanto empeora la obstruccion).",
        "<b>Tos perruna + estridor + febricula</b> &rarr; crup (dexametasona; adrenalina nebulizada si grave). "
        "<b>Fiebre alta + babeo + posicion en tripode + aspecto toxico</b> &rarr; epiglotitis (no explorar la "
        "garganta; via aerea en quirofano). <b>Inicio subito atragantandose</b> &rarr; cuerpo extrano.",
        "En epiglotitis NO bajalenguas ni maniobras que agiten: pueden cerrar la via aerea. Mantener al nino con "
        "su cuidador, comodo."),
    E + ["estridor"])

add(deck_e, caso("EJE 7 — Choque pediatrico: la TAQUICARDIA es precoz; la HIPOTENSION es TARDIA"),
    eje("Imagen: el nino compensa y compensa... hasta que cae de golpe. El choque <b>compensado</b> (taquicardia, "
        "llenado capilar lento, frialdad distal, oliguria) precede a la <b>hipotension</b>, que es signo "
        "preterminal.",
        "<b>Compensado</b> &rarr; reconocer y tratar YA (bolos 10-20 mL/kg, repetir, valorar inotropico). "
        "<b>Hipotenso</b> &rarr; choque descompensado, urgencia maxima. El mas frecuente es el <b>hipovolemico</b> "
        "(deshidratacion); tambien septico.",
        "Esperar a que caiga la TA para actuar es tarde. La taquicardia persistente sin causa clara (dolor/fiebre) "
        "es choque hasta demostrar lo contrario."),
    E + ["choque"])

add(deck_e, caso("EJE 8 — El nino sano tambien es consulta: vacunas, desarrollo, crecimiento y MALTRATO"),
    eje("Imagen: cada visita es prevencion. Reviso <b>esquema de vacunacion</b>, <b>hitos del desarrollo</b> "
        "(motor grueso/fino, lenguaje, social), <b>curvas de crecimiento</b> (peso/talla/PC) y el <b>entorno</b>.",
        "Vacunas incompletas &rarr; completar (oportunidad). Retraso del desarrollo o caida de percentiles &rarr; "
        "estudiar. <b>Lesiones que no encajan con la historia/edad</b> &rarr; sospecha de maltrato.",
        "Olvidar revisar vacunas/desarrollo o no reconocer banderas de <b>maltrato</b> (lesiones incongruentes, "
        "retraso en consultar, relato cambiante) es una falla grave. Notificar es obligacion."),
    E + ["nino_sano"])


# ===================== CORE / COMUNES (18) =====================
C = ["core"]
core(deck_c, "Reanimacion neonatal",
     "<b>Pasos iniciales</b> (calentar, secar, estimular, posicionar via aerea) y reevaluo. Si apnea/jadeo o "
     "<b>FC &lt;100</b> &rarr; <b>VPP</b> (lo mas importante). FC &lt;60 pese a VPP efectiva &rarr; compresiones "
     "<b>3:1</b> + adrenalina.",
     "Al nacer, lo que casi siempre necesita el bebe es ayuda para respirar (no masaje ni medicamentos). Secamos, "
     "estimulamos y, si no respira, ventilamos con mascarilla.",
     "La <b>ventilacion</b> es la piedra angular (la causa del paro neonatal es respiratoria). Relacion 3:1 (90 "
     "compresiones + 30 ventilaciones/min). Pinzamiento tardio del cordon si esta vigoroso.", C + ["rcp_neonatal"])

core(deck_c, "Ictericia neonatal / hiperbilirrubinemia",
     "Trato segun <b>bilirrubina total vs umbral por edad en HORAS + EG + factores de riesgo</b> (nomograma AAP): "
     "<b>fototerapia</b> sobre el umbral; exanguinotransfusion si muy alta/datos de encefalopatia.",
     "La piel amarilla del recien nacido suele ser normal, pero medimos la bilirrubina porque si sube mucho puede "
     "danar el cerebro. Si pasa el limite, usamos luz (fototerapia).",
     "<b>Patologica si: aparece &lt;24 h, sube rapido, o ictericia que persiste</b>. La &lt;24 h sugiere hemolisis "
     "(incompatibilidad). Vigila kernicterus (letargia, hipertonia, llanto agudo).", C + ["ictericia"])

core(deck_c, "Sepsis neonatal",
     "<b>Hemocultivo + estudio (orina, valorar LCR) y NO retrasar el antibiotico empirico</b>. Precoz (&lt;72 h, "
     "vertical): <b>ampicilina + gentamicina</b> (SGB, Listeria, E. coli). Tardia: cobertura nosocomial.",
     "El recien nacido puede infectarse gravemente con signos sutiles (come mal, esta decaido, temperatura "
     "inestable). Tomamos cultivos y empezamos antibiotico de inmediato.",
     "Los signos son INESPECIFICOS (hipo/hipertermia, rechazo del alimento, apnea, ictericia). Ante la duda, trata. "
     "Precoz = SGB/Listeria/E. coli (de ahi la ampicilina).", C + ["sepsis_neonatal"])

core(deck_c, "Fiebre sin foco en lactante &lt; 3 meses",
     "Estratifico por <b>edad + biomarcadores</b>. <b>&le;28 d</b>: sangre + orina + <b>LCR</b> + antibiotico "
     "empirico + ingreso. <b>29-60 d</b>: sangre + orina; PL/antibiotico segun <b>PCT/PCR</b> y aspecto. "
     "Orina por <b>sondaje/suprapubica</b> (no bolsa).",
     "Un bebe con fiebre puede tener una infeccion seria sin un foco evidente. Por su edad hacemos estudios y, en "
     "los mas pequenos, antibiotico e ingreso por precaucion.",
     "Neonato febril = estudio completo + antibiotico SIEMPRE (aunque se vea bien). La muestra de orina valida NO "
     "es la de bolsa recolectora.", C + ["fiebre_sin_foco"])

core(deck_c, "ITU pediatrica",
     "<b>Urocultivo</b> de muestra valida (sondaje/suprapubica en el que no controla esfinter; chorro medio en el "
     "continente) + <b>antibiotico</b> (oral si tolera; IV si grave/lactante pequeno). <b>Ecografia renal</b> tras "
     "ITU febril.",
     "Es una infeccion de orina, que en el lactante puede dar solo fiebre. Confirmamos con un cultivo bien tomado y "
     "damos antibiotico; despues revisamos los rinones con un ultrasonido.",
     "En el lactante la ITU puede presentarse como <b>fiebre sin foco</b>. La muestra de bolsa solo sirve para "
     "descartar (no para confirmar). Valora reflujo si recurrente/atipica.", C + ["itu"])

core(deck_c, "Bronquiolitis (VRS)",
     "<b>Soporte</b>: hidratacion + <b>oxigeno si SatO2 &lt;90%</b> + lavados nasales. NO de rutina "
     "broncodilatadores, esteroides ni antibioticos. Vigilo dificultad respiratoria y alimentacion.",
     "Es la primera infeccion viral de los bronquiolos en menores de 2 anos; da tos, mocos y silbidos. No hay "
     "medicamento que la cure: cuidamos la respiracion y la hidratacion mientras pasa.",
     "Primer episodio de sibilancias en &lt;2 anos (VRS). Banderas de ingreso: <b>apneas, SatO2 baja, mala "
     "alimentacion, dificultad respiratoria, &lt;3 meses</b>.", C + ["bronquiolitis"])

core(deck_c, "Crup (laringotraqueitis)",
     "<b>Dexametasona a casi todos</b> (una dosis) + medidas de calma. <b>Estridor en reposo/grave</b> &rarr; "
     "<b>adrenalina nebulizada</b> + observacion. O2 si hipoxia.",
     "Es una inflamacion viral de la via aerea alta: tos perruna y un silbido al inhalar. Una dosis de cortisona "
     "desinflama; si esta agitado, mejor dejarlo tranquilo con su mama.",
     "Tos perruna + estridor inspiratorio + disfonia. Mantener al nino calmado (el llanto empeora el estridor). "
     "Diferenciar de epiglotitis (aspecto toxico, babeo, sin tos perruna).", C + ["crup"])

core(deck_c, "Neumonia pediatrica",
     "Valoro gravedad (<b>taquipnea</b> es el mejor signo). <b>Amoxicilina</b> de 1a linea en la tipica no "
     "complicada ambulatoria; IV/ingreso si grave, hipoxia o lactante pequeno. O2 e hidratacion.",
     "Es una infeccion del pulmon. Lo principal es el antibiotico (amoxicilina si es ambulatoria) y vigilar la "
     "respiracion y el oxigeno.",
     "<b>Taquipnea por edad (OMS)</b>: &lt;2 m &ge;60; 2-12 m &ge;50; 1-5 a &ge;40. Tiraje/hipoxia/mal estado = "
     "ingreso. Sospecha derrame/empiema si no mejora.", C + ["neumonia"])

core(deck_c, "Crisis asmatica pediatrica",
     "<b>Oxigeno</b> (meta SatO2) + <b>SABA (salbutamol) repetido</b> + <b>corticoide sistemico precoz</b> + "
     "ipratropio en grave. Reevaluo respuesta; magnesio IV si grave/refractaria.",
     "Es una crisis de asma: los bronquios se cierran. Abrimos con el inhalador repetido, damos cortisona y "
     "oxigeno; revisamos la tecnica del inhalador y el plan de control.",
     "Silencio auscultatorio, agotamiento, SatO2 baja o somnolencia = grave (riesgo de paro). Da el corticoide "
     "pronto (cambia el curso).", C + ["asma"])

core(deck_c, "Otitis media aguda (OMA)",
     "<b>Analgesia</b> siempre. <b>Amoxicilina a dosis altas</b> si &lt;6 meses, grave, bilateral en &lt;2 anos u "
     "otorrea; <b>observacion 48-72 h</b> en &ge;2 anos sin gravedad. Amoxi-clavulanico si falla/factores.",
     "Es una infeccion del oido medio. Lo primero es calmar el dolor; segun la edad y la gravedad damos antibiotico "
     "o esperamos 2-3 dias vigilando.",
     "Dx por <b>abombamiento timpanico</b> + derrame. Mastoiditis (oido protruido, eritema retroauricular, fiebre) "
     "&rarr; urgencia.", C + ["oma"])

core(deck_c, "Faringoamigdalitis estreptococica",
     "Estimo probabilidad con <b>Centor/McIsaac</b> y confirmo (prueba rapida/cultivo). Estreptococo confirmado "
     "&rarr; <b>penicilina o amoxicilina</b> (alergia: macrolido) + analgesia.",
     "Es dolor de garganta; muchas son virales. Si los datos y la prueba apuntan a estreptococo, damos antibiotico "
     "para evitar complicaciones.",
     "El antibiotico previene la <b>fiebre reumatica</b>. La mayoria en &lt;3 anos es viral (no suele ser "
     "estreptococo). No des antibiotico solo por la clinica sin probabilidad alta/prueba.", C + ["faringitis"])

core(deck_c, "Gastroenteritis aguda y deshidratacion",
     "Prioridad: <b>valorar el grado de deshidratacion</b> (no el germen) &rarr; plan: <b>A</b> (casa), <b>B</b> "
     "(SRO oral supervisada), <b>C</b> (IV si grave/choque). Seguir alimentando; zinc segun contexto. "
     "Antibiotico solo en casos especificos.",
     "Es una infeccion intestinal, casi siempre viral y autolimitada. Lo clave es reponer liquidos con suero oral y "
     "seguir alimentando; la mayoria no necesita antibiotico.",
     "La <b>rehidratacion oral</b> es de eleccion (salvo choque/intolerancia). Vigila deshidratacion grave. "
     "Evita antibiotico de rutina (riesgo de SHU en E. coli O157).", C + ["gea"])

core(deck_c, "Convulsion febril",
     "<b>Simple</b> (generalizada, &lt;15 min, una en 24 h, 6 m-5 a): el foco es la fiebre &rarr; <b>buscar y "
     "tratar el foco</b>, antitermicos, educacion; NO requiere de rutina EEG/TAC/PL. <b>Compleja</b> o atipica "
     "&rarr; estudiar.",
     "Es una convulsion por la fiebre en un nino pequeno; asusta mucho pero suele ser benigna y no deja secuela. "
     "Buscamos la causa de la fiebre y explicamos como actuar si se repite.",
     "Descarta <b>meningitis</b> si hay datos meningeos, mal estado o no se ve la fuente. Estatus (&gt;5 min) &rarr; "
     "benzodiacepina. Tranquiliza: la febril simple no es epilepsia.", C + ["convulsion_febril"])

core(deck_c, "Meningitis bacteriana (lactante / nino)",
     "<b>Antibiotico empirico urgente</b> (no esperar la PL si esta inestable) + valorar <b>dexametasona</b> + "
     "soporte. Empirico segun edad (neonato: ampicilina+cefotaxima; mayor: cefalosporina 3a &plusmn; vancomicina).",
     "(urgencia) Es una infeccion de las meninges; puede ser muy grave. Empezamos antibiotico de inmediato y "
     "hacemos una puncion lumbar para confirmar y dirigir el tratamiento.",
     "Lactante: signos sutiles (irritabilidad, rechazo, <b>fontanela abombada</b>, mala succion); Kernig/Brudzinski "
     "no son fiables en el bebe. <b>Petequias/purpura</b> = meningococemia (antibiotico YA).", C + ["meningitis"])

core(deck_c, "Enfermedad de Kawasaki",
     "<b>Inmunoglobulina IV + aspirina</b> lo antes posible (idealmente &lt;10 dias) + <b>ecocardiograma</b> "
     "(buscar aneurismas coronarios). Referir.",
     "Es una inflamacion de los vasos que se trata pronto con una infusion de anticuerpos y aspirina, porque lo "
     "importante es proteger las arterias del corazon.",
     "Dx: <b>fiebre &ge;5 dias + 4 de 5</b> (conjuntivitis no exudativa, labios/lengua aframbuesada, exantema, "
     "cambios en manos/pies, adenopatia cervical). El riesgo es el <b>aneurisma coronario</b>.", C + ["kawasaki"])

core(deck_c, "Paro pediatrico (PALS)",
     "<b>RCP de alta calidad</b> (100-120/min, 15:2 con 2 reanimadores) + ventilacion + tratar la causa. Ritmos "
     "<b>desfibrilables</b> (FV/TV sin pulso) &rarr; desfibrilar; <b>no desfibrilables</b> (asistolia/AESP, los mas "
     "frecuentes) &rarr; adrenalina + RCP.",
     "(urgencia) El corazon del nino se detuvo, casi siempre por falta de oxigeno. Lo principal es una buena "
     "reanimacion (compresiones y ventilacion) y corregir la causa.",
     "La causa mas frecuente del paro pediatrico es <b>hipoxica/respiratoria</b> (no cardiaca como el adulto): la "
     "ventilacion es clave. Dosis y energia por kg.", C + ["pals"])

core(deck_c, "Vacunacion (esquema del nino)",
     "Reviso y completo el <b>esquema segun edad</b> (oportunidad en cada visita). Aplico simultaneas las que "
     "correspondan; reinicio NO es necesario si hubo retraso (continuo donde quedo).",
     "Aprovecho la consulta para revisar las vacunas y poner las que falten segun su edad. Las vacunas previenen "
     "enfermedades graves; un retraso no obliga a empezar de cero.",
     "Contraindica vacunas de <b>virus vivos</b> en inmunodepresion grave y embarazo. La fiebre leve/catarro NO "
     "contraindica. No reinicies esquemas por retraso.", C + ["vacunas"])

core(deck_c, "Vigilancia del desarrollo y crecimiento",
     "Evaluo <b>hitos por areas</b> (motor grueso/fino, lenguaje, social) y <b>curvas</b> (peso, talla, perimetro "
     "cefalico). Tamizo desarrollo en visitas clave; intervengo/derivo si hay retraso o caida de percentiles.",
     "Reviso que el nino crezca y aprenda lo esperado para su edad. Si algo va lento o se sale de las curvas, lo "
     "estudiamos a tiempo, que es cuando mas se puede ayudar.",
     "Banderas: no sostiene cefalo, no sonrisa social, no sedestacion/marcha en tiempo, <b>perdida</b> de hitos "
     "(regresion = urgente), microcefalia/macrocefalia, caida de percentiles.", C + ["desarrollo"])


# ===================== MENOS COMUNES (22) =====================
menos(deck_m, "Meningitis neonatal",
      "<b>Antibiotico empirico que cubra SGB, Listeria y gramnegativos (ampicilina + cefotaxima)</b> + soporte; PL "
      "para confirmar/dirigir. Es parte del estudio de sepsis neonatal.",
      "(urgencia) En el recien nacido la infeccion de las meninges da signos sutiles. Iniciamos antibiotico de "
      "inmediato y confirmamos con puncion lumbar.",
      "Signos inespecificos (igual que sepsis): NO esperes signos meningeos clasicos. Cobertura distinta a la del "
      "nino mayor (Listeria!).", ["meningitis_neonatal"])

menos(deck_m, "Infecciones congenitas (TORCH)",
      "<b>Sospecho y estudio</b> (serologias/PCR madre-RN segun caso) y refiero. Toxoplasma, Otros (sifilis, VIH, "
      "varicela, zika), Rubeola, CMV (la mas frecuente), Herpes. Tratamiento dirigido por agente.",
      "Son infecciones que pasan de la madre al bebe durante el embarazo y pueden dejar secuelas. Se buscan con "
      "estudios y se tratan segun cual sea.",
      "Pistas: <b>CMV</b> (microcefalia, calcificaciones periventriculares, sordera); <b>toxo</b> (coriorretinitis, "
      "hidrocefalia, calcificaciones difusas); <b>sifilis/rubeola</b> (cardiopatia, sordera, hueso/ojo).", ["torch"])

menos(deck_m, "Conjuntivitis neonatal (oftalmia)",
      "Tiempo de aparicion orienta el agente y el tratamiento: <b>&lt;24 h</b> quimica; <b>2-5 d</b> <b>gonococo</b> "
      "(ceftriaxona IV, urgencia); <b>5-14 d</b> <b>Chlamydia</b> (eritromicina <b>oral</b>). Profilaxis ocular al "
      "nacer.",
      "Es una infeccion de los ojos del recien nacido. Segun cuando aparece sospechamos el germen; algunas (como "
      "el gonococo) son urgentes porque pueden danar el ojo.",
      "Gonococo (2-5 d): secrecion purulenta abundante &rarr; urgencia (perforacion corneal). Chlamydia se trata "
      "<b>oral</b> (cubre la neumonia asociada), no solo topico.", ["conjuntivitis_neonatal"])

menos(deck_m, "VIH perinatal",
      "<b>Prevencion</b>: TAR materna + profilaxis al RN + evitar lactancia (segun contexto/carga viral) + cesarea "
      "si carga alta. Dx del RN por <b>PCR/carga viral</b> (no serologia, por anticuerpos maternos). Referir.",
      "Si la mama vive con VIH, con tratamiento y medidas el riesgo de contagiar al bebe es muy bajo. Al bebe se le "
      "da profilaxis y se le hace una prueba especial (no la de anticuerpos).",
      "En el RN/lactante el dx es por <b>PCR/carga viral</b> (los anticuerpos son de la madre y dan falso +). "
      "Profilaxis antibiotica contra Pneumocystis segun guia.", ["vih_perinatal"])

menos(deck_m, "Epiglotitis (Hib)",
      "<b>URGENCIA de via aerea</b>: NO explorar la garganta ni agitar; mantener al nino comodo con su cuidador; "
      "<b>via aerea en quirofano</b> (intubacion/traqueostomia disponible) + <b>antibiotico (cefalosporina 3a)</b>.",
      "(urgencia) Es una inflamacion grave de la epiglotis que puede cerrar la via aerea. No revisamos la garganta "
      "para no empeorar; aseguramos la respiracion en quirofano y damos antibiotico.",
      "Aspecto <b>toxico + babeo + posicion en tripode + voz apagada + SIN tos perruna</b>. Casi desaparecida por la "
      "vacuna Hib. NO uses bajalenguas (puede provocar paro).", ["epiglotitis"])

menos(deck_m, "Tos ferina (Bordetella pertussis)",
      "<b>Macrolido (azitromicina)</b> + aislamiento + <b>profilaxis a contactos</b>. Soporte (el lactante pequeno "
      "puede requerir ingreso por apneas). Prevencion: <b>vacuna (incluida Tdap en el embarazo)</b>.",
      "Es una tos muy intensa por una bacteria. Damos un antibiotico (mas util temprano), protegemos a los "
      "contactos y vigilamos al bebe, que es quien mas se complica.",
      "Fases: catarral &rarr; <b>paroxistica</b> (accesos + 'gallo' inspiratorio + vomito postusivo) &rarr; "
      "convalecencia. En &lt;6 meses puede dar <b>apnea sin tos clasica</b> (peligroso).", ["tos_ferina"])

menos(deck_m, "Sarampion",
      "<b>Soporte + vitamina A</b> + aislamiento. Notificacion obligatoria. Prevencion: vacuna SRP.",
      "Es una enfermedad viral muy contagiosa con fiebre alta y salpullido. No hay tratamiento especifico (damos "
      "vitamina A y soporte); lo importante es vacunar y aislar.",
      "<b>Manchas de Koplik</b> + fiebre, tos, coriza, conjuntivitis, luego exantema cefalo-caudal. Complicaciones: "
      "neumonia, encefalitis. Enfermedad de notificacion.", ["sarampion"])

menos(deck_m, "Escarlatina",
      "<b>Penicilina/amoxicilina</b> (es estreptococo del grupo A) + analgesia.",
      "Es una infeccion por la misma bacteria de la faringitis estreptococica, con un salpullido aspero. Se trata "
      "con antibiotico, que ademas previene complicaciones.",
      "<b>Lengua aframbuesada + piel en lija</b> + faringitis + lineas de Pastia; descamacion posterior. "
      "El antibiotico previene la fiebre reumatica.", ["escarlatina"])

menos(deck_m, "Varicela",
      "<b>Soporte</b> (antihistaminico, antitermico -<b>NO aspirina</b>-, cuidado de la piel). Aciclovir en grupos "
      "de riesgo (adolescente/adulto, inmunodeprimido, neonato). Prevencion: vacuna.",
      "Es el virus de la varicela: ampollas con comezon en distintas etapas. En el nino sano suele ser leve y se "
      "trata el sintoma; evitamos rascado e infeccion de las lesiones.",
      "<b>Vesiculas en distintos estadios</b> a la vez. <b>NO aspirina</b> (sindrome de Reye). Vigila "
      "sobreinfeccion bacteriana de las lesiones.", ["varicela"])

menos(deck_m, "Exantema subito (roseola, VHH-6)",
      "<b>Soporte</b>; es benigno y autolimitado. Tranquilizar.",
      "Es un virus benigno del lactante: fiebre alta unos dias y, cuando se quita la fiebre, aparece el salpullido. "
      "No necesita tratamiento.",
      "Patron clasico: <b>fiebre alta 3 dias que cede y APARECE el exantema al desaparecer la fiebre</b>. Causa "
      "frecuente de convulsion febril.", ["roseola"])

menos(deck_m, "Eritema infeccioso (5a enfermedad, parvovirus B19)",
      "<b>Soporte</b>. Vigilar en grupos especiales (anemia/crisis aplasica en hemoglobinopatias; riesgo fetal en "
      "embarazo &rarr; hidrops).",
      "Es un virus que da el aspecto de 'mejillas abofeteadas' y luego un salpullido en encaje. En el nino sano es "
      "leve, pero hay que avisar en el embarazo.",
      "<b>'Cara abofeteada'</b> + exantema reticular. Cuando aparece el exantema <b>ya casi no contagia</b>. "
      "Riesgo: crisis aplasica (anemias) y dano fetal en embarazadas.", ["eritema_infeccioso"])

menos(deck_m, "Mano-pie-boca (coxsackie)",
      "<b>Soporte + analgesia/hidratacion</b> (vigilar que beba por las ulceras de la boca). Benigno y autolimitado.",
      "Es un virus que da ampollas en manos, pies y boca. Lo importante es el dolor de las llagas de la boca: "
      "cuidamos que el nino siga bebiendo para que no se deshidrate.",
      "Vesiculas en <b>manos, pies y boca</b>. Vigila deshidratacion por rechazo a tragar (ulceras dolorosas).", ["mano_pie_boca"])

menos(deck_m, "Rubeola",
      "<b>Soporte</b>; notificacion. Prevencion: vacuna SRP. Importancia real: <b>rubeola congenita</b> si infecta "
      "a embarazada.",
      "Es un virus leve en el nino (fiebre baja, salpullido, ganglios detras de las orejas). Lo grave es si lo "
      "contrae una embarazada, por el dano al bebe.",
      "Adenopatias <b>retroauriculares/occipitales</b> + exantema leve. El gran riesgo es la <b>rubeola "
      "congenita</b> (sordera, cardiopatia, cataratas).", ["rubeola"])

menos(deck_m, "Impetigo / infecciones de piel",
      "<b>Impetigo localizado</b>: antibiotico <b>topico</b> (mupirocina). Extenso o con celulitis: antibiotico "
      "<b>oral</b> (cubrir S. aureus y estreptococo). Higiene; evitar contagio.",
      "Es una infeccion superficial de la piel con costras color miel. Si es poca, una pomada antibiotica basta; si "
      "es extensa o hay celulitis, antibiotico por boca.",
      "Costra <b>melicerica</b> (color miel). Vigila celulitis (eritema caliente que avanza) y, tras impetigo "
      "estreptococico, glomerulonefritis posestreptococica.", ["impetigo"])

menos(deck_m, "Parasitosis intestinal",
      "Tratamiento segun agente: <b>antihelmintico (albendazol/mebendazol)</b> en geohelmintos/oxiuros; "
      "<b>metronidazol</b> en giardia/amebas. Medidas higienicas y, segun contexto, desparasitacion familiar.",
      "Son lombrices o parasitos del intestino. Damos un antiparasitario segun cual sea y reforzamos higiene "
      "(lavado de manos, agua segura) para evitar reinfeccion.",
      "Oxiuros: prurito anal nocturno (test de Graham). Giardia: diarrea cronica/malabsorcion. Anemia + "
      "geohelmintos en zonas endemicas.", ["parasitosis"])

menos(deck_m, "Maltrato infantil / lesion no accidental",
      "<b>Garantizo la seguridad del nino + estudio dirigido</b> (exploracion completa, fondo de ojo, serie osea/"
      "imagen segun edad) + documento textual y objetivamente + <b>NOTIFICO</b> (es obligacion legal).",
      "(con tacto, sin acusar) Algunas lesiones no encajan con lo relatado y debemos protegerlo. Hacemos estudios y, "
      "por ley, damos aviso a las autoridades de proteccion para cuidar al nino.",
      "Banderas: <b>lesion incongruente con la historia o la edad/desarrollo</b>, retraso en consultar, relato "
      "cambiante, lesiones patognomonicas (hemorragias retinianas, fracturas en distintos estadios, quemaduras en "
      "guante/calcetin). Notificar es obligatorio.", ["maltrato"])

menos(deck_m, "Atragantamiento / cuerpo extrano en via aerea",
      "<b>Tos efectiva</b> &rarr; animar a toser, NO intervenir. <b>Tos inefectiva consciente</b>: lactante "
      "<b>5 golpes interescapulares + 5 compresiones toracicas</b>; nino <b>maniobra de Heimlich</b>. "
      "<b>Inconsciente</b> &rarr; RCP.",
      "(urgencia) Si algo le obstruye la via aerea y tose bien, lo dejamos toser. Si no puede, hacemos maniobras "
      "segun la edad para sacarlo; si pierde el conocimiento, iniciamos reanimacion.",
      "<b>NO hagas barrido digital a ciegas</b> (empuja el objeto). En el lactante: golpes en la espalda + "
      "compresiones toracicas (no Heimlich abdominal).", ["atragantamiento"])

menos(deck_m, "Anemia ferropenica del lactante",
      "<b>Hierro oral</b> + ajuste de la dieta (reducir leche de vaca, introducir alimentos ricos en hierro). "
      "Tamizo segun riesgo. Busco la causa (dieta, prematuridad, perdidas).",
      "Es falta de hierro, muy comun por tomar mucha leche de vaca y poco hierro en la dieta. Damos hierro y "
      "ajustamos la alimentacion; mejora la energia y el desarrollo.",
      "<b>Exceso de leche de vaca</b> (&gt;500-700 mL/d o antes del ano) es causa clasica. Afecta el "
      "neurodesarrollo: tamiza y trata. Microcitica con ferritina baja.", ["ferropenia"])

menos(deck_m, "Displasia del desarrollo de la cadera (DDC)",
      "<b>Tamizaje clinico</b> (Ortolani/Barlow en el RN; limitacion de la abduccion y asimetria de pliegues mas "
      "tarde) + <b>USG de cadera</b> (&lt;6 meses) o Rx (&gt;6 meses). Referir a ortopedia (arnes de Pavlik).",
      "Es una cadera que no encaja bien desde el nacimiento. La buscamos en las revisiones del bebe; si se detecta "
      "pronto, se corrige con un arnes y se evita la cirugia.",
      "Factores: <b>presentacion pelvica, sexo femenino, antecedente familiar</b>. Detectarla temprano cambia el "
      "pronostico (evita cirugia/artrosis). Ortolani/Barlow en toda revision del RN.", ["ddc"])

menos(deck_m, "Abdomen quirurgico pediatrico (enlace a Cirugia)",
      "Reconozco y <b>refiero</b>: <b>invaginacion</b> (lactante, dolor colico + 'heces en jalea de grosella' + "
      "masa &rarr; enema; cirugia si falla/perforacion); <b>estenosis pilorica</b> (vomito en proyectil no bilioso, "
      "3-6 sem, alcalosis &rarr; corregir y piloromiotomia); apendicitis.",
      "Algunos dolores de panza del nino son quirurgicos. Los reconozco para enviarlo pronto al hospital; el detalle "
      "del manejo esta en el deck de Cirugia.",
      "<b>Vomito BILIOSO en el RN/lactante = malrotacion/volvulo hasta demostrar lo contrario</b> (urgencia). "
      "Invaginacion: la triada completa es tardia; sospecha con dolor colico intermitente + decaimiento.", ["abdomen_qx"])

menos(deck_m, "Soplo / cardiopatia (enlace a Ruidos Cardiacos)",
      "Distingo <b>soplo inocente</b> (asintomatico, sistolico suave, sin otros datos, varia con la posicion) de "
      "<b>patologico</b> (refiero + ecocardiograma). Cianosis/insuficiencia &rarr; urgencia.",
      "Muchos soplos del nino son normales ('inocentes') y no necesitan nada. Si hay datos de alarma, lo enviamos "
      "para un ultrasonido del corazon.",
      "Banderas (referir): <b>cianosis</b>, soplo diastolico/holosistolico/intenso, pulsos femorales debiles "
      "(coartacion), mala ganancia de peso, fatiga con la toma. Detalle en el deck de Ruidos Cardiacos.", ["soplo"])


def build():
    for d, f in [(deck_e, "Manejo_01_Ejes.apkg"), (deck_c, "Manejo_02_Core.apkg"), (deck_m, "Manejo_03_Menos.apkg")]:
        genanki.Package(d).write_to_file(os.path.join(OUTPUT_DIR, f))
        print(f"  -> {f} ({len(d.notes)} notas)")
    genanki.Package([deck_e, deck_c, deck_m]).write_to_file(
        os.path.join(OUTPUT_DIR, "No_Hay_Tiempo_Ped_Manejo_TODOS.apkg"))
    print(f"  -> TODOS ({sum(len(d.notes) for d in [deck_e, deck_c, deck_m])} notas)")


if __name__ == "__main__":
    build()
