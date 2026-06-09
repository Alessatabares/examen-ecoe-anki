"""FINAL - Bloques ECOE (memorizar en horas, asociativo).

10 bloques de alto rendimiento comprimidos por CONVERGENCIA:
  - una sola "llave" de interrogatorio/manejo se reutiliza en muchos Dx
  - tablas discriminador -> Dx (memorizas el patron, no 80 ensayos)
  - cada entidad lleva su gatillo-de-quirofano, su dosis y su 🗣️ ECOE

Bloques:
  1 Abdomen agudo + ATLS/trauma
  2 Nutricion en embarazo (guia alimentaria)
  3 PRONAM primeros 1000 dias (prenatal/puerperio/RN/tamices)
  4 Cancer de mama
  5 Infecciones respiratorias adulto
  6 Pediatria (respiratorio/exantema/convulsion/diarrea)
  7 DM2 y sindrome metabolico
  8 Sobrepeso y obesidad
  9 Hipertension arterial
  10 Vacunacion a lo largo de la vida

Sin acentos (convencion del repo). Dosis/metas son orientativas: verifica
alergias, embarazo, funcion renal, resistencias locales y guia vigente de tu sede.
"""
import os
import genanki

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "output")
os.makedirs(OUTPUT_DIR, exist_ok=True)

MODEL_ID = 1990010001  # reusa "NHT Matriz" (Front/Back)

CSS_BASE = """
.card { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  font-size: 18px; text-align: left; color: #1a1a1a; background-color: #fafafa;
  padding: 18px; line-height: 1.5; }
.caso { font-size: 21px; font-weight: 800; color: #1e3a8a; display:block; }
.eje { font-size:12px; font-weight:800; letter-spacing:.8px; text-transform:uppercase; color:#64748b; display:block;}
.prompt { display:block; margin-top:6px; color:#b45309; font-style:italic; }
#extra { margin-top: 14px; border: none; border-top: 1px solid #d4d4d4; padding-top: 10px; }
.b { display: block; margin: 9px 0; padding: 9px 12px; border-radius: 8px; }
.l { display: block; font-size: 12px; font-weight: 800; letter-spacing: .6px;
  text-transform: uppercase; margin-bottom: 4px; }
.itg { background:#eef2ff; border-left:4px solid #1e3a8a; } .itg .l{color:#1e3a8a;}
.ddx { background:#f5f3ff; border-left:4px solid #6d28d9; } .ddx .l{color:#6d28d9;}
.exp { background:#fff7ed; border-left:4px solid #c2410c; } .exp .l{color:#c2410c;}
.est { background:#f1f5f9; border-left:4px solid #334155; } .est .l{color:#334155;}
.mng { background:#ecfdf5; border-left:4px solid #047857; } .mng .l{color:#047857;}
.rec { background:#fffbeb; border-left:4px solid #b45309; } .rec .l{color:#b45309;}
.com { background:#fdf2f8; border-left:4px solid #be185d; } .com .l{color:#be185d;}
.alr { background:#fef2f2; border-left:4px solid #b91c1c; } .alr .l{color:#b91c1c;}
b { color: #111; } .v { color:#b45309; font-style:italic; } u { text-decoration-color:#6d28d9; }
table.k { border-collapse:collapse; width:100%; font-size:15px; margin-top:4px;}
table.k td { border:1px solid #cbd5e1; padding:3px 6px; vertical-align:top;}
table.k td:first-child{ font-weight:700; white-space:nowrap; background:#fff;}
"""

model = genanki.Model(
    MODEL_ID, "NHT Matriz",
    fields=[{"name": "Front"}, {"name": "Back"}],
    templates=[{"name": "Caso", "qfmt": "{{Front}}", "afmt": '{{Front}}<hr id="extra">{{Back}}'}],
    css=CSS_BASE)

BASE_TAGS = ["no_hay_tiempo", "ecoe", "final", "bloques"]


def B(clase, label, html):
    return f'<span class="b {clase}"><span class="l">{label}</span>{html}</span>'


def kt(rows):
    body = "".join(f"<tr><td>{a}</td><td>{b}</td></tr>" for a, b in rows)
    return f'<table class="k">{body}</table>'


def mk(deck, eje):
    def card(titulo, prompt, back, tags):
        front = (f'<span class="eje">{eje}</span><span class="caso">{titulo}</span>'
                 f'<span class="prompt">{prompt}</span>')
        deck.add_note(genanki.Note(model=model, fields=[front, back], tags=BASE_TAGS + tags))
    return card


decks = []

# ==========================================================================
# BLOQUE 1 - ABDOMEN AGUDO + ATLS
# ==========================================================================
d1 = genanki.Deck(1990009601, "No hay tiempo::FINAL Bloques::1 - Abdomen agudo + ATLS")
decks.append(d1)
c = mk(d1, "Bloque 1 - Abdomen agudo / ATLS")

c("LLAVE - Interrogatorio de TODO abdomen agudo",
  'Cualquier dolor abdominal. "Una sola bateria; la respuesta te tira al Dx."',
  B("itg", "7 ejes (memoriza el esqueleto)", kt([
    ("Dolor", "subito/progresivo, localizacion, irradiacion/migracion, colico vs constante, relacion con comida, que mejora/empeora"),
    ("GI", "nausea, vomito, transito, gases, diarrea, sangre/melena"),
    ("Sistemico", "fiebre, escalofrios, perdida de peso"),
    ("Urinario", "disuria, hematuria, dolor lumbar"),
    ("Gine", "FUM, embarazo, sangrado, flujo, dolor pelvico"),
    ("Riesgo", "cx previas, hernias, OH, AINE, anticoag, FA, HTA, DM, litos"),
    ("Gravedad", "mareo, sincope, confusion, oliguria, disnea")])) +
  B("alr", "Regla madre", "Toda mujer fertil con dolor abdominal = <b>β-hCG</b>. Subito y maximo desde el inicio = vascular hasta probar lo contrario."),
  ["interrogatorio", "abdomen_agudo"])

c("LLAVE - Bucket de MANEJO del abdomen agudo quirurgico",
  'Abdomen agudo quirurgico. "Mismo esqueleto; solo cambia el antibiotico y el destino."',
  B("mng", "Esqueleto compartido", "<b>NPO</b> + <b>Hartmann 1 L IV</b> (30 mL/kg si sepsis/hipotension) + analgesia + <b>ATB</b> + <b>cirugia/CPRE</b>.") +
  B("est", "Switch del antibiotico", kt([
    ("Apendicitis / colecistitis / diverticulitis hosp", "ceftriaxona 1-2 g c/24 + metronidazol 500 mg c/8"),
    ("Foco grave o alto (colangitis, perforacion/peritonitis, isquemia mesenterica)", "piperacilina-tazobactam 4.5 g c/6-8"),
    ("Pancreatitis", "NO ATB de rutina (solo si colangitis/necrosis infectada)")])) +
  B("alr", "Gatillos de quirofano", "Abdomen en tabla / peritonitis difusa / inestable + FAST+ / AAA con hipotension = <b>quirofano sin esperar imagen</b>."),
  ["manejo", "abdomen_agudo", "antibiotico"])

c("CONVERGENCIA - Localizacion del dolor -> Dx",
  'Te dan la localizacion. "El cuadrante jerarquiza el diferencial."',
  B("ddx", "Cuadrante -> sospecha", kt([
    ("FID", "apendicitis; en mujer fertil: ectopico / torsion"),
    ("HCD >6 h + fiebre", "colecistitis (Murphy); +ictericia = colangitis"),
    ("Epigastrio -> espalda, mejora inclinado", "pancreatitis"),
    ("FII adulto mayor + fiebre", "diverticulitis"),
    ("Difuso subito + tabla", "perforacion / peritonitis"),
    ("Desproporcionado a la EF, FA sin ACO", "isquemia mesenterica"),
    ("Lumbar/abdominal + masa pulsatil + hipoTA", "AAA roto"),
    ("Pelvico unilateral subito, mujer", "torsion ovarica / ectopico")])),
  ["diferencial", "localizacion"])

