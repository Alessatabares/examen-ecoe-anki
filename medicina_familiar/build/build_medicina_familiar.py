"""Generador de 5 subdecks Anki para ECOE de Medicina Familiar.

Capas 1-4: Cloze (Imagen Viva, Exploracion Dirigida, Estudios, Diferenciales).
Capa 5: Q&A clasico (Tratamiento Practico ECOE).
Guias base: USPSTF, ADA 2025, ACC/AHA 2017+2018+2023, ATS/IDSA 2019, GOLD 2024, GINA 2024, AAFP.
"""
import os
import genanki

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "output")
os.makedirs(OUTPUT_DIR, exist_ok=True)

MODEL_CLOZE_ID = 1607392319
MODEL_QA_ID = 1607392320

DECK_ID_C1 = 1366039575
DECK_ID_C2 = 1990608935
DECK_ID_C3 = 1185531197
DECK_ID_C4 = 1507672676
DECK_ID_C5 = 1095533052

DECK_NAME_C1 = "Medicina Familiar Adulto::Capa 1 - Imagen Viva"
DECK_NAME_C2 = "Medicina Familiar Adulto::Capa 2 - Exploracion Dirigida"
DECK_NAME_C3 = "Medicina Familiar Adulto::Capa 3 - Estudios e Interpretacion"
DECK_NAME_C4 = "Medicina Familiar Adulto::Capa 4 - Diferenciales Rapidos"
DECK_NAME_C5 = "Medicina Familiar Adulto::Capa 5 - Tratamiento Practico"

CSS_BASE = """
.card {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  font-size: 19px; text-align: left; color: #1a1a1a;
  background-color: #fafafa; padding: 20px; line-height: 1.55;
}
.cloze { font-weight: 600; color: #2563eb; }
#extra { margin-top: 16px; border: none; border-top: 1px solid #d4d4d4; padding-top: 12px; }
.ecoe { color: #b45309; font-style: italic; margin-top: 10px; display: block; }
.contraste { color: #6d28d9; display: block; margin-top: 6px; }
.viva { color: #047857; display: block; margin-top: 6px; font-style: italic; }
.redflag { color: #b91c1c; font-weight: 600; display: block; margin-top: 6px; }
b { color: #111; }
"""

model_cloze = genanki.Model(
    MODEL_CLOZE_ID, "Estudio Medico Cloze",
    fields=[{"name": "Text"}, {"name": "Extra"}],
    templates=[{"name": "Cloze", "qfmt": "{{cloze:Text}}",
                "afmt": '{{cloze:Text}}<hr id="extra">{{Extra}}'}],
    css=CSS_BASE, model_type=genanki.Model.CLOZE,
)
model_qa = genanki.Model(
    MODEL_QA_ID, "Estudio Medico QA",
    fields=[{"name": "Front"}, {"name": "Back"}],
    templates=[{"name": "QA", "qfmt": "{{Front}}",
                "afmt": '{{Front}}<hr id="extra">{{Back}}'}],
    css=CSS_BASE,
)

deck_c1 = genanki.Deck(DECK_ID_C1, DECK_NAME_C1)
deck_c2 = genanki.Deck(DECK_ID_C2, DECK_NAME_C2)
deck_c3 = genanki.Deck(DECK_ID_C3, DECK_NAME_C3)
deck_c4 = genanki.Deck(DECK_ID_C4, DECK_NAME_C4)
deck_c5 = genanki.Deck(DECK_ID_C5, DECK_NAME_C5)

BASE_TAGS = ["medicina_familiar", "ecoe"]


def add_cloze(deck, text, extra, tags):
    deck.add_note(genanki.Note(model=model_cloze, fields=[text, extra], tags=BASE_TAGS + tags))


def add_qa(deck, front, back, tags):
    deck.add_note(genanki.Note(model=model_qa, fields=[front, back], tags=BASE_TAGS + tags))


# ============================================================
# CAPA 1 - IMAGEN VIVA (25 cloze)
# ============================================================
C1 = ["capa1", "imagen_viva"]

# Respiratorio + ORL (10)
add_cloze(deck_c1,
    "Neumonia: {{c1::alveolos llenos de exudado purulento}} -> {{c2::intercambio gaseoso fallando}}; clinica = fiebre + tos productiva + crepitantes localizados",
    '<span class="viva">Imagen: pulmon con zona "blanca" (consolidada) en la Rx.</span>',
    C1 + ["respiratorio", "neumonia"])

add_cloze(deck_c1,
    "Bronquitis aguda: {{c1::bronquios inflamados con moco}} -> tos + esputo; {{c2::los alveolos NO estan comprometidos}} (intercambio gaseoso preservado)",
    '<span class="viva">Imagen: tubos hinchados, alveolos limpios.</span>'
    '<span class="contraste">Por eso la auscultacion es limpia, sin crepitantes focales.</span>',
    C1 + ["respiratorio", "bronquitis"])

add_cloze(deck_c1,
    "Asma exacerbacion: {{c1::broncoespasmo}} + {{c2::edema bronquial}} + {{c3::moco espeso}} -> obstruccion al flujo aereo {{c4::REVERSIBLE}}",
    '<span class="viva">Imagen: bronquios estrechados, atrapamiento aereo.</span>'
    '<span class="contraste">Reversibilidad post-broncodilatador es la clave que la diferencia de EPOC.</span>',
    C1 + ["respiratorio", "asma"])

add_cloze(deck_c1,
    "EPOC: {{c1::destruccion alveolar (enfisema)}} + {{c2::inflamacion cronica de via aerea (bronquitis cronica)}} -> obstruccion {{c3::NO reversible}}",
    '<span class="viva">Imagen: alveolos dilatados como bolsas rotas, atrapamiento aereo.</span>'
    '<span class="contraste">Tabaquismo &gt;10 paquetes-ano es el factor #1.</span>',
    C1 + ["respiratorio", "epoc"])

add_cloze(deck_c1,
    "IVAS viral (resfriado): {{c1::virus invade mucosa nasal/faringe}} -> inflamacion local + moco {{c2::claro abundante}}, sin compromiso sistemico severo",
    '<span class="viva">Imagen: mucosa rosada hinchada con secrecion clara.</span>',
    C1 + ["respiratorio", "ivas"])

add_cloze(deck_c1,
    "Sinusitis: {{c1::ostium del seno paranasal obstruido}} -> {{c2::secrecion atrapada}} + presion + sobreinfeccion -> dolor facial + rinorrea purulenta",
    '<span class="viva">Imagen: cavidad cerrada con liquido a presion.</span>'
    '<span class="redflag">Bacteriana si: sintomas &gt;10 dias o doble empeoramiento.</span>',
    C1 + ["orl", "sinusitis"])

add_cloze(deck_c1,
    "Otitis media aguda: {{c1::disfuncion de trompa de Eustaquio}} -> presion negativa + liquido en oido medio -> {{c2::tropezamiento de germenes}} de nasofaringe",
    '<span class="viva">Imagen: aspiradora cerrada que acumula moco infectado.</span>',
    C1 + ["orl", "otitis_media"])

add_cloze(deck_c1,
    "Otitis externa: {{c1::piel del conducto auditivo externo inflamada}} (humedad + maceracion) -> sobreinfeccion bacteriana (Pseudomonas, S. aureus)",
    '<span class="viva">Imagen: piel del oido rojo, dolor al jalar pabellon (signo del trago).</span>'
    '<span class="contraste">Otitis externa: dolor al MANIPULAR; otitis media: dolor INTERNO.</span>',
    C1 + ["orl", "otitis_externa"])

add_cloze(deck_c1,
    "Faringitis estreptococica: {{c1::Streptococcus pyogenes (grupo A)}} invade amigdalas -> exudado purulento + fiebre + adenopatia cervical + {{c2::ausencia de tos/rinorrea}}",
    '<span class="viva">Imagen: amigdalas rojas con manchas blancas, ganglios duelen.</span>'
    '<span class="redflag">Tratar para prevenir fiebre reumatica.</span>',
    C1 + ["orl", "faringitis"])

add_cloze(deck_c1,
    "Influenza: {{c1::virus invade epitelio respiratorio}} + {{c2::respuesta inmune sistemica intensa}} -> fiebre alta + mialgias + cefalea + postracion (mas alla del resfriado)",
    '<span class="viva">Imagen: el paciente se siente "atropellado", no solo congestionado.</span>'
    '<span class="contraste">IVAS comun: nariz tapada, te sigues funcionando; influenza: te tumba.</span>',
    C1 + ["respiratorio", "influenza"])

# Urinario + Abdominal + Dolor (8)
add_cloze(deck_c1,
    "Cistitis (ITU baja): {{c1::bacteria asciende uretra}} -> coloniza vejiga -> inflamacion de mucosa vesical -> {{c2::disuria + frecuencia + urgencia}}",
    '<span class="viva">Imagen: vejiga roja por dentro, sin fiebre porque no llega al rinon.</span>'
    '<span class="contraste">Si fiebre o lumbalgia -&gt; pielonefritis (ITU alta).</span>',
    C1 + ["urinario", "cistitis"])

add_cloze(deck_c1,
    "Pielonefritis: {{c1::infeccion asciende por ureter hasta rinon}} -> inflamacion del parenquima renal -> fiebre + dolor lumbar + sintomas sistemicos",
    '<span class="viva">Imagen: rinon hinchado e infectado. Bacteriemia posible.</span>'
    '<span class="redflag">Embarazada con bacteriuria SI tratar (riesgo de pielonefritis y parto pretermino).</span>',
    C1 + ["urinario", "pielonefritis"])

add_cloze(deck_c1,
    "Colico renal: {{c1::calculo obstruye el ureter}} -> distension del sistema colector -> contracciones de musculo liso ureteral -> dolor {{c2::colico irradiado de flanco a ingle}}",
    '<span class="viva">Imagen: paciente que NO encuentra postura, se retuerce. Diferente al abdomen quirurgico (paciente quieto).</span>',
    C1 + ["urinario", "colico_renal"])

add_cloze(deck_c1,
    "Gastroenteritis aguda: {{c1::inflamacion intestinal viral o bacteriana}} -> hipersecrecion + hiperperistalsis -> diarrea + vomito + dolor abdominal colico",
    '<span class="viva">Imagen: intestino "lavandose", vaciandose con prisa.</span>'
    '<span class="redflag">Red flags: sangre en heces, fiebre alta, deshidratacion severa, inmunocompromiso.</span>',
    C1 + ["abdominal", "gastroenteritis"])

add_cloze(deck_c1,
    "Apendicitis: {{c1::obstruccion de la luz apendicular (fecalito, hiperplasia linfoide)}} -> distension + isquemia -> dolor {{c2::periumbilical que migra a FID}} en 12-24 h",
    '<span class="viva">Imagen: apendice hinchado a punto de reventar (peritonitis si rompe).</span>'
    '<span class="redflag">Si fiebre + signos peritoneales -&gt; quirurgico urgente.</span>',
    C1 + ["abdominal", "apendicitis"])

add_cloze(deck_c1,
    "Cefalea tensional: {{c1::contraccion sostenida de musculos pericraneales}} (cuello, frontal, occipital) -> dolor {{c2::opresivo bilateral en banda}}, sin nauseas ni fotofobia",
    '<span class="viva">Imagen: casco apretando la cabeza. Suele ser por estres o postura.</span>',
    C1 + ["dolor", "cefalea_tensional"])

add_cloze(deck_c1,
    "Migrana: {{c1::activacion trigemino-vascular}} + neuroinflamacion -> dolor {{c2::pulsatil hemicraneal}} + nauseas + fotofobia + fonofobia; puede tener aura visual",
    '<span class="viva">Imagen: vasos dilatados pulsando dolor; el paciente busca cuarto oscuro.</span>'
    '<span class="redflag">Cefalea peor de mi vida / en trueno / con fiebre / con foco -&gt; secundaria, urgencia.</span>',
    C1 + ["dolor", "migrana"])

