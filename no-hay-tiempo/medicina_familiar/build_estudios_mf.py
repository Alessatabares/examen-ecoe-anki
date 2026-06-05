"""No hay tiempo / Medicina Familiar — PILAR EXPLORACION + ESTUDIOS.

A) DISCRIMINADOR: una herramienta separa un grupo por un hallazgo (por herramienta).
B) PANEL/workup: una entidad pide una bateria con rol de cada estudio (por enfermedad).
Enfoque de 1er contacto: que pido en consultorio, que NO pido de rutina, cuando refiero.
Guia: GPC MX, GINA, GOLD, ADA, AHA/ACC, ESC, IDSA, USPSTF, CENETEC.
"""
import os
import genanki

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "output")
os.makedirs(OUTPUT_DIR, exist_ok=True)

MODEL_QA_ID = 1990009903
DECK_ID_D, DECK_ID_P, DECK_ID_M = 1990009021, 1990009022, 1990009023
DECK_NAME_D = "No hay tiempo::Medicina Familiar::Estudios::1 - Discriminadores (herramienta)"
DECK_NAME_P = "No hay tiempo::Medicina Familiar::Estudios::2 - Paneles (por entidad)"
DECK_NAME_M = "No hay tiempo::Medicina Familiar::Estudios::3 - Signos y scores"

CSS_BASE = """
.card { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  font-size: 19px; text-align: left; color: #1a1a1a; background-color: #fafafa;
  padding: 20px; line-height: 1.5; }
.caso { font-size: 21px; font-weight: 700; color: #1e3a8a; }
#extra { margin-top: 16px; border: none; border-top: 1px solid #d4d4d4; padding-top: 12px; }
.bloque { display: block; margin: 12px 0; padding: 10px 14px; border-radius: 8px; }
.lab { display: block; font-size: 13px; font-weight: 700; letter-spacing: .5px;
  text-transform: uppercase; margin-bottom: 4px; }
.paraque { background: #eef2ff; border-left: 4px solid #1e3a8a; }
.trampa { background: #fef2f2; border-left: 4px solid #b91c1c; }
.pido { background: #eef2ff; border-left: 4px solid #1e3a8a; }
.descarto { background: #fff7ed; border-left: 4px solid #b45309; }
.clave { background: #ecfdf5; border-left: 4px solid #047857; }
.paraque .lab { color: #1e3a8a; } .trampa .lab { color: #b91c1c; }
.pido .lab { color: #1e3a8a; } .descarto .lab { color: #b45309; } .clave .lab { color: #047857; }
table.disc { border-collapse: collapse; width: 100%; margin: 6px 0 4px 0; font-size: 17px; }
table.disc td { border-bottom: 1px solid #e5e7eb; padding: 7px 8px; vertical-align: top; }
table.disc td.dx { font-weight: 700; color: #065f46; white-space: nowrap; }
b { color: #111; }
"""
model_qa = genanki.Model(MODEL_QA_ID, "NHT MF Estudios QA",
    fields=[{"name": "Front"}, {"name": "Back"}],
    templates=[{"name": "QA", "qfmt": "{{Front}}", "afmt": '{{Front}}<hr id="extra">{{Back}}'}],
    css=CSS_BASE)

deck_d = genanki.Deck(DECK_ID_D, DECK_NAME_D)
deck_p = genanki.Deck(DECK_ID_P, DECK_NAME_P)
deck_m = genanki.Deck(DECK_ID_M, DECK_NAME_M)
BASE_TAGS = ["medicina_familiar", "ecoe", "no_hay_tiempo", "estudios"]


def add(deck, front, back, tags):
    deck.add_note(genanki.Note(model=model_qa, fields=[front, back], tags=BASE_TAGS + tags))

def caso(t): return f'<span class="caso">{t}</span>'

def disc(pq, filas, tr):
    rows = "".join(f'<tr><td>{h}</td><td class="dx">{d}</td></tr>' for h, d in filas)
    return (f'<span class="bloque paraque"><span class="lab">Para que lo pido</span>{pq}</span>'
            f'<table class="disc">{rows}</table>'
            f'<span class="bloque trampa"><span class="lab">Trampa</span>{tr}</span>')

def panel(pido, des, clave):
    return (f'<span class="bloque pido"><span class="lab">Pido (bateria + para que)</span>{pido}</span>'
            f'<span class="bloque descarto"><span class="lab">Descarto / vigilo</span>{des}</span>'
            f'<span class="bloque clave"><span class="lab">Clave / criterio</span>{clave}</span>')