c("Apendicitis aguda",
  'Joven, dolor periumbilical que migra a FID, anorexia, nausea, fiebre.',
  B("exp", "Signos", "McBurney, <b>Rovsing</b>, psoas, obturador, rebote/defensa.") +
  B("est", "Estudios", "BH, QS/EGO, <b>β-hCG en mujer fertil</b>, USG/TAC segun caso.") +
  B("mng", "Manejo", "Bucket quirurgico + ceftriaxona + metronidazol + <b>apendicectomia laparoscopica</b>.") +
  B("alr", "Alarma", "Perforacion, peritonitis, fiebre alta, choque."),
  ["apendicitis"])

c("CONVERGENCIA - Triada biliar: colecistitis / colangitis / pancreatitis",
  'Dolor en hipocondrio/epigastrio. "Lo que las separa: ictericia y lipasa."',
  B("ddx", "Discriminador -> Dx", kt([
    ("Murphy+, HCD >6 h, SIN ictericia marcada", "colecistitis -> colecistectomia &lt;72 h"),
    ("Charcot: fiebre + HCD + ICTERICIA", "colangitis (coledocolitiasis)"),
    ("Reynolds: Charcot + confusion + hipoTA", "colangitis grave -> pip-tazo + <b>CPRE urgente</b>"),
    ("Epigastrio -> espalda, mejora inclinado, lipasa >3x", "pancreatitis")])) +
  B("est", "Patron colestasico (colangitis)", "BD, FA, GGT altas; hemocultivos x2; lactato.") +
  B("alr", "Cierre", "Colecistitis con ictericia/confusion/hipoTA = piensa colangitis."),
  ["biliar", "colecistitis", "colangitis", "pancreatitis"])

c("Pancreatitis aguda",
  'Epigastrio intenso en barra a espalda, vomito, mejora inclinado, OH/litos/TG.',
  B("est", "Estudios", "<b>Lipasa >3x</b>, BH, QS/BUN/Cr, PFH, USG hepatobiliar, TG, calcio; gas/lactato si grave.") +
  B("mng", "Manejo", "Hospitalizar, NPO inicial + Hartmann, morfina 2-4 mg IV lenta, ondansetron, reinicio VO temprano. <b>NO ATB de rutina</b>.") +
  B("alr", "ATB solo si", "Colangitis, necrosis infectada o infeccion documentada. Alarma: disnea, oliguria, hipoTA."),
  ["pancreatitis"])

c("Diverticulitis aguda",
  'Adulto mayor, dolor FII, fiebre, estreñimiento, episodios previos.',
  B("est", "Estudio", "BH, QS/Cr, EGO; <b>TAC con contraste</b> si dudoso/complicacion.") +
  B("mng", "Manejo por gravedad", kt([
    ("Leve", "dieta liquida/blanda + paracetamol + hidratacion, control 48-72 h"),
    ("Ambulatorio c/ATB", "amoxiclav 875/125 c/12 x 7-10 d"),
    ("Hospital", "ceftriaxona + metronidazol"),
    ("Absceso >3-4 cm", "drenaje; peritonitis = cirugia")])),
  ["diverticulitis"])

c("Perforacion / peritonitis",
  'Dolor subito intenso, abdomen en tabla, rebote difuso, fiebre/taquicardia.',
  B("exp", "EF", "Defensa involuntaria, rigidez, rebote difuso, ruidos disminuidos, choque.") +
  B("est", "Imagen", "<b>Rx de pie: aire libre</b>; TAC si estable; lactato, grupo/Rh.") +
  B("mng", "Manejo", "NPO, 2 vias, Hartmann, SNG, Foley, morfina, <b>pip-tazo 4.5 g c/6-8</b>, cirugia urgente (control foco/lavado).") +
  B("alr", "Regla", "Abdomen en tabla = quirofano."),
  ["perforacion", "peritonitis"])

c("Isquemia mesenterica aguda",
  'Adulto mayor con FA sin anticoagular, dolor 10/10 desproporcionado, sangre al tacto.',
  B("exp", "Pista", "Abdomen <b>relativamente blando</b> con dolor intenso, pulso irregularmente irregular.") +
  B("est", "Estudio", "<b>Angio-TAC</b>, BH, QS, gas/<b>lactato</b>, coagulacion, ECG.") +
  B("mng", "Manejo", "NPO, Hartmann, analgesia, <b>heparina no fraccionada IV</b>, pip-tazo, revascularizacion; laparotomia si peritonitis/inestable.") +
  B("alr", "Alarma", "Lactato alto, acidosis, peritonitis, hipoTA."),
  ["isquemia_mesenterica"])

c("AAA roto",
  'Hombre >65, HTA/fumador, dolor abdominal-lumbar subito, hipoTA, masa pulsatil.',
  B("est", "Imagen", "<b>Inestable: NO TAC.</b> Estable: angio-TAC.") +
  B("mng", "Manejo", "ABC, 2 vias, pruebas cruzadas, sangre, <b>reanimacion hipotensiva PAS 70-90</b>, cirugia vascular/EVAR inmediata.") +
  B("alr", "Regla", "Dolor lumbar + hipotension = quirofano."),
  ["aaa"])

c("CONVERGENCIA gine - Ectopico vs torsion ovarica",
  'Mujer fertil, dolor pelvico unilateral. "Ambos: β-hCG + USG TV."',
  B("ddx", "Discriminador", kt([
    ("FUM ~7 sem, sangrado escaso, mareo, EIP previa", "embarazo ectopico"),
    ("Dolor subito + nausea/vomito + masa anexial/quiste", "torsion ovarica")])) +
  B("mng", "Manejo", kt([
    ("Ectopico estable", "MTX si hCG &lt;5000, masa &lt;3.5-4 cm, sin latido/ruptura, funcion renal-hepatica ok"),
    ("Ectopico inestable", "cirugia urgente; Rh- = anti-D"),
    ("Torsion", "laparoscopia + detorsion; Doppler normal NO descarta")])),
  ["ectopico", "torsion_ovarica"])

c("ATLS torax - Neumotorax tension / Hemotorax masivo / Taponamiento",
  'Trauma + hipotension. "El examen del torax decide; Dx clinico, no esperes Rx."',
  B("ddx", "Hallazgo -> Dx -> accion", kt([
    ("Hiperresonancia, ausencia murmullo, IY, desvia traquea (tardio)", "NEUMOTORAX TENSION -> descompresion con aguja 2EIC LMC o 4-5EIC LAA + tubo"),
    ("Matidez + murmullo disminuido + shock", "HEMOTORAX MASIVO -> tubo 28-36 Fr; toracotomia si >1500 mL o >200 mL/h"),
    ("Triada Beck (hipoTA, IY, ruidos velados) + trauma penetrante", "TAPONAMIENTO -> FAST, pericardiocentesis puente / toracotomia")])) +
  B("alr", "Comun", "Los tres son <b>choque obstructivo</b>; no retrases por imagen."),
  ["atls", "neumotorax", "hemotorax", "taponamiento"])

c("ATLS - Choque hemorragico + trauma abdominal",
  'Trauma con taquicardia, hipoTA, piel fria, confusion, oliguria.',
  B("mng", "Choque hemorragico", "O2, 2 vias 14-16G, control sangrado, cristaloide tibio 500-1000 mL <b>solo puente</b>, <b>transfusion 1:1:1</b>, <b>TXA 1 g en 10 min + 1 g/8 h si trauma &lt;3 h</b>.") +
  B("est", "Penetrante vs cerrado", kt([
    ("Penetrante", "NO retirar objeto; cubrir evisceracion con gasa esteril humeda; ATB amplio + tetanos"),
    ("Cerrado", "FAST; inestable + FAST+ = laparotomia; estable = TAC")])) +
  B("alr", "Regla", "Hipotension + FAST+ = quirofano. No solo cristaloides."),
  ["choque_hemorragico", "trauma_abdominal"])

