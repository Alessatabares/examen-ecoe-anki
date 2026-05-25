"""Capa 5 - Integrador de Discriminador Clinico (Gineco-Obstetricia Adulto).

Formato Q&A:
- Front: localizacion de exploracion + 3 discriminadores clinicos clave.
- Back: diagnostico + tip ECOE.

Pedagogia: invierte el flujo de aprendizaje. En lugar de "dado el dx -> recordar
clinica", se entrena "dado el hallazgo en exploracion -> disparar dx".
Util para ECOE donde el sinodal describe una escena y la alumna debe nombrar
el dx en segundos.

Guia: GPC mexicanas + ACOG + Williams (misma base que Capas 1-4).
"""
import os
import genanki

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "output")
os.makedirs(OUTPUT_DIR, exist_ok=True)

MODEL_QA_ID = 1607392320  # reusable Q&A
DECK_ID = 2079099594
DECK_NAME = "Gineco-Obstetricia Adulto::Capa 5 - Integrador de Discriminador Clinico"

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

BASE_TAGS = ["gineco_obstetricia", "ecoe", "capa5", "integrador"]


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
# 1. INSPECCION GENERAL / SIGNOS VITALES (6)
# ============================================================
LOC = "INSPECCION GENERAL / SIGNOS VITALES"
TAG = ["inspeccion_general"]

add(LOC,
    "TA &ge;140/90 tras 20 sem",
    "Sin edema relevante",
    "Sin sintomas",
    "HTA gestacional",
    "TA elevada despues de 20 sem sin proteinuria ni otros datos.",
    TAG + ["hta_gestacional"])

add(LOC,
    "TA &ge;140/90",
    "Edema facial / generalizado",
    "Cefalea + fosfenos",
    "Preeclampsia",
    "Preeclampsia: TA elevada + proteinuria o datos clinicos despues de 20 sem.",
    TAG + ["preeclampsia"])

add(LOC,
    "TA &ge;160/110",
    "Hiperreflexia",
    "Epigastralgia",
    "Preeclampsia con datos de severidad",
    "Datos de severidad; sulfato de Mg + antiHTA + interrupcion.",
    TAG + ["preeclampsia_severa"])

add(LOC,
    "Convulsion tonico-clonica",
    "HTA previa conocida",
    "Embarazo o postparto reciente",
    "Eclampsia",
    "ABC + sulfato de Mg + interrupcion una vez estable.",
    TAG + ["eclampsia"])

add(LOC,
    "Epigastralgia",
    "Ictericia",
    "Petequias / equimosis",
    "Sindrome HELLP",
    "HELLP; interrupcion sin demora + sulfato de Mg.",
    TAG + ["hellp"])

add(LOC,
    "Fiebre materna",
    "Taquicardia materna y fetal",
    "Irritabilidad uterina",
    "Corioamnionitis",
    "Antibiotico de amplio espectro + interrupcion independiente de la EG.",
    TAG + ["corioamnionitis"])


# ============================================================
# 2. EXPLORACION MAMARIA (6)
# ============================================================
LOC = "EXPLORACION MAMARIA"
TAG = ["mama"]

add(LOC,
    "Masa dura / fija",
    "Retraccion cutanea o piel de naranja",
    "Adenopatia axilar",
    "Cancer de mama",
    "Biopsia con aguja gruesa y referencia oncologica.",
    TAG + ["cancer_mama"])

add(LOC,
    "Masa movil firme bien delimitada",
    "Indolora",
    "Mujer &lt;30 a&ntilde;os",
    "Fibroadenoma",
    "USG mamario; observacion si BI-RADS 3.",
    TAG + ["fibroadenoma"])

add(LOC,
    "Masa lisa movil",
    "Cambia con el ciclo menstrual",
    "Mujer 30-50 a&ntilde;os",
    "Quiste mamario",
    "USG anecoico con refuerzo posterior; puncion si complejo.",
    TAG + ["quiste_mama"])