# ===================== DISCRIMINADORES (8) =====================
D = ["discriminador"]
add(deck_d, caso("Otoscopia"),
    disc("Diferenciar las causas de otalgia/hipoacusia en el consultorio.",
         [("<b>Timpano abombado, hiperemico, opaco</b>", "Otitis media aguda"),
          ("Nivel hidroaereo / burbujas, timpano retraido", "Otitis media con derrame"),
          ("<b>Conducto edematoso, eritematoso, otorrea</b>", "Otitis externa"),
          ("Timpano perforado con otorrea", "OMA perforada / cronica"),
          ("Tapon de cerumen", "Hipoacusia por cerumen")],
         "Dolor que aumenta al traccionar el pabellon = externa; dolor con timpano abombado = media."),
    D + ["otoscopia"])

add(deck_d, caso("Espirometria"),
    disc("Separar el patron obstructivo del restrictivo y confirmar EPOC/asma.",
         [("<b>FEV1/FVC &lt;0.70 NO reversible</b>", "EPOC"),
          ("Obstruccion <b>reversible</b> con broncodilatador (&Delta;FEV1 &ge;12% y 200 mL)", "Asma"),
          ("FEV1/FVC normal con <b>FVC baja</b>", "Patron restrictivo"),
          ("Espirometria normal", "No descarta asma (variabilidad) -> flujometria")],
         "La reversibilidad apunta a asma; la obstruccion fija al EPOC. El dx de EPOC exige espirometria, no solo clinica."),
    D + ["espirometria"])

add(deck_d, caso("ECG en el consultorio"),
    disc("Tamizar isquemia, arritmia y datos electrolitos en dolor toracico/palpitaciones/sincope.",
         [("<b>Elevacion del ST</b>", "IAMCEST -> urgencia"),
          ("Infra-ST / T invertidas", "Isquemia / SCASEST"),
          ("<b>Sin onda P + R-R irregular</b>", "Fibrilacion auricular"),
          ("ST difuso concavo + descenso PR", "Pericarditis"),
          ("QT largo / preexcitacion / bloqueos", "Riesgo de sincope cardiogenico")],
         "ECG normal NO descarta SCA: ante dolor isquemico, traslado a urgencias y troponina seriada."),
    D + ["ecg"])

add(deck_d, caso("Tira reactiva de orina (EGO)"),
    disc("Apoyar el dx de ITU y orientar otras nefropatias en el consultorio.",
         [("<b>Leucocitos (esterasa) + nitritos</b>", "ITU"),
          ("Hematuria + proteinuria + cilindros", "Glomerulopatia -> referir"),
          ("<b>Proteinuria persistente</b>", "Dano renal (DM/HTA) -> cuantificar (RAC)"),
          ("Glucosuria", "Hiperglucemia / diabetes"),
          ("Nitritos negativos pero clinica clara", "No descarta ITU (urocultivo)")],
         "Bacteriuria asintomatica NO se trata (salvo embarazo o procedimiento urologico). Toma urocultivo en complicada."),
    D + ["ego"])

add(deck_d, caso("Glucemia / HbA1c (criterios de diabetes)"),
    disc("Clasificar el estado glucemico y tamizar.",
         [("<b>HbA1c &ge;6.5%</b> o glucosa ayuno &ge;126 o 2 h &ge;200 o azar &ge;200 + sintomas", "Diabetes"),
          ("HbA1c <b>5.7-6.4%</b> o glucosa ayuno 100-125", "Prediabetes"),
          ("HbA1c &lt;5.7% / glucosa &lt;100", "Normal")],
         "Confirma con 2da prueba salvo hiperglucemia inequivoca con sintomas. La HbA1c se altera con anemia/hemoglobinopatias."),
    D + ["glucemia"])

add(deck_d, caso("Perfil tiroideo (TSH primero)"),
    disc("Orientar disfuncion tiroidea con la TSH como tamiz.",
         [("<b>TSH alta + T4L baja</b>", "Hipotiroidismo primario"),
          ("TSH alta + T4L normal", "Hipotiroidismo subclinico"),
          ("<b>TSH baja + T4L/T3 altas</b>", "Hipertiroidismo"),
          ("TSH baja + T4L normal", "Hipertiroidismo subclinico")],
         "La TSH es el mejor tamiz, pero NO en enfermedad aguda grave (sx del eutiroideo enfermo): difiere el estudio."),
    D + ["perfil_tiroideo"])

