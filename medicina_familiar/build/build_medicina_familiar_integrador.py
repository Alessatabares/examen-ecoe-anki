"""Deck INTEGRADOR de Medicina Familiar (Adulto) - agrupadores y clasificaciones.

Reagrupa el contenido de la Capa 1 (Imagen Viva) en sentido inverso: de
"caso -> entidad" a "categoria paraguas -> entidades + el parametro que las
separa". Formato Q&A con tablas.

Generado con un workflow multi-agente (agrupacion por dominio de primer nivel +
verificacion adversarial contra GINA 2025, GOLD 2025, CURB-65/IDSA, Centor,
criterios de sinusitis bacteriana, ICHD-3, red flags de lumbalgia, ATA, USPSTF,
OMS, UpToDate). 1 tarjeta corregida (ferropenia inexplicada en adulto -> endoscopia
BIDIRECCIONAL gastroscopia + colonoscopia, no solo colonoscopia).

Deck: "Medicina Familiar Adulto::Integrador - Clasificaciones"
Fuente: medicina_familiar/build/build_medicina_familiar.py (Capa 1, 25 cloze)
"""
import os
import genanki

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "output")
os.makedirs(OUTPUT_DIR, exist_ok=True)

MODEL_QA_ID = 1607392320          # reusable (ids.json: qa_estandar)
DECK_ID = 1382947561              # nuevo, unico
DECK_NAME = "Medicina Familiar Adulto::Integrador - Clasificaciones"

CSS_BASE = """
.card {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  font-size: 19px; text-align: left; color: #1a1a1a;
  background-color: #fafafa; padding: 20px; line-height: 1.5;
}
#extra { margin-top: 16px; border: none; border-top: 1px solid #d4d4d4; padding-top: 12px; }
.ecoe { color: #b45309; font-style: italic; margin-top: 12px; display: block; }
.disc { color: #6d28d9; display: block; margin-top: 10px; font-weight: 600; }
.redflag { color: #b91c1c; font-weight: 600; display: block; margin-top: 8px; }
.q { font-weight: 600; color: #1d4ed8; }
table { border-collapse: collapse; width: 100%; margin-top: 8px; font-size: 15px; }
th, td { border: 1px solid #cbd5e1; padding: 5px 8px; text-align: left; vertical-align: top; }
th { background: #eef2ff; color: #111; }
td b { color: #b91c1c; }
"""

model_qa = genanki.Model(
    MODEL_QA_ID, "Estudio Medico QA",
    fields=[{"name": "Front"}, {"name": "Back"}],
    templates=[{"name": "QA", "qfmt": '<div class="q">{{Front}}</div>',
                "afmt": '<div class="q">{{Front}}</div><hr id="extra">{{Back}}'}],
    css=CSS_BASE,
)

deck = genanki.Deck(DECK_ID, DECK_NAME)
BASE_TAGS = ["medicina_familiar", "integrador", "ecoe"]