add(LOC,
    "Cuadrante eritematoso / caliente",
    "Paciente lactando",
    "Fiebre",
    "Mastitis puerperal",
    "Dicloxacilina + vaciamiento + mantener lactancia.",
    TAG + ["mastitis"])

add(LOC,
    "Masa fluctuante",
    "Signos inflamatorios marcados",
    "Post-mastitis no resuelta",
    "Absceso mamario",
    "Drenaje guiado por USG + antibiotico; mantener lactancia.",
    TAG + ["absceso_mama"])

add(LOC,
    "Eccema unilateral del pez&oacute;n",
    "Ulceracion",
    "Secrecion serosanguinolenta",
    "Enfermedad de Paget mamaria",
    "Biopsia del pezon + mamografia bilateral + RM.",
    TAG + ["paget"])


# ============================================================
# 3. EXPLORACION ABDOMINAL OBSTETRICA (6)
# ============================================================
LOC = "ABDOMEN OBSTETRICO"
TAG = ["abdomen_obstetrico"]

add(LOC,
    "&Uacute;tero le&ntilde;oso / hipertonico",
    "Dolor abdominal subito intenso",
    "Sangrado oscuro escaso",
    "DPPNI",
    "Cesarea urgente + vigilancia de coagulopatia.",
    TAG + ["dppni"])

add(LOC,
    "Cese brusco de contracciones",
    "Cicatriz uterina previa",
    "Bradicardia fetal + dolor subito",
    "Ruptura uterina",
    "Laparotomia urgente.",
    TAG + ["ruptura_uterina"])

add(LOC,
    "Altura uterina mayor que EG",
    "Hiperemesis intensa",
    "Sangrado intermitente",
    "Sospecha de enfermedad trofoblastica (mola)",
    "&beta;-hCG &gt;100,000 + USG en panal; AMEU + seguimiento.",
    TAG + ["mola"])

add(LOC,
    "Altura uterina menor que EG",
    "Oligohidramnios asociado",
    "Doppler umbilical alterado",
    "Restriccion del crecimiento intrauterino (RCIU)",
    "Vigilancia con Doppler + interrupcion segun severidad.",
    TAG + ["rciu"])

add(LOC,
    "Situacion transversa al Leopold",
    "Presentacion pelvica al termino",
    "Cabeza no encajada al termino",
    "Distocia de presentacion",
    "Cesarea programada o version externa segun caso.",
    TAG + ["distocia_presentacion"])

add(LOC,
    "FCF &lt;110 lpm",
    "Variabilidad ausente",
    "Desaceleraciones tardias repetidas",
    "Sufrimiento fetal agudo (RCTG categoria III)",
    "Reanimacion intrauterina + interrupcion.",
    TAG + ["sufrimiento_fetal"])


# ============================================================
# 4. EXPLORACION ABDOMINAL GINECOLOGICA (4)
# ============================================================
LOC = "ABDOMEN GINECOLOGICO"
TAG = ["abdomen_ginecologico"]

add(LOC,
    "&Uacute;tero crecido irregular palpable suprapubico",
    "Indoloro",
    "Movil",
    "Miomatosis uterina",
    "USG TV; manejo segun deseo reproductivo.",
    TAG + ["miomatosis"])

add(LOC,
    "Masa pelvica fija",
    "Ascitis",
    "Deterioro del estado general",
    "Cancer de ovario",
    "CA-125 + HE4 + TC; referir a oncologia ginecologica.",
    TAG + ["ca_ovario"])

add(LOC,
    "Dolor pelvico bilateral",
    "Defensa abdominal",
    "Fiebre",
    "Enfermedad pelvica inflamatoria (EIP)",
    "Triple esquema ATB; hospitalizar si embarazo o absceso.",
    TAG + ["eip"])

add(LOC,
    "Blumberg (+)",
    "Signo de Cullen",
    "Inestabilidad hemodinamica",
    "Embarazo ectopico roto",
    "Cirugia urgente + reanimacion.",
    TAG + ["ectopico_roto"])


