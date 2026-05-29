"""Deck INTEGRADOR de Medicina Interna (Adulto) - agrupadores y clasificaciones.

Reagrupa el contenido de la Capa 1 (Reconocimiento de Patron) en sentido inverso:
en vez de "caso -> entidad", va de "categoria paraguas -> subclasificaciones +
el parametro que las separa". Formato Q&A (front = concepto padre; back = tabla
de hijos con valores discriminadores).

  Tipo A (17): agrupadores -> front categoria, back tabla de subtipos + discriminador
  Tipo B (6):  discriminador rapido -> front parametros, back a que clasificacion apuntan

Deck: "Medicina Interna Adulto::Integrador - Clasificaciones"
Fuente de contenido: medicina_interna/build/build_medicina_interna.py (Capa 1, 45 cloze)
Guias: ACC/AHA SCA/IC/HTA + ADA + KDIGO/Sepsis-3/CURB-65/Duke/Anthonisen/Wells + ATA + UpToDate
"""
import os
import genanki

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "output")
os.makedirs(OUTPUT_DIR, exist_ok=True)

MODEL_QA_ID = 1607392320          # reusable (ids.json: qa_estandar)
DECK_ID = 1573829104              # nuevo, unico (no colisiona con ids.json)
DECK_NAME = "Medicina Interna Adulto::Integrador - Clasificaciones"

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
BASE_TAGS = ["medicina_interna", "integrador", "ecoe"]


def qa(front, back, tags):
    deck.add_note(genanki.Note(model=model_qa, fields=[front, back], tags=BASE_TAGS + tags))


def tabla(headers, filas):
    th = "".join(f"<th>{h}</th>" for h in headers)
    body = ""
    for fila in filas:
        body += "<tr>" + "".join(f"<td>{c}</td>" for c in fila) + "</tr>"
    return f"<table><tr>{th}</tr>{body}</table>"


AG = ["agrupador"]
DR = ["discriminador_rapido"]

# ============================================================
# TIPO A - AGRUPADORES (categoria -> subtipos + discriminador)
# ============================================================

# 1. Complicaciones metabolicas agudas de la DM
qa("Complicaciones metabolicas agudas de la diabetes mellitus: cuales son y que parametro las separa?",
   tabla(["Entidad", "Glucosa", "Cetonas/acidosis", "Osmolaridad", "Perfil tipico"],
         [["<b>CAD</b>", "&gt;250", "SI (pH &lt;7.3, HCO3 &lt;18, anion gap alto)", "variable", "DM1; precipitante: infeccion, no adherencia, IAM"],
          ["<b>EHH</b>", "&gt;600", "NO significativas", "&gt;320", "DM2, adulto mayor; deficit 8-10 L"]]) +
   '<span class="disc">Discriminador: cetoacidosis (CAD) vs hiperosmolaridad sin cetosis (EHH); la insulinemia residual del DM2 evita la cetogenesis franca.</span>'
   '<span class="ecoe">ECOE: "Ante hiperglucemia + alteracion mental, separo CAD de EHH con cetonas, pH y osmolaridad."</span>',
   AG + ["endocrino", "dm_agudas"])

# 2. Sindrome coronario agudo
qa("Sindrome coronario agudo: subtipos y los parametros que los definen.",
   tabla(["Tipo", "ECG", "Troponina", "Manejo clave"],
         [["<b>IAMCEST</b>", "ST &ge;1 mm en 2 contiguas (&ge;2 mm V2-V3) o BRI nuevo", "elevada", "reperfusion: ICP &lt;90 min / fibrinolisis &lt;120 min"],
          ["<b>IAMSEST</b>", "ST descendido / T invertida (sin ST elevado persistente)", "elevada", "invasivo &lt;24 h si alto riesgo (GRACE/TIMI)"],
          ["<b>Angina inestable</b>", "sin cambios persistentes", "NORMAL", "estratificar riesgo"]]) +
   '<span class="disc">Discriminador: ST elevado persistente -> IAMCEST; la troponina separa IAMSEST (elevada) de angina inestable (normal).</span>'
   '<span class="ecoe">ECOE: "Clasifico el SCA por el ECG (ST) y la troponina; eso define el tiempo y la via de reperfusion."</span>',
   AG + ["cardio", "sca"])

