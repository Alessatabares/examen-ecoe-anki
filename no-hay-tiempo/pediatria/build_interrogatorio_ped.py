"""No hay tiempo / Pediatria — PILAR INTERROGATORIO (tronco + llaves).

Tronco contextual por motivo de consulta + llave que fija el dx (incluye al cuidador).
Guia: AAP, AHA/PALS, GINA, OMS, Nelson, GPC MX.
"""
import os
import genanki

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "output")
os.makedirs(OUTPUT_DIR, exist_ok=True)

MODEL_QA_ID = 1990010902
DECK_ID_T, DECK_ID_C, DECK_ID_M = 1990010011, 1990010012, 1990010013
DECK_NAME_T = "No hay tiempo::Pediatria::Interrogatorio::1 - Troncos (ejes)"
DECK_NAME_C = "No hay tiempo::Pediatria::Interrogatorio::2 - Llaves comunes (core)"
DECK_NAME_M = "No hay tiempo::Pediatria::Interrogatorio::3 - Llaves menos comunes"

CSS_BASE = """
.card { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  font-size: 19px; text-align: left; color: #1a1a1a; background-color: #fafafa;
  padding: 20px; line-height: 1.55; }
.caso { font-size: 21px; font-weight: 700; color: #1e3a8a; }
#extra { margin-top: 16px; border: none; border-top: 1px solid #d4d4d4; padding-top: 12px; }
.bloque { display: block; margin: 12px 0; padding: 10px 14px; border-radius: 8px; }
.lab { display: block; font-size: 13px; font-weight: 700; letter-spacing: .5px;
  text-transform: uppercase; margin-bottom: 4px; }
.contexto { background: #eef2ff; border-left: 4px solid #1e3a8a; }
.ramifica { background: #f5f3ff; border-left: 4px solid #6d28d9; }
.llave { background: #eef2ff; border-left: 4px solid #1e3a8a; }
.patron { background: #f5f3ff; border-left: 4px solid #6d28d9; }
.dx { background: #ecfdf5; border-left: 4px solid #047857; }
.contexto .lab { color: #1e3a8a; } .ramifica .lab { color: #6d28d9; }
.llave .lab { color: #1e3a8a; } .patron .lab { color: #6d28d9; } .dx .lab { color: #047857; }
.dx b { color: #065f46; }
b { color: #111; }
"""
model_qa = genanki.Model(MODEL_QA_ID, "NHT Ped Interrogatorio QA",
    fields=[{"name": "Front"}, {"name": "Back"}],
    templates=[{"name": "QA", "qfmt": "{{Front}}", "afmt": '{{Front}}<hr id="extra">{{Back}}'}],
    css=CSS_BASE)

deck_t = genanki.Deck(DECK_ID_T, DECK_NAME_T)
deck_c = genanki.Deck(DECK_ID_C, DECK_NAME_C)
deck_m = genanki.Deck(DECK_ID_M, DECK_NAME_M)
BASE_TAGS = ["pediatria", "ecoe", "no_hay_tiempo", "interrogatorio"]


def add(deck, front, back, tags):
    deck.add_note(genanki.Note(model=model_qa, fields=[front, back], tags=BASE_TAGS + tags))

def caso(t): return f'<span class="caso">{t}</span>'

def tronco(ctx, ram):
    return (f'<span class="bloque contexto"><span class="lab">Pregunto siempre (contexto)</span>{ctx}</span>'
            f'<span class="bloque ramifica"><span class="lab">Esto me ramifica (sintoma guia -&gt; dx)</span>{ram}</span>')

def llave(p, pat, dx):
    return (f'<span class="bloque llave"><span class="lab">Pregunta-llave</span>{p}</span>'
            f'<span class="bloque patron"><span class="lab">Patron que confirma</span>{pat}</span>'
            f'<span class="bloque dx"><span class="lab">Diagnostico</span><b>{dx}</b></span>')


