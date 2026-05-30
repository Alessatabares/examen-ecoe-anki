"""Deck de EJES DIAGNOSTICOS (Adulto) - matriz sistema x eje etiologico.

Filosofia: para cada sistema/sitio anatomico, recorrer los 10 ejes de causa.
  Eje 01 Topografico: cuando falla el sitio, que diferencial por localizacion.
  Eje 02 Vascular ... Eje 10 Toxico/Farmacologico: que pensar por cada mecanismo.

Estructura: 10 subdecks (uno por eje). Front = sistema dentro del eje;
Back = diferencial + pista (tabla en Eje 01, linea en Ejes 02-10). Q&A.

Construido directo desde las tablas maestras (ancladas en el contenido ECOE del repo:
ATLS, ADA, AHA/ACC, KDIGO, GINA/GOLD, ATA, USPSTF, etc.).
"""
import os
import genanki

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "output")
os.makedirs(OUTPUT_DIR, exist_ok=True)

MODEL_QA_ID = 1607392320  # reusable (ids.json: qa_estandar)

# 10 deck_ids nuevos, unicos
DECK_IDS = {
    "01 - Topografico":              1290110011,
    "02 - Vascular":                 1290220022,
    "03 - Infeccioso":               1290330033,
    "04 - Metabolico-Endocrino":     1290440044,
    "05 - Degenerativo":             1290550055,
    "06 - Congenito":                1290660066,
    "07 - Traumatico":               1290770077,
    "08 - Autoinmune-Inflamatorio":  1290880088,
    "09 - Neoplasico":               1290990099,
    "10 - Toxico-Farmacologico":     1291010101,
}
PADRE = "Ejes Diagnosticos Adulto"

CSS_BASE = """
.card { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  font-size: 19px; text-align: left; color: #1a1a1a; background-color: #fafafa;
  padding: 20px; line-height: 1.5; }
#extra { margin-top: 16px; border: none; border-top: 1px solid #d4d4d4; padding-top: 12px; }
.disc { color: #6d28d9; display: block; margin-top: 10px; font-weight: 600; }
.redflag { color: #b91c1c; font-weight: 600; display: block; margin-top: 8px; }
.q { font-weight: 600; color: #1d4ed8; }
table { border-collapse: collapse; width: 100%; margin-top: 8px; font-size: 15px; }
th, td { border: 1px solid #cbd5e1; padding: 5px 8px; text-align: left; vertical-align: top; }
th { background: #eef2ff; color: #111; }
td b { color: #b91c1c; }
b { color: #111; }
"""

model_qa = genanki.Model(
    MODEL_QA_ID, "Estudio Medico QA",
    fields=[{"name": "Front"}, {"name": "Back"}],
    templates=[{"name": "QA", "qfmt": '<div class="q">{{Front}}</div>',
                "afmt": '<div class="q">{{Front}}</div><hr id="extra">{{Back}}'}],
    css=CSS_BASE,
)

# Etiqueta corta por sistema (para tags y front)
SYS_TAG = {
    "Pulmon / Respiratorio": "pulmon", "Corazon": "corazon",
    "Higado / Biliar / Pancreas": "higado", "Intestino": "intestino",
    "Rinon / Urinario": "rinon", "Cerebro / SNC": "cerebro", "Ojo": "ojo",
    "Oido": "oido", "Endocrino / Suprarrenal": "endocrino",
    "Ap. reproductor femenino": "repro_fem", "Ap. reproductor masculino": "repro_masc",
    "Cabeza / Craneofacial": "cabeza", "Musculoesqueletico": "musculoesqueletico",
    "Piel": "piel", "Sangre / Hematologico": "sangre",
    "Nariz / Garganta / Cuello": "orl_cuello", "Boca / Dental": "boca",
    "Vascular periferico": "vascular_perif", "Inmune": "inmune",
}