add(deck_d, caso("Indices de la anemia (VCM, ferritina, reticulocitos)"),
    disc("Clasificar la anemia para dirigir el estudio en 1er contacto.",
         [("<b>VCM bajo + ferritina baja</b>", "Ferropenica"),
          ("VCM bajo/normal + ferritina normal/alta", "Enfermedad cronica"),
          ("<b>VCM alto + hipersegmentados</b>", "Megaloblastica (B12/folato)"),
          ("Reticulocitos altos", "Hemolisis / sangrado"),
          ("Reticulocitos bajos", "Falla de produccion")],
         "Ferropenica en varon/posmenopausica = descartar sangrado digestivo. Ferritina normal/alta no excluye ferropenia (inflamacion)."),
    D + ["indices_anemia"])

add(deck_d, caso("Exploracion neurologica del vertigo (Dix-Hallpike / HINTS)"),
    disc("Separar el vertigo periferico (benigno) del central (peligroso).",
         [("<b>Dix-Hallpike +</b> (nistagmo breve, fatigable)", "VPPB (periferico) -> Epley"),
          ("Nistagmo <b>que no fatiga</b>, vertical/cambiante", "Central -> referir"),
          ("<b>HINTS central</b> (impulso cefalico normal, skew, nistagmo direccional)", "Central (EVC fosa post.)"),
          ("Hipoacusia + acufeno + vertigo prolongado", "Periferico (Meniere/neuronitis)")],
         "Paradoja: <b>impulso cefalico NORMAL</b> en un vertigo agudo sugiere causa CENTRAL (no tranquiliza)."),
    D + ["vertigo_hints"])


# ===================== PANELES (10) =====================
P = ["panel"]
add(deck_p, caso("Panel del control del paciente cronico (DM/HTA)"),
    panel("<b>Glucosa/HbA1c</b>, <b>lipidos</b>, <b>funcion renal + albuminuria (RAC)</b>, electrolitos, TA, IMC, "
          "ECG; fondo de ojo y exploracion de pies (DM). Calculo riesgo CV.",
          "Dano de organo blanco (retina, rinon, corazon, pie), complicaciones, comorbilidad.",
          "El control integra cifras + dano de organo + adherencia + prevencion (vacunas/tamizaje), no solo la glucosa/TA."),
    P + ["cronico"])

add(deck_p, caso("Panel de la infeccion urinaria"),
    panel("<b>Tira reactiva/EGO</b> (esterasa, nitritos) + <b>urocultivo</b> si complicada/recurrente/embarazo; "
          "funcion renal si grave. Imagen (USG) si no mejora, sospecha de obstruccion o varon.",
          "Pielonefritis (fiebre + lumbar), complicacion (DM, embarazo, sonda, litiasis), obstruccion.",
          "No complicada en mujer: tratar empirico sin urocultivo. Embarazo: tamizar y tratar bacteriuria asintomatica."),
    P + ["itu"])

add(deck_p, caso("Panel del dolor toracico (1er contacto)"),
    panel("<b>ECG inmediato</b> + signos vitales + SatO2; troponina si disponible/traslado. Rx torax. "
          "Calcular probabilidad y trasladar si datos isquemicos.",
          "Lo que mata: SCA, TEP, diseccion, neumotorax, taponamiento. Causas benignas son exclusion.",
          "ECG normal NO descarta SCA. En 1er contacto: AAS + traslado urgente ante dolor isquemico."),
    P + ["dolor_toracico"])

add(deck_p, caso("Panel respiratorio (tos/disnea)"),
    panel("Exploracion + SatO2; <b>Rx de torax</b> si sospecha de neumonia/derrame/neumotorax; "
          "<b>espirometria</b> (programada, no en agudo) para asma/EPOC; flujometria en asma.",
          "Neumonia (consolidacion), derrame, neumotorax; obstruccion cronica (EPOC) vs reversible (asma).",
          "No pidas Rx a todo catarro/bronquitis. La espirometria confirma EPOC/asma pero NO en la exacerbacion aguda."),
    P + ["respiratorio"])