CARDS = CARDS = [
  {
    "front": "Tos y disnea: cómo distinguir neumonía, bronquitis aguda, asma (exacerbación) y EPOC",
    "back": "<table><tr><th>Entidad</th><th>Mecanismo</th><th>Auscultación / Rx</th><th>Obstrucción / reversibilidad</th></tr><tr><td><b>Neumonía</b></td><td>Alveolos con exudado purulento (falla intercambio gaseoso)</td><td>Crepitantes LOCALIZADOS; consolidación ('zona blanca') en Rx</td><td>No es el eje; severidad por CURB-65</td></tr><tr><td><b>Bronquitis aguda</b></td><td>Bronquios inflamados con moco; alveolos NO comprometidos; mayormente viral</td><td>Auscultación limpia, SIN crepitantes focales, sin consolidación</td><td>No</td></tr><tr><td><b>Asma (exacerbación)</b></td><td>Broncoespasmo + edema bronquial + moco espeso</td><td>Obstrucción difusa</td><td>Obstrucción REVERSIBLE (mejora post-broncodilatador)</td></tr><tr><td><b>EPOC</b></td><td>Destrucción alveolar (enfisema) + bronquitis crónica</td><td>Obstrucción difusa</td><td>Obstrucción NO reversible; factor #1 tabaquismo &gt;10 paquetes-año</td></tr></table><span class=\"disc\">Discriminador: consolidación focal + crepitantes localizados = neumonía; auscultación limpia sin Rx alterada = bronquitis; obstrucción que REVIERTE con broncodilatador = asma vs NO revierte = EPOC.</span><span class=\"ecoe\">ECOE: \"Tengo tos y me falta el aire; ¿mejoro cuando uso el inhalador?\"</span>",
    "tags": [
      "agrupador",
      "respiratorio"
    ]
  },
  {
    "front": "Cuadro febril respiratorio: cómo distinguir influenza del resfriado común (IVAS)",
    "back": "<table><tr><th>Entidad</th><th>Mecanismo</th><th>Síntomas clave</th><th>Estado funcional</th></tr><tr><td><b>Influenza</b></td><td>Virus + respuesta inmune sistémica intensa</td><td>Fiebre alta + mialgias + cefalea + postración</td><td>'Te tumba' (no puedes funcionar)</td></tr><tr><td><b>IVAS / resfriado común</b></td><td>Virus en mucosa nasal/faringe</td><td>Moco claro, sin compromiso sistémico severo</td><td>Sigues funcionando</td></tr></table><span class=\"disc\">Discriminador: el grado de compromiso sistémico (fiebre alta, mialgias, postración) y si el paciente queda incapacitado vs sigue su rutina.</span><span class=\"ecoe\">ECOE: \"De repente me dio fiebre y dolor en todo el cuerpo, no me puedo levantar.\"</span>",
    "tags": [
      "agrupador",
      "respiratorio"
    ]
  },
  {
    "front": "EPOC con hipoxia crónica: cómo se desarrolla el cor pulmonale (cascada fisiopatológica)",
    "back": "<table><tr><th>Paso</th><th>Mecanismo</th><th>Consecuencia</th></tr><tr><td><b>Hipoxia crónica (EPOC)</b></td><td>Hipoxemia mantenida por destrucción alveolar/bronquitis crónica</td><td>Estímulo vascular pulmonar</td></tr><tr><td><b>Vasoconstricción pulmonar hipóxica</b></td><td>Respuesta de los vasos pulmonares a la hipoxia</td><td>Aumento de resistencia pulmonar</td></tr><tr><td><b>Hipertensión pulmonar</b></td><td>Presión elevada en circuito pulmonar</td><td>Sobrecarga del ventrículo derecho</td></tr><tr><td><b>Cor pulmonale (falla del VD)</b></td><td>Claudicación del ventrículo derecho</td><td>Edema, ingurgitación yugular, hepatomegalia</td></tr></table><span class=\"disc\">Discriminador: signos de congestión DERECHA (edema, ingurgitación yugular, hepatomegalia) en un paciente con EPOC = cor pulmonale, no falla izquierda.</span><span class=\"redflag\">Red flag: edema + ingurgitación yugular + hepatomegalia en EPOC avanzado.</span><span class=\"ecoe\">ECOE: \"Soy EPOC y ahora se me hinchan las piernas y se me marcan las venas del cuello.\"</span>",
    "tags": [
      "agrupador",
      "respiratorio"
    ]
  },
  {
    "front": "Infección de vía aérea superior: cómo distinguir resfriado viral (IVAS) de sinusitis y de faringitis estreptocócica",
    "back": "<table><tr><th>Entidad</th><th>Síntoma clave</th><th>Tos/rinorrea</th><th>Criterio que confirma</th></tr><tr><td><b>IVAS viral (resfriado)</b></td><td>Moco claro abundante, sin compromiso sistémico severo</td><td>Presentes (típicas)</td><td>Autolimitado, sigue funcionando</td></tr><tr><td><b>Sinusitis</b></td><td>Dolor facial + presión + rinorrea purulenta</td><td>Rinorrea purulenta</td><td>BACTERIANA si síntomas &gt;10 días o doble empeoramiento</td></tr><tr><td><b>Faringitis estreptocócica</b></td><td>Exudado faríngeo + fiebre + adenopatía cervical</td><td>AUSENCIA de tos/rinorrea</td><td>Criterios de Centor (tos/rinorrea presentes = viral)</td></tr></table><span class=\"disc\">Discriminador: rinorrea/moco claro + sin fiebre alta = viral; rinorrea purulenta + dolor facial + &gt;10 días = sinusitis bacteriana; exudado + fiebre + adenopatía SIN tos ni rinorrea = estreptocócica.</span><span class=\"redflag\">Tratar faringitis por S. pyogenes para prevenir fiebre reumática.</span><span class=\"ecoe\">ECOE: \"Paciente con odinofagia, fiebre y ganglios cervicales dolorosos, sin tos ni mocos: pienso en faringitis estreptocócica (Centor) y la trato.\"</span>",
    "tags": [
      "agrupador",
      "orl"
    ]
  },
  {
    "front": "Dolor de oído (otalgia): cómo distinguir otitis media aguda de otitis externa",
    "back": "<table><tr><th>Entidad</th><th>Mecanismo</th><th>Localización del dolor</th><th>Signo discriminador</th></tr><tr><td><b>Otitis media aguda</b></td><td>Disfunción de trompa de Eustaquio &rarr; líquido en oído medio</td><td>Dolor INTERNO (profundo)</td><td>Sin dolor al manipular el pabellón</td></tr><tr><td><b>Otitis externa</b></td><td>Inflamación de la piel del conducto auditivo externo (humedad/maceración); Pseudomonas/S. aureus</td><td>Dolor en el conducto/pabellón</td><td>Dolor al MANIPULAR el pabellón (signo del trago)</td></tr></table><span class=\"disc\">Discriminador: dolor al traccionar el pabellón o presionar el trago = otitis EXTERNA; oído tapado con dolor interno tras IVAS = otitis MEDIA.</span><span class=\"ecoe\">ECOE: \"Le tiro suavemente de la oreja: si le duele, es otitis externa; si no, sospecho otitis media.\"</span>",
    "tags": [
      "agrupador",
      "orl"
    ]
  },
  {
    "front": "Síntomas urinarios bajos vs fiebre/dolor lumbar vs dolor que irradia a ingle: cómo distinguir cistitis, pielonefritis y cólico renal",
    "back": "<table><tr><th>Entidad</th><th>Mecanismo</th><th>Fiebre / sistémico</th><th>Síntoma clave discriminador</th></tr><tr><td><b>Cistitis (ITU baja)</b></td><td>Bacteria asciende uretra a vejiga</td><td>NO (no llega al riñón)</td><td>Disuria + frecuencia + urgencia</td></tr><tr><td><b>Pielonefritis (ITU alta)</b></td><td>Infección asciende por uréter al riñón</td><td>SÍ (fiebre + síntomas sistémicos)</td><td>Dolor lumbar / puñopercusión positiva</td></tr><tr><td><b>Cólico renal</b></td><td>Cálculo obstruye el uréter</td><td>NO suele haber fiebre</td><td>Dolor cólico que irradia de flanco a ingle; paciente INQUIETO</td></tr></table><span class=\"disc\">Discriminador: SIN fiebre + síntomas miccionales = cistitis; CON fiebre + dolor lumbar = pielonefritis; dolor irradiado a ingle con paciente que no halla postura = cólico renal (el inquieto vs el quieto del abdomen quirúrgico).</span><span class=\"redflag\">Red flag: embarazada con bacteriuria SÍ se trata (riesgo de pielonefritis y parto pretérmino).</span><span class=\"ecoe\">ECOE: \"Mujer con disuria y febrícula, ¿cuándo sospechas que la infección subió al riñón?\"</span>",
    "tags": [
      "agrupador",
      "urinario"
    ]
  },
  {
    "front": "Dolor abdominal con diarrea vs dolor que migra a fosa iliaca derecha: cómo distinguir gastroenteritis aguda de apendicitis",
    "back": "<table><tr><th>Entidad</th><th>Mecanismo</th><th>Patrón del dolor</th><th>Síntomas acompañantes</th></tr><tr><td><b>Gastroenteritis aguda</b></td><td>Inflamación intestinal viral o bacteriana</td><td>Dolor cólico difuso</td><td>Diarrea + vómito</td></tr><tr><td><b>Apendicitis</b></td><td>Obstrucción de la luz apendicular (fecalito, hiperplasia linfoide)</td><td>Dolor periumbilical que MIGRA a FID en 12-24 h</td><td>Anorexia (sin diarrea predominante)</td></tr></table><span class=\"disc\">Discriminador: diarrea + vómito con cólico difuso = gastroenteritis; dolor que MIGRA del ombligo a fosa iliaca derecha + anorexia = apendicitis.</span><span class=\"redflag\">Red flag GEA: sangre en heces, fiebre alta, deshidratación severa, inmunocompromiso. Red flag apendicitis: fiebre + signos peritoneales &rarr; quirúrgico urgente.</span><span class=\"ecoe\">ECOE: \"Paciente con dolor que empezó cerca del ombligo y ahora está en la FID con falta de apetito, ¿diagnóstico y conducta?\"</span>",
    "tags": [
      "agrupador",
      "abdominal"
    ]
  },
  {
    "front": "Cefalea primaria: cómo distinguir cefalea tensional de migraña (y cuándo pensar en cefalea secundaria)",
    "back": "<table><tr><th>Entidad</th><th>Mecanismo</th><th>Tipo/localización del dolor</th><th>Síntomas acompañantes</th><th>Conducta del paciente</th></tr><tr><td><b>Cefalea tensional</b></td><td>Contracción sostenida de músculos pericraneales (estrés/postura)</td><td>Opresivo, bilateral, 'en banda'</td><td>SIN náuseas ni fotofobia</td><td>Sigue funcionando</td></tr><tr><td><b>Migraña</b></td><td>Activación trigémino-vascular + neuroinflamación</td><td>Pulsátil, hemicraneal</td><td>Náuseas + fotofobia + fonofobia; puede haber aura visual</td><td>Busca cuarto oscuro</td></tr><tr><td><b>Cefalea secundaria (urgencia)</b></td><td>Causa estructural/infecciosa subyacente</td><td>'La peor de mi vida' / en trueno</td><td>Fiebre y/o foco neurológico</td><td>Requiere estudio urgente</td></tr></table><span class=\"disc\">Discriminador: la presencia de náuseas/fotofobia + dolor pulsátil hemicraneal define migraña frente al dolor opresivo bilateral SIN cortejo de la tensional; criterios ICHD-3.</span><span class=\"redflag\">Red flags de cefalea secundaria: cefalea 'en trueno' o 'la peor de mi vida', con fiebre, o con foco neurológico.</span><span class=\"ecoe\">ECOE: \"Mujer con dolor pulsátil en la mitad de la cabeza, con náuseas y molestia a la luz, que se mete en un cuarto oscuro\" -> migraña.</span>",
    "tags": [
      "agrupador",
      "dolor",
      "cefalea",
      "neuro"
    ]
  },
  {
    "front": "Lumbalgia: cómo distinguir la lumbalgia mecánica benigna de una lumbalgia con red flags (potencialmente grave)",
    "back": "<table><tr><th>Entidad</th><th>Mecanismo</th><th>Relación con movimiento/reposo</th><th>Síntomas neurológicos/sistémicos</th><th>Conducta</th></tr><tr><td><b>Lumbalgia mecánica</b></td><td>Tensión/esguince de músculos y ligamentos paravertebrales</td><td>Empeora con el movimiento, mejora con el reposo</td><td>SIN síntomas radiculares ni sistémicos</td><td>Manejo conservador</td></tr><tr><td><b>Lumbalgia con red flags</b></td><td>Causa secundaria (infección, tumor, fractura, compresión)</td><td>Puede ser de reposo/nocturna; no clásica mecánica</td><td>Déficit motor, anestesia en silla de montar, retención urinaria, fiebre, pérdida de peso</td><td>Estudio dirigido urgente</td></tr></table><span class=\"disc\">Discriminador: la lumbalgia mecánica es dolor que empeora al moverse y mejora en reposo SIN clínica radicular ni sistémica; cualquier red flag obliga a descartar causa secundaria.</span><span class=\"redflag\">Red flags de lumbalgia: trauma, fiebre, pérdida de peso, déficit motor, anestesia en silla de montar, retención urinaria, edad &lt;20 o &gt;50 años.</span><span class=\"ecoe\">ECOE: \"Paciente con lumbalgia y anestesia en silla de montar + retención urinaria\" -> sospecha de síndrome de cola de caballo, urgencia.</span>",
    "tags": [
      "agrupador",
      "dolor",
      "lumbalgia",
      "musculoesqueletico"
    ]
  },
  {
    "front": "Tiroides: cómo distinguir hipotiroidismo de hipertiroidismo (y reconocer la tormenta tiroidea)",
    "back": "<table><tr><th>Entidad</th><th>Causa #1</th><th>Metabolismo</th><th>Clínica clave</th><th>TSH / T4L</th></tr><tr><td><b>Hipotiroidismo</b></td><td>Hashimoto</td><td>Enlentecido</td><td>Fatiga, intolerancia al frío, ganancia de peso, bradicardia, piel seca, depresión</td><td>TSH alta / T4L baja</td></tr><tr><td><b>Hipertiroidismo</b></td><td>Graves</td><td>Acelerado</td><td>Taquicardia, pérdida de peso, calor, sudoración, ansiedad, temblor; exoftalmos en Graves</td><td>TSH baja / T4L alta</td></tr></table><span class=\"disc\">Discriminador: la TSH se mueve en sentido OPUESTO a la clínica: TSH alta &gt; metabolismo lento (hipo); TSH baja &gt; metabolismo acelerado (hiper). El exoftalmos es propio de Graves.</span><span class=\"redflag\">Red flag: tormenta tiroidea = fiebre + taquicardia extrema + delirio = urgencia.</span><span class=\"ecoe\">ECOE: \"Mujer con fatiga, aumento de peso e intolerancia al frío; TSH alta y T4L baja: hipotiroidismo por Hashimoto.\"</span>",
    "tags": [
      "agrupador",
      "tiroides",
      "endocrino",
      "cronicos"
    ]
  },
  {
    "front": "Crónicos vasculares: cómo distinguir HTA, DM2 y dislipidemia por su mecanismo y daño de órgano",
    "back": "<table><tr><th>Entidad</th><th>Mecanismo</th><th>Daño / complicación</th><th>Pista discriminadora</th></tr><tr><td><b>HTA</b></td><td>Presión elevada crónica &gt; daño endotelial y remodelación vascular</td><td>Órgano blanco: corazón, riñón, retina, cerebro</td><td>Presión arterial elevada crónica</td></tr><tr><td><b>DM2</b></td><td>Resistencia a la insulina + declive de células beta &gt; hiperglucemia crónica</td><td>Micro (retino, nefro, neuropatía) y macro (IAM, EVC, EAP)</td><td>Hiperglucemia crónica</td></tr><tr><td><b>Dislipidemia</b></td><td>LDL alta entra a la pared arterial &gt; oxidación &gt; placa ateromatosa</td><td>Ruptura de placa y trombosis (IAM, EVC)</td><td>LDL elevada / ateroma</td></tr></table><span class=\"disc\">Discriminador: el parámetro alterado define la entidad: presión (HTA), glucosa (DM2), LDL (dislipidemia); los tres convergen en daño vascular y eventos cardiovasculares.</span><span class=\"redflag\">Red flag: crisis hipertensiva + daño agudo de órgano blanco = emergencia hipertensiva.</span><span class=\"ecoe\">ECOE: \"Paciente con cifras tensionales altas y retinopatía: HTA con daño de órgano blanco.\"</span>",
    "tags": [
      "agrupador",
      "cronicos",
      "cardiovascular",
      "metabolico"
    ]
  },
  {
    "front": "Crónicos que se ven en biometría: anemia ferropénica frente a las alteraciones tiroideas y el porqué de la colonoscopia",
    "back": "<table><tr><th>Entidad</th><th>Causa / mecanismo</th><th>Hallazgo de laboratorio</th><th>Conducta clave</th></tr><tr><td><b>Anemia ferropénica</b></td><td>Hierro insuficiente (pérdida crónica, dieta, malabsorción)</td><td>Eritrocitos microcíticos hipocrómicos</td><td>Adulto con ferropenia sin causa clara &gt; endoscopia bidireccional (gastroscopia + colonoscopia) para descartar neoplasia digestiva, sobre todo Ca de colon</td></tr><tr><td><b>Hipotiroidismo</b></td><td>Déficit de hormona tiroidea (Hashimoto)</td><td>TSH alta, T4L baja</td><td>Sustitución hormonal</td></tr></table><span class=\"disc\">Discriminador: la anemia ferropénica da microcitosis e hipocromía; ante ferropenia inexplicada en varón o mujer posmenopáusica el siguiente paso es la endoscopia bidireccional (gastroscopia + colonoscopia), siendo la colonoscopia clave para descartar cáncer de colon.</span><span class=\"redflag\">Red flag: ferropenia sin causa aparente en adulto = sangrado digestivo / neoplasia hasta demostrar lo contrario.</span><span class=\"ecoe\">ECOE: \"Adulto cansado con anemia microcítica hipocrómica y ferritina baja sin causa clara: solicitar endoscopia bidireccional (gastroscopia + colonoscopia).\"</span>",
    "tags": [
      "agrupador",
      "cronicos",
      "hematologia",
      "tiroides"
    ]
  }
]

for c in CARDS:
    deck.add_note(genanki.Note(model=model_qa, fields=[c["front"], c["back"]],
                               tags=BASE_TAGS + c["tags"]))

out = os.path.join(OUTPUT_DIR, "Medicina_Familiar_Adulto_Integrador.apkg")
genanki.Package([deck]).write_to_file(out)
print(f"OK -> {out}")
print(f"TOTAL notas: {len(deck.notes)}")