# ============================================================
# EJE 01 - TOPOGRAFICO  (system -> [(sitio, diferencial, pista), ...])
# ============================================================
EJE1 = {
"Pulmon / Respiratorio": [
 ("Bronquio (reversible)", "<b>Asma</b>", "obstruccion que revierte con broncodilatador"),
 ("Bronquio (no reversible)", "<b>EPOC</b>", "tabaquismo &gt;10 paq-ano, no revierte"),
 ("Alveolo (exudado)", "<b>Neumonia</b> · TB", "crepitantes localizados + consolidacion; TB si cronico/hemoptisis"),
 ("Pleura (aire a presion)", "<b>Neumotorax a tension</b>", "desviacion traqueal + IY + timpanismo; dx clinico"),
 ("Pleura (liquido/sangre)", "Derrame / hemotorax / empiema", "matidez + ausencia de murmullo"),
 ("Vasculatura pulmonar", "<b>TEP</b> · hipertension pulmonar", "disnea subita + Wells"),
 ("Intersticio", "EPID / fibrosis", "crepitantes velcro, disnea progresiva")],
"Corazon": [
 ("Coronaria", "<b>SCA</b> (IAMCEST/IAMSEST/angina)", "ST elevado vs troponina"),
 ("Miocardio (bomba)", "<b>IC</b> (FEr sistolica / FEp diastolica)", "S3 vs S4; FEVI"),
 ("Sistema electrico", "<b>Arritmia</b> (FA, TV, bloqueos)", "pulso irregular; ECG"),
 ("Pericardio", "Pericarditis / <b>Tamponade</b>", "frote; triada de Beck"),
 ("Valvula", "Estenosis/insuf. Ao-Mi · endocarditis", "soplo + foco; fiebre + soplo nuevo"),
 ("Aorta", "<b>Diseccion</b> · <b>AAA roto</b>", "dolor desgarrante, pulsos asimetricos; masa pulsatil"),
 ("Trauma", "Trauma penetrante &rarr; tamponade", "herida precordial + Beck")],
"Higado / Biliar / Pancreas": [
 ("Parenquima agudo", "Hepatitis (viral/alcoholica)", "AST/ALT &gt;2 + GGT = alcohol"),
 ("Parenquima cronico", "<b>MASLD/MASH</b> · cirrosis", "AST/ALT &lt;1 + sd metabolico"),
 ("Circulacion portal", "<b>Hipertension portal</b>", "varices + ascitis + esplenomegalia"),
 ("Funcion sintetica/detox", "Insuficiencia hepatica", "encefalopatia, ictericia, coagulopatia"),
 ("Via biliar", "Colelitiasis / colecistitis / <b>colangitis</b>", "Murphy; triada de Charcot"),
 ("Pancreas exocrino", "<b>Pancreatitis</b> · cancer", "lipasa &gt;3x; dolor en cinturon"),
 ("Pancreas endocrino (islotes)", "DM · insulinoma · hipoglucemia", "glucosa")],
"Intestino": [
 ("Esofago", "ERGE · varices · acalasia · Mallory-Weiss · Boerhaave", "hematemesis; disfagia"),
 ("Estomago/duodeno", "<b>Ulcera/HDA</b> · perforacion · cancer", "AINE/H. pylori; abdomen en tabla + aire libre"),
 ("Intestino delgado", "<b>Obstruccion</b> · isquemia mesenterica · Crohn", "vomito bilioso; dolor desproporcionado + FA"),
 ("Apendice", "<b>Apendicitis</b>", "dolor migra a FID"),
 ("Colon", "Diverticulitis · volvulo · Ca colon · CU · HDB", "FII &gt;50a; hematoquezia"),
 ("Recto/ano", "Hemorroides · fisura · absceso", "rectorragia roja brillante"),
 ("Peritoneo", "<b>Peritonitis</b>", "abdomen en tabla + sepsis")],
"Rinon / Urinario": [
 ("Perfusion (prerrenal)", "<b>AKI prerrenal</b>", "FeNa &lt;1%, BUN/Cr &gt;20"),
 ("Glomerulo", "Sd. nefrotico / nefritico", "proteinuria &gt;3.5 vs hematuria + cilindros"),
 ("Tubulo/intersticio", "NTA · nefritis intersticial", "FeNa &gt;2%, cilindros granulosos"),
 ("Obstruccion (postrenal)", "Litiasis · HBP · hidronefrosis", "anuria + hidronefrosis USG"),
 ("Funcion cronica", "<b>ERC</b>", "eGFR bajo + albuminuria (G/A KDIGO)"),
 ("Vejiga / pelvis renal", "Cistitis (baja) vs pielonefritis (alta)", "disuria sin fiebre vs fiebre + lumbalgia")],
"Cerebro / SNC": [
 ("Vascular", "<b>EVC</b> isquemico · hemorragico · <b>HSA</b>", "deficit focal subito; cefalea en trueno = HSA"),
 ("Meninges", "<b>Meningitis</b> · encefalitis", "fiebre + rigidez nucal + fotofobia"),
 ("Masa/presion", "HIC · tumor · absceso · hidrocefalia", "cefalea progresiva + papiledema + vomito"),
 ("Electrico", "Crisis convulsiva / status", "movimientos + postictal"),
 ("Medula", "Compresion medular · Guillain-Barre · EM", "nivel sensitivo; debilidad ascendente"),
 ("Degenerativo", "Demencia · Parkinson", "cronicidad"),
 ("Trauma", "TCE · hematoma epidural/subdural", "intervalo lucido vs anciano/ACO")],
"Ojo": [
 ("Ojo rojo", "Conjuntivitis · uveitis · <b>glaucoma agudo</b> · escleritis", "doloroso + halos + midriasis = glaucoma agudo"),
 ("Perdida visual subita", "Oclusion art/vena retiniana · desprendimiento · neuritis optica", "indolora subita; cortina/destellos"),
 ("Perdida visual gradual", "Cataratas · glaucoma cronico · DMAE · retinopatia DM", "cronicidad + comorbilidad"),
 ("Orbita/parpado", "<b>Celulitis orbitaria</b> vs preseptal · orzuelo", "dolor a la mirada + proptosis = orbitaria")],
"Oido": [
 ("Conducto externo", "<b>Otitis externa</b>", "dolor al traccionar pabellon (signo del trago)"),
 ("Oido medio", "Otitis media · derrame · colesteatoma", "dolor interno tras IVAS; otorrea cronica fetida"),
 ("Oido interno/vestibulo", "Vertigo (VPPB, Meniere, neuritis) · hipoacusia neurosensorial", "posicional vs continuo + acufeno"),
 ("Mastoides", "<b>Mastoiditis</b>", "desplazamiento del pabellon + dolor retroauricular")],
"Endocrino / Suprarrenal": [
 ("Hipotalamo-hipofisis", "DI · SIADH · prolactinoma · acromegalia · panhipopituitarismo", "Na+; campos visuales"),
 ("Tiroides", "Hipo / hipertiroidismo · tormenta · coma mixedematoso", "TSH opuesta a la clinica"),
 ("Paratiroides", "Hiper / hipoparatiroidismo", "calcio serico"),
 ("Suprarrenal - corteza", "Insuf. suprarrenal/crisis (Addison) · Cushing · Conn", "hipoTA+hipoNa+hiperK; HTA+hipoK"),
 ("Suprarrenal - medula", "<b>Feocromocitoma</b>", "HTA paroxistica + cefalea + sudoracion + palpitaciones"),
 ("Islotes beta (insulina)", "DM1/DM2 · CAD · EHH · insulinoma", "cetonas/acidosis vs osmolaridad"),
 ("Hueso", "Osteoporosis", "DMO T-score &le; -2.5")],
"Ap. reproductor femenino": [
 ("Utero", "Miomas · sangrado uterino anormal · Ca endometrio", "sangrado posmenopausico = Ca"),
 ("Embarazo (anexo/utero)", "<b>Ectopico roto</b> · aborto · DPPNI · placenta previa", "amenorrea + dolor + inestabilidad = ectopico"),
 ("Embarazo (sistemico)", "<b>Preeclampsia/eclampsia</b>", "HTA + proteinuria &gt;20 sem"),
 ("Ovario/anexo", "Torsion ovarica · quiste · EPI · Ca ovario", "dolor subito; dolor a movilizacion cervical"),
 ("Cervix", "Ca cervicouterino · cervicitis", "sangrado poscoital"),
 ("Mama", "<b>Ca de mama</b> · mastitis · fibroadenoma", "masa dura fija; piel de naranja"),
 ("Vulvovaginal", "Vaginosis · candidiasis · ITS", "flujo caracteristico")],
"Ap. reproductor masculino": [
 ("Testiculo", "<b>Torsion testicular</b> · epididimitis · Ca · varicocele/hidrocele", "Prehn negativo + sin cremasterico = torsion (6h)"),
 ("Prostata", "HBP · prostatitis · Ca de prostata", "LUTS; tacto rectal + APE"),
 ("Pene", "Disfuncion erectil · <b>priapismo</b> · balanitis · fimosis", "ereccion &gt;4h dolorosa = urgencia"),
 ("Uretra", "Uretritis (gonococica/no)", "secrecion + ITS")],
"Cabeza / Craneofacial": [
 ("Cefaleas primarias", "Tensional · migrana · cluster", "bilateral en banda vs pulsatil hemicraneal"),
 ("Cefalea secundaria", "Red flags (trueno, fiebre, foco, &gt;50a)", "descartar HSA, ACG, masa"),
 ("Arteria temporal", "<b>Arteritis de celulas gigantes</b>", "&gt;50a + cefalea temporal + claudicacion mandibula + vision baja"),
 ("Senos", "Sinusitis", "dolor facial + rinorrea purulenta &gt;10 d"),
 ("Nervio facial/trigemino", "Paralisis de Bell · neuralgia del trigemino", "paralisis facial periferica (afecta frente)"),
 ("Glandula salival", "Parotiditis · sialolitiasis", "tumefaccion preauricular")],
"Musculoesqueletico": [
 ("Monoartritis aguda", "Gota · <b>artritis septica</b> · pseudogota", "cristales; septica = aspirar SIEMPRE"),
 ("Poliartritis", "AR · LES · psoriasica", "simetrica + anti-CCP; rash malar"),
 ("Cintura escapular/pelvica &gt;50a", "PMR", "VSG/PCR muy altas"),
 ("Hueso", "Fractura · osteomielitis · osteoporosis · metastasis", "dolor + fiebre; T-score &le; -2.5"),
 ("Columna", "Lumbalgia mecanica vs red flags · hernia discal", "radicular vs cola de caballo")],
"Piel": [
 ("Infeccion superficial", "Celulitis · erisipela · impetigo", "bordes; erisipela bien delimitada"),
 ("Infeccion profunda", "<b>Fascitis necrotizante</b>", "dolor desproporcionado + crepitacion"),
 ("Exantema grave", "<b>SSJ/NET</b> · DRESS", "Nikolsky + mucosas + farmaco"),
 ("Tumor", "Melanoma · CBC · CEC", "ABCDE"),
 ("Ulcera", "Venosa · arterial · diabetica · por presion", "localizacion + pulsos")],
"Sangre / Hematologico": [
 ("Serie roja (baja)", "Anemia micro/normo/macro", "clasificar por VCM"),
 ("Serie roja (alta)", "Policitemia", "Hto alto, prurito"),
 ("Serie blanca/medula", "Leucemia · linfoma · <b>neutropenia febril</b>", "blastos; fiebre + neutropenia = urgencia"),
 ("Plaquetas", "Trombocitopenia (PTI, PTT) · trombocitosis", "petequias; PTT = pentada"),
 ("Coagulacion", "Hemofilia · CID · deficit vit K", "TP/TTPa; sangrado + consumo"),
 ("Trombosis", "Trombofilia · TVP/TEP", "edema unilateral; Wells")],
"Nariz / Garganta / Cuello": [
 ("Nariz", "Epistaxis · rinitis · polipos · cuerpo extrano", "anterior (Kiesselbach) vs posterior"),
 ("Garganta", "Faringoamigdalitis · absceso periamigdalino · <b>epiglotitis</b> · laringitis", "voz de papa caliente; babeo + estridor"),
 ("Cuello", "Adenopatias · masa tiroidea · absceso profundo · quiste", "duracion; consistencia"),
 ("Via aerea", "<b>Obstruccion / estridor</b>", "tiraje, cianosis")],
"Boca / Dental": [
 ("Diente/encia", "Absceso dentario · gingivitis/periodontitis", "dolor + tumefaccion focal"),
 ("Mucosa", "Aftas · candidiasis · leucoplasia · Ca oral", "placas que no se desprenden = sospecha"),
 ("Piso de boca", "<b>Angina de Ludwig</b>", "celulitis submandibular + via aerea")],
"Vascular periferico": [
 ("Venoso agudo", "<b>TVP</b>", "edema unilateral + Wells"),
 ("Venoso cronico", "Insuf. venosa · varices · ulcera venosa", "maleolar interna"),
 ("Arterial agudo", "<b>Isquemia arterial aguda</b>", "6 P; urgencia"),
 ("Arterial cronico", "EAP", "claudicacion; ITB &lt;0.9"),
 ("Linfatico", "Linfedema", "sin fovea")],
"Inmune": [
 ("Reaccion sistemica", "<b>Anafilaxia</b>", "via aerea + hipotension + urticaria &rarr; adrenalina IM"),
 ("Submucosa", "Angioedema (IECA, hereditario C1-INH)", "sin urticaria &rarr; bradicinina"),
 ("Farmacologica grave", "DRESS · SSJ/NET", "eosinofilia + organo")],
}