add_cloze(deck_c1,
    "Lumbalgia mecanica: {{c1::tension o esguince de musculos/ligamentos paravertebrales}} -> dolor lumbar {{c2::que empeora con movimiento, mejora con reposo}}, sin sintomas radiculares",
    '<span class="viva">Imagen: musculos espasmados, no hay compromiso neural.</span>'
    '<span class="redflag">Red flags: trauma, fiebre, perdida de peso, deficit motor, anestesia silla de montar, retencion urinaria, &lt;20 o &gt;50 anos.</span>',
    C1 + ["dolor", "lumbalgia"])

# Cronicos + Preventivo (7)
add_cloze(deck_c1,
    "HTA: presion arterial elevada cronica -> {{c1::dano endotelial y remodelacion vascular}} -> dano de organo blanco ({{c2::corazon, rinon, retina, cerebro}})",
    '<span class="viva">Imagen: tuberias rigidas y dilatadas, bomba (corazon) trabajando contra resistencia.</span>'
    '<span class="redflag">Crisis HTA + dano organo agudo = emergencia hipertensiva.</span>',
    C1 + ["cronico", "hta"])

add_cloze(deck_c1,
    "DM2: {{c1::resistencia a la insulina (musculo/higado/tejido adiposo)}} + {{c2::declive progresivo de celulas beta}} -> hiperglucemia cronica -> microvasculares (retino, nefro, neuropatia) y macrovasculares (IAM, EVC, EAP)",
    '<span class="viva">Imagen: glucosa en sangre cocinando los vasos (glicacion de proteinas).</span>',
    C1 + ["cronico", "dm2"])

add_cloze(deck_c1,
    "Dislipidemia: {{c1::LDL elevada}} entra a la pared arterial -> oxidacion -> macrofagos forman {{c2::placa ateromatosa}} -> riesgo de ruptura y trombosis (IAM, EVC)",
    '<span class="viva">Imagen: paredes de arteria con depositos amarillos (placas), pueden romperse y obstruir.</span>',
    C1 + ["cronico", "dislipidemia"])

add_cloze(deck_c1,
    "Anemia ferropenica: {{c1::hierro insuficiente}} (perdida cronica, dieta, malabsorcion) -> eritropoyesis defectuosa -> eritrocitos {{c2::microciticos hipocromicos}}",
    '<span class="viva">Imagen: globulos pequenos y palidos en frotis. Fatiga, palidez, palidez de mucosas.</span>'
    '<span class="redflag">Adulto con ferropenia y sin causa clara = colonoscopia (descartar Ca colon).</span>',
    C1 + ["cronico", "anemia"])

add_cloze(deck_c1,
    "Hipotiroidismo: {{c1::deficit de hormona tiroidea}} (Hashimoto es la causa #1) -> {{c2::metabolismo enlentecido}}: fatiga, intolerancia al frio, ganancia de peso, bradicardia, piel seca, depresion",
    '<span class="viva">Imagen: el cuerpo en camara lenta.</span>',
    C1 + ["cronico", "hipotiroidismo"])

add_cloze(deck_c1,
    "Hipertiroidismo: {{c1::exceso de hormona tiroidea}} (Graves es la causa #1) -> {{c2::metabolismo acelerado}}: taquicardia, perdida de peso, calor, sudoracion, ansiedad, temblor",
    '<span class="viva">Imagen: cuerpo en sobremarcha. Exoftalmos en Graves.</span>'
    '<span class="redflag">Tormenta tiroidea: fiebre + taquicardia extrema + delirio = urgencia.</span>',
    C1 + ["cronico", "hipertiroidismo"])

add_cloze(deck_c1,
    "EPOC con hipoxia cronica: {{c1::vasoconstriccion pulmonar hipoxica}} -> hipertension pulmonar -> {{c2::falla del ventriculo derecho (cor pulmonale)}} con edema, ingurgitacion yugular, hepatomegalia",
    '<span class="viva">Imagen: VD trabajando contra pulmones obstruidos hasta claudicar.</span>',
    C1 + ["cronico", "epoc"])


# ============================================================
# CAPA 2 - EXPLORACION DIRIGIDA (30 cloze)
# ============================================================
C2 = ["capa2", "exploracion"]

# Respiratorio + ORL (12)
add_cloze(deck_c2,
    "Neumonia - exploracion dirigida: {{c1::FR elevada}}, {{c2::SatO2}}, {{c3::percusion mate localizada}}, {{c4::estertores crepitantes}}, {{c5::egofonia (E suena A)}}, {{c6::broncofonia (voz transmitida amplificada)}}",
    '<span class="ecoe">ECOE: "Ausculto en bases buscando crepitantes localizados, percuto buscando matidez."</span>',
    C2 + ["respiratorio", "neumonia"])

add_cloze(deck_c2,
    "Asma exacerbacion - signos de severidad: {{c1::uso de musculos accesorios}}, {{c2::sibilancias espiratorias o silencio auscultatorio (mas grave)}}, {{c3::SatO2 &lt;92%}}, {{c4::habla en palabras (no frases)}}, {{c5::FC &gt;120}}",
    '<span class="ecoe">ECOE: "Valoro severidad por uso accesorios, habla y SatO2."</span>'
    '<span class="redflag">Silencio auscultatorio = obstruccion muy severa.</span>',
    C2 + ["respiratorio", "asma"])

add_cloze(deck_c2,
    "EPOC - exploracion: {{c1::espiracion prolongada}}, {{c2::sibilancias}}, {{c3::torax en tonel}} (diametro AP aumentado), {{c4::hipocratismo digital}}, {{c5::cianosis central}}",
    '<span class="ecoe">ECOE: "Tiempo espiratorio alargado, sibilancias bilaterales."</span>',
    C2 + ["respiratorio", "epoc"])

add_cloze(deck_c2,
    "Bronquitis aguda - exploracion: tipicamente {{c1::sin signos focales}}; puede haber {{c2::sibilancias difusas o roncus dispersos}} pero NO crepitantes localizados",
    '<span class="contraste">Auscultacion limpia + tos = bronquitis. Crepitantes focales = neumonia.</span>',
    C2 + ["respiratorio", "bronquitis"])

add_cloze(deck_c2,
    "Sinusitis - exploracion: {{c1::dolor a la palpacion de senos paranasales}}, {{c2::dolor que empeora al inclinarse hacia delante}}, {{c3::rinorrea purulenta}}, {{c4::transiluminacion disminuida}}",
    '<span class="ecoe">ECOE: "Palpo senos frontales y maxilares, busco dolor."</span>',
    C2 + ["orl", "sinusitis"])

add_cloze(deck_c2,
    "Otitis media aguda - otoscopia: timpano {{c1::abombado}}, {{c2::opaco}}, {{c3::hiperemico}}, sin {{c4::movilidad neumatica}}; reflejo luminoso desplazado o ausente",
    '<span class="ecoe">ECOE: "Otoscopia con timpano abombado opaco, sin movilidad neumatica."</span>',
    C2 + ["orl", "otitis_media"])

add_cloze(deck_c2,
    "Otitis externa - exploracion: {{c1::dolor al traccionar pabellon}} (signo del trago) + {{c2::dolor al presionar el trago}} + eritema del CAE + secrecion",
    '<span class="contraste">Otitis media: dolor "interno"; externa: dolor a la MANIPULACION.</span>'
    '<span class="ecoe">ECOE: "Compruebo signo del trago positivo."</span>',
    C2 + ["orl", "otitis_externa"])

add_cloze(deck_c2,
    "Criterios de Centor modificados (faringitis estreptococica): {{c1::fiebre &gt;38}}, {{c2::adenopatia cervical anterior dolorosa}}, {{c3::exudado amigdalino}}, {{c4::ausencia de tos}}; +1 si {{c5::3-14 anos}}, -1 si &gt;45 anos",
    '<span class="ecoe">ECOE: "Cumple X de 5 criterios, indica prueba rapida/tratamiento."</span>'
    '<span class="contraste">3-4 puntos -&gt; alto riesgo; trato o pruebo. 0-1 -&gt; viral, no antibiotico.</span>',
    C2 + ["orl", "faringitis"])

add_cloze(deck_c2,
    "IVAS viral - hallazgos: {{c1::faringe hiperemica SIN exudado}}, {{c2::sin adenopatias dolorosas significativas}}, eritema conjuntival, rinorrea clara",
    '<span class="contraste">SIN exudado, CON tos/rinorrea = viral.</span>',
    C2 + ["respiratorio", "ivas"])

add_cloze(deck_c2,
    "Exploracion respiratoria completa: {{c1::inspeccion}} (uso accesorios, retracciones, cianosis) -> {{c2::palpacion}} (fremitus, expansibilidad) -> {{c3::percusion}} (mate, claro, timpanico) -> {{c4::auscultacion}} (todos los campos)",
    '<span class="ecoe">ECOE: orden estricto IPPA para no perder hallazgos.</span>',
    C2 + ["respiratorio"])

add_cloze(deck_c2,
    "Faringe - exploracion: usar {{c1::abatelenguas}} con buena iluminacion; evaluar {{c2::exudado}}, {{c3::eritema}}, {{c4::petequias en paladar}}, {{c5::desviacion de uvula (absceso periamigdalino)}}",
    '<span class="ecoe">ECOE: "Faringe sin exudado, sin desviacion de uvula."</span>',
    C2 + ["orl"])

add_cloze(deck_c2,
    "Otoscopia normal: timpano {{c1::gris perlado, semitransparente}}, {{c2::reflejo luminoso visible}} en cuadrante antero-inferior, {{c3::movil con maniobra neumatica}}",
    '<span class="ecoe">ECOE: "Timpano de caracteristicas normales bilateralmente."</span>',
    C2 + ["orl"])

# Urinario + Abdominal + Dolor (10)
add_cloze(deck_c2,
    "Abdomen agudo - exploracion sistematica: {{c1::inspeccion}} (distension, cicatrices, peristaltismo visible) -> {{c2::auscultacion}} (RHA disminuidos -&gt; ileo; aumentados -&gt; obstruccion) -> {{c3::percusion}} (timpanismo, matidez) -> {{c4::palpacion superficial}} -> {{c5::palpacion profunda}} -> {{c6::signos peritoneales}}",
    '<span class="ecoe">ECOE: "Exploracion sistematica de los 9 cuadrantes."</span>',
    C2 + ["abdomen"])

add_cloze(deck_c2,
    "Apendicitis - signos clasicos: {{c1::McBurney (dolor en union 1/3 externo con 2/3 internos de linea espina iliaca a ombligo)}}, {{c2::Blumberg (rebote)}}, {{c3::Rovsing (dolor en FID al palpar FII)}}, {{c4::Psoas}}, {{c5::Obturador}}",
    '<span class="ecoe">ECOE: "Compruebo McBurney, Blumberg, Rovsing positivos."</span>',
    C2 + ["abdomen", "apendicitis"])

add_cloze(deck_c2,
    "Pielonefritis - exploracion: {{c1::punopercusion renal positiva (Giordano)}}, {{c2::dolor a la palpacion costovertebral}}, fiebre, taquicardia",
    '<span class="ecoe">ECOE: "Giordano positivo del lado afectado."</span>',
    C2 + ["urinario", "pielonefritis"])

add_cloze(deck_c2,
    "Colico renal - exploracion: dolor {{c1::lumbar irradiado a ingle/genital}}, paciente {{c2::inquieto sin postura antialgica clara}}, abdomen blando, puede haber {{c3::Giordano +}} pero {{c4::SIN signos peritoneales}}",
    '<span class="contraste">Abdomen quirurgico: paciente quieto. Colico: paciente se retuerce.</span>',
    C2 + ["urinario", "colico_renal"])

add_cloze(deck_c2,
    "Lumbalgia - exploracion neurologica: {{c1::Lasegue (SLR)}} para radiculopatia L5/S1, {{c2::reflejos rotuliano (L4) y aquileo (S1)}}, {{c3::fuerza por miotoma}}, {{c4::sensibilidad por dermatoma}}",
    '<span class="ecoe">ECOE: "Lasegue positivo a 45 grados sugiere compresion radicular."</span>',
    C2 + ["dolor", "lumbalgia"])