# 3. IC segun FEVI
qa("Insuficiencia cardiaca clasificada por FEVI: clases y que las orienta.",
   tabla(["Clase", "FEVI", "Mecanismo", "Pistas clinicas"],
         [["<b>IC-FEr</b>", "&le;40%", "falla SISTOLICA", "S3 (galope), cardiopatia isquemica; 4 pilares (ARNI/IECA+BB+ARM+iSGLT2)"],
          ["<b>IC-FElr</b>", "41-49%", "intermedia", "zona de transicion"],
          ["<b>IC-FEp</b>", "&ge;50%", "falla DIASTOLICA", "mujer mayor, HTA cronica, S4"]]) +
   '<span class="disc">Discriminador: la FEVI%; S3 apunta a sistolica (FEr), S4 a diastolica (FEp).</span>'
   '<span class="ecoe">ECOE: "Defino el tipo de IC por la FEVI del eco; eso decide si aplico los 4 pilares."</span>',
   AG + ["cardio", "ic"])

# 4. Crisis hipertensiva
qa("Crisis hipertensiva (PA &ge;180/120): como se subclasifica y que la define?",
   tabla(["Tipo", "Definicion", "Manejo"],
         [["<b>Emergencia</b>", "CON dano agudo de organo (encefalopatia, EAP, IAM, diseccion, eclampsia)", "antihipertensivo IV en UCI; bajar &le;25% en 1a hora"],
          ["<b>Urgencia</b>", "SIN dano agudo de organo", "VO ambulatorio; descenso gradual en 24-48 h"]]) +
   '<span class="disc">Discriminador: NO es la cifra, es la presencia de dano de organo blanco.</span>'
   '<span class="ecoe">ECOE: "Diferencio emergencia de urgencia por el dano organico, no por el numero de la PA."</span>',
   AG + ["cardio", "crisis_hta"])

# 5. Valvulopatias izquierdas / soplos
qa("Soplos de valvulopatias izquierdas severas: como se distinguen?",
   tabla(["Lesion", "Soplo", "Foco / irradiacion", "Pista"],
         [["<b>Estenosis aortica</b>", "sistolico expulsivo", "foco aortico -> carotidas", "triada sincope + angina + disnea; pulso parvus et tardus"],
          ["<b>Insuf. mitral</b>", "holosistolico", "apex -> axila", "cronica: dilatacion VI; aguda: EAP fulminante"]]) +
   '<span class="disc">Discriminador: morfologia del soplo (expulsivo vs holosistolico) + foco e irradiacion.</span>'
   '<span class="ecoe">ECOE: "Localizo el soplo y su irradiacion; eso me orienta la valvula afectada y pido eco."</span>',
   AG + ["cardio", "valvulopatias"])

# 6. Emergencias tiroideas
qa("Emergencias tiroideas: cuales son y como se diferencian?",
   tabla(["Entidad", "Eje", "Hallazgos", "Escala / tratamiento"],
         [["<b>Tormenta tiroidea</b>", "hiper grave", "fiebre &ge;38.5, taqui/FA, agitacion, falla multiorganica", "Burch-Wartofsky; propranolol + tionamida + yodo + corticoide"],
          ["<b>Coma mixedematoso</b>", "hipo grave", "hipotermia, hipoventilacion, bradicardia, edema sin fovea", "TSH muy alta; levotiroxina IV + hidrocortisona"]]) +
   '<span class="redflag">Ambas con alta mortalidad; el coma mixedematoso lleva hidrocortisona por posible insuf. suprarrenal asociada.</span>'
   '<span class="ecoe">ECOE: "Reconozco el extremo del eje tiroideo (hiper vs hipo) y trato en UCI sin esperar laboratorio definitivo."</span>',
   AG + ["endocrino", "emergencias_tiroideas"])

# 7. Disfuncion tiroidea cronica
qa("Disfuncion tiroidea cronica: como se clasifica por TSH y hormonas?",
   tabla(["Cuadro", "TSH", "T4 libre", "Marcador / nota"],
         [["<b>Graves (hiper)</b>", "suprimida", "alta", "TRAb +, bocio difuso, oftalmopatia"],
          ["<b>Hipotiroidismo 1&deg;</b>", "elevada", "baja", "Hashimoto (anti-TPO +); levotiroxina 1.6 mcg/kg/d"],
          ["<b>Subclinico</b>", "alterada", "normal", "tratar hipo si TSH &gt;10 o sintomas/bocio"]]) +
   '<span class="disc">Discriminador: TSH define la direccion; T4 libre define si es clinico o subclinico.</span>'
   '<span class="ecoe">ECOE: "Leo primero la TSH; si la T4 libre es normal estoy ante un subclinico."</span>',
   AG + ["endocrino", "tiroides"])

