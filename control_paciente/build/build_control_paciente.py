"""Generador del deck Anki "Control del Paciente Cronico" para ECOE.

UN SOLO deck (.apkg) con el padre "Control del Paciente Cronico Adulto"
y 4 subdecks por capa:

  Capa 1 - Estratificacion        (Cloze)  -> donde esta el paciente en el mapa
  Capa 2 - Metas y Monitoreo      (Cloze)  -> cifras objetivo + que laboratorio pedir
  Capa 3 - Manejo y Transiciones  (Cloze)  -> farmaco, dosis y QUE CAMBIA al cruzar franja
  Capa 4 - Casos Integradores     (Q&A)    -> paciente con varios ejes a la vez

Filosofia (estilo Musel): cada enfermedad = eje con franjas (estratos). El paciente
es un punto que se mueve. La tarjeta estrella es la MATRIZ DE TRANSICION: que cambia
en el manejo al subir de franja o sumar comorbilidad.

Guias base (verificadas 2026-05):
  ADA Standards of Care in Diabetes 2026 (Diabetes Care vol 49, Supl 1)
  AHA/ACC 2025 High Blood Pressure (umbral/meta 130/80 universal, ecuaciones PREVENT)
  AHA/ACC 2018 + ECDP 2022 colesterol
  KDIGO 2024 ERC (iSGLT2 eGFR>=20; finerenona eGFR>25 + UACR>=30 + K&lt;5.0)
  AASLD 2023 MASLD + actualizacion resmetirom 2024 (FIB-4 1.3 / 2.67)
  ATA 2016 hipertiroidismo + 2014 hipotiroidismo
  NCEP-ATP III (sindrome metabolico) + WHO (anemia) + USPSTF (tabaco/alcohol)
"""
import os
import genanki

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "output")
os.makedirs(OUTPUT_DIR, exist_ok=True)

MODEL_CLOZE_ID = 1607392319  # reusable (ids.json: cloze_estandar)
MODEL_QA_ID = 1607392320     # reusable (ids.json: qa_estandar)

# deck_ids nuevos, unicos (no colisionan con ids.json)
DECK_ID_C1 = 1928374650
DECK_ID_C2 = 1837465029
DECK_ID_C3 = 1746528390
DECK_ID_C4 = 1659302847