add_cloze(deck_c2,
    "Banderas rojas en lumbalgia: {{c1::fiebre}}, {{c2::trauma significativo}}, {{c3::&gt;50 anos primera vez}}, {{c4::antecedente de cancer}}, {{c5::perdida de peso}}, {{c6::deficit neurologico progresivo}}, {{c7::anestesia en silla de montar/retencion urinaria (cauda equina)}}, {{c8::uso de drogas IV/inmunosupresion}}",
    '<span class="redflag">Bandera roja = imagen + estudios; no es lumbalgia mecanica.</span>',
    C2 + ["dolor", "lumbalgia", "redflag"])

add_cloze(deck_c2,
    "Cefalea - exploracion neurologica: {{c1::TA}}, {{c2::fondo de ojo (papiledema?)}}, {{c3::pares craneales}}, {{c4::signos meningeos (Kernig, Brudzinski, rigidez de nuca)}}, {{c5::deficit motor/sensorial focal}}",
    '<span class="redflag">Cualquier hallazgo focal o meningeo -&gt; estudios urgentes.</span>',
    C2 + ["dolor", "cefalea"])

add_cloze(deck_c2,
    "Dolor toracico - exploracion: {{c1::TA en AMBOS brazos (asimetria &gt;20 mmHg sugiere diseccion)}}, {{c2::pulsos perifericos (radiales, femorales)}}, {{c3::auscultacion cardiaca (soplos, R3, frote)}}, {{c4::auscultacion pulmonar}}, {{c5::signos de TVP en MMII}}",
    '<span class="redflag">Asimetria TA brazos o pulsos = sospecha diseccion aortica.</span>',
    C2 + ["dolor", "dolor_toracico"])

add_cloze(deck_c2,
    "Vertigo - exploracion: {{c1::Romberg}}, {{c2::Dix-Hallpike para VPPB}}, {{c3::observar nistagmo (direccion, fatigable o no)}}, {{c4::HINTS para descartar central}}, {{c5::pares craneales}}",
    '<span class="contraste">Periferico: nistagmo unidireccional, fatigable, no signos centrales. Central: nistagmo cambia direccion, no fatigable, signos focales.</span>',
    C2 + ["dolor", "vertigo"])

add_cloze(deck_c2,
    "Red flags dolor abdominal: {{c1::peritonismo}}, {{c2::fiebre alta}}, {{c3::distension progresiva}}, {{c4::hematemesis/melena}}, {{c5::ictericia}}, {{c6::inestabilidad hemodinamica}}",
    '<span class="redflag">Red flag = imagen y/o laparoscopia/laparotomia.</span>',
    C2 + ["abdomen", "redflag"])

# Cronicos + Preventivo (8)
add_cloze(deck_c2,
    "Toma correcta de TA: paciente {{c1::sentado con espalda apoyada, pies en piso}}, {{c2::reposo &gt;=5 min}}, {{c3::brazo a nivel del corazon}}, manguito {{c4::cubre 80% del brazo}}; {{c5::2 tomas separadas 1-2 min}}, promediar; medir en {{c6::ambos brazos}} la primera vez",
    '<span class="ecoe">ECOE: "Verifico tecnica antes de declarar HTA."</span>',
    C2 + ["cronico", "hta"])

add_cloze(deck_c2,
    "Exploracion del pie diabetico: {{c1::inspeccion (deformidades, callos, ulceras, infeccion)}}, {{c2::monofilamento 10 g en 4-10 puntos plantares}}, {{c3::diapason 128 Hz (vibracion)}}, {{c4::reflejos aquileos}}, {{c5::pulsos pedios y tibiales posteriores}}",
    '<span class="ecoe">ECOE: "Tamizaje completo de pie diabetico anual."</span>',
    C2 + ["cronico", "dm2", "pie_diabetico"])

add_cloze(deck_c2,
    "Exploracion CV en consulta familiar: {{c1::TA}}, {{c2::FC y ritmo}}, {{c3::soplos cardiacos (R1-R2, R3, R4, sistolicos/diastolicos)}}, {{c4::soplos carotideos}}, {{c5::ingurgitacion yugular}}, {{c6::pulsos perifericos}}, {{c7::edemas}}",
    '<span class="ecoe">ECOE: "Exploracion CV sin hallazgos patologicos."</span>',
    C2 + ["cardio"])

add_cloze(deck_c2,
    "Tiroides - exploracion: {{c1::inspeccion (asimetria, masa visible al deglutir)}}, {{c2::palpacion bilateral con paciente deglutiendo}}, {{c3::auscultacion (soplo tiroideo en hipertiroidismo)}}, {{c4::evaluar nodulos: consistencia, movilidad, ganglios cervicales}}",
    '<span class="ecoe">ECOE: "Tiroides palpable normal sin nodulos."</span>',
    C2 + ["cronico", "tiroides"])

add_cloze(deck_c2,
    "Signos de anemia en exploracion: {{c1::palidez de piel y mucosas (conjuntivas, lecho ungueal)}}, {{c2::queilosis angular}}, {{c3::glositis depapilada}}, {{c4::coiloniquia (uñas en cuchara)}} en ferropenia severa",
    '<span class="ecoe">ECOE: "Palidez de mucosas con queilosis sugiere anemia ferropenica."</span>',
    C2 + ["cronico", "anemia"])

add_cloze(deck_c2,
    "Antropometria del adulto: {{c1::peso, talla, IMC}}; {{c2::perimetro abdominal}} (riesgo CV: &gt;102 cm hombres, &gt;88 cm mujeres); {{c3::TA}}; {{c4::FC}}; calcular {{c5::riesgo ASCVD 10 anos si 40-79}}",
    '<span class="ecoe">ECOE: "IMC X, perimetro Y, calcular riesgo CV."</span>',
    C2 + ["preventivo"])

add_cloze(deck_c2,
    "Tamizajes USPSTF en consulta de adulto sano: {{c1::TA (anual)}}, {{c2::DM2 si 35-70 con sobrepeso}}, {{c3::lipidos cada 4-6 anos si 40-75}}, {{c4::Pap segun edad}}, {{c5::colonoscopia desde 45 anos}}, {{c6::mamografia 40-74}}, {{c7::AAA en hombres fumadores 65-75}}",
    '<span class="ecoe">ECOE: "Ofrezco tamizajes que corresponden a su edad y factores."</span>',
    C2 + ["preventivo"])

add_cloze(deck_c2,
    "Inmunizaciones del adulto a verbalizar: {{c1::influenza anual}}, {{c2::Tdap c/10 anos (refuerzo)}}, {{c3::neumococo (PCV20 o PCV15+PPSV23) en &gt;=65 o riesgo}}, {{c4::zoster (Shingrix) en &gt;=50}}, {{c5::COVID actualizado}}, {{c6::VPH hasta 26 anos (45 en algunos casos)}}",
    '<span class="ecoe">ECOE: "Reviso esquema y actualizo vacunas faltantes."</span>',
    C2 + ["preventivo", "vacunas"])


# ============================================================
# CAPA 3 - ESTUDIOS E INTERPRETACION (30 cloze)
# ============================================================
C3 = ["capa3", "estudios"]

# Respiratorio + ORL (8)
add_cloze(deck_c3,
    "Rx torax en neumonia: {{c1::consolidacion lobar/segmentaria}} con broncograma aereo -> probable {{c2::bacteriana (S. pneumoniae el #1)}}; {{c3::infiltrado intersticial difuso}} -> probable {{c4::viral/atipica (Mycoplasma, Chlamydophila)}}",
    '<span class="ecoe">ECOE: "Consolidacion en lobulo inferior derecho compatible con NAC."</span>',
    C3 + ["neumonia"])

add_cloze(deck_c3,
    "CURB-65 (riesgo en NAC): {{c1::Confusion}}, {{c2::Urea &gt;19 mg/dL (BUN &gt;7 mmol/L)}}, {{c3::FR &gt;=30}}, {{c4::BP &lt;90/60}}, {{c5::edad &gt;=65}}; 0-1 ambulatorio, 2 hospital, &gt;=3 UCI",
    '<span class="ecoe">ECOE: "Calcula CURB-65 antes de decidir manejo ambulatorio."</span>',
    C3 + ["neumonia"])

add_cloze(deck_c3,
    "BH en infeccion bacteriana vs viral: {{c1::leucocitosis con neutrofilia y bandas}} -> bacteriana; {{c2::linfocitosis o leucopenia}} -> viral; {{c3::eosinofilia}} -> parasitos o alergia",
    '<span class="ecoe">ECOE: "Patron de BH sugiere etiologia bacteriana."</span>',
    C3 + ["laboratorio"])

add_cloze(deck_c3,
    "Test rapido faringitis (strep A): si {{c1::positivo}} -> tratar; si {{c2::negativo en nino o adolescente}} -> confirmar con cultivo; en adulto puede prescindirse del cultivo (baja prevalencia)",
    '<span class="ecoe">ECOE: "Centor &gt;=3 + RADT positivo -&gt; antibiotico."</span>',
    C3 + ["faringitis"])

add_cloze(deck_c3,
    "Espirometria en asma: {{c1::FEV1/FVC &lt;70%}} (o &lt;LLN) + {{c2::reversibilidad post-broncodilatador (delta FEV1 &gt;=12% y &gt;=200 mL)}}",
    '<span class="contraste">Reversibilidad significativa = asma; sin reversibilidad = EPOC.</span>',
    C3 + ["asma"])

add_cloze(deck_c3,
    "Espirometria en EPOC: {{c1::FEV1/FVC &lt;70% post-broncodilatador}}; severidad GOLD por FEV1: {{c2::GOLD 1 &gt;=80%}}, {{c3::GOLD 2 50-79%}}, {{c4::GOLD 3 30-49%}}, {{c5::GOLD 4 &lt;30%}}",
    '<span class="ecoe">ECOE: "EPOC GOLD X segun FEV1 postBD."</span>',
    C3 + ["epoc"])

add_cloze(deck_c3,
    "SatO2 en exacerbacion respiratoria: {{c1::&lt;92% al aire ambiente}} = severa, requiere O2 y posible hospitalizacion; {{c2::&lt;90%}} = critica",
    '<span class="ecoe">ECOE: "SatO2 baja, indica oxigeno y nivel de atencion superior."</span>',
    C3 + ["respiratorio"])

add_cloze(deck_c3,
    "Influenza - dx: {{c1::PCR multiplex o test rapido de antigeno (RIDT)}}; tratar empiricamente con oseltamivir si {{c2::&lt;48 h del inicio + alto riesgo de complicacion}} (embarazo, &gt;=65, comorbilidad, inmunocomprometido)",
    '<span class="ecoe">ECOE: "Indicacion de oseltamivir por alto riesgo."</span>',
    C3 + ["influenza"])

# Urinario + Abdominal + Dolor (10)
add_cloze(deck_c3,
    "EGO sugestivo de ITU: {{c1::esterasa leucocitaria positiva}}, {{c2::nitritos positivos (especificidad alta)}}, {{c3::leucocitos &gt;=10/campo}}, {{c4::piuria}}; hematuria puede acompanar",
    '<span class="ecoe">ECOE: "EGO compatible con ITU; inicio empirico."</span>',
    C3 + ["itu"])

add_cloze(deck_c3,
    "Urocultivo - cuando: {{c1::ITU complicada}}, {{c2::ITU recurrente}}, {{c3::embarazo}}, {{c4::pielonefritis}}, {{c5::falla a Tx empirico}}; significativo si {{c6::&gt;=10^5 UFC/mL}} (&gt;=10^2 en sintomatica con cateter)",
    '<span class="ecoe">ECOE: "Solicito urocultivo por X razon."</span>',
    C3 + ["itu"])

add_cloze(deck_c3,
    "ITU baja no complicada vs pielonefritis: ITU baja = {{c1::disuria, frecuencia, urgencia, sin fiebre}}; pielonefritis = {{c2::fiebre, dolor lumbar, escalofrios, +/- sintomas urinarios bajos, leucocitosis sistemica}}",
    '<span class="contraste">Hay fiebre y dolor lumbar = ya no es ITU baja.</span>',
    C3 + ["itu"])

add_cloze(deck_c3,
    "USG renal en ITU - cuando: {{c1::pielonefritis con falla a Tx en 48-72 h}}, {{c2::sospecha de obstruccion (litiasis, anomalia)}}, {{c3::primera ITU febril en nino}}, {{c4::ITU recurrente con anomalia estructural sospechada}}",
    '<span class="ecoe">ECOE: "Solicito USG para descartar obstruccion."</span>',
    C3 + ["itu"])