add(deck_p, caso("Panel del sindrome anemico"),
    panel("<b>BH con indices (VCM)</b> + <b>ferritina/hierro/saturacion</b>, reticulocitos; segun patron: B12/folato, "
          "funcion renal/tiroidea, sangre oculta en heces. Frotis si dudas.",
          "Causa: ferropenia (sangrado/dieta), enfermedad cronica, megaloblastica, hemolisis, ERC.",
          "Ferropenica en varon o posmenopausica obliga a estudio del tubo digestivo (endoscopia/colonoscopia)."),
    P + ["anemia"])

add(deck_p, caso("Panel de la prostata (LUTS en varon mayor)"),
    panel("<b>Tacto rectal + PSA</b> + EGO/urocultivo (descartar ITU) + funcion renal si retencion; "
          "<b>IPSS</b> (sintomas). USG si retencion/hematuria/litiasis.",
          "HPB (prostata lisa) vs cancer (nodulo duro); retencion, infeccion, dano renal por obstruccion.",
          "Tamizaje de cancer de prostata es <b>decision compartida</b> (PSA + tacto), no universal."),
    P + ["prostata"])

add(deck_p, caso("Panel preventivo / chequeo del adulto sano"),
    panel("<b>TA</b>, <b>glucosa/HbA1c</b>, <b>lipidos</b>; tamizaje de cancer por edad/sexo (<b>cervico, mama, "
          "colon</b>, prostata individualizado); <b>VIH</b> al menos una vez; revision de <b>vacunas</b>; IMC, "
          "agudeza visual, salud mental, consejo de tabaco/alcohol.",
          "Enfermedad asintomatica (HTA, DM, dislipidemia, cancer, VIH); factores de riesgo modificables.",
          "Tamizaje por edad/riesgo (USPSTF/GPC), no 'a todos todo'. Aprovecha la visita para vacunas y consejo breve."),
    P + ["preventivo"])

add(deck_p, caso("Panel de la cefalea (cuando SI estudiar)"),
    panel("Cefalea primaria: <b>dx clinico, SIN imagen</b>. <b>Neuroimagen (TC/RM)</b> y/o PL solo con banderas: "
          "trueno, focalidad, fiebre + rigidez, &gt;50 de novo, inmunodeprimido, papiledema, cambio de patron.",
          "Secundaria peligrosa: HSA, meningitis, masa, arteritis de celulas gigantes (VSG/PCR).",
          "La mayoria de las cefaleas NO necesita imagen. Pedirla sin banderas es sobrestudio; con banderas es urgente."),
    P + ["cefalea"])

add(deck_p, caso("Panel digestivo alto (dispepsia / ERGE)"),
    panel("Sin banderas y &lt;60 a: <b>NO endoscopia de entrada</b> &rarr; <b>prueba de H. pylori no invasiva</b> "
          "(antigeno en heces / prueba de aliento) y/o prueba con IBP. Suspender AINE.",
          "Banderas que obligan a <b>endoscopia</b>: disfagia, perdida de peso, sangrado/anemia, vomito "
          "persistente, masa, &gt;60 a de novo (descartar Ca eso-gastrico/ulcera).",
          "Para la prueba de H. pylori (aliento/antigeno) suspende IBP ~2 sem y antibiotico ~4 sem (falsos negativos). "
          "Confirma erradicacion."),
    P + ["digestivo_alto"])

add(deck_p, caso("Panel de diarrea cronica / malabsorcion"),
    panel("<b>BH, ferritina, PCR/VSG, TSH, serologia celiaca (anti-transglutaminasa IgA + IgA total)</b>, "
          "electrolitos, coprologico/coprocultivo segun caso, <b>calprotectina fecal</b>; colonoscopia si banderas.",
          "Funcional (SII) vs organico (EII, celiaca, malabsorcion, tiroides); banderas (sangre, ↓peso, anemia).",
          "<b>Calprotectina fecal</b> separa funcional de inflamatorio (EII). Pide la serologia celiaca CON gluten en "
          "la dieta."),
    P + ["diarrea_cronica"])