PADRE = "Control del Paciente Cronico Adulto"
DECK_NAME_C1 = f"{PADRE}::Capa 1 - Estratificacion"
DECK_NAME_C2 = f"{PADRE}::Capa 2 - Metas y Monitoreo"
DECK_NAME_C3 = f"{PADRE}::Capa 3 - Manejo y Transiciones"
DECK_NAME_C4 = f"{PADRE}::Capa 4 - Casos Integradores"

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
.meta { color: #0e7490; display: block; margin-top: 6px; }
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

BASE_TAGS = ["control_paciente", "ecoe"]


def cz(deck, text, extra, tags):
    deck.add_note(genanki.Note(model=model_cloze, fields=[text, extra], tags=BASE_TAGS + tags))


def qa(deck, front, back, tags):
    deck.add_note(genanki.Note(model=model_qa, fields=[front, back], tags=BASE_TAGS + tags))


C1 = ["capa1", "estratificacion"]
C2 = ["capa2", "metas_monitoreo"]
C3 = ["capa3", "manejo_transiciones"]
C4 = ["capa4", "integrador"]

# ============================================================
# SECCION 1 - SINDROME METABOLICO
# ============================================================
cz(deck_c1,
   "Sindrome metabolico (NCEP-ATP III): {{c1::>=3 de 5 criterios}} -> "
   "{{c2::perimetro abdominal >102 cm (H) / >88 cm (M)}}, {{c3::TG >=150 mg/dL}}, "
   "{{c4::HDL &lt;40 (H) / &lt;50 (M)}}, {{c5::PA >=130/85}}, {{c6::glucosa ayuno >=100 mg/dL}}",
   '<span class="contraste">Tener el criterio tambien si ya recibes tratamiento para ese componente '
   '(antihipertensivo, hipolipemiante, hipoglucemiante).</span>'
   '<span class="ecoe">ECOE: "Cumple criterios de sindrome metabolico; lo leo como marcador de alto riesgo CV y de DM2."</span>',
   C1 + ["sx_metabolico"])

cz(deck_c1,
   "El sindrome metabolico no es un diagnostico que se trate con un farmaco: es un "
   "{{c1::predictor de riesgo cardiovascular y de diabetes tipo 2}}; el manejo es "
   "{{c2::tratar cada componente por separado}} + {{c3::cambios intensivos de estilo de vida}}",
   '<span class="ecoe">ECOE: "No persigo el sindrome como entidad; ataco cada eje (PA, lipidos, glucosa, peso)."</span>',
   C1 + ["sx_metabolico"])

cz(deck_c2,
   "Sindrome metabolico - metas por componente: PA {{c1::&lt;130/80}}, TG {{c2::&lt;150}}, "
   "HDL {{c3::>40 H / >50 M}}, glucosa ayuno {{c4::&lt;100}}, perdida de peso {{c5::>=5-10%}}",
   '<span class="meta">Eje rector = riesgo CV global, no un solo numero.</span>',
   C2 + ["sx_metabolico"])

cz(deck_c2,
   "Seguimiento del paciente con sindrome metabolico: perfil de lipidos + glucosa/HbA1c "
   "{{c1::anual (o antes si fuera de meta)}}; vigilar progresion a {{c2::diabetes}} y "
   "{{c3::MASLD (higado graso metabolico)}}",
   '<span class="ecoe">ECOE: "Cribo anualmente glucemia y lipidos; busco activamente diabetes y esteatosis hepatica."</span>',
   C2 + ["sx_metabolico"])

# ============================================================
# SECCION 2 - PREDIABETES -> DM2
# ============================================================
cz(deck_c1,
   "Diagnostico de DM (ADA 2026): HbA1c {{c1::>=6.5%}}, glucosa en ayuno {{c2::>=126 mg/dL}}, "
   "OGTT 2h {{c3::>=200 mg/dL}}, o glucosa al azar {{c4::>=200 + sintomas clasicos}}",
   '<span class="redflag">Salvo hiperglucemia inequivoca, se requieren 2 pruebas anormales '
   '(2 distintas en la misma muestra o la misma prueba repetida).</span>',
   C1 + ["diabetes", "diagnostico"])

cz(deck_c1,
   "Prediabetes (ADA 2026): HbA1c {{c1::5.7-6.4%}}, glucosa ayuno (GAA) {{c2::100-125 mg/dL}}, "
   "OGTT 2h (ITG) {{c3::140-199 mg/dL}}",
   '<span class="contraste">Por encima de estos cortes ya es diabetes; por debajo, normal.</span>'
   '<span class="ecoe">ECOE: "Prediabetes = ventana de prevencion; intervengo agresivo en estilo de vida."</span>',
   C1 + ["prediabetes"])

cz(deck_c1,
   "Cribado de DM2 (USPSTF/ADA): adultos {{c1::35-70 anos con sobrepeso/obesidad}}; "
   "si normal, repetir cada {{c2::3 anos}}; si prediabetes, {{c3::anual}}",
   '<span class="ecoe">ECOE: "Tamizo diabetes desde los 35 anos en sobrepeso, antes si hay factores de riesgo."</span>',
   C1 + ["diabetes", "cribado"])

cz(deck_c2,
   "Meta de HbA1c (ADA 2026): mayoria de adultos no embarazadas {{c1::&lt;7%}}; "
   "mas estricta {{c2::&lt;6.5%}} si se logra sin hipoglucemia; mas laxa {{c3::&lt;8%}} en "
   "fragil / expectativa de vida limitada / riesgo alto de hipoglucemia",
   '<span class="meta">Glucosa preprandial 80-130 mg/dL; pico postprandial &lt;180 mg/dL.</span>'
   '<span class="ecoe">ECOE: "Individualizo la meta de HbA1c segun edad, fragilidad y riesgo de hipoglucemia."</span>',
   C2 + ["diabetes", "metas"])

cz(deck_c2,
   "Monitoreo en DM2: HbA1c cada {{c1::3 meses}} si fuera de meta o cambio de tratamiento, "
   "cada {{c2::6 meses}} si estable; anual {{c3::UACR + eGFR + perfil lipidico + fondo de ojo + pies}}",
   '<span class="ecoe">ECOE: "Cada visita reviso pies; cada ano cribo retinopatia, nefropatia y dislipidemia."</span>',
   C2 + ["diabetes", "monitoreo"])

cz(deck_c3,
   "Prediabetes - manejo: {{c1::cambios intensivos de estilo de vida (perdida 7% peso + actividad)}}; "
   "agregar {{c2::metformina}} si IMC {{c3::>=35}}, edad {{c4::&lt;60 anos}} o {{c5::diabetes gestacional previa}}",
   '<span class="ecoe">ECOE: "Prediabetes de alto riesgo: dieta, ejercicio y considero metformina."</span>',
   C3 + ["prediabetes"])

cz(deck_c3,
   "DM2 sin complicaciones - inicio: {{c1::metformina + estilo de vida}}; "
   "pero si hay ECV/IC/ERC establecidas se agrega {{c2::GLP-1 RA y/o iSGLT2}} "
   "{{c3::independiente de la HbA1c y de la metformina}}",
   '<span class="contraste">El motor de la eleccion ya no es "bajar glucosa" sino "proteger organo".</span>',
   C3 + ["diabetes", "inicio"])

# --- TARJETA ESTRELLA: matriz de transicion DM ---
cz(deck_c3,
   "<b>Matriz de transicion DM - como cambia el manejo al cruzar franja:</b><br>"
   "&bull; Prediabetico -> {{c1::estilo de vida +/- metformina}}<br>"
   "&bull; DM2 sin complicaciones -> {{c2::metformina; meta HbA1c &lt;7%}}<br>"
   "&bull; DM2 + ECV/IC -> {{c3::agregar GLP-1 RA (ateroesclerosis) y/o iSGLT2 (IC), sin importar HbA1c}}<br>"
   "&bull; DM2 + nefropatia (UACR>=30) -> {{c4::iSGLT2 (eGFR>=20) + IECA/ARA-II a dosis maxima + finerenona si eGFR>25 y K&lt;5.0}}",
   '<span class="redflag">El orden de prioridad migra de glucemia -> proteccion cardiorrenal a medida que aparece dano de organo.</span>'
   '<span class="ecoe">ECOE: "Ubico al paciente en la franja y elijo el farmaco por el organo que debo proteger, no solo por el azucar."</span>',
   C3 + ["diabetes", "matriz_transicion"])

# ============================================================
# SECCION 3 - DM2 CON HIPERTENSION
# ============================================================
cz(deck_c1,
   "En DM2 + HTA el umbral diagnostico de hipertension es el mismo: {{c1::>=130/80 mmHg}} "
   "(AHA/ACC 2025); la coexistencia multiplica el {{c2::riesgo cardiovascular y de nefropatia}}",
   '<span class="ecoe">ECOE: "Diabetico con PA >=130/80 ya es hipertenso; intervengo temprano por el riesgo sumado."</span>',
   C1 + ["dm_hta"])

cz(deck_c2,
   "Meta de PA en el diabetico (ADA 2026): {{c1::&lt;130/80}} en la mayoria; "
   "{{c2::&lt;120 sistolica}} si alto riesgo CV/renal y se tolera; mas laxa {{c3::&lt;140/90}} en "
   "mala salud / expectativa limitada",
   '<span class="contraste">ADA 2026 bajo la meta hacia &lt;120 en alto riesgo, acercandose a KDIGO.</span>',
   C2 + ["dm_hta", "metas"])

cz(deck_c2,
   "Tras iniciar IECA/ARA-II en diabetico, controlar {{c1::creatinina y potasio}} en "
   "{{c2::1-4 semanas}}; un alza de creatinina {{c3::&lt;=30%}} es aceptable y no obliga a suspender",
   '<span class="redflag">Suspender/revisar si creatinina sube >30% o hiperpotasemia.</span>',
   C2 + ["dm_hta", "monitoreo"])

cz(deck_c3,
   "DM2 + HTA - farmaco de eleccion: {{c1::IECA o ARA-II}}, sobre todo si hay {{c2::albuminuria}}; "
   "si no se alcanza meta, combinar con {{c3::calcioantagonista dihidropiridinico o tiazida tipo clortalidona}}",
   '<span class="ecoe">ECOE: "En diabetico con albuminuria elijo IECA/ARA-II por su efecto nefroprotector."</span>',
   C3 + ["dm_hta"])

cz(deck_c3,
   "Regla de seguridad en DM2 + HTA: {{c1::nunca combinar IECA + ARA-II}} (no se demostro "
   "beneficio y aumenta hiperpotasemia, IRA e hipotension)",
   '<span class="redflag">IECA + ARA juntos = mas dano renal, no menos.</span>',
   C3 + ["dm_hta", "seguridad"])

# ============================================================
# SECCION 4 - DM2 CON NEFROPATIA
# ============================================================
cz(deck_c1,
   "Nefropatia diabetica se define por {{c1::UACR >=30 mg/g persistente}} y/o "
   "{{c2::eGFR &lt;60 mL/min/1.73m2}} durante {{c3::>=3 meses}}, atribuibles a la diabetes",
   '<span class="ecoe">ECOE: "Confirmo dano renal con dos UACR alterados en 3-6 meses, no con uno aislado."</span>',
   C1 + ["dm_nefropatia"])

cz(deck_c1,
   "Categorias de albuminuria (KDIGO): A1 {{c1::&lt;30 mg/g (normal-leve)}}, "
   "A2 {{c2::30-300 (moderada)}}, A3 {{c3::>300 (severa)}}",
   '<span class="contraste">"Microalbuminuria/macroalbuminuria" son terminos antiguos; ahora se usan A1-A3.</span>',
   C1 + ["dm_nefropatia", "albuminuria"])

cz(deck_c2,
   "Metas en nefropatia diabetica: reducir UACR {{c1::>=30%}}, PA {{c2::&lt;130/80 (o &lt;120 sist. si tolera)}}, "
   "HbA1c {{c3::individualizada ~&lt;7%}}; vigilar K+ tras IECA/ARA y finerenona",
   '<span class="meta">La reduccion de albuminuria es marcador de nefroproteccion exitosa.</span>',
   C2 + ["dm_nefropatia", "metas"])

cz(deck_c2,
   "Cribado de nefropatia en DM2: {{c1::UACR + eGFR anuales desde el diagnostico}}; "
   "si hay ERC, monitoreo {{c2::1-4 veces al ano segun categoria de riesgo KDIGO}}",
   '<span class="ecoe">ECOE: "En DM2 tamizo nefropatia desde el dia del diagnostico, no a los 5 anos (eso es DM1)."</span>',
   C2 + ["dm_nefropatia", "cribado"])

cz(deck_c3,
   "Pilar 1 de nefroproteccion: {{c1::IECA o ARA-II}} titulado a {{c2::dosis maxima tolerada}} "
   "cuando hay albuminuria o ERC (reduce progresion y eventos CV)",
   '<span class="ecoe">ECOE: "Subo el IECA/ARA a la dosis maxima tolerada para frenar la albuminuria."</span>',
   C3 + ["dm_nefropatia"])

cz(deck_c3,
   "Pilar 2: {{c1::iSGLT2 (dapagliflozina/empagliflozina)}} si eGFR {{c2::>=20 mL/min}} "
   "(reno y cardioproteccion, con o sin buen control glucemico)",
   '<span class="contraste">Se inicia con eGFR>=20 y se mantiene aunque luego baje; se suspende solo en dialisis.</span>',
   C3 + ["dm_nefropatia"])

cz(deck_c3,
   "Pilar 3: {{c1::finerenona}} (ARM no esteroideo) si eGFR {{c2::>25}}, UACR {{c3::>=30}}, "
   "potasio {{c4::&lt;5.0}}, ya con IECA/ARA + iSGLT2; vigilar {{c5::potasio}}",
   '<span class="redflag">Contraindicada si hiperpotasemia; controlar K+ tras iniciar y al subir dosis.</span>'
   '<span class="ecoe">ECOE: "Agrego finerenona como tercer pilar si persiste albuminuria y el potasio lo permite."</span>',
   C3 + ["dm_nefropatia", "finerenona"])

# ============================================================
# SECCION 5 - HIPERTENSION
# ============================================================
cz(deck_c1,
   "Categorias de PA (AHA/ACC 2025): normal {{c1::&lt;120/80}}, elevada {{c2::120-129 / &lt;80}}, "
   "estadio 1 {{c3::130-139 o 80-89}}, estadio 2 {{c4::>=140 o >=90}}",
   '<span class="contraste">El riesgo se estratifica con las ecuaciones PREVENT (reemplazan a las pooled cohort).</span>',
   C1 + ["hta", "estadios"])

cz(deck_c1,
   "Crisis hipertensiva = PA {{c1::>=180/120}}; distinguir {{c2::emergencia (con dano agudo de organo: "
   "encefalopatia, EAP, SCA, diseccion, eclampsia, ictus)}} de {{c3::urgencia (sin dano agudo)}}",
   '<span class="redflag">Lo que define emergencia NO es la cifra, es el dano de organo blanco.</span>',
   C1 + ["hta", "crisis"])

cz(deck_c2,
   "Meta de PA (AHA/ACC 2025): {{c1::&lt;130/80 mmHg universal}}, con excepciones individualizadas "
   "(institucionalizados, expectativa de vida limitada, embarazo)",
   '<span class="meta">Medir con tecnica estandarizada y confirmar con monitoreo domiciliario/MAPA.</span>'
   '<span class="ecoe">ECOE: "Mi meta general es &lt;130/80; confirmo el diagnostico fuera del consultorio."</span>',
   C2 + ["hta", "metas"])

cz(deck_c2,
   "Cuando iniciar farmaco (AHA/ACC 2025): PA {{c1::>=140/90}} en todos; o {{c2::>=130/80}} si "
   "hay ECV establecida, DM, ERC o riesgo PREVENT {{c3::>=7.5%}}; si riesgo bajo, probar "
   "{{c4::3-6 meses de estilo de vida}} primero",
   '<span class="ecoe">ECOE: "Decido farmaco por cifra + riesgo global, no solo por el numero."</span>',
   C2 + ["hta", "inicio"])

cz(deck_c3,
   "HTA - primera linea (cualquiera de): {{c1::tiazida (clortalidona/indapamida)}}, "
   "{{c2::calcioantagonista (amlodipino)}}, {{c3::IECA o ARA-II}}; "
   "betabloqueante {{c4::no es primera linea salvo indicacion (IC, post-IAM, FA)}}",
   '<span class="contraste">DM/ERC con albuminuria -> preferir IECA/ARA; afrodescendiente sin ERC -> tiazida o CCB.</span>',
   C3 + ["hta", "farmacos"])

cz(deck_c3,
   "Si la PA esta {{c1::>=20/10 mmHg por encima de la meta}}, iniciar de entrada con "
   "{{c2::dos farmacos}} (idealmente combinacion en un solo comprimido)",
   '<span class="ecoe">ECOE: "Con PA muy por encima de meta arranco con terapia combinada, no monoterapia."</span>',
   C3 + ["hta", "combinacion"])

cz(deck_c3,
   "Emergencia hipertensiva: {{c1::antihipertensivo IV en monitoreo}}; reducir PA "
   "{{c2::&lt;=25% en la primera hora}}, luego gradual",
   '<span class="redflag">Excepciones: diseccion aortica (PAS &lt;120 rapido) e ictus isquemico (umbrales propios).</span>'
   '<span class="ecoe">ECOE: "En emergencia bajo la PA de forma controlada, no la normalizo de golpe."</span>',
   C3 + ["hta", "emergencia"])

# ============================================================
# SECCION 6 - DISLIPIDEMIA / RIESGO CV
# ============================================================
cz(deck_c1,
   "Intensidad de estatina: alta = {{c1::atorvastatina 40-80 / rosuvastatina 20-40}} (LDL -{{c2::>=50%}}); "
   "moderada = {{c3::atorva 10-20 / rosuva 5-10 / simva 20-40}} (LDL -{{c4::30-49%}})",
   '<span class="ecoe">ECOE: "Elijo intensidad de estatina por el porcentaje de reduccion de LDL que necesito."</span>',
   C1 + ["dislipidemia", "estatinas"])

cz(deck_c1,
   "Grupos de beneficio de estatina (AHA/ACC): {{c1::ECV ateroesclerotica clinica}}, "
   "{{c2::LDL >=190}}, {{c3::DM 40-75 anos}}, y {{c4::riesgo estimado elevado (PREVENT/pooled)}}",
   '<span class="contraste">En prevencion primaria el riesgo a 10 anos guia la decision e intensidad.</span>',
   C1 + ["dislipidemia", "grupos"])

cz(deck_c2,
   "Metas de LDL: ECV clinica {{c1::&lt;70 mg/dL}}; muy alto riesgo {{c2::&lt;55 mg/dL}}; "
   "en DM se busca reduccion {{c3::>=50%}} respecto al basal",
   '<span class="meta">Umbral para anadir ezetimiba/PCSK9 en prevencion secundaria: LDL persistente >=70.</span>',
   C2 + ["dislipidemia", "metas"])

cz(deck_c2,
   "Monitoreo de lipidos: perfil a las {{c1::4-12 semanas}} de iniciar/ajustar estatina, "
   "luego cada {{c2::3-12 meses}}; medir CK/transaminasas {{c3::solo si hay sintomas}}, no de rutina",
   '<span class="ecoe">ECOE: "Compruebo adherencia y respuesta con un perfil a las 4-12 semanas."</span>',
   C2 + ["dislipidemia", "monitoreo"])

cz(deck_c3,
   "Prevencion secundaria (ECV establecida): {{c1::estatina de alta intensidad}}; "
   "si LDL sigue {{c2::>=70}}, agregar {{c3::ezetimiba}} y luego {{c4::iPCSK9}} si persiste",
   '<span class="ecoe">ECOE: "Tras un evento CV escalono: estatina alta -> ezetimiba -> iPCSK9 hasta meta."</span>',
   C3 + ["dislipidemia"])

cz(deck_c3,
   "DM 40-75 anos sin ECV: al menos {{c1::estatina de intensidad moderada}}; "
   "subir a {{c2::alta intensidad}} si multiples factores de riesgo o riesgo a 10 anos alto",
   '<span class="contraste">DM >=75 anos: razonable estatina moderada, revaluando riesgo-beneficio.</span>',
   C3 + ["dislipidemia", "diabetes"])

cz(deck_c3,
   "Hipertrigliceridemia severa {{c1::>=500 mg/dL}} -> riesgo de {{c2::pancreatitis}}; "
   "tratar con {{c3::fibrato +/- icosapent de etilo}} y control de causas (alcohol, glucemia)",
   '<span class="redflag">Por encima de 500 el objetivo cambia: prevenir pancreatitis, no solo riesgo CV.</span>',
   C3 + ["dislipidemia", "trigliceridos"])

# ============================================================
# SECCION 7 - ERC (KDIGO)
# ============================================================
cz(deck_c1,
   "Categorias de eGFR (KDIGO): G1 {{c1::>=90}}, G2 {{c2::60-89}}, G3a {{c3::45-59}}, "
   "G3b {{c4::30-44}}, G4 {{c5::15-29}}, G5 {{c6::&lt;15 (falla renal)}}",
   '<span class="contraste">G1-G2 solo son ERC si hay marcador de dano (p.ej. albuminuria); el filtrado solo no basta.</span>',
   C1 + ["erc", "categorias"])

cz(deck_c1,
   "ERC se clasifica por causa + {{c1::categoria G (filtrado)}} + {{c2::categoria A (albuminuria)}}; "
   "el mapa de calor KDIGO combina ambas para estimar {{c3::riesgo de progresion y eventos}}",
   '<span class="ecoe">ECOE: "Defino la ERC con el binomio G y A, no solo con la creatinina."</span>',
   C1 + ["erc", "clasificacion"])

cz(deck_c2,
   "ERC - metas: PA {{c1::&lt;120 sistolica (KDIGO, medida estandarizada)}}; "
   "estatina en {{c2::todo paciente >=50 anos no en dialisis}}; "
   "objetivo transversal = {{c3::frenar la progresion (reducir albuminuria)}}",
   '<span class="contraste">KDIGO empuja a &lt;120 sist.; ADA/AHA general &lt;130/80 -> conflicto a verbalizar.</span>',
   C2 + ["erc", "metas"])

cz(deck_c3,
   "Nefroproteccion en ERC (con o sin DM): {{c1::IECA/ARA-II}} si hay albuminuria + "
   "{{c2::iSGLT2 si eGFR >=20}}; control de PA y de la causa de base",
   '<span class="ecoe">ECOE: "iSGLT2 ya no es solo del diabetico; protege el rinon proteinurico aunque no haya DM."</span>',
   C3 + ["erc"])

cz(deck_c3,
   "Referir a nefrologia si: eGFR {{c1::&lt;30}}, UACR {{c2::>300}}, "
   "{{c3::progresion rapida / causa no clara / hiperpotasemia refractaria}}",
   '<span class="ecoe">ECOE: "Derivo a nefrologia con eGFR&lt;30, albuminuria severa o deterioro acelerado."</span>',
   C3 + ["erc", "referencia"])

# ============================================================
# SECCION 8 - MASLD / HIGADO GRASO - ALCOHOL
# ============================================================
cz(deck_c1,
   "MASLD (esteatosis hepatica metabolica) = {{c1::esteatosis por imagen/biopsia}} + "
   "{{c2::>=1 factor de riesgo cardiometabolico}} (sobrepeso, DM/prediabetes, HTA, dislipidemia)",
   '<span class="contraste">MASLD reemplaza a "NAFLD"; MASH (antes NASH) = esteatohepatitis con inflamacion.</span>',
   C1 + ["masld"])

cz(deck_c1,
   "Patron de transaminasas: AST/ALT {{c1::>2}} + GGT alta -> sugiere {{c2::hepatopatia alcoholica}}; "
   "AST/ALT {{c3::&lt;1}} con ALT levemente alta en obeso/DM -> {{c4::MASLD}}",
   '<span class="ecoe">ECOE: "El cociente AST/ALT y la GGT me orientan entre alcohol y origen metabolico."</span>',
   C1 + ["masld", "alcohol"])

cz(deck_c2,
   "FIB-4 estratifica riesgo de fibrosis avanzada: {{c1::&lt;1.3 = bajo}}, "
   "{{c2::1.3-2.67 = indeterminado}}, {{c3::>2.67 = alto}}",
   '<span class="meta">FIB-4 usa edad, AST, ALT y plaquetas; es el primer filtro no invasivo.</span>',
   C2 + ["masld", "fib4"])

cz(deck_c2,
   "Si FIB-4 es indeterminado o alto -> siguiente paso {{c1::elastografia (VCTE/FibroScan) o ELF}}; "
   "bajo riesgo (&lt;1.3) -> {{c2::reevaluar en 1-3 anos}} controlando factores metabolicos",
   '<span class="ecoe">ECOE: "Escalono no invasivo: FIB-4 primero, elastografia si sale dudoso o alto."</span>',
   C2 + ["masld", "monitoreo"])

cz(deck_c3,
   "MASLD - base del manejo: {{c1::perdida de peso >=7-10%}} (revierte esteatosis y mejora fibrosis) + "
   "control de DM/lipidos; utiles {{c2::GLP-1 RA (semaglutida) y pioglitazona}} si DM2/MASH",
   '<span class="ecoe">ECOE: "El pilar es perder >=10% de peso; ahi reside la mejora de la fibrosis."</span>',
   C3 + ["masld"])

cz(deck_c3,
   "MASH con fibrosis {{c1::F2-F3}} (no cirrotica) -> farmaco especifico aprobado = "
   "{{c2::resmetirom}} + dieta/ejercicio; en hepatopatia alcoholica el pilar es {{c3::abstinencia total}}",
   '<span class="redflag">Resmetirom NO se usa en cirrosis (F4) descompensada.</span>',
   C3 + ["masld", "resmetirom"])

# ============================================================
# SECCION 9 - TIROIDES (HIPER + HIPO)
# ============================================================
cz(deck_c1,
   "Hipertiroidismo: {{c1::TSH baja}} + {{c2::T4 libre y/o T3 elevadas}}; "
   "subclinico = {{c3::TSH baja con T4/T3 normales}}",
   '<span class="ecoe">ECOE: "Confirmo tirotoxicosis con TSH suprimida y hormonas libres altas."</span>',
   C1 + ["tiroides", "hiper"])

cz(deck_c1,
   "Hipotiroidismo primario: {{c1::TSH alta}} + {{c2::T4 libre baja}}; "
   "subclinico = {{c3::TSH alta con T4 libre normal}}",
   '<span class="contraste">Causa mas frecuente: tiroiditis de Hashimoto (anti-TPO +).</span>',
   C1 + ["tiroides", "hipo"])

cz(deck_c2,
   "Meta en hipotiroidismo tratado: {{c1::TSH dentro del rango normal}} (en jovenes ~1-2.5); "
   "reajustar y medir TSH cada {{c2::6-8 semanas}} tras cambio de dosis, luego {{c3::anual}}",
   '<span class="meta">En >65-70 anos se acepta una TSH algo mas alta para evitar sobretratamiento.</span>',
   C2 + ["tiroides", "hipo", "metas"])

cz(deck_c2,
   "Cuando tratar subclinicos: hipotiroidismo subclinico si {{c1::TSH >=10}} (o sintomas/embarazo/anti-TPO+); "
   "hipertiroidismo subclinico si {{c2::TSH &lt;0.1}} + edad >65 / cardiopatia / osteoporosis",
   '<span class="ecoe">ECOE: "No todo subclinico se trata; decido por la cifra de TSH y el riesgo del paciente."</span>',
   C2 + ["tiroides", "subclinico"])

cz(deck_c3,
   "Hipertiroidismo por Graves: {{c1::metimazol (1a linea)}}; usar {{c2::propiltiouracilo}} en "
   "{{c3::1er trimestre de embarazo y tormenta tiroidea}}; alternativas {{c4::yodo radiactivo o cirugia}}; "
   "{{c5::betabloqueante}} para sintomas adrenergicos",
   '<span class="redflag">Metimazol: vigilar agranulocitosis y hepatotoxicidad.</span>'
   '<span class="ecoe">ECOE: "Inicio metimazol + betabloqueo sintomatico; PTU solo en 1er trimestre o tormenta."</span>',
   C3 + ["tiroides", "hiper"])

cz(deck_c3,
   "Hipotiroidismo - tratamiento: {{c1::levotiroxina}} a dosis plena {{c2::~1.6 ug/kg/dia}}; "
   "en anciano o cardiopata iniciar bajo {{c3::12.5-25 ug/dia}} y titular",
   '<span class="ecoe">ECOE: "Tomar en ayunas, 30-60 min antes del desayuno, separada de calcio/hierro."</span>',
   C3 + ["tiroides", "hipo"])

# ============================================================
# SECCION 10 - TABACO / ALCOHOL / PESO
# ============================================================
cz(deck_c1,
   "Cuantificacion de habitos: tabaco en {{c1::paquetes-ano (cajetillas/dia x anos fumando)}}; "
   "alcohol con {{c2::AUDIT-C o CAGE}}; peso con {{c3::IMC + perimetro abdominal}}",
   '<span class="ecoe">ECOE: "Cuantifico siempre: paquetes-ano, AUDIT-C e IMC/perimetro."</span>',
   C1 + ["habitos"])

cz(deck_c2,
   "Cese de tabaco: {{c1::consejo breve + farmacoterapia}}; opciones de 1a linea "
   "{{c2::vareniclina, bupropion, terapia de reemplazo de nicotina}}; objetivo = {{c3::abstinencia total}}",
   '<span class="ecoe">ECOE: "Ofrezco consejo estructurado (5 A) + vareniclina o TRN en cada visita."</span>',
   C2 + ["habitos", "tabaco"])

cz(deck_c2,
   "Sobrepeso/obesidad - meta inicial {{c1::perdida >=5-10% del peso}}; "
   "farmacos {{c2::GLP-1/GIP (semaglutida, tirzepatida)}}; cirugia bariatrica si "
   "{{c3::IMC >=40, o >=35 con comorbilidad}}",
   '<span class="meta">Una perdida del 5-10% ya mejora glucemia, PA, lipidos y esteatosis.</span>',
   C2 + ["habitos", "peso"])

cz(deck_c2,
   "Alcohol: limites de bajo riesgo {{c1::&lt;=2 bebidas/dia (H) y &lt;=1 (M)}}; "
   "AUDIT-C positivo -> {{c2::intervencion breve}}; dependencia -> {{c3::naltrexona/acamprosato + apoyo}}",
   '<span class="ecoe">ECOE: "Tamizo con AUDIT-C; consejo breve si positivo y farmaco si hay dependencia."</span>',
   C2 + ["habitos", "alcohol"])

# ============================================================
# SECCION 11 - ANEMIA
# ============================================================
cz(deck_c1,
   "Anemia (OMS): Hb {{c1::&lt;13 g/dL en hombre}}, {{c2::&lt;12 en mujer no embarazada}}; "
   "primer paso de clasificacion = {{c3::el VCM}}",
   '<span class="ecoe">ECOE: "Confirmo anemia por umbral de Hb y la clasifico por VCM."</span>',
   C1 + ["anemia"])

cz(deck_c1,
   "Anemia por VCM: {{c1::&lt;80 = microcitica (ferropenia, talasemia)}}; "
   "{{c2::80-100 = normocitica (enf. cronica, ERC, sangrado agudo)}}; "
   "{{c3::>100 = macrocitica (B12/folato, alcohol, hipotiroidismo)}}",
   '<span class="ecoe">ECOE: "El VCM divide la anemia en tres rutas diagnosticas."</span>',
   C1 + ["anemia", "vcm"])

cz(deck_c2,
   "Estudios de hierro: ferritina {{c1::&lt;30 ng/mL}} confirma ferropenia "
   "(o {{c2::&lt;100 si hay inflamacion/ERC}}); indice de saturacion de transferrina {{c3::&lt;20%}}",
   '<span class="meta">Ferritina es reactante de fase aguda: sube con inflamacion y enmascara deficit.</span>',
   C2 + ["anemia", "hierro"])

cz(deck_c2,
   "Anemia de la ERC: tratar hierro si {{c1::IST &lt;30% y ferritina &lt;500}}; "
   "iniciar eritropoyetina (ESA) cuando Hb {{c2::&lt;10 g/dL}} tras repletar hierro",
   '<span class="redflag">No sobrecorregir: meta de Hb ~10-11.5, evitar >=13 (mas eventos CV).</span>',
   C2 + ["anemia", "erc"])

cz(deck_c1,
   "Ferropenia confirmada en adulto -> obligatorio {{c1::buscar la causa, sobre todo sangrado digestivo oculto}} "
   "(considerar colonoscopia/endoscopia segun edad y contexto)",
   '<span class="redflag">Anemia ferropenica en varon o mujer posmenopausica = cancer GI hasta demostrar lo contrario.</span>',
   C1 + ["anemia", "ferropenia"])

# ============================================================
# SECCION 12 - PACIENTE INTEGRADO (Q&A)
# ============================================================
qa(deck_c4,
   "Diabetico + ERC G3b/A3 + PA 145/88 + LDL 120, ya con IECA. "
   "Da los 3 movimientos prioritarios y su porque.",
   "(1) <b>iSGLT2</b> (eGFR>=20): reno y cardioproteccion.<br>"
   "(2) <b>Estatina de alta intensidad</b>: DM + ERC = muy alto riesgo, meta LDL &lt;70.<br>"
   "(3) <b>Finerenona</b> si persiste albuminuria y K&lt;5.0, sobre IECA + iSGLT2.<br>"
   '<span class="contraste">Meta de PA: ADA/AHA &lt;130/80 vs KDIGO &lt;120 sist. -> verbalizar el matiz.</span>'
   '<span class="ecoe">ECOE: "Priorizo proteger el rinon y el corazon; la glucemia es secundaria aqui."</span>',
   C4 + ["integrador", "dm_nefropatia"])

qa(deck_c4,
   "Paciente con alto riesgo CV/renal. La PA esta en 128/78. "
   "Segun ADA 2026, que meta de PA persigues y como decides?",
   "Meta general &lt;130/80, pero ADA 2026 baja a <b>&lt;120 sistolica</b> en alto riesgo CV/renal "
   "si se tolera (alineado con KDIGO). Decido por riesgo, tolerancia y medicion estandarizada; "
   "vigilo hipotension, K+ y funcion renal.<br>"
   '<span class="ecoe">ECOE: "En alto riesgo busco &lt;120 sistolica si el paciente lo tolera, midiendo bien la PA."</span>',
   C4 + ["integrador", "hta", "metas"])

qa(deck_c4,
   "Prediabetico (HbA1c 6.1%) + sindrome metabolico + ALT alta con AST/ALT 0.8 + IMC 34. "
   "Plan integral.",
   "Lectura: prediabetes + MASLD probable. <br>"
   "(1) <b>Perdida de peso >=7-10%</b> (eje que mejora glucemia, lipidos, PA y esteatosis).<br>"
   "(2) <b>Metformina</b> por prediabetes de alto riesgo (IMC, edad).<br>"
   "(3) <b>FIB-4</b> para estratificar fibrosis hepatica; estatina segun riesgo CV.<br>"
   '<span class="ecoe">ECOE: "Un solo eje -el peso- mueve todos los demas; ahi concentro la intervencion."</span>',
   C4 + ["integrador", "masld", "prediabetes"])

qa(deck_c4,
   "Cronico complejo: HTA + DM2 + tabaco + alcohol + LDL alto + anemia leve. "
   "Cual es el eje rector y como ordenas el manejo?",
   "Eje rector = <b>riesgo cardiovascular global</b>. Orden: "
   "(1) estatina + control de PA con IECA/ARA + manejo de glucemia con organoproteccion; "
   "(2) cese de tabaco y alcohol (mayor impacto en mortalidad); "
   "(3) estudiar la anemia por VCM (descartar sangrado).<br>"
   '<span class="ecoe">ECOE: "El ECOE no quiere 10 diagnosticos, quiere que priorices el riesgo CV global."</span>',
   C4 + ["integrador", "riesgo_cv"])

qa(deck_c4,
   "Diabetico con Hb 10.8, VCM 78, ferritina 18. Como lo abordas?",
   "Anemia <b>microcitica ferropenica</b> (ferritina &lt;30). "
   "(1) Repletar hierro. (2) <b>Buscar la causa</b>: sangrado digestivo oculto -> valorar endoscopia/colonoscopia. "
   "(3) Recordar que la ERC diabetica tambien causa anemia (normocitica) -> revisar eGFR.<br>"
   '<span class="redflag">No quedarse en "doy hierro"; la ferropenia en adulto obliga a buscar sangrado.</span>',
   C4 + ["integrador", "anemia"])

qa(deck_c4,
   "Hipertiroidismo subclinico (TSH 0.05, T4/T3 normales) en mujer de 68 anos con fibrilacion auricular. "
   "Tratar o no?",
   "Si: hipertiroidismo subclinico con <b>TSH &lt;0.1</b> + edad >65 + FA es indicacion de tratamiento "
   "(riesgo de FA, eventos CV y osteoporosis). Estudiar causa (Graves, nodulo autonomo) y tratar "
   "(antitiroideo, yodo radiactivo) + control de la FA.<br>"
   '<span class="ecoe">ECOE: "TSH &lt;0.1 con FA y edad avanzada inclina claramente a tratar el subclinico."</span>',
   C4 + ["integrador", "tiroides"])

# ============================================================
# EMPAQUETADO - un solo .apkg con los 4 subdecks
# ============================================================
pkg = genanki.Package([deck_c1, deck_c2, deck_c3, deck_c4])
out = os.path.join(OUTPUT_DIR, "Control_Paciente_Cronico_Adulto.apkg")
pkg.write_to_file(out)

total = sum(len(d.notes) for d in (deck_c1, deck_c2, deck_c3, deck_c4))
print(f"OK -> {out}")
print(f"Capa 1: {len(deck_c1.notes)} | Capa 2: {len(deck_c2.notes)} | "
      f"Capa 3: {len(deck_c3.notes)} | Capa 4: {len(deck_c4.notes)} | TOTAL: {total}")
