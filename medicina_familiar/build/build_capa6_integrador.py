"""Capa 6 - Integrador de Discriminador Clinico (Medicina Familiar Adulto).

Formato Q&A:
- Front: localizacion de exploracion + 3 discriminadores clinicos clave.
- Back: diagnostico + tip ECOE.

Pedagogia: invierte el flujo de aprendizaje. En lugar de "dado el dx -> recordar
clinica", se entrena "dado el hallazgo en exploracion -> disparar dx".
Util para ECOE donde el sinodal describe una escena y la alumna debe nombrar
el dx en segundos.

Guia: USPSTF + ADA 2025 + ACC/AHA + IDSA + GOLD 2024 + GINA 2024 (misma base que C1-C5).
"""
import os
import genanki

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "output")
os.makedirs(OUTPUT_DIR, exist_ok=True)

MODEL_QA_ID = 1607392320  # reusable Q&A
DECK_ID = 1184046378
DECK_NAME = "Medicina Familiar Adulto::Capa 6 - Integrador de Discriminador Clinico"

CSS_BASE = """
.card {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  font-size: 19px; text-align: left; color: #1a1a1a;
  background-color: #fafafa; padding: 20px; line-height: 1.55;
}
.loc {
  display: inline-block; padding: 4px 12px; margin-bottom: 14px;
  background: #1e3a8a; color: #fff; border-radius: 6px;
  font-size: 14px; letter-spacing: 0.5px; font-weight: 600;
}
ul.disc { margin: 8px 0 18px 0; padding-left: 22px; }
ul.disc li { margin: 6px 0; }
.prompt { color: #2563eb; font-weight: 600; margin-top: 10px; }
.dx { font-size: 22px; font-weight: 700; color: #047857; margin-top: 4px; }
.ecoe { color: #b45309; font-style: italic; margin-top: 12px; display: block; }
#extra { margin-top: 16px; border: none; border-top: 1px solid #d4d4d4; padding-top: 12px; }
"""

model_qa = genanki.Model(
    MODEL_QA_ID,
    "Estudio Medico QA",
    fields=[{"name": "Front"}, {"name": "Back"}],
    templates=[{
        "name": "QA",
        "qfmt": "{{Front}}",
        "afmt": '{{Front}}<hr id="extra">{{Back}}',
    }],
    css=CSS_BASE,
)

deck = genanki.Deck(DECK_ID, DECK_NAME)

BASE_TAGS = ["medicina_familiar", "ecoe", "capa6", "integrador"]


def front(loc, d1, d2, d3):
    return (
        f'<div class="loc">{loc}</div>'
        f'<ul class="disc"><li>{d1}</li><li>{d2}</li><li>{d3}</li></ul>'
        f'<div class="prompt">&iquest;Diagn&oacute;stico?</div>'
    )


def back(dx, ecoe):
    return (
        f'<div class="dx">{dx}</div>'
        f'<span class="ecoe">ECOE: &laquo;{ecoe}&raquo;</span>'
    )


def add(loc, d1, d2, d3, dx, ecoe, extra_tags):
    note = genanki.Note(
        model=model_qa,
        fields=[front(loc, d1, d2, d3), back(dx, ecoe)],
        tags=BASE_TAGS + extra_tags,
    )
    deck.add_note(note)


# ============================================================
# 1. SIGNOS VITALES + ESTADO GENERAL (6)
# ============================================================
LOC = "SIGNOS VITALES + ESTADO GENERAL"
TAG = ["signos_vitales"]

add(LOC,
    "Fiebre o hipotermia",
    "Taquicardia + taquipnea",
    "Alteracion del estado mental + hipotension (qSOFA &ge;2)",
    "Sepsis",
    "Activar codigo sepsis: lactato, hemocultivos, ATB en la 1a hora.",
    TAG + ["sepsis"])