add_cloze(deck_c3,
    "TC sin contraste abdomen y pelvis: gold standard para {{c1::litiasis urinaria (calculos &gt;=2 mm)}}; tambien util en {{c2::apendicitis dudosa}}, {{c3::diverticulitis}}, {{c4::abdomen agudo}}",
    '<span class="ecoe">ECOE: "TC sin contraste por sospecha de colico renal."</span>',
    C3 + ["abdomen"])

add_cloze(deck_c3,
    "Apendicitis - hallazgos: {{c1::leucocitosis con neutrofilia}}, {{c2::PCR elevada}}; imagen: USG con {{c3::apendice &gt;6-7 mm, no compresible}} o TC con {{c4::engrosamiento de pared apendicular y trabeculacion grasa}}",
    '<span class="ecoe">ECOE: "Imagen confirma apendicitis aguda."</span>',
    C3 + ["apendicitis"])

add_cloze(deck_c3,
    "Score de Alvarado para apendicitis (MANTRELS): {{c1::Migracion del dolor}}, {{c2::Anorexia}}, {{c3::Nauseas/vomito}}, {{c4::dolor en FID (Tenderness)}}, {{c5::Rebote (Rebound)}}, {{c6::fiebre Elevada}}, {{c7::Leucocitosis}}, {{c8::desviacion izquierda (Shift)}}; {{c9::&gt;=7 alta sospecha}}",
    '<span class="ecoe">ECOE: "Alvarado X, indica imagen o cirugia."</span>',
    C3 + ["apendicitis"])

add_cloze(deck_c3,
    "ECG en dolor toracico - busco: {{c1::elevacion del ST &gt;=1 mm en 2 derivaciones contiguas (IAM con ST)}}, {{c2::depresion ST/T invertidas (isquemia)}}, {{c3::BCRI nuevo (equivalente IAM)}}, {{c4::Q patologicas (necrosis antigua)}}, {{c5::arritmias}}",
    '<span class="redflag">ECG normal NO descarta SCA; usar troponinas seriadas si sospecha.</span>',
    C3 + ["dolor_toracico"])

add_cloze(deck_c3,
    "Troponina (hs-Tn): cuando {{c1::&gt; percentil 99 con curva (subida/bajada)}} = lesion miocardica; si sintomas + hs-Tn elevada -&gt; {{c2::SCA}}; algoritmo 0-1h o 0-3h segun protocolo",
    '<span class="ecoe">ECOE: "Solicito hs-Tn al ingreso y a la hora."</span>',
    C3 + ["dolor_toracico"])

add_cloze(deck_c3,
    "Cefalea - imagen urgente: {{c1::cefalea en trueno (descartar HSA)}}, {{c2::deficit focal o convulsion}}, {{c3::fiebre + signos meningeos}}, {{c4::&gt;50 anos primera vez (descartar arteritis temporal/tumor)}}, {{c5::postraumatica}}, {{c6::inmunodeprimido}}",
    '<span class="ecoe">ECOE: "TC sin contraste por red flag X."</span>',
    C3 + ["cefalea", "redflag"])

# Cronicos + Preventivo (12)
add_cloze(deck_c3,
    "HTA - clasificacion ACC/AHA 2017: {{c1::&lt;120/&lt;80 normal}}, {{c2::120-129/&lt;80 elevada}}, {{c3::130-139/80-89 estadio 1}}, {{c4::&gt;=140/90 estadio 2}}",
    '<span class="ecoe">ECOE: "TA de X clasifica como estadio Y."</span>',
    C3 + ["hta"])

add_cloze(deck_c3,
    "DM2 - criterios diagnosticos ADA (cualquiera, repetir si asintomatico): {{c1::glucosa en ayuno &gt;=126 mg/dL}}, {{c2::HbA1c &gt;=6.5%}}, {{c3::glucosa 2h en CTOG con 75g &gt;=200}}, {{c4::glucosa random &gt;=200 + sintomas clasicos}}",
    '<span class="ecoe">ECOE: "Cumple criterio X de ADA; confirmo DM2."</span>',
    C3 + ["dm2"])

add_cloze(deck_c3,
    "Prediabetes (ADA): {{c1::glucosa ayuno 100-125 (IFG)}}, {{c2::HbA1c 5.7-6.4%}}, {{c3::glucosa 2h en CTOG 140-199 (IGT)}}",
    '<span class="ecoe">ECOE: "Prediabetes; intervencion intensiva en estilo de vida y considerar metformina."</span>',
    C3 + ["dm2"])

add_cloze(deck_c3,
    "HbA1c metas (ADA): {{c1::&lt;7% general}}, {{c2::&lt;6.5% si joven, sin comorbilidad, baja exposicion a hipoglucemia}}, {{c3::&lt;8% en ancianos fragiles o expectativa de vida limitada}}",
    '<span class="ecoe">ECOE: "Meta de HbA1c &lt;7% por su perfil."</span>',
    C3 + ["dm2"])

add_cloze(deck_c3,
    "Dislipidemia - metas LDL ACC/AHA 2018 segun riesgo: {{c1::muy alto (ASCVD + factor de riesgo extra) LDL &lt;55 mg/dL}}, {{c2::alto (ASCVD) &lt;70}}, {{c3::moderado (ASCVD &gt;=7.5% a 10 anos) &lt;100}}, {{c4::bajo &lt;130}}",
    '<span class="ecoe">ECOE: "Meta LDL de &lt;X segun su riesgo."</span>',
    C3 + ["dislipidemia"])

add_cloze(deck_c3,
    "Riesgo ASCVD a 10 anos (calculadora ACC/AHA): {{c1::&lt;5% bajo}}, {{c2::5-7.5% borderline}}, {{c3::7.5-20% intermedio}}, {{c4::&gt;=20% alto}}",
    '<span class="ecoe">ECOE: "Calculo riesgo y oriento sobre estatina."</span>',
    C3 + ["dislipidemia"])

add_cloze(deck_c3,
    "Anemia ferropenica - perfil: {{c1::Hb baja}}, {{c2::VCM bajo (microcitico)}}, {{c3::HCM bajo (hipocromico)}}, {{c4::RDW alto}}, {{c5::ferritina baja (&lt;15-30 ng/mL)}}, hierro serico bajo, capacidad de fijacion alta",
    '<span class="ecoe">ECOE: "Patron ferropenico, indico hierro + buscar fuente de sangrado."</span>',
    C3 + ["anemia"])

add_cloze(deck_c3,
    "Anemia megaloblastica (B12 o folato): {{c1::Hb baja}}, {{c2::VCM alto (macrocitica)}}, {{c3::B12 baja (&lt;200 pg/mL)}} o folato bajo, frotis con {{c4::macrocitos ovalados e hipersegmentacion neutrofilica (&gt;=5 lobulos)}}",
    '<span class="ecoe">ECOE: "Macrocitica con B12 baja; reposicion."</span>'
    '<span class="redflag">B12 baja + sintomas neurologicos -&gt; tratar SI O SI parenteral.</span>',
    C3 + ["anemia"])

add_cloze(deck_c3,
    "Anemia de enfermedad cronica: {{c1::Hb baja}}, VCM {{c2::normal (mas comun) o ligeramente bajo}}, ferritina {{c3::normal o alta (porque es reactante de fase aguda)}}, hierro serico bajo, capacidad de fijacion {{c4::baja o normal}}",
    '<span class="contraste">Ferropenica: ferritina BAJA. Enf cronica: ferritina NORMAL/ALTA.</span>',
    C3 + ["anemia"])

add_cloze(deck_c3,
    "Hipotiroidismo primario: {{c1::TSH alta}} + {{c2::T4 libre baja}}; subclinico = {{c3::TSH alta + T4L normal}}; secundario = {{c4::TSH baja/normal + T4L baja}} (hipofisis)",
    '<span class="ecoe">ECOE: "Hipotiroidismo primario; inicio levotiroxina."</span>',
    C3 + ["tiroides"])

add_cloze(deck_c3,
    "Hipertiroidismo: {{c1::TSH baja}} + {{c2::T4L y/o T3 altas}}; en Graves agregar {{c3::TRAb (anti-receptor de TSH)}}, anti-TPO; gammagrafia/RAIU si duda etiologica",
    '<span class="ecoe">ECOE: "Patron de hipertiroidismo primario, evaluar Graves."</span>',
    C3 + ["tiroides"])

add_cloze(deck_c3,
    "Tamizaje USPSTF de DM2: ofrecer en adultos {{c1::35-70 anos con sobrepeso/obesidad}}; cada {{c2::3 anos}} si normal",
    '<span class="ecoe">ECOE: "Solicito glucosa de tamiz por edad y peso."</span>',
    C3 + ["preventivo", "dm2"])


# ============================================================
# CAPA 4 - DIFERENCIALES RAPIDOS (35 cloze)
# ============================================================
C4 = ["capa4", "diferenciales"]

# Respiratorio + ORL (12)
add_cloze(deck_c4,
    "Tos + fiebre: anchor {{c1::neumonia (crepitantes + consolidacion)}}; contraste {{c2::bronquitis aguda (auscultacion limpia)}}; variaciones {{c3::influenza (sistemico intenso)}}, {{c4::COVID (anosmia + sistemico)}}",
    '<span class="redflag">SatO2 &lt;92% o CURB-65 &gt;=2 -&gt; referir.</span>',
    C4 + ["respiratorio"])

add_cloze(deck_c4,
    "Disnea aguda: {{c1::asma exacerbacion (sibilancias, reversible)}}, {{c2::EPOC exacerbacion (espiracion prolongada, antecedente)}}, {{c3::NAC (fiebre + foco)}}, {{c4::edema pulmonar (estertores difusos, ortopnea)}}, {{c5::TEP (taquicardia + factor de riesgo)}}, {{c6::neumotorax (dolor pleuritico subito, hipersonido)}}",
    '<span class="redflag">Asimetria + dolor pleuritico subito -&gt; descartar neumotorax con Rx.</span>',
    C4 + ["respiratorio"])

add_cloze(deck_c4,
    "Otalgia: anchor {{c1::OMA (timpano abombado, fiebre)}}; contraste {{c2::otitis externa (dolor al trago)}}; variaciones {{c3::ATM (dolor mandibular)}}, {{c4::dental referida}}, {{c5::mastoiditis (eritema retroauricular = urgencia)}}",
    '<span class="redflag">Mastoiditis: ingresar para antibiotico IV.</span>',
    C4 + ["orl"])

add_cloze(deck_c4,
    "Odinofagia: anchor {{c1::faringitis viral (rinorrea, sin exudado)}}; contraste {{c2::estreptococica (exudado + adenopatia + sin tos)}}; variaciones {{c3::mononucleosis (adenopatia generalizada, esplenomegalia)}}, {{c4::absceso periamigdalino (uvula desplazada, voz de papa caliente)}}",
    '<span class="redflag">Absceso periamigdalino -&gt; drenaje + antibiotico IV.</span>',
    C4 + ["orl"])

add_cloze(deck_c4,
    "Rinorrea: {{c1::IVAS viral (clara, &lt;7 dias)}}, {{c2::rinitis alergica (clara + prurito + estornudos, cronica)}}, {{c3::sinusitis bacteriana (purulenta + dolor facial, &gt;10 dias o doble empeoramiento)}}",
    '<span class="contraste">No todo lo verde-amarillo es bacteriano; duracion y patron mandan.</span>',
    C4 + ["orl"])

add_cloze(deck_c4,
    "Estornudos + prurito ocular/nasal + ojos llorosos + clinica estacional/perenne -> {{c1::rinitis alergica}}; sin fiebre, suele tener {{c2::historia familiar o personal de atopia}}",
    '<span class="ecoe">ECOE: "Rinitis alergica; inicio CIE nasal + antihistaminico."</span>',
    C4 + ["orl", "alergia"])