c("FRASE universal ECOE de cierre",
  'Para cerrar cualquier urgencia ante el sinodal.',
  B("com", "🗣️ ECOE", '"Mi prioridad es estabilizar al paciente, identificar diagnosticos que amenazan la vida, iniciar manejo inicial y referir de forma urgente al servicio correspondiente <b>sin retrasar tratamiento por estudios innecesarios</b>."'),
  ["verbalizacion", "frase"])

# ==========================================================================
# BLOQUE 2 - NUTRICION EN EMBARAZO
# ==========================================================================
d2 = genanki.Deck(1990009602, "No hay tiempo::FINAL Bloques::2 - Nutricion en embarazo")
decks.append(d2)
c = mk(d2, "Bloque 2 - Nutricion en embarazo")

c("LLAVE - Suplementacion y metas de hidratacion",
  'Toda embarazada. "Lo que SIEMPRE indicas, mas las metas duras."',
  B("mng", "Base", kt([
    ("Acido folico", "400 mcg c/24 (4 mg si alto riesgo de defecto del tubo neural)"),
    ("Hierro elemental", "≥27 mg/d prenatal; anemia: sulfato ferroso 60-120 mg Fe elemental/d"),
    ("Agua simple", "9 vasos embarazo / 10 vasos lactancia"),
    ("Hierro vegetal", "+ vitamina C (limon/naranja/jitomate); separado de cafe/te/lacteos")])) +
  B("alr", "Cero absoluto", "Alcohol: no hay nivel seguro (muerte fetal, discapacidad permanente)."),
  ["suplementos", "embarazo"])

c("Anemia ferropenica en embarazo",
  '20 SDG, cansancio, palidez, mareo; come poco hierro.',
  B("ddx", "Diferenciales", "Ferropenica (mas probable) > deficit folato/B12 > fatiga fisiologica > hipotiroidismo/depresion > sangrado obstetrico.") +
  B("est", "Estudios", "BH (VCM), ferritina/perfil de hierro, EGO; glucosa/tamiz segun semana.") +
  B("mng", "Manejo", "Hierro diario (carne/pollo/higado) + vit C; <b>sulfato ferroso 60-120 mg Fe/d</b>; control 2-4 sem.") +
  B("alr", "Alarma", "Sincope, disnea en reposo, palpitaciones, sangrado, ↓movimientos fetales."),
  ["anemia"])

c("Bajo consumo de verduras/frutas y exceso de jugos",
  '16 SDG, "no llenan", prefiere jugos naturales.',
  B("mng", "Meta", "Verduras y frutas en cada comida, <b>≥400 g/d</b> priorizando verduras; <b>fruta entera, no jugo</b> (concentra azucar, menos saciedad/fibra).") +
  B("alr", "Vigila", "Ganancia excesiva de peso y estreñimiento por falta de fibra."),
  ["micronutrientes"])

c("Estreñimiento y flatulencia por baja fibra",
  '24 SDG, estreñimiento, distension, evita frijoles "porque inflaman".',
  B("mng", "Manejo", "Leguminosas <b>2-3 porciones/d</b> progresivas (remojar, tirar agua, cocer bien = menos gases) + agua + movimiento; combinar con cereal + vit C.") +
  B("est", "Farmaco", "Primero fibra + agua; si persiste <b>psyllium 3.5 g c/24</b> con abundante agua.") +
  B("alr", "Descartar", "Obstruccion si dolor intenso + vomito + no canaliza gases."),
  ["estrenimiento"])

c("Dieta de refinados / ultraprocesados",
  'Base en pan dulce, arroz blanco, cereal de caja, papitas, sopas instantaneas.',
  B("mng", "Sustituir, no prohibir", kt([
    ("Refinados", "tortilla de maiz, avena, arroz integral, papa/camote"),
    ("Cereal caja", "avena; pan dulce -> fruta + yogur natural"),
    ("Papitas", "pepino/jicama/zanahoria con limon"),
    ("Sopa instantanea", "sopa casera con verdura + leguminosa")])) +
  B("est", "Tamiz", "Glucosa/tamiz 24-28 SDG (antes si alto riesgo); enseñar <b>sellos</b>.") +
  B("alr", "Alarma metabolica", "Poliuria/polidipsia, vision borrosa, TA elevada, edema subito."),
  ["refinados", "ultraprocesados", "dmg"])

c("Nausea / reflujo por ayunos y cenas pesadas",
  '13 SDG, agruras, se salta desayuno, cena abundante.',
  B("mng", "Manejo", "<b>Comidas pequeñas y frecuentes</b> (3 + 2 colaciones), no ayunos, no cenar y acostarse, evitar grasa/irritantes.") +
  B("est", "Farmaco", "Nausea: <b>piridoxina 10-25 mg c/8</b> -> doxilamina/piridoxina. Reflujo: famotidina 20 c/12 u omeprazol 20 c/24.") +
  B("alr", "Hiperemesis", "No tolera liquidos, perdida de peso, oliguria, sangre en vomito."),
  ["nausea", "reflujo"])

c("Embarazo vegano / vegetariano",
  '11 SDG, dieta vegana estricta, sin suplementos, cansada.',
  B("ddx", "Deficits", "B12 (muy probable) > hierro hemo > folato/calcio/vitD.") +
  B("mng", "Manejo", "Leguminosas diarias + cereal integral + semillas + fortificados; <b>B12 obligada: cianocobalamina 250-500 mcg/d</b>; Fe/folato/Ca/vitD segun riesgo; referir a nutricion.") +
  B("alr", "Alarma", "Parestesias progresivas, debilidad, glositis, sincope."),
  ["vegana", "b12"])

c("Lactancia - 'mi leche no llena' / adolescente bajo peso",
  'Posparto 7 d, bebe llora; o adolescente con ganancia insuficiente.',
  B("mng", "Lactancia", "<b>LME a libre demanda 8-12 tomas/24 h</b>; corregir agarre (boca abierta, labios evertidos, mas areola inferior); NO agua/te/formula salvo indicacion; madre come suficiente + 10 vasos agua.") +
  B("est", "Mejor indicador", "Pañales mojados + evacuaciones + peso del bebe (no labs de rutina).") +
  B("alr", "Adolescente", "No 'comer por dos': densidad nutricional + tamiz psicosocial (violencia, depresion)."),
  ["lactancia", "adolescente"])

# ==========================================================================
# BLOQUE 3 - PRONAM PRIMEROS 1000 DIAS
# ==========================================================================
d3 = genanki.Deck(1990009603, "No hay tiempo::FINAL Bloques::3 - PRONAM 1000 dias")
decks.append(d3)
c = mk(d3, "Bloque 3 - PRONAM 1000 dias")

c("Control prenatal inicial de bajo riesgo",
  'Prueba positiva, FUM 8 sem, sin dolor ni sangrado.',
  B("est", "Labs base", "BH, grupo/Rh (+Coombs si Rh-), glucosa ayuno, Cr/ac urico, EGO, <b>VIH y sifilis &lt;12 sem</b>, USG 1er T (localizacion/viabilidad/EG), <b>O'Sullivan 24-28 SDG</b>.") +
  B("mng", "Manejo", "Ac folico 0.4 mg (4 mg alto riesgo) + Fe ≥27 mg; vacunas <b>Tdpa ≥20 (ideal 27-36)</b>, influenza, COVID 2-3T; consejeria nutricion/ejercicio.") +
  B("alr", "Referir", "<b>Coopland >4</b>, comorbilidad, multiple, sangrado, HTA/DM, sospecha RCIU."),
  ["prenatal"])