# ===================== TRONCOS (8) =====================
T = ["tronco"]
add(deck_t, caso("TRONCO — Fiebre en el nino (por edad)"),
    tronco("<b>Edad</b> (clave), temperatura y forma de medirla, dias de fiebre, <b>foco</b> (respiratorio, oido, "
           "orina, piel, ORL), <b>aspecto/TEP</b>, ingesta y diuresis (panales mojados), vacunas, contactos, "
           "viajes, exantema/petequias.",
           "<b>&lt;3 meses</b> &rarr; estratificar por edad (estudio). <b>Foco respiratorio/otico/urinario</b> &rarr; "
           "su entidad. <b>&ge;5 dias + criterios</b> &rarr; Kawasaki. <b>Petequias + mal estado</b> &rarr; "
           "meningococemia (urgencia)."),
    T + ["fiebre"])

add(deck_t, caso("TRONCO — Dificultad respiratoria / tos"),
    tronco("Edad, tiempo, <b>fiebre</b>, tipo de tos (perruna, accesos), <b>estridor vs sibilancias</b>, "
           "<b>tiraje/aleteo/quejido</b>, alimentacion, apneas, atopia, contacto/epidemia, vacunas, "
           "atragantamiento subito.",
           "<b>Sibilancias 1er episodio en &lt;2 a</b> &rarr; bronquiolitis. <b>Sibilancias recurrentes "
           "reversibles</b> &rarr; asma. <b>Tos perruna + estridor</b> &rarr; crup. <b>Fiebre + taquipnea + "
           "foco</b> &rarr; neumonia. <b>Inicio subito atragantado</b> &rarr; cuerpo extrano."),
    T + ["respiratorio"])

add(deck_t, caso("TRONCO — Fiebre + exantema"),
    tronco("<b>Pródromo</b> (que vino antes), <b>tipo de lesion</b> (mácula/pápula/vesícula/petequia) y "
           "<b>distribucion/progresion</b>, fiebre (dias y patron), enantema (boca), <b>vacunas</b>, contactos, "
           "<b>prurito</b>, estado general.",
           "<b>Koplik + coriza</b> &rarr; sarampion. <b>Vesiculas en estadios</b> &rarr; varicela. <b>Piel en "
           "lija + lengua aframbuesada</b> &rarr; escarlatina. <b>Fiebre 3 d que cede y aparece exantema</b> &rarr; "
           "roseola. <b>Petequias que no blanquean + mal estado</b> &rarr; meningococemia."),
    T + ["exantema"])

add(deck_t, caso("TRONCO — Vomito / diarrea / deshidratacion"),
    tronco("Numero y caracter de evacuaciones/vomitos, <b>sangre/moco</b>, <b>bilioso?</b>, fiebre, dolor, "
           "<b>diuresis (panales) y lagrimas</b>, ingesta de liquidos, peso previo, contactos/alimentos, edad.",
           "<b>Diarrea + vomito + valoro deshidratacion</b> &rarr; GEA (plan A/B/C). <b>Vomito en proyectil no "
           "bilioso 3-6 sem</b> &rarr; estenosis pilorica. <b>Vomito BILIOSO</b> &rarr; obstruccion/malrotacion "
           "(urgencia). <b>Colico + jalea de grosella</b> &rarr; invaginacion."),
    T + ["digestivo"])

add(deck_t, caso("TRONCO — Lactante que 'no se ve bien' / irritable / come mal"),
    tronco("<b>TEP</b> (apariencia), succion/ingesta, decaimiento vs irritabilidad inconsolable, fiebre o "
           "<b>hipotermia</b>, vomito, panales, fontanela, <b>antecedentes perinatales</b>, y el <b>entorno/relato</b> "
           "(coherencia, quien lo cuida).",
           "<b>Neonato decaido + come mal + temp inestable</b> &rarr; sepsis. <b>Irritabilidad + fontanela "
           "abombada</b> &rarr; meningitis. <b>Llanto colico + jalea de grosella</b> &rarr; invaginacion. "
           "<b>Lesiones incongruentes con el relato</b> &rarr; maltrato."),
    T + ["lactante_malo"])

add(deck_t, caso("TRONCO — Convulsion / evento neurologico"),
    tronco("<b>Fiebre?</b>, edad, duracion, <b>generalizada vs focal</b>, numero en 24 h, recuperacion, glucemia, "
           "trauma, toxicos, antecedentes (epilepsia, perinatales), desarrollo previo.",
           "<b>Fiebre + generalizada + &lt;15 min + 6 m-5 a</b> &rarr; convulsion febril simple. <b>Focal/"
           "prolongada/repetida</b> &rarr; compleja (estudiar). <b>Sin fiebre</b> &rarr; epilepsia/metabolico/"
           "lesion. <b>Datos meningeos/mal estado</b> &rarr; descartar meningitis."),
    T + ["convulsion"])