add_cloze(deck_c4,
    "Tos cronica (&gt;=8 sem) - top 3 causas: {{c1::sindrome de tos por via aerea superior (goteo postnasal)}}, {{c2::asma}}, {{c3::ERGE}}; otras: tabaquismo/EPOC, IECA (tos seca), bronquiectasias, TB",
    '<span class="ecoe">ECOE: "Evaluo causas habituales y descarto red flags."</span>'
    '<span class="redflag">Tos + hemoptisis, perdida peso, fumador -&gt; descartar Ca pulmon.</span>',
    C4 + ["respiratorio"])

add_cloze(deck_c4,
    "Sibilancias en adulto: {{c1::asma (reversible)}}, {{c2::EPOC (no reversible, fumador)}}, {{c3::ICC (asma cardiaca, mas estertores)}}, {{c4::cuerpo extrano (subito, unilateral)}}, {{c5::anafilaxia (con urticaria, hipotension)}}",
    '<span class="redflag">Anafilaxia: epinefrina IM inmediata.</span>',
    C4 + ["respiratorio"])

add_cloze(deck_c4,
    "Faringe con exudado: {{c1::estreptococo grupo A (Centor positivo)}}, {{c2::mononucleosis (adenopatia generalizada, esplenomegalia, fatiga, jovenes)}}, {{c3::gonorrea farangea (historia sexual)}}, {{c4::candidiasis (inmunocomprometido, placas blancas)}}",
    '<span class="redflag">Mono + amoxicilina = rash. Evitar empirico.</span>',
    C4 + ["orl"])

add_cloze(deck_c4,
    "Acufeno (tinnitus) - causas: {{c1::OMA/serosa}}, {{c2::otosclerosis}}, {{c3::Meniere (vertigo + hipoacusia + tinnitus)}}, {{c4::presbiacusia}}, {{c5::ototoxicos (aminoglucosidos, AINE, furosemida, cisplatino)}}",
    '<span class="redflag">Acufeno unilateral pulsatil -&gt; descartar tumor vascular/neuroma.</span>',
    C4 + ["orl"])

add_cloze(deck_c4,
    "Disfonia: aguda (&lt;2 sem) suele ser {{c1::laringitis viral}}; cronica (&gt;2 sem) requiere {{c2::laringoscopia para descartar Ca laringeo}} especialmente en fumadores",
    '<span class="redflag">Disfonia &gt;2 sem en fumador -&gt; referencia urgente ORL.</span>',
    C4 + ["orl"])

add_cloze(deck_c4,
    "Epistaxis: {{c1::anterior 90% (plexo de Kiesselbach)}} - controlable con compresion; {{c2::posterior 10%}} - dificil de controlar, hipertenso/anciano, mas grave; descartar {{c3::HTA, anticoagulacion, trauma, neoplasia}}",
    '<span class="redflag">Epistaxis posterior recurrente -&gt; referencia ORL.</span>',
    C4 + ["orl"])

# Urinario + Abdominal + Dolor (12)
add_cloze(deck_c4,
    "Disuria: anchor {{c1::ITU baja (frecuencia + urgencia, EGO con leucos/nitritos)}}; contraste {{c2::uretritis (ITS - gonorrea, chlamydia)}}; variaciones {{c3::vaginitis (en mujer; flujo, prurito)}}, {{c4::prostatitis (varon; dolor perineal, fiebre)}}",
    '<span class="ecoe">ECOE: "Disuria + flujo en mujer joven -&gt; tamizo ITS."</span>',
    C4 + ["urinario"])

add_cloze(deck_c4,
    "Hematuria: {{c1::ITU (sintomas urinarios)}}, {{c2::litiasis (dolor colico)}}, {{c3::Ca vejiga (indolora en &gt;40 fumador)}}, {{c4::glomerulonefritis (HTA + proteinuria + cilindros)}}, {{c5::trauma}}",
    '<span class="redflag">Hematuria indolora en &gt;40 anos -&gt; cistoscopia (descartar Ca vejiga).</span>',
    C4 + ["urinario"])

add_cloze(deck_c4,
    "Dolor lumbar agudo: anchor {{c1::mecanico (con movimiento, sin red flags)}}; contraste {{c2::colico renal (irradiado a ingle, inquieto)}}; variaciones {{c3::pielonefritis (fiebre + Giordano)}}, {{c4::herpes zoster (dolor + vesiculas en dermatoma)}}",
    '<span class="redflag">Cualquier red flag = imagen + estudios.</span>',
    C4 + ["dolor", "lumbalgia"])

add_cloze(deck_c4,
    "Dolor en FID: anchor {{c1::apendicitis (migracion + Blumberg + leucocitosis)}}; contrastes {{c2::ginecologico (ovulacion, ectopico, torsion, EIP - en mujer)}}, {{c3::ITU/colico renal}}, {{c4::adenitis mesenterica (joven, post-viral)}}, {{c5::diverticulitis cecal (raro)}}",
    '<span class="ecoe">ECOE: "Mujer + dolor FID = test de embarazo OBLIGADO."</span>',
    C4 + ["abdomen"])

add_cloze(deck_c4,
    "Dolor epigastrico: {{c1::dispepsia/gastritis (postprandial, alivia con antiacido)}}, {{c2::ulcera peptica (relacion comidas, sangrado)}}, {{c3::pancreatitis (irradiado a espalda, vomito, lipasa alta)}}, {{c4::colelitiasis/colecistitis (postprandial graso, Murphy)}}, {{c5::IAM inferior (cuidado en diabeticos/ancianos)}}",
    '<span class="redflag">Epigastralgia + factores de riesgo CV -&gt; ECG SIEMPRE.</span>',
    C4 + ["abdomen"])

add_cloze(deck_c4,
    "Dolor toracico - tiempo critico: {{c1::SCA (opresivo, irradiado, sudoracion, factores CV)}}, {{c2::TEP (pleuritico + disnea + factor de riesgo)}}, {{c3::diseccion aortica (desgarro, irradiado a espalda, asimetria TA)}}, {{c4::neumotorax}}, {{c5::pericarditis (mejora sentado/inclinado, frote)}}; benignos: {{c6::costocondritis, ERGE, ansiedad}}",
    '<span class="redflag">Los 4 primeros son mortales si se pierden.</span>',
    C4 + ["dolor_toracico"])

add_cloze(deck_c4,
    "Cefalea red flags: {{c1::trueno (HSA)}}, {{c2::deficit focal nuevo (EVC/masa)}}, {{c3::fiebre + meningismo (meningitis)}}, {{c4::&gt;50 anos nueva con dolor temporal (arteritis temporal)}}, {{c5::papiledema (HTIC)}}, {{c6::vomito en escopeta matutino (HTIC)}}",
    '<span class="redflag">Cualquier red flag = imagen urgente.</span>',
    C4 + ["cefalea"])

add_cloze(deck_c4,
    "Cefalea primaria benigna: {{c1::tensional (opresiva bilateral, sin nauseas)}}, {{c2::migrana (pulsatil hemicraneal + nauseas + foto/fonofobia)}}, {{c3::cluster (unilateral periorbitaria intensa + lagrimeo + congestion nasal)}}",
    '<span class="ecoe">ECOE: "Cefalea primaria; no requiere imagen rutinaria."</span>',
    C4 + ["cefalea"])

add_cloze(deck_c4,
    "Mareo - clarificar: {{c1::vertigo (sensacion de movimiento - VPPB, vestibular, central)}}, {{c2::presincope (mareo + perdida inminente del estado de alerta - ortostatismo, arritmia)}}, {{c3::desequilibrio (inestabilidad al caminar - multifactorial en ancianos)}}",
    '<span class="ecoe">ECOE: "Primero clarificar QUE tipo de mareo."</span>',
    C4 + ["vertigo"])

add_cloze(deck_c4,
    "Diarrea aguda (&lt;14 dias): {{c1::viral (autoresolutiva, sin sangre)}}, {{c2::bacteriana (sangre/fiebre alta, Salmonella, Shigella, Campylobacter)}}, {{c3::toxina alimentaria (S. aureus, B. cereus - inicio rapido)}}, {{c4::C. difficile (antibiotico reciente)}}, {{c5::parasitaria (subaguda, Giardia)}}",
    '<span class="redflag">Sangre, fiebre alta, deshidratacion severa, inmunodeprimido -&gt; coprocultivo + considerar antibiotico.</span>',
    C4 + ["abdomen", "gastroenteritis"])

add_cloze(deck_c4,
    "Diarrea cronica (&gt;=4 sem): {{c1::SII (sin red flags, alteracion del habito)}}, {{c2::IBD - Crohn/CUCI (sangre, perdida de peso, sintomas extraintestinales)}}, {{c3::celiaquia/malabsorcion}}, {{c4::infeccion parasitaria}}, {{c5::hipertiroidismo}}, {{c6::Ca colon en &gt;50}}",
    '<span class="redflag">Sangre, perdida peso, anemia, &gt;50, historia familiar Ca -&gt; colonoscopia.</span>',
    C4 + ["abdomen"])

add_cloze(deck_c4,
    "Vomito: {{c1::gastroenteritis (con diarrea)}}, {{c2::obstruccion intestinal (sin gas/heces, dolor colico)}}, {{c3::gastroparesia (DM, posprandial)}}, {{c4::embarazo (test obligado en mujer en edad reproductiva)}}, {{c5::farmacos/quimio}}, {{c6::HTIC (en escopeta, matutino, +cefalea)}}",
    '<span class="ecoe">ECOE: "Vomito en mujer = test de embarazo."</span>',
    C4 + ["abdomen"])

# Cronicos + Preventivo (11)
add_cloze(deck_c4,
    "Hiperglucemia descompensada: {{c1::DKA (T1 mas comun, glucosa 250-600, cetonas, acidosis, anion gap)}}; {{c2::EHH (T2, glucosa &gt;600, osmolaridad &gt;320, sin cetonas, sin acidosis)}}",
    '<span class="redflag">Ambos urgencia: hidratacion + insulina IV + electrolitos.</span>',
    C4 + ["dm2"])

add_cloze(deck_c4,
    "Hipoglucemia: causas en diabetico: {{c1::sulfonilureas}}, {{c2::insulina excesiva}}, {{c3::falla renal/hepatica}}, {{c4::alcohol}}, {{c5::ayuno o ejercicio sin ajuste}}; en no diabetico considerar {{c6::insulinoma, sepsis}}",
    '<span class="ecoe">ECOE: "Sulfonilurea + AKI = combinacion peligrosa para hipoglucemia."</span>',
    C4 + ["dm2"])

add_cloze(deck_c4,
    "Fatiga cronica (&gt;1 mes) - causas medicas a descartar: {{c1::anemia (BH)}}, {{c2::hipotiroidismo (TSH)}}, {{c3::depresion (PHQ-9)}}, {{c4::apnea sueño (Epworth, polisomnografia)}}, {{c5::ICC}}, {{c6::DM mal controlada}}, {{c7::cancer oculto}}",
    '<span class="ecoe">ECOE: "Tamiz dirigido: BH, TSH, glucosa, PHQ-9."</span>',
    C4 + ["cronico"])

add_cloze(deck_c4,
    "Perdida de peso involuntaria &gt;5% en 6 meses - causas: {{c1::Ca}}, {{c2::hipertiroidismo}}, {{c3::DM descompensada}}, {{c4::depresion}}, {{c5::malabsorcion (celiaquia, IBD)}}, {{c6::TB / VIH}}, {{c7::demencia (en ancianos)}}",
    '<span class="redflag">Estudio completo: BH, QS, TSH, VIH, TC torax-abdomen, endoscopia.</span>',
    C4 + ["cronico"])

add_cloze(deck_c4,
    "Edema bilateral: {{c1::ICC (disnea, ortopnea, R3, ingurgitacion yugular)}}, {{c2::IR (creatinina alta, proteinuria)}}, {{c3::cirrosis (estigmas hepaticos, ascitis)}}, {{c4::hipoalbuminemia (proteinas bajas)}}, {{c5::farmacos (CCB, AINE, glitazonas)}}",
    '<span class="ecoe">ECOE: "Sistematizar: cardiaco, renal, hepatico, farmacos."</span>',
    C4 + ["edema"])