c("LLAVE - Datos de alarma del embarazo (preeclampsia)",
  'Sintomas de alarma >20 SDG. "Memoriza el ramillete de preeclampsia."',
  B("alr", "Urgencia inmediata", "Cefalea intensa, <b>fosfenos, acufenos</b>, epigastralgia, <b>edema de cara/manos</b>, sangrado, salida de liquido, fiebre, dolor abdominal, contracciones, disnea, <b>↓movimientos fetales ≥20 sem</b>.") +
  B("est", "Confirmar", "TA repetida + EGO/proteinuria; BH (plaquetas), Cr, AST/ALT, DHL (HELLP)."),
  ["preeclampsia", "alarma"])

c("Embarazo con obesidad / sospecha DMG",
  '28-30 SDG, IMC 32, ganancia excesiva, glucosa capilar alta.',
  B("est", "Estudios", "Glucosa ayuno y/o <b>O'Sullivan/curva 24-28</b>, EGO, BH, Cr/ac urico si sospecha preeclampsia, USG crecimiento.") +
  B("mng", "Manejo", "Consejeria sin restringir energia peligrosamente; reducir azucar/jugos/ultraprocesados; ejercicio; DMG = dieta+ejercicio+monitoreo, referir si mal control.") +
  B("alr", "Alarma", "Preeclampsia, macrosomia/RCIU, polihidramnios."),
  ["dmg", "obesidad_embarazo"])

c("IVU / pielonefritis en embarazo",
  '24 SDG, ardor al orinar, fiebre y dolor lumbar.',
  B("ddx", "Cistitis vs pielonefritis", "Cistitis = disuria sin fiebre. Pielonefritis = fiebre + dolor lumbar + <b>puñopercusion+</b> (riesgo sepsis/parto pretermino).") +
  B("mng", "Manejo", kt([
    ("Cistitis", "nitrofurantoina 100 c/12 x5d (evitar a termino), cefalexina 500 c/6, fosfomicina 3 g DU"),
    ("Pielonefritis", "REFERIR 2o nivel: ATB IV + vigilancia materno-fetal")])),
  ["ivu", "pielonefritis"])

c("Salud mental perinatal",
  '32 SDG, llora, duerme mal, falta a controles.',
  B("itg", "Pregunta obligatoria", '"¿Ha pensado en hacerse daño, en no querer vivir o en dañar al bebe?"') +
  B("ddx", "Diferenciales", "Depresion/ansiedad perinatal; <b>bipolar</b> (cuidado con antidepresivo solo); <b>psicosis = urgencia</b>; violencia de pareja; hipotiroidismo/anemia.") +
  B("mng", "Manejo", "1a linea psicosocial/TCC; referir si moderada-grave, psicosis o <b>riesgo suicida/dañar al bebe</b>."),
  ["salud_mental_perinatal"])

c("Puerperio + lactancia + anticoncepcion (APEO)",
  'Madre 24 h posparto, RN sano, pide anticoncepcion.',
  B("ddx", "Vigilar", "HPP (sangrado/taquicardia), endometritis (<b>loquios fetidos</b> + fiebre + dolor uterino), mastitis, depresion posparto.") +
  B("mng", "Manejo", "LME libre demanda 8-12/24; consejeria APEO antes del egreso o &lt;42 d; <b>Rh- y RN Rh+ = inmunoglobulina anti-D</b>; cita 5-7 d y RN a 28 d.") +
  B("alr", "RN", "Fiebre ≥38, dificultad respiratoria, no come, no orina, cordon rojo/fetido, ictericia intensa."),
  ["puerperio", "apeo"])

c("RN sano - hora dorada y egreso",
  'RN de termino, vigoroso. Cuidados inmediatos y tamices.',
  B("mng", "Hora dorada", "Pinzamiento <b>30-60 s</b>, piel con piel <b>≥50 min</b>, lactancia temprana, <b>vitamina K 1 mg IM</b>, profilaxis oftalmica, evitar hipotermia.") +
  B("est", "Tamices", kt([
    ("Metabolico", "72 h - 5o dia"), ("Auditivo", "24-48 h"),
    ("Cardiaco", ">24 h y &lt;3 d"), ("Oftalmologico", "1er mes"), ("Cadera", "1-4 meses")])),
  ["rn_sano", "tamices"])

c("Ictericia neonatal",
  'RN 5 d, piel amarilla, duerme mucho, succiona poco.',
  B("ddx", "Fisiologica vs patologica", kt([
    ("Fisiologica", ">24 h, pico dia 3-5, RN sano"),
    ("Patologica", "&lt;24 h, hemolisis ABO/Rh/G6PD, BD alta (colestasis/atresia), prolongada >2 sem")])) +
  B("est", "Estudios", "BT y BD por hora de vida, grupo/Rh + Coombs, BH/reticulocitos, G6PD; <b>zonas de Kramer</b>.") +
  B("mng", "Manejo", "Asegurar 8-12 tomas; <b>fototerapia por umbral</b>; exanguinotransfusion si critico. <b>NO asolear</b>."),
  ["ictericia_neonatal"])

c("Sepsis neonatal",
  'RN 12 d, fiebre 38.2, succion debil, somnoliento.',
  B("itg", "Regla", "Todo RN con fiebre ≥38 o hipotermia + rechazo/letargia = <b>urgencia</b>.") +
  B("est", "Estudios", "Hemocultivo, BH, PCR/procalcitonina, glucosa, EGO/urocultivo, PL si indicada.") +
  B("mng", "Manejo", "Referencia inmediata; <b>ampicilina + gentamicina IV</b>; <b>no retrasar ATB por esperar cultivos</b>; mantener temperatura/glucosa/perfusion."),
  ["sepsis_neonatal"])

c("Tamiz cardiaco + metabolico positivos",
  'RN 36 h SpO2 91/86 preductal/postductal; o tamiz TSH alterado.',
  B("ddx", "Dos urgencias", kt([
    ("Cardiopatia critica", "tamiz+ si SpO2 &lt;90% o dif pre/postductal; eco confirma; PGE1 si ducto-dependiente; NO alta"),
    ("Hipotiroidismo congenito", "TSH alta + somnoliento + estreñido + ictericia prolongada + llanto ronco; levotiroxina, no retrasar")])),
  ["cardiopatia_critica", "hipotiroidismo_congenito"])

# ==========================================================================
# BLOQUE 4 - CANCER DE MAMA
# ==========================================================================
d4 = genanki.Deck(1990009604, "No hay tiempo::FINAL Bloques::4 - Cancer de mama")
decks.append(d4)
c = mk(d4, "Bloque 4 - Cancer de mama")

c("Tamizaje en mujer asintomatica",
  '42 anos, sin sintomas, pregunta por mastografia.',
  B("mng", "Tamizaje", "<b>Mastografia ±tomosintesis desde los 40</b>; alto riesgo +RM; BRCA: RM+masto alternadas c/6 m; <b>autoexploracion 5-10 d post-menstruacion</b>.") +
  B("est", "No pedir", "Sin TAC/PET/marcadores/biopsia si asintomatica y sin lesion.") +
  B("alr", "Signos de alarma", "Bolita nueva, secrecion sanguinolenta, retraccion, piel de naranja, ulcera, ganglio."),
  ["tamizaje"])

c("Riesgo alto / sindrome hereditario (BRCA)",
  '35 anos, madre y tia con cancer de mama.',
  B("ddx", "Criterios", "Mama/ovario &lt;50, <b>bilateral</b>, varon, triple negativo, Ashkenazi, mutacion familiar conocida; TP53/PALB2/PTEN/CHEK2.") +
  B("mng", "Manejo", "Consejo genetico ANTES del panel; vigilancia intensiva RM+masto; cirugia reductora de riesgo en BRCA; <b>quimioprevencion</b>: tamoxifeno 20 mg/raloxifeno 60 (posmen)/anastrozol 1/exemestano 25."),
  ["genetica", "brca"])