# 8. Trastornos del potasio
qa("Trastornos del potasio: patron ECG y manejo de cada uno.",
   tabla(["Trastorno", "ECG (progresion)", "Manejo clave"],
         [["<b>Hiperkalemia</b>", "T picudas -> QRS ancho -> ondas sinusoidales -> paro", "gluconato de calcio (estabiliza) + insulina/glucosa + beta2 + diuretico/resina/dialisis"],
          ["<b>Hipokalemia</b>", "T aplanada + ondas U + QT largo", "reponer K (riesgo de torsade)"]]) +
   '<span class="disc">Discriminador: T picudas (hiper) vs T plana con onda U (hipo).</span>'
   '<span class="ecoe">ECOE: "Con cambios ECG por hiperK, gluconato de calcio inmediato y luego redistribuyo el potasio."</span>',
   AG + ["electrolitos", "potasio"])

# 9. AKI por localizacion
qa("Lesion renal aguda (AKI): clasificacion por localizacion y parametros que orientan.",
   tabla(["Tipo", "BUN/Cr", "FeNa", "Sedimento / USG"],
         [["<b>Prerrenal</b>", "&gt;20", "&lt;1%", "normal; responde a volumen (hipoperfusion: deshidratacion, IC, sepsis)"],
          ["<b>Intrinseca (NTA)</b>", "&lt;20", "&gt;2%", "cilindros granulosos marrones (isquemia/nefrotoxinas)"],
          ["<b>Postrenal</b>", "variable", "variable", "hidronefrosis en USG; anuria subita (HBP, neoplasia, litiasis)"]]) +
   '<span class="disc">Discriminador: FeNa y BUN/Cr separan pre/intrinseca; la USG (hidronefrosis) marca la postrenal.</span>'
   '<span class="ecoe">ECOE: "Clasifico la AKI con BUN/Cr, FeNa y USG renal antes de decidir conducta."</span>',
   AG + ["renal", "aki"])

# 10. Sindromes glomerulares
qa("Sindromes glomerulares: nefrotico vs nefritico, que los separa?",
   tabla(["Sindrome", "Proteinuria", "Sedimento", "Otros"],
         [["<b>Nefrotico</b>", "&gt;3.5 g/d", "lipiduria", "hipoalbuminemia + edema + dislipidemia + hipercoagulabilidad"],
          ["<b>Nefritico</b>", "&lt;3.5 g/d", "cilindros eritrocitarios (hematuria)", "HTA + AKI"]]) +
   '<span class="disc">Discriminador: magnitud de la proteinuria (&gt;3.5 nefrotico) y el sedimento (cilindros eritrocitarios -> nefritico).</span>'
   '<span class="ecoe">ECOE: "Separo nefrotico de nefritico por proteinuria y sedimento, y refiero a nefrologia para biopsia."</span>',
   AG + ["renal", "glomerular"])

# 11. Patron de hepatopatia (transaminasas)
qa("Patron de transaminasas en hepatopatia cronica: alcoholica vs metabolica.",
   tabla(["Entidad", "AST/ALT", "Otros", "Severidad / manejo"],
         [["<b>Hepatitis alcoholica</b>", "&gt;2", "GGT alta, fiebre, ictericia, hepatomegalia dolorosa", "Maddrey (mDF) &ge;32 -> corticoide; abstinencia"],
          ["<b>MASLD / MASH</b>", "&lt;1", "obesidad/DM/dislipidemia/sd metabolico", "perdida de peso 7-10%; resmetirom en MASH F2-F3"]]) +
   '<span class="disc">Discriminador: cociente AST/ALT (&gt;2 alcohol; &lt;1 metabolico) + GGT.</span>'
   '<span class="ecoe">ECOE: "El cociente AST/ALT y la GGT me orientan entre origen alcoholico y metabolico."</span>',
   AG + ["hepatico", "transaminasas"])

