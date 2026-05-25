"""Capa 6 - Eje Clinico (Gineco-Obstetricia Adulto).

Formato Q&A integrador:
- Front: un eje sintomatico (flujo, sangrado, dolor, etc.) + lista numerada
  de presentaciones distintas.
- Back: la misma lista con el diagnostico mas probable de cada presentacion.

Pedagogia: entrena el reconocimiento de patrones DENTRO de un sintoma comun.
Cuando el paciente llega con flujo, sangrado, dolor pelvico, etc., la alumna
debe disparar el dx correcto en segundos segun los matices.

Guia: GPC mexicanas + ACOG + Williams (misma base que C1-C5).
"""
import os
import genanki

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "output")
os.makedirs(OUTPUT_DIR, exist_ok=True)

MODEL_QA_ID = 1607392320  # reusable Q&A
DECK_ID = 1178771173
DECK_NAME = "Gineco-Obstetricia Adulto::Capa 6 - Eje Clinico"

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
ol.dx li {
  margin: 8px 0; font-weight: 700; color: #047857;
}
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

BASE_TAGS = ["gineco_obstetricia", "ecoe", "capa6", "eje_clinico"]


def make_card(eje, items, tag):
    """items = list of (presentacion, dx) tuples"""
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

make_card("Flujo vaginal", [
    ("Blanco grumoso (queso cottage), sin olor", "Candidiasis vulvovaginal"),
    ("Grisaceo homogeneo + olor a pescado", "Vaginosis bacteriana"),
    ("Amarillo-verdoso espumoso + cervix en fresa", "Tricomoniasis"),
    ("Mucopurulento endocervical", "Cervicitis (GC/CT)"),
    ("Acuoso continuo en embarazo", "RPM"),
    ("Sanguinolento maloliente en posmenopausica", "Ca de endometrio"),
    ("Cafe/marron intermitente con DIU", "Sangrado intermenstrual por DIU"),
    ("Amarillo cremoso + uretritis", "Gonorrea"),
], "flujo_vaginal")

make_card("Sangrado uterino anormal", [
    ("Poscoital en mujer joven", "Cervicitis / polipo cervical"),
    ("Poscoital en mujer &ge;40 anos", "Ca cervicouterino"),
    ("Posmenopausico", "Ca de endometrio"),
    ("Intermenstrual con ACO o DIU", "Sangrado por metodo anticonceptivo"),
    ("Hipermenorrea + utero crecido irregular", "Miomatosis uterina"),
    ("Hipermenorrea + utero globoso simetrico", "Adenomiosis"),
    ("Hipermenorrea desde menarca", "Coagulopatia (von Willebrand)"),
    ("Polimenorrea en adolescente", "Anovulacion fisiologica del eje inmaduro"),
    ("1T + cuello cerrado + embrion vivo", "Amenaza de aborto"),
    ("1T + &beta;-hCG sin duplicar", "Embarazo ectopico"),
    ("3T INDOLORO rojo brillante", "Placenta previa"),
    ("3T + utero lenoso", "DPPNI"),
    ("Sangrado al romper membranas + bradicardia", "Vasa previa"),
], "sangrado_anormal")

make_card("Dolor pelvico", [
    ("Agudo unilateral + amenorrea", "Embarazo ectopico"),
    ("Agudo subito + nausea/vomito + masa anexial", "Torsion ovarica"),
    ("Mitad del ciclo, unilateral, autolimitado", "Mittelschmerz (dolor ovulatorio)"),
    ("Ciclico, con la menstruacion", "Endometriosis"),
    ("Dismenorrea desde menarca sin patologia", "Dismenorrea primaria"),
    ("Bilateral + fiebre + dolor a movilizacion cervical", "EIP"),
    ("EIP + dolor en hipocondrio derecho", "Sx de Fitz-Hugh-Curtis"),
    ("Cronico + ardor vulvar sin lesiones", "Vulvodinia"),
    ("Dispareunia profunda + nodularidad en saco posterior", "Endometriosis profunda"),
    ("Dispareunia superficial + sequedad posmenopausica", "Vaginitis atrofica"),
], "dolor_pelvico")

make_card("Masa anexial (USG)", [
    ("Quiste simple anecoico &lt;5 cm en edad fertil", "Quiste folicular funcional"),
    ("Quiste con ecos en &laquo;vidrio esmerilado&raquo;", "Endometrioma"),
    ("Quiste con dientes/grasa/calcio", "Teratoma maduro (quiste dermoide)"),
    ("Solido + ascitis + CA-125 alto en posmenopausica", "Ca de ovario epitelial"),
    ("Quiste con tabiques gruesos y papilas", "Cistoadenocarcinoma"),
    ("Hidrosalpinx en &laquo;rueda de carro&raquo;", "Secuela de EIP"),
    ("Masa anexial + virilizacion rapida", "Tumor de celulas de Sertoli-Leydig"),
], "masa_anexial")