c("Bolita sospechosa + conducta BI-RADS",
  '48 anos, bolita dura. "Sospechosa de cancer hasta probar lo contrario."',
  B("ddx", "Maligno vs benigno", "Maligno = dura, irregular, fija, <b>no dolorosa</b>, unilateral, ganglio/piel alterada. Fibroadenoma = movil joven; quiste = fluctuante; mastitis = fiebre/lactancia.") +
  B("est", "Ruta dx", "Masto dx bilateral + US + <b>BI-RADS</b>; <b>4-5 = biopsia con aguja gruesa</b> (no se observan: se biopsian). 0 = completar ≤15 d. 3 = control 6 m. 6 = tratar.") +
  B("alr", "Regla", "No dar AINE/ATB como sustituto de imagen si hay sospecha."),
  ["birads", "bolita"])

c("Mastitis vs cancer inflamatorio",
  'Mama roja. "Lacta = infeccion; no lacta + piel de naranja rapida = cancer."',
  B("ddx", "Discriminador", kt([
    ("Lactancia, fiebre, dolor, eritema", "MASTITIS/absceso"),
    ("No lactante, piel de naranja difusa, progresion rapida, ±sin fiebre", "CANCER INFLAMATORIO")])) +
  B("mng", "Manejo", "Mastitis: vaciar mama + <b>dicloxacilina 500 c/6</b> (o cefalexina; clinda si MRSA) 10-14 d, drenar absceso. Inflamatorio: <b>no retrasar imagen/biopsia por ATB</b>, neoadyuvancia + multidisciplinario."),
  ["mastitis", "cancer_inflamatorio"])

c("Secrecion por pezon + enfermedad de Paget",
  'Descarga por pezon o eccema areolar que no cicatriza.',
  B("ddx", "Patologica", "<b>Unilateral, espontanea, sanguinolenta/serosanguinolenta, 1 ducto</b>. Papiloma intraductal, ectasia (verdosa), galactorrea (bilateral lechosa -> prolactina/TSH).") +
  B("mng", "Manejo", "Patologica: masto + US + BAG. <b>Paget</b> = eccema unilateral que no cicatriza -> biopsia de piel; no seguir cremas.") +
  B("alr", "Alarma", "Sangre por pezon, lesion areolar que no cicatriza, masa, retraccion, ganglios."),
  ["secrecion_pezon", "paget"])

c("Cancer confirmado - subtipo + etapa + referencia",
  'Biopsia confirma cancer. "Objetivo: IHQ, estadio, referir."',
  B("est", "Obligatorio", "<b>IHQ: RE, RP, HER2, Ki-67</b>; labs (BH, renal, hepatica, FA, calcio); estradiol/FSH si pre/perimenopausia.") +
  B("est", "Extension", "Solo si ≥IIB, >5 cm, N+ clinico, sintomas o labs alterados (TAC/gamagrama/PET); <b>eco si antraciclinas o anti-HER2</b>.") +
  B("mng", "Tratamiento", "Luminal pequeño cN0 = cirugia inicial; <b>HER2+ o triple negativo >2 cm o N+ = neoadyuvancia</b>. Luminal: tamoxifeno (premen)/IA (posmen) x5 anos."),
  ["estadificacion", "ihq"])

# ==========================================================================
# BLOQUE 5 - INFECCIONES RESPIRATORIAS ADULTO
# ==========================================================================
d5 = genanki.Deck(1990009605, "No hay tiempo::FINAL Bloques::5 - Infecciones respiratorias")
decks.append(d5)
c = mk(d5, "Bloque 5 - Resp. adulto")

c("IVAS viral / bronquitis aguda",
  'Rinorrea, tos, febricula, auscultacion limpia, SatO2 normal.',
  B("mng", "Manejo", "Sintomatico: paracetamol/ibuprofeno, salino nasal, hidratacion, miel (no &lt;1 a). <b>NO antibiotico</b> (mayoria virales).") +
  B("alr", "Alarma", "Disnea, SatO2 baja, dolor pleuritico, fiebre >3 d o muy alta, confusion, no mejora en 7-10 d."),
  ["ivas", "bronquitis"])

c("Faringitis - Centor/McIsaac",
  'Dolor de garganta. "Cuento Centor: 4 + edad."',
  B("itg", "Centor", "Fiebre + <b>ausencia de tos</b> + exudado amigdalino + adenopatia cervical anterior dolorosa (+ edad).") +
  B("ddx", "Diferenciar", "Viral (tos/rinorrea/conjuntivitis); mononucleosis (adenopatia posterior, hepatoesplenomegalia); <b>absceso periamigdalino</b> (trismus, voz de papa caliente, uvula desviada); epiglotitis (babeo/estridor).") +
  B("mng", "Estrep confirmado", "<b>Penicilina V o amoxicilina 500 c/12 x10 d</b>; alt penicilina G benzatinica 1.2 M UI IM DU."),
  ["faringitis", "centor"])

c("Sinusitis bacteriana aguda",
  'Congestion + dolor facial. "3 criterios que la separan de viral."',
  B("itg", "Criterio bacteriano", "<b>>10 d sin mejorar</b>, o inicio severo (fiebre alta + purulenta + dolor facial), o <b>doble empeoramiento</b>.") +
  B("mng", "Manejo", "Leve/buen seguimiento: observar 48-72 h + sintomatico. Bacteriana: <b>amoxiclav 875/125 c/12 x5-7 d</b> (doxi si alergia). <b>No Rx de senos de rutina</b>; evitar macrolidos.") +
  B("alr", "Complicacion", "Edema/dolor ocular, alteracion visual, cefalea intensa, rigidez de nuca, confusion."),
  ["sinusitis"])

c("Otalgia - OMA vs otitis externa",
  'Dolor de oido. "El otoscopio y el dolor al mover la oreja deciden."',
  B("ddx", "Discriminador", kt([
    ("Dolor profundo, fiebre, hipoacusia, timpano abombado/opaco", "OMA"),
    ("Dolor al presionar trago/mover pabellon, antecedente de agua/cotonete", "OTITIS EXTERNA")])) +
  B("mng", "Manejo", "OMA: <b>amoxicilina 500 c/8 u 875 c/12 x5-7 d</b> (amoxiclav si falla). OE: gotas <b>ciprofloxacino ±esteroide</b>; <b>evitar aminoglucosidos si perforacion</b>.") +
  B("alr", "Mastoiditis", "Dolor retroauricular, pabellon desplazado, fiebre."),
  ["otitis", "oma"])

c("Neumonia adquirida en la comunidad",
  'Fiebre, tos, disnea, crepitantes focales. "CURB-65 decide destino."',
  B("itg", "CURB-65", "Confusion, Urea alta, FR ≥30, TA baja, edad ≥65.") +
  B("mng", "Ambulatorio", kt([
    ("Sano", "amoxicilina 1 g c/8 o doxiciclina 100 c/12, ≥5 d"),
    ("Comorbilidad", "amoxiclav 875/125 c/12 + doxiciclina/macrolido")])) +
  B("alr", "Hospital", "SatO2 baja, FR alta, hipoTA, confusion, no tolera VO, sepsis, CURB-65 alto."),
  ["nac", "curb65"])

c("Asma - crisis y control",
  'Disnea episodica, sibilancias, tos nocturna, mejora con salbutamol.',
  B("mng", "Crisis", "<b>Salbutamol 4-10 disparos con espaciador c/20 min la 1a hora</b> + O2 si baja; moderada-grave: <b>prednisona 40-50 mg/d x5-7 d</b>.") +
  B("mng", "Control cronico", "<b>NO dejar SABA solo</b>: siempre corticoide inhalado (ICS-formoterol).") +
  B("alr", "Grave", "No habla, silencio auscultatorio, cianosis, somnolencia, no mejora con salbutamol, intubacion previa."),
  ["asma"])