# ============================================================
# 5. INSPECCION VULVOPERINEAL (5)
# ============================================================
LOC = "INSPECCION VULVOPERINEAL"
TAG = ["vulvoperineal"]

add(LOC,
    "&Uacute;lcera UNICA",
    "INDOLORA",
    "Bordes indurados",
    "Sifilis primaria (chancro)",
    "Penicilina G benzatinica 2.4 millones UI IM dosis unica.",
    TAG + ["sifilis"])

add(LOC,
    "Vesiculas agrupadas DOLOROSAS",
    "Adenopatia inguinal",
    "Recurrencia",
    "Herpes genital",
    "Aciclovir 400 mg c/8 h x 7-10 dias + consejeria.",
    TAG + ["herpes"])

add(LOC,
    "Lesiones verrugosas friables",
    "Acetoblanqueo (+)",
    "Crecimiento progresivo",
    "Condilomas (VPH bajo riesgo)",
    "Crioterapia, podofilino, imiquimod o escision.",
    TAG + ["condilomas"])

add(LOC,
    "Masa fluctuante en labio mayor (4-8 hr)",
    "Unilateral",
    "Dolor intenso",
    "Absceso de Bartholino",
    "Cateter de Word o marsupializacion.",
    TAG + ["bartholino"])

add(LOC,
    "Piel blanca atrofica",
    "Prurito vulvar cronico",
    "Distribucion en &laquo;8&raquo; (vulva + perianal)",
    "Liquen escleroso vulvar",
    "Clobetasol topico de alta potencia.",
    TAG + ["liquen_escleroso"])


# ============================================================
# 6. ESPECULOSCOPIA (7)
# ============================================================
LOC = "ESPECULOSCOPIA"
TAG = ["especuloscopia"]

add(LOC,
    "Flujo blanco grumoso (queso cottage)",
    "Paredes vaginales eritematosas",
    "Sin olor",
    "Candidiasis vulvovaginal",
    "Fluconazol 150 mg VO dosis unica; topico en embarazo.",
    TAG + ["candidiasis"])

add(LOC,
    "Flujo grisaceo homogeneo",
    "Olor a pescado",
    "Sin signos inflamatorios",
    "Vaginosis bacteriana",
    "Metronidazol 500 mg c/12 h x 7 dias; NO tratar pareja.",
    TAG + ["vaginosis"])

add(LOC,
    "Flujo amarillo-verdoso espumoso",
    "C&eacute;rvix en fresa",
    "Colpitis macular",
    "Tricomoniasis",
    "Metronidazol 2 g VO dosis unica + tratar pareja.",
    TAG + ["tricomoniasis"])

add(LOC,
    "Cervix friable",
    "Flujo mucopurulento endocervical",
    "Sangrado al contacto",
    "Cervicitis por gonococo / clamidia",
    "Ceftriaxona 500 mg IM + doxiciclina 7 dias.",
    TAG + ["cervicitis"])

add(LOC,
    "Lesion exofitica / ulcerada en cervix",
    "Sangrado al contacto",
    "Cervix duro irregular",
    "Cancer cervicouterino invasor",
    "Referencia urgente a oncologia ginecologica.",
    TAG + ["cancer_cervix"])

add(LOC,
    "Salida franca de liquido por cervix",
    "Liquido en fondo de saco posterior",
    "Sin sangrado activo",
    "Ruptura prematura de membranas (RPM)",
    "Manejo segun EG; cristalizacion + nitrazina para confirmar.",
    TAG + ["rpm"])

add(LOC,
    "Sangrado rojo brillante INDOLORO",
    "Cervix sin modificaciones",
    "NO realizar tacto vaginal",
    "Placenta previa",
    "USG TV, NO tacto; cesarea segun semanas y severidad.",
    TAG + ["placenta_previa"])


# ============================================================
# 7. TACTO BIMANUAL GINECOLOGICO (6)
# ============================================================
LOC = "TACTO BIMANUAL GINECOLOGICO"
TAG = ["tacto_bimanual"]