make_card("Masa mamaria", [
    ("Movil firme bien delimitada en &lt;30 anos", "Fibroadenoma"),
    ("Lisa movil que cambia con el ciclo", "Quiste mamario"),
    ("Dura fija irregular + retraccion cutanea", "Ca de mama"),
    ("Fluctuante dolorosa en lactando", "Absceso mamario"),
    ("Crecimiento rapido + tamano grande movil", "Tumor filoides"),
    ("Masa post-traumatica indurada", "Necrosis grasa"),
    ("Mama eritematosa difusa &laquo;piel de naranja&raquo; sin tumor palpable", "Carcinoma inflamatorio"),
], "masa_mamaria")

make_card("Secrecion del pezon", [
    ("Sanguinolenta unilateral uniductal", "Papiloma intraductal"),
    ("Lechosa bilateral fuera de lactancia", "Hiperprolactinemia (prolactinoma)"),
    ("Verdosa multiductal bilateral", "Ectasia ductal"),
    ("Purulenta en lactando", "Mastitis puerperal"),
    ("Cualquier secrecion + eccema unilateral del pezon", "Enfermedad de Paget"),
], "secrecion_pezon")

make_card("Amenorrea", [
    ("Secundaria + &beta;-hCG (+)", "Embarazo"),
    ("Secundaria + galactorrea", "Prolactinoma"),
    ("Secundaria + bochornos en &lt;40 anos", "Falla ovarica prematura"),
    ("Secundaria + bochornos &ge;45 anos", "Menopausia"),
    ("Secundaria + hiperandrogenismo + obesidad", "SOP"),
    ("Secundaria + bajo peso / atleta / estres", "Amenorrea hipotalamica funcional"),
    ("Secundaria post-legrado", "Sindrome de Asherman"),
    ("Primaria + talla baja + cuello alado", "Sindrome de Turner"),
    ("Primaria + caracteres femeninos + ausencia de utero", "Mayer-Rokitansky"),
    ("Primaria + caracteres femeninos + testiculos inguinales", "Insensibilidad a androgenos"),
], "amenorrea")

make_card("Hiperandrogenismo / hirsutismo", [
    ("Hirsutismo gradual + oligomenorrea + obesidad", "SOP"),
    ("Hirsutismo de inicio rapido + virilizacion", "Tumor androgenico (ovario/suprarrenal)"),
    ("Hirsutismo + estrias violaceas + cara de luna", "Sindrome de Cushing"),
    ("Hirsutismo leve desde menarca con ciclos normales", "HSC tardia (21-OH)"),
], "hirsutismo")

make_card("Prurito vulvar", [
    ("+ flujo blanco grumoso", "Candidiasis"),
    ("+ piel blanca atrofica en figura de &laquo;8&raquo;", "Liquen escleroso"),
    ("+ reticulado blanco erosivo", "Liquen plano vulvar"),
    ("+ lesion pigmentada irregular", "Melanoma vulvar"),
    ("+ lesiones blancas multifocales en mujer joven", "VIN (neoplasia intraepitelial)"),
    ("Cronico sin lesiones, con liquenificacion", "Liquen simple cronico"),
], "prurito_vulvar")

make_card("Prurito en embarazo", [
    ("Palmas y plantas, 3T, sin lesiones, predominio nocturno", "Colestasis intrahepatica del embarazo"),
    ("Papulas/placas en estrias abdominales (3T, primigesta)", "PUPPP"),
    ("Vesiculas periumbilicales que se extienden", "Penfigoide gestacional"),
    ("Generalizado + ictericia + nausea + hipoglucemia", "Higado graso agudo del embarazo"),
], "prurito_embarazo")

make_card("Lesiones vulvares", [
    ("Ulcera unica indolora indurada", "Sifilis primaria (chancro)"),
    ("Vesiculas agrupadas dolorosas", "Herpes genital"),
    ("Ulceras dolorosas multiples con bordes irregulares", "Chancroide (H. ducreyi)"),
    ("Verrugas friables exofiticas", "Condilomas (VPH 6/11)"),
    ("Adenopatia inguinal que fistuliza (&laquo;signo del surco&raquo;)", "Linfogranuloma venereo"),
    ("Masa fluctuante en labio mayor (4-8 hr)", "Absceso de Bartholino"),
    ("Papulas perladas umbilicadas", "Molusco contagioso"),
    ("Quiste indoloro lateral a uretra/clitoris", "Quiste de Skene / Gartner"),
], "lesiones_vulvares")