c("EPOC / exacerbacion / cor pulmonale",
  'Tabaco o biomasa, tos cronica, disnea progresiva.',
  B("ddx", "Tres caras", kt([
    ("EPOC estable", "FEV1/FVC bajo postBD persistente"),
    ("Exacerbacion", "↑disnea, ↑volumen o ↑purulencia del esputo"),
    ("Cor pulmonale", "falla derecha: IY, hepatomegalia, edema")])) +
  B("mng", "Manejo", "Dejar tabaco + vacunas; broncodilatador largo (<b>LAMA/LABA</b>); rehabilitacion; O2 cronico si hipoxemia.") +
  B("alr", "Bandera roja", "Perdida de peso/hemoptisis = descartar cancer pulmonar."),
  ["epoc"])

# ==========================================================================
# BLOQUE 6 - PEDIATRIA
# ==========================================================================
d6 = genanki.Deck(1990009606, "No hay tiempo::FINAL Bloques::6 - Pediatria")
decks.append(d6)
c = mk(d6, "Bloque 6 - Pediatria")

c("LLAVE - Umbrales peds que deciden gravedad",
  'Cualquier nino. "Numeros que cambian el destino."',
  B("est", "Memoriza", kt([
    ("SatO2 &lt;90%", "hipoxemia -> O2 y hospital (umbral OMS)"),
    ("Convulsion febril simple", "6 m-5 a, generalizada, &lt;15 min, no repite 24 h, recupera, sin meningeos"),
    ("Deshidratacion mod (Plan B)", "SRO 75 mL/kg en 4 h"),
    ("Paracetamol", "10-15 mg/kg/dosis c/6 h"),
    ("Convulsion >5 min", "benzodiacepina (diazepam/midazolam)")])),
  ["umbrales_peds"])

c("Neumonia comunitaria grave (peds)",
  'Lactante 8 m, fiebre, tos, dificultad respiratoria, SatO2 89%.',
  B("est", "Estudios", "SatO2 continua, <b>Rx torax</b> (consolidacion/broncograma/derrame), BH, glucosa, electrolitos.") +
  B("mng", "Manejo", "Hospitalario: O2 para SatO2 ≥90, vias IV, <b>ampicilina IV</b> o <b>ceftriaxona/cefotaxima IV</b> si grave/vacunacion incompleta.") +
  B("alr", "Alarma", "Cianosis, tiraje intenso, no lacta, somnolencia, pausas respiratorias."),
  ["neumonia_peds"])

c("Bronquiolitis",
  'Lactante 5 m, rinorrea, tos, 1er episodio de sibilancias.',
  B("ddx", "Vs neumonia/asma", "<b>&lt;2 a + 1er episodio + sibilancias difusas + viral</b>. Neumonia = foco + consolidacion; asma = episodios previos.") +
  B("mng", "Manejo", "Soporte: <b>lavados nasales + hidratacion + O2 si baja</b>. <b>NO ATB, no antitusivos</b>; salbutamol solo si prueba con respuesta clara.") +
  B("alr", "Alarma", "Pausas respiratorias, cianosis, no come, &lt;3 meses."),
  ["bronquiolitis"])

c("Crup (laringotraqueitis)",
  'Nino 2 a, tos perruna, ronquera, estridor inspiratorio.',
  B("mng", "Manejo", "<b>Dexametasona 0.15-0.6 mg/kg DU</b> (VO/IM/IV); <b>adrenalina nebulizada</b> si estridor en reposo (observar por rebote); O2 si hipoxemia.") +
  B("ddx", "Vs epiglotitis", "Epiglotitis = fiebre alta, babeo, toxico, posicion tripode -> <b>no manipular via aerea</b>."),
  ["crup"])

c("Crisis asmatica pediatrica",
  'Nino 6 a, sibilancias, disnea, episodios previos.',
  B("mng", "Manejo", "O2 si baja; <b>salbutamol 4-10 disparos c/20 min 1a hora</b>; ipratropio si moderada-grave; <b>prednisolona 1-2 mg/kg/d x3-5 d</b>.") +
  B("alr", "Grave", "No habla/come, cianosis, silencio auscultatorio, somnolencia, no mejora con salbutamol."),
  ["asma_peds"])

c("OMA y faringitis pediatricas",
  'Otalgia/fiebre o exudado amigdalino + adenopatia anterior.',
  B("mng", "Dosis peds", kt([
    ("OMA", "amoxicilina 80-90 mg/kg/d c/12 x5-10 d; ATB si &lt;2 a / bilateral / fiebre alta / otorrea"),
    ("Faringitis estrep", "amoxicilina 50 mg/kg/d x10 d (Centor)")])) +
  B("alr", "Alarma OMA", "Dolor retroauricular, pabellon desplazado, rigidez de nuca = mastoiditis."),
  ["oma_peds", "faringitis_peds"])

c("Fiebre con exantema - Kawasaki",
  '4 a, fiebre 5 d, exantema, ojos rojos, labios fisurados, adenopatia.',
  B("itg", "Criterios", "<b>Fiebre ≥5 d + 4/5</b>: conjuntivitis bilateral no exudativa, cambios orales (labios/lengua fresa), exantema polimorfo, adenopatia cervical, cambios manos/pies.") +
  B("mng", "Manejo", "Hospitalizar; <b>IGIV 2 g/kg DU &lt;10 dias</b> + AAS; eco para aneurismas coronarios.") +
  B("ddx", "No perder", "Sarampion, escarlatina, <b>meningococcemia</b> (petequias/purpura = urgencia)."),
  ["kawasaki"])

c("Meningitis vs convulsion febril simple",
  '18 meses con fiebre y convulsion.',
  B("est", "Siempre", "<b>Glucosa capilar inmediata</b> (hipoglucemia convulsiona).") +
  B("ddx", "Meningitis (no perder)", "Fiebre + irritabilidad/letargia, <b>fontanela abombada</b>, rigidez de nuca, petequias, convulsion focal/prolongada/recurrente, no recupera.") +
  B("mng", "Manejo", "CFS: paracetamol + explicar benignidad + buscar foco (no EEG/TAC/anticonvulsivo). Sospecha meningitis: <b>hospitalizar + ATB IV inmediato</b> (PL si no contraindicada)."),
  ["meningitis", "convulsion_febril"])

c("Diarrea con deshidratacion moderada",
  'Bebe 7 m, diarrea, ojos hundidos, sed, alerta.',
  B("mng", "Plan B", "<b>SRO 75 mL/kg en 4 h</b>, continuar lactancia, tomas pequeñas frecuentes; <b>no antidiarreicos</b>, no ATB sin indicacion.") +
  B("ddx", "No perder", "Disenteria (sangre/moco -> coprocultivo), <b>invaginacion</b> (dolor colico + heces en jalea), abdomen agudo.") +
  B("alr", "Alarma", "Letargia, no tolera VO, llenado capilar lento, oliguria, sangre en heces."),
  ["diarrea_peds"])

# ==========================================================================
# BLOQUE 7 - DM2 / SINDROME METABOLICO
# ==========================================================================
d7 = genanki.Deck(1990009607, "No hay tiempo::FINAL Bloques::7 - DM2 y sindrome metabolico")
decks.append(d7)
c = mk(d7, "Bloque 7 - DM2 / Sx metabolico")

c("LLAVE - Diagnostico de DM, prediabetes y Sx metabolico",
  'Cualquier tamiz metabolico. "Memoriza los cortes."',
  B("est", "Cortes diagnosticos", kt([
    ("Diabetes", "ayuno ≥126, HbA1c ≥6.5, o casual ≥200 con sintomas"),
    ("Prediabetes", "ayuno 100-125 o HbA1c 5.7-6.4"),
    ("Sx metabolico", "cintura alta + ≥2: TA ≥130/85, glu ≥100, TG ≥150, HDL bajo"),
    ("Umbral con comorbilidad", "tratar HTA desde ≥130/80; LDL ≤70 si ECV")])),
  ["diagnostico_dm", "sindrome_metabolico"])