add_cloze(deck_c4,
    "Edema unilateral de miembro inferior: anchor {{c1::TVP (dolor + edema + Wells positivo)}}; contraste {{c2::celulitis (eritema, calor, dolor a la palpacion, fiebre)}}; variaciones {{c3::linfedema (cronico, sin fovea)}}, {{c4::trauma/hematoma}}, {{c5::sindrome posflebitico}}",
    '<span class="redflag">Sospecha TVP -&gt; Wells + dimero-D y/o USG doppler.</span>',
    C4 + ["edema"])

add_cloze(deck_c4,
    "Sincope: {{c1::vasovagal (precipitante, prodromo, recuperacion rapida) - mas comun}}, {{c2::ortostatico (al ponerse de pie, drogas, hipovolemia)}}, {{c3::cardiogenico (subito, sin prodromo, ejercicio, FH muerte subita) - PELIGROSO}}",
    '<span class="redflag">Sincope con ejercicio o FH muerte subita -&gt; cardiologia urgente.</span>',
    C4 + ["sincope"])

add_cloze(deck_c4,
    "Sintomatologia tiroidea: hipo = {{c1::frio, fatiga, peso ganancia, piel seca, bradicardia, estrenimiento}}; hiper = {{c2::calor, sudor, peso perdida, taquicardia, ansiedad, diarrea, exoftalmos en Graves}}",
    '<span class="ecoe">ECOE: "Cuadro compatible con hipo/hipertiroidismo, solicito TSH."</span>',
    C4 + ["tiroides"])

add_cloze(deck_c4,
    "Anemia con LDH alta + bilirrubina indirecta alta + haptoglobina baja: {{c1::HEMOLISIS}}; investigar autoinmune (Coombs), G6PD, talasemia, drepanocitosis, valvulas mecanicas, microangiopatia (PTT/SUH)",
    '<span class="redflag">PTT/SUH: emergencia hematologica.</span>',
    C4 + ["anemia"])

add_cloze(deck_c4,
    "HTA secundaria - sospechar cuando: {{c1::&lt;30 anos o &gt;55 nueva}}, {{c2::refractaria a 3 farmacos optimizados}}, {{c3::hipocalemia espontanea (Conn)}}, {{c4::masa abdominal o crisis hipertensivas episodicas con sudor/palpitaciones (feocromocitoma)}}, {{c5::soplo abdominal (renovascular)}}",
    '<span class="ecoe">ECOE: "Tamiz de HTA secundaria por X razon."</span>',
    C4 + ["hta"])

add_cloze(deck_c4,
    "Soplos cardiacos: {{c1::sistolico de eyeccion (estenosis aortica, MCH)}}, {{c2::sistolico regurgitante (insuficiencia mitral)}}, {{c3::diastolico (estenosis mitral, insuficiencia aortica - SIEMPRE patologico)}}, {{c4::continuo (PCA)}}",
    '<span class="redflag">Diastolico = patologico; eco urgente.</span>',
    C4 + ["cardio"])


# ============================================================
# CAPA 5 - TRATAMIENTO PRACTICO (40 Q&A)
# ============================================================
C5 = ["capa5", "tratamiento"]

# Respiratorio + ORL (12)
add_qa(deck_c5,
    "Manejo: <b>NAC ambulatoria sin comorbilidades</b> (IDSA/ATS 2019)",
    "<b>Amoxicilina 1 g VO c/8 h por 5 dias</b> (1ra eleccion).<br>"
    "Alternativas: <b>doxiciclina 100 mg c/12 h</b> o <b>azitromicina 500 mg dia 1, luego 250 mg dias 2-5</b> (si baja resistencia a macrolidos).<br>"
    "Considerar duracion mas larga si no mejoria en 48-72 h."
    '<span class="ecoe">ECOE: "Amoxi 5 dias; reevaluar en 48-72 h."</span>',
    C5 + ["neumonia"])

add_qa(deck_c5,
    "Manejo: <b>NAC ambulatoria con comorbilidades</b> (DM, EPOC, ICC, alcoholismo, &gt;65)",
    "<b>Amoxicilina-clavulanato 875/125 mg c/12 h + macrolido (azitromicina)</b><br>"
    "<b>O</b> cefuroxima/cefpodoxima + macrolido<br>"
    "<b>O</b> monoterapia con <b>fluoroquinolona respiratoria</b>: levofloxacino 750 mg c/24 h o moxifloxacino 400 mg c/24 h.<br>"
    "Duracion 5-7 dias."
    '<span class="ecoe">ECOE: "Esquema de comorbilidades por su perfil."</span>',
    C5 + ["neumonia"])

add_qa(deck_c5,
    "Manejo: <b>Bronquitis aguda</b>",
    "<b>NO antibiotico</b> (es viral en &gt;90%).<br>"
    "Sintomatico: antitusivo si tos seca (dextrometorfano), broncodilatador inhalado si sibilancias, hidratacion, acetaminofen para fiebre.<br>"
    "Educar sobre duracion (tos puede durar 3 semanas)."
    '<span class="ecoe">ECOE: "Explico que es viral, no requiere antibiotico."</span>',
    C5 + ["bronquitis"])

add_qa(deck_c5,
    "Manejo: <b>Sinusitis bacteriana aguda</b> (IDSA)",
    "Criterios: sintomas &gt;10 dias, doble empeoramiento (mejora y vuelve a empeorar), o sintomas severos &gt;3-4 dias.<br>"
    "<b>Amoxicilina-clavulanato 875/125 mg VO c/12 h por 5-7 dias</b> (adultos).<br>"
    "Alergia a penicilina: doxiciclina o levofloxacino.<br>"
    "Sintomatico: corticoide nasal, irrigacion salina, analgesia."
    '<span class="ecoe">ECOE: "Cumple criterios; amoxi-clav 5-7 dias."</span>',
    C5 + ["sinusitis"])

add_qa(deck_c5,
    "Manejo: <b>Otitis media aguda en adulto/adolescente</b>",
    "<b>Amoxicilina 1 g VO c/8 h por 5-7 dias</b> (1ra eleccion).<br>"
    "Si falla en 48-72 h o uso reciente: <b>amoxi-clav 875/125 c/12 h</b>.<br>"
    "Analgesia con AINE o acetaminofen.<br>"
    "Observacion sin antibiotico solo en casos leves seleccionados (esp. niños)."
    '<span class="ecoe">ECOE: "Amoxi 5-7 dias + analgesia."</span>',
    C5 + ["otitis"])

add_qa(deck_c5,
    "Manejo: <b>Otitis externa aguda</b>",
    "<b>Ciprofloxacino + dexametasona gotas oticas</b> (Ciprodex) o ciprofloxacino solo, 4 gotas c/12 h por 7-10 dias.<br>"
    "Mantener oido seco. Analgesia VO. NO usar tapones de algodon humedos. <br>"
    "Antibiotico VO solo si: celulitis perilesional, otitis externa maligna (DM, inmunodeprimido), fiebre."
    '<span class="ecoe">ECOE: "Cipro gotas + mantener seco."</span>',
    C5 + ["otitis"])

add_qa(deck_c5,
    "Manejo: <b>Faringitis estreptococica (Centor &gt;=3 o RADT positivo)</b>",
    "<b>Penicilina V 500 mg VO c/12 h por 10 dias</b> O <b>amoxicilina 1 g/dia por 10 dias</b>.<br>"
    "Alergia: <b>cefalexina 500 mg c/12 h x 10 dias</b> (si no reaccion grave) o <b>azitromicina 500 mg dia 1, 250 mg dias 2-5</b> o <b>clindamicina</b>.<br>"
    "Sintomatico: AINE, hidratacion.<br>"
    "Tratar previene fiebre reumatica y disminuye contagio; NO previene glomerulonefritis."
    '<span class="ecoe">ECOE: "Penicilina o amoxi por 10 dias."</span>',
    C5 + ["faringitis"])

add_qa(deck_c5,
    "Manejo: <b>Asma exacerbacion leve-moderada</b>",
    "1) <b>SABA</b>: albuterol 4-8 puffs con espaciador o 2.5-5 mg nebulizado, repetir c/20 min x 1 h.<br>"
    "2) <b>Oxigeno</b> para SatO2 93-95%.<br>"
    "3) <b>Corticoide sistemico</b> si no respuesta optima a SABA: prednisona 40-60 mg VO x 5 dias (sin retiro gradual).<br>"
    "4) Si SatO2 &lt;92%, FC &gt;120, habla palabras, silencio auscultatorio -&gt; ingresar.<br>"
    "5) Plan de accion + revisar tecnica inhalatoria."
    '<span class="ecoe">ECOE: "SABA + corticoide oral 5 dias."</span>',
    C5 + ["asma"])

add_qa(deck_c5,
    "Manejo: <b>Exacerbacion EPOC</b>",
    "1) <b>SABA +/- SAMA</b> nebulizados (albuterol + ipratropio).<br>"
    "2) <b>Corticoide sistemico</b>: prednisona 40 mg VO x 5 dias.<br>"
    "3) <b>Antibiotico</b> si esputo purulento O 2 de 3 sintomas de Anthonisen (disnea, volumen, purulencia): amoxi-clav 5-7 dias o doxiciclina o macrolido.<br>"
    "4) <b>Oxigeno</b> con meta SatO2 88-92% (cuidado retenedor CO2).<br>"
    "5) Ingresar si severo o falla a Tx ambulatorio."
    '<span class="ecoe">ECOE: "SABA + corticoide + antibiotico por purulencia."</span>',
    C5 + ["epoc"])

add_qa(deck_c5,
    "Manejo: <b>Influenza</b>",
    "<b>Oseltamivir 75 mg VO c/12 h por 5 dias</b> si:<br>"
    "- &lt;48 h de inicio de sintomas<br>"
    "- Alto riesgo: embarazo, &gt;=65, &lt;5 anos, comorbilidad, inmunocomprometido, residentes de unidades de cuidado.<br>"
    "Sintomatico: acetaminofen, hidratacion. NO aspirina en jovenes (Reye).<br>"
    "Vacunacion anual previene; reportar a salud publica si brote."
    '<span class="ecoe">ECOE: "Inicia oseltamivir por estar dentro de las 48 h y alto riesgo."</span>',
    C5 + ["influenza"])

add_qa(deck_c5,
    "Manejo: <b>Rinitis alergica</b>",
    "1ra linea: <b>corticoide intranasal</b> (fluticasona, mometasona, budesonida) 1-2 puff por fosa c/24 h.<br>"
    "Agregar <b>antihistaminico oral 2da generacion</b> (loratadina 10 mg/dia, cetirizina 10 mg/dia, fexofenadina 180 mg/dia) si insuficiente o sintomas sistemicos.<br>"
    "Inmunoterapia (subcutanea o sublingual) si refractario y disparador identificado.<br>"
    "Educacion: evitar alergenos, control ambiental."
    '<span class="ecoe">ECOE: "CIE nasal + antihistaminico 2da gen."</span>',
    C5 + ["rinitis"])

add_qa(deck_c5,
    "Manejo: <b>Resfriado comun (IVAS viral)</b>",
    "<b>Sintomatico unicamente</b>: acetaminofen/ibuprofeno para fiebre y dolor, hidratacion, descongestionantes nasales (oximetazolina) MAX 3 dias para evitar rinitis medicamentosa, antihistaminicos 1ra gen en la noche.<br>"
    "<b>NO antibiotico</b>. Educacion sobre duracion (7-10 dias)."
    '<span class="ecoe">ECOE: "Explico autolimitacion, no antibiotico."</span>',
    C5 + ["ivas"])

# Urinario + Abdominal + Dolor (12)
add_qa(deck_c5,
    "Manejo: <b>ITU baja no complicada en mujer adulta no embarazada</b> (IDSA)",
    "<b>1ra linea:</b><br>"
    "- <b>Nitrofurantoina 100 mg VO c/12 h x 5 dias</b><br>"
    "- <b>TMP-SMX DS c/12 h x 3 dias</b> (si resistencia local &lt;20%)<br>"
    "- <b>Fosfomicina 3 g VO dosis unica</b><br>"
    "Alternativas: cefalexina, beta-lactamicos.<br>"
    "<b>NO usar fluoroquinolonas como 1ra linea en cistitis no complicada</b>."
    '<span class="ecoe">ECOE: "Nitrofurantoina 5 dias."</span>',
    C5 + ["itu"])