add(LOC,
    "TA &ge;180/120",
    "Cefalea, vision borrosa o focalidad",
    "Dano de organo blanco agudo (cerebro, corazon, rinon, retina)",
    "Emergencia hipertensiva",
    "IV: labetalol, nicardipino o nitroprusiato; bajar TA 10-20% en la 1a hora.",
    TAG + ["hta_emergencia"])

add(LOC,
    "Respiracion de Kussmaul",
    "Aliento a frutas (cetonas)",
    "Deshidratacion severa + glucemia &gt;250",
    "Cetoacidosis diabetica (DKA)",
    "Hidratacion + insulina IV + reposicion de potasio.",
    TAG + ["dka"])

add(LOC,
    "Diaforesis profusa",
    "Temblor + taquicardia",
    "Alteracion del estado mental que CEDE con glucosa",
    "Hipoglucemia",
    "Glucosa 25 g IV o glucagon IM si no hay acceso.",
    TAG + ["hipoglucemia"])

add(LOC,
    "Fiebre alta",
    "Taquicardia extrema (&gt;130 lpm)",
    "Delirio / agitacion + antecedente de hipertiroidismo",
    "Tormenta tiroidea",
    "Tionamidas + betabloqueador + corticoide + soporte.",
    TAG + ["tormenta_tiroidea"])

add(LOC,
    "Hipotension refractaria a volumen",
    "Hiperpigmentacion mucocutanea",
    "Hiponatremia + hiperpotasemia",
    "Crisis adrenal",
    "Hidrocortisona 100 mg IV de inmediato + volumen.",
    TAG + ["crisis_adrenal"])


# ============================================================
# 2. PIEL Y MUCOSAS (6)
# ============================================================
LOC = "PIEL Y MUCOSAS"
TAG = ["piel_mucosas"]

add(LOC,
    "Palidez de mucosas",
    "Queilosis angular",
    "Glositis depapilada",
    "Anemia ferropenica",
    "BH + ferritina; en adulto sin causa clara, colonoscopia.",
    TAG + ["anemia"])

add(LOC,
    "Escleras amarillas",
    "Coluria",
    "Acolia",
    "Ictericia obstructiva",
    "USG abdominal urgente; descartar coledocolitiasis o tumor periampular.",
    TAG + ["ictericia"])

add(LOC,
    "Ulcera plantar (cabeza de metatarso)",
    "Perdida de sensibilidad al monofilamento",
    "Pulsos pedios disminuidos o ausentes",
    "Pie diabetico",
    "Curacion + descarga + control glucemico + valorar vascular.",
    TAG + ["pie_diabetico"])

add(LOC,
    "Piel seca y aspera",
    "Edema facial periorbitario",
    "Cabello fragil, cola de las cejas escasa",
    "Hipotiroidismo",
    "TSH alta + T4 libre baja; levotiroxina 1.6 mcg/kg/d.",
    TAG + ["hipotiroidismo"])

add(LOC,
    "Piel calida y sudorosa",
    "Temblor fino distal",
    "Exoftalmos + retraccion palpebral + bocio difuso",
    "Hipertiroidismo (enfermedad de Graves)",
    "TSH suprimida + T4/T3 altos; tionamidas + propranolol.",
    TAG + ["hipertiroidismo"])

add(LOC,
    "Cara de luna llena",
    "Estrias violaceas abdominales",
    "Giba dorsal + obesidad central",
    "Sindrome de Cushing",
    "Cortisol salival nocturno o supresion con dexametasona.",
    TAG + ["cushing"])


# ============================================================
# 3. CABEZA, CUELLO Y ORL (8)
# ============================================================
LOC = "CABEZA, CUELLO Y ORL"
TAG = ["orl"]

add(LOC,
    "Exudado amigdalino purulento",
    "Adenopatia cervical anterior dolorosa",
    "AUSENCIA de tos y rinorrea (criterios Centor)",
    "Faringitis estreptococica",
    "Penicilina o amoxicilina 10 dias; prevenir fiebre reumatica.",
    TAG + ["faringitis"])

