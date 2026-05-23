"""Generador de 4 subdecks Anki para ECOE de Medicina Interna.

Capa 1 - Reconocimiento de Patron Internista (Cloze)
Capa 2 - Exploracion Dirigida y Calculadoras (Cloze)
Capa 3 - Interpretacion de Estudios (Cloze)
Capa 4 - Manejo y Diagnostico Diferencial (Q&A)

Guias base: ACC/AHA 2017 HTA, AHA 2018 lipidos, ACC/AHA 2023 IC, ACC/AHA 2023 ACS,
ACC/AHA 2019 FA, ADA 2025, KDIGO 2024, AASLD, ATS/IDSA 2019, GOLD 2024, GINA 2024,
ACR 2020 gota, Surviving Sepsis 2021, USPSTF, UpToDate.

Filosofia: 3 grandes bloques en ECOE - urgencias vitales, abdomen+cardio+pulmon,
paciente cronico complejo con riesgo CV alto. El cronico complejo es ORO en ECOE.
Eje dominante = riesgo CV global -> priorizacion integral.
"""
import os
import genanki

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "output")
os.makedirs(OUTPUT_DIR, exist_ok=True)

MODEL_CLOZE_ID = 1607392319
MODEL_QA_ID = 1607392320

DECK_ID_C1 = 1465810910
DECK_ID_C2 = 1137569095
DECK_ID_C3 = 1306015269
DECK_ID_C4 = 1710703980