# ===================== SIGNOS Y SCORES (21) =====================
M = ["signo_score"]
simple = [
    ("Centor / McIsaac", "Probabilidad de <b>faringitis estreptococica</b> (fiebre, exudado, adenopatias, AUSENCIA de tos, edad) -> decide antibiotico.", "faringitis"),
    ("CURB-65", "Gravedad de la <b>neumonia</b> (Confusion, Urea, FR&ge;30, TA baja, &ge;65) -> sitio de manejo.", "nac"),
    ("Criterios de Anthonisen", "Definen <b>exacerbacion de EPOC</b> (aumento de disnea + esputo + purulencia) -> antibiotico.", "epoc"),
    ("Reversibilidad espirometrica", "&Delta;FEV1 &ge;12% y 200 mL post-broncodilatador = <b>asma</b>; obstruccion fija = EPOC.", "asma"),
    ("Score de Wells (TVP/TEP)", "Probabilidad pretest de <b>TVP/TEP</b> -> guia dimero D vs Doppler/angio-TAC.", "tvp"),
    ("CHA2DS2-VASc", "Riesgo embolico en <b>FA</b> -> decide anticoagulacion.", "icc"),
    ("Banderas de alarma digestivas", "Disfagia, perdida de peso, sangrado/anemia, vomito persistente, masa, &gt;55-60 a de novo -> <b>endoscopia + referir</b> (descartar Ca eso-gastrico).", "disfagia_alarma"),
    ("Test-and-treat de H. pylori", "Sin banderas y &lt;60 a: <b>prueba no invasiva</b> (antigeno en heces/aliento); si + erradico (triple/cuadruple) -> <b>dispepsia/ulcera</b>.", "dispepsia"),
    ("Criterios de Roma IV", "Dx <b>positivo</b> del SII: dolor abdominal recurrente relacionado con la defecacion + cambio en frecuencia/forma, sin banderas.", "sii"),
    ("Anti-transglutaminasa (tTG-IgA) + IgA total", "Tamiz serologico de <b>enfermedad celiaca</b> (pedir CON gluten); confirmar con biopsia duodenal.", "celiaca"),
    ("Calprotectina fecal", "Marcador de inflamacion intestinal: separa <b>SII (funcional)</b> de <b>EII (organico)</b>.", "eii"),
    ("Signo de Lasegue", "Dolor radicular al elevar la pierna recta = <b>ciatica/radiculopatia</b> lumbar.", "ciatica"),
    ("SNNOOP (banderas de cefalea)", "Sintomas sistemicos, Neoplasia/inmunodep., Neurologico, Onset en trueno, Older &gt;50, cambio de Patron -> <b>estudiar</b>.", "cefalea_red_flag"),
    ("Dix-Hallpike / Epley", "Maniobra que reproduce el <b>VPPB</b> (Dix-Hallpike) y lo trata (Epley).", "vppb"),
    ("HINTS", "Bateria oculomotora que distingue vertigo <b>central</b> (peligroso) del periferico.", "vertigo_central"),
    ("FAST / hora de inicio", "Cara-Brazo-Habla-Tiempo: tamiz de <b>EVC</b>; la hora de inicio define la ventana.", "evc"),
    ("Triada de la estenosis aortica", "Angina + sincope + disnea de esfuerzo + soplo eyectivo = <b>estenosis aortica</b> severa.", "estenosis_aortica"),
    ("Triada de Cushing (sospecha clinica)", "Obesidad central + estrias violaceas + cara de luna/giba + HTA/DM -> cribar <b>Cushing</b>.", "cushing"),
    ("Clasificacion de Wagner", "Gradua la <b>ulcera del pie diabetico</b> (0 a 5) y guia el manejo/derivacion.", "pie_diabetico"),
    ("IPSS", "Puntua la gravedad de los <b>sintomas prostaticos (LUTS)</b> en HPB.", "hpb"),
    ("qSOFA", "Tamiz de gravedad en infeccion (TAS&le;100, FR&ge;22, alterado) -> riesgo de <b>sepsis</b>.", "sepsis"),
]
for titulo, texto, tag in simple:
    add(deck_m, caso(titulo),
        f'<span class="bloque paraque"><span class="lab">Que es / como se lee</span>{texto}</span>',
        M + [tag])


def build():
    for d, f in [(deck_d, "Estudios_01_Discriminadores.apkg"), (deck_p, "Estudios_02_Paneles.apkg"),
                 (deck_m, "Estudios_03_Signos_scores.apkg")]:
        genanki.Package(d).write_to_file(os.path.join(OUTPUT_DIR, f))
        print(f"  -> {f} ({len(d.notes)} notas)")
    genanki.Package([deck_d, deck_p, deck_m]).write_to_file(
        os.path.join(OUTPUT_DIR, "No_Hay_Tiempo_MF_Estudios_TODOS.apkg"))
    print(f"  -> TODOS ({sum(len(d.notes) for d in [deck_d, deck_p, deck_m])} notas)")


if __name__ == "__main__":
    build()