# ============================================================
# EJES 02-10  (eje -> system -> (diferencial, pista))
# ============================================================
EJES = {
"02 - Vascular": {
 "Pulmon / Respiratorio": ("<b>TEP</b> / infarto pulmonar · hipertension pulmonar · hemorragia alveolar", "embolo venoso; HTP &rarr; cor pulmonale"),
 "Corazon": ("<b>SCA/IAM</b> (oclusion coronaria) · IC isquemica · <b>diseccion aortica</b>", "trombo sobre placa; dolor desgarrante"),
 "Higado / Biliar / Pancreas": ("<b>Budd-Chiari</b> · trombosis portal · higado de shock (isquemico)", "ascitis subita; hipoperfusion &rarr; ALT muy alta"),
 "Intestino": ("<b>Isquemia mesenterica aguda</b> · colitis isquemica · trombosis venosa mesenterica · angiodisplasia", "dolor desproporcionado + FA"),
 "Rinon / Urinario": ("Estenosis art. renal (HTA renovascular) · infarto renal · trombosis vena renal · nefroangioesclerosis · <b>SHU/PTT</b>", "HTA refractaria; flanco + LDH alta"),
 "Cerebro / SNC": ("<b>EVC isquemico</b> · hemorragico · <b>HSA</b> (aneurisma) · trombosis venosa cerebral", "deficit focal subito; cefalea en trueno"),
 "Ojo": ("<b>OACR</b> · <b>OVCR</b> · NAION · amaurosis fugax · retinopatia HTA/DM", "perdida visual indolora subita"),
 "Oido": ("Hipoacusia subita neurosensorial (isquemia laberintica) · acufeno pulsatil (glomus)", "unilateral subita; soplo"),
 "Endocrino / Suprarrenal": ("<b>Apoplejia hipofisaria</b> (Sheehan) · <b>hemorragia suprarrenal</b> (Waterhouse-Friderichsen)", "shock + hipoglucemia; meningococo"),
 "Ap. reproductor femenino": ("<b>Ectopico roto</b> · <b>DPPNI</b> · torsion ovarica · trombosis ovarica", "hemoperitoneo; compromiso vascular del anexo"),
 "Ap. reproductor masculino": ("<b>Torsion testicular</b> (isquemia) · varicocele · priapismo (estasis)", "ventana 6 h; ereccion &gt;4h"),
 "Cabeza / Craneofacial": ("<b>Arteritis de celulas gigantes</b> · malformacion AV", "vision baja + claudicacion mandibula + VSG alta"),
 "Musculoesqueletico": ("<b>Necrosis avascular</b> · <b>sindrome compartimental</b> · vasculitis", "corticoides/cadera; dolor desproporcionado + 6 P"),
 "Piel": ("<b>Vasculitis</b> (purpura palpable) · Raynaud · isquemia/gangrena · ulcera arterial", "purpura en miembros; trifasico de color"),
 "Nariz / Garganta / Cuello": ("Epistaxis · vasculitis (GPA/Wegener)", "Kiesselbach; ANCA"),
 "Vascular periferico": ("<b>TVP</b> · <b>isquemia arterial aguda</b> · EAP · aneurisma (AAA)", "es el organo vaso mismo"),
 "Inmune": ("<b>Vasculitis sistemicas</b> (ANCA, IgA, arteritis)", "purpura, mononeuritis, reactantes altos"),
},
"03 - Infeccioso": {
 "Pulmon / Respiratorio": ("<b>Neumonia</b> · <b>TB</b> · absceso · empiema · PCP", "S. pneumoniae; TB si cronico+hemoptisis; PCP en VIH"),
 "Corazon": ("<b>Endocarditis</b> · miocarditis viral · pericarditis · fiebre reumatica", "fiebre + soplo nuevo (Duke); Coxsackie"),
 "Higado / Biliar / Pancreas": ("<b>Hepatitis viral A-E</b> · absceso (piogeno/amebiano) · <b>colangitis</b> · <b>PBE</b>", "Charcot = colangitis; PBE = ascitis + PMN &gt;250"),
 "Intestino": ("<b>Gastroenteritis</b> · <b>C. difficile</b> · fiebre tifoidea · parasitosis · diverticulitis", "ATB reciente = C. diff; sangre+fiebre = invasiva"),
 "Rinon / Urinario": ("<b>Cistitis</b> · <b>pielonefritis</b> · prostatitis · absceso renal", "E. coli; fiebre+lumbalgia = alta"),
 "Cerebro / SNC": ("<b>Meningitis</b> · <b>encefalitis</b> (HSV) · absceso · neurocisticercosis", "rigidez nucal; HSV = temporal + crisis"),
 "Ojo": ("Conjuntivitis · queratitis · <b>endoftalmitis</b> · <b>celulitis orbitaria</b>", "lente de contacto = Pseudomonas; proptosis dolorosa"),
 "Oido": ("<b>Otitis externa</b> · <b>otitis media</b> · <b>mastoiditis</b> · otomicosis", "Pseudomonas (externa); pabellon desplazado = mastoiditis"),
 "Endocrino / Suprarrenal": ("<b>Tiroiditis subaguda (De Quervain)</b> · suprarrenalitis (TB/histo) · <b>Waterhouse-Friderichsen</b>", "tiroides dolorosa posviral; meningococo"),
 "Ap. reproductor femenino": ("<b>EPI</b> · cervicitis/vaginitis (ITS) · <b>corioamnionitis</b> · endometritis · absceso tuboovarico · mastitis", "dolor a movilizacion cervical; gonococo/clamidia"),
 "Ap. reproductor masculino": ("<b>Uretritis</b> (gonococica/clamidia) · <b>epididimitis/orquitis</b> · prostatitis", "secrecion uretral; Prehn positivo"),
 "Cabeza / Craneofacial": ("<b>Sinusitis</b> · <b>parotiditis</b> · celulitis facial · <b>Ramsay Hunt</b>", "&gt;10 d purulento; paralisis facial + vesiculas"),
 "Musculoesqueletico": ("<b>Artritis septica</b> · <b>osteomielitis</b> · espondilodiscitis · piomiositis", "monoartritis caliente &rarr; aspirar; S. aureus"),
 "Piel": ("<b>Celulitis/erisipela</b> · impetigo · absceso · <b>fascitis necrotizante</b> · herpes/varicela", "S. pyogenes/aureus; dolor desproporcionado = necrotizante"),
 "Sangre / Hematologico": ("<b>Sepsis/bacteriemia</b> · <b>neutropenia febril</b> · malaria · mononucleosis · VIH", "qSOFA; neutrofilos &lt;500 = urgencia"),
 "Nariz / Garganta / Cuello": ("<b>Faringitis estreptococica</b> · absceso periamigdalino/retrofaringeo · <b>epiglotitis</b> · difteria", "Centor; babeo + estridor = epiglotitis"),
 "Boca / Dental": ("<b>Absceso dentario</b> · <b>candidiasis oral</b> · <b>angina de Ludwig</b> · herpangina", "placas que no se desprenden; piso de boca + via aerea"),
 "Vascular periferico": ("<b>Tromboflebitis septica</b> · infeccion de cateter/injerto · ulcera infectada", "cordon eritematoso + fiebre"),
 "Inmune": ("<b>Sepsis</b> · <b>oportunistas</b> (PCP, CMV, candidiasis, TB, criptococo)", "CD4 bajo guia el germen"),
},
"04 - Metabolico-Endocrino": {
 "Pulmon / Respiratorio": ("<b>Respiracion de Kussmaul</b> (acidosis) · hipoventilacion por mixedema · derrame en hipotiroidismo", "compensacion de CAD; TSH alta"),
 "Corazon": ("Hiper &rarr; FA/alto gasto; hipo &rarr; bradicardia · <b>dis-K/dis-Ca &rarr; arritmias</b> · DM/dislipidemia &rarr; ateroesclerosis · feocromocitoma", "K (T picudas/U); Ca (QT); catecolaminas"),
 "Higado / Biliar / Pancreas": ("<b>MASLD/MASH</b> · <b>hemocromatosis</b> · <b>Wilson</b> · deficit a1-antitripsina · glucogenosis", "DM/sd metabolico; ferritina/Cu"),
 "Intestino": ("Hiper &rarr; diarrea / hipo &rarr; estrenimiento · <b>gastroparesia diabetica</b> · hiperCa estrenimiento · hipoK ileo · celiaquia", "TSH; glucosa cronica"),
 "Rinon / Urinario": ("<b>Nefropatia diabetica</b> · nefroangioesclerosis · hiperCa (litiasis) · hiperuricemia · <b>DI/SIADH</b>", "UACR/eGFR; Na y osmolaridad"),
 "Cerebro / SNC": ("<b>Hipo/hiperglucemia</b> (CAD/EHH) · <b>hipo/hiperNa</b> · enc. hepatica/uremica · <b>Wernicke</b> · mixedema/tormenta", "glucosa primero; corregir Na lento"),
 "Ojo": ("<b>Retinopatia diabetica</b> · retinopatia HTA · <b>orbitopatia de Graves</b> · catarata (DM/esteroides) · xantelasma", "fondo de ojo; proptosis = Graves"),
 "Oido": ("DM &rarr; <b>otitis externa maligna</b> · hipotiroidismo &rarr; hipoacusia", "diabetico + otalgia severa + paralisis facial"),
 "Endocrino / Suprarrenal": ("<b>Hipofisis</b>: panhipopit/acromegalia/prolactinoma/DI/SIADH · <b>Tiroides</b> · <b>Paratiroides</b> · <b>Suprarrenal</b> (Addison/Cushing/Conn/feo) · <b>Islotes</b> (DM/CAD/EHH)", "la glandula define el eje; pensar MEN si multiples"),
 "Ap. reproductor femenino": ("<b>SOP</b> · hiperprolactinemia · tiroides &rarr; trastorno menstrual · <b>DM gestacional</b> · Sheehan", "hirsutismo + oligomenorrea; prolactina"),
 "Ap. reproductor masculino": ("<b>Hipogonadismo</b> · DM &rarr; <b>disfuncion erectil</b> · hiperprolactinemia · ginecomastia", "libido + testosterona/prolactina"),
 "Cabeza / Craneofacial": ("<b>Acromegalia</b> · <b>Cushing</b> (cara de luna) · facies mixedematosa · tumor hipofisario", "rasgos faciales; hemianopsia bitemporal"),
 "Musculoesqueletico": ("<b>Osteoporosis</b> · <b>osteomalacia</b> (vit D) · <b>gota</b> (urato) · pseudogota · miopatia tiroidea/esteroidea", "T-score; acido urico; PTH/Ca"),
 "Piel": ("<b>Acantosis nigricans</b> · necrobiosis lipoidica · <b>mixedema pretibial</b> · estrias (Cushing) · <b>hiperpigmentacion</b> (Addison) · xantomas", "el signo cutaneo delata la endocrinopatia"),
 "Sangre / Hematologico": ("Anemia de hipotiroidismo · anemia de ERC (EPO) · <b>B12/perniciosa</b> · policitemia (tumor EPO)", "TSH, eGFR; macrocitosis"),
 "Nariz / Garganta / Cuello": ("<b>Bocio/nodulo/Ca tiroideo</b> · adenoma paratiroideo · quiste tirogloso · acromegalia &rarr; macroglosia", "masa cervical que sigue deglucion"),
 "Boca / Dental": ("DM &rarr; periodontitis/candidiasis · pigmentacion (Addison) · glositis (B12/hierro) · macroglosia", "control glucemico; lengua lisa"),
 "Vascular periferico": ("DM &rarr; micro/macroangiopatia, <b>pie diabetico</b> · dislipidemia &rarr; EAP · hiperhomocisteinemia", "ITB; ulcera neuroisquemica"),
 "Inmune": ("Hiperglucemia &rarr; inmunosupresion · Cushing &rarr; inmunosupresion · <b>sd. poliglandular autoinmune</b>", "diabetico/esteroides + infeccion recurrente"),
},
"05 - Degenerativo": {
 "Pulmon / Respiratorio": ("<b>Enfisema</b> · <b>fibrosis pulmonar idiopatica</b> · perdida de retroceso elastico senil", "disnea progresiva; crepitantes velcro + panal en TC"),
 "Corazon": ("<b>Estenosis aortica calcificada (senil)</b> · calcificacion anular mitral · <b>fibrosis del sistema de conduccion</b> · amiloidosis", "soplo en &gt;70a; bloqueo AV del anciano"),
 "Higado / Biliar / Pancreas": ("<b>Cirrosis</b> (fibrosis terminal) · atrofia hepatica", "nodularidad + hipertension portal"),
 "Intestino": ("<b>Diverticulosis</b> · presbiesofago · gastritis atrofica · estrenimiento por dismotilidad", "hematoquezia/diverticulitis en &gt;60a"),
 "Rinon / Urinario": ("<b>Nefroesclerosis/glomeruloesclerosis</b> del envejecimiento · caida fisiologica del FG", "eGFR bajo progresivo sin otra causa"),
 "Cerebro / SNC": ("<b>Alzheimer</b> · demencia vascular · cuerpos de Lewy · frontotemporal · <b>Parkinson</b> · <b>ELA</b> · Huntington", "demencia vs trastorno del movimiento"),
 "Ojo": ("<b>Catarata senil</b> · <b>DMAE</b> · glaucoma cronico · presbicia", "perdida visual gradual; central (DMAE) vs periferica (glaucoma)"),
 "Oido": ("<b>Presbiacusia</b> · otosclerosis", "hipoacusia neurosensorial bilateral del anciano"),
 "Endocrino / Suprarrenal": ("<b>Menopausia</b> · andropausia · <b>declive de celulas beta</b> (DM2) · atrofia tiroidea · somatopausia", "hormona que cae con la edad"),
 "Ap. reproductor femenino": ("<b>Menopausia</b> · atrofia urogenital · <b>prolapso de organos pelvicos</b> · incontinencia", "debilitamiento del soporte; sequedad vaginal"),
 "Ap. reproductor masculino": ("<b>HBP</b> · andropausia · disfuncion erectil", "LUTS progresivos; tacto rectal liso aumentado"),
 "Cabeza / Craneofacial": ("Osteoartritis de <b>ATM</b> · atrofia osea facial · atrofia cerebral", "crepitacion/dolor mandibular"),
 "Musculoesqueletico": ("<b>Artrosis (osteoartritis)</b> · <b>osteoporosis</b> · espondilosis/<b>estenosis de canal</b> · <b>sarcopenia</b> · rotura de manguito", "dolor mecanico que mejora con reposo; nodulos de Heberden"),
 "Piel": ("<b>Fotoenvejecimiento/elastosis</b> · <b>purpura senil</b> · dermatoporosis · queratosis seborreica/actinica", "atrofia + fragilidad; lesiones actinicas"),
 "Sangre / Hematologico": ("<b>Sindrome mielodisplasico</b> · anemia del anciano · declive de reserva medular", "citopenias + displasia en &gt;70a"),
 "Nariz / Garganta / Cuello": ("<b>Presbifonia</b> (atrofia de cuerdas) · presbifagia", "voz debil; disfagia del anciano"),
 "Boca / Dental": ("<b>Edentulismo</b> · recesion gingival · desgaste dental · xerostomia", "perdida de piezas; boca seca"),
 "Vascular periferico": ("<b>Ateroesclerosis</b> · <b>rigidez arterial</b> · <b>aneurisma</b> (AAA) · varices", "claudicacion; masa pulsatil; PA sistolica aislada alta"),
 "Inmune": ("<b>Inmunosenescencia</b>", "peor respuesta vacunal + mas infeccion/cancer en el anciano"),
},
"06 - Congenito": {
 "Pulmon / Respiratorio": ("<b>Fibrosis quistica</b> · <b>deficit a1-antitripsina</b> · CPAM · secuestro · Kartagener · hernia diafragmatica", "FQ: cloro en sudor; enfisema joven no fumador = a1-AT"),
 "Corazon": ("<b>Acianoticas</b>: CIV, CIA, PCA, coartacion · <b>Cianoticas</b>: Tetralogia de Fallot, transposicion · bicuspide · QT largo · MCH", "soplo neonatal; cianosis vs no; SatO2 pre/postductal"),
 "Higado / Biliar / Pancreas": ("<b>Atresia biliar</b> · quiste de coledoco · <b>Gilbert</b> · Crigler-Najjar · <b>Wilson</b> · <b>hemocromatosis</b>", "bilirrubina indirecta aislada = Gilbert; Cu/ferritina"),
 "Intestino": ("<b>Hirschsprung</b> · atresias · malrotacion/volvulo · <b>estenosis pilorica</b> · <b>Meckel</b> · ano imperforado · PAF", "no expulsa meconio; vomito en proyectil; regla del 2"),
 "Rinon / Urinario": ("<b>Poliquistosis renal</b> · rinon en herradura · agenesia · <b>reflujo vesicoureteral</b> · valvulas uretrales posteriores · Alport", "masas en flancos + HTA; ITU de repeticion"),
 "Cerebro / SNC": ("<b>Defectos del tubo neural</b> · hidrocefalia · <b>paralisis cerebral</b> · <b>facomatosis</b> (NF, esclerosis tuberosa) · trisomia 21 · fenilcetonuria", "acido folico; manchas cafe con leche; tamiz metabolico"),
 "Ojo": ("<b>Retinoblastoma</b> (leucocoria) · catarata/<b>glaucoma congenito</b> · retinopatia del prematuro · aniridia · albinismo", "reflejo blanco pupilar = urgencia oncologica"),
 "Oido": ("<b>Hipoacusia congenita</b> (conexina 26, Pendred, Usher) · microtia/atresia · sordera por <b>TORCH (CMV)</b>", "tamiz auditivo neonatal"),
 "Endocrino / Suprarrenal": ("<b>Hipotiroidismo congenito</b> · <b>hiperplasia suprarrenal congenita</b> (21-OH) · MODY/diabetes neonatal · Kallmann", "tamiz neonatal; genitales ambiguos + hiponatremia"),
 "Ap. reproductor femenino": ("<b>Turner</b> (45,X) · malformaciones mullerianas (Rokitansky) · himen imperforado · insensibilidad a androgenos", "amenorrea primaria + cuello alado"),
 "Ap. reproductor masculino": ("<b>Criptorquidia</b> · <b>hipospadias</b> · <b>Klinefelter</b> (47,XXY) · deformidad badajo de campana", "testiculo no palpable; talla alta + testes pequenos"),
 "Cabeza / Craneofacial": ("<b>Labio/paladar hendido</b> · <b>craneosinostosis</b> · Pierre Robin · Crouzon/Apert/Treacher Collins · encefalocele", "craneo deforme; dificultad para alimentarse"),
 "Musculoesqueletico": ("<b>Displasia de cadera</b> · <b>pie equinovaro</b> · <b>osteogenesis imperfecta</b> · acondroplasia · <b>Duchenne</b> · Marfan", "Ortolani/Barlow; escleras azules; Gowers"),
 "Piel": ("<b>Epidermolisis bullosa</b> · ictiosis · <b>manchas cafe con leche</b> (NF1) · nevus congenito · albinismo · xeroderma pigmentoso", "ampollas al roce; &ge;6 manchas = facomatosis"),
 "Sangre / Hematologico": ("<b>Hemofilia A/B</b> · <b>von Willebrand</b> · <b>talasemias</b> · <b>drepanocitosis</b> · esferocitosis · <b>deficit G6PD</b>", "hemartrosis; crisis vasooclusivas; hemolisis con farmaco/habas"),
 "Nariz / Garganta / Cuello": ("<b>Atresia de coanas</b> · <b>quiste tirogloso/branquial</b> · <b>laringomalacia</b> · higroma quistico · fistula traqueoesofagica", "cianosis al mamar que mejora al llorar; estridor que mejora prono"),
 "Boca / Dental": ("<b>Paladar hendido</b> · amelogenesis/dentinogenesis imperfecta · <b>anquiloglosia</b> · hipodoncia · perlas de Epstein", "dificultad de succion; lengua anclada"),
 "Vascular periferico": ("<b>Malformaciones AV/linfaticas</b> · <b>telangiectasia hemorragica hereditaria</b> (Rendu-Osler) · <b>Marfan/Ehlers-Danlos</b> · linfedema (Milroy)", "epistaxis recurrente + telangiectasias; habito marfanoide"),
 "Inmune": ("<b>Inmunodeficiencias primarias</b>: SCID, Bruton, deficit IgA, <b>DiGeorge</b> (22q11), EGC, <b>angioedema hereditario</b>", "infecciones graves desde la lactancia; tetania + cardiopatia (DiGeorge)"),
},
"07 - Traumatico": {
 "Pulmon / Respiratorio": ("<b>Neumotorax a tension</b> · <b>hemotorax masivo</b> · contusion pulmonar · <b>torax inestable</b> · fractura costal", "dx clinico &rarr; descomprimir; &gt;1500 mL sonda &rarr; toracotomia"),
 "Corazon": ("<b>Tamponade</b> (penetrante) · contusion miocardica · <b>ruptura aortica</b> (desaceleracion)", "triada de Beck; mediastino ancho"),
 "Higado / Biliar / Pancreas": ("<b>Laceracion/ruptura hepatica</b> · hematoma subcapsular", "2o organo mas lesionado en cerrado; FAST +"),
 "Intestino": ("<b>Lesion esplenica</b> (Kehr) · perforacion de viscera hueca · lesion duodeno-pancreatica (cinturon) · hematoma mesenterico", "bazo = mas frecuente en cerrado; signo del cinturon"),
 "Rinon / Urinario": ("Trauma renal (<b>hematuria</b>) · <b>ruptura vesical</b> · <b>lesion uretral</b>", "fractura pelvica + sangre en meato = NO sondar"),
 "Cerebro / SNC": ("<b>Hematoma epidural</b> (intervalo lucido) · <b>subdural</b> (anciano/ACO) · HSA traumatica · LAD · contusion", "epidural lenticular vs subdural en semiluna"),
 "Ojo": ("<b>Fractura orbitaria (blowout)</b> · <b>ruptura del globo</b> · <b>hifema</b> · abrasion corneal · quemadura quimica", "diplopia + enoftalmos; quemadura quimica = irrigar YA"),
 "Oido": ("<b>Perforacion timpanica</b> · <b>fractura de temporal</b> · hematoma auricular (coliflor) · otolicuorrea", "otorragia + Battle = fractura base de craneo"),
 "Endocrino / Suprarrenal": ("<b>Diabetes insipida postraumatica</b> (TCE) · hipopituitarismo postraumatico · hemorragia suprarrenal", "poliuria tras TCE; hipotension refractaria"),
 "Ap. reproductor femenino": ("<b>Ruptura uterina</b> · desgarros perineales · trauma genital/sexual · trauma mamario", "obstetrico; valoracion forense"),
 "Ap. reproductor masculino": ("<b>Fractura de pene</b> (chasquido en coito) · <b>ruptura testicular</b> · trauma uretral", "berenjena + deformidad; eco testicular"),
 "Cabeza / Craneofacial": ("Fracturas <b>Le Fort I/II/III</b> · nasal · <b>mandibular</b> · cigomatica · base de craneo", "ojos de mapache + Battle; maloclusion"),
 "Musculoesqueletico": ("<b>Fracturas</b> · <b>luxaciones</b> · <b>sindrome compartimental</b> · <b>fractura de cadera</b> (anciano) · esguinces (LCA)", "6 P del compartimental; cadera acortada + rotada externa"),
 "Piel": ("<b>Quemaduras</b> (termica/quimica/electrica) · heridas (incisas/contusas/punzantes) · avulsiones · <b>mordeduras</b>", "regla de los 9; profundidad; profilaxis antirrabica"),
 "Sangre / Hematologico": ("<b>Choque hemorragico</b> (clases ATLS I-IV) · <b>coagulopatia del trauma</b> · CID", "clase III: FC&gt;120 + confuso; transfusion 1:1:1"),
 "Nariz / Garganta / Cuello": ("<b>Trauma penetrante de cuello</b> (zonas I-III) · <b>fractura laringea</b> · epistaxis · lesion vascular cervical", "no explorar a ciegas; via aerea primero"),
 "Boca / Dental": ("<b>Avulsion dental</b> · fractura mandibular · laceracion lengua/labio · <b>luxacion de ATM</b>", "reimplantar diente &lt;60 min (leche/saliva)"),
 "Vascular periferico": ("Hemorragia arterial · <b>sindrome compartimental</b> · <b>aplastamiento &rarr; rabdomiolisis</b> · pseudoaneurisma · fistula AV", "presion directa; CK alta + mioglobinuria"),
 "Inmune": ("<b>Tetanos</b> (herida sucia) · inmunosupresion postraumatica · infeccion de heridas", "profilaxis antitetanica segun herida y vacunacion"),
},
"08 - Autoinmune-Inflamatorio": {
 "Pulmon / Respiratorio": ("<b>Sarcoidosis</b> · vasculitis (<b>Wegener/GPA</b>, EGPA) · <b>Goodpasture</b> · EPID por conectivopatia", "adenopatias hiliares; ANCA; anti-MBG"),
 "Corazon": ("<b>Pericarditis lupica</b> · <b>fiebre reumatica</b> · miocarditis · <b>Dressler</b> · Libman-Sacks · Kawasaki", "frote; ASLO; derrame + conectivopatia"),
 "Higado / Biliar / Pancreas": ("<b>Hepatitis autoinmune</b> · <b>CBP</b> · <b>CEP</b> (asociada a CU)", "ASMA/anti-LKM; AMA+ = CBP; colangio en cuentas"),
 "Intestino": ("<b>EII</b> (Crohn vs CU) · <b>celiaquia</b> · colitis microscopica · gastritis autoinmune", "calprotectina; anti-transglutaminasa; ASCA/p-ANCA"),
 "Rinon / Urinario": ("<b>Nefritis lupica</b> · <b>GN</b> (IgA, membranosa, rapidamente progresiva) · <b>vasculitis ANCA</b> · Goodpasture", "sedimento nefritico; anti-dsDNA; ANCA"),
 "Cerebro / SNC": ("<b>Esclerosis multiple</b> · <b>miastenia gravis</b> · <b>Guillain-Barre</b> · encefalitis anti-NMDA · lupus neuropsiquiatrico", "brotes + bandas oligoclonales; fatigabilidad; debilidad ascendente"),
 "Ojo": ("<b>Uveitis</b> (HLA-B27, Behcet, sarcoide) · <b>escleritis</b> (AR) · <b>Sjogren</b> · orbitopatia de Graves · neuritis optica", "ojo rojo doloroso + fotofobia; Schirmer"),
 "Oido": ("<b>Policondritis recidivante</b> · hipoacusia autoinmune · GPA (oido medio)", "pabellon inflamado respetando lobulo"),
 "Endocrino / Suprarrenal": ("<b>Hashimoto</b> · <b>Graves</b> · <b>DM1</b> · <b>Addison autoinmune</b> · <b>sindromes poliglandulares</b> · tiroiditis posparto", "anti-TPO; TRAb; anti-GAD; anti-21-OH"),
 "Ap. reproductor femenino": ("<b>Sd. antifosfolipido</b> (abortos + trombosis) · insuficiencia ovarica autoinmune · <b>endometriosis</b> · lupus + embarazo", "anticardiolipina/anti-b2GP1; dismenorrea + dispareunia"),
 "Ap. reproductor masculino": ("<b>Orquitis autoinmune</b> · infertilidad por Ac antiespermatozoide · vasculitis testicular (PAN)", "rara; en contexto sistemico"),
 "Cabeza / Craneofacial": ("<b>Arteritis de celulas gigantes</b> · <b>Sjogren</b> · sialadenitis", "&gt;50a + cefalea temporal + claudicacion + VSG alta"),
 "Musculoesqueletico": ("<b>AR</b> · <b>LES</b> · <b>espondiloartropatias</b> (anquilosante, psoriasica, reactiva; HLA-B27) · <b>esclerodermia</b> · <b>poli/dermatomiositis</b> · PMR", "anti-CCP; ANA/anti-dsDNA; rigidez matutina &gt;1 h; Gottron"),
 "Piel": ("<b>Psoriasis</b> · <b>lupus cutaneo</b> · <b>dermatomiositis</b> · <b>penfigo/penfigoide</b> · vitiligo · vasculitis (purpura palpable)", "Nikolsky; placas con escama plateada"),
 "Sangre / Hematologico": ("<b>AHAI</b> (Coombs+) · <b>PTI</b> · PTT · <b>anemia perniciosa</b>", "Coombs+; plaquetas bajas aisladas; anti-FI"),
 "Nariz / Garganta / Cuello": ("<b>GPA/Wegener</b> (nariz en silla de montar) · policondritis · <b>tiroiditis</b> · Sjogren", "c-ANCA (PR3); destruccion del tabique"),
 "Boca / Dental": ("<b>Aftas recurrentes</b> (Behcet, EII, celiaquia) · <b>liquen plano oral</b> · penfigo · Sjogren", "aftas + ulceras genitales + uveitis = Behcet"),
 "Vascular periferico": ("<b>Vasculitis por tamano de vaso</b> (ACG/Takayasu; PAN/Kawasaki; ANCA/IgA) · <b>Buerger</b> · <b>Raynaud</b>", "purpura palpable; pulsos asimetricos; trifasico de color"),
 "Inmune": ("<b>LES</b> · <b>vasculitis sistemicas</b> · <b>sarcoidosis</b> · <b>Behcet</b> · enf. relacionada con IgG4 · Still", "ANA como tamiz; multisistemico + reactantes altos"),
},
"09 - Neoplasico": {
 "Pulmon / Respiratorio": ("<b>Ca de pulmon</b> (SCLC vs NSCLC) · <b>mesotelioma</b> (asbesto) · carcinoide · <b>metastasis</b> · Pancoast", "tabaco; SCLC = paraneoplasico (SIADH, Cushing); nodulo en TC"),
 "Corazon": ("<b>Mixoma</b> (auricula izq, primario mas frecuente) · rabdomioma (nino) · <b>metastasis</b>", "sincope posicional + soplo cambiante"),
 "Higado / Biliar / Pancreas": ("<b>Hepatocarcinoma</b> (sobre cirrosis) · colangiocarcinoma · <b>metastasis</b> · <b>Ca de pancreas</b>", "AFP alta + cirrosis; CA 19-9"),
 "Intestino": ("<b>Ca colorrectal</b> · <b>Ca gastrico</b> · Ca esofagico · GIST · linfoma MALT · carcinoide", "anemia ferropenica + cambio de habito; CEA; Virchow"),
 "Rinon / Urinario": ("<b>Ca de celulas renales</b> · <b>Ca de vejiga</b> (hematuria INDOLORA, tabaco) · <b>Wilms</b> (nino)", "hematuria indolora = urotelial hasta demostrar"),
 "Cerebro / SNC": ("<b>Metastasis</b> (pulmon/mama/melanoma) · <b>glioblastoma</b> · <b>meningioma</b> · meduloblastoma (nino) · adenoma hipofisario", "cefalea progresiva + foco + crisis nueva en adulto"),
 "Ojo": ("<b>Retinoblastoma</b> (nino, leucocoria) · <b>melanoma coroideo</b> (adulto) · metastasis · linfoma intraocular", "reflejo blanco pupilar = urgencia"),
 "Oido": ("<b>Schwannoma vestibular</b> (NF2) · <b>paraganglioma</b> (acufeno pulsatil) · Ca de CAE", "hipoacusia neurosensorial asimetrica &rarr; RM"),
 "Endocrino / Suprarrenal": ("<b>Ca de tiroides</b> (papilar; medular = MEN2) · <b>adenoma hipofisario</b> · <b>feocromocitoma</b> · insulinoma/gastrinoma · <b>MEN 1/2</b>", "nodulo tiroideo frio; hipersecrecion hormonal"),
 "Ap. reproductor femenino": ("<b>Ca de mama</b> · <b>Ca cervicouterino</b> (VPH) · <b>Ca de endometrio</b> · <b>Ca de ovario</b> · enf. trofoblastica", "BRCA; CA-125; mola = b-hCG muy alta"),
 "Ap. reproductor masculino": ("<b>Ca de prostata</b> (mayor, APE) · <b>Ca testicular</b> (joven, masa INDOLORA) · Ca de pene", "AFP/b-hCG/LDH; masa testicular dura no transilumina"),
 "Cabeza / Craneofacial": ("<b>Ca de cabeza y cuello</b> (escamoso: tabaco/alcohol/VPH) · tumor de <b>parotida</b> · <b>Ca nasofaringeo</b> (EBV)", "ulcera/masa que no cura; adenopatia cervical"),
 "Musculoesqueletico": ("<b>Metastasis oseas</b> (mama, prostata, pulmon, tiroides, rinon) · <b>mieloma multiple</b> · <b>osteosarcoma</b> (joven) · Ewing", "dolor oseo nocturno; CRAB; hipercalcemia"),
 "Piel": ("<b>Melanoma</b> (ABCDE) · <b>carcinoma basocelular</b> (mas frecuente) · <b>escamoso</b> · queratosis actinica · Kaposi (VIH)", "lesion que cambia/sangra/no cura; sol"),
 "Sangre / Hematologico": ("<b>Leucemias</b> (LLA nino, LMA adulto, LLC, LMC) · <b>linfomas</b> (Hodgkin/no Hodgkin) · <b>mieloma</b>", "blastos; sintomas B; pancitopenia; pico monoclonal"),
 "Nariz / Garganta / Cuello": ("<b>Ca laringeo</b> (disfonia &gt;3 sem, tabaco) · <b>nasofaringeo</b> (EBV) · <b>Ca tiroideo</b> · linfoma", "disfonia persistente = laringoscopia"),
 "Boca / Dental": ("<b>Ca escamoso oral</b> (lengua/piso de boca; tabaco+alcohol) · <b>eritroplasia/leucoplasia</b>", "ulcera indolora que no cura &gt;2 sem"),
 "Vascular periferico": ("<b>Sarcoma de Kaposi</b> · angiosarcoma · <b>Sd. de Trousseau</b> (&rarr; Ca oculto, pancreas)", "trombosis recurrente sin causa &rarr; buscar cancer"),
 "Inmune": ("<b>Linfomas</b> (adenopatia indolora + sintomas B) · <b>timoma</b> (+ miastenia) · neoplasias en inmunodeprimidos", "adenopatias firmes no dolorosas; masa mediastinica"),
},
"10 - Toxico-Farmacologico": {
 "Pulmon / Respiratorio": ("<b>Fibrosis</b> (amiodarona, bleomicina, metotrexato, nitrofurantoina) · <b>EVALI</b> (vapeo) · edema por opioides · neumoconiosis", "tabaco &rarr; EPOC/Ca; patron restrictivo nuevo + farmaco"),
 "Corazon": ("<b>Cocaina</b> &rarr; IAM/arritmia · <b>antraciclinas</b> · <b>QT largo</b> &rarr; torsade · <b>digoxina</b> · alcohol &rarr; MCD", "IAM en joven = cocaina; digoxina &rarr; Ac antidigital"),
 "Higado / Biliar / Pancreas": ("<b>Paracetamol</b> · <b>alcohol</b> · DILI (isoniazida, amoxi-clav, metotrexato) · Amanita", "paracetamol &rarr; N-acetilcisteina; AST/ALT en miles"),
 "Intestino": ("<b>AINE</b> &rarr; ulcera/HDA · <b>antibioticos</b> &rarr; C. difficile · <b>opioides</b> &rarr; ileo · causticos · plomo", "ATB reciente + diarrea = C. diff"),
 "Rinon / Urinario": ("<b>NTA</b> (aminoglucosidos, contraste, anfotericina, vancomicina) · <b>AINE</b> · <b>nefritis intersticial</b> · <b>litio</b> (DI nefrogenica)", "suspender nefrotoxico; FeNa &gt;2%"),
 "Cerebro / SNC": ("<b>Opioides</b> (miosis + depresion respiratoria) · <b>alcohol</b> (intox/abstinencia, Wernicke) · benzodiacepinas · <b>CO</b> · sd. serotoninergico/NMS", "opioide &rarr; naloxona; benzo &rarr; flumazenil; tiamina antes que glucosa"),
 "Ojo": ("<b>Metanol</b> (ceguera) · <b>etambutol</b> (neuritis optica) · <b>hidroxicloroquina</b> (retinopatia) · corticoides · digoxina (xantopsia)", "metanol &rarr; fomepizol/etanol; campimetria en antiTB"),
 "Oido": ("<b>Aminoglucosidos</b> · <b>furosemida</b> · <b>cisplatino</b> · <b>salicilatos</b> (acufeno reversible) · quinina", "acufeno + dosis alta AAS; hipoacusia tras aminoglucosido"),
 "Endocrino / Suprarrenal": ("<b>Corticoides</b> &rarr; Cushing iatrogeno + supresion suprarrenal · <b>amiodarona</b> &rarr; tiroides · <b>litio</b> · tiazidas", "no suspender esteroide cronico de golpe (crisis)"),
 "Ap. reproductor femenino": ("<b>Teratogenos</b> (warfarina, isotretinoina, IECA, valproato, alcohol) · <b>ACO</b> &rarr; trombosis · <b>tamoxifeno</b> &rarr; Ca endometrio", "categoria en embarazo; sangrado + tamoxifeno"),
 "Ap. reproductor masculino": ("<b>Disfuncion erectil</b> (betabloqueantes, tiazidas, ISRS, finasterida) · <b>ginecomastia</b> (espironolactona, cimetidina) · <b>anabolicos</b>", "revisar lista de farmacos en DE/ginecomastia"),
 "Cabeza / Craneofacial": ("<b>Cefalea por abuso de analgesicos</b> · <b>osteonecrosis mandibular</b> (bifosfonatos) · <b>hiperplasia gingival</b> (fenitoina, nifedipino)", "cefalea diaria + analgesicos &gt;15 d/mes"),
 "Musculoesqueletico": ("<b>Estatinas</b> &rarr; miopatia/rabdomiolisis · <b>corticoides</b> &rarr; osteoporosis + necrosis avascular · <b>fluoroquinolonas</b> &rarr; rotura tendinosa · diureticos &rarr; gota", "CK alta + estatina; dolor de cadera + esteroide"),
 "Piel": ("<b>Farmacodermia</b>: <b>SSJ/NET</b> (alopurinol, anticonvulsivantes, sulfas) · <b>DRESS</b> · fotosensibilidad (doxiciclina, tiazidas)", "Nikolsky + mucosas + farmaco nuevo = urgencia"),
 "Sangre / Hematologico": ("<b>Agranulocitosis</b> (antitiroideos, metamizol, clozapina) · <b>HIT</b> (heparina) · <b>mielosupresion</b> · hemolisis (G6PD + farmaco)", "fiebre + neutropenia tras farmaco; plaquetas bajas con heparina"),
 "Nariz / Garganta / Cuello": ("<b>Cocaina</b> &rarr; perforacion septal · <b>IECA</b> &rarr; angioedema + tos · rinitis medicamentosa", "angioedema de lengua/labios sin urticaria = bradicinina"),
 "Boca / Dental": ("<b>Hiperplasia gingival</b> (fenitoina, ciclosporina, calcioantagonistas) · <b>osteonecrosis mandibular</b> (bifosfonatos) · <b>xerostomia</b>", "encias crecidas + anticonvulsivante"),
 "Vascular periferico": ("<b>Trombosis</b> (ACO/estrogenos + tabaco) · <b>HIT</b> · <b>necrosis cutanea por warfarina</b> · vasoespasmo (ergotamina/cocaina)", "trombosis + heparina = sospechar HIT"),
 "Inmune": ("<b>Lupus inducido por farmacos</b> (hidralazina, procainamida, isoniazida) · inmunosupresion &rarr; oportunistas · <b>anafilaxia</b> (farmaco/contraste)", "anti-histona+; respeta rinon/SNC (a diferencia del LES)"),
},
}