# 12. Descompensacion de cirrosis
qa("Cirrosis descompensada: como se define y como se gradua?",
   tabla(["Forma de descompensacion", "Pista / manejo"],
         [["<b>Ascitis</b>", "paracentesis; restriccion de sodio + diureticos"],
          ["<b>Encefalopatia hepatica</b>", "asterixis; lactulosa + rifaximina + tratar precipitante"],
          ["<b>Sangrado variceal</b>", "endoscopia + vasoactivo + ATB profilactico"],
          ["<b>Ictericia</b>", "marcador de deterioro funcional"]]) +
   '<span class="disc">Gradacion del pronostico: MELD y Child-Pugh.</span>'
   '<span class="ecoe">ECOE: "Cualquiera de estas cuatro define descompensacion; estratifico con MELD y valoro trasplante."</span>',
   AG + ["hepatico", "cirrosis"])

# 13. Anemia por VCM
qa("Anemia clasificada por VCM: las tres rutas y su subclasificacion.",
   tabla(["VCM", "Grupo", "Causas / siguiente paso"],
         [["<b>&lt;80 (micro)</b>", "ferropenica (1a)", "buscar sangrado oculto (endoscopia+colonoscopia en adulto); tambien talasemia"],
          ["<b>80-100 (normo)</b>", "enf. cronica / ERC / hemolisis", "ferritina normal-alta; reticulocitos, LDH/bili"],
          ["<b>&gt;100 (macro)</b>", "megaloblastica vs no", "B12/folato (megalo) vs alcohol/hipotiroidismo/MDS (no megalo)"]]) +
   '<span class="disc">Discriminador inicial: el VCM. Reponer folato sin descartar B12 puede empeorar la neuropatia.</span>'
   '<span class="ecoe">ECOE: "El VCM divide la anemia en tres rutas; en adulto con ferropenia busco siempre sangrado digestivo."</span>',
   AG + ["hemato", "anemia_vcm"])

# 14. Artritis (mono vs poli)
qa("Artritis: como agrupar gota, AR, LES y PMR por patron articular y serologia.",
   tabla(["Entidad", "Patron articular", "Marcador / clave"],
         [["<b>Gota</b>", "monoartritis aguda (podagra 1a MTF)", "cristales de urato negativos a luz polarizada"],
          ["<b>Artritis reumatoide</b>", "poliartritis simetrica pequenas (MCF/IFP)", "anti-CCP (mas especifico que FR); rigidez &gt;1 h"],
          ["<b>LES</b>", "artralgias + multisistemico", "ANA, anti-dsDNA/anti-Sm; rash malar"],
          ["<b>PMR</b>", "rigidez cintura escapular/pelvica (&gt;50 a)", "VSG/PCR muy altas; respuesta a prednisona 15-20 mg"]]) +
   '<span class="redflag">PMR puede asociar arteritis temporal: cefalea, claudicacion mandibular, perdida visual subita -> prednisona 60 mg urgente.</span>'
   '<span class="ecoe">ECOE: "Clasifico la artritis por numero de articulaciones, simetria y serologia."</span>',
   AG + ["reumato", "artritis"])

# 15. Disnea aguda / patrones respiratorios
qa("Disnea aguda: agrupadores respiratorios y su escala/criterio.",
   tabla(["Cuadro", "Criterio / escala", "Pista de gravedad"],
         [["<b>EPOC exacerbado</b>", "Anthonisen (disnea + esputo + purulencia)", "ATB si 2-3 criterios"],
          ["<b>Asma severa</b>", "PEF &lt;50% del predicho", "torax silente, somnolencia, cianosis"],
          ["<b>TEP</b>", "Wells / Geneva + dimero D / angio-TC", "inestabilidad + disfuncion VD -> trombolisis"],
          ["<b>NAC</b>", "CURB-65", "decide ambulatorio vs hospital vs UCI"]]) +
   '<span class="disc">Cada patron tiene su escala propia: Anthonisen, PEF, Wells, CURB-65.</span>'
   '<span class="ecoe">ECOE: "Ante disnea aguda aplico la escala que corresponde al patron sospechado."</span>',
   AG + ["pulmonar", "disnea"])

# 16. Sindromes infecciosos graves
qa("Sindromes infecciosos graves del adulto: agrupadores y su criterio diagnostico.",
   tabla(["Sindrome", "Criterio", "Conducta"],
         [["<b>Sepsis / shock septico</b>", "qSOFA &ge;2 / SOFA; shock = vasopresor PAM &ge;65 + lactato &gt;2", "bundle hora-1 (Surviving Sepsis 2021)"],
          ["<b>Endocarditis</b>", "Duke modificados (hemocultivos + eco)", "hemocultivos seriados antes de ATB"],
          ["<b>Pielonefritis / ITU complicada</b>", "fiebre + punopercusion + leucocituria; complicada si DM/embarazo/sonda/varon", "urocultivo; IV si sepsis"]]) +
   '<span class="disc">Cada uno tiene su sistema: qSOFA/Sepsis-3, Duke, factores de complicacion en ITU.</span>'
   '<span class="ecoe">ECOE: "Identifico el foco y aplico el criterio formal (qSOFA, Duke) antes de iniciar antibiotico."</span>',
   AG + ["infecto", "infecciones_graves"])