add(deck_t, caso("TRONCO — Recien nacido (problemas neonatales)"),
    tronco("<b>Antecedentes perinatales</b> (EG, parto, Apgar, SGB materno, ruptura de membranas), edad en HORAS, "
           "<b>ictericia</b> (cuando aparecio), succion/alimentacion, deposiciones/orina, <b>tamiz neonatal</b>, "
           "peso, infecciones maternas (TORCH/VIH).",
           "<b>Ictericia &lt;24 h</b> &rarr; hemolisis (patologica). <b>Decaido + come mal</b> &rarr; sepsis. "
           "<b>Vomito bilioso</b> &rarr; obstruccion. <b>Conjuntivitis segun dia</b> &rarr; quimica/gonococo/"
           "Chlamydia. <b>Cianosis/soplo</b> &rarr; cardiopatia."),
    T + ["recien_nacido"])

add(deck_t, caso("TRONCO — Nino sano / control (desarrollo, crecimiento, vacunas)"),
    tronco("<b>Hitos del desarrollo</b> por area, <b>curvas</b> (peso/talla/PC), alimentacion (lactancia/ablactacion, "
           "leche de vaca), <b>esquema de vacunacion</b>, sueno, tamizajes (cadera, visual/auditivo), entorno y "
           "seguridad.",
           "<b>Hitos retrasados o perdidos</b> &rarr; estudiar (regresion = urgente). <b>Caida de percentiles</b> "
           "&rarr; investigar. <b>Mucha leche de vaca + palidez</b> &rarr; ferropenia. <b>Vacunas incompletas</b> "
           "&rarr; completar."),
    T + ["nino_sano"])


# ===================== LLAVES CORE (16) =====================
C = ["core"]
add(deck_c, caso("Lactante de 6 semanas con fiebre y sin foco aparente"),
    llave("&iquest;<b>Edad exacta</b>? &iquest;temperatura rectal &ge;38? &iquest;come/orina? &iquest;como se ve "
          "(TEP)? &iquest;vacunas?",
          "Fiebre en &lt;3 meses sin foco; la edad estratifica el riesgo de infeccion bacteriana grave.",
          "Fiebre sin foco del lactante"),
    C + ["fiebre_sin_foco"])

add(deck_c, caso("Lactante de 5 meses con primer episodio de tos, mocos y silbidos en epoca de VRS"),
    llave("&iquest;<b>Primer episodio de sibilancias en &lt;2 anos</b> tras catarro? &iquest;come bien? "
          "&iquest;apneas? &iquest;SatO2?",
          "Primer cuadro de sibilancias + dificultad respiratoria viral en &lt;2 anos.",
          "Bronquiolitis"),
    C + ["bronquiolitis"])

add(deck_c, caso("Nino con tos 'de perro' y un silbido al inspirar, de noche"),
    llave("&iquest;<b>Tos perruna + estridor inspiratorio + disfonia</b>? &iquest;febricula? &iquest;empeora al "
          "agitarse/llorar?",
          "Tos perruna + estridor + disfonia de origen viral; sin aspecto toxico ni babeo.",
          "Crup (laringotraqueitis)"),
    C + ["crup"])

add(deck_c, caso("Nino con fiebre y respiracion rapida"),
    llave("&iquest;<b>Fiebre + taquipnea</b> (por edad) + tiraje? &iquest;hipoxia? &iquest;foco a la auscultacion?",
          "Fiebre + taquipnea (mejor signo) + signos focales/consolidacion.",
          "Neumonia pediatrica"),
    C + ["neumonia"])

add(deck_c, caso("Nino atopico con crisis de disnea y sibilancias recurrentes"),
    llave("&iquest;Episodios <b>recurrentes y reversibles</b> de sibilancias/tos, peor de noche o con gatillos? "
          "&iquest;atopia? &iquest;usa inhalador?",
          "Sibilancias recurrentes reversibles + atopia; responde a broncodilatador.",
          "Asma (crisis)"),
    C + ["asma"])