c("Metformina - inicio y limites",
  'Prediabetes o DM2 inicial sin catabolismo.',
  B("mng", "Inicio", "<b>Metformina 850 c/24 con comida x7 d -> 850 c/12</b> si tolera.") +
  B("alr", "Limites", "<b>No si TFGe &lt;30</b>; vigila B12 baja en uso cronico; efectos GI.") +
  B("est", "Escalada", "<b>HbA1c ≥9% o catabolismo -> combinado</b>; con catabolismo: metformina + <b>insulina basal 0.3 UI/kg</b>."),
  ["metformina"])

c("Organo-proteccion en DM2 (mas alla del azucar)",
  'DM2 + albuminuria / ERC / IC / ECV. "Eliges farmaco por el organo."',
  B("mng", "Switch por organo", kt([
    ("Albuminuria/ERC/IC/ECV", "iSGLT2: dapagliflozina 10 c/24 o empagliflozina"),
    ("HTA + albuminuria", "IECA/ARA: losartan 50 c/24 (revisar Cr/K)"),
    ("Diabetes + LDL alto", "atorvastatina (40-80 si ECV; meta LDL ≤70)")])) +
  B("com", "🗣️ ECOE", '"Mi objetivo no es solo bajar el azucar: reduzco riesgo cardiovascular, renal, visual y de pie."'),
  ["isglt2", "nefroproteccion"])

c("Pie diabetico, neuropatia y nefropatia",
  'DM2 de anos, ardor en pies, RAC elevado.',
  B("exp", "Tamiz de pie/organos", "<b>Monofilamento</b> (neuropatia), <b>ITB &lt;0.9</b> (EAP), <b>RAC ≥30</b> (nefropatia), fondo de ojo (retinopatia).") +
  B("mng", "Manejo", "Dolor neuropatico: gabapentina/pregabalina/duloxetina; <b>B12 si usa metformina</b>; cuidado de pies (secar interdigital, calzado ancho, no descalza); referir angiologia si ITB/pulsos."),
  ["pie_diabetico", "neuropatia"])

c("Criterios de referencia a 2o nivel (DM2)",
  '"Cuando supera la capacidad segura del primer nivel."',
  B("est", "Referir si", kt([
    ("Embarazo + DM", "alto riesgo materno-fetal"),
    ("TFGe ≤30", "nefrologia; evitar metformina"),
    ("Vision subita / miodesopsias", "oftalmologia urgente"),
    ("IMC ≥40", "obesidad grave"),
    ("Sospecha DM1 / cetosis", "urgencias"),
    ("Descontrol pese a insulina basal+rapida", "endocrino")])),
  ["referencia_dm"])

# ==========================================================================
# BLOQUE 8 - SOBREPESO Y OBESIDAD
# ==========================================================================
d8 = genanki.Deck(1990009608, "No hay tiempo::FINAL Bloques::8 - Sobrepeso y obesidad")
decks.append(d8)
c = mk(d8, "Bloque 8 - Obesidad")

c("Clasificacion, cintura y 5A",
  'Adulto con IMC elevado. "Clasifico, mido cintura, aplico 5A."',
  B("est", "Clases", "Sobrepeso 25-29.9; clase I 30-34.9; II 35-39.9; III ≥40. <b>Cintura ≥80 mujer / ≥90 varon</b> = obesidad abdominal.") +
  B("mng", "5A + tratamiento", "Preguntar permiso, Evaluar, Aconsejar, Acordar, Ayudar; cambios de estilo de vida; <b>farmaco solo si no pierde ≥5% en 6 meses</b> -> referir 2o nivel.") +
  B("est", "Comorbilidad", "Glucosa/HbA1c, lipidos, transaminasas (higado graso), ac urico; TSH si clinica."),
  ["clasificacion_imc", "5a"])

c("Obesidad complicada (SAHOS/HTA/artrosis/ERGE)",
  'IMC 38, ronca con pausas, somnolencia, cefalea matutina, reflujo.',
  B("itg", "STOP-Bang", "Ronca, cansancio, apneas observadas, HTA, IMC ≥35, edad ≥50, varon, cuello aumentado -> <b>polisomnografia</b> si intermedio/alto.") +
  B("mng", "Manejo", "Ejercicio adaptado; ERGE: omeprazol 20 c/24; dolor: paracetamol (evitar AINE cronico); <b>referir si IMC ≥35 con comorbilidad o ≥40</b>.") +
  B("alr", "Alarma", "Somnolencia al conducir, apneas severas, disfagia/perdida de peso (endoscopia)."),
  ["sahos", "obesidad_complicada"])

c("Obesidad + SOP",
  '28 anos, IMC 33, acne, hirsutismo, oligomenorrea, infertilidad, acantosis.',
  B("ddx", "Descartar primero", "<b>Embarazo</b> siempre; hipotiroidismo, hiperprolactinemia, Cushing, tumor androgenico.") +
  B("mng", "Manejo", "Perdida de peso (mejora ciclos/fertilidad); <b>si no desea embarazo: ACO combinado</b>; metformina si resistencia/prediabetes; deseo de embarazo -> referir infertilidad."),
  ["sop"])

c("Obesidad secundaria / por farmaco (Cushing exogeno)",
  'Aumento de 18 kg en 8 meses, estrias violaceas, debilidad proximal, usa prednisona.',
  B("ddx", "Banderas", "Aumento rapido + <b>estrias violaceas + debilidad proximal + HTA nueva</b> = sospecha secundaria; antipsicoticos/esteroides suben peso.") +
  B("mng", "Manejo", "<b>No suspender esteroide bruscamente</b> (insuficiencia suprarrenal); coordinar menor dosis; manejar riesgo metabolico; referir endocrino."),
  ["cushing", "obesidad_secundaria"])

# ==========================================================================
# BLOQUE 9 - HIPERTENSION ARTERIAL
# ==========================================================================
d9 = genanki.Deck(1990009609, "No hay tiempo::FINAL Bloques::9 - Hipertension arterial")
decks.append(d9)
c = mk(d9, "Bloque 9 - HTA")

c("HTA de reciente diagnostico + tecnica",
  '48 anos, PA 150/94, sedentario, dieta salada.',
  B("itg", "Tecnica + confirmacion", "Reposo 5 min, sin cafe/tabaco/ejercicio 30 min, 3 tomas; <b>≥140/90 en consultorio confirmado fuera</b> (AMPA/MAPA). Descartar bata blanca/enmascarada.") +
  B("mng", "Manejo", "Estilo de vida en todos; <b>meta &lt;130/80</b>.") +
  B("est", "Estudios base", "BH, QS, Na/K/Ca, ac urico, HbA1c, EGO+albuminuria, lipidos, ECG."),
  ["dx_hta", "tecnica"])

c("Inicio de tratamiento - terapia dual",
  'HTA confirmada. "Combinacion, no monoterapia de rutina."',
  B("mng", "Esquemas", kt([
    ("ARA/IECA + calcioantagonista", "valsartan/amlodipino, perindopril/amlodipino"),
    ("ARA/IECA + tiazida", "telmisartan/HCTZ")])) +
  B("alr", "Cuidado", "En Sx metabolico/DM preferir IECA-ARA + calcioantagonista; vigilar Cr/K tras IECA/ARA."),
  ["tratamiento_hta"])