# 17. Crisis suprarrenal aguda
qa("Crisis suprarrenal aguda: tetrada que la define y tratamiento inmediato.",
   tabla(["Componente", "Hallazgo"],
         [["Hemodinamia", "<b>hipotension refractaria a volumen</b>"],
          ["Glucosa", "hipoglucemia"],
          ["Sodio", "hiponatremia"],
          ["Potasio", "hiperkalemia"]]) +
   '<span class="disc">Contexto: estres en insuf. suprarrenal cronica o suspension brusca de esteroide.</span>'
   '<span class="redflag">Tratamiento: hidrocortisona 100 mg IV en bolo + 100 mg c/6 h + SF + glucosa; NO esperar cortisol.</span>'
   '<span class="ecoe">ECOE: "Sospecho crisis suprarrenal y administro hidrocortisona IV de inmediato."</span>',
   AG + ["endocrino", "crisis_suprarrenal"])

# ============================================================
# TIPO B - DISCRIMINADOR RAPIDO (parametros -> clasificacion)
# ============================================================
qa("FeNa &lt;1% + BUN/Cr &gt;20 + oliguria que responde a volumen. Que tipo de AKI?",
   '<b>AKI prerrenal</b> (hipoperfusion: deshidratacion, hemorragia, IC, sepsis).'
   '<span class="ecoe">ECOE: "Reanimo con cristaloides y corrijo la causa de hipoperfusion."</span>',
   DR + ["renal", "aki"])

qa("Glucosa &gt;600 + osmolaridad &gt;320 + alteracion mental, SIN cetonas ni acidosis, en adulto mayor con DM2. Diagnostico?",
   '<b>Estado hiperglucemico hiperosmolar (EHH)</b>.'
   '<span class="ecoe">ECOE: "Reposicion de volumen agresiva e insulina cuando la glucosa baje de 300."</span>',
   DR + ["endocrino", "ehh"])

qa("Glucosa &gt;250 + cetonas + pH &lt;7.3 + HCO3 &lt;18 + anion gap elevado. Diagnostico?",
   '<b>Cetoacidosis diabetica (CAD)</b>, mas frecuente en DM1.'
   '<span class="ecoe">ECOE: "Cristaloides + insulina IV + reposicion de potasio + busco el precipitante."</span>',
   DR + ["endocrino", "cad"])

qa("Proteinuria &gt;3.5 g/d + hipoalbuminemia + edema + estado de hipercoagulabilidad. Que sindrome?",
   '<b>Sindrome nefrotico</b> (contrasta con nefritico: hematuria con cilindros eritrocitarios + HTA + proteinuria &lt;3.5).'
   '<span class="ecoe">ECOE: "Cuadro nefrotico; refiero a nefrologia para biopsia."</span>',
   DR + ["renal", "glomerular"])

qa("VCM &gt;100 + neuropatia + glositis + atrofia gastrica. Tipo de anemia y causa?",
   '<b>Anemia macrocitica megaloblastica por deficit de B12</b>.'
   '<span class="redflag">No reponer folato aislado: puede empeorar la neuropatia por B12.</span>',
   DR + ["hemato", "macrocitica"])

qa("Elevacion del ST &ge;1 mm en 2 derivaciones contiguas + dolor isquemico. Clasificacion y conducta?",
   '<b>IAMCEST</b> -> reperfusion: ICP primaria &lt;90 min (door-to-balloon) o fibrinolisis &lt;120 min.'
   '<span class="ecoe">ECOE: "IAMCEST = sala de hemodinamia inmediata; doble antiagregacion + anticoagulacion."</span>',
   DR + ["cardio", "iamcest"])

# ============================================================
# EMPAQUETADO
# ============================================================
out = os.path.join(OUTPUT_DIR, "Medicina_Interna_Adulto_Integrador.apkg")
genanki.Package([deck]).write_to_file(out)
print(f"OK -> {out}")
print(f"TOTAL notas: {len(deck.notes)} (17 agrupadores + 6 discriminador rapido)")