add_qa(deck_c5,
    "Manejo: <b>ITU/bacteriuria en embarazo</b>",
    "<b>SIEMPRE tratar</b> bacteriuria asintomatica en embarazo.<br>"
    "<b>Nitrofurantoina 100 mg c/12 h x 5-7 dias</b> (evitar 1er trimestre y &gt;36 sem)<br>"
    "<b>O cefalexina 500 mg c/6 h x 7 dias</b><br>"
    "<b>O amoxicilina 500 mg c/8 h x 7 dias</b> (segun susceptibilidad).<br>"
    "<b>EVITAR</b>: TMP-SMX en 1er trimestre y termino, fluoroquinolonas, tetraciclinas.<br>"
    "Urocultivo post-tratamiento para confirmar erradicacion."
    '<span class="ecoe">ECOE: "Cefalexina + urocultivo de control."</span>',
    C5 + ["itu", "embarazo"])

add_qa(deck_c5,
    "Manejo: <b>Pielonefritis no complicada ambulatoria</b>",
    "<b>Ciprofloxacino 500 mg VO c/12 h por 7 dias</b> (si resistencia local aceptable)<br>"
    "<b>O TMP-SMX DS c/12 h x 14 dias</b> (solo si susceptibilidad conocida).<br>"
    "Considerar 1 dosis IV inicial (ceftriaxona 1 g) si se opta por ambulatorio con FQ.<br>"
    "<b>Hospitalizar si</b>: vomito, sepsis, embarazo, comorbilidad, inestabilidad, falla a Tx en 72 h.<br>"
    "Urocultivo siempre."
    '<span class="ecoe">ECOE: "Cipro 7 dias + urocultivo."</span>',
    C5 + ["pielonefritis"])

add_qa(deck_c5,
    "Manejo: <b>Colico renal no complicado</b>",
    "1) <b>Analgesia: AINE</b> (ketorolaco 30 mg IV/IM o ibuprofeno 600 mg VO) 1ra linea; opioide si refractario.<br>"
    "2) <b>Hidratacion oral generosa</b>.<br>"
    "3) <b>Antiemetico</b> si nausea (ondansetron).<br>"
    "4) <b>Tamsulosina 0.4 mg/dia</b> (terapia medica expulsiva) si calculo 5-10 mm distal.<br>"
    "5) <b>Filtrar orina</b>.<br>"
    "6) Urologia si: calculo &gt;10 mm, obstruccion + infeccion (emergencia), falla a expulsion espontanea en 4-6 sem, rinon unico."
    '<span class="ecoe">ECOE: "AINE + tamsulosina + filtrar; control en 4 sem."</span>',
    C5 + ["colico_renal"])

add_qa(deck_c5,
    "Manejo: <b>Gastroenteritis viral aguda</b>",
    "<b>Rehidratacion oral</b> (SRO) - 1ra linea.<br>"
    "Antiemetico si vomito persistente: ondansetron 4 mg VO.<br>"
    "<b>NO antibiotico</b>; <b>NO antidiarreicos</b> (loperamida) si fiebre o sangre.<br>"
    "Reintroducir dieta normal pronto (BRAT no es necesario estrictamente).<br>"
    "Hospitalizar si deshidratacion severa, intolerancia VO, vulnerables (anciano, &lt;6 meses)."
    '<span class="ecoe">ECOE: "SRO + observacion; signos de alarma."</span>',
    C5 + ["gastroenteritis"])

add_qa(deck_c5,
    "Manejo: <b>Diarrea bacteriana severa (sangre, fiebre alta) o del viajero</b>",
    "<b>Azitromicina 1 g VO dosis unica</b> (preferida si resistencia a FQ o disenteria)<br>"
    "<b>O Ciprofloxacino 500 mg c/12 h x 1-3 dias</b>.<br>"
    "Para diarrea del viajero leve: loperamida + hidratacion sin antibiotico.<br>"
    "Coprocultivo si: sangre, fiebre alta, brote, inmunocomprometido, &gt;7 dias.<br>"
    "<b>NUNCA</b> antibioticos empiricos si sospecha de E. coli enterohemorragica (SUH)."
    '<span class="ecoe">ECOE: "Azitro dosis unica + hidratacion."</span>',
    C5 + ["gastroenteritis"])

add_qa(deck_c5,
    "Manejo: <b>Apendicitis aguda</b>",
    "1) NPO + hidratacion IV.<br>"
    "2) <b>Antibiotico IV preoperatorio</b>: cefoxitina o piperacilina-tazobactam o ceftriaxona + metronidazol.<br>"
    "3) <b>Apendicectomia (laparoscopica preferida)</b> en las primeras horas.<br>"
    "4) Analgesia (sin enmascarar el cuadro).<br>"
    "5) Considerar manejo no quirurgico con antibiotico en casos seleccionados no complicados (pero alta tasa de recurrencia)."
    '<span class="ecoe">ECOE: "NPO + ATB IV + apendicectomia urgente."</span>',
    C5 + ["apendicitis"])

add_qa(deck_c5,
    "Manejo: <b>Cefalea tensional</b>",
    "<b>Agudo</b>: AINE (ibuprofeno 400-600 mg, naproxeno 500 mg) o acetaminofen 1 g; <b>evitar opioides</b>.<br>"
    "<b>Profilaxis</b> si &gt;=2 episodios/sem o cefalea cronica: amitriptilina 10-50 mg en la noche; alternativas: mirtazapina, venlafaxina.<br>"
    "No farmacologico: relajacion, manejo de estres, ejercicio, higiene del sueno, tratamiento ortodontico si bruxismo."
    '<span class="ecoe">ECOE: "AINE en agudo, amitriptilina para profilaxis si frecuente."</span>',
    C5 + ["cefalea"])

add_qa(deck_c5,
    "Manejo: <b>Migrana</b>",
    "<b>Agudo</b>:<br>"
    "1) Leve: AINE (naproxeno, ibuprofeno) +/- antiemetico (metoclopramida).<br>"
    "2) Moderado-severo: <b>triptan</b> (sumatriptan 50-100 mg VO, o SC 6 mg si severo) - <b>contraindicado en cardiopatia isquemica, ACV, HTA no controlada, hemiplejica</b>.<br>"
    "3) AINE + triptan combinado si refractario.<br>"
    "<b>Profilaxis</b> si &gt;=4 ataques/mes o discapacitantes: propranolol, topiramato, amitriptilina, valproato; en mujer reproductiva precaucion con valproato/topiramato (teratogenicos)."
    '<span class="ecoe">ECOE: "Sumatriptan + AINE; profilaxis si frecuente."</span>',
    C5 + ["cefalea"])

add_qa(deck_c5,
    "Manejo: <b>Lumbalgia mecanica aguda sin red flags</b>",
    "1) <b>Educacion</b>: pronostico favorable (90% mejora en 4-6 sem); reposo prolongado contraproducente.<br>"
    "2) <b>Actividad regular</b> tolerable.<br>"
    "3) <b>AINE</b> (ibuprofeno 600 mg c/8 h por max 7-10 dias) + acetaminofen.<br>"
    "4) Relajante muscular corto (ciclobenzaprina 5-10 mg por noche x 5-7 dias) si espasmo.<br>"
    "5) <b>NO imagen rutinaria en las primeras 4-6 sem</b> si no red flags.<br>"
    "6) Fisioterapia y ejercicio si dolor persistente."
    '<span class="ecoe">ECOE: "AINE + actividad, sin imagen rutinaria."</span>',
    C5 + ["lumbalgia"])

add_qa(deck_c5,
    "Manejo: <b>Cetoacidosis diabetica (DKA)</b>",
    "1) <b>Hidratacion IV agresiva</b>: SS 0.9% 15-20 mL/kg en 1ra hora, luego segun deshidratacion y sodio.<br>"
    "2) <b>Insulina IV regular</b>: bolo 0.1 U/kg, luego infusion 0.1 U/kg/h (titular para bajar glucosa 50-75 mg/dL/h).<br>"
    "3) <b>Potasio</b>: agregar K si K serico &lt;5.3; suspender insulina si K &lt;3.3 hasta reponer.<br>"
    "4) Glucosa 5% cuando glucosa &lt;200 mg/dL (sigue insulina IV hasta cerrar anion gap).<br>"
    "5) Identificar y tratar precipitante (infeccion, omision insulina, IAM).<br>"
    "6) Transicion a insulina SC cuando AG cerrado y paciente tolere VO."
    '<span class="ecoe">ECOE: "Hidratacion + insulina IV + K, vigilar K horario."</span>',
    C5 + ["dm2", "dka"])

# Cronicos + Preventivo (16)
add_qa(deck_c5,
    "Manejo: <b>HTA estadio 1 (130-139/80-89)</b>",
    "<b>Sin enfermedad CV ni DM/ERC</b>: estilo de vida x 3-6 meses (dieta DASH, sal &lt;2.3 g/dia, ejercicio aerobico, perdida de peso, alcohol moderado, no tabaco).<br>"
    "<b>Con ASCVD, DM, ERC o riesgo ASCVD &gt;=10%</b>: iniciar farmaco + estilo de vida.<br>"
    "Reevaluar en 1-3 meses."
    '<span class="ecoe">ECOE: "Estilo de vida; farmaco si comorbilidad/alto riesgo."</span>',
    C5 + ["hta"])

add_qa(deck_c5,
    "Manejo: <b>HTA estadio 2 (&gt;=140/90)</b>",
    "<b>Iniciar 2 farmacos directamente</b> + estilo de vida.<br>"
    "Metas:<br>"
    "- <b>&lt;130/80</b> general (incluye DM y ERC sin proteinuria)<br>"
    "- &lt;140/90 frágiles, &gt;=65 anos con multiples comorbilidades<br>"
    "Reevaluar c/2-4 sem hasta alcanzar meta, luego c/3-6 meses."
    '<span class="ecoe">ECOE: "Dos farmacos de entrada; meta &lt;130/80."</span>',
    C5 + ["hta"])

add_qa(deck_c5,
    "Manejo: <b>Antihipertensivos de primera linea (ACC/AHA)</b>",
    "<b>1ra linea</b> (cualquiera segun perfil):<br>"
    "- <b>Tiazida</b> (HCTZ 25 mg, clortalidona 12.5-25 mg, indapamida)<br>"
    "- <b>CCB-DHP</b> (amlodipino 5-10 mg)<br>"
    "- <b>IECA</b> (lisinopril, enalapril) o <b>ARA-II</b> (losartan, telmisartan)<br>"
    "<b>Combinaciones recomendadas</b>: IECA/ARA + CCB, IECA/ARA + tiazida.<br>"
    "Afroamericanos sin DM/ERC: tiazida o CCB de inicio.<br>"
    "ERC con proteinuria: IECA o ARA-II obligado.<br>"
    "DM: IECA o ARA preferido si albuminuria."
    '<span class="ecoe">ECOE: "Selecciono segun comorbilidades."</span>',
    C5 + ["hta"])

add_qa(deck_c5,
    "Manejo: <b>Urgencia hipertensiva</b> (TA &gt;180/120 SIN dano organico agudo)",
    "<b>NO bajar agresivamente</b>; manejo VO ambulatorio.<br>"
    "Captopril 25 mg VO, clonidina 0.1-0.2 mg VO, o labetalol 200-400 mg VO.<br>"
    "Objetivo: bajar 25% en horas a dias.<br>"
    "Reanudar/iniciar farmacos cronicos y seguimiento estrecho."
    '<span class="ecoe">ECOE: "VO + observacion; no IV en urgencia."</span>',
    C5 + ["hta", "urgencia"])

add_qa(deck_c5,
    "Manejo: <b>Emergencia hipertensiva</b> (TA alta + dano organo agudo)",
    "<b>UCI + IV</b>: reducir 10-20% en 1ra hora, no mas de 25% en 24 h (excepto algunos casos como diseccion aortica que requieren bajar mas rapido).<br>"
    "Farmacos:<br>"
    "- <b>Nicardipino o clevidipino</b> (encefalopatia, EVC)<br>"
    "- <b>Nitroprusiato</b> (cuidado intoxicacion cianuro)<br>"
    "- <b>Labetalol o esmolol</b> (diseccion aortica - ANTES de vasodilatador)<br>"
    "- <b>Nitroglicerina IV</b> (SCA, edema pulmonar)<br>"
    "EVITAR nifedipino sublingual (caida brusca)."
    '<span class="ecoe">ECOE: "Ingreso UCI; bajar 10-20% en 1 h."</span>',
    C5 + ["hta", "emergencia"])