make_card("Edema en embarazo", [
    ("MMII vespertino sin HTA", "Edema fisiologico del embarazo"),
    ("Generalizado + facial + HTA", "Preeclampsia"),
    ("Unilateral en MMII + dolor pantorrilla", "TVP"),
    ("MMII + ascitis + proteinuria masiva", "Sindrome nefrotico"),
], "edema_embarazo")

make_card("Cefalea en embarazo", [
    ("+ TA &ge;160/110 + fosfenos + epigastralgia", "Preeclampsia severa"),
    ("+ deficit focal + cefalea en &laquo;trueno&raquo;", "Trombosis venosa cerebral"),
    ("Pulsatil unilateral con aura, antecedente previo", "Migrana"),
    ("Postpuncion dural, ortostatica", "Cefalea post-bloqueo neuroaxial"),
], "cefalea_embarazo")

make_card("Convulsion en embarazo / postparto", [
    ("+ TA &ge;140/90 + edema", "Eclampsia"),
    ("Postparto &gt;48 h + cefalea + deficit focal", "Trombosis de senos venosos cerebrales"),
    ("+ foco neurologico subito", "EVC hemorragico/isquemico"),
    ("Sin HTA con epilepsia previa", "Crisis epileptica recurrente"),
], "convulsion_embarazo")

make_card("Fiebre puerperal", [
    ("Loquios fetidos + subinvolucion", "Endometritis puerperal"),
    ("Mama eritematosa en lactando", "Mastitis puerperal"),
    ("Dolor en pantorrilla + edema", "TVP puerperal"),
    ("Fiebre persistente sin foco + dolor pelvico", "Tromboflebitis pelvica septica"),
    ("Giordano (+) + disuria", "Pielonefritis"),
    ("Herida quirurgica eritematosa/drenando", "Infeccion del sitio quirurgico"),
], "fiebre_puerperal")

make_card("Perdida de liquido vaginal", [
    ("Salida franca + cristalizacion en helecho", "RPM"),
    ("Goteo intermitente claro con esfuerzo", "Incontinencia urinaria de esfuerzo"),
    ("Tenido de meconio", "Sufrimiento fetal / posttermino"),
    ("Fetido + restos", "Aborto septico"),
], "perdida_liquido")

make_card("Hiperemesis / nausea severa", [
    ("AU &gt; EG + &beta;-hCG &gt;100,000", "Mola hidatiforme"),
    ("Embarazo con 2 polos fetales", "Embarazo gemelar"),
    ("1T sin otra causa + cetosis", "Hiperemesis gravidica"),
    ("3T + epigastralgia + ictericia", "HELLP / higado graso agudo"),
], "hiperemesis")

make_card("Dispareunia", [
    ("Profunda + nodularidad en fondo de saco", "Endometriosis profunda"),
    ("Superficial en posmenopausica seca", "Vaginitis atrofica"),
    ("De entrada, contraccion involuntaria", "Vaginismo"),
    ("Ardor focal en vestibulo al tacto", "Vestibulodinia (vulvodinia localizada)"),
    ("Postparto con desgarro mal cicatrizado", "Dispareunia por cicatriz/episiotomia"),
], "dispareunia")

make_card("Sintomas vasomotores", [
    ("Bochornos + amenorrea &ge;12 meses &ge;45 anos", "Menopausia"),
    ("Bochornos en &lt;40 anos + FSH alta", "Falla ovarica prematura"),
    ("Bochornos + diarrea + flushing", "Sindrome carcinoide"),
    ("Bochornos en usuaria de tamoxifeno/IA", "Efecto adverso hormonal"),
], "vasomotores")

make_card("Aumento del volumen abdominal", [
    ("Masa pelvica fija + ascitis + saciedad precoz", "Ca de ovario"),
    ("Utero crecido irregular + hipermenorrea", "Miomatosis voluminosa"),
    ("Distension + amenorrea en edad fertil", "Embarazo (descartar siempre)"),
    ("Ascitis benigna + tumor ovarico + derrame pleural", "Sindrome de Meigs"),
], "volumen_abdominal")

make_card("Disminucion de movimientos fetales", [
    ("&lt;10 movimientos en 2 h + RCTG no reactivo", "Sufrimiento fetal cronico (urgencia)"),
    ("Cese subito tras evento materno", "Obito fetal"),
    ("Disminucion + AU &lt; EG + Doppler alterado", "RCIU severo"),
], "movimientos_fetales")