c("Urgencia vs emergencia hipertensiva",
  'PA ≥180/110. "La diferencia es el daño agudo a organo blanco."',
  B("ddx", "Discriminador", kt([
    ("≥180/110 SIN daño agudo", "URGENCIA: bajar en 24-48 h VO (amlodipino 5-10), revisar adherencia"),
    ("≥180/110 CON daño (SCA, EVC, EAP, diseccion, LRA, retina)", "EMERGENCIA: reducir ~25% en 1-2 h IV, referir")])) +
  B("alr", "Regla", "<b>NO sublingual</b> (hipoperfusion cerebral/coronaria/renal)."),
  ["urgencia_hta", "emergencia_hta"])

c("HTA en embarazo / preeclampsia",
  '28 SDG, PA 150/96, cefalea y edema.',
  B("ddx", "Clasificar", "<b>≥140/90 >20 sem</b>: gestacional (sin proteinuria) vs <b>preeclampsia</b> (+proteinuria/daño); HELLP (epigastralgia + plaquetas bajas).") +
  B("mng", "Farmacos seguros", "Alfametildopa, nifedipino LP, labetalol/metoprolol; <b>EVITAR IECA/ARA</b>. Preeclampsia severa/eclampsia: <b>sulfato de magnesio</b> + referir.") +
  B("alr", "Alarma", "Cefalea, fosfenos, epigastralgia, convulsiones, ↓movimientos fetales."),
  ["hta_embarazo", "preeclampsia"])

c("HTA secundaria en joven",
  '28 anos, PA 160/100, crisis de cefalea/palpitacion/sudor.',
  B("ddx", "Pista -> causa", kt([
    ("Crisis cefalea+palpitacion+sudor", "feocromocitoma (metanefrinas)"),
    ("HTA + hipoK, calambres", "hiperaldosteronismo (aldosterona/renina)"),
    ("Soplo abdominal", "renovascular (Doppler renal)"),
    ("Pulsos femorales disminuidos", "coartacion aortica"),
    ("Estrias violaceas, obesidad central", "Cushing"),
    ("Ronquido/somnolencia", "SAHOS")])) +
  B("mng", "Manejo", "Tratar mientras estudias + <b>referir</b> (puede haber causa curable)."),
  ["hta_secundaria"])

c("Adulto mayor fragil con ortostatismo",
  '87 anos, mareo al levantarse, caida; PA sentada 150/82, de pie 125/70.',
  B("exp", "Diagnostico", "Caida <b>PAS ≥20 o PAD ≥10 mmHg al ponerse de pie</b> (medir sentado y a 1-3 min de pie).") +
  B("mng", "Manejo", "Causa frecuente: <b>sobretratamiento/polifarmacia</b> + deshidratacion; deprescribir, revisar farmacos; escala de fragilidad Rockwood individualiza metas."),
  ["ortostatismo", "adulto_mayor"])

# ==========================================================================
# BLOQUE 10 - VACUNACION
# ==========================================================================
d10 = genanki.Deck(1990009610, "No hay tiempo::FINAL Bloques::10 - Vacunacion")
decks.append(d10)
c = mk(d10, "Bloque 10 - Vacunacion")

c("LLAVE - Interrogatorio universal antes de vacunar",
  'Antes de cualquier vacuna. "Edad+cartilla -> riesgo -> contraindicaciones."',
  B("itg", "Checklist", kt([
    ("Edad/cartilla", "que falta; nunca le dijeron que no se vacune"),
    ("Reaccion previa", "anafilaxia (no repetir esa vacuna)"),
    ("Enfermedad actual", "leve no contraindica; moderada-grave pospone"),
    ("Inmunosupresion", "evitar VIVAS (BCG, SRP) si VIH no controlado/cancer/QT/esteroides"),
    ("Embarazo", "no vivas (SRP/BCG)"),
    ("Transfusion/Ig reciente", "posponer SRP")])),
  ["interrogatorio_vacunas"])

c("RN / lactante - esquema inicial",
  'Recien nacido/lactante a vacunacion basal.',
  B("mng", "Esquema", kt([
    ("BCG", "DU, intradermica, ≥2000 g"),
    ("Hepatitis B", "RN &lt;24 h (no como dosis neonatal despues de 7 d)"),
    ("Rotavirus", "2 y 4 m; 1a desde 6 sem, 2a no >7 m 29 d"),
    ("Hexavalente", "2-4-6-18 m"),
    ("Neumococo 13v", "2-4-12 m")])) +
  B("alr", "Post-rotavirus", "Vomito persistente, <b>evacuacion con sangre/jalea</b>, encoger piernas = invaginacion."),
  ["rn_vacunas", "rotavirus"])

c("Preescolar 4-6 anos con cartilla incompleta",
  'Nino 5 a entra a primaria.',
  B("mng", "Aplicar", "<b>DPT refuerzo a los 4 a</b> (max 6 a 11 m), <b>SRP</b> (12 y 18 m), influenza anual, neumococo si aplica.") +
  B("alr", "Regla", "Cartilla incompleta = <b>actualizar, NO reiniciar</b> el esquema."),
  ["preescolar_vacunas", "dpt", "srp"])

c("Adolescente 11 anos - VPH",
  'Revision escolar, no sabe si tiene VPH.',
  B("mng", "VPH", "<b>Dosis unica</b> a los 11 a / 5o de primaria; <b>3 dosis 0-2-6</b> si VIH o protocolo de violacion. <b>No requiere prueba de VPH</b> ni sustituye tamizaje.") +
  B("mng", "Rescate", "Hepatitis B (0-1-6) si no documentada; SR/SRP si incompleta (no embarazo/inmunosupresion)."),
  ["vph", "adolescente_vacunas"])

c("Embarazada - vacunas maternas",
  '28 SDG, pregunta que puede recibir.',
  B("mng", "Indicadas", "<b>Tdpa cada embarazo desde sem 20 (ideal 27-36)</b>, influenza anual, COVID (prefiere 2-3 T).") +
  B("alr", "Contraindicadas", "<b>SRP y BCG (vivas)</b> -> SRP posparto si falta."),
  ["embarazada_vacunas", "tdpa"])

c("Adulto con riesgo - hepatitis B",
  'Personal de salud / multiples parejas / UDIV / dialisis / VIH.',
  B("mng", "Esquema", "0, 1 y 6 meses; <b>dialisis: 40 mcg</b> y confirmar seroconversion.") +
  B("est", "Proteccion", "<b>anti-HBs ≥10 UI/mL = protegido</b>; si &lt;10, reforzar; si no responde a 2o esquema = no conversor."),
  ["hepatitis_b", "adulto_riesgo"])

c("Adulto mayor ≥60 con comorbilidad",
  '65 a, diabetes y EPOC, no recuerda vacunas.',
  B("mng", "Esquema", kt([
    ("Influenza", "anual"), ("COVID", "anual ≥60"),
    ("Neumococo conjugada 13v", "DU desde 60 a"),
    ("Neumococo polisacarida 23v", "desde 61 a, ≥12 m despues de la conjugada"),
    ("Td", "refuerzo c/10 a")])),
  ["adulto_mayor_vacunas", "neumococo"])

c("Evento adverso vs reaccion esperada",
  'Vacunado hace 24-48 h con dolor/fiebre. "¿Fue mala reaccion?"',
  B("ddx", "Esperado vs grave", kt([
    ("Esperado", "dolor local, eritema, fiebre baja, irritabilidad, buen estado"),
    ("GRAVE", "anafilaxia, invaginacion post-rotavirus (jalea), BCGitis, convulsion/alteracion de alerta")])) +
  B("alr", "Anafilaxia", "Urticaria generalizada, edema facial, dificultad respiratoria, hipotension -> urgencias."),
  ["evento_adverso"])

# ==========================================================================
package = genanki.Package(decks)
out = os.path.join(OUTPUT_DIR, "No_Hay_Tiempo_FINAL_Bloques.apkg")
package.write_to_file(out)
total = sum(len(d.notes) for d in decks)
print(f"OK -> {out}")
print(f"Decks: {len(decks)} | Notas: {total}")
for d in decks:
    print(f"  [{len(d.notes):2}] {d.name}")