add_qa(deck_c5,
    "Manejo: <b>DM2 - inicio del tratamiento</b> (ADA 2025)",
    "<b>Estilo de vida + Metformina 500 mg/dia titular hasta 1000 mg c/12 h</b> (1ra linea independiente de HbA1c, salvo contraindicacion).<br>"
    "Si <b>HbA1c &gt;=9%</b>: considerar terapia combinada inicial.<br>"
    "Si <b>sintomatico o HbA1c &gt;10% o glucosa &gt;300</b>: insulina inicial.<br>"
    "<b>Si ASCVD/ICC/ERC -&gt; GLP-1 RA o SGLT2 INDEPENDIENTE de HbA1c</b> (efecto cardio/renoprotector).<br>"
    "Meta HbA1c &lt;7% (individualizar)."
    '<span class="ecoe">ECOE: "Metformina + estilo de vida; agregar SGLT2/GLP-1 si comorbilidad."</span>',
    C5 + ["dm2"])

add_qa(deck_c5,
    "Manejo: <b>DM2 con ASCVD establecida o riesgo alto</b>",
    "<b>GLP-1 RA con beneficio CV demostrado</b>: semaglutida (SC u oral), liraglutida, dulaglutida.<br>"
    "<b>O SGLT2i con beneficio CV demostrado</b>: empagliflozina, canagliflozina, dapagliflozina.<br>"
    "Estas se agregan a metformina (o solas si metformina contraindicada) <b>independiente de HbA1c</b>.<br>"
    "Estatina de alta intensidad. IECA/ARA si HTA o albuminuria. Aspirina solo en prevencion secundaria."
    '<span class="ecoe">ECOE: "Agrego GLP-1 o SGLT2 por su perfil CV."</span>',
    C5 + ["dm2"])

add_qa(deck_c5,
    "Manejo: <b>Hipoglucemia</b>",
    "<b>Consciente, capaz de tragar</b>: <b>15 g de carbohidratos rapidos VO</b> (4 cucharaditas azucar, 1/2 vaso jugo, 3 pastillas glucosa); revaluar en 15 min, repetir si glucosa &lt;70.<br>"
    "<b>Inconsciente / no puede tragar</b>: <b>glucagon 1 mg IM/SC</b> o <b>dextrosa 50% 25-50 mL IV</b>.<br>"
    "Una vez estable, alimento con carbohidratos complejos. Identificar causa (insulina, sulfonilurea, AKI, ayuno, alcohol)."
    '<span class="ecoe">ECOE: "Regla del 15: 15 g, 15 min, revisar."</span>',
    C5 + ["dm2", "hipoglucemia"])

add_qa(deck_c5,
    "Manejo: <b>Dislipidemia - prevencion secundaria</b> (ASCVD establecida)",
    "<b>Estatina de alta intensidad</b>: <b>atorvastatina 40-80 mg</b> o <b>rosuvastatina 20-40 mg</b>.<br>"
    "Meta: <b>LDL &lt;70 mg/dL</b> (o &lt;55 mg/dL si muy alto riesgo: ASCVD + factores adicionales).<br>"
    "Si no alcanza meta: agregar <b>ezetimibe 10 mg</b>; luego <b>iPCSK9</b> (alirocumab/evolocumab) o acido bempedoico."
    '<span class="ecoe">ECOE: "Atorva 80 + ezetimibe si LDL no en meta."</span>',
    C5 + ["dislipidemia"])

add_qa(deck_c5,
    "Manejo: <b>Dislipidemia - prevencion primaria</b>",
    "Calcular ASCVD a 10 anos:<br>"
    "- <b>&lt;5%</b>: estilo de vida<br>"
    "- <b>5-7.5% (borderline)</b>: estilo de vida; estatina si factores potenciadores (FH, LDL persistente &gt;160, sindrome metabolico, ERC, inflamatorio cronico, CAC &gt;0)<br>"
    "- <b>7.5-20%</b>: <b>estatina moderada intensidad</b> (atorva 10-20, rosu 5-10, simva 20-40, prava 40-80)<br>"
    "- <b>&gt;=20%</b>: <b>estatina de alta intensidad</b><br>"
    "Edad &lt;40 o &gt;75 individualizar; DM 40-75 anos: estatina moderada al menos."
    '<span class="ecoe">ECOE: "Riesgo X%, estatina de Y intensidad."</span>',
    C5 + ["dislipidemia"])

add_qa(deck_c5,
    "Manejo: <b>Anemia ferropenica</b>",
    "<b>Sulfato ferroso 325 mg (65 mg de hierro elemental) VO c/24-48 h</b> (mejor absorcion c/48 h) con <b>vitamina C/jugo citrico</b>; evitar te, lacteos, antiacidos 2 h antes/despues.<br>"
    "Continuar <b>3-6 meses despues de normalizar Hb</b> para reponer reservas.<br>"
    "Hierro IV (sacarosa, carboximaltosa) si intolerancia VO, malabsorcion, perdidas continuas grandes, ERC.<br>"
    "<b>SIEMPRE buscar la causa</b>: sangrado GI oculto, menorragia, dieta, malabsorcion. En &gt;50 anos o anemia inexplicable -&gt; <b>colonoscopia + endoscopia alta</b>."
    '<span class="ecoe">ECOE: "Sulfato ferroso + buscar causa con endoscopia."</span>',
    C5 + ["anemia"])

add_qa(deck_c5,
    "Manejo: <b>Anemia megaloblastica por deficit de B12</b>",
    "<b>Cianocobalamina 1000 mcg IM</b>: dia 1, 3, 7 y 14, luego mensual indefinido si causa permanente (anemia perniciosa, posgastrectomia).<br>"
    "Alternativa VO: cianocobalamina 1000-2000 mcg/dia (incluso en anemia perniciosa la VO funciona en muchos casos).<br>"
    "Corregir tambien folato si bajo, <b>pero NUNCA folato solo</b> sin descartar deficit B12 (puede empeorar neuropatia).<br>"
    "Buscar causa: anti-FI, anti-celulas parietales, dieta, gastritis atrofica, metformina cronica, alcohol."
    '<span class="ecoe">ECOE: "B12 IM esquema de carga + mantenimiento."</span>',
    C5 + ["anemia"])

add_qa(deck_c5,
    "Manejo: <b>Hipotiroidismo primario</b>",
    "<b>Levotiroxina 1.6 mcg/kg/dia</b> VO en ayuno (30-60 min antes de desayuno).<br>"
    "<b>Iniciar bajo en</b>: ancianos (25-50 mcg/dia), cardiopatas (12.5-25 mcg) y titular cada 6-8 sem.<br>"
    "Ajustar segun <b>TSH</b> (no T4):<br>"
    "- Meta general: TSH 0.5-2.5 (joven) o 1-4 (anciano)<br>"
    "- En embarazo: TSH &lt;2.5 con T4 libre normal-alto<br>"
    "Repetir TSH 6-8 sem post-ajuste."
    '<span class="ecoe">ECOE: "Levotiroxina dosis-peso; ajustar c/6-8 sem por TSH."</span>',
    C5 + ["tiroides"])

add_qa(deck_c5,
    "Manejo: <b>Cese de tabaquismo</b> (1ra linea)",
    "1) <b>Asesoria breve estructurada</b> (5 As: Ask, Advise, Assess, Assist, Arrange).<br>"
    "2) <b>Farmacos 1ra linea</b>:<br>"
    "- <b>Vareniclina 0.5-1 mg c/12 h</b> (mas eficaz, evitar si depresion severa/suicidio reciente)<br>"
    "- <b>Terapia de reemplazo nicotinico (TRN)</b> combinada (parche + chicle/spray)<br>"
    "- <b>Bupropion SR 150 mg c/12 h</b> (evitar si convulsion, BMI bajo)<br>"
    "Duracion 12 sem; soporte/consejeria conductual.<br>"
    "Tamizaje de Ca pulmon (TC baja dosis anual) en 50-80 anos con &gt;=20 paquetes-ano y fumador actual o que dejo &lt;15 anos."
    '<span class="ecoe">ECOE: "Asesoria 5As + vareniclina/TRN."</span>',
    C5 + ["preventivo", "tabaquismo"])

add_qa(deck_c5,
    "Manejo: <b>Tamizaje en consulta de adulto sano</b> (USPSTF resumen)",
    "<b>Todos los adultos</b>: TA anual; depresion/ansiedad anual; alcohol (AUDIT); IPV en mujeres en edad reproductiva; obesidad (IMC); tabaquismo.<br>"
    "<b>DM2</b>: 35-70 anos con sobrepeso, c/3 anos.<br>"
    "<b>Lipidos</b>: hombres &gt;=35, mujeres &gt;=45 con factores; tambien 40-75 para ASCVD score.<br>"
    "<b>Ca cervix</b>: Pap 21-29 c/3a; 30-65 Pap+VPH c/5a o Pap solo c/3a.<br>"
    "<b>Ca mama</b>: mamografia 40-74 c/2a (USPSTF 2024).<br>"
    "<b>Ca colon</b>: 45-75 (FIT anual, colonoscopia c/10a, etc.).<br>"
    "<b>AAA</b>: USG abdominal una vez en hombres 65-75 que fumaron alguna vez.<br>"
    "<b>Ca pulmon</b>: TC baja dosis anual en 50-80 con 20+ paquetes-ano, actual o quit &lt;15 anos.<br>"
    "<b>Osteoporosis</b>: DEXA en mujeres &gt;=65."
    '<span class="ecoe">ECOE: "Verbalizo tamizajes que aplican por edad/sexo/factores."</span>',
    C5 + ["preventivo"])

add_qa(deck_c5,
    "Manejo: <b>Profilaxis postexposicion VIH (PEP)</b>",
    "Iniciar <b>dentro de las 72 h</b> de la exposicion (idealmente &lt;2 h).<br>"
    "<b>Esquema preferido (CDC)</b>: <b>tenofovir/emtricitabina (TDF/FTC) + dolutegravir o raltegravir</b>, por <b>28 dias</b>.<br>"
    "Basal: VIH (idealmente prueba 4ta gen), VHB, VHC, embarazo, funcion renal, ITS.<br>"
    "Seguimiento: VIH a las 4-6 sem y 3 meses (4 meses si test 4ta gen).<br>"
    "Considerar PrEP a largo plazo si exposiciones recurrentes."
    '<span class="ecoe">ECOE: "Inicio TDF/FTC + DTG x 28 dias."</span>',
    C5 + ["preventivo", "vih"])


# ============================================================
# Build packages
# ============================================================
def build():
    decks = [
        (deck_c1, "Medicina_Familiar_Adulto_Capa1.apkg"),
        (deck_c2, "Medicina_Familiar_Adulto_Capa2.apkg"),
        (deck_c3, "Medicina_Familiar_Adulto_Capa3.apkg"),
        (deck_c4, "Medicina_Familiar_Adulto_Capa4.apkg"),
        (deck_c5, "Medicina_Familiar_Adulto_Capa5.apkg"),
    ]
    for d, fname in decks:
        pkg = genanki.Package(d)
        out = os.path.join(OUTPUT_DIR, fname)
        pkg.write_to_file(out)
        print(f"  -> {fname} ({len(d.notes)} notas)")

    combined = genanki.Package([deck_c1, deck_c2, deck_c3, deck_c4, deck_c5])
    combined_out = os.path.join(OUTPUT_DIR, "Medicina_Familiar_Adulto_TODOS.apkg")
    combined.write_to_file(combined_out)
    total = sum(len(d.notes) for d in [deck_c1, deck_c2, deck_c3, deck_c4, deck_c5])
    print(f"  -> Medicina_Familiar_Adulto_TODOS.apkg ({total} notas totales)")


if __name__ == "__main__":
    build()