add(LOC,
    "Rinorrea clara abundante",
    "Tos seca leve",
    "Faringe eritematosa SIN exudado",
    "IVAS viral (resfriado comun)",
    "Manejo sintomatico; NO antibiotico.",
    TAG + ["ivas"])

add(LOC,
    "Fiebre alta de inicio subito",
    "Mialgias intensas + cefalea",
    "Postracion (paciente &laquo;tumbado&raquo;)",
    "Influenza",
    "Oseltamivir si &lt;48 h del inicio o riesgo alto.",
    TAG + ["influenza"])

add(LOC,
    "Rinorrea purulenta",
    "Dolor facial + presion retroocular",
    "Sintomas &gt;10 dias o doble empeoramiento",
    "Sinusitis bacteriana",
    "Amoxicilina-clavulanato 7-10 dias.",
    TAG + ["sinusitis"])

add(LOC,
    "Otalgia profunda",
    "Membrana timpanica abombada y eritematosa",
    "Fiebre (especialmente en nino)",
    "Otitis media aguda",
    "Amoxicilina 80-90 mg/kg/d en nino; observacion 48 h en casos leves.",
    TAG + ["oma"])

add(LOC,
    "Dolor al jalar el pabellon (signo del trago)",
    "Edema y secrecion en CAE",
    "Antecedente de humedad / nado",
    "Otitis externa",
    "Gotas oticas con quinolona +/- corticoide; mantener seco.",
    TAG + ["otitis_externa"])

add(LOC,
    "Aumento glandular tiroideo simetrico",
    "SIN nodulos palpables",
    "Sintomas de hipo o hiperfuncion",
    "Bocio difuso",
    "TSH + T4 libre + USG tiroideo.",
    TAG + ["bocio"])

add(LOC,
    "Nodulo tiroideo unico firme &gt;1 cm",
    "Adenopatia cervical asociada",
    "Disfonia o disfagia",
    "Cancer de tiroides (sospecha)",
    "USG + BAAF; referir a endocrinologia.",
    TAG + ["nodulo_tiroideo"])


# ============================================================
# 4. CARDIOVASCULAR (6)
# ============================================================
LOC = "CARDIOVASCULAR"
TAG = ["cardio"]

add(LOC,
    "Dolor opresivo retroesternal",
    "Irradiado a MII / mandibula / espalda",
    "Diaforesis + nausea",
    "Sindrome coronario agudo (SCA / IAM)",
    "EKG en 10 min + troponina + ASA + manejo segun ST.",
    TAG + ["sca"])

add(LOC,
    "Dolor pleuritico que MEJORA al inclinarse adelante",
    "Frote pericardico a la auscultacion",
    "Cambios EKG difusos (supradesnivel concavo, PR descendido)",
    "Pericarditis aguda",
    "AINEs + colchicina; descartar derrame y taponamiento.",
    TAG + ["pericarditis"])

add(LOC,
    "Ortopnea + disnea paroxistica nocturna",
    "Ingurgitacion yugular",
    "Edema bilateral en MI + crepitantes basales",
    "Insuficiencia cardiaca descompensada",
    "Diuretico IV + oxigeno; investigar disparador.",
    TAG + ["icc"])

add(LOC,
    "Soplo sistolico eyectivo en 2EID",
    "Irradiado a carotidas",
    "Pulso parvus et tardus",
    "Estenosis aortica",
    "Eco transtoracico; valorar reemplazo valvular si sintomatica.",
    TAG + ["estenosis_aortica"])

add(LOC,
    "Edema unilateral de pantorrilla",
    "Empastamiento + Homans (+)",
    "Calor y enrojecimiento local",
    "Trombosis venosa profunda",
    "Wells + dimero D + USG Doppler; anticoagulacion si confirmada.",
    TAG + ["tvp"])