add(deck_c, caso("Nino con otalgia y fiebre tras un catarro"),
    llave("&iquest;<b>Otalgia + fiebre</b>? &iquest;tira de la oreja (lactante)? &iquest;otorrea? (timpano "
          "abombado)",
          "Timpano abombado, hiperemico, con derrame; dolor que NO aumenta al traccionar el pabellon.",
          "Otitis media aguda"),
    C + ["oma"])

add(deck_c, caso("Nino de 7 anos con odinofagia, fiebre y exudado, sin tos"),
    llave("&iquest;<b>Fiebre + exudado amigdalino + adenopatias + AUSENCIA de tos</b> (McIsaac)? &iquest;edad "
          "&ge;3 a?",
          "McIsaac alto + prueba rapida/cultivo positivos (estreptococo del grupo A).",
          "Faringoamigdalitis estreptococica"),
    C + ["faringitis"])

add(deck_c, caso("Lactante con diarrea y vomito; valoro si esta deshidratado"),
    llave("&iquest;Numero de evacuaciones/vomitos? &iquest;<b>orina (panales), lagrimas, ojos hundidos, pliegue, "
          "estado de alerta</b>? &iquest;tolera liquidos?",
          "Diarrea/vomito agudos + signos que estiman el grado de deshidratacion.",
          "GEA con deshidratacion"),
    C + ["gea"])

add(deck_c, caso("Nino de 2 anos con convulsion durante un cuadro febril"),
    llave("&iquest;<b>Fiebre + crisis generalizada &lt;15 min, una en 24 h, 6 m-5 a</b>? &iquest;recupero bien? "
          "&iquest;cual es el foco de la fiebre?",
          "Crisis breve generalizada en contexto febril, con recuperacion completa; sin datos meningeos.",
          "Convulsion febril simple"),
    C + ["convulsion_febril"])

add(deck_c, caso("Lactante febril, irritable, con fontanela abombada"),
    llave("&iquest;<b>Irritabilidad inconsolable, rechazo del alimento, fontanela abombada, somnolencia</b>? "
          "&iquest;petequias?",
          "Fiebre + signos sutiles (lactante) o meningeos (mayor); fontanela abombada.",
          "Meningitis bacteriana"),
    C + ["meningitis"])

add(deck_c, caso("Recien nacido de 3 dias con ictericia"),
    llave("&iquest;<b>A que HORA/dia aparecio</b> (24 h?)? &iquest;EG, grupo/Rh de la madre, alimentacion, color "
          "de heces? &iquest;como se ve?",
          "Ictericia evaluada por nivel de bilirrubina vs umbral por horas/EG; &lt;24 h sugiere hemolisis.",
          "Ictericia neonatal"),
    C + ["ictericia"])

add(deck_c, caso("Recien nacido decaido que come mal con temperatura inestable"),
    llave("&iquest;<b>Come mal, decaido, temperatura inestable, apneas, ictericia</b>? &iquest;SGB materno, ruptura "
          "de membranas, fiebre materna?",
          "Signos inespecificos en el RN + factores perinatales; sospecha que basta para tratar.",
          "Sepsis neonatal"),
    C + ["sepsis_neonatal"])

add(deck_c, caso("Nino con fiebre alta de 5 dias, ojos rojos y labios agrietados"),
    llave("&iquest;<b>Fiebre &ge;5 dias</b> + conjuntivitis no exudativa + labios/lengua aframbuesada + exantema + "
          "cambios en manos/pies + adenopatia?",
          "Fiebre &ge;5 d + &ge;4 de 5 criterios clinicos; riesgo de aneurisma coronario.",
          "Enfermedad de Kawasaki"),
    C + ["kawasaki"])

add(deck_c, caso("Nino con fiebre, tos, coriza, conjuntivitis y manchas blancas en la boca"),
    llave("&iquest;<b>Fiebre + tos + coriza + conjuntivitis</b> y <b>manchas de Koplik</b> antes del exantema? "
          "&iquest;vacunacion SRP? &iquest;contacto?",
          "Pródromo catarral + Koplik + exantema maculopapular cefalo-caudal.",
          "Sarampion"),
    C + ["sarampion"])