add(LOC,
    "&Uacute;tero aumentado de tama&ntilde;o",
    "Sangrado postmenopausico al retirar el dedo",
    "Cuello normal",
    "Cancer de endometrio",
    "USG TV (endometrio &ge;5 mm) + biopsia con Pipelle.",
    TAG + ["cancer_endometrio"])

add(LOC,
    "&Uacute;tero globoso SIMETRICO",
    "Doloroso a la movilizacion",
    "Consistencia reblandecida",
    "Adenomiosis",
    "USG TV o RM (zona juncional &gt;12 mm).",
    TAG + ["adenomiosis"])

add(LOC,
    "Nodularidad en fondo de saco posterior",
    "Dolor a la movilizacion",
    "&Uacute;tero fijo / retrovertido",
    "Endometriosis profunda infiltrante",
    "USG TV + RM; laparoscopia gold standard.",
    TAG + ["endometriosis"])

add(LOC,
    "Dolor a la movilizacion cervical",
    "Masa anexial dolorosa",
    "Cuello con flujo purulento",
    "Enfermedad pelvica inflamatoria (EIP)",
    "Triada de Hager; triple esquema ATB.",
    TAG + ["eip"])

add(LOC,
    "Masa anexial unilateral dolorosa",
    "&Uacute;tero menor que amenorrea",
    "Dolor a la movilizacion cervical",
    "Embarazo ectopico no roto",
    "&beta;-hCG + USG TV; MTX si criterios o cirugia.",
    TAG + ["ectopico"])

add(LOC,
    "Hirsutismo / acne",
    "Ovarios palpables aumentados",
    "Obesidad centroabdominal",
    "Sindrome de ovario poliquistico (SOP)",
    "Rotterdam 2/3; estilo de vida + ACO o letrozol.",
    TAG + ["sop"])


# ============================================================
# 8. TACTO VAGINAL OBSTETRICO (6)
# ============================================================
LOC = "TACTO VAGINAL OBSTETRICO"
TAG = ["tacto_obstetrico"]

add(LOC,
    "Dilatacion progresiva",
    "Borramiento",
    "Descenso de presentacion",
    "Trabajo de parto verdadero",
    "Ingreso a labor + vigilancia con partograma.",
    TAG + ["tp_verdadero"])

add(LOC,
    "Trabajo de parto entre 24-37 sem",
    "Contracciones regulares",
    "Cuello modificandose",
    "Trabajo de parto pretermino",
    "Tocolisis 48 h + maduracion pulmonar + Mg si &lt;32 sem.",
    TAG + ["pretermino"])

add(LOC,
    "Cuello CERRADO",
    "Sangrado escaso",
    "Sin restos en OCI",
    "Amenaza de aborto",
    "Reposo relativo + datos de alarma + USG control.",
    TAG + ["amenaza_aborto"])

add(LOC,
    "Cuello DILATADO",
    "Restos visibles / palpables en OCI",
    "Sangrado activo",
    "Aborto en evolucion / incompleto",
    "AMEU o misoprostol segun caso.",
    TAG + ["aborto_incompleto"])

add(LOC,
    "Signo de la tortuga tras salir la cabeza",
    "Hombro anterior atascado",
    "Cabeza retraida al perine",
    "Distocia de hombros",
    "McRoberts + presion suprapubica; nemotecnia HELPERR.",
    TAG + ["distocia_hombros"])

add(LOC,
    "&Uacute;tero blando supraumbilical",
    "Sangrado abundante activo",
    "Sin contraccion tras masaje",
    "Atonia uterina (hemorragia postparto T1)",
    "Masaje + uterotonicos escalonados; balon de Bakri si refractario.",
    TAG + ["atonia"])


# ============================================================
# Build
# ============================================================
def build():
    out_path = os.path.join(OUTPUT_DIR, "Gineco_Obstetricia_Adulto_Capa5_Integrador.apkg")
    genanki.Package(deck).write_to_file(out_path)
    print(f"OK: {out_path}  ({len(deck.notes)} notas)")


if __name__ == "__main__":
    build()