add(LOC,
    "Prodromo (sudor, nausea, mareo)",
    "Desencadenante (calor, ortostatismo, dolor)",
    "Recuperacion rapida sin foco neurologico",
    "Sincope vasovagal",
    "Maniobras de contrapresion; hidratacion; descartar causa cardiaca si dudoso.",
    TAG + ["sincope"])


# ============================================================
# 5. PULMONAR (6)
# ============================================================
LOC = "EXPLORACION PULMONAR"
TAG = ["pulmonar"]

add(LOC,
    "Crepitantes localizados",
    "Matidez a la percusion",
    "Egofonia / broncofonia",
    "Neumonia adquirida en la comunidad",
    "CURB-65 + Rx torax; amoxicilina o macrolido segun severidad.",
    TAG + ["neumonia"])

add(LOC,
    "Tos productiva",
    "Auscultacion pulmonar LIMPIA (sin crepitantes focales)",
    "Sin fiebre alta ni signos sistemicos",
    "Bronquitis aguda",
    "Manejo sintomatico; NO antibiotico de rutina.",
    TAG + ["bronquitis"])

add(LOC,
    "Sibilancias espiratorias difusas",
    "Uso de musculos accesorios",
    "Reversibilidad post-broncodilatador",
    "Crisis asmatica",
    "SABA + corticoide sistemico; oxigeno si SatO2 &lt;94%.",
    TAG + ["asma"])

add(LOC,
    "Torax en tonel",
    "Espiracion prolongada con sibilancias",
    "Tabaquismo &gt;10 paquetes-ano",
    "EPOC exacerbado",
    "Broncodilatador + corticoide + ATB si esputo purulento.",
    TAG + ["epoc"])

add(LOC,
    "Matidez a la percusion",
    "MV abolido en la zona",
    "Egofonia en limite superior del derrame",
    "Derrame pleural",
    "Rx + USG; toracocentesis diagnostica (criterios de Light).",
    TAG + ["derrame_pleural"])

add(LOC,
    "Hiperresonancia a la percusion",
    "MV ausente unilateral",
    "Desviacion de traquea contralateral (si a tension)",
    "Neumotorax",
    "Si a tension: toracostomia inmediata 2EIC LMC.",
    TAG + ["neumotorax"])


# ============================================================
# 6. ABDOMINAL (6)
# ============================================================
LOC = "EXPLORACION ABDOMINAL"
TAG = ["abdomen"]

add(LOC,
    "Dolor que migra de periumbilical a FID",
    "McBurney (+)",
    "Blumberg (+) / signo del psoas",
    "Apendicitis aguda",
    "Apendicectomia; ATB perioperatorio.",
    TAG + ["apendicitis"])

add(LOC,
    "Murphy (+)",
    "Dolor en HCD + fiebre",
    "Vesicula palpable dolorosa",
    "Colecistitis aguda",
    "Ayuno + ATB + colecistectomia temprana (24-72 h).",
    TAG + ["colecistitis"])

add(LOC,
    "Dolor abdominal colico difuso",
    "Peristalsis aumentada / borborigmos",
    "Sin defensa ni rebote",
    "Gastroenteritis aguda",
    "Hidratacion + manejo sintomatico; ATB solo en casos especificos.",
    TAG + ["gastroenteritis"])

add(LOC,
    "Dolor epigastrico irradiado en cinturon",
    "Signos de Cullen / Grey-Turner si grave",
    "Vomito persistente",
    "Pancreatitis aguda",
    "Lipasa &gt;3x; ayuno + hidratacion agresiva + analgesia.",
    TAG + ["pancreatitis"])

add(LOC,
    "Dolor en fosa iliaca izquierda",
    "Fiebre",
    "Adulto &gt;50 anos",
    "Diverticulitis",
    "TC abdominal; ATB ambulatorio si no complicada.",
    TAG + ["diverticulitis"])