make_card("Disuria / sintomas urinarios", [
    ("Disuria + polaquiuria sin fiebre en embarazada", "Cistitis"),
    ("+ fiebre + Giordano (+)", "Pielonefritis aguda"),
    ("Urocultivo &ge;10&#8309; UFC/mL sin sintomas en embarazo", "Bacteriuria asintomatica (tratar)"),
    ("Disuria + flujo mucopurulento en joven sexualmente activa", "Uretritis por Chlamydia"),
    ("Perdida de orina con esfuerzo", "Incontinencia urinaria de esfuerzo"),
    ("Urgencia + frecuencia sin infeccion", "Vejiga hiperactiva"),
], "disuria")

make_card("Galactorrea (fuera de lactancia)", [
    ("Bilateral + amenorrea + cefalea/alteraciones visuales", "Prolactinoma"),
    ("Bilateral + fatiga + estrenimiento", "Hipotiroidismo primario"),
    ("Asociada a antipsicoticos/metoclopramida", "Galactorrea farmacologica"),
    ("Sin causa, prolactina normal", "Galactorrea idiopatica"),
], "galactorrea")

make_card("Infertilidad", [
    ("Oligomenorrea + hiperandrogenismo + obesidad", "SOP (anovulacion)"),
    ("Dismenorrea progresiva + dispareunia profunda", "Endometriosis"),
    ("Antecedente de EIP / cirugia tubarica", "Factor tubarico"),
    ("Amenorrea + galactorrea", "Hiperprolactinemia"),
    ("Espermograma alterado en pareja", "Factor masculino"),
], "infertilidad")

make_card("Perdida gestacional recurrente", [
    ("Perdidas 2T recurrentes sin dolor", "Insuficiencia cervical"),
    ("TVP + abortos + plaquetopenia", "Sindrome antifosfolipido"),
    ("Cariotipo paterno/materno con translocacion", "Causa genetica parental"),
    ("Perdidas 1T + cavidad anormal en USG", "Utero septado / malformacion mulleriana"),
], "perdida_recurrente")

make_card("Adenopatia inguinal", [
    ("+ ulcera unica indolora vulvar", "Sifilis primaria"),
    ("+ vesiculas dolorosas", "Herpes genital"),
    ("+ ulceras dolorosas multiples", "Chancroide"),
    ("+ &laquo;signo del surco&raquo;", "Linfogranuloma venereo"),
    ("Dura fija + lesion vulvar pigmentada", "Ca de vulva avanzado"),
], "adenopatia_inguinal")

make_card("Sensacion de cuerpo extrano vaginal", [
    ("Bulto que asoma con Valsalva + multipara", "Prolapso de organos pelvicos"),
    ("Bulto + perdida de orina al esfuerzo", "Cistocele"),
    ("Bulto posterior + estrenimiento/digitacion", "Rectocele"),
    ("Bulto + cuello uterino visible en vulva", "Histerocele / prolapso uterino completo"),
], "prolapso")

make_card("Sintomas psicologicos del puerperio", [
    ("Llanto + labilidad dias 2-10, autolimitado", "Baby blues"),
    ("Anhedonia + insomnio + Edimburgo &ge;10 por &ge;2 sem", "Depresion postparto"),
    ("Alucinaciones + delirios + ideacion infanticida", "Psicosis puerperal"),
    ("Flashbacks de parto traumatico", "TEPT postparto"),
], "psicologico_puerperio")

make_card("Mastalgia", [
    ("Bilateral ciclica premenstrual", "Mastalgia ciclica fisiologica"),
    ("No ciclica focal punzante", "Quiste sintomatico"),
    ("Dolor reproducible a la presion costal", "Costocondritis (Tietze)"),
    ("+ fiebre en lactando", "Mastitis puerperal"),
], "mastalgia")

make_card("Ictericia en embarazo", [
    ("3T + prurito palmoplantar + sales biliares altas", "Colestasis intrahepatica del embarazo"),
    ("3T + epigastralgia + plaquetas &lt;100k", "HELLP"),
    ("3T + hipoglucemia + coagulopatia + nausea", "Higado graso agudo del embarazo"),
    ("Cualquier trimestre + dolor HCD + Murphy (+)", "Colecistitis aguda"),
    ("1T + transaminasas en miles", "Hepatitis viral aguda"),
], "ictericia_embarazo")


# ============================================================
# Build
# ============================================================
def build():
    out_path = os.path.join(OUTPUT_DIR, "Gineco_Obstetricia_Adulto_Capa6_EjeClinico.apkg")
    genanki.Package(deck).write_to_file(out_path)
    print(f"OK: {out_path}  ({len(deck.notes)} notas)")


if __name__ == "__main__":
    build()
