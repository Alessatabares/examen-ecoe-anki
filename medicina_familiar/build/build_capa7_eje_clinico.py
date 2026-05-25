"""Capa 7 - Eje Clinico (Medicina Familiar Adulto).

Formato Q&A integrador:
- Front: un eje sintomatico (tos, disnea, cefalea, etc.) + lista numerada
  de presentaciones distintas.
- Back: la misma lista con el diagnostico mas probable de cada presentacion.

Pedagogia: entrena el reconocimiento de patrones DENTRO de un sintoma comun.
Cuando el paciente llega con tos, dolor abdominal, cefalea o fatiga,
la alumna debe disparar el dx correcto en segundos segun los matices.

Guia: USPSTF + ADA 2025 + ACC/AHA + IDSA + GOLD 2024 + GINA 2024 (misma base que C1-C6).
"""
import os
import genanki

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "output")
os.makedirs(OUTPUT_DIR, exist_ok=True)

MODEL_QA_ID = 1607392320  # reusable Q&A
DECK_ID = 1897089931
DECK_NAME = "Medicina Familiar Adulto::Capa 7 - Eje Clinico"

CSS_BASE = """
.card {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  font-size: 18px; text-align: left; color: #1a1a1a;
  background-color: #fafafa; padding: 20px; line-height: 1.55;
}
.eje {
  display: inline-block; padding: 5px 14px; margin-bottom: 14px;
  background: #7c2d12; color: #fff; border-radius: 6px;
  font-size: 13px; letter-spacing: 0.8px; font-weight: 700;
  text-transform: uppercase;
}
.prompt { color: #2563eb; font-weight: 600; margin: 8px 0 12px 0; }
ol.pres { margin: 4px 0 0 0; padding-left: 28px; }
ol.pres li { margin: 8px 0; }
ol.dx { margin: 4px 0 0 0; padding-left: 28px; }
ol.dx li { margin: 8px 0; font-weight: 700; color: #047857; }
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

BASE_TAGS = ["medicina_familiar", "ecoe", "capa7", "eje_clinico"]


def make_card(eje, items, tag):
    front = (
        f'<div class="eje">EJE: {eje}</div>'
        f'<div class="prompt">&iquest;Dx m&aacute;s probable seg&uacute;n presentaci&oacute;n?</div>'
        '<ol class="pres">'
        + "".join(f"<li>{p}</li>" for p, _ in items)
        + '</ol>'
    )
    back = (
        '<ol class="dx">'
        + "".join(f"<li>{d}</li>" for _, d in items)
        + '</ol>'
    )
    note = genanki.Note(
        model=model_qa,
        fields=[front, back],
        tags=BASE_TAGS + [tag],
    )
    deck.add_note(note)


# ============================================================
# EJES SINTOMATICOS
# ============================================================

make_card("Tos", [
    ("Aguda productiva + crepitantes localizados + fiebre", "Neumonia"),
    ("Aguda productiva + auscultacion pulmonar limpia", "Bronquitis aguda"),
    ("Cronica + tabaquismo + disnea progresiva", "EPOC"),
    ("Episodica con sibilancias + reversible", "Asma"),
    ("Seca persistente en usuario de IECA", "Tos por IECA"),
    ("Cronica + hemoptisis + baja de peso + sudores nocturnos", "Tuberculosis o Ca de pulmon"),
    ("Carraspeo cronico + secrecion posterior nasal", "Goteo postnasal (rinitis cronica)"),
    ("Nocturna + pirosis + acidez", "Tos por ERGE"),
], "tos")

make_card("Disnea", [
    ("Subita + dolor pleuritico + taquicardia", "TEP"),
    ("Subita + dolor opresivo retroesternal", "SCA / IAM"),
    ("Progresiva + ortopnea + edema MI", "ICC descompensada"),
    ("Sibilancias + reversibilidad con broncodilatador", "Asma"),
    ("Torax en tonel + tabaquismo cronico", "EPOC"),
    ("Pulmon limpio + ansiedad + parestesias periorales", "Crisis de panico"),
    ("Palidez + taquicardia + Hb baja", "Disnea por anemia"),
    ("Subita + hiperresonancia unilateral", "Neumotorax"),
], "disnea")

make_card("Dolor toracico", [
    ("Opresivo retroesternal irradiado a MII/mandibula + diaforesis", "SCA / IAM"),
    ("Pleuritico que mejora al inclinarse adelante", "Pericarditis"),
    ("Punzante reproducible a la palpacion costocondral", "Costocondritis (Tietze)"),
    ("Quemante + pirosis postprandial", "ERGE"),
    ("Pleuritico + disnea subita + taquicardia", "TEP"),
    ("Quemante en dermatoma + vesiculas en banda", "Herpes zoster"),
    ("Desgarrante irradiado a espalda + asimetria de TA", "Diseccion aortica"),
    ("Ansiedad + parestesias periorales + miedo a morir", "Crisis de panico"),
], "dolor_toracico")

make_card("Cefalea", [
    ("Pulsatil hemicraneal + fotofobia + nausea", "Migrana"),
    ("Opresiva bilateral &laquo;en banda&raquo; sin nausea", "Cefalea tensional"),
    ("Periorbitaria unilateral + lagrimeo + rinorrea unilateral", "Cefalea en racimos (cluster)"),
    ("&laquo;Peor cefalea de mi vida&raquo; / en trueno", "Hemorragia subaracnoidea"),
    ("+ fiebre + rigidez de nuca + foco", "Meningitis / encefalitis"),
    ("Matutina + nausea + papiledema", "Hipertension intracraneal (tumor)"),
    ("Temporal + claudicacion mandibular + VSG alta en &gt;50", "Arteritis temporal (Horton)"),
    ("Electrica facial al cepillar dientes", "Neuralgia del trigemino"),
], "cefalea")

make_card("Fatiga / astenia", [
    ("Palidez + queilosis + glositis", "Anemia ferropenica"),
    ("Intolerancia al frio + ganancia de peso + bradicardia", "Hipotiroidismo"),
    ("Poliuria + polidipsia + perdida de peso", "DM2 descompensada"),
    ("Anhedonia + insomnio + tristeza &ge;2 sem", "Depresion mayor"),
    ("Ronquido + apneas observadas + somnolencia diurna", "Apnea obstructiva del sueno"),
    ("+ dolor articular + rash en mariposa", "Lupus"),
    ("Disnea + ortopnea + edema MI", "ICC"),
    ("+ sudores nocturnos + adenopatias", "Linfoma"),
], "fatiga")

make_card("Perdida de peso involuntaria", [
    ("+ poliuria + polidipsia", "DM2 descompensada"),
    ("+ temblor + intolerancia al calor + taquicardia", "Hipertiroidismo"),
    ("+ sudores nocturnos + adenopatias + fiebre vespertina", "Linfoma / TB"),
    ("+ cambio del habito intestinal + sangrado oculto", "Ca de colon"),
    ("+ anhedonia + apetito disminuido", "Depresion"),
    ("+ ictericia + masa abdominal indolora", "Ca de pancreas / via biliar"),
    ("+ disfagia progresiva a solidos", "Ca esofagico"),
], "perdida_peso")

make_card("Diarrea", [
    ("Aguda acuosa + nausea/vomito sin sangre", "Gastroenteritis viral"),
    ("Aguda con sangre + tenesmo + fiebre", "Disenteria bacteriana (Shigella, Salmonella)"),
    ("Tras uso reciente de antibiotico + olor fetido", "Colitis por C. difficile"),
    ("Cronica + dolor abdominal + baja de peso + sangrado", "Enfermedad inflamatoria intestinal"),
    ("Cronica + esteatorrea + flatulencia + distension", "Sindrome de malabsorcion / celiaquia"),
    ("Profusa post-comida + tirotoxicosis", "Hipertiroidismo"),
    ("Alterna con estrenimiento + dolor que cede al evacuar", "Sindrome de intestino irritable"),
    ("Tras viaje a zona tropical", "Diarrea del viajero (ETEC)"),
], "diarrea")

make_card("Estrenimiento", [
    ("Reciente + cambio de habito + sangrado en &gt;50 anos", "Ca de colon"),
    ("Cronico + ganancia de peso + intolerancia al frio", "Hipotiroidismo"),
    ("Asociado a uso de opioides", "Estrenimiento inducido por opioides"),
    ("Cronico que alivia tras evacuar en joven", "Sindrome de intestino irritable"),
    ("Severo + impactacion palpable + anciano encamado", "Estrenimiento cronico funcional"),
], "estrenimiento")

make_card("Nausea / vomito", [
    ("Matutino en mujer en edad fertil + amenorrea", "Embarazo"),
    ("+ cefalea matutina + papiledema", "Hipertension intracraneal"),
    ("+ dolor epigastrico en cinturon", "Pancreatitis aguda"),
    ("+ diarrea + fiebre + dolor colico", "Gastroenteritis"),
    ("+ Kussmaul + aliento a frutas + glucemia alta", "Cetoacidosis diabetica"),
    ("+ cefalea pulsatil + fotofobia", "Migrana"),
    ("+ vertigo + nistagmo", "Vertigo periferico / central"),
    ("+ distension + ausencia de evacuaciones", "Obstruccion intestinal"),
], "nausea_vomito")

make_card("Dolor abdominal", [
    ("Periumbilical que migra a FID + McBurney (+)", "Apendicitis aguda"),
    ("HCD + Murphy (+) + fiebre", "Colecistitis aguda"),
    ("Epigastrico irradiado a espalda + vomito persistente", "Pancreatitis aguda"),
    ("FII + fiebre + adulto &gt;50 anos", "Diverticulitis"),
    ("Colico difuso + diarrea + peristalsis aumentada", "Gastroenteritis"),
    ("Flanco que irradia a ingle + paciente inquieto", "Colico renal"),
    ("Suprapubico + disuria + polaquiuria", "Cistitis"),
    ("Hipogastrico + amenorrea + &beta;-hCG (+)", "Embarazo ectopico"),
    ("Epigastrico nocturno que alivia con comida", "Ulcera duodenal"),
    ("Epigastrico que empeora con comida + baja peso", "Ulcera gastrica / Ca gastrico"),
], "dolor_abdominal")

make_card("Disuria / sintomas urinarios", [
    ("Disuria + polaquiuria sin fiebre", "Cistitis"),
    ("+ fiebre + Giordano (+) + dolor lumbar", "Pielonefritis aguda"),
    ("Disuria + flujo en hombre joven sexualmente activo", "Uretritis (gonococo/clamidia)"),
    ("Chorro debil + nicturia + esfuerzo en hombre &gt;50", "Hiperplasia prostatica benigna"),
    ("Hematuria indolora en fumador &gt;40 anos", "Ca vesical"),
    ("Urgencia + frecuencia sin infeccion", "Vejiga hiperactiva"),
    ("Urocultivo (+) sin sintomas + embarazada", "Bacteriuria asintomatica del embarazo"),
    ("Perdida de orina con esfuerzo (tos, risa)", "Incontinencia urinaria de esfuerzo"),
], "disuria")

make_card("Vertigo / mareo", [
    ("Posicional + Dix-Hallpike (+) + nistagmo agotable", "Vertigo posicional paroxistico benigno (BPPV)"),
    ("Crisis recurrentes con tinnitus + hipoacusia fluctuante", "Enfermedad de Meniere"),
    ("Crisis unica severa + nausea sin tinnitus", "Neuritis vestibular"),
    ("Vertigo + foco neurologico + nistagmo no agotable", "Vertigo central / EVC vertebrobasilar"),
    ("Mareo al levantarse + caida de TA &gt;20 mmHg", "Hipotension ortostatica"),
    ("Sensacion de cabeza vacia + ansiedad + hiperventilacion", "Mareo psicogeno / panico"),
], "vertigo")

make_card("Artralgias / dolor articular", [
    ("1a MTF muy dolorosa, roja y caliente + acido urico alto", "Gota"),
    ("Simetrico en pequenas articulaciones manos + rigidez matutina &gt;1 h", "Artritis reumatoide"),
    ("Asimetrico + psoriasis + unas con pitting", "Artritis psoriasica"),
    ("Una articulacion caliente con fiebre + leucocitosis", "Artritis septica"),
    ("Rodillas/manos + rigidez breve + crepitacion + edad &gt;50", "Artrosis"),
    ("Migratorio + faringitis previa en nino + nodulos subcutaneos", "Fiebre reumatica"),
    ("+ rash malar + fotosensibilidad + serositis", "Lupus"),
    ("Lumbalgia + uveitis + sacroileitis en joven", "Espondilitis anquilosante"),
], "artralgias")

make_card("Edema", [
    ("Bilateral MI vespertino sin disnea", "Insuficiencia venosa cronica"),
    ("Generalizado + ortopnea + DPN", "ICC descompensada"),
    ("Periorbitario matutino + proteinuria masiva", "Sindrome nefrotico"),
    ("Ascitis + ictericia + aranas vasculares", "Cirrosis hepatica"),
    ("Unilateral MI + dolor + Homans (+)", "TVP"),
    ("Cronico unilateral indoloro tras vaciamiento axilar", "Linfedema postquirurgico"),
    ("Facial + voz ronca + mixedema cutaneo", "Hipotiroidismo (mixedema)"),
], "edema")

make_card("Palpitaciones", [
    ("Irregularmente irregulares + ausencia de onda P en EKG", "Fibrilacion auricular"),
    ("Inicio y fin subitos + responden a maniobras vagales", "Taquicardia supraventricular"),
    ("+ sincope + cardiopatia estructural", "Taquicardia ventricular"),
    ("+ temblor + intolerancia al calor + perdida de peso", "Hipertiroidismo"),
    ("+ ansiedad + parestesias + miedo a morir", "Crisis de panico"),
    ("+ palidez + Hb baja", "Palpitaciones por anemia"),
    ("Paroxisticas con sudor + cefalea + HTA", "Feocromocitoma"),
], "palpitaciones")

make_card("Sincope", [
    ("Prodromo (sudor, nausea) + desencadenante + recuperacion rapida", "Sincope vasovagal"),
    ("Al levantarse + caida de TA ortostatica", "Hipotension ortostatica"),
    ("Subito sin prodromo durante el esfuerzo", "Sincope cardiaco (EAo, arritmia)"),
    ("+ foco neurologico transitorio", "AIT"),
    ("Al voltear el cuello o por colocarse corbata", "Hipersensibilidad del seno carotideo"),
    ("Adulto mayor con multiples antihipertensivos", "Sincope por polifarmacia / ortostatismo"),
], "sincope")

make_card("Hematuria", [
    ("Indolora + fumador &gt;40 anos", "Ca vesical"),
    ("+ colico en flanco que irradia a ingle", "Litiasis renal"),
    ("+ disuria aguda + polaquiuria", "ITU hemorragica"),
    ("+ fiebre + Giordano (+)", "Pielonefritis"),
    ("+ edema + proteinuria + HTA en joven", "Glomerulonefritis"),
    ("+ masa palpable en flanco", "Ca renal"),
], "hematuria")

make_card("Hemoptisis", [
    ("Cronica + tabaquismo + baja de peso", "Ca pulmonar"),
    ("+ sudores nocturnos + tos cronica + fiebre vespertina", "Tuberculosis"),
    ("Recurrente + bronquiectasias conocidas", "Bronquiectasias"),
    ("Subita + dolor pleuritico + disnea", "TEP"),
    ("Edema pulmonar con esputo rosado espumoso", "Edema pulmonar cardiogenico"),
    ("+ estenosis mitral + soplo diastolico", "Hemoptisis por hipertension pulmonar"),
], "hemoptisis")

make_card("Ronquera / disfonia", [
    ("Aguda + IVAS reciente", "Laringitis viral aguda"),
    ("Cronica &gt;2 sem en fumador", "Cancer laringeo"),
    ("Cronica + carraspeo + pirosis", "Laringitis por reflujo"),
    ("Profesional de la voz + lesion bilateral en cuerdas", "Nodulos vocales"),
    ("Paralisis cordal post-cirugia tiroidea", "Lesion del nervio laringeo recurrente"),
], "disfonia")

make_card("Insomnio", [
    ("Dificultad de conciliacion + ansiedad anticipatoria", "Trastorno de ansiedad"),
    ("Despertar precoz + anhedonia + tristeza", "Depresion"),
    ("Ronquido + apneas observadas + somnolencia diurna", "Apnea obstructiva del sueno"),
    ("Necesidad de mover piernas al acostarse", "Sindrome de piernas inquietas"),
    ("Turnos rotatorios o jet lag", "Trastorno del ritmo circadiano"),
], "insomnio")

make_card("Adenopatias", [
    ("Cervicales dolorosas + IVAS o faringitis", "Adenopatia reactiva"),
    ("Cervicales + faringitis + esplenomegalia en adolescente", "Mononucleosis (EBV)"),
    ("Cervicales firmes indoloras &gt;4 sem", "Linfoma / metastasis"),
    ("Generalizadas + sudores + baja de peso", "Linfoma / VIH / TB"),
    ("Inguinal + ulcera genital", "ITS (sifilis, herpes, chancroide)"),
    ("Supraclavicular izquierda (Virchow)", "Ca abdominal (gastrico, pancreatico)"),
], "adenopatias")

make_card("Erupcion cutanea", [
    ("Placas eritematosas pruriginosas en pliegues", "Dermatitis atopica"),
    ("Placas con escama plateada en codos, rodillas, cuero cabelludo", "Psoriasis"),
    ("Vesiculas dolorosas en dermatoma unilateral", "Herpes zoster"),
    ("Rash en mariposa + fotosensibilidad", "Lupus"),
    ("Petequias + fiebre + rigidez de nuca", "Meningococcemia"),
    ("Eritema migrans + picadura de garrapata", "Enfermedad de Lyme"),
    ("Diana eritematosa simetrica + ATB reciente", "Eritema multiforme"),
    ("Despegamiento epidermico + mucosas + Nikolsky (+)", "Stevens-Johnson / NET"),
], "erupcion_cutanea")

make_card("Hipertension secundaria (sospechas)", [
    ("HTA en &lt;30 anos + soplo abdominal", "HTA renovascular (displasia fibromuscular)"),
    ("Crisis paroxisticas con sudor + palpitaciones + cefalea", "Feocromocitoma"),
    ("HTA + hipopotasemia + alcalosis metabolica", "Hiperaldosteronismo primario (Conn)"),
    ("HTA + cara de luna + estrias violaceas", "Sindrome de Cushing"),
    ("HTA en MMSS con pulsos disminuidos en MMII", "Coartacion de aorta"),
    ("HTA + roncopatia + somnolencia diurna", "HTA por SAOS"),
], "hta_secundaria")

make_card("Alteracion de la glucemia", [
    ("&gt;200 + poliuria + polidipsia + perdida peso", "DM2 descompensada"),
    ("&gt;250 + cetonas + Kussmaul + aliento a frutas", "Cetoacidosis diabetica"),
    ("&lt;70 + diaforesis + temblor que cede con glucosa", "Hipoglucemia"),
    ("&gt;600 + osmolaridad muy alta sin cetonas en anciano", "Estado hiperosmolar hiperglucemico"),
    ("Glucemia ayuno 100-125 o HbA1c 5.7-6.4%", "Prediabetes"),
    ("Glucemia ayuno &ge;126 repetida o HbA1c &ge;6.5%", "DM2 diagnostica"),
], "glucemia")

make_card("Anemia (por caracteristicas)", [
    ("Microcitica hipocromica + ferritina baja", "Anemia ferropenica"),
    ("Microcitica + HbA2 elevada + ascendencia mediterranea", "Talasemia"),
    ("Macrocitica + parestesias + glositis", "Deficit de vitamina B12"),
    ("Macrocitica + alcoholismo cronico sin neuropatia", "Deficit de folato"),
    ("Normocitica + enfermedad inflamatoria/IRC", "Anemia de enfermedad cronica"),
    ("+ esquistocitos + reticulocitosis + LDH alta", "Anemia hemolitica"),
    ("+ sangrado evidente (TGI, menorragia)", "Anemia por perdidas"),
], "anemia")

make_card("Otalgia", [
    ("MT abombada eritematosa + fiebre en nino", "OMA"),
    ("Dolor al jalar el pabellon + edema CAE", "Otitis externa"),
    ("+ mareo + tinnitus + hipoacusia fluctuante", "Enfermedad de Meniere"),
    ("Hipoacusia conductiva + MT integra + tapon visible", "Cerumen impactado"),
    ("Irradiada de molestia dental", "Otalgia referida (odontalgia)"),
    ("Irradiada + disfagia + disfonia en fumador", "Otalgia referida por Ca laringeo"),
], "otalgia")

make_card("Sangrado de tubo digestivo", [
    ("Hematemesis + melena + ulcera previa o AINEs", "STDA por ulcera peptica"),
    ("Sangrado rectal rojo brillante + estrenimiento", "Hemorroides"),
    ("Sangre oculta + anemia + cambio del habito + &gt;50 anos", "Ca de colon"),
    ("Diarrea sanguinolenta + fiebre + tenesmo", "Disenteria / colitis infecciosa"),
    ("Hematemesis masiva + cirrosis + aranas", "Varices esofagicas"),
    ("Sangrado rectal + dolor anal intenso al evacuar", "Fisura anal"),
], "stda_stdb")

make_card("Disfagia", [
    ("Progresiva a solidos + baja de peso en fumador", "Ca de esofago"),
    ("A solidos y liquidos desde el inicio + regurgitacion", "Acalasia"),
    ("Intermitente a solidos + pirosis cronica", "Estenosis peptica por ERGE"),
    ("Tras EVC + tos al deglutir", "Disfagia orofaringea neurologica"),
    ("Sensacion de bolo en garganta sin perdida de peso", "Globo histerico (funcional)"),
], "disfagia")

make_card("Trastornos del animo / psiquiatricos", [
    ("Anhedonia + insomnio o hipersomnia + culpa &ge;2 sem", "Depresion mayor"),
    ("Episodios de euforia + grandiosidad + insomnio sin fatiga", "Trastorno bipolar (mania)"),
    ("Preocupacion constante + tension muscular + insomnio", "Trastorno de ansiedad generalizada"),
    ("Crisis subita con disnea + parestesias + miedo a morir", "Crisis de panico"),
    ("Trauma previo + flashbacks + evitacion + hiperalerta", "Trastorno por estres postraumatico"),
    ("Pensamientos obsesivos + compulsiones repetitivas", "Trastorno obsesivo-compulsivo"),
], "salud_mental")


# ============================================================
# Build
# ============================================================
def build():
    out_path = os.path.join(OUTPUT_DIR, "Medicina_Familiar_Adulto_Capa7_EjeClinico.apkg")
    genanki.Package(deck).write_to_file(out_path)
    print(f"OK: {out_path}  ({len(deck.notes)} notas)")


if __name__ == "__main__":
    build()