add(LOC,
    "Distension + timpanismo difuso",
    "Peristalsis metalica / de lucha",
    "Ausencia de evacuaciones y gases",
    "Obstruccion intestinal",
    "SNG + hidratacion; cirugia si estrangulacion o no resuelve.",
    TAG + ["obstruccion"])


# ============================================================
# 7. NEUROLOGICO (6)
# ============================================================
LOC = "EXPLORACION NEUROLOGICA"
TAG = ["neuro"]

add(LOC,
    "Asimetria facial subita",
    "Disartria",
    "Debilidad de extremidad (FAST positivo)",
    "EVC isquemico",
    "Activar codigo ictus; TC sin contraste; trombolisis si &lt;4.5 h.",
    TAG + ["evc"])

add(LOC,
    "Cefalea pulsatil hemicraneal",
    "Fotofobia + nausea",
    "Paciente busca cuarto oscuro y silencio",
    "Migrana",
    "Triptan o AINE; profilaxis si &ge;4 episodios/mes.",
    TAG + ["migrana"])

add(LOC,
    "Cefalea opresiva bilateral &laquo;en banda&raquo;",
    "SIN nausea ni fotofobia",
    "Gatillada por estres o postura",
    "Cefalea tensional",
    "Paracetamol o AINE; manejo de estres.",
    TAG + ["cefalea_tensional"])

add(LOC,
    "&laquo;Peor cefalea de mi vida&raquo; o en trueno",
    "+ Foco neurologico o fiebre",
    "Despierta al paciente / cambio del patron habitual",
    "Cefalea secundaria (red flag)",
    "TC sin contraste urgente; considerar PL para HSA.",
    TAG + ["cefalea_red_flag"])

add(LOC,
    "Vertigo desencadenado por cambios de posicion",
    "Dix-Hallpike (+)",
    "Nistagmo agotable y unidireccional",
    "Vertigo posicional paroxistico benigno (BPPV)",
    "Maniobra de Epley; sin necesidad de imagen.",
    TAG + ["bppv"])

add(LOC,
    "Vertigo + foco neurologico",
    "Nistagmo NO agotable o vertical",
    "Ataxia desproporcionada al vertigo",
    "Vertigo central",
    "RM urgente; descartar EVC vertebrobasilar.",
    TAG + ["vertigo_central"])


# ============================================================
# 8. COLUMNA / MUSCULOESQUELETICO (4)
# ============================================================
LOC = "COLUMNA / MUSCULOESQUELETICO"
TAG = ["msk"]

add(LOC,
    "Dolor lumbar + contractura paravertebral",
    "Empeora con movimiento, mejora con reposo",
    "SIN foco neurologico ni red flags",
    "Lumbalgia mecanica",
    "AINEs + actividad temprana; sin imagen de rutina.",
    TAG + ["lumbalgia"])

add(LOC,
    "Anestesia en silla de montar",
    "Retencion urinaria / incontinencia",
    "Trauma, fiebre, baja de peso o deficit motor agudo",
    "Lumbalgia con red flags (sospecha cauda equina)",
    "RM urgente; valoracion quirurgica inmediata.",
    TAG + ["cauda_equina"])

add(LOC,
    "Dolor lumbar irradiado por MI",
    "Lasegue / SLR (+)",
    "Parestesia en dermatoma especifico (L5/S1)",
    "Ciatica / radiculopatia",
    "AINEs + actividad; RM si persiste &gt;6 sem o deficit.",
    TAG + ["ciatica"])

add(LOC,
    "Dolor cervical + contractura paravertebral",
    "ROM cervical limitado",
    "SIN deficit neurologico",
    "Cervicalgia mecanica",
    "AINEs + calor local; evitar collarines prolongados.",
    TAG + ["cervicalgia"])


# ============================================================
# 9. GENITOURINARIO (6)
# ============================================================
LOC = "GENITOURINARIO"
TAG = ["gu"]

add(LOC,
    "Disuria",
    "Polaquiuria + urgencia",
    "SIN fiebre ni Giordano",
    "Cistitis (ITU baja)",
    "Nitrofurantoina o fosfomicina; 3-7 dias segun esquema.",
    TAG + ["cistitis"])