DECK_NAME_C1 = "Medicina Interna Adulto::Capa 1 - Reconocimiento de Patron Internista"
DECK_NAME_C2 = "Medicina Interna Adulto::Capa 2 - Exploracion Dirigida y Calculadoras"
DECK_NAME_C3 = "Medicina Interna Adulto::Capa 3 - Interpretacion de Estudios"
DECK_NAME_C4 = "Medicina Interna Adulto::Capa 4 - Manejo y Diagnostico Diferencial"

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
.redflag { color: #b91c1c; font-weight: 600; display: block; margin-top: 6px; }
.viva { color: #047857; display: block; margin-top: 6px; font-style: italic; }
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

BASE_TAGS = ["medicina_interna", "ecoe"]


def add_cloze(deck, text, extra, tags):
    deck.add_note(genanki.Note(model=model_cloze, fields=[text, extra], tags=BASE_TAGS + tags))


def add_qa(deck, front, back, tags):
    deck.add_note(genanki.Note(model=model_qa, fields=[front, back], tags=BASE_TAGS + tags))


# ============================================================
# CAPA 1 - RECONOCIMIENTO DE PATRON INTERNISTA (45 cloze)
# ============================================================
C1 = ["capa1", "reconocimiento"]

# --- PACIENTE CRONICO COMPLEJO (5) - eje ORO en ECOE
add_cloze(deck_c1,
    "Paciente 52 a + HTA + DM2 + tabaco 20 cig/d + alcohol diario + LDL 210 + HbA1c 6.6 + AST/ALT 70/55 + Hb 11.8 -> eje dominante = {{c1::riesgo cardiovascular global alto}}; prioridad = {{c2::estatina alta intensidad + IECA/ARA-II + manejo metabolico + cambios de estilo de vida}}",
    '<span class="redflag">El ECOE NO quiere 20 diagnosticos; quiere que detectes el eje dominante.</span>'
    '<span class="ecoe">ECOE: "Paciente con alto riesgo cardiovascular global; priorizo reduccion de riesgo con estatina alta intensidad, control estricto de PA con ARA-II, manejo metabolico y modificacion de habitos."</span>',
    C1 + ["cronico_complejo", "riesgo_cv"])

add_cloze(deck_c1,
    "Sindrome metabolico (NCEP-ATP III): {{c1::>=3 de 5 criterios}} -> {{c2::obesidad central (>102 cm varon / >88 cm mujer)}}, {{c3::TG >=150}}, {{c4::HDL &lt;40 varon / &lt;50 mujer}}, {{c5::PA >=130/85}}, {{c6::glucosa ayuno >=100}}",
    '<span class="ecoe">ECOE: "Cumple criterios de sindrome metabolico; alto riesgo CV y DM2."</span>',
    C1 + ["cronico_complejo", "sd_metabolico"])

add_cloze(deck_c1,
    "Relacion AST/ALT {{c1::>2}} con GGT elevada -> sugiere {{c2::hepatopatia alcoholica}}; relacion {{c3::&lt;1}} con ALT levemente elevada en obeso/DM -> {{c4::MASLD (esteatosis hepatica metabolica)}}",
    '<span class="contraste">MASLD es ahora el termino preferido (antes NAFLD); MASH = esteatohepatitis.</span>'
    '<span class="ecoe">ECOE: "Patron sugiere hepatopatia alcoholica vs MASLD; solicito serologias y USG hepatico."</span>',
    C1 + ["cronico_complejo", "transaminasas"])

add_cloze(deck_c1,
    "Anemia leve en adulto cronico complejo -> primero clasificar por {{c1::VCM}}: &lt;80 = {{c2::ferropenica (buscar sangrado oculto)}}; 80-100 = {{c3::enfermedad cronica/mixta}}; >100 = {{c4::B12/folato/alcohol/hipotiroidismo}}",
    '<span class="ecoe">ECOE: "Clasifico anemia por VCM, busco sangrado digestivo y deficits nutricionales."</span>',
    C1 + ["cronico_complejo", "anemia"])

add_cloze(deck_c1,
    "Prediabetes (ADA 2025): HbA1c {{c1::5.7-6.4%}} o glucosa ayuno {{c2::100-125 mg/dL}}; conducta = {{c3::cambios de estilo de vida + metformina}} si alto riesgo (IMC >35, &lt;60 a, antecedente diabetes gestacional)",
    '<span class="ecoe">ECOE: "Prediabetes; intervencion intensiva con dieta, ejercicio y consideracion de metformina."</span>',
    C1 + ["cronico_complejo", "prediabetes"])

# --- CARDIO (8)
add_cloze(deck_c1,
    "IC con FE reducida (FEr): FEVI {{c1::&lt;=40%}}; clinica = disnea + edema + ortopnea + {{c2::tercer ruido (S3, galope ventricular)}}; etiologia frecuente = {{c3::cardiopatia isquemica}}",
    '<span class="contraste">FEp (FEVI >=50%): mujer mayor con HTA cronica, S4, fisiopatologia distinta.</span>'
    '<span class="ecoe">ECOE: "IC con FE reducida; aplico los cuatro pilares (ARNI/IECA + BB + ARM + iSGLT2)."</span>',
    C1 + ["cardio", "ic"])

add_cloze(deck_c1,
    "IAMCEST: {{c1::elevacion del ST >=1 mm en 2 derivaciones contiguas}} (o >=2 mm V2-V3) o BRI nuevo + clinica isquemica -> reperfusion {{c2::ICP primaria &lt;90 min}} (door-to-balloon) o fibrinolisis {{c3::&lt;120 min}} si traslado largo",
    '<span class="redflag">Tiempo es musculo; reperfusion lo mas pronto posible.</span>'
    '<span class="ecoe">ECOE: "IAMCEST = sala de hemodinamia inmediata; doble antiagregacion + anticoagulacion."</span>',
    C1 + ["cardio", "iamcest"])

add_cloze(deck_c1,
    "IAMSEST: {{c1::troponina elevada}} + cambios ECG (depresion ST o T invertida) sin elevacion ST persistente; estratificar con {{c2::GRACE/TIMI}}; manejo invasivo {{c3::&lt;24 h}} si alto riesgo",
    '<span class="ecoe">ECOE: "IAMSEST de alto riesgo; cateterismo en menos de 24 h."</span>',
    C1 + ["cardio", "iamsest"])

add_cloze(deck_c1,
    "Fibrilacion auricular: pulso {{c1::irregularmente irregular}}; ECG con ausencia de {{c2::ondas P}} y RR variable; complicacion principal = {{c3::ictus cardioembolico}}",
    '<span class="ecoe">ECOE: "FA; calculo CHA2DS2-VASc para decidir anticoagulacion."</span>',
    C1 + ["cardio", "fa"])

add_cloze(deck_c1,
    "Crisis hipertensiva = PAS {{c1::>=180}} o PAD {{c2::>=120}}; clasificacion: {{c3::emergencia (con dano de organo blanco: encefalopatia, EAP, IAM, diseccion, eclampsia)}} vs {{c4::urgencia (sin dano agudo)}}",
    '<span class="contraste">Emergencia = IV inmediato en UCI; urgencia = VO ambulatorio con descenso gradual 24-48 h.</span>'
    '<span class="ecoe">ECOE: "Diferencio emergencia vs urgencia HTA por presencia de dano organico."</span>',
    C1 + ["cardio", "crisis_hta"])

add_cloze(deck_c1,
    "Estenosis aortica severa: triada {{c1::sincope}} + {{c2::angina}} + {{c3::disnea/IC}}; soplo {{c4::sistolico expulsivo}} en foco aortico irradiado a carotidas + pulso parvus et tardus",
    '<span class="redflag">Sincope con esfuerzo en EAo = indicacion de reemplazo valvular (SAVR/TAVR).</span>'
    '<span class="ecoe">ECOE: "EAo severa sintomatica; reemplazo valvular sin demora."</span>',
    C1 + ["cardio", "eao"])

add_cloze(deck_c1,
    "Insuficiencia mitral severa: soplo {{c1::holosistolico}} en {{c2::apex}} irradiado a {{c3::axila}}; cronica = sobrecarga volumen + dilatacion VI; aguda = EAP fulminante",
    '<span class="ecoe">ECOE: "Soplo holosistolico apical irradiado a axila; sospecho IM severa, eco urgente."</span>',
    C1 + ["cardio", "im"])

add_cloze(deck_c1,
    "Pericarditis aguda: dolor toracico {{c1::pleuritico}} que mejora al {{c2::inclinarse hacia adelante}}; ECG con elevacion ST {{c3::concava difusa}} + descenso del PR; auscultacion: {{c4::frote pericardico}}",
    '<span class="contraste">A diferencia de IAM: ST elevado en MULTIPLES territorios, no recipricidad.</span>'
    '<span class="ecoe">ECOE: "Pericarditis; AINE/colchicina, descarto tamponade con eco."</span>',
    C1 + ["cardio", "pericarditis"])

# --- ENDOCRINO (6)
add_cloze(deck_c1,
    "Cetoacidosis diabetica (CAD): glucosa {{c1::>250}} + {{c2::cetonas en sangre/orina}} + acidosis metabolica (pH {{c3::&lt;7.3}}, HCO3 {{c4::&lt;18}}) + {{c5::anion gap elevado}}",
    '<span class="contraste">Mas frecuente en DM1; precipitante: infeccion, no adherencia, IAM, embarazo.</span>'
    '<span class="ecoe">ECOE: "CAD; reanimacion con LR + insulina IV + reposicion de K + buscar precipitante."</span>',
    C1 + ["endocrino", "cad"])

add_cloze(deck_c1,
    "Estado hiperglucemico hiperosmolar (EHH): glucosa {{c1::>600}} + osmolaridad {{c2::>320}} + alteracion del estado mental + {{c3::SIN cetonas significativas}} ni acidosis franca; tipico en {{c4::adulto mayor con DM2}}",
    '<span class="contraste">A diferencia de CAD: insulinemia residual evita cetogenesis franca.</span>'
    '<span class="ecoe">ECOE: "EHH; reposicion volumen agresiva (deficit 8-10 L), insulina cuando glucosa &lt;300."</span>',
    C1 + ["endocrino", "ehh"])

add_cloze(deck_c1,
    "Tormenta tiroidea: hipertiroidismo grave + {{c1::fiebre >=38.5}} + {{c2::taquicardia/FA con respuesta rapida}} + {{c3::alteracion del estado mental/agitacion}} + falla multiorganica; escala de {{c4::Burch-Wartofsky}}",
    '<span class="redflag">Mortalidad alta sin tratamiento (>20%).</span>'
    '<span class="ecoe">ECOE: "Tormenta tiroidea; propranolol + tionamida + yodo (1 h despues) + corticoide + control de precipitante."</span>',
    C1 + ["endocrino", "tormenta"])

add_cloze(deck_c1,
    "Coma mixedematoso: {{c1::hipotermia}} + {{c2::hipoventilacion (hipercapnia)}} + bradicardia + alteracion mental + edema sin fovea; TSH {{c3::muy elevada}} con T4L baja",
    '<span class="redflag">Tratamiento empirico con levotiroxina IV + hidrocortisona; mortalidad alta.</span>'
    '<span class="ecoe">ECOE: "Coma mixedematoso; UCI + levotiroxina IV + hidrocortisona (descarto insuf suprarrenal asociada)."</span>',
    C1 + ["endocrino", "mixedema"])

add_cloze(deck_c1,
    "Crisis suprarrenal aguda: {{c1::hipotension refractaria a volumen}} + {{c2::hipoglucemia}} + {{c3::hiponatremia}} + {{c4::hiperkalemia}}; tratamiento: {{c5::hidrocortisona 100 mg IV bolo + 100 mg IV c/6 h}} + SF + glucosa",
    '<span class="contraste">Sospechar en estres en paciente con insuf suprarrenal cronica o suspension brusca de esteroide cronico.</span>'
    '<span class="ecoe">ECOE: "Crisis suprarrenal; hidrocortisona IV YA, no esperar cortisol."</span>',
    C1 + ["endocrino", "crisis_suprarrenal"])

add_cloze(deck_c1,
    "Hiperkalemia con cambios ECG: {{c1::T picudas}} -> {{c2::QRS ancho}} -> {{c3::ondas sinusoidales}} -> paro; manejo: {{c4::gluconato de calcio (estabiliza membrana) + insulina/glucosa + beta2 + bicarbonato + diuretico/resina/dialisis}}",
    '<span class="contraste">HipoK: T aplanada + ondas U + QT largo + arritmias (riesgo torsade).</span>'
    '<span class="ecoe">ECOE: "HiperK con cambios ECG; gluconato de calcio inmediato + medidas de redistribucion."</span>',
    C1 + ["endocrino", "potasio"])

# --- RENAL (4)
add_cloze(deck_c1,
    "AKI prerrenal: {{c1::BUN/Cr >20}}, {{c2::FeNa &lt;1%}}, oliguria; etiologias = {{c3::deshidratacion, hemorragia, IC, sepsis (hipoperfusion)}}; respuesta a {{c4::reposicion de volumen}}",
    '<span class="ecoe">ECOE: "AKI prerrenal; reanimo con cristaloides y ajusto causa subyacente."</span>',
    C1 + ["renal", "aki"])

add_cloze(deck_c1,
    "AKI intrinseca por NTA: {{c1::FeNa >2%}}, sedimento con {{c2::cilindros granulosos marrones}}; causas = {{c3::isquemia prolongada, nefrotoxinas (aminoglucosidos, contraste, AINE, anfotericina)}}",
    '<span class="contraste">Glomerulonefritis: HTA + hematuria con cilindros eritrocitarios + proteinuria nefrotica/nefritica.</span>'
    '<span class="ecoe">ECOE: "NTA isquemica/toxica; soporte, retirar nefrotoxinas, considerar dialisis si criterios."</span>',
    C1 + ["renal", "nta"])

add_cloze(deck_c1,
    "AKI postrenal: {{c1::anuria subita}} (obstruccion completa bilateral) + {{c2::hidronefrosis en USG}}; causas comunes en adulto: {{c3::HBP, neoplasia pelvica, litiasis bilateral, fibrosis retroperitoneal}}",
    '<span class="ecoe">ECOE: "AKI postrenal; sonda Foley o nefrostomia segun nivel de obstruccion."</span>',
    C1 + ["renal", "postrenal"])

add_cloze(deck_c1,
    "Sindrome nefrotico: {{c1::proteinuria >3.5 g/d}} + {{c2::hipoalbuminemia}} + {{c3::edema}} + dislipidemia + {{c4::estado de hipercoagulabilidad}}; nefritico: {{c5::hematuria con cilindros eritrocitarios + HTA + AKI + proteinuria &lt;3.5}}",
    '<span class="ecoe">ECOE: "Cuadro nefrotico vs nefritico; refiero a nefrologia para biopsia."</span>',
    C1 + ["renal", "glomerular"])

# --- HEPATICO (4)
add_cloze(deck_c1,
    "Cirrosis descompensada se define por aparicion de {{c1::ascitis}}, {{c2::encefalopatia hepatica}}, {{c3::sangrado variceal}} o {{c4::ictericia}}; gradacion = MELD/Child-Pugh",
    '<span class="ecoe">ECOE: "Cirrosis descompensada; estratifico con MELD y evaluo trasplante."</span>',
    C1 + ["hepatico", "cirrosis"])

add_cloze(deck_c1,
    "Encefalopatia hepatica: {{c1::asterixis (flapping)}} + alteracion del estado mental + factor {{c2::precipitante (sangrado digestivo, infeccion, hipoK, estrenimiento, sedantes, transgresion proteica)}}",
    '<span class="ecoe">ECOE: "Encefalopatia hepatica; lactulosa + rifaximina + identifico precipitante."</span>',
    C1 + ["hepatico", "encefalopatia"])

add_cloze(deck_c1,
    "MASLD/esteatosis hepatica metabolica: {{c1::AST/ALT &lt;1}} + ALT levemente elevada + obesidad/DM/dislipidemia/sd metabolico; tratamiento = {{c2::perdida de peso 7-10%}} + control de comorbilidades",
    '<span class="contraste">Antes llamada NAFLD; MASH = esteatohepatitis (con inflamacion + fibrosis).</span>'
    '<span class="ecoe">ECOE: "MASLD; perdida de peso, control HTA/DM/dislipidemia, considero resmetirom en MASH F2-F3."</span>',
    C1 + ["hepatico", "masld"])

add_cloze(deck_c1,
    "Hepatitis alcoholica: {{c1::AST/ALT >2}} + GGT alta + fiebre + ictericia + hepatomegalia dolorosa; severidad: {{c2::Maddrey discriminant function (mDF) >=32}} = corticoide",
    '<span class="ecoe">ECOE: "Hepatitis alcoholica grave; corticoide si Maddrey >=32 y descarto infeccion."</span>',
    C1 + ["hepatico", "alcoholica"])

# --- HEMATO (3)
add_cloze(deck_c1,
    "Anemia microcitica (VCM {{c1::&lt;80}}): primero pensar {{c2::ferropenica}} -> buscar {{c3::sangrado oculto digestivo (endoscopia + colonoscopia obligatoria en adulto)}}, malabsorcion, menstruacion",
    '<span class="contraste">Otras micro: talasemia (electroforesis), anemia sideroblastica, anemia de enf cronica avanzada.</span>'
    '<span class="ecoe">ECOE: "Anemia ferropenica en adulto; obligo estudio endoscopico para buscar fuente."</span>',
    C1 + ["hemato", "ferropenica"])

add_cloze(deck_c1,
    "Anemia normocitica (VCM 80-100): considerar {{c1::anemia de enfermedad cronica}} (ferritina {{c2::normal/alta}}, hierro bajo, saturacion baja), anemia hemolitica, aplasia medular, ERC con deficit EPO",
    '<span class="ecoe">ECOE: "Anemia normocitica; perfil ferrico, reticulocitos, LDH/bili para descartar hemolisis."</span>',
    C1 + ["hemato", "cronica"])

add_cloze(deck_c1,
    "Anemia macrocitica (VCM {{c1::>100}}): {{c2::megaloblastica (B12 o folato)}} vs no-megaloblastica ({{c3::alcohol, hipotiroidismo, MDS, farmacos}}); B12 + neuropatia + glositis + atrofia gastrica",
    '<span class="contraste">Reponer folato sin descartar B12 puede empeorar la neuropatia por B12.</span>'
    '<span class="ecoe">ECOE: "Macrocitosis; pido B12, folato, TSH y reviso consumo de alcohol."</span>',
    C1 + ["hemato", "macrocitica"])

# --- REUMATO (4)
add_cloze(deck_c1,
    "Gota aguda: {{c1::monoartritis aguda eritematosa muy dolorosa}}, {{c2::podagra (1a MTF)}} clasica; factores precipitantes: {{c3::alcohol (cerveza), carne roja/mariscos, diureticos tiazidicos, deshidratacion}}",
    '<span class="contraste">Confirmacion: cristales de urato monosodico negativos con luz polarizada en liquido sinovial.</span>'
    '<span class="ecoe">ECOE: "Gota aguda; AINE/colchicina/corticoide intra-articular + alopurinol despues."</span>',
    C1 + ["reumato", "gota"])

add_cloze(deck_c1,
    "Artritis reumatoide: {{c1::poliartritis simetrica}} de pequenas articulaciones (MCF, IFP, munecas) + {{c2::rigidez matutina >1 h}} + {{c3::FR/anti-CCP positivos}} + erosiones radiograficas",
    '<span class="contraste">Anti-CCP es mas especifica que FR.</span>'
    '<span class="ecoe">ECOE: "AR; metotrexato primera linea + AINE; biologico si refractaria."</span>',
    C1 + ["reumato", "ar"])

add_cloze(deck_c1,
    "LES: mujer joven + {{c1::rash malar en alas de mariposa}} + fotosensibilidad + artralgias + serositis + {{c2::ANA positivo}} + {{c3::anti-dsDNA / anti-Sm}} + nefropatia lupica",
    '<span class="contraste">Criterios EULAR/ACR 2019; afectacion renal y SNC marcan pronostico.</span>'
    '<span class="ecoe">ECOE: "LES; refiero a reumatologia, hidroxicloroquina base, busco afectacion organica."</span>',
    C1 + ["reumato", "les"])

add_cloze(deck_c1,
    "Polimialgia reumatica: paciente {{c1::>50 a}} + dolor + rigidez matutina en {{c2::cintura escapular y pelvica}} + VSG/PCR {{c3::muy elevadas}} + respuesta dramatica a {{c4::prednisona 15-20 mg/d}}",
    '<span class="redflag">Asociacion con arteritis temporal (gigantocelular): cefalea temporal, claudicacion mandibular, perdida visual subita -> prednisona 60 mg/d urgente + biopsia.</span>'
    '<span class="ecoe">ECOE: "PMR; prednisona dosis bajas; vigilo sintomas de arteritis temporal."</span>',
    C1 + ["reumato", "pmr"])

# --- PULMONAR (4)
add_cloze(deck_c1,
    "EPOC exacerbado (criterios Anthonisen): {{c1::aumento de disnea}} + {{c2::aumento de esputo}} + {{c3::esputo purulento}}; mas usado: cualquier empeoramiento que requiera cambio en tratamiento basal",
    '<span class="ecoe">ECOE: "EPOC exacerbado; broncodilatador + corticoide sistemico + ATB si criterios Anthonisen 2-3."</span>',
    C1 + ["pulmonar", "epoc"])

add_cloze(deck_c1,
    "Asma exacerbacion severa: {{c1::FR alta + uso de musculos accesorios + sibilancias intensas}}; signos de gravedad extrema: {{c2::torax silente, somnolencia, cianosis, PEF &lt;50% del predicho}}",
    '<span class="redflag">Torax silente = obstruccion severisima, riesgo de paro respiratorio.</span>'
    '<span class="ecoe">ECOE: "Asma exacerbacion severa; SABA + corticoide sistemico + magnesio IV si refractaria."</span>',
    C1 + ["pulmonar", "asma"])

add_cloze(deck_c1,
    "TEP: {{c1::disnea subita}} + {{c2::dolor pleuritico}} + taquicardia + a veces hemoptisis; factores de riesgo (Virchow): {{c3::inmovilizacion, cirugia, neoplasia, embarazo, ACO, trombofilia}}; Wells/Geneva para probabilidad",
    '<span class="redflag">TEP masivo: inestabilidad hemodinamica + disfuncion VD = trombolisis.</span>'
    '<span class="ecoe">ECOE: "Sospecho TEP; calculo Wells, dimero D si baja prob, angio-TC si alta o dimero positivo."</span>',
    C1 + ["pulmonar", "tep"])

add_cloze(deck_c1,
    "NAC: tos productiva + fiebre + dolor pleuritico + {{c1::crepitos focales}} + consolidacion radiografica; severidad con {{c2::CURB-65}}: Confusion, Urea >19, FR >=30, PA sistolica &lt;90 o diastolica &lt;=60, edad >=65",
    '<span class="ecoe">ECOE: "Aplico CURB-65 para decidir ambulatorio vs hospital vs UCI."</span>',
    C1 + ["pulmonar", "nac"])

# --- INFECTO (4)
add_cloze(deck_c1,
    "Endocarditis infecciosa: {{c1::fiebre persistente}} + {{c2::soplo nuevo o cambiante}} + estigmas embolicos ({{c3::Janeway, Osler, Roth, hemorragias en astilla}}); criterios diagnosticos = {{c4::Duke modificados}}",
    '<span class="contraste">Mayores: hemocultivos persistentemente positivos + eco con vegetacion. Menores: factor predisponente, fiebre, fenomenos vasculares/inmunologicos, cultivo menor.</span>'
    '<span class="ecoe">ECOE: "Sospecho EI; hemocultivos seriados antes de ATB y eco transtoracica/transesofagica."</span>',
    C1 + ["infecto", "endocarditis"])

add_cloze(deck_c1,
    "Pielonefritis aguda: {{c1::fiebre + escalofrios}} + {{c2::dolor lumbar/punopercusion positiva}} + sintomas urinarios bajos + {{c3::leucocituria + bacteriuria + cilindros leucocitarios}}",
    '<span class="contraste">E. coli es el agente mas frecuente en comunidad.</span>'
    '<span class="ecoe">ECOE: "PNA; hospitalizar si sepsis/intolerancia oral; ceftriaxona o quinolona IV."</span>',
    C1 + ["infecto", "pna"])

add_cloze(deck_c1,
    "ITU complicada: ITU + uno o mas factores de riesgo: {{c1::sexo masculino}}, {{c2::embarazo}}, {{c3::DM o inmunosupresion}}, sonda vesical, anomalia urinaria/urolitiasis, instrumentacion reciente",
    '<span class="ecoe">ECOE: "ITU complicada; urocultivo obligatorio y tratamiento mas prolongado."</span>',
    C1 + ["infecto", "itu_complicada"])

add_cloze(deck_c1,
    "Sepsis (Sepsis-3): sospecha de infeccion + {{c1::qSOFA >=2}} (FR>=22, PAS&lt;=100, alt mental) o disfuncion organica (SOFA); shock septico = sepsis + {{c2::vasopresor para PAM >=65}} + {{c3::lactato >2 pese a reanimacion adecuada}}",
    '<span class="ecoe">ECOE: "Activo bundle hora-1 Surviving Sepsis 2021."</span>',
    C1 + ["infecto", "sepsis"])

# --- ESPECIALES (3)
add_cloze(deck_c1,
    "Hipertiroidismo de Graves: {{c1::bocio difuso}} + {{c2::oftalmopatia (proptosis)}} + dermopatia (mixedema pretibial) + TSH {{c3::suprimida}} + T4L alta + {{c4::TRAb positivos}}",
    '<span class="ecoe">ECOE: "Graves; tionamida (metimazol) + betabloqueador; valoro yodo radiactivo o cirugia."</span>',
    C1 + ["endocrino", "graves"])

add_cloze(deck_c1,
    "Hipotiroidismo primario: fatiga + intolerancia al frio + ganancia de peso + bradicardia + piel seca + estrenimiento + bradipsiquia; TSH {{c1::elevada}} + T4L {{c2::baja}}",
    '<span class="contraste">Subclinico: TSH alta con T4L normal; tratar si >10 mUI/L o sintomas/bocio.</span>'
    '<span class="ecoe">ECOE: "Hipotiroidismo primario; levotiroxina 1.6 mcg/kg/d, ajuste por TSH a 6-8 sem."</span>',
    C1 + ["endocrino", "hipotiroidismo"])

add_cloze(deck_c1,
    "Hiponatremia sintomatica (Na {{c1::&lt;125}} con sintomas neurologicos: nausea, cefalea, convulsion, coma) -> {{c2::salino hipertonico al 3%}} 100 mL en 10 min, repetir hasta 3 veces; correccion {{c3::&lt;=8-10 mEq en 24 h}} (riesgo de mielinolisis pontina)",
    '<span class="ecoe">ECOE: "Hiponatremia sintomatica; salino al 3% controlado, no corregir mas de 10 mEq/24 h."</span>',
    C1 + ["electrolitos", "hipoNa"])


# ============================================================
# CAPA 2 - EXPLORACION DIRIGIDA Y CALCULADORAS (35 cloze)
# ============================================================
C2 = ["capa2", "exploracion"]

# --- CARDIOVASCULAR (8)
add_cloze(deck_c2,
    "Medir PA en {{c1::ambos brazos}}; diferencia {{c2::>15-20 mmHg}} entre brazos sugiere {{c3::vasculopatia (subclavia, diseccion aortica, coartacion)}}",
    '<span class="ecoe">ECOE: "Mido PA en ambos brazos; documento diferencia significativa."</span>',
    C2 + ["cv", "pa"])

add_cloze(deck_c2,
    "Pulsos perifericos a explorar: {{c1::carotideos, radiales, femorales, popliteos, tibiales posteriores y pedios}}; gradacion {{c2::0 (ausente), 1+ (debil), 2+ (normal), 3+ (aumentado)}}",
    '<span class="ecoe">ECOE: "Exploro pulsos en seis territorios, comparo simetria."</span>',
    C2 + ["cv", "pulsos"])

add_cloze(deck_c2,
    "Focos de auscultacion cardiaca: {{c1::aortico (2do EIC derecho)}}, {{c2::pulmonar (2do EIC izquierdo)}}, {{c3::tricuspideo (apendice xifoideo)}}, {{c4::mitral/apical (5to EIC linea medioclavicular)}}",
    '<span class="ecoe">ECOE: "Ausculto los cuatro focos, identifico cambios con maniobras."</span>',
    C2 + ["cv", "focos"])

add_cloze(deck_c2,
    "{{c1::Tercer ruido (S3)}}: galope ventricular, sugiere {{c2::IC con FE reducida / sobrecarga de volumen}}; {{c3::cuarto ruido (S4)}}: galope auricular, indica {{c4::cardiopatia hipertensiva / disfuncion diastolica}}",
    '<span class="ecoe">ECOE: "S3 patologico en adulto = IC sistolica."</span>',
    C2 + ["cv", "ruidos"])

add_cloze(deck_c2,
    "Ingurgitacion yugular: medir desde {{c1::angulo esternal (Louis)}}; altura >{{c2::3 cm}} sobre el angulo + paciente a 30-45 grados = elevada -> sugiere {{c3::sobrecarga de volumen / IC derecha / tamponade}}",
    '<span class="ecoe">ECOE: "PVY elevada; sugiere insuficiencia cardiaca derecha."</span>',
    C2 + ["cv", "pvy"])

add_cloze(deck_c2,
    "Edemas perifericos: gradacion {{c1::+1 (apenas perceptible)}} a {{c2::+4 (profundo, lento)}}; bilateral sugiere {{c3::IC, ERC, hepatopatia, hipoalbuminemia, CCB}}; unilateral = {{c4::TVP, celulitis, linfedema}}",
    '<span class="ecoe">ECOE: "Edemas bilaterales con fovea +2; sugiere etiologia sistemica."</span>',
    C2 + ["cv", "edemas"])

add_cloze(deck_c2,
    "Fondo de ojo en HTA cronica - Keith-Wagener: I = {{c1::estrechez arteriolar}}; II = {{c2::cruces AV (Salus, Gunn)}}; III = {{c3::exudados algodonosos + hemorragias en llama}}; IV = {{c4::papiledema (emergencia HTA)}}",
    '<span class="ecoe">ECOE: "Realizo o solicito fondo de ojo; documento grado Keith-Wagener."</span>',
    C2 + ["cv", "fondo_ojo"])

add_cloze(deck_c2,
    "Reflujo hepatoyugular: comprimir hipocondrio derecho 30-60 seg con paciente a 45 grados; PVY {{c1::sube >=3 cm}} y se mantiene = positivo -> {{c2::IC derecha / sobrecarga de VD}}",
    '<span class="ecoe">ECOE: "Reflujo hepatoyugular positivo, signo de IC derecha."</span>',
    C2 + ["cv", "hepatoyugular"])

# --- RESPIRATORIO (3)
add_cloze(deck_c2,
    "Auscultacion respiratoria: {{c1::sibilancias}} (obstruccion bronquial: asma, EPOC); {{c2::crepitos finos}} en bases (intersticial, IC); {{c3::roncus}} (secreciones gruesas); {{c4::frote pleural}} (pleuritis)",
    '<span class="ecoe">ECOE: "Ausculto los seis campos; identifico el tipo de ruido."</span>',
    C2 + ["respi", "auscultacion"])

add_cloze(deck_c2,
    "Sindrome de condensacion: {{c1::matidez a la percusion}} + {{c2::aumento del fremito vocal}} + {{c3::broncofonia, egofonia, pectoriloquia}} + {{c4::soplo tubario y crepitos}}",
    '<span class="ecoe">ECOE: "Hallazgos de condensacion en hemitorax inferior derecho; sospecho neumonia."</span>',
    C2 + ["respi", "condensacion"])

add_cloze(deck_c2,
    "Derrame pleural: {{c1::matidez}} + {{c2::abolicion del fremito vocal}} + {{c3::abolicion del murmullo vesicular}} + soplo espirativo en el limite superior",
    '<span class="contraste">Neumotorax: timpanismo + abolicion de fremito + abolicion de murmullo + ausencia de soplo.</span>'
    '<span class="ecoe">ECOE: "Patron de derrame pleural; toracocentesis diagnostica."</span>',
    C2 + ["respi", "derrame"])

# --- ABDOMEN HEPATICO (4)
add_cloze(deck_c2,
    "Estigmas de hepatopatia cronica: {{c1::aranas vasculares}} (telangiectasias), {{c2::eritema palmar}}, {{c3::ginecomastia}}, hipertrofia parotidea, contractura de {{c4::Dupuytren}}, atrofia testicular, vello pubico femenino",
    '<span class="ecoe">ECOE: "Estigmas de hepatopatia cronica; busco causa (OH, viral, MASLD)."</span>',
    C2 + ["abd", "estigmas"])

add_cloze(deck_c2,
    "Exploracion de ascitis: {{c1::matidez cambiante}} (desplazamiento de matidez al cambio de posicion); {{c2::oleada ascitica}} (transmision de onda al percutir lado contrario); {{c3::signo del tempano}} (organomegalia flotante)",
    '<span class="ecoe">ECOE: "Confirmo ascitis con matidez cambiante; paracentesis si nueva o sintomatica."</span>',
    C2 + ["abd", "ascitis"])

add_cloze(deck_c2,
    "Hepatomegalia significativa: borde hepatico palpable {{c1::>2 cm bajo reborde costal}} en linea medioclavicular o {{c2::altura hepatica >12 cm}} por percusion",
    '<span class="ecoe">ECOE: "Hepatomegalia; describo borde, consistencia, dolor."</span>',
    C2 + ["abd", "hepatomegalia"])

add_cloze(deck_c2,
    "Esplenomegalia: bazo {{c1::no debe palparse normalmente}}; cuando palpable bajo reborde costal izquierdo = significativa; causas: {{c2::hipertension portal, hemopatias, infecciones (mononucleosis, malaria)}}",
    '<span class="ecoe">ECOE: "Esplenomegalia palpable; sospecho hipertension portal o hematologica."</span>',
    C2 + ["abd", "bazo"])

# --- PIE DIABETICO (4)
add_cloze(deck_c2,
    "Monofilamento de {{c1::Semmes-Weinstein 10 g}}: aplicar en {{c2::cuatro puntos plantares}} (pulpejo 1er ortejo, 1a, 3a y 5a cabeza metatarsal); >=1 punto sin percibir = neuropatia",
    '<span class="ecoe">ECOE: "Aplico monofilamento 10 g en cuatro puntos plantares."</span>',
    C2 + ["pie_dm", "monofilamento"])

add_cloze(deck_c2,
    "Diapason {{c1::128 Hz}} en {{c2::maleolo medial}} o cabeza del 1er metatarsiano; tiempo de percepcion &lt;{{c3::10 segundos}} = neuropatia",
    '<span class="ecoe">ECOE: "Vibracion con diapason 128 Hz en maleolos."</span>',
    C2 + ["pie_dm", "vibracion"])

add_cloze(deck_c2,
    "Pulsos {{c1::pedios y tibiales posteriores}}: clave para evaluar {{c2::perfusion}}; ausencia o disminucion + neuropatia = pie de alto riesgo; complementar con {{c3::indice tobillo-brazo (ITB)}} &lt;0.9 = EAP",
    '<span class="ecoe">ECOE: "Palpo pulsos pedios y tibiales; calculo ITB si sospecha EAP."</span>',
    C2 + ["pie_dm", "perfusion"])

add_cloze(deck_c2,
    "Inspeccion del pie diabetico busca: {{c1::deformidades (Charcot, dedos en martillo)}}, {{c2::callosidades}}, {{c3::ulceras (Wagner I-V)}}, espacios interdigitales (micosis), color, temperatura, edema",
    '<span class="ecoe">ECOE: "Inspecciono pie completo, descalzo, espacios interdigitales."</span>',
    C2 + ["pie_dm", "inspeccion"])

# --- REUMATO (3)
add_cloze(deck_c2,
    "DAS28 (actividad AR): cuenta de articulaciones {{c1::dolorosas + tumefactas (de 28)}} + {{c2::VSG o PCR}} + EVA del paciente; {{c3::&lt;2.6 remision}}; 2.6-3.2 baja; 3.2-5.1 moderada; >5.1 alta",
    '<span class="ecoe">ECOE: "DAS28 estratifica actividad de AR; gua escalada terapeutica."</span>',
    C2 + ["reumato", "das28"])

add_cloze(deck_c2,
    "AR avanzada: {{c1::desviacion cubital de los dedos}}, {{c2::deformidad en cuello de cisne}}, {{c3::deformidad en boutonniere}}, dedo en martillo, atrofia muscular interoseo",
    '<span class="contraste">A diferencia de osteoartritis: AR afecta MCF/IFP, no IFD (los nodulos de Heberden son de OA, no AR).</span>'
    '<span class="ecoe">ECOE: "Manos con patron de AR; sin nodulos de Heberden."</span>',
    C2 + ["reumato", "ar"])

add_cloze(deck_c2,
    "Gota: buscar {{c1::tofos}} en helix de la oreja, codo (bursa olecraneana), tendon de Aquiles, articulacion MTF; confirmacion definitiva: {{c2::aspiracion de liquido sinovial}} con cristales {{c3::birrefringencia negativa}} bajo luz polarizada",
    '<span class="ecoe">ECOE: "Busco tofos; artrocentesis si no se ha hecho previamente."</span>',
    C2 + ["reumato", "gota"])

# --- CALCULADORAS (10)
add_cloze(deck_c2,
    "ASCVD Risk PCE (ACC/AHA): variables = {{c1::edad, sexo, raza, PA sistolica + tratamiento, colesterol total y HDL, DM, tabaquismo}}; categorias: bajo &lt;5%, limite 5-7.5%, intermedio {{c2::7.5-19.9%}}, alto {{c3::>=20%}}",
    '<span class="ecoe">ECOE: "Calculo ASCVD a 10 anos; guia decision de estatina."</span>',
    C2 + ["calculadoras", "ascvd"])

add_cloze(deck_c2,
    "CHA2DS2-VASc (FA, anticoagulacion): {{c1::C}}ardiac failure, {{c2::H}}ypertension, {{c3::A}}ge >=75 (2 pts), {{c4::D}}M, {{c5::S}}troke previo (2 pts), {{c6::V}}ascular dx, {{c7::A}}ge 65-74, {{c8::Sc - sexo femenino}}; anticoagular si {{c9::>=2 varon o >=3 mujer}}",
    '<span class="ecoe">ECOE: "Calculo CHA2DS2-VASc; indico DOAC si >=2 (varon)."</span>',
    C2 + ["calculadoras", "chads"])

add_cloze(deck_c2,
    "HAS-BLED (sangrado en anticoagulado): {{c1::H}}TA no controlada, {{c2::A}}brnormal renal/hepatica, {{c3::S}}troke, {{c4::B}}leeding, {{c5::L}}abil INR, {{c6::E}}lderly >65, {{c7::D}}rugs/alcohol; >=3 = alto riesgo (no contraindica, intensifica vigilancia)",
    '<span class="ecoe">ECOE: "HAS-BLED no contraindica; modifica factores corregibles."</span>',
    C2 + ["calculadoras", "hasbled"])

add_cloze(deck_c2,
    "MELD score: {{c1::creatinina + bilirrubina + INR}} (+ sodio en MELD-Na); predice mortalidad a 3 meses en cirrosis; >=15 = considerar {{c2::trasplante hepatico}}",
    '<span class="ecoe">ECOE: "MELD para priorizar trasplante."</span>',
    C2 + ["calculadoras", "meld"])

add_cloze(deck_c2,
    "Child-Pugh: {{c1::Bilirrubina + Albumina + INR + Ascitis + Encefalopatia}}; clases A (5-6), B (7-9), C (10-15); estima mortalidad postoperatoria en cirrotico",
    '<span class="ecoe">ECOE: "Child-Pugh para clasificar severidad de cirrosis."</span>',
    C2 + ["calculadoras", "child"])

add_cloze(deck_c2,
    "CURB-65 (NAC): {{c1::C}}onfusion + urea >{{c2::19 mg/dL}} (BUN >7 mmol/L) + FR >={{c3::30}} + PA sistolica &lt;90 o diastolica &lt;=60 + edad >={{c4::65}}; 0-1 ambulatorio, 2 hospital, >=3 UCI",
    '<span class="ecoe">ECOE: "CURB-65 = 3, indico hospitalizacion en planta o UCI."</span>',
    C2 + ["calculadoras", "curb"])

add_cloze(deck_c2,
    "Wells TEP: clinica TVP (3), TEP mas probable (3), FC >100 (1.5), inmovilizacion/cirugia (1.5), TEP/TVP previo (1.5), hemoptisis (1), cancer (1); {{c1::&lt;=4 = poco probable -> dimero D}}, {{c2::>4 = probable -> angio-TC}}",
    '<span class="ecoe">ECOE: "Wells &lt;=4 + dimero negativo descarta TEP."</span>',
    C2 + ["calculadoras", "wells_tep"])

add_cloze(deck_c2,
    "Wells TVP: cancer activo, paralisis/inmovilizacion, encamamiento >3d/cirugia mayor, dolor a lo largo de vena, edema completo MI, pantorrilla 3 cm > contralateral, edema con fovea, venas superficiales colaterales, TVP previa, alternativa probable (-2); {{c1::>=2 = probable}}",
    '<span class="ecoe">ECOE: "Wells TVP >=2 + dimero positivo -> USG Doppler."</span>',
    C2 + ["calculadoras", "wells_tvp"])

add_cloze(deck_c2,
    "GRACE score (ACS): predice mortalidad intrahospitalaria y a 6 meses; variables = {{c1::edad, FC, PA, Killip, creatinina, paro, desviacion ST, biomarcadores}}; alto riesgo guia {{c2::estrategia invasiva temprana}}",
    '<span class="ecoe">ECOE: "GRACE >140 -> cateterismo &lt;24 h en SCASEST."</span>',
    C2 + ["calculadoras", "grace"])

add_cloze(deck_c2,
    "TIMI score (SCASEST): {{c1::edad >=65, >=3 factores RCV, estenosis coronaria previa, ASA en 7 d, angina severa reciente, biomarcadores positivos, desviacion ST >=0.5 mm}}; >=3 = riesgo intermedio-alto",
    '<span class="ecoe">ECOE: "TIMI guia intensidad terapeutica en SCASEST."</span>',
    C2 + ["calculadoras", "timi"])

# --- FRASES ECOE (3)
add_cloze(deck_c2,
    "Frase ECOE clave (paciente cronico complejo): {{c1::Paciente con alto riesgo cardiovascular global}}",
    '<span class="ecoe">ECOE: Reconoces el eje dominante - sumas puntos por juicio clinico integral.</span>',
    C2 + ["frases"])

add_cloze(deck_c2,
    "Frase ECOE clave: {{c1::Priorizare reduccion de riesgo mediante estatina de alta intensidad, control estricto de presion con ARA-II, manejo metabolico y modificaciones del estilo de vida}}",
    '<span class="ecoe">ECOE: Demuestra orden de prioridad terapeutica, no listado caotico.</span>',
    C2 + ["frases"])

add_cloze(deck_c2,
    "Frase ECOE clave: {{c1::Programare consulta de seguimiento estructurado y solicitare laboratorios de control en 4-6 semanas}}",
    '<span class="ecoe">ECOE: Demuestra continuidad de cuidados.</span>',
    C2 + ["frases"])


# ============================================================
# CAPA 3 - INTERPRETACION DE ESTUDIOS (40 cloze)
# ============================================================
C3 = ["capa3", "estudios"]

# --- LIPIDOS Y RCV (5)
add_cloze(deck_c3,
    "LDL {{c1::>=190 mg/dL}} = indicacion automatica de {{c2::estatina de alta intensidad}} sin importar otro factor (AHA 2018)",
    '<span class="contraste">Alta intensidad: atorvastatina 40-80 mg, rosuvastatina 20-40 mg.</span>'
    '<span class="ecoe">ECOE: "LDL >=190 = estatina alta intensidad obligada."</span>',
    C3 + ["lipidos", "ldl"])

add_cloze(deck_c3,
    "Metas LDL por categoria de riesgo (AHA 2018): ASCVD establecido muy alto riesgo {{c1::&lt;55-70}}; ASCVD secundaria {{c2::&lt;70}}; alto riesgo primario (DM, ASCVD calculado >=20%) {{c3::reduccion >=50% del basal}}",
    '<span class="ecoe">ECOE: "Defino meta LDL por categoria de riesgo."</span>',
    C3 + ["lipidos", "metas"])

add_cloze(deck_c3,
    "Trigliceridos >={{c1::500 mg/dL}} = riesgo de {{c2::pancreatitis aguda}}; tratamiento prioritario: {{c3::fibrato (fenofibrato) o icosapent-etil + control glucemico/peso/OH}}",
    '<span class="ecoe">ECOE: "TG muy elevados; fibrato y abstinencia OH."</span>',
    C3 + ["lipidos", "tg"])

add_cloze(deck_c3,
    "Riesgo ASCVD a 10 anos: &lt;{{c1::5% = bajo}} (estilo de vida); {{c2::5-7.5% = limite}} (considerar enhancers); {{c3::7.5-20% = intermedio}} (estatina moderada); {{c4::>=20% = alto}} (estatina alta intensidad)",
    '<span class="ecoe">ECOE: "Calculo ASCVD; intensidad de estatina segun categoria."</span>',
    C3 + ["lipidos", "ascvd"])

add_cloze(deck_c3,
    "Apo B y no-HDL como objetivos secundarios mas precisos que LDL en {{c1::sd metabolico/DM/TG altos}}; Lp(a) elevado = factor de riesgo independiente, util en pacientes con historia familiar premature",
    '<span class="ecoe">ECOE: "Solicito apoB/no-HDL en DM o sd metabolico."</span>',
    C3 + ["lipidos", "apob"])

# --- DM (4)
add_cloze(deck_c3,
    "Criterios ADA 2025 de DM (cualquier 1 confirmado o 1 + sintomas): {{c1::HbA1c >=6.5%}}; {{c2::glucosa ayuno >=126}}; {{c3::glucosa 2 h post-OGTT >=200}}; {{c4::glucosa casual >=200 + sintomas}}",
    '<span class="ecoe">ECOE: "Confirmo DM con dos pruebas anormales o una + sintomas."</span>',
    C3 + ["dm", "criterios"])

add_cloze(deck_c3,
    "Prediabetes (ADA 2025): {{c1::HbA1c 5.7-6.4%}} o {{c2::glucosa ayuno 100-125}} o glucosa 2 h post-OGTT 140-199",
    '<span class="ecoe">ECOE: "Prediabetes; intervencion intensiva + metformina si alto riesgo."</span>',
    C3 + ["dm", "prediabetes"])

add_cloze(deck_c3,
    "Meta HbA1c (ADA 2025): {{c1::general &lt;7%}}; {{c2::&lt;6.5% en jovenes sin riesgo hipoglucemia}}; {{c3::&lt;8% en adulto mayor fragil o con expectativa de vida limitada}}",
    '<span class="ecoe">ECOE: "Individualizo meta HbA1c por edad y comorbilidades."</span>',
    C3 + ["dm", "meta_hba1c"])

add_cloze(deck_c3,
    "Microalbuminuria: ratio albumina/creatinina {{c1::30-300 mg/g}} = nefropatia diabetica incipiente; macroalbuminuria {{c2::>300 mg/g}} = nefropatia establecida; indicacion de {{c3::IECA/ARA-II + iSGLT2}}",
    '<span class="ecoe">ECOE: "Albuminuria positiva; IECA + iSGLT2 para nefroproteccion."</span>',
    C3 + ["dm", "albuminuria"])

# --- RENAL (5)
add_cloze(deck_c3,
    "TFG por {{c1::CKD-EPI}} (preferida sobre MDRD); estadios KDIGO: G1 >=90, G2 60-89, G3a 45-59, G3b 30-44, G4 15-29, G5 &lt;15 (dialisis)",
    '<span class="ecoe">ECOE: "Calculo TFG con CKD-EPI; clasifico segun KDIGO."</span>',
    C3 + ["renal", "tfg"])

add_cloze(deck_c3,
    "ERC: estadiar por {{c1::TFG (G1-G5)}} + {{c2::albuminuria (A1 &lt;30, A2 30-300, A3 >300)}}; la combinacion da pronostico (color verde a rojo)",
    '<span class="ecoe">ECOE: "ERC G3a A2; riesgo intermedio, sigo cada 6 meses."</span>',
    C3 + ["renal", "kdigo"])

add_cloze(deck_c3,
    "AKI (KDIGO): {{c1::aumento de creatinina >=0.3 mg/dL en 48 h}}; o {{c2::aumento >=1.5x basal en 7 dias}}; o {{c3::diuresis &lt;0.5 mL/kg/h por >=6 h}}",
    '<span class="ecoe">ECOE: "AKI KDIGO estadio 1; identifico causa y suspendo nefrotoxicos."</span>',
    C3 + ["renal", "aki"])

add_cloze(deck_c3,
    "FeNa: {{c1::&lt;1% = prerrenal}} (avido de sodio); {{c2::>2% = renal/NTA}} (perdida); excepciones donde no aplica: {{c3::contraste, AINE (prerrenal con FeNa alto), glomerulonefritis (puede ser baja), diuretico reciente}}",
    '<span class="contraste">FeUrea es alternativa si diuretico reciente: &lt;35% = prerrenal.</span>'
    '<span class="ecoe">ECOE: "FeNa &lt;1% apoya AKI prerrenal."</span>',
    C3 + ["renal", "fena"])

add_cloze(deck_c3,
    "Sedimento urinario: {{c1::cilindros granulosos pigmentados}} = NTA; {{c2::cilindros eritrocitarios}} = glomerulonefritis; {{c3::cilindros leucocitarios}} = pielonefritis/NTIA; cilindros graseos = nefrotico",
    '<span class="ecoe">ECOE: "Sedimento con cilindros granulosos = NTA establecida."</span>',
    C3 + ["renal", "sedimento"])

# --- HEPATICO (4)
add_cloze(deck_c3,
    "Ratio AST/ALT: {{c1::>2 = hepatopatia alcoholica}} (mayoritariamente); {{c2::&lt;1 = MASLD/hepatitis viral}}; {{c3::>1000 ambas = hepatitis viral aguda, hepatotoxicidad (acetaminofeno), isquemica}}",
    '<span class="ecoe">ECOE: "AST/ALT >2 en bebedor = hepatopatia alcoholica."</span>',
    C3 + ["hepatico", "transaminasas"])

add_cloze(deck_c3,
    "Patron colestasico: {{c1::FA + GGT + bilirrubina directa}} elevadas; con dilatacion biliar en USG/TAC = {{c2::obstruccion extrahepatica}} (litiasis, neoplasia, estenosis); sin dilatacion = {{c3::colestasis intrahepatica}} (cirrosis biliar primaria, farmaco)",
    '<span class="ecoe">ECOE: "Patron colestasico con dilatacion biliar = obstruccion, valoro CPRE."</span>',
    C3 + ["hepatico", "colestasis"])

add_cloze(deck_c3,
    "Funcion hepatica sintetica: {{c1::INR (factores II, V, VII, X)}} + {{c2::albumina}} + {{c3::bilirrubina total}}; el INR es el marcador mas rapido (vida media factor VII 6 h), la albumina es lenta (vida media 3 semanas)",
    '<span class="ecoe">ECOE: "INR es indicador rapido de funcion sintetica hepatica."</span>',
    C3 + ["hepatico", "sintetica"])

add_cloze(deck_c3,
    "Serologias hepatitis virales: {{c1::HBsAg positivo}} = HBV activa; {{c2::anti-HBc IgM}} = HBV aguda; {{c3::anti-HBs positivo}} = inmunidad (vacuna o resolucion); {{c4::anti-HCV positivo + RNA HCV positivo}} = infeccion activa por HCV (todos deben tratarse hoy)",
    '<span class="ecoe">ECOE: "Solicito panel hepatitis completo; HCV activo se trata."</span>',
    C3 + ["hepatico", "serologias"])

# --- HEMATO (4)
add_cloze(deck_c3,
    "Clasificacion de anemias por {{c1::VCM}}: microcitica &lt;80, normocitica 80-100, macrocitica >100; primer paso ante cualquier anemia",
    '<span class="ecoe">ECOE: "Primera clasificacion: VCM define la ruta de estudio."</span>',
    C3 + ["hemato", "vcm"])

add_cloze(deck_c3,
    "Anemia ferropenica: {{c1::ferritina baja (&lt;30 ng/mL)}} es el marcador mas especifico; {{c2::hierro serico bajo + transferrina/TIBC alta + saturacion baja (&lt;20%)}}; {{c3::RDW alto}}; reticulocitos bajos",
    '<span class="contraste">Ferritina puede estar normal/alta en inflamacion - usar saturacion y RDW.</span>'
    '<span class="ecoe">ECOE: "Ferritina &lt;30 confirma ferropenia."</span>',
    C3 + ["hemato", "ferropenica"])

add_cloze(deck_c3,
    "Anemia de enfermedad cronica: {{c1::ferritina normal/alta}} (reactante de fase aguda), {{c2::hierro bajo}}, transferrina baja, saturacion baja; mediada por {{c3::hepcidina}}; tratar la causa subyacente",
    '<span class="ecoe">ECOE: "AEC; trato la enfermedad subyacente; EPO si ERC con Hb &lt;10."</span>',
    C3 + ["hemato", "aec"])

add_cloze(deck_c3,
    "Anemia megaloblastica: VCM {{c1::>100}}; {{c2::B12 baja}} -> neuropatia + glositis + sd cordonal posterior (riesgo neurologico irreversible); {{c3::folato bajo}} -> embarazo/OH, sin neuropatia",
    '<span class="redflag">Siempre confirmar B12 antes de reponer folato (puede empeorar neuropatia por B12).</span>'
    '<span class="ecoe">ECOE: "Macrocitosis = pido B12 + folato + TSH + descarto OH."</span>',
    C3 + ["hemato", "megaloblastica"])

# --- ECG (5)
add_cloze(deck_c3,
    "ECG en FA: {{c1::ausencia de ondas P}} + linea de base irregular + RR {{c2::irregularmente irregular}}; FC variable; complicacion principal = ictus cardioembolico",
    '<span class="ecoe">ECOE: "ECG con FA; anticoagulacion segun CHA2DS2-VASc."</span>',
    C3 + ["ecg", "fa"])

add_cloze(deck_c3,
    "IAMCEST por territorio: {{c1::anterior V1-V4 (DA)}}; {{c2::lateral I, aVL, V5-V6 (Cx)}}; {{c3::inferior II, III, aVF (CD habitualmente)}}; posterior V7-V9 + recipricidad en V1-V2",
    '<span class="ecoe">ECOE: "Localizo IAM por territorio en ECG."</span>',
    C3 + ["ecg", "iamcest"])

add_cloze(deck_c3,
    "Hipertrofia ventricular izquierda - criterios voltaje: {{c1::Sokolow-Lyon (S V1 + R V5 o V6 >=35 mm)}}; {{c2::Cornell (R aVL + S V3 >28 en varon o >20 en mujer)}}; alteraciones secundarias en repolarizacion (strain)",
    '<span class="ecoe">ECOE: "HVI por criterios de voltaje sugiere cardiopatia HTA o EAo."</span>',
    C3 + ["ecg", "hvi"])

add_cloze(deck_c3,
    "Bloqueo AV: 1er grado = {{c1::PR >200 ms}} constante; 2do Mobitz I (Wenckebach) = {{c2::PR se alarga progresivamente hasta bloqueo}}; 2do Mobitz II = PR fijo + {{c3::bloqueos suabitos}}; 3er grado = {{c4::disociacion AV completa}}",
    '<span class="contraste">Mobitz II y bloqueo completo = marcapasos.</span>'
    '<span class="ecoe">ECOE: "Mobitz II y BAV completo son indicacion de marcapasos."</span>',
    C3 + ["ecg", "bav"])

add_cloze(deck_c3,
    "Alteraciones por K: {{c1::hiperK -> T picudas, QRS ancho, PR largo, P aplanada, fusion en ondas sinusoidales}}; {{c2::hipoK -> T aplanada, ondas U, QT largo, riesgo torsade de pointes}}",
    '<span class="ecoe">ECOE: "Cambios ECG dictan urgencia de correccion."</span>',
    C3 + ["ecg", "potasio"])

# --- ECO (3)
add_cloze(deck_c3,
    "FEVI por ecocardiografia (AHA 2022): {{c1::normal >=55%}}; {{c2::levemente reducida 41-49% (IC con FE levemente reducida, HFmrEF)}}; {{c3::reducida &lt;=40% (IC con FE reducida, HFrEF)}}",
    '<span class="ecoe">ECOE: "Clasifico IC segun FEVI."</span>',
    C3 + ["eco", "fevi"])

add_cloze(deck_c3,
    "Estenosis aortica severa: area valvular {{c1::&lt;1 cm2}}, gradiente medio {{c2::>=40 mmHg}}, velocidad pico {{c3::>=4 m/s}}; indicacion de reemplazo valvular si sintomatica o FEVI &lt;50%",
    '<span class="ecoe">ECOE: "EAo severa sintomatica = SAVR/TAVR."</span>',
    C3 + ["eco", "eao"])

add_cloze(deck_c3,
    "Endocarditis - eco: {{c1::vegetacion (masa oscilante)}} es criterio mayor Duke; eco transesofagico {{c2::mas sensible}} (especialmente protesis); buscar absceso, perforacion, dehiscencia",
    '<span class="ecoe">ECOE: "ETE para confirmar vegetacion en EI sospechosa."</span>',
    C3 + ["eco", "endocarditis"])

# --- TIROIDES (3)
add_cloze(deck_c3,
    "Hipertiroidismo primario: {{c1::TSH suprimida}} + {{c2::T4L elevada}}; causas: Graves, BMN toxica, adenoma toxico, tiroiditis (transitorio)",
    '<span class="ecoe">ECOE: "Hipertiroidismo primario; busco etiologia con TRAb y gammagrafia."</span>',
    C3 + ["tiroides", "hiper"])

add_cloze(deck_c3,
    "Hipotiroidismo primario: {{c1::TSH elevada}} + {{c2::T4L baja}}; causa mas frecuente = {{c3::tiroiditis de Hashimoto (anti-TPO/anti-TG positivos)}}",
    '<span class="ecoe">ECOE: "Hipotiroidismo primario; levotiroxina y ajuste por TSH a 6-8 sem."</span>',
    C3 + ["tiroides", "hipo"])

add_cloze(deck_c3,
    "Hipotiroidismo subclinico: {{c1::TSH elevada}} + T4L {{c2::normal}}; tratar si TSH {{c3::>10}} o sintomatica/embarazo/bocio/anticuerpos positivos; vigilancia si &lt;10 y asintomatico",
    '<span class="ecoe">ECOE: "Subclinico; tratar solo si criterios."</span>',
    C3 + ["tiroides", "subclinico"])

# --- GASOMETRIA (3)
add_cloze(deck_c3,
    "Acidosis metabolica: {{c1::pH bajo + HCO3 bajo}}; calcular {{c2::anion gap = Na - (Cl + HCO3)}} normal 8-12; anion gap elevado = MUDPILES; normal = perdida HCO3 (diarrea, RTA)",
    '<span class="ecoe">ECOE: "Acidosis metabolica con anion gap alto; investigo MUDPILES."</span>',
    C3 + ["gaso", "acidosis"])

add_cloze(deck_c3,
    "MUDPILES (acidosis con anion gap elevado): {{c1::Metanol, Uremia, Diabeticocetoacidosis, Paraldehido, INH/Hierro, Lactato (sepsis/isquemia), Etilenglicol, Salicilatos}}",
    '<span class="ecoe">ECOE: "Diferencial de acidosis con gap = MUDPILES."</span>',
    C3 + ["gaso", "mudpiles"])

add_cloze(deck_c3,
    "Compensacion respiratoria esperada en acidosis metabolica (Winter): {{c1::PaCO2 esperado = 1.5 x HCO3 + 8 (+/- 2)}}; si PaCO2 mayor = acidosis respiratoria asociada; menor = alcalosis respiratoria asociada",
    '<span class="ecoe">ECOE: "Aplico Winter para detectar trastorno mixto."</span>',
    C3 + ["gaso", "compensacion"])

# --- MARCADORES (4)
add_cloze(deck_c3,
    "Troponina (hs-cTn): patron de {{c1::elevacion-pico-descenso}} + clinica de isquemia + cambios ECG = IAM (definicion universal); algoritmo {{c2::0/1 h o 0/3 h}} para descartar IAM en ECOE/Urgencias",
    '<span class="contraste">Troponina elevada por otras causas: IC, TEP, sepsis, ERC, miocarditis - clinica integra.</span>'
    '<span class="ecoe">ECOE: "Troponina seriada con algoritmo rapido descarta IAM."</span>',
    C3 + ["marcadores", "troponina"])

add_cloze(deck_c3,
    "BNP/NT-proBNP en disnea aguda: {{c1::BNP &lt;100 / NT-proBNP &lt;300}} = IC poco probable; {{c2::BNP >400 / NT-proBNP >450 (&lt;50a), >900 (50-75a), >1800 (>75a)}} = IC probable; zona gris intermedia",
    '<span class="contraste">Falsos altos: ERC, FA, edad avanzada. Falsos bajos: obesidad.</span>'
    '<span class="ecoe">ECOE: "BNP elevado en disnea = IC; integro con clinica y eco."</span>',
    C3 + ["marcadores", "bnp"])

add_cloze(deck_c3,
    "Procalcitonina: {{c1::>0.5 ng/mL}} sugiere infeccion bacteriana sistemica; util en {{c2::guiar suspension de ATB}} (caida del 80% = retirar); valores muy altos en sepsis severa/shock septico",
    '<span class="ecoe">ECOE: "PCT guia inicio y duracion de ATB."</span>',
    C3 + ["marcadores", "pct"])

add_cloze(deck_c3,
    "PCR y VSG en reumatologia: ambas inespecificas; muy elevadas (>100 mg/L PCR o >100 mm VSG) en {{c1::polimialgia reumatica, arteritis temporal, infeccion grave, vasculitis}}",
    '<span class="ecoe">ECOE: "VSG/PCR muy altas con cuadro de PMR/AT = corticoide rapido."</span>',
    C3 + ["marcadores", "vsg_pcr"])


# ============================================================
# CAPA 4 - MANEJO Y DDX (55 Q&A)
# ============================================================
C4 = ["capa4", "manejo"]

# --- PACIENTE CRONICO COMPLEJO (5) - el bloque ORO en ECOE
add_qa(deck_c4,
    "Manejo integral: <b>Paciente cronico complejo</b> (HTA + DM2 + tabaco + OH + LDL 210 + HbA1c 6.6 + transaminasas + anemia)",
    "<b>Eje dominante: RIESGO CARDIOVASCULAR GLOBAL ALTO</b>.<br><br>"
    "<b>Prioridad terapeutica (en orden)</b>:<br>"
    "1) <b>Estatina alta intensidad</b> (atorvastatina 40-80 mg o rosuvastatina 20-40 mg) - LDL >=190 obliga.<br>"
    "2) <b>Control PA con IECA/ARA-II</b> (eleccion en DM: ARA-II/IECA; meta &lt;130/80).<br>"
    "3) <b>Metformina + iSGLT2 o GLP-1</b> (cardio/nefroproteccion segun ADA 2025).<br>"
    "4) <b>Suspender AINE</b> si usa (riesgo renal y CV).<br>"
    "5) <b>Intervencion tabaquismo</b>: counseling 5A + farmacoterapia (vareniclina, bupropion, NRT).<br>"
    "6) <b>Intervencion alcohol</b>: counseling + AUDIT + naltrexona/acamprosato si dependencia.<br>"
    "7) <b>Estudio de transaminasas</b>: perfil hepatico completo, USG hepatico, serologias hepatitis si sospecha.<br>"
    "8) <b>Estudio de anemia</b>: BH con VCM, ferritina, B12/folato, endoscopia + colonoscopia si ferropenica.<br>"
    "9) <b>Seguimiento estructurado</b> 4-6 sem con laboratorios."
    '<span class="ecoe">ECOE: "Eje = riesgo CV global; estatina alta intensidad + ARA-II + metformina/iSGLT2 + intervencion habitos + estudio transaminasas y anemia + seguimiento."</span>',
    C4 + ["cronico_complejo", "integral"])

add_qa(deck_c4,
    "Manejo: <b>Sindrome metabolico</b>",
    "1) <b>Cambios de estilo de vida</b> (pilar): perdida de peso 7-10%, dieta mediterranea/DASH, ejercicio 150 min/sem aerobico + 2/sem fuerza.<br>"
    "2) <b>Tratar cada componente</b>:<br>"
    "&nbsp;&nbsp;- HTA: IECA/ARA-II.<br>"
    "&nbsp;&nbsp;- Dislipidemia: estatina segun ASCVD.<br>"
    "&nbsp;&nbsp;- Hiperglucemia: metformina si prediabetes con riesgo.<br>"
    "&nbsp;&nbsp;- TG altos: estilo de vida; fibrato si >500.<br>"
    "3) <b>Aspirina</b> NO rutina en prevencion primaria; valorar caso a caso (USPSTF 2022).<br>"
    "4) Tamizaje: MASLD/MASH (ALT, USG), apnea del sueno si obesidad."
    '<span class="ecoe">ECOE: "Sd metabolico; estilo de vida + tratar componentes individualmente."</span>',
    C4 + ["cronico_complejo", "sd_metabolico"])

add_qa(deck_c4,
    "Manejo: <b>Prevencion secundaria post-IAM o post-ACV</b>",
    "<b>A</b>spirina 75-100 mg/d indefinida + segundo antiagregante 12 m (DAPT post-ACS).<br>"
    "<b>B</b>etabloqueador (especialmente si FEVI &lt;40%, IAM previo).<br>"
    "<b>C</b>olesterol: estatina alta intensidad, meta LDL &lt;70 (ideal &lt;55); ezetimiba/PCSK9 si no alcanza.<br>"
    "<b>D</b>ieta + Diabetes control + ejercicio (rehabilitacion cardiaca).<br>"
    "<b>E</b>nalapril/IECA/ARA-II (especialmente DM, FEVI baja, ERC, HTA).<br>"
    "<b>F</b>umar: dejar (vareniclina, bupropion, NRT).<br>"
    "<b>+ iSGLT2/ARNI/ARM</b> en IC; <b>anticoagulacion</b> si FA o trombo VI."
    '<span class="ecoe">ECOE: "Prevencion secundaria con ABCDE + iSGLT2 si IC."</span>',
    C4 + ["prevencion"])

add_qa(deck_c4,
    "Manejo: <b>Polifarmacia en adulto mayor</b> (STOPP-START / Beers)",
    "Aplicar herramientas validadas:<br>"
    "- <b>STOPP</b>: medicamentos a evitar (benzodiacepinas en >65, anticolinergicos, AINE prolongados, digoxina &gt;0.125 con ERC, glibenclamida).<br>"
    "- <b>START</b>: medicamentos infraindicados a iniciar (estatina en ASCVD, IECA en IC, anticoagulacion en FA con CHA2DS2-VASc).<br>"
    "- <b>Beers</b>: similar enfoque, AGS.<br>"
    "Revision sistematica cada visita; deprescripcion estructurada (objetivo: simplificar).<br>"
    "Vigilar interacciones, adherencia, autonomia."
    '<span class="ecoe">ECOE: "Aplico STOPP-START; identifico medicamentos a retirar y faltantes."</span>',
    C4 + ["polifarmacia"])

add_qa(deck_c4,
    "DDx: <b>Transaminasas elevadas leves en adulto cronico complejo</b>",
    "1) <b>MASLD/esteatosis metabolica</b> (la mas probable en obeso/DM): AST/ALT &lt;1, USG con esteatosis.<br>"
    "2) <b>Hepatopatia alcoholica</b>: AST/ALT &gt;2, GGT alta, antecedente.<br>"
    "3) <b>Hepatitis viral</b> (HBV, HCV): serologias.<br>"
    "4) <b>Hepatotoxicidad por farmacos</b>: estatinas, paracetamol, isoniazida, amiodarona, metotrexato.<br>"
    "5) <b>Hepatitis autoinmune</b>: ANA, anti-LKM, IgG.<br>"
    "6) <b>Hemocromatosis</b>: ferritina + saturacion alta, HFE.<br>"
    "7) <b>Wilson</b> (joven): ceruloplasmina, cobre urinario.<br>"
    "8) <b>Causas extrahepaticas</b>: hipotiroidismo, celiaca, ejercicio extenuante."
    '<span class="ecoe">ECOE: "DDx transaminasas; ordeno por probabilidad y solicito panel completo + USG."</span>',
    C4 + ["ddx", "transaminasas"])

# --- HTA (3)
add_qa(deck_c4,
    "Manejo: <b>HTA</b> (ACC/AHA 2017)",
    "<b>Categorias</b>: normal &lt;120/&lt;80; elevada 120-129/&lt;80; HTA estadio 1 130-139/80-89; HTA estadio 2 &gt;=140/&gt;=90.<br>"
    "<b>Meta general</b>: &lt;130/80 (incluye DM, ERC, mayores).<br>"
    "<b>Inicio farmacologico</b>:<br>"
    "- Estadio 1 + ASCVD/DM/ERC/&gt;=10% ASCVD: inicio.<br>"
    "- Estadio 2: inicio (frecuentemente con 2 farmacos).<br>"
    "<b>Primera linea</b>: tiazida, IECA/ARA-II, CCB dihidropiridinico.<br>"
    "<b>Afroamericano sin ERC</b>: tiazida o CCB primero.<br>"
    "<b>DM o ERC</b>: IECA/ARA-II preferido.<br>"
    "<b>IC FEr</b>: ARNI/IECA + BB + ARM + iSGLT2.<br>"
    "<b>Embarazo</b>: labetalol, nifedipino LP, metildopa (evitar IECA/ARA-II)."
    '<span class="ecoe">ECOE: "HTA estadio 2 en DM = IECA/ARA-II + tiazida; meta &lt;130/80."</span>',
    C4 + ["hta"])

add_qa(deck_c4,
    "Manejo: <b>Crisis hipertensiva</b>",
    "<b>Emergencia HTA</b> (con dano de organo blanco: encefalopatia, EAP, IAM, diseccion, eclampsia, AKI):<br>"
    "- UCI + monitorizacion invasiva.<br>"
    "- Reducir PA <b>10-20% en la primera hora</b>, luego 5-15% adicional en 24 h (no abruptamente, riesgo de isquemia).<br>"
    "- Farmacos IV segun tipo: <b>labetalol o nicardipino</b> (general); <b>esmolol</b> (diseccion + control FC); <b>nitroprusiato</b> (encefalopatia, EAP); <b>nitroglicerina</b> (IAM, EAP).<br>"
    "- Diseccion aortica: PAS objetivo &lt;120 + FC &lt;60.<br><br>"
    "<b>Urgencia HTA</b> (sin dano agudo):<br>"
    "- Ambulatorio.<br>"
    "- VO: captopril/amlodipino; reduccion gradual en 24-48 h.<br>"
    "- Reiniciar/optimizar tratamiento cronico, identificar causa de no adherencia."
    '<span class="ecoe">ECOE: "Emergencia HTA = IV en UCI, descenso 10-20% en 1 h; urgencia = VO ambulatorio."</span>',
    C4 + ["hta", "crisis"])

add_qa(deck_c4,
    "Manejo: <b>HTA en diabetico</b>",
    "<b>Meta &lt;130/80</b> (ADA 2025 + ACC/AHA).<br>"
    "<b>Primera linea</b>: <b>IECA o ARA-II</b> (nefroproteccion en albuminuria) + tiazida o CCB.<br>"
    "<b>Si albuminuria moderada-severa</b>: <b>iSGLT2 anadido</b> (empagliflozina, dapagliflozina) - cardio + nefroproteccion.<br>"
    "<b>Si resistente</b>: considerar espironolactona (PATHWAY-2).<br>"
    "Estilo de vida obligatorio: DASH, sodio &lt;2.3 g/d, peso, ejercicio, OH limitado."
    '<span class="ecoe">ECOE: "HTA + DM = ARA-II/IECA + iSGLT2 si albuminuria."</span>',
    C4 + ["hta", "dm"])

# --- DM (4)
add_qa(deck_c4,
    "Manejo: <b>DM2</b> (ADA 2025)",
    "1) <b>Estilo de vida</b> (siempre): perdida peso 5-10%, dieta, ejercicio 150 min/sem.<br>"
    "2) <b>Metformina</b> primera linea (salvo TFG &lt;30 o contraindicacion).<br>"
    "3) <b>Anadir segundo agente segun comorbilidades</b>:<br>"
    "&nbsp;&nbsp;- <b>ASCVD establecida o alto riesgo</b>: GLP-1 con beneficio CV (liraglutide, semaglutide, dulaglutide) o iSGLT2.<br>"
    "&nbsp;&nbsp;- <b>IC con FEr</b>: iSGLT2 (empagliflozina, dapagliflozina).<br>"
    "&nbsp;&nbsp;- <b>ERC o albuminuria</b>: iSGLT2; GLP-1 si TFG bajo (no iSGLT2).<br>"
    "&nbsp;&nbsp;- <b>Necesidad de perdida de peso</b>: GLP-1 (semaglutide, tirzepatide).<br>"
    "&nbsp;&nbsp;- <b>Costos limitados</b>: sulfonilurea, pioglitazona.<br>"
    "4) <b>Insulina basal</b> si HbA1c &gt;10%, glucosa &gt;300 o sintomatica/catabolica.<br>"
    "5) <b>Estatina</b> (alta intensidad si ASCVD; moderada en mayores de 40 sin ASCVD).<br>"
    "6) Aspirina secundaria; tamizaje retinopatia, nefropatia, neuropatia, pie."
    '<span class="ecoe">ECOE: "Metformina + iSGLT2 si IC/ERC o GLP-1 si ASCVD/obesidad."</span>',
    C4 + ["dm"])

add_qa(deck_c4,
    "Manejo: <b>Insulinizacion en DM2</b>",
    "<b>Cuando</b>: HbA1c &gt;10%, glucosa &gt;300, sintomatica, no logra meta con orales, situaciones agudas (CAD, EHH, infeccion grave, esteroides altas dosis).<br>"
    "<b>Inicio</b>: <b>insulina basal (glargina, detemir, degludec) 10 U o 0.1-0.2 U/kg al acostarse</b>.<br>"
    "<b>Ajuste</b>: titular cada 3 dias hasta glucosa ayuno 80-130.<br>"
    "<b>Intensificacion</b>: anadir bolos prandiales (analogos rapidos) o usar premezclas; esquema basal-bolo si requiere control prandial."
    '<span class="ecoe">ECOE: "Inicio insulina basal nocturna y titulo por glucosa ayuno."</span>',
    C4 + ["dm", "insulina"])

add_qa(deck_c4,
    "Manejo: <b>Cetoacidosis diabetica (CAD)</b>",
    "1) <b>Fluidos</b>: SF 0.9% 1 L primera hora, luego 500 mL/h; cambiar a SF 0.45% cuando Na corregido normal/alto y a SG 5% + insulina cuando glucosa &lt;200-250.<br>"
    "2) <b>Potasio</b>: si K &lt;3.3 -> reponer ANTES de insulina; si 3.3-5.3 -> anadir 20-30 mEq/L; si &gt;5.3 -> no reponer aun.<br>"
    "3) <b>Insulina</b>: bolo 0.1 U/kg + infusion 0.1 U/kg/h (o sin bolo, infusion 0.14 U/kg/h); meta caida glucosa 50-75/h.<br>"
    "4) <b>Bicarbonato</b>: solo si pH &lt;6.9.<br>"
    "5) <b>Identificar y tratar precipitante</b>: infeccion, no adherencia, IAM, CVA.<br>"
    "6) Transicion a insulina SC cuando: pH &gt;7.3, HCO3 &gt;18, anion gap &lt;12, tolerancia VO (overlap 1-2 h)."
    '<span class="ecoe">ECOE: "CAD: SF + K + insulina; no bicarbonato salvo pH &lt;6.9; precipitante siempre."</span>',
    C4 + ["cad"])

add_qa(deck_c4,
    "Manejo: <b>Estado hiperglucemico hiperosmolar (EHH)</b>",
    "1) <b>Reposicion volumen agresiva</b> (deficit 8-10 L): SF 0.9% 1-1.5 L/h primeras 2 h, luego ajustar.<br>"
    "2) <b>Potasio</b>: similar a CAD; anadir cuando K &lt;5.3.<br>"
    "3) <b>Insulina</b>: empezar cuando glucosa estabilizada con fluidos (0.05-0.1 U/kg/h infusion); evitar bajadas bruscas.<br>"
    "4) <b>Identificar precipitante</b>: infeccion (mas frecuente), IAM, ACV, no adherencia.<br>"
    "5) Vigilar comorbilidades cardiovasculares (anciano).<br>"
    "6) Transicion a basal-bolus cuando estable."
    '<span class="ecoe">ECOE: "EHH: volumen primero (deficit grande), insulina despues, busco infeccion subyacente."</span>',
    C4 + ["ehh"])

# --- DISLIPIDEMIA (3)
add_qa(deck_c4,
    "Manejo: <b>Dislipidemia</b> (AHA 2018)",
    "<b>Indicaciones de estatina (4 grupos)</b>:<br>"
    "1) ASCVD clinica establecida.<br>"
    "2) LDL &gt;=190 mg/dL.<br>"
    "3) DM 40-75 anos.<br>"
    "4) ASCVD calculado &gt;=7.5% en 40-75 anos sin ASCVD ni DM.<br>"
    "<b>Intensidad</b>:<br>"
    "- <b>Alta</b> (reduccion LDL &gt;=50%): atorvastatina 40-80 mg, rosuvastatina 20-40 mg.<br>"
    "- <b>Moderada</b> (reduccion 30-49%): atorvastatina 10-20, rosuvastatina 5-10, simvastatina 20-40, pravastatina 40.<br>"
    "<b>Anadir si no llega meta</b>: ezetimiba; <b>PCSK9</b> (alirocumab, evolocumab) si refractario y muy alto riesgo; <b>icosapent-etil</b> si TG persisten 150-499."
    '<span class="ecoe">ECOE: "Estatina alta intensidad si ASCVD o LDL >=190; ezetimiba/PCSK9 si no meta."</span>',
    C4 + ["dislipidemia"])

add_qa(deck_c4,
    "Manejo: <b>Hipertrigliceridemia severa</b> (TG &gt;500)",
    "<b>Prioridad: prevenir pancreatitis aguda</b> (TG &gt;1000 = riesgo alto).<br>"
    "1) <b>Fibrato (fenofibrato 145 mg/d o gemfibrozilo)</b> primera linea.<br>"
    "2) <b>Cambios de estilo de vida</b>: abstinencia alcohol, perdida peso, bajar carbohidratos refinados.<br>"
    "3) <b>Acidos grasos omega-3</b> (icosapent-etil 4 g/d).<br>"
    "4) Control glucemico estricto si DM.<br>"
    "5) Suspender estrogenos, retinoides, glucocorticoides si posible.<br>"
    "6) Estatina si LDL elevado tambien (vigilar interaccion con gemfibrozilo - rabdomiolisis)."
    '<span class="ecoe">ECOE: "TG &gt;500 = fibrato + abstinencia OH + omega-3."</span>',
    C4 + ["dislipidemia", "tg"])

add_qa(deck_c4,
    "Indicaciones de <b>PCSK9 (alirocumab/evolocumab)</b>",
    "Pacientes muy alto riesgo (ASCVD o LDL &gt;=190 - hipercolesterolemia familiar) que con <b>estatina maxima tolerada + ezetimiba</b> NO alcanzan meta LDL.<br>"
    "Reducen LDL ~60% adicional.<br>"
    "<b>Inclisiran</b> (siRNA) opcion mas reciente, dosificacion semestral (cada 6 meses)."
    '<span class="ecoe">ECOE: "PCSK9 si refractario con estatina maxima + ezetimiba."</span>',
    C4 + ["dislipidemia", "pcsk9"])

# --- IC (3)
add_qa(deck_c4,
    "Manejo: <b>IC con FE reducida (FEr)</b> - 4 pilares (ACC/AHA 2022)",
    "<b>Cuatro pilares + diuretico segun congestion</b>:<br>"
    "1) <b>ARNI</b> (sacubitrilo/valsartan) - preferido sobre IECA/ARA-II si tolerado y sin contraindicaciones (evitar 36 h tras IECA por angioedema); IECA o ARA-II si no ARNI.<br>"
    "2) <b>Betabloqueador con evidencia en IC</b>: <b>carvedilol, bisoprolol o metoprolol succinato</b>.<br>"
    "3) <b>ARM</b> (espironolactona o eplerenona) - vigilar K y funcion renal.<br>"
    "4) <b>iSGLT2</b> (dapagliflozina, empagliflozina) - aun sin DM.<br>"
    "+ <b>Diuretico de asa</b> (furosemida) segun congestion - no modifica mortalidad pero sintomatico.<br>"
    "+ Ivabradina si FC &gt;70 sinusal pese a BB maximo; vericiguat en clase III-IV; resincronizacion (CRT) si QRS &gt;=150 ms con BRI; DAI si FEVI &lt;=35% pese a OMT."
    '<span class="ecoe">ECOE: "Cuatro pilares en IC FEr: ARNI + BB + ARM + iSGLT2."</span>',
    C4 + ["ic", "fer"])

add_qa(deck_c4,
    "Manejo: <b>IC con FE preservada (FEp)</b>",
    "1) <b>Control de comorbilidades</b>: HTA estricta, FA con control FC, DM (iSGLT2), obesidad, apnea sueno.<br>"
    "2) <b>iSGLT2</b> (empagliflozina, dapagliflozina) - <b>UNICA clase con evidencia consistente de beneficio</b> en HFpEF (EMPEROR-Preserved, DELIVER).<br>"
    "3) <b>Diuretico de asa</b> segun congestion.<br>"
    "4) Considerar ARM (espironolactona) si HFpEF leve sintomatica.<br>"
    "5) Rehabilitacion cardiaca."
    '<span class="ecoe">ECOE: "HFpEF: iSGLT2 base + control de HTA y comorbilidades + diuretico."</span>',
    C4 + ["ic", "fep"])

add_qa(deck_c4,
    "Manejo: <b>IC descompensada aguda</b>",
    "1) <b>Posicion semisentado + O2</b> (si SatO2 &lt;90); <b>VNI (BiPAP/CPAP)</b> si EAP/hipercapnia.<br>"
    "2) <b>Diuretico de asa IV</b>: furosemida 1-2.5x dosis ambulatoria IV bolo o infusion.<br>"
    "3) <b>Vasodilatador IV</b> (nitroglicerina, nitroprusiato) si HTA con EAP.<br>"
    "4) <b>Inotropico</b> (dobutamina, milrinona) si bajo gasto/shock cardiogenico.<br>"
    "5) <b>Identificar precipitante</b>: SCA, FA rapida, IRA, infeccion, no adherencia, isquemia, miocarditis.<br>"
    "6) Continuar/iniciar tratamiento basal optimo (NO suspender BB excepto shock); iSGLT2 puede iniciarse durante hospitalizacion (SOLOIST-WHF)."
    '<span class="ecoe">ECOE: "EAP: O2/VNI + furosemida IV + vasodilatador + busco precipitante."</span>',
    C4 + ["ic", "aguda"])

# --- FA (2)
add_qa(deck_c4,
    "Manejo: <b>FA</b> - anticoagulacion (ACC/AHA 2019/2023)",
    "<b>CHA2DS2-VASc</b>:<br>"
    "- 0 (varon) o 1 (mujer): sin anticoagulacion.<br>"
    "- 1 (varon) o 2 (mujer): considerar.<br>"
    "- &gt;=2 (varon) o &gt;=3 (mujer): <b>anticoagular</b>.<br>"
    "<b>Eleccion</b>:<br>"
    "- <b>DOAC preferido</b>: apixaban (5 mg c/12 h o 2.5 si criterios), rivaroxaban (20 mg/d), dabigatran (150 mg c/12 h), edoxaban.<br>"
    "- <b>Warfarina</b>: en valvulopatia mitral mecanica o estenosis mitral moderada-severa (DOAC contraindicado).<br>"
    "Reevaluar HAS-BLED para optimizar factores modificables; cierre de orejuela (Watchman) si contraindicacion absoluta a anticoagulacion a largo plazo."
    '<span class="ecoe">ECOE: "FA con CHA2DS2-VASc >=2 = DOAC; warfarina solo si valvular."</span>',
    C4 + ["fa", "anticoagulacion"])

add_qa(deck_c4,
    "Manejo: <b>FA - control de ritmo vs frecuencia</b>",
    "<b>Control de frecuencia</b> (mayor parte de pacientes - AFFIRM): meta FC &lt;110 (lenient) o &lt;80 (strict si sintomatico).<br>"
    "- BB (metoprolol, bisoprolol) primera linea.<br>"
    "- CCB no dihidropiridinico (diltiazem, verapamilo) - evitar si FEr.<br>"
    "- Digoxina segunda linea.<br><br>"
    "<b>Control de ritmo</b>: preferido si sintomas pese a control FC, FA paroxistica, joven, IC, ablacion exitosa.<br>"
    "- Cardioversion electrica si inestable.<br>"
    "- Farmacos: flecainida/propafenona (sin cardiopatia), amiodarona (con cardiopatia), dofetilida.<br>"
    "- <b>Ablacion por cateter</b> (aislamiento venas pulmonares) - eleccion en FA paroxistica sintomatica refractaria; EAST-AFNET 4 sugiere control de ritmo temprano mejora outcomes.<br><br>"
    "Anticoagulacion segun CHA2DS2-VASc <b>independiente</b> de estrategia ritmo/frecuencia."
    '<span class="ecoe">ECOE: "Decido ritmo vs frecuencia segun sintomas y comorbilidades; anticoagulacion sin importar."</span>',
    C4 + ["fa", "control"])

# --- ACS (2)
add_qa(deck_c4,
    "Manejo: <b>IAMCEST</b> (ACC/AHA 2023)",
    "1) <b>Reperfusion urgente</b>:<br>"
    "&nbsp;&nbsp;- <b>ICP primaria &lt;90 min</b> (door-to-balloon) en centro con hemodinamia.<br>"
    "&nbsp;&nbsp;- <b>Fibrinolisis &lt;120 min</b> si traslado &gt;120 min (alteplasa, tenecteplasa).<br>"
    "2) <b>MONA - reformado</b>:<br>"
    "&nbsp;&nbsp;- ASA 162-325 mg cargar + 81 mg/d indefinida.<br>"
    "&nbsp;&nbsp;- <b>Inhibidor P2Y12</b> (ticagrelor 180 cargar luego 90 c/12; prasugrel; clopidogrel) - <b>DAPT 12 meses</b>.<br>"
    "&nbsp;&nbsp;- Anticoagulacion peri-ICP (heparina, bivalirudina, enoxaparina).<br>"
    "&nbsp;&nbsp;- O2 solo si SatO2 &lt;90 (no rutina).<br>"
    "&nbsp;&nbsp;- Nitroglicerina sublingual; morfina si dolor persistente (evitar abuso).<br>"
    "3) <b>Estatina alta intensidad</b> + IECA/ARA-II (si FEVI baja/HTA/DM) + BB.<br>"
    "4) Rehabilitacion cardiaca + prevencion secundaria ABCDE."
    '<span class="ecoe">ECOE: "IAMCEST = ICP &lt;90 min, DAPT, anticoagulacion, estatina alta, ABCDE."</span>',
    C4 + ["acs", "iamcest"])

add_qa(deck_c4,
    "Manejo: <b>IAMSEST/Angina inestable</b>",
    "1) <b>Estratificacion</b>: <b>GRACE/TIMI</b>; troponina seriada; eco/funcion VI.<br>"
    "2) <b>Antiagregacion</b>: ASA + inhibidor P2Y12 (ticagrelor preferido si estrategia invasiva, prasugrel post-anatomia).<br>"
    "3) <b>Anticoagulacion</b>: enoxaparina, fondaparinux o heparina IV.<br>"
    "4) <b>Estrategia invasiva</b>:<br>"
    "&nbsp;&nbsp;- <b>Inmediata (&lt;2 h)</b>: inestabilidad hemodinamica/electrica, angina refractaria, IC aguda, ST dinamico.<br>"
    "&nbsp;&nbsp;- <b>Temprana (&lt;24 h)</b>: GRACE &gt;140, troponina dinamica, cambios ECG dinamicos.<br>"
    "&nbsp;&nbsp;- <b>Diferida (&lt;72 h)</b>: riesgo intermedio.<br>"
    "5) <b>Conservadora</b> si bajo riesgo + comorbilidades.<br>"
    "6) Mismo manejo post-ICP que IAMCEST: DAPT 12 m, estatina alta, BB, IECA/ARA-II, prevencion secundaria."
    '<span class="ecoe">ECOE: "IAMSEST: estratifico GRACE; invasiva &lt;24 h si alto riesgo."</span>',
    C4 + ["acs", "iamsest"])

# --- PULMONAR (3)
add_qa(deck_c4,
    "Manejo: <b>EPOC exacerbacion</b> (GOLD 2024)",
    "1) <b>SABA + SAMA</b> nebulizados (salbutamol + ipratropio).<br>"
    "2) <b>Corticoide sistemico</b>: prednisona 40 mg/d VO x 5 dias (o metilprednisolona IV si no tolera VO).<br>"
    "3) <b>Antibiotico</b> si criterios Anthonisen 2-3 (aumento esputo purulento) o requiere VMI:<br>"
    "&nbsp;&nbsp;- Amoxicilina-clavulanico, azitromicina, doxiciclina, o cefuroxima 5-7 dias.<br>"
    "&nbsp;&nbsp;- Si riesgo Pseudomonas (FEV1 &lt;30%, bronquiectasias, ATB recientes, hospitalizacion): fluoroquinolona antipseudomona (levo/cipro) o pip-tazo.<br>"
    "4) <b>O2 controlado</b> (SatO2 88-92%, evitar narcosis CO2).<br>"
    "5) <b>VNI (BiPAP)</b> si pH &lt;7.35 + PaCO2 &gt;45 - <b>reduce mortalidad e intubacion</b>.<br>"
    "6) Optimizar tratamiento basal post-alta + rehabilitacion + vacunacion + dejar de fumar."
    '<span class="ecoe">ECOE: "EPOC exacerbado: SABA/SAMA + corticoide + ATB si Anthonisen + VNI si acidosis."</span>',
    C4 + ["epoc"])

add_qa(deck_c4,
    "Manejo: <b>Asma exacerbacion</b> (GINA 2024)",
    "<b>Severidad</b>: leve-moderada (puede hablar oraciones), severa (palabras), inminencia parada (somnolencia, torax silente).<br>"
    "1) <b>SABA</b> (salbutamol) inhalado/nebulizado en MDI con espaciador 4-10 puffs cada 20 min en la primera hora.<br>"
    "2) <b>O2</b> para SatO2 93-95% (94-98% en ninos).<br>"
    "3) <b>Corticoide sistemico</b>: prednisona 40-50 mg VO o metilprednisolona IV 5-7 dias.<br>"
    "4) <b>Bromuro de ipratropio</b> nebulizado si severa.<br>"
    "5) <b>Magnesio IV</b> 2 g en 20 min si severa refractaria.<br>"
    "6) Considerar <b>ventilacion no invasiva</b> o intubacion si fallo respiratorio.<br>"
    "7) Post-alta: revisar tecnica inhaladora, plan accion, controlador (ICS-formoterol SMART).<br>"
    "<b>GINA 2024</b>: track 1 preferido = <b>ICS-formoterol SMART</b> (mantenimiento + rescate)."
    '<span class="ecoe">ECOE: "Asma severo: SABA + corticoide sistemico + ipratropio + Mg IV si refractario."</span>',
    C4 + ["asma"])

add_qa(deck_c4,
    "Manejo: <b>NAC</b> (ATS/IDSA 2019)",
    "<b>Decidir setting con CURB-65</b>: 0-1 ambulatorio, 2 hospital, &gt;=3 considerar UCI.<br>"
    "<b>ATB empirico</b>:<br>"
    "- <b>Ambulatorio sano</b>: amoxicilina 1 g c/8 h, o doxiciclina, o macrolido (si resistencia local &lt;25%).<br>"
    "- <b>Ambulatorio con comorbilidades</b>: amox-clav o cefalosporina + macrolido; o monoterapia con quinolona respiratoria (levo/moxifloxacino).<br>"
    "- <b>Hospital (no UCI)</b>: B-lactamico (ceftriaxona, ampicilina-sulbactam, ceftarolina) + macrolido; o quinolona respiratoria monoterapia.<br>"
    "- <b>UCI</b>: B-lactamico + macrolido o B-lactamico + quinolona respiratoria.<br>"
    "&nbsp;&nbsp;- Si MRSA o Pseudomonas riesgo: anadir vanco/linezolid o pip-tazo/cefepime.<br>"
    "<b>Duracion</b>: minimo 5 dias, hasta 48-72 h afebril; revisar a las 48-72 h.<br>"
    "Vacunacion neumococica + influenza al alta."
    '<span class="ecoe">ECOE: "NAC: CURB-65 + ATB segun setting + vacunacion."</span>',
    C4 + ["nac"])

# --- ERC (3)
add_qa(deck_c4,
    "Manejo: <b>ERC</b> (KDIGO 2024)",
    "<b>Pilares</b>:<br>"
    "1) <b>IECA o ARA-II</b> dosis maxima tolerada (titular K y Cr).<br>"
    "2) <b>iSGLT2</b> (dapagliflozina, empagliflozina) - nefroproteccion en TFG &gt;=20 (incluso sin DM).<br>"
    "3) <b>Finerenona</b> (ARM no esteroideo) en DM con albuminuria persistente pese a IECA/ARA-II maximo.<br>"
    "4) <b>Control PA &lt;130/80 (mejor SBP &lt;120 si tolerado, KDIGO 2021)</b>.<br>"
    "5) <b>Control glucemico</b> en DM.<br>"
    "6) <b>Estatina</b> en TFG &lt;60 sin dialisis.<br>"
    "7) Manejo de complicaciones: anemia (EPO + hierro), alteraciones mineral-oseo (vitD, quelantes fosfato), acidosis (bicarbonato), hiperK (dieta + quelantes).<br>"
    "8) Vacunacion (influenza, neumo, HBV, herpes zoster); evitar nefrotoxicos.<br>"
    "9) Referir a nefrologia si TFG &lt;30 o A3 o progresion rapida; preparar acceso vascular si TFG &lt;20."
    '<span class="ecoe">ECOE: "ERC = IECA/ARA-II + iSGLT2 + control PA + control DM + tratamiento complicaciones."</span>',
    C4 + ["erc"])

add_qa(deck_c4,
    "Manejo: <b>Anemia en ERC</b> (KDIGO 2024)",
    "1) <b>Evaluar y corregir deficits</b>: ferritina &gt;100 (no dialisis) o &gt;200 (dialisis), saturacion transferrina &gt;20%; tratar B12/folato si bajos.<br>"
    "2) <b>Hierro</b>: VO si tolerado y deficit leve; IV si malabsorcion/intolerancia o dialisis.<br>"
    "3) <b>ESA (agentes estimulantes de eritropoyesis: EPO, darbepoetina)</b>:<br>"
    "&nbsp;&nbsp;- Iniciar si Hb &lt;10 g/dL.<br>"
    "&nbsp;&nbsp;- Meta Hb 10-11.5 g/dL (no &gt;13 por riesgo CV).<br>"
    "&nbsp;&nbsp;- Vigilar PA (puede empeorar HTA).<br>"
    "4) <b>HIF-PHI</b> (inhibidores del HIF prolil hidroxilasa - roxadustat) opcion VO emergente."
    '<span class="ecoe">ECOE: "Anemia ERC: corregir hierro/B12/folato; EPO si Hb &lt;10, meta 10-11.5."</span>',
    C4 + ["erc", "anemia"])

add_qa(deck_c4,
    "Manejo: <b>HiperK aguda con cambios ECG</b>",
    "1) <b>Gluconato de calcio 10% 10 mL IV</b> en 2-3 min - <b>estabiliza membrana cardiaca</b> (efecto rapido, no reduce K).<br>"
    "2) <b>Redistribucion intracelular</b>:<br>"
    "&nbsp;&nbsp;- Insulina regular 10 U IV + glucosa 25 g (D50W 50 mL).<br>"
    "&nbsp;&nbsp;- Salbutamol nebulizado 10-20 mg.<br>"
    "&nbsp;&nbsp;- Bicarbonato de sodio si acidosis metabolica.<br>"
    "3) <b>Eliminacion</b>:<br>"
    "&nbsp;&nbsp;- Furosemida IV si funcion renal preservada.<br>"
    "&nbsp;&nbsp;- Resinas (patiromer, ciclosilicato de zirconio - mas modernos y mejor tolerados que kayexalate).<br>"
    "&nbsp;&nbsp;- <b>Hemodialisis</b> si K muy alto refractario, ERC avanzada, o intoxicacion.<br>"
    "4) Suspender medicamentos que retienen K (IECA, ARA-II, ARM, AINE, heparina, trimetoprim)."
    '<span class="ecoe">ECOE: "HiperK con ECG: calcio YA + insulina-glucosa + beta2 + diuretico/resina/dialisis."</span>',
    C4 + ["hiperk"])

# --- HEPATOLOGIA (4)
add_qa(deck_c4,
    "Manejo: <b>Cirrosis con ascitis</b>",
    "1) <b>Restriccion sodio dietetico</b> &lt;2 g/d.<br>"
    "2) <b>Diuretico</b>: espironolactona 100 mg/d + furosemida 40 mg/d (ratio 100:40); titular hasta perdida 0.5 kg/d (1 kg si edema).<br>"
    "3) <b>Paracentesis terapeutica</b> si ascitis grado 3 (a tension); &gt;5 L = administrar <b>albumina 6-8 g/L extraido</b> para prevenir disfuncion circulatoria post-paracentesis.<br>"
    "4) <b>Restriccion liquidos</b> a 1-1.5 L/d si Na &lt;125.<br>"
    "5) Evaluar <b>TIPS</b> si ascitis refractaria.<br>"
    "6) Cribado <b>SBP</b> con paracentesis diagnostica (PMN &gt;=250) en ingreso o sintomas; profilaxis SBP secundaria con norfloxacino o ciprofloxacino.<br>"
    "7) Evaluar trasplante hepatico segun MELD."
    '<span class="ecoe">ECOE: "Cirrosis con ascitis: restriccion Na + esp/furo + paracentesis con albumina."</span>',
    C4 + ["cirrosis", "ascitis"])

add_qa(deck_c4,
    "Manejo: <b>Profilaxis y tratamiento de PBE (peritonitis bacteriana espontanea)</b>",
    "<b>Diagnostico</b>: PMN en liquido ascitico &gt;=250/mm3 (con o sin sintomas).<br>"
    "<b>Tratamiento</b>:<br>"
    "- <b>Cefotaxima 2 g IV c/8 h</b> o ceftriaxona 2 g IV c/24 h x 5-7 dias.<br>"
    "- <b>Albumina 1.5 g/kg dia 1 + 1 g/kg dia 3</b> si Cr &gt;1 o bili &gt;4 (reduce sindrome hepatorrenal).<br>"
    "<b>Profilaxis primaria</b>:<br>"
    "- Sangrado variceal -> ceftriaxona 1 g/d x 7 d.<br>"
    "- Proteina ascitis &lt;1.5 + disfuncion (Child C o renal) -> norfloxacino 400 mg/d.<br>"
    "<b>Profilaxis secundaria</b>: norfloxacino 400 mg/d indefinida o ciprofloxacino."
    '<span class="ecoe">ECOE: "PBE: cefotaxima + albumina; profilaxis 2a con quinolona."</span>',
    C4 + ["cirrosis", "pbe"])

add_qa(deck_c4,
    "Manejo: <b>Encefalopatia hepatica</b>",
    "1) <b>Identificar y corregir precipitante</b>: sangrado digestivo, infeccion (SBP, ITU, neumonia), hipoK, deshidratacion, estrenimiento, sedantes/opioides, transgresion proteica, TIPS.<br>"
    "2) <b>Lactulosa</b> VO o por SNG 25-30 mL c/1-2 h hasta 2-3 deposiciones blandas/d; meta = mantener 2-3 deposiciones/d.<br>"
    "3) <b>Rifaximina 550 mg c/12 h</b> anadida o como segunda linea para reducir recurrencia.<br>"
    "4) Soporte general (proteccion via aerea si Glasgow bajo).<br>"
    "5) Evitar restriccion proteica prolongada (sarcopenia)."
    '<span class="ecoe">ECOE: "Encefalopatia: lactulosa + rifaximina + corrijo precipitante."</span>',
    C4 + ["cirrosis", "encefalopatia"])

add_qa(deck_c4,
    "Manejo: <b>MASLD/MASH</b>",
    "1) <b>Perdida de peso 7-10%</b> (objetivo principal) - dieta mediterranea + ejercicio.<br>"
    "2) <b>Control comorbilidades</b>: DM (metformina, GLP-1, iSGLT2 - beneficio hepatico), HTA, dislipidemia (estatinas SEGURAS en MASLD; ASCVD prevalente).<br>"
    "3) <b>Vacunacion HAV/HBV</b>.<br>"
    "4) Evitar alcohol y hepatotoxicos.<br>"
    "5) <b>Resmetirom</b> (agonista THR-beta) aprobado FDA 2024 para MASH con fibrosis F2-F3.<br>"
    "6) <b>Semaglutide y tirzepatide</b> mejoran esteatosis y NASH.<br>"
    "7) <b>Cirugia bariatrica</b> en MASH con obesidad severa.<br>"
    "8) Vigilancia HCC si cirrosis (USG + AFP cada 6 m)."
    '<span class="ecoe">ECOE: "MASLD: perdida peso + control DM/lipidos; resmetirom o GLP-1 en MASH avanzada."</span>',
    C4 + ["masld"])

# --- ANEMIAS (3)
add_qa(deck_c4,
    "Manejo: <b>Anemia ferropenica</b>",
    "1) <b>Identificar y tratar causa</b> (obligatorio en adulto):<br>"
    "&nbsp;&nbsp;- <b>Sangrado digestivo</b>: endoscopia + colonoscopia en adulto, especialmente &gt;50 a y/o sintomas.<br>"
    "&nbsp;&nbsp;- Menstruacion abundante (mujer fertil).<br>"
    "&nbsp;&nbsp;- Malabsorcion (celiaca, gastrectomia).<br>"
    "&nbsp;&nbsp;- Dieta inadecuada.<br>"
    "2) <b>Reposicion VO</b>: sulfato ferroso 325 mg (65 mg Fe elemental) 1-3 veces/d <b>en ayuno con vitamina C</b>; dia alterno puede ser mejor tolerado y absorbido (Stoffel 2017).<br>"
    "3) <b>Hierro IV</b> (carboximaltosa, sacarosa, hierro dextran): si intolerancia VO, malabsorcion, ERC, IC, perdidas masivas, embarazo 2do-3er trim refractario.<br>"
    "4) <b>Transfusion</b> si Hb &lt;7 (o &lt;8 con cardiopatia) o sintomatica.<br>"
    "5) Reevaluar Hb a 4-6 sem; continuar 3-6 meses tras Hb normal para llenar depositos."
    '<span class="ecoe">ECOE: "Ferropenica: hierro VO + endoscopia/colonoscopia OBLIGADA en adulto."</span>',
    C4 + ["anemia", "ferropenica"])

add_qa(deck_c4,
    "Manejo: <b>Deficit de B12</b>",
    "1) <b>Identificar causa</b>: anemia perniciosa (anti-FI, anti-celulas parietales), gastrectomia, ileitis/reseccion ileal, vegetarianos estrictos, metformina, IBP cronicos, sobrecrecimiento bacteriano.<br>"
    "2) <b>Tratamiento</b>:<br>"
    "&nbsp;&nbsp;- <b>Cianocobalamina IM 1000 mcg</b>: diaria x 1 sem, semanal x 4-8 sem, mensual de por vida (si causa cronica como perniciosa).<br>"
    "&nbsp;&nbsp;- Alternativa VO 1000-2000 mcg/d (incluso en perniciosa funciona, absorcion pasiva).<br>"
    "3) <b>NUNCA reponer folato sin descartar B12</b> primero (puede empeorar neuropatia irreversible).<br>"
    "4) Seguimiento: respuesta hematologica en sem (reticulocitos en 7 d); neurologica meses, puede no ser completa."
    '<span class="ecoe">ECOE: "B12: descarto causa, repongo IM o VO altas dosis; nunca folato solo."</span>',
    C4 + ["anemia", "b12"])

add_qa(deck_c4,
    "Estudio: <b>Anemia ferropenica en adulto - estudio digestivo OBLIGADO</b>",
    "<b>Toda anemia ferropenica en adulto requiere descartar sangrado digestivo</b>, especialmente:<br>"
    "- Varon de cualquier edad.<br>"
    "- Mujer postmenopausica.<br>"
    "- Mujer fertil sin causa ginecologica clara.<br>"
    "<b>Estudio</b>: <b>endoscopia alta + colonoscopia</b> (orden segun sintomas).<br>"
    "- Si ambas negativas y persiste sangrado oculto: capsula endoscopica o enteroscopia (intestino delgado).<br>"
    "- Considerar celiaca: anti-transglutaminasa.<br>"
    "- Considerar H. pylori, sobrecrecimiento bacteriano.<br>"
    "Buscar siempre <b>neoplasia colorrectal</b> como diagnostico potencial."
    '<span class="ecoe">ECOE: "Ferropenica adulto = endoscopia + colonoscopia OBLIGATORIA para descartar neoplasia."</span>',
    C4 + ["anemia", "estudio"])

# --- REUMATO (3)
add_qa(deck_c4,
    "Manejo: <b>Gota aguda y profilaxis</b> (ACR 2020)",
    "<b>Gota aguda (cualquiera de los 3)</b>:<br>"
    "1) <b>AINE</b> (naproxeno 500 mg c/12 h) - evitar si ERC, ulcera, anticoagulado.<br>"
    "2) <b>Colchicina</b> 1.2 mg + 0.6 mg en 1 h luego 0.6 mg c/12 h.<br>"
    "3) <b>Corticoide</b>: prednisona 30-40 mg/d x 5 d (sistemico), o triamcinolona intraarticular.<br><br>"
    "<b>Tratamiento hipouricemiante a largo plazo</b> (indicaciones ACR: &gt;=2 ataques/ano, tofos, dano renal por uratos, gota tofacea, ERC G3, urolitiasis):<br>"
    "- <b>Alopurinol</b> 100 mg/d titular (ajustar TFG); meta urato &lt;6 mg/dL (5 si tofos).<br>"
    "- Febuxostat alternativa (precaucion CV).<br>"
    "- <b>Profilaxis con colchicina 0.6 mg/d (o AINE bajo dosis) los primeros 3-6 meses</b> al iniciar hipouricemiante (evita ataques por mobilizacion uratos).<br>"
    "- Cambios estilo de vida: bajar OH (especialmente cerveza), evitar carnes rojas/mariscos, suspender tiazida si posible."
    '<span class="ecoe">ECOE: "Gota aguda: AINE/colchicina/corticoide; alopurinol cronico con colchicina profilactica."</span>',
    C4 + ["gota"])

add_qa(deck_c4,
    "Manejo: <b>Artritis reumatoide</b>",
    "1) <b>Metotrexato</b> como FAME ancla (7.5-25 mg/sem VO o SC) + acido folico.<br>"
    "2) <b>AINE</b> y/o corticoide a bajas dosis (puente sintomatico - no monoterapia cronica).<br>"
    "3) <b>Si refractaria o alta actividad</b> -&gt; combinar FAMEs (triple terapia: MTX + sulfasalazina + hidroxicloroquina) o anadir <b>biologico</b>:<br>"
    "&nbsp;&nbsp;- <b>Anti-TNF</b> (etanercept, adalimumab, infliximab) primera linea biologica.<br>"
    "&nbsp;&nbsp;- IL-6 (tocilizumab), abatacept, rituximab segun escenarios.<br>"
    "&nbsp;&nbsp;- Inhibidores JAK (tofacitinib, baricitinib) VO; precaucion CV/tromboembolica (ORAL Surveillance).<br>"
    "4) Tamizaje pre-biologico: TBC latente (PPD/IGRA), HBV, HCV, vacunas.<br>"
    "5) Monitoreo DAS28; perfil hepatico/renal/BH con MTX cada 2-3 meses."
    '<span class="ecoe">ECOE: "AR: MTX primera linea + AINE/corticoide puente; biologico si refractario."</span>',
    C4 + ["ar"])

add_qa(deck_c4,
    "Manejo: <b>Polimialgia reumatica y arteritis temporal</b>",
    "<b>PMR (sin arteritis)</b>:<br>"
    "- <b>Prednisona 12.5-25 mg/d</b>, descenso lento (1 mg/mes) tras respuesta clinica y VSG.<br>"
    "- Duracion tipica 1-2 anos.<br>"
    "- Profilaxis osteoporosis con corticoide (calcio, vitamina D, bifosfonato si alto riesgo).<br><br>"
    "<b>Arteritis temporal/gigantocelular</b>:<br>"
    "- <b>Prednisona 40-60 mg/d INMEDIATAMENTE</b> ante sospecha (no esperar biopsia - riesgo ceguera).<br>"
    "- Si afectacion visual: <b>metilprednisolona IV 500-1000 mg x 3 dias</b> luego oral.<br>"
    "- <b>Biopsia de arteria temporal</b> en primeras 1-2 sem (positiva incluso tras iniciar esteroide).<br>"
    "- <b>Tocilizumab</b> SC anadido permite descenso mas rapido de corticoide (GiACTA).<br>"
    "- ASA 81 mg si no contraindicacion."
    '<span class="ecoe">ECOE: "Arteritis temporal sospechada = prednisona YA, biopsia despues."</span>',
    C4 + ["pmr", "arteritis_temporal"])

# --- ENDOCARDITIS Y SEPSIS (3)
add_qa(deck_c4,
    "Manejo: <b>Endocarditis infecciosa</b>",
    "1) <b>Hemocultivos seriados (3 sets de sitios distintos)</b> antes de antibiotico.<br>"
    "2) <b>Eco transtoracico</b>; si dudoso, <b>eco transesofagico</b> (mas sensible, sobre todo en protesis).<br>"
    "3) <b>ATB empirico</b> (segun sospecha) tras cultivos:<br>"
    "&nbsp;&nbsp;- <b>Valvula nativa subaguda</b>: <b>ampicilina + gentamicina + ceftriaxona</b> (cobertura S. viridans, enterococo, HACEK).<br>"
    "&nbsp;&nbsp;- <b>Valvula nativa aguda o IV drogas</b>: <b>vancomicina + cefepime/ceftriaxona</b> (cubrir S. aureus incluido MRSA).<br>"
    "&nbsp;&nbsp;- <b>Valvula protesica</b>: <b>vancomicina + gentamicina + rifampicina + cefepime</b>.<br>"
    "4) <b>Ajustar segun cultivos</b>; duracion 4-6 sem habitualmente.<br>"
    "5) <b>Profilaxis ATB endocarditis</b> (AHA 2007): solo en alto riesgo (protesis valvular, EI previa, cardiopatia congenita cianogena no reparada) ante procedimientos dentales con manipulacion mucosa o respiratorios."
    '<span class="ecoe">ECOE: "EI: 3 hemocultivos, eco, ATB empirico segun sospecha, duracion 4-6 sem."</span>',
    C4 + ["endocarditis"])

add_qa(deck_c4,
    "Indicaciones <b>quirurgicas en endocarditis</b>",
    "<b>Cirugia temprana (en hospitalizacion)</b>:<br>"
    "1) <b>IC por disfuncion valvular severa</b> (mas frecuente).<br>"
    "2) <b>Infeccion no controlada</b>: persistencia &gt;7-10 d pese a ATB, microorganismos virulentos (S. aureus, hongos), absceso/fistula.<br>"
    "3) <b>Prevencion de embolia</b>: vegetacion &gt;10 mm movil pese a ATB con embolia previa, o vegetacion &gt;15 mm.<br>"
    "4) Endocarditis sobre valvula protesica con disfuncion o dehiscencia.<br>"
    "5) Endocarditis fungica casi siempre."
    '<span class="ecoe">ECOE: "EI quirurgica: IC, infeccion no controlada, vegetacion grande con embolia."</span>',
    C4 + ["endocarditis", "cirugia"])

add_qa(deck_c4,
    "Manejo: <b>Sepsis</b> - bundle hora-1 (Surviving Sepsis Campaign 2021)",
    "Dentro de la <b>primera hora</b>:<br>"
    "1) <b>Medir lactato</b>; re-medir si &gt;2 mmol/L.<br>"
    "2) <b>Hemocultivos antes de antibiotico</b> (si no retrasa).<br>"
    "3) <b>Antibiotico de amplio espectro IV</b> inmediato (segun foco sospechado).<br>"
    "4) <b>Cristaloide balanceado 30 mL/kg</b> en hipotension o lactato &gt;=4.<br>"
    "5) <b>Vasopresor (norepinefrina primera linea)</b> si hipotension no responde; meta PAM &gt;=65 mmHg.<br>"
    "6) <b>Control del foco</b> (drenaje, cirugia) tan pronto factible.<br>"
    "Reevaluacion continua de perfusion (llenado capilar, diuresis, lactato).<br>"
    "Corticoides (hidrocortisona 200 mg/d) en shock septico que requiere vasopresor."
    '<span class="ecoe">ECOE: "Bundle hora 1: lactato + cultivos + ATB + fluido 30 mL/kg + vasopresor + control foco."</span>',
    C4 + ["sepsis"])

# --- ITU (2)
add_qa(deck_c4,
    "Manejo: <b>ITU no complicada vs complicada</b>",
    "<b>Cistitis no complicada (mujer joven no embarazada)</b>:<br>"
    "- <b>Nitrofurantoina 100 mg c/12 h x 5 d</b> (primera linea).<br>"
    "- Fosfomicina 3 g dosis unica.<br>"
    "- TMP/SMX 160/800 c/12 h x 3 d (si resistencia local &lt;20%).<br>"
    "- Evitar quinolonas en cistitis no complicada (toxicidad, ecologia).<br><br>"
    "<b>Cistitis complicada (varon, embarazo, DM, sonda, anatomia anormal, instrumentacion, inmunosuprimido)</b>:<br>"
    "- Urocultivo OBLIGATORIO.<br>"
    "- ATB 7-14 dias.<br>"
    "- Esquemas: nitrofurantoina, TMP/SMX, amox-clav, cefalosporina, o quinolona segun susceptibilidad.<br>"
    "<b>Bacteriuria asintomatica</b>: solo tratar en embarazo y pre-procedimientos urologicos."
    '<span class="ecoe">ECOE: "Cistitis no compl = nitrofurantoina 5 d; complicada = urocultivo + 7-14 d."</span>',
    C4 + ["itu"])

add_qa(deck_c4,
    "Manejo: <b>Pielonefritis aguda</b>",
    "1) <b>Hospitalizar si</b>: sepsis, intolerancia oral, embarazo, comorbilidades severas, ITU complicada, sospecha de obstruccion.<br>"
    "2) <b>Urocultivo + hemocultivos</b> (sepsis).<br>"
    "3) <b>ATB empirico IV</b>:<br>"
    "&nbsp;&nbsp;- <b>Ceftriaxona 1-2 g/d</b> o ceftazidima.<br>"
    "&nbsp;&nbsp;- Ampicilina + gentamicina si enterococo sospecha.<br>"
    "&nbsp;&nbsp;- Pip-tazo o carbapenem si sepsis grave o resistencia conocida.<br>"
    "4) <b>Transicion VO</b> tras 48 h afebril con sensibilidades: cipro o TMP/SMX 7-14 d totales.<br>"
    "5) <b>USG/TAC si</b> no mejora en 48-72 h, sospecha de obstruccion, urolitiasis, absceso.<br>"
    "6) Ambulatorio leve estable: ciprofloxacino 500 mg c/12 h o levofloxacino 750 mg/d x 7 d."
    '<span class="ecoe">ECOE: "PNA hospitalizada: ceftriaxona IV, transicion VO a 48 h afebril, imagen si no mejora."</span>',
    C4 + ["pna"])

# --- DDX (8)
add_qa(deck_c4,
    "DDx: <b>Dolor toracico agudo</b>",
    "<b>Potencialmente mortales (descartar primero)</b>:<br>"
    "- <b>SCA (IAM)</b>: opresivo, irradiacion brazo/mandibula, diaforesis - ECG + troponina.<br>"
    "- <b>TEP</b>: pleuritico, disnea subita, factores Virchow - Wells, dimero D, angio-TC.<br>"
    "- <b>Diseccion aortica</b>: desgarrante, irradiacion espalda, diferencia pulsos - TAC con contraste.<br>"
    "- <b>Neumotorax a tension</b>: subito, disnea, hiperresonancia - clinico + Rx.<br>"
    "- <b>Tamponade</b>: triada de Beck + pulso paradojico - eco.<br><br>"
    "<b>Otros</b>: pericarditis, miocarditis, esofagitis/RGE, espasmo esofagico, costocondritis, herpes zoster, ansiedad, neumonia."
    '<span class="ecoe">ECOE: "Descarto los 5 letales antes de pensar en otros."</span>',
    C4 + ["ddx", "torax"])

add_qa(deck_c4,
    "DDx: <b>Disnea aguda</b>",
    "<b>Cardiaca</b>: IC descompensada, EAP, IAM, arritmia (FA rapida), tamponade.<br>"
    "<b>Pulmonar</b>: asma, EPOC exacerbado, neumonia, TEP, neumotorax, derrame pleural, SDRA.<br>"
    "<b>Sistemica</b>: anemia severa, acidosis (CAD, sepsis), hipertiroidismo, intoxicacion (salicilatos, monoxido).<br>"
    "<b>Funcional/ansiedad</b> - diagnostico de exclusion.<br>"
    "<b>Mecanica</b>: obstruccion via aerea, cuerpo extrano, anafilaxia.<br>"
    "Estudios iniciales: O2/SatO2, gasometria, BNP, ECG, Rx torax, troponina, dimero D segun sospecha."
    '<span class="ecoe">ECOE: "Diferencio cardiaca, pulmonar, sistemica; BNP para apoyar/descartar IC."</span>',
    C4 + ["ddx", "disnea"])

add_qa(deck_c4,
    "DDx: <b>Edema bilateral de miembros inferiores</b>",
    "<b>Cardiaca</b>: IC (S3, IY elevada, BNP alto).<br>"
    "<b>Renal</b>: ERC, sd nefrotico (proteinuria, hipoalbuminemia).<br>"
    "<b>Hepatica</b>: cirrosis (ascitis, estigmas, INR alto).<br>"
    "<b>Hipoalbuminemia</b>: desnutricion, enteropatia perdedora de proteinas.<br>"
    "<b>Farmacos</b>: CCB dihidropiridinicos (amlodipino), AINE, esteroides, pioglitazona, gabapentina.<br>"
    "<b>Endocrina</b>: hipotiroidismo (mixedema), hipertiroidismo (raro), sd Cushing.<br>"
    "<b>Venosa</b>: insuficiencia venosa cronica.<br>"
    "<b>Linfedema</b>."
    '<span class="ecoe">ECOE: "Edemas bilaterales: diferencio sistemico (cardio/renal/hepatico/albumina) vs venoso/linfatico."</span>',
    C4 + ["ddx", "edema"])

add_qa(deck_c4,
    "DDx: <b>Anemia con sangrado oculto en adulto</b>",
    "1) <b>Neoplasia colorrectal</b> (siempre considerar - cribado).<br>"
    "2) <b>Ulcera peptica</b> sangrante cronica (AINE, H. pylori).<br>"
    "3) <b>Gastritis erosiva</b>.<br>"
    "4) <b>Angiodisplasia</b> (mas en mayores, ERC, EAo).<br>"
    "5) <b>Diverticulosis colonica</b> con sangrado lento.<br>"
    "6) <b>EII</b> (colitis ulcerosa, Crohn).<br>"
    "7) <b>Polipos</b>.<br>"
    "8) <b>Celiaca</b> (con malabsorcion).<br>"
    "9) <b>Neoplasia esofagica/gastrica</b>.<br>"
    "10) <b>Sangrado oculto del intestino delgado</b>: capsula endoscopica.<br>"
    "Estudio sistematico: endoscopia alta + colonoscopia."
    '<span class="ecoe">ECOE: "Ferropenica adulto = neoplasia colorrectal hasta demostrar lo contrario."</span>',
    C4 + ["ddx", "anemia"])

add_qa(deck_c4,
    "DDx: <b>Hipokalemia</b>",
    "<b>Perdidas digestivas</b>: vomito (alcalosis), diarrea (acidosis), abuso de laxantes.<br>"
    "<b>Perdidas renales</b>: diureticos (asa, tiazidas), hiperaldosteronismo primario (Conn), sd Cushing, Bartter/Gitelman, RTA tipo 1 y 2.<br>"
    "<b>Redistribucion</b>: insulina + glucosa, beta-agonistas, alcalosis, paralisis periodica hipoK familiar, tirotoxicosis.<br>"
    "<b>Bajo aporte</b>: anorexia, alcoholismo.<br>"
    "<b>Estudio</b>: pH, anion gap, K urinario (TTKG), magnesio (corregir antes que K).<br>"
    "Riesgo: arritmias (torsade), debilidad, ileo."
    '<span class="ecoe">ECOE: "HipoK con vomito o diuretico mas frecuente; corregir Mg primero."</span>',
    C4 + ["ddx", "hipok"])

add_qa(deck_c4,
    "DDx: <b>Hiperkalemia</b>",
    "<b>Disminucion excrecion</b>: AKI/ERC, hipoaldosteronismo (Addison), hiporeninismo (DM, AINE), IECA/ARA-II, ARM, trimetoprim, heparina, ciclosporina/tacrolimus.<br>"
    "<b>Redistribucion al espacio extracelular</b>: acidosis, lisis tumoral, rabdomiolisis, hemolisis, beta-bloqueador, succinilcolina, isquemia.<br>"
    "<b>Pseudohiperkalemia</b>: hemolisis de muestra, leucocitosis/trombocitosis extremas, torniquete prolongado.<br>"
    "<b>Aumento de aporte</b>: dieta + ERC, transfusion masiva, sustitutos sal con K."
    '<span class="ecoe">ECOE: "HiperK: descarto pseudo, AKI/ERC + IECA/ARA-II/ARM frecuentes."</span>',
    C4 + ["ddx", "hiperk"])

add_qa(deck_c4,
    "DDx: <b>Sincope</b>",
    "<b>Reflejo (mas frecuente)</b>: vasovagal (susto, dolor, sangre, miccion), situacional (tos, defecacion).<br>"
    "<b>Ortostatico</b>: deshidratacion, farmacos antihipertensivos, neuropatia autonomica.<br>"
    "<b>Cardiaco (mas grave)</b>:<br>"
    "&nbsp;&nbsp;- Arritmico: bradiarritmia (BAV, disfuncion sinusal), taquiarritmia (TV, TSV).<br>"
    "&nbsp;&nbsp;- Estructural: EAo, MHO, mixoma, TEP, IAM, tamponade.<br>"
    "<b>Cerebrovascular</b>: muy raro como sincope puro; sd de robo de subclavia.<br>"
    "<b>Otras</b>: hipoglucemia, anemia severa.<br>"
    "<b>Rojas en evaluacion</b>: con ejercicio, sin prodromo, decubito, antecedente familiar muerte subita, soplo, ECG anormal."
    '<span class="ecoe">ECOE: "Sincope con red flags = ingreso para estudio cardiologico."</span>',
    C4 + ["ddx", "sincope"])

add_qa(deck_c4,
    "DDx: <b>Fiebre de origen desconocido (FUO)</b>",
    "Definicion clasica (Petersdorf): fiebre &gt;38.3 documentada en multiples ocasiones, &gt;3 semanas, sin diagnostico tras estudio adecuado.<br>"
    "<b>Categorias</b>:<br>"
    "1) <b>Infecciones (40%)</b>: TBC (incluso extrapulmonar), endocarditis, abscesos ocultos (intraabd, dental, sinusal), VIH, CMV/EBV, brucelosis, malaria.<br>"
    "2) <b>Neoplasias (20-30%)</b>: linfomas, leucemias, hepatocarcinoma, renal, mielodisplasia.<br>"
    "3) <b>Autoinmunes/inflamatorias (10-20%)</b>: arteritis temporal, polimialgia reumatica, LES, AR, enf de Still, sd Bechet, vasculitis.<br>"
    "4) <b>Otras</b>: fiebre por farmacos, tromboflebitis, hipertiroidismo, sd hereditarios (fiebre mediterranea).<br>"
    "5) <b>Sin diagnostico</b>: 30%.<br>"
    "<b>Estudio escalonado</b>: H+EF detallada (incluso fondo de ojo, tacto rectal/genital, busqueda nodulos), BH+VSG+PCR+procalcitonina, cultivos, serologias, autoinmunidad, TAC torax-abdomen-pelvis, PET-TC (cada vez mas usado)."
    '<span class="ecoe">ECOE: "FUO: estudio escalonado infeccion/neoplasia/autoinmune; PET-TC util."</span>',
    C4 + ["ddx", "fuo"])

# --- INTEGRACION (4)
add_qa(deck_c4,
    "Cribado en adulto (USPSTF actualizado)",
    "<b>Mama</b>: mamografia bianual mujer 40-74 (USPSTF 2024 bajo edad inicial a 40).<br>"
    "<b>Cervix</b>: Pap cada 3 anos 21-29; Pap c/3 a + co-test (Pap+VPH) c/5 a o VPH solo c/5 a en 30-65; suspender &gt;65 si historial adecuado.<br>"
    "<b>Colon</b>: 45-75 anos - colonoscopia c/10, sigmoidoscopia c/5, SOH anual, FIT anual, FIT-DNA c/1-3 a.<br>"
    "<b>Pulmon</b>: TAC torax baja dosis anual en 50-80 a con &gt;=20 paquetes-ano y fumador actual o que dejo &lt;15 a.<br>"
    "<b>AAA</b>: USG abdominal 1 vez en varones 65-75 fumadores.<br>"
    "<b>Lipidos/RCV</b>: cribado adultos &gt;=40 con factores; ASCVD calculator.<br>"
    "<b>DM</b>: 35-70 con sobrepeso/obesidad cada 3 anos.<br>"
    "<b>HTA</b>: anual &gt;=18 (mas frecuente si elevada).<br>"
    "<b>Osteoporosis</b>: DEXA mujer &gt;=65 o postmenopausica con FRAX alto.<br>"
    "<b>VIH</b>: una vez 15-65 (mas si riesgo)."
    '<span class="ecoe">ECOE: "Conozco cribados USPSTF para adulto."</span>',
    C4 + ["cribado"])

add_qa(deck_c4,
    "Vacunacion en adulto cronico (CDC/ACIP 2025)",
    "<b>Anual</b>: influenza inactivada (alta dosis &gt;=65 o adyuvada).<br>"
    "<b>Neumococo</b>: <b>PCV20 dosis unica</b> (preferido); o PCV15 + PPSV23 a 1 ano. Indicado &gt;=65 o &lt;65 con comorbilidades.<br>"
    "<b>Herpes zoster</b>: <b>Shingrix (recombinante) 2 dosis</b> &gt;=50 anos (incluso inmunocompetentes); preferido sobre Zostavax.<br>"
    "<b>Td/Tdap</b>: cada 10 anos; Tdap una vez (sustituir Td).<br>"
    "<b>HBV</b>: 3 dosis si no inmune y factor de riesgo (DM, ERC, HCV, conductas, trabajador salud).<br>"
    "<b>COVID-19</b>: actualizado segun ACIP/CDC vigente.<br>"
    "<b>VPH</b>: hasta 26 a; valorar individual 27-45.<br>"
    "<b>VSR</b>: &gt;=60 a (decision compartida; obligatoria si comorbilidad cardio-pulmonar)."
    '<span class="ecoe">ECOE: "Vacunacion en adulto cronico: influenza, neumo, zoster, Tdap, HBV si riesgo."</span>',
    C4 + ["vacunacion"])

add_qa(deck_c4,
    "Manejo: <b>Suspension perioperatoria de anticoagulantes/antiagregantes</b>",
    "<b>Antiagregantes</b>:<br>"
    "- ASA: continuar en cirugia con alto riesgo CV (vascular, cardiaca); suspender 7-10 d en cirugias con alto riesgo hemorragico (neuroquirurgia).<br>"
    "- Clopidogrel: suspender 5-7 d antes.<br>"
    "- Ticagrelor: 3-5 d.<br>"
    "- Stent reciente (BMS &lt;1 mes, DES &lt;3-6 m): no suspender DAPT - diferir cirugia electiva.<br><br>"
    "<b>Anticoagulantes</b>:<br>"
    "- Warfarina: suspender 5 d antes; <b>bridging</b> con HBPM solo si alto riesgo trombotico (FA con CHA2DS2-VASc alto + valvular, valvula mecanica mitral, TEV reciente &lt;3 m).<br>"
    "- DOAC: suspender 24-48 h (riesgo bajo de sangrado) o 48-72 h (alto riesgo) segun TFG; <b>no requiere bridging</b> rutinario.<br>"
    "<b>Riesgo quirurgico CV: RCRI o Lee score</b>."
    '<span class="ecoe">ECOE: "DOAC: 24-48 h pre-cirugia, sin bridging; warfarina: bridging si alto riesgo."</span>',
    C4 + ["perioperatorio"])

add_qa(deck_c4,
    "Resumen integral: <b>Plan del paciente cronico complejo en ECOE</b>",
    "<b>Estructura de presentacion al sinodal</b>:<br><br>"
    "1) <b>Diagnostico sindromico</b>: \"Paciente con alto riesgo cardiovascular global por convergencia de factores: HTA + DM2 + dislipidemia + tabaquismo + alcoholismo + alteracion hepatica + anemia.\"<br><br>"
    "2) <b>Eje dominante</b>: \"Prioridad = reduccion del riesgo cardiovascular.\"<br><br>"
    "3) <b>Plan terapeutico jerarquizado</b>:<br>"
    "&nbsp;&nbsp;a) Estatina alta intensidad.<br>"
    "&nbsp;&nbsp;b) IECA/ARA-II para HTA + nefroproteccion.<br>"
    "&nbsp;&nbsp;c) Metformina + iSGLT2/GLP-1 segun perfil.<br>"
    "&nbsp;&nbsp;d) Cesar tabaco (counseling 5A + farmacoterapia).<br>"
    "&nbsp;&nbsp;e) Reducir alcohol (AUDIT + intervencion breve).<br>"
    "&nbsp;&nbsp;f) Suspender AINE.<br><br>"
    "4) <b>Estudios complementarios</b>:<br>"
    "&nbsp;&nbsp;a) Perfil hepatico completo + USG hepatico + serologias hepatitis.<br>"
    "&nbsp;&nbsp;b) BH + VCM + ferritina; endoscopia/colonoscopia si ferropenica.<br>"
    "&nbsp;&nbsp;c) Creatinina + TFG + ratio albumina/Cr.<br>"
    "&nbsp;&nbsp;d) Perfil lipidico, HbA1c, electrolitos.<br>"
    "&nbsp;&nbsp;e) ECG.<br><br>"
    "5) <b>Seguimiento estructurado</b>: 4-6 semanas con laboratorios; visitas trimestrales el primer ano.<br><br>"
    "6) <b>Cribado preventivo</b> apropiado para edad (USPSTF) + vacunacion (CDC)."
    '<span class="ecoe">ECOE: "Estructura clara: diagnostico, eje, plan jerarquizado, estudios, seguimiento, prevencion."</span>',
    C4 + ["cronico_complejo", "resumen"])


# ============================================================
# Build packages
# ============================================================
def build():
    decks = [
        (deck_c1, "Medicina_Interna_Adulto_Capa1.apkg"),
        (deck_c2, "Medicina_Interna_Adulto_Capa2.apkg"),
        (deck_c3, "Medicina_Interna_Adulto_Capa3.apkg"),
        (deck_c4, "Medicina_Interna_Adulto_Capa4.apkg"),
    ]
    for d, fname in decks:
        pkg = genanki.Package(d)
        out = os.path.join(OUTPUT_DIR, fname)
        pkg.write_to_file(out)
        print(f"  -> {fname} ({len(d.notes)} notas)")

    combined = genanki.Package([deck_c1, deck_c2, deck_c3, deck_c4])
    combined_out = os.path.join(OUTPUT_DIR, "Medicina_Interna_Adulto_TODOS.apkg")
    combined.write_to_file(combined_out)
    total = sum(len(d.notes) for d in [deck_c1, deck_c2, deck_c3, deck_c4])
    print(f"  -> Medicina_Interna_Adulto_TODOS.apkg ({total} notas totales)")


if __name__ == "__main__":
    build()