add(deck_c, caso("Nino con faringitis, lengua aframbuesada y piel aspera"),
    llave("&iquest;<b>Faringitis + exantema 'en lija' + lengua aframbuesada</b> + lineas de Pastia? &iquest;palidez "
          "peribucal?",
          "Exantema en lija + lengua aframbuesada en contexto de faringitis estreptococica.",
          "Escarlatina"),
    C + ["escarlatina"])

add(deck_c, caso("Nino sano en consulta de control"),
    llave("&iquest;<b>Hitos del desarrollo por edad</b>? &iquest;curvas (peso/talla/PC)? &iquest;esquema de "
          "vacunacion? &iquest;alimentacion, sueno, seguridad?",
          "Revision sistematica de desarrollo, crecimiento, vacunas y entorno (oportunidad preventiva).",
          "Control del nino sano"),
    C + ["nino_sano"])


# ===================== LLAVES MENOS (16) =====================
M = ["menos_comun"]
pares = [
    ("Nino con fiebre alta, babeo y posicion en tripode, de aspecto toxico",
     "&iquest;<b>Fiebre alta + babeo + dificultad para tragar + en tripode + SIN tos perruna</b>? &iquest;mal "
     "estado? &iquest;vacuna Hib?",
     "Aspecto toxico + babeo + disfagia + tripode (NO explorar la garganta).", "Epiglotitis (Hib)", "epiglotitis"),
    ("Lactante con accesos de tos intensa, 'gallo' y vomito tras toser",
     "&iquest;<b>Accesos de tos + gallo inspiratorio + vomito postusivo</b>? &iquest;apneas (en el bebe)? "
     "&iquest;contacto? &iquest;vacunas?",
     "Tos paroxistica + gallo + vomito postusivo; en &lt;6 meses puede ser apnea sin tos clasica.", "Tos ferina", "tos_ferina"),
    ("Nino con ampollas pruriginosas en distintas etapas",
     "&iquest;<b>Vesiculas en distintos estadios</b> (papula, vesicula, costra) + prurito? &iquest;contacto? "
     "&iquest;vacunado?",
     "Lesiones en distintos estadios a la vez + prurito; inicio en tronco.", "Varicela", "varicela"),
    ("Lactante con fiebre alta 3 dias y exantema que aparece al quitarse la fiebre",
     "&iquest;<b>Fiebre alta 3 dias que CEDE y entonces aparece el exantema</b>? &iquest;buen estado general?",
     "Fiebre alta que cede y aparece exantema al desaparecer la fiebre (lactante).", "Exantema subito (roseola)", "roseola"),
    ("Nino con mejillas muy rojas 'abofeteadas' y exantema en encaje",
     "&iquest;<b>'Cara abofeteada'</b> seguida de exantema reticular en extremidades? &iquest;contacto escolar?",
     "Eritema malar 'en bofetada' + exantema reticular; ya casi no contagia al aparecer.", "Eritema infeccioso (parvovirus B19)", "eritema_infeccioso"),
    ("Nino con ulceras en la boca y vesiculas en manos y pies",
     "&iquest;<b>Vesiculas en manos, pies y ulceras en la boca</b>? &iquest;rechaza tragar? &iquest;guarderia?",
     "Vesiculas en manos/pies + enantema vesiculoso; riesgo de deshidratacion por dolor.", "Mano-pie-boca (coxsackie)", "mano_pie_boca"),
    ("Nino con fiebre leve, exantema y ganglios detras de las orejas",
     "&iquest;Exantema leve + <b>adenopatias retroauriculares/occipitales</b>? &iquest;contacto con embarazadas? "
     "&iquest;vacuna SRP?",
     "Exantema leve + adenopatias retroauriculares; riesgo real = rubeola congenita.", "Rubeola", "rubeola"),
    ("Nino con costras color miel alrededor de la nariz y boca",
     "&iquest;<b>Lesiones con costra melicerica (color miel)</b>? &iquest;se extienden? &iquest;eritema caliente "
     "alrededor (celulitis)?",
     "Costra melicerica superficial (S. aureus/estreptococo); localizado vs extenso.", "Impetigo", "impetigo"),
    ("Recien nacido con secrecion ocular purulenta a los 3 dias",
     "&iquest;<b>A que dia aparecio</b>? &iquest;secrecion purulenta abundante? &iquest;ITS materna? &iquest;recibio "
     "profilaxis ocular?",
     "Conjuntivitis segun el dia: &lt;24 h quimica; 2-5 d gonococo; 5-14 d Chlamydia.", "Conjuntivitis neonatal", "conjuntivitis_neonatal"),
    ("Recien nacido con microcefalia, sordera o calcificaciones cerebrales",
     "&iquest;<b>Infecciones maternas en el embarazo</b>? &iquest;microcefalia, sordera, ictericia, "
     "hepatoesplenomegalia, lesiones oculares?",
     "Estigmas congenitos multiples + serologia/PCR; CMV es la mas frecuente.", "Infeccion congenita (TORCH)", "torch"),
    ("Hijo de madre con VIH",
     "&iquest;<b>Estado de VIH materno y carga viral</b>? &iquest;recibio TAR/profilaxis? &iquest;tipo de parto? "
     "&iquest;lactancia?",
     "RN expuesto; dx por PCR/carga viral (no serologia, por anticuerpos maternos).", "VIH perinatal", "vih_perinatal"),
    ("Nino con prurito anal nocturno o diarrea cronica",
     "&iquest;<b>Prurito anal nocturno</b> (oxiuros) o <b>diarrea cronica/malabsorcion</b> (giardia)? &iquest;agua/"
     "higiene? &iquest;contactos?",
     "Sintomas segun parasito; oxiuros (Graham) vs giardia (diarrea cronica).", "Parasitosis intestinal", "parasitosis"),
    ("Nino con lesiones que no encajan con la historia que cuentan",
     "&iquest;El <b>mecanismo relatado explica la lesion</b> para la edad/desarrollo? &iquest;retraso en consultar? "
     "&iquest;relato que cambia? &iquest;lesiones en distintos estadios?",
     "Incongruencia lesion-relato + banderas (retraso, relato cambiante, lesiones patognomonicas).", "Maltrato infantil", "maltrato"),
    ("Lactante de 4 semanas con vomito en proyectil no bilioso tras comer",
     "&iquest;<b>Vomito en proyectil NO bilioso</b> a las 3-6 semanas? &iquest;queda con hambre? &iquest;baja de "
     "peso? &iquest;'oliva' palpable?",
     "Vomito proyectil no bilioso + alcalosis hipocloremica; oliva pilorica.", "Estenosis pilorica", "pilorica"),
    ("Lactante con episodios de llanto/dolor colico y heces en jalea de grosella",
     "&iquest;<b>Episodios de dolor colico que lo encogen + decaimiento entre crisis</b>? &iquest;heces en 'jalea "
     "de grosella'? &iquest;masa abdominal?",
     "Dolor colico intermitente + decaimiento + jalea de grosella (tardia); masa en salchicha.", "Invaginacion intestinal", "invaginacion"),
    ("Recien nacido con palidez y mala ganancia que toma mucha leche de vaca",
     "&iquest;<b>Cuanta leche de vaca</b> (&gt;500-700 mL/d o antes del ano)? &iquest;palidez, irritabilidad, "
     "desarrollo? &iquest;dieta pobre en hierro?",
     "Anemia microcitica + dieta con exceso de leche de vaca/pobre en hierro.", "Anemia ferropenica del lactante", "ferropenia"),
]
for titulo, p, pat, dx, tag in pares:
    add(deck_m, caso(titulo), llave(p, pat, dx), M + [tag])


def build():
    for d, f in [(deck_t, "Interrogatorio_01_Troncos.apkg"), (deck_c, "Interrogatorio_02_Llaves_core.apkg"),
                 (deck_m, "Interrogatorio_03_Llaves_menos.apkg")]:
        genanki.Package(d).write_to_file(os.path.join(OUTPUT_DIR, f))
        print(f"  -> {f} ({len(d.notes)} notas)")
    genanki.Package([deck_t, deck_c, deck_m]).write_to_file(
        os.path.join(OUTPUT_DIR, "No_Hay_Tiempo_Ped_Interrogatorio_TODOS.apkg"))
    print(f"  -> TODOS ({sum(len(d.notes) for d in [deck_t, deck_c, deck_m])} notas)")


if __name__ == "__main__":
    build()