add(LOC,
    "Fiebre alta + escalofrios",
    "Dolor lumbar",
    "Giordano (+) + sintomas urinarios",
    "Pielonefritis aguda",
    "Cefalosporina IV; hospitalizar si severa o embarazada.",
    TAG + ["pielonefritis"])

add(LOC,
    "Dolor en flanco que irradia a ingle",
    "Paciente inquieto que NO encuentra postura",
    "Hematuria",
    "Colico renal (litiasis)",
    "AINE + alfa-bloqueador; TC sin contraste si dx dudoso.",
    TAG + ["colico_renal"])

add(LOC,
    "Bacteriuria sintomatica o asintomatica",
    "Urocultivo &ge;10&#8309; UFC/mL",
    "Paciente embarazada",
    "ITU en embarazo",
    "TRATAR SIEMPRE: nitrofurantoina (no 1T ni cerca del termino) o cefalexina.",
    TAG + ["itu_embarazo"])

add(LOC,
    "Prostata aumentada lisa elastica al tacto",
    "Sintomas obstructivos (chorro debil, nicturia, esfuerzo)",
    "SIN nodulos ni dureza",
    "Hiperplasia prostatica benigna (HBP)",
    "Tamsulosina; finasteride si proximada grande.",
    TAG + ["hbp"])

add(LOC,
    "Prostata nodular indurada",
    "Perdida del surco medio",
    "PSA elevado",
    "Cancer de prostata (sospecha)",
    "Referir a urologia; biopsia transrectal.",
    TAG + ["ca_prostata"])


# ============================================================
# 10. ENDOCRINO / METABOLICO (5)
# ============================================================
LOC = "ENDOCRINO / METABOLICO"
TAG = ["endocrino"]

add(LOC,
    "Poliuria + polidipsia",
    "Perdida de peso involuntaria",
    "Glucemia &gt;200 mg/dL o HbA1c &ge;6.5%",
    "Diabetes mellitus tipo 2 descompensada",
    "Metformina + estilo de vida; agregar GLP-1 o iSGLT2 segun perfil.",
    TAG + ["dm2"])

add(LOC,
    "TA &ge;140/90 sostenida sin emergencia aguda",
    "Hipertrofia ventricular izquierda / proteinuria",
    "Retinopatia hipertensiva (Keith-Wagener)",
    "HTA cronica con dano de organo blanco",
    "Antihipertensivo segun comorbilidades; meta &lt;130/80.",
    TAG + ["hta"])

add(LOC,
    "Taquicardia + perdida de peso pese a apetito conservado",
    "Temblor fino distal",
    "Exoftalmos + bocio difuso",
    "Hipertiroidismo (enfermedad de Graves)",
    "TSH suprimida + anti-TRAB; tionamidas + propranolol.",
    TAG + ["hipertiroidismo"])

add(LOC,
    "Fatiga + intolerancia al frio",
    "Ganancia de peso + bradicardia",
    "Piel seca + estrenimiento + depresion",
    "Hipotiroidismo",
    "TSH alta + T4 libre baja; levotiroxina 1.6 mcg/kg/d.",
    TAG + ["hipotiroidismo"])

add(LOC,
    "Xantelasmas / arco corneal",
    "Obesidad central",
    "LDL elevado, HDL bajo, triglicerios altos en perfil",
    "Dislipidemia",
    "Estatina segun riesgo ASCVD; estilo de vida primero.",
    TAG + ["dislipidemia"])


# ============================================================
# Build
# ============================================================
def build():
    out_path = os.path.join(OUTPUT_DIR, "Medicina_Familiar_Adulto_Capa6_Integrador.apkg")
    genanki.Package(deck).write_to_file(out_path)
    print(f"OK: {out_path}  ({len(deck.notes)} notas)")


if __name__ == "__main__":
    build()