EJE_NOMBRE = {
 "01 - Topografico": "Topografico", "02 - Vascular": "Vascular",
 "03 - Infeccioso": "Infeccioso", "04 - Metabolico-Endocrino": "Metabolico/Endocrino",
 "05 - Degenerativo": "Degenerativo", "06 - Congenito": "Congenito/Genetico",
 "07 - Traumatico": "Traumatico", "08 - Autoinmune-Inflamatorio": "Autoinmune/Inflamatorio",
 "09 - Neoplasico": "Neoplasico", "10 - Toxico-Farmacologico": "Toxico/Farmacologico",
}

BASE_TAGS = ["ejes_diagnosticos", "ecoe"]
decks = {}
for k, did in DECK_IDS.items():
    decks[k] = genanki.Deck(did, f"{PADRE}::Eje {k}")


def add(eje_key, system, back, extra_tags):
    eje_tag = "eje_" + eje_key.split(" - ")[0]
    nombre = EJE_NOMBRE[eje_key]
    front = f"Eje {eje_key.split(' - ')[0]} ({nombre}) &mdash; {system}: cuando falla, &iquest;en que pienso?"
    tags = BASE_TAGS + [eje_tag, SYS_TAG.get(system, "otro")] + extra_tags
    decks[eje_key].add_note(genanki.Note(model=model_qa, fields=[front, back], tags=tags))


# Eje 01: back = tabla de subsitios
for system, rows in EJE1.items():
    body = "".join(f"<tr><td>{s}</td><td>{d}</td><td>{p}</td></tr>" for s, d, p in rows)
    back = ("<table><tr><th>Sitio</th><th>Piensa en</th><th>Pista</th></tr>"
            + body + "</table>")
    add("01 - Topografico", system, back, ["topografico"])

# Ejes 02-10: back = diferencial + pista
for eje_key, mapping in EJES.items():
    for system, (dif, pista) in mapping.items():
        back = (f"<b>Cuando el problema es {EJE_NOMBRE[eje_key].lower()}, piensa en:</b><br>{dif}"
                f'<span class="disc">Pista: {pista}</span>')
        add(eje_key, system, back, [])

# Empaquetado
all_decks = list(decks.values())
out = os.path.join(OUTPUT_DIR, "Ejes_Diagnosticos_Adulto.apkg")
genanki.Package(all_decks).write_to_file(out)
total = sum(len(d.notes) for d in all_decks)
print(f"OK -> {out}")
for k in DECK_IDS:
    print(f"  Eje {k}: {len(decks[k].notes)} tarjetas")
print(f"TOTAL: {total}")
