# -*- coding: utf-8 -*-
"""Deck 4 — Estudios Básicos a interpretar (transversal ECOE).

Formato Q&A con FLIP pedagógico:
- Front: QUÉ reportas (valores normales + anormalidades principales).
- Back: QUÉ ORIENTA cada anormalidad + notas por estación + tip ECOE +
  penalización + fuente.

Cobertura (32 cards):
- 14 cards universales por estudio (BH, QS, EGO, PFH, GA, coag, ECGx2,
  RxTx x2, RxSPN, USG+Rx abd, FAST, β-hCG).
- 12 cards específicos por estación (HbA1c, lípidos, albuminuria, tiroides,
  marcadores cardio, pancreatitis, tamiz neonatal + BH ped, pre-psicofármaco,
  niveles séricos, prenatal, DG, USG obstétrico).
- 6 cards "cheat sheet" por estación: dx más comunes + estudio + parámetro
  disparador + criterio dx + siguiente paso.

Cross-link: tu repo ya tiene "Capa 3 - Interpretación de Estudios" para
MF, MI, Cx, GyO. Esto es el canon TRANSVERSAL básico, complementario.

Tags por sistema, estación y tipo → filtrar con Custom Study en Anki.

Guías: ADA 2025 + AHA/ACC 2018 lípidos + KDIGO 2024 + Atlanta revisada +
Ranson + BISAP + TG24 + Alvarado + ATA 2015 tiroides + IADPSG + ACOG +
USPSTF 2025 + AAP Bright Futures 2022 + CDC + UpToDate.
"""
import os
import genanki

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "output")
os.makedirs(OUTPUT_DIR, exist_ok=True)

MODEL_QA_ID = 1607392320
DECK_ID = 1736284091
DECK_NAME = "Preparación Verbalizada::Deck 4 - Estudios Básicos"

# ============================================================
# CSS
# ============================================================
CSS = """
.card {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  font-size: 16px; text-align: left; color: #1a1a1a;
  background-color: #fafafa; padding: 20px; line-height: 1.5;
}
.badge {
  display: inline-block; padding: 5px 14px; margin-bottom: 12px;
  color: #fff; border-radius: 6px;
  font-size: 12px; letter-spacing: 0.7px; font-weight: 700;
  text-transform: uppercase;
}
.tip-hema    { background: #7f1d1d; }
.tip-bioq    { background: #b45309; }
.tip-urina   { background: #65a30d; }
.tip-hepat   { background: #c2410c; }
.tip-acido   { background: #0e7490; }
.tip-coag    { background: #7e22ce; }
.tip-cardio  { background: #b91c1c; }
.tip-pulm    { background: #1d4ed8; }
.tip-orl     { background: #78350f; }
.tip-abdomen { background: #92400e; }
.tip-trauma  { background: #991b1b; }
.tip-gyo     { background: #db2777; }
.tip-endo    { background: #0d9488; }
.cs-mf       { background: #047857; }
.cs-mi       { background: #0e7490; }
.cs-cx       { background: #b91c1c; }
.cs-ped      { background: #c2410c; }
.cs-psiq     { background: #7e22ce; }
.cs-gyo      { background: #db2777; }

.titulo { font-size: 16px; font-weight: 700; color: #111;
          margin: 0 0 10px 0; }
.subt   { margin-top: 12px; font-weight: 700; font-size: 13px;
          letter-spacing: 0.5px; text-transform: uppercase;
          color: #374151; }
.vn { color: #1e40af; font-weight: 500;
      background: #eff6ff; border-left: 3px solid #2563eb;
      padding: 10px 14px; margin: 6px 0 10px 0; border-radius: 3px;
      white-space: pre-line; font-size: 15px; }
.anorm { color: #b91c1c; font-weight: 500;
         background: #fef2f2; border-left: 3px solid #dc2626;
         padding: 10px 14px; margin: 6px 0 0 0; border-radius: 3px;
         white-space: pre-line; font-size: 15px; }
ul.orienta { margin: 6px 0 0 0; padding-left: 22px; }
ul.orienta li { margin: 5px 0; font-size: 15px; }
.por-est { background: #fff7ed; border-left: 3px solid #f97316;
           padding: 10px 14px; margin: 10px 0; border-radius: 3px;
           font-size: 15px; }
.tip-ecoe { background: #ecfdf5; border-left: 3px solid #059669;
            padding: 8px 12px; margin: 10px 0; border-radius: 3px;
            font-size: 14px; }
.penaliza { background: #fef2f2; border-left: 3px solid #dc2626;
            padding: 8px 12px; margin: 10px 0; border-radius: 3px;
            font-size: 14px; }
.fuente { color: #6b7280; font-size: 12px; font-style: italic;
          margin-top: 10px; }
table.cs { width: 100%; border-collapse: collapse; margin: 6px 0;
           font-size: 14px; }
table.cs th { background: #1f2937; color: #fff; padding: 6px 8px;
              text-align: left; font-size: 12px; }
table.cs td { border-bottom: 1px solid #e5e7eb; padding: 6px 8px;
              vertical-align: top; }
table.cs tr:nth-child(even) td { background: #f9fafb; }
.dx { font-weight: 700; color: #b91c1c; }
.par { color: #1e40af; font-weight: 600; }
#extra { margin-top: 14px; border: none;
         border-top: 1px solid #d4d4d4; padding-top: 12px; }
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
    css=CSS,
)

deck = genanki.Deck(DECK_ID, DECK_NAME)
BASE_TAGS = ["estudios", "interpretacion", "ecoe", "preparacion_verbalizada"]


def make_card(badge_text, badge_class, titulo, valores_normales,
              anormalidades, orienta, por_estacion, ecoe_tip, penaliza,
              fuente, *extra_tags):
    """Card por estudio: front=valores+anormalidades, back=qué orienta."""
    front = (
        f'<div class="badge {badge_class}">{badge_text}</div>'
        f'<div class="titulo">{titulo}</div>'
        f'<div class="subt">Valores normales</div>'
        f'<div class="vn">{valores_normales}</div>'
        f'<div class="subt">Anormalidades a reportar</div>'
        f'<div class="anorm">{anormalidades}</div>'
    )
    orienta_html = "".join(f"<li>{o}</li>" for o in orienta)
    back = (
        f'<div class="subt">¿Qué orienta cada anormalidad?</div>'
        f'<ul class="orienta">{orienta_html}</ul>'
        f'<div class="por-est"><b>Por estación:</b> {por_estacion}</div>'
        f'<div class="tip-ecoe">🗣️ ECOE: {ecoe_tip}</div>'
        f'<div class="penaliza">⚠️ Penaliza si: {penaliza}</div>'
        f'<div class="fuente">📚 {fuente}</div>'
    )
    note = genanki.Note(
        model=model_qa,
        fields=[front, back],
        tags=BASE_TAGS + list(extra_tags),
    )
    deck.add_note(note)


def make_cheat(badge_text, badge_class, titulo, table_rows, criterios,
               ecoe_tip, penaliza, fuente, *extra_tags):
    """Card cheat sheet por estación: front=tabla dx/estudio/parámetro,
    back=criterio dx exacto + siguiente paso."""
    rows_html = "".join(
        f'<tr><td class="dx">{dx}</td><td>{est}</td>'
        f'<td class="par">{par}</td></tr>'
        for dx, est, par in table_rows
    )
    front = (
        f'<div class="badge {badge_class}">{badge_text}</div>'
        f'<div class="titulo">{titulo}</div>'
        f'<table class="cs">'
        f'<tr><th>Diagnóstico</th><th>Estudio</th><th>Parámetro clave</th></tr>'
        f'{rows_html}</table>'
    )
    crit_html = "".join(f"<li>{c}</li>" for c in criterios)
    back = (
        f'<div class="subt">Criterio dx exacto + siguiente paso</div>'
        f'<ul class="orienta">{crit_html}</ul>'
        f'<div class="tip-ecoe">🗣️ ECOE: {ecoe_tip}</div>'
        f'<div class="penaliza">⚠️ Penaliza si: {penaliza}</div>'
        f'<div class="fuente">📚 {fuente}</div>'
    )
    note = genanki.Note(
        model=model_qa,
        fields=[front, back],
        tags=BASE_TAGS + ["cheat_sheet"] + list(extra_tags),
    )
    deck.add_note(note)


# ============================================================
# A · UNIVERSALES — 14 cards
# ============================================================

make_card(
    "HEMATOLOGÍA", "tip-hema",
    "EB1 · Biometría hemática completa (3 series + diferencial)",
    'Eritrocitos: Hb H 13-17 / M 12-15 g/dL · Hto H 40-50 / M 36-44 %\n'
    'Índices: VCM 80-100 fL · HCM 27-33 pg · CHCM 32-36 g/dL · RDW 11-15%\n'
    'Reticulocitos: 0.5-2.5%\n'
    'Leucocitos: 4,500-11,000/mm³\n'
    'Fórmula: Neu 50-70 · Linf 20-40 · Mono 4-8 · Eos 1-4 · Bas 0-1 %\n'
    'Plaquetas: 150,000-450,000/mm³',
    'Hb ↓ → caracterizar por VCM (micro/normo/macro)\n'
    'Leucocitosis &gt;11k / leucopenia &lt;4k\n'
    'Neutrofilia, linfocitosis, eosinofilia, monocitosis\n'
    'Trombocitopenia &lt;150k / trombocitosis &gt;450k\n'
    'Pancitopenia (3 series bajas)',
    [
        "Anemia microcítica (VCM &lt;80) → ferropenia (90%), talasemia, anemia inflamatoria; pedir ferritina, TSAT, perfil de hierro.",
        "Anemia macrocítica (VCM &gt;100) → B12/folato, OH, hipotiroidismo, MDS, fármacos; pedir B12 + folato + TSH.",
        "Anemia normocítica → sangrado agudo, hemólisis, ERC, inflamatoria; reticulocitos altos = hemorragia/hemólisis; bajos = central.",
        "Leucocitosis + neutrofilia + bandemia = bacteriana, sepsis; linfocitosis = viral, EBV, CMV; eosinofilia = parásitos, alergia, vasculitis, Hodgkin.",
        "Leucopenia + neutropenia &lt;500 = agranulocitosis (clozapina, quimio) = riesgo séptico.",
        "Trombocitopenia &lt;50k = riesgo sangrado; &lt;20k = transfundir profiláctico; &lt;10k = espontáneo.",
        "Pancitopenia = aplasia medular, leucemia, linfoma, hiperesplenismo, mielodisplasia, déf B12 severo.",
    ],
    "MF/MI: anemia adulto → siempre VCM + sangrado oculto. Cx: leucocitos &gt;12k + clínica abdominal = peritonismo. Ped: ferropenia lactante (Hb &lt;11). Psiq: clozapina vigila neutros. GyO: anemia gestacional Hb &lt;11.",
    "siempre caracterizar la anemia por VCM antes de pedir más estudios.",
    "dices 'tiene anemia' sin VCM ni descartar sangrado oculto.",
    "Beutler 2006; UpToDate 'Approach to anemia'; OMS anemia cutoffs.",
    "hematologia", "bh", "universal",
)

make_card(
    "BIOQUÍMICA", "tip-bioq",
    "EB2 · Química sanguínea (glucosa · función renal · electrolitos)",
    'Glucosa: 70-100 mg/dL (ayuno)\n'
    'Urea: 7-20 mg/dL · BUN 7-20\n'
    'Creatinina: H 0.7-1.3 / M 0.6-1.1 mg/dL\n'
    'TFG (CKD-EPI): ≥90 mL/min/1.73 m²\n'
    'Na: 135-145 mEq/L · K: 3.5-5.0 · Cl: 98-107 · HCO₃: 22-28\n'
    'Ca total 8.5-10.5 / iónico 4.5-5.3 · Mg 1.5-2.5 · P 2.5-4.5\n'
    'Anion gap: 8-12 mEq/L = Na − (Cl + HCO₃)',
    'Glucosa: hipo &lt;70, hiper &gt;126 ayuno o &gt;200 random\n'
    'Cr ↑ + TFG ↓ → AKI o ERC (clasificar)\n'
    'Na: hipoNa &lt;135 / hiperNa &gt;145\n'
    'K: hipoK &lt;3.5 / hiperK &gt;5.0\n'
    'Anion gap ↑ &gt;12 → acidosis metabólica con AG\n'
    'Ca/Mg/P alterado',
    [
        "Glu &lt;70 sintomática = hipoglicemia → dextrosa IV (ml de D50%); &gt;180 hospitalario = control glucémico.",
        "Cr ↑ aguda → AKI por KDIGO (etapas 1-3); subagudo → ERC; FENa &lt;1% prerrenal, &gt;2% intrínseca.",
        "HipoNa &lt;130 sintomática = SIADH, hipovolémica, hipervolémica (cirrosis, IC); corregir &lt;10 mEq/24h.",
        "HiperK &gt;6.0 + cambios ECG (ondas T altas, QRS ancho) = urgencia → gluconato Ca, insulina+glucosa, β2, kayexalato, diálisis.",
        "Anion gap ↑ (MUDPILES): metanol, uremia, DKA, paraldehído, INH/isoniazida, lactato, etilenglicol, salicilatos.",
        "HipoCa &lt;7 sintomático = Chvostek, Trousseau, tetania, convulsión, prolongación QT → reposición.",
        "HipoK + hipoMg = no corrige hipoK hasta corregir Mg (Mg cofactor de bomba Na-K).",
    ],
    "MF/MI: glucosa + creatinina/TFG son tamizaje básico anual. Cx: K + creatinina + Na pre/postop. Ped: cuidar deshidratación (hipoNa, hipoK). Psiq: litio → vigilar Na/Cr; ISRS → hipoNa; metformina → contraindicada con TFG &lt;30. GyO: glucosa en embarazo (DG).",
    "siempre calcular TFG con CKD-EPI; anion gap en acidosis metabólica.",
    "registras Cr sin calcular TFG o no calculas AG en acidosis.",
    "KDIGO 2024; ADA 2025; UpToDate 'Electrolyte disorders'.",
    "bioquimica", "qs", "renal", "universal",
)

make_card(
    "URINARIO", "tip-urina",
    "EB3 · Examen general de orina (EGO) + sedimento",
    'Físico: color amarillo claro · aspecto transparente · olor sui generis\n'
    'Densidad: 1.005-1.030 · pH: 4.5-8.0\n'
    'Químico: glucosa negativa · cetonas negativas · proteínas negativas o trazas\n'
    'Bilirrubina/urobilinógeno: negativos / trazas\n'
    'Hemoglobina: negativa · esterasa leucocitaria: negativa · nitritos: negativos\n'
    'Sedimento: leucocitos &lt;5/HPF · eritrocitos &lt;3/HPF · sin cilindros patológicos · sin cristales',
    'Proteinuria + (qualitative) o A/Cr ≥30\n'
    'Glucosuria + (sin hiperglucemia = renal)\n'
    'Cetonuria + (DKA, ayuno, etanol)\n'
    'Hematuria (macro o &gt;3 eritrocitos/HPF)\n'
    'Leucocituria &gt;10 + nitritos + → ITU\n'
    'Cilindros (hialinos, granulares, hemáticos, leucocitarios, céreos)',
    [
        "Proteinuria persistente A/Cr ≥30 = nefropatía DM/HTA; ≥300 = albuminuria establecida; rango nefrótico &gt;3.5 g/24h.",
        "Glucosuria + glucemia normal = glucosuria renal (Fanconi, embarazo); SGLT2 esperado.",
        "Cetonuria + glu &gt;250 + acidosis = DKA; cetonuria + glu normal = ayuno o etilismo.",
        "Hematuria con cilindros hemáticos = origen glomerular (GN aguda, IgA, lupus); sin cilindros = postrenal (litiasis, neoplasia, ITU).",
        "Leucos + nitritos + esterasa + → ITU (E. coli 80%); urocultivo ≥10⁵ UFC confirma.",
        "Cilindros leucocitarios = pielonefritis; cilindros céreos/granulares = ERC avanzada; cilindros eritrocitarios = GN.",
        "Cristales: ácido úrico (gota, urato), oxalato cálcico (litiasis), estruvita (infección bacterias ureasa-positivas).",
    ],
    "MF: ITU + tamizaje albuminuria DM/HTA. MI: sedimento ≠ contexto (AKI, GN). Cx: hematuria postrauma renal. Ped: ITU pediátrica (leucos + nitritos en mayor &gt;2 a; en lactante puede ser negativo). Psiq: tóxicos en orina rutinario. GyO: bacteriuria asintomática en embarazo tratar siempre.",
    "describir sedimento siempre que el EGO es anormal; pedir urocultivo si nitritos+ o leucos &gt;10.",
    "registras 'EGO patológico' sin caracterizar proteínas, sedimento, urocultivo.",
    "UpToDate 'Interpretation of the urinalysis'; KDIGO; CDC.",
    "urinario", "ego", "universal",
)

make_card(
    "HEPÁTICO", "tip-hepat",
    "EB4 · Pruebas hepáticas + INR + albúmina",
    'AST: H ≤40 / M ≤32 U/L · ALT: H ≤41 / M ≤33 U/L\n'
    'FA: 40-130 U/L · GGT: H 8-61 / M 5-36 U/L\n'
    'Bilirrubina total: 0.3-1.2 mg/dL (directa &lt;0.3, indirecta &lt;0.9)\n'
    'Albúmina: 3.5-5.0 g/dL · Proteínas totales: 6.0-8.0 g/dL\n'
    'INR: 0.8-1.2 (sin anticoagulante)\n'
    'LDH: 140-280 U/L',
    'Patrón hepatocelular: AST/ALT ↑↑ predominante\n'
    'Patrón colestásico: FA/GGT ↑↑ predominante\n'
    'BT ↑ con BD &gt;1 = colestasis; con BI &gt;1 = hemólisis o Gilbert\n'
    'Albúmina &lt;3.5 = hipoalbuminemia\n'
    'INR &gt;1.5 = coagulopatía hepática severa',
    [
        "AST/ALT &gt;1000 = hepatitis viral, isquémica o tóxica (paracetamol, hongos); de Ritis (AST/ALT &gt;2) sugiere etílica o cirrosis.",
        "FA y GGT ↑↑ con BT ↑ y BD predominante = colestasis (obstructiva: coledocolitiasis, neoplasia páncreas; intrahepática: CBP, fármacos).",
        "FA ↑ con GGT normal = origen óseo (Paget, metástasis, raquitismo, embarazo).",
        "BT &gt;3 + AST/ALT alterados + INR &gt;1.5 + alteración mental = falla hepática fulminante → trasplante.",
        "BI ↑ aislada + reticulocitos ↑ + LDH ↑ + haptoglobina ↓ = hemólisis.",
        "Albúmina baja crónica + edema = cirrosis (síntesis), nefrótico (pérdida), malabsorción, malnutrición.",
        "Síndrome HELLP: hemólisis + elevación enzimas + plaquetas bajas en embarazada con preeclampsia.",
    ],
    "MF: tamizaje de hígado graso (NAFLD/MASLD) en sx metabólico. MI: hepatitis viral (serologías), cirrosis, hepatitis tóxica. Cx: pancreatitis biliar (PFH + lipasa). Ped: hepatitis A (común), B (vertical), atresia de vías biliares. Psiq: VPA hepatotóxico, carbamazepina. GyO: HELLP, colestasis intrahepática del embarazo.",
    "diferenciar patrón hepatocelular vs colestásico y calcular relación AST/ALT.",
    "registras 'PFH alteradas' sin caracterizar patrón ni patología sospechada.",
    "AASLD 2024; UpToDate 'Approach to elevated liver enzymes'.",
    "hepatico", "pfh", "universal",
)

make_card(
    "EQUILIBRIO Á/B", "tip-acido",
    "EB5 · Gasometría arterial + lactato",
    'pH: 7.35-7.45 · PaCO₂: 35-45 mmHg · PaO₂: 80-100 mmHg\n'
    'HCO₃: 22-26 mEq/L · EB: −2 a +2 mEq/L\n'
    'SatO₂: 95-100% · Lactato &lt;2 mmol/L\n'
    'Gradiente A-a (FiO₂ 21%): &lt;15 mmHg (joven); ≤edad/4 + 4\n'
    'Anion gap: 8-12 (calcular si acidosis met)',
    'Acidemia &lt;7.35 / alcalemia &gt;7.45\n'
    'Acidosis metabólica (HCO₃ ↓) ± anion gap\n'
    'Acidosis respiratoria (PaCO₂ ↑) ± compensación\n'
    'Alcalosis metabólica (HCO₃ ↑) / respiratoria (PaCO₂ ↓)\n'
    'Lactato &gt;2 = hipoperfusión; &gt;4 = shock\n'
    'PaO₂ &lt;60 = falla respiratoria',
    [
        "Algoritmo: 1) pH → acidemia/alcalemia; 2) PaCO₂ y HCO₃ identifican primario; 3) calcular compensación esperada (Winters: PaCO₂ ≈ 1.5×HCO₃ + 8); 4) AG en acidosis met.",
        "Acidosis met AG ↑ (MUDPILES): metanol, uremia, DKA, propilenglicol, INH/IRC, lactato, etilenglicol, salicilatos.",
        "Acidosis met AG normal (hiperclorémica): diarrea, RTA tipo 1 o 4, acetazolamida, inhibidores SGLT2.",
        "Alcalosis met: vómito, diuréticos, hiperaldosteronismo, hipokalemia.",
        "Acidosis respi aguda no compensada (HCO₃ normal con PaCO₂ ↑) = falla respiratoria aguda; tipo II = hipercápnica (EPOC reagudizado).",
        "Lactato ≥4 mmol/L + sepsis = sepsis-shock séptico (SSC bundle 1h).",
        "Trastornos mixtos: AG cambiado vs HCO₃ + AG corregido = sospechar 2 trastornos simultáneos.",
    ],
    "Cx: shock + sepsis + politrauma (Surviving Sepsis bundle). MI: DKA, EHH, intoxicaciones, EPOC reagudizado. Ped: deshidratación severa, intoxicaciones. Psiq: intoxicación por salicilatos o alcohol (acidosis met AG). GyO: emesis severa (alcalosis met hipoclorémica).",
    "siempre seguir el algoritmo (pH → primario → compensación → AG).",
    "registras GA sin identificar el trastorno primario ni calcular AG.",
    "Surviving Sepsis 2021; KDIGO; UpToDate 'Approach to acid-base disorders'.",
    "acidobase", "ga", "universal",
)

make_card(
    "COAGULACIÓN", "tip-coag",
    "EB6 · Coagulación: TP/INR · TTPa · fibrinógeno · plaquetas · dímero D",
    'TP: 11-13 s · INR: 0.8-1.2\n'
    'TTPa: 25-35 s\n'
    'Tiempo de trombina: 14-19 s\n'
    'Fibrinógeno: 200-400 mg/dL\n'
    'Plaquetas: 150,000-450,000/mm³\n'
    'Dímero D: &lt;500 ng/mL (≥edad×10 en ≥50 a)\n'
    'Sangrado patológico: PFA-100, factor von Willebrand, agregación',
    'TP/INR prolongado (vía extrínseca, factor VII)\n'
    'TTPa prolongado (vía intrínseca, VIII, IX, XI, XII, XII)\n'
    'Plaquetas &lt;100k = trombocitopenia\n'
    'Fibrinógeno &lt;100 = consumo (CID, hepatopatía)\n'
    'Dímero D ↑ = activación coagulación (TEP, TVP, CID, sepsis, embarazo)',
    [
        "TP/INR ↑ aislado: déficit factor VII (warfarina temprana, déf vit K, hepatopatía leve).",
        "TTPa ↑ aislado: heparina, déf factor VIII (hemofilia A), IX (B), XI, XII; lupus anticoagulante.",
        "TP + TTPa ↑ ambos: warfarina avanzada, hepatopatía, déf vit K severa, CID, fibrinolíticos.",
        "Trombocitopenia + esquistocitos + ↑ LDH + ↓ haptoglobina = MAT (PTT, SUH, HELLP, MAT inducida por fármaco).",
        "Plaquetopenia inmune (PTI): plaquetas aisladas, megacariocitos ↑ médula; tratar &lt;30k o sangrado.",
        "CID: TP ↑ + TTPa ↑ + fibrinógeno ↓ + plaquetas ↓ + dímero D ↑↑; tratar causa (sepsis, neoplasia, obstétrica, trauma).",
        "Dímero D negativo en Wells ≤4 (TVP) o ≤4 (TEP) excluye con alta sensibilidad.",
    ],
    "MI: heparina vs warfarina vs DOAC; reversión (vit K, PCC, plasma, andexanet, idarucizumab). Cx: pre/postoperatorio, anticoagulación postcirugía. Ped: hemofilia A/B (TTPa ↑ + factor ↓). Psiq: VPA puede causar trombocitopenia. GyO: embarazo es estado protrombótico; profilaxis HBPM en alto riesgo; CID en DPPNI, embolia LA.",
    "TP/INR + TTPa siempre con plaquetas + fibrinógeno + dímero D si sospecha CID.",
    "interpretas coagulación sin contexto clínico (anticoag, antiagregantes, hepatopatía).",
    "ASH; ISTH CID criteria; UpToDate 'Approach to bleeding'.",
    "coagulacion", "universal",
)

make_card(
    "CARDIO", "tip-cardio",
    "EB7 · ECG · lectura sistematizada (ritmo · FC · eje · intervalos · segmentos)",
    'Velocidad 25 mm/s · 1 mm = 0.04 s · 5 mm = 0.2 s\n'
    'Ritmo: sinusal si P precede QRS, P + en DII\n'
    'FC: 1500/RR(mm) o método 300/150/100/75/60/50\n'
    'Eje: aVF y DI. Normal −30° a +90°. Desviado izq &lt;−30° / der &gt;+90°\n'
    'Onda P: &lt;2.5 mm alto · &lt;0.12 s ancho\n'
    'PR: 0.12-0.20 s\n'
    'QRS: 0.06-0.10 s\n'
    'QT corregido (Bazett): &lt;460 mujer / &lt;450 hombre\n'
    'Segmento ST: isoeléctrico ± 1 mm\n'
    'Onda T: positiva en DI, DII, V3-V6',
    'Bradicardia &lt;60 · taquicardia &gt;100\n'
    'No sinusal (FA, flutter, ritmo de la unión, marcapasos)\n'
    'PR &gt;0.20 = BAV 1° · PR variable y bloqueo = BAV 2° o 3°\n'
    'QRS &gt;0.12 = bloqueo de rama u origen ventricular\n'
    'QTc &gt;500 = riesgo de torsade\n'
    'ST elevado/deprimido · T invertida · onda Q patológica',
    [
        "FA: irregularmente irregular, sin onda P, ondas f; calcular CHA₂DS₂-VASc para anticoagulación.",
        "Flutter auricular: ondas F en sierra a ~300/min, respuesta variable.",
        "BAV 1° (PR &gt;0.20 estable): observación; BAV 2° tipo Mobitz I (Wenckebach) suele ser benigno; Mobitz II = riesgo de progresión a BAV 3° → marcapasos.",
        "BAV 3° (disociación AV completa): marcapasos transitorio + permanente.",
        "Bloqueo de rama izq: QRS ancho + R-R' en V5-V6 + Q-S en V1; bloqueo de rama der: R-R' en V1-V2 + S en V5-V6.",
        "QTc &gt;500 = riesgo de torsade; corregir K, Mg; revisar fármacos (macrólidos, antiarrítmicos, antipsicóticos, ondansetrón).",
        "Eje desviado a la izquierda + onda Q en DI, aVL = bloqueo fascicular anterior izq.",
    ],
    "MI: arritmias, IC. Cx: ECG pre-op en ≥65 a, FRCV, cirugía mayor. Psiq: QTc pre-antipsicóticos (haloperidol, ziprasidona, citalopram). GyO: cardiomiopatía periparto.",
    "verbalizar el orden: ritmo → FC → eje → intervalos → segmentos → onda T.",
    "no calculas FC ni QTc, o no identificas el ritmo basal.",
    "ACC/AHA; ESC; UpToDate 'ECG approach'.",
    "cardio", "ecg", "lectura", "universal",
)

make_card(
    "CARDIO", "tip-cardio",
    "EB8 · ECG · patrones clínicos (isquemia · hipertrofias · arritmias)",
    'IAM con elevación ST (STEMI):\n'
    ' • Anteroseptal: V1-V2-V3 (DA proximal)\n'
    ' • Anterior extenso: V1-V6 (DA)\n'
    ' • Lateral: DI, aVL, V5-V6 (Cx)\n'
    ' • Inferior: DII, DIII, aVF (CD)\n'
    ' • Posterior: depresión ST V1-V2 con R alta\n'
    ' • VD: V4R con elevación (asociado a inferior)\n'
    'NSTEMI / angina inestable: depresión ST + onda T invertida\n'
    'Hipertrofia VI (Sokolow-Lyon): S V1 + R V5/V6 ≥35 mm; Cornell: R aVL + S V3 &gt;28 H / &gt;20 M\n'
    'Hipertrofia VD: R V1 &gt;7 mm + eje derecho + S persistente V5-V6\n'
    'TV monomorfa: QRS ancho regular &gt;120 ms · TSV: QRS estrecho regular &gt;150',
    'Elevación ST &gt;1 mm en ≥2 derivaciones contiguas (&gt;2 mm V2-V3) → STEMI\n'
    'Depresión ST &gt;0.5 mm + síntomas → NSTEMI/IAU\n'
    'Onda Q patológica (&gt;0.04 s, &gt;25% R) = infarto antiguo\n'
    'Onda T invertida simétrica + onda U = isquemia o hipoK\n'
    'Arritmia ventricular vs supraventricular\n'
    'Patrón S1Q3T3 → TEP (no patognomónico)\n'
    'Brugada · QT largo · Wolff-Parkinson-White',
    [
        "STEMI = código IAM: doble antiagregación + heparina + reperfusión (ICP &lt;90 min o fibrinólisis &lt;30 min si no ICP).",
        "STEMI inferior + R alta V1 + onda T positiva V1 = considerar IAM posterior asociado; pedir V7-V9.",
        "STEMI inferior + bradicardia + hipoTA = afectación VD; precarga dependiente, NO nitratos.",
        "Bloqueo de rama izq nuevo + síntomas = equivalente a STEMI.",
        "FA con respuesta ventricular rápida + inestable = cardioversión eléctrica; estable = control de frecuencia (β-bloq, BCC).",
        "TV sostenida sin pulso = desfibrilar; con pulso estable = amiodarona; inestable = cardioversión sincronizada.",
        "QT largo congénito + síncope familiar = riesgo torsade; β-bloq + evitar fármacos prolongadores.",
        "Brugada (V1-V3 elevación ST en cubierta, T negativa) = riesgo muerte súbita; desfibrilador implantable si sintomático.",
        "WPW (PR corto + onda delta + QRS ancho) = vía accesoria; evitar BCC/digoxina si FA (riesgo FV).",
    ],
    "MI/MF: tamizaje pre-op, dolor torácico, palpitaciones, síncope. Cx: pre/postop alto riesgo. Ped: cardiopatías congénitas (eje, QRS, signos). Psiq: QTc en antipsicóticos / ISRS. GyO: cardiopatía periparto.",
    "localizar IAM por derivaciones y citar arteria coronaria responsable.",
    "no identificas STEMI o no activas código IAM si dolor &lt;12 h.",
    "ACC/AHA 2023 SICA; ESC STEMI 2023; UpToDate.",
    "cardio", "ecg", "iam", "universal",
)

make_card(
    "PULMONAR", "tip-pulm",
    "EB9 · RxTx · técnica + lectura sistematizada (ABCDEFGH)",
    'Técnica: PA + lateral, inspiración (≥10 arcos costales posteriores), penetración (apenas se ven vértebras tras silueta cardio), rotación (clavículas simétricas).\n'
    'ABCDEFGH:\n'
    ' A — Airway: tráquea centrada, carina.\n'
    ' B — Breathing: hemidiafragmas, ángulos costofrénicos.\n'
    ' C — Cardiac: silueta, índice cardiotorácico &lt;0.5 PA.\n'
    ' D — Diafragma: derecho a nivel del 10° arco posterior.\n'
    ' E — Effusion: ángulos costofrénicos romos.\n'
    ' F — Fields: parénquima por campos (apical, medio, basal).\n'
    ' G — Gastric bubble: cámara gástrica izq.\n'
    ' H — Hilios: vasculatura, simetría, masas.\n'
    'Tejidos blandos + óseo: clavículas, costillas, columna.',
    'Tráquea desplazada, ICT &gt;0.5\n'
    'Hemidiafragma elevado (parálisis, masa, derrame, neumonía basal)\n'
    'Ángulo costofrénico romo: &gt;250 mL derrame\n'
    'Cámara gástrica con aire libre subdiafragmático = neumoperitoneo\n'
    'Infiltrado · consolidación · derrame · neumotórax · cardiomegalia · masa · atelectasia\n'
    'Fractura costal, escoliosis',
    [
        "Tráquea desplazada al lado opuesto = neumotórax a tensión, masa, derrame masivo; al mismo lado = atelectasia.",
        "ICT &gt;0.5 = cardiomegalia; puede ser falso si Rx AP o mala inspiración.",
        "Aire libre subdiafragmático (signo del balón, Rigler) = neumoperitoneo → perforación víscera hueca.",
        "Líneas B de Kerley (líneas septales en bases) + redistribución vascular = edema intersticial (IC izq).",
        "Patrón en alas de mariposa perihilar = EAP cardiogénico.",
        "Patrón miliar (nódulos &lt;3 mm difusos) = TB miliar, neumoconiosis, neoplasia.",
        "Consolidación con broncograma aéreo = neumonía bacteriana lobar.",
        "Atelectasia: opacidad + desplazamiento mediastino al lado opaco + elevación diafragma ipsilateral.",
    ],
    "MF/MI: NAC, EPOC, IC, masa pulmonar. Cx: trauma torácico (neumotórax, hemotórax, contusión), preop, postop. Ped: neumonía, bronquiolitis, cuerpo extraño. Psiq: pre-clozapina (descartar derrame). GyO: pre-anestesia, sospecha TEP (RxTx típicamente normal).",
    "leer en orden ABCDEFGH; nunca saltarse hilios ni partes blandas.",
    "describes hallazgos sin verificar técnica (rotación, inspiración, penetración).",
    "Bates; ATS; Felson's Principles of Chest Roentgenology; UpToDate.",
    "pulmonar", "rxtx", "universal",
)

make_card(
    "PULMONAR", "tip-pulm",
    "EB10 · RxTx · patrones patológicos clave",
    'Consolidación: opacidad alveolar con broncograma aéreo.\n'
    'Derrame pleural: borramiento ángulo costofrénico, línea de Damoiseau, derrame masivo desplaza mediastino contralateral.\n'
    'Neumotórax: línea de pleura visceral + ausencia trama vascular periférica; a tensión = desplazamiento mediastino contralateral, depresión diafragma.\n'
    'IC / EAP: cardiomegalia, redistribución vascular, líneas B de Kerley, infiltrados perihilares "alas de mariposa", derrame.\n'
    'EPI: patrón reticular o reticulonodular, panal de abeja, predominio basal-periférico (FPI).\n'
    'EPOC enfisema: hiperinflación, aplanamiento diafragmas, ↑ AP, bulas.\n'
    'Atelectasia: opacidad + desviación estructuras al lado opaco.\n'
    'Masa pulmonar: nódulo solitario &gt;3 cm o múltiples; cavitación; espiculaciones.\n'
    'TB: nódulos apicales, cavernas, ganglios hiliares, derrame, miliar.',
    'Identificar patrón → DDx → plan diagnóstico (TC tórax, broncoscopia, biopsia)',
    [
        "Consolidación lobar única + leucos ↑ + fiebre = neumonía bacteriana (S. pneumoniae #1) → CURB-65 / PSI.",
        "Consolidación bilateral basal en paciente joven afebril = neumonía aspirativa (anaerobios).",
        "Derrame unilateral nuevo en &gt;50 a + ↓ peso = paramaligno, considerar neoplasia (TC + toracocentesis).",
        "Derrame transudado (Light) = IC, cirrosis, nefrótico; exudado = paraneumónico, ca, TB, AR, autoinmune.",
        "Neumotórax a tensión = dx CLÍNICO; descomprimir antes de Rx.",
        "Patrón en panal con predominio basal y periférico + acropaquia + crepitantes velcro = FPI.",
        "Patrón miliar = TB miliar, neumoconiosis, metástasis (linfangitis carcinomatosa).",
        "Nódulo solitario &gt;3 cm en fumador + espiculaciones = altamente sospechoso de ca pulmón → biopsia (TC-PET).",
    ],
    "Cx: trauma (4 letales de B). MI: NAC, EAP, EPOC reagudizado. Ped: bronquiolitis vs neumonía. MF: tamizaje LDCT en fumadores 50-80 a + 20 paq-año. GyO: TEP es dx clínico (RxTx típica normal), pedir angio-TC o V/Q.",
    "identificar patrón pleural + parenquimatoso + mediastinal en orden.",
    "no diferencias derrame de consolidación o de atelectasia.",
    "ATS NAC; GOLD; ATS FPI; UpToDate.",
    "pulmonar", "rxtx", "universal",
)

make_card(
    "ORL", "tip-orl",
    "EB11 · Rx senos paranasales (Waters · Caldwell · Cavum)",
    'Proyección de Waters (occipitomentoplaca): senos maxilares y frontales.\n'
    'Caldwell (frontonasoplaca): senos frontales y etmoidales.\n'
    'Lateral: senos esfenoidales, cavum (adenoides en niños).\n'
    'Submentovertex (Hirtz): senos esfenoidales.\n'
    'Valores normales: senos aireados (negro), mucosa &lt;3 mm, sin niveles hidroaéreos.',
    'Niveles hidroaéreos en seno maxilar/frontal\n'
    'Opacidad total de seno\n'
    'Engrosamiento mucoso &gt;5 mm\n'
    'Defecto óseo (fractura, neoplasia)\n'
    'Cuerpo extraño metálico\n'
    'Cavum: hipertrofia adenoidea',
    [
        "Nivel hidroaéreo agudo + clínica de sinusitis ≥10 d = sinusitis bacteriana → amoxicilina o amoxi-clavulánico 7-10 d.",
        "Opacidad total de seno + clínica crónica &gt;12 sem = sinusitis crónica → considerar TC senos + ORL.",
        "Engrosamiento mucoso aislado sin nivel = puede ser viral o alérgica (NO ATB).",
        "Defecto óseo de seno + sintomas tumorales (epistaxis, masa, diplopía) = neoplasia (carcinoma, linfoma) → TC + biopsia.",
        "Fractura nasal/maxilar postrauma: enfisema subcutáneo, niveles hidroaéreos secundarios a sangrado.",
        "Hipertrofia adenoidea + ronquido + apneas + respiración bucal crónica = SAOS pediátrico → adenoidectomía.",
    ],
    "MF: sinusitis aguda (mayoría viral; ATB si ≥10 d severa o doble enfermedad). MI: tomografía senos en complicación (celulitis orbitaria, abceso epidural, trombosis cavernoso). Ped: hipertrofia adenoidea, sinusitis recurrente. Cx: trauma facial (Le Fort, fractura nasal). GyO: NA. Psiq: NA.",
    "no diagnosticar sinusitis bacteriana sin criterio clínico (síntomas ≥10 d, fiebre, dolor maxilar focal).",
    "indicas ATB en sinusitis sin cumplir criterios; pides Rx en niños (preferir TC si necesario).",
    "IDSA sinusitis 2012; AAO-HNS 2015; Cochrane sinusitis ATB.",
    "orl", "rxspn", "sinusitis",
)

make_card(
    "ABDOMEN", "tip-abdomen",
    "EB12 · USG abdomen + Rx simple abdomen",
    'Rx abdomen simple (de pie + decúbito):\n'
    ' • Aire intestinal: estómago, colon (haustras), recto.\n'
    ' • Niveles hidroaéreos: &lt;3 normales en ID.\n'
    ' • Dilatación ID &gt;3 cm · colon &gt;6 cm · ciego &gt;9 cm = obstrucción.\n'
    ' • Aire libre subdiafragmático (de pie) o entre asa y pared (Rigler) = neumoperitoneo.\n'
    ' • Asa centinela, ileo paralítico, vólvulo.\n'
    'USG abdomen:\n'
    ' • Hígado: ecogenicidad, tamaño, lesiones focales.\n'
    ' • Vesícula: pared (&lt;3 mm), litiasis, líquido perivesicular, Murphy ecográfico.\n'
    ' • Vía biliar: colédoco &lt;7 mm (&lt;10 mm postcolecistectomía).\n'
    ' • Páncreas (limitado por gas).\n'
    ' • Riñones: ectasia, litiasis, masas.\n'
    ' • Vejiga, aorta.',
    'Rx: dilatación intestinal, niveles, asa centinela, neumoperitoneo, calcificaciones.\n'
    'USG: pared vesicular engrosada, líquido perivesicular, litos, dilatación vías biliares, ascitis libre, masas hepáticas, hidronefrosis.',
    [
        "Niveles hidroaéreos múltiples + dilatación ID &gt;3 cm = obstrucción intestinal mecánica (causa #1 bridas postquirúrgicas).",
        "Asa centinela (asa dilatada aislada) = inflamación adyacente (apendicitis, pancreatitis, colecistitis).",
        "Neumoperitoneo (aire subdiafragmático en bipedestación) = perforación de víscera hueca → laparotomía.",
        "Vólvulo de sigmoides (asa en grano de café) o cecal: descompresión endoscópica + cirugía electiva.",
        "USG vesícula: pared &gt;4 mm + líquido perivesicular + Murphy ecográfico + litos = colecistitis aguda.",
        "Vía biliar dilatada + litiasis + PFH colestásicas = coledocolitiasis → CPRE.",
        "Hidronefrosis + dolor flanco + hematuria = litiasis ureteral; cálculo radiopaco en Rx (90% son cálcicos).",
        "Aorta abdominal &gt;3 cm = AAA; &gt;5.5 cm = reparación electiva; ruptura = emergencia (FAST con líquido libre, hipotensión).",
    ],
    "Cx: abdomen agudo, trauma. MI: ascitis, hepatopatía, AKI obstructiva. Ped: estenosis pilórica (USG: pared píloro &gt;3 mm + longitud &gt;15 mm), invaginación (signo del donut, pseudoriñon). GyO: USG TV ginecológico no es lo mismo que USG abdominal (ver EBGO3).",
    "interpretar Rx en orden: gas intestinal → niveles → calibre → aire libre → calcificaciones.",
    "no identificas neumoperitoneo en perforación o no reconoces hidronefrosis en cólico renal.",
    "Tokyo Guidelines 2024; ACG; UpToDate.",
    "abdomen", "rx_simple", "usg", "universal",
)

make_card(
    "TRAUMA", "tip-trauma",
    "EB13 · FAST · 4 ventanas en politraumatizado",
    '4 ventanas estándar:\n'
    ' 1) Subxifoidea (pericárdica): líquido alrededor del corazón = tamponade.\n'
    ' 2) Cuadrante superior derecho (Morrison/hepatorrenal): líquido entre hígado y riñón derecho.\n'
    ' 3) Cuadrante superior izquierdo (espleno-renal): líquido entre bazo y riñón izquierdo (también perisplénico/subdiafragmático).\n'
    ' 4) Suprapúbica (pélvica): líquido en fondo de saco de Douglas (M) o retrovesical (H).\n'
    'eFAST extendido: añade ventanas pleurales bilaterales (neumotórax: ausencia de "deslizamiento pleural") y pulmonares.',
    'Líquido anecoico en cualquier ventana = positivo\n'
    'Volumen estimado: 250 mL detectable; &gt;500 mL evidente\n'
    'Ausencia de deslizamiento pleural (eFAST) = neumotórax\n'
    'Engrosamiento pericárdico + colapso ventrículo der = tamponade',
    [
        "FAST positivo + inestabilidad hemodinámica = laparotomía exploradora urgente (no esperar TC).",
        "FAST positivo + estable = TC con contraste para caracterizar lesión.",
        "FAST negativo + inestable = buscar otros 4 sitios de sangrado (tórax, abdomen, pelvis, retroperitoneo, huesos largos); no descarta retroperitoneal.",
        "Tamponade: hipotensión + IVY + ruidos cardíacos apagados (Beck) + FAST subxifoidea con líquido + colapso VD = pericardiocentesis.",
        "Neumotórax en eFAST se detecta antes que en RxTx; punto pulmonar = patognomónico.",
        "Hemotórax (ventana pleural): líquido en seno costofrénico + colapso pulmonar parcial → drenaje torácico si &gt;500 mL.",
        "Embarazada con trauma: FAST igualmente útil; valorar feto con USG separado + FCF.",
    ],
    "Cx: politraumatizado (todos). MI: tamponade cardíaco, ascitis aguda. Ped: trauma cerrado (sensibilidad ↓ vs adulto). GyO: trauma en embarazada (HELLP no = FAST positivo; DPPNI = USG separado).",
    "verbalizar las 4 ventanas en orden y describir lo encontrado (positivo/negativo) en cada una.",
    "saltas ventanas, no haces eFAST en sospecha de neumotórax, o no actúas con FAST positivo + inestabilidad.",
    "ATLS 10ª; ACEP focused assessment with sonography for trauma; UpToDate.",
    "trauma", "fast", "atls", "universal",
)

make_card(
    "GYO / UNIVERSAL", "tip-gyo",
    "EB14 · β-hCG cualitativa y cuantitativa",
    'Cualitativa (orina o suero): negativa &lt;5 mUI/mL · positiva ≥25 (orina) o ≥5 (suero).\n'
    'Cuantitativa sérica:\n'
    ' • &lt;5 = no embarazo.\n'
    ' • 5-25 = zona gris (repetir 48 h).\n'
    ' • ≥1500-2000 = saco intrauterino debe verse en USG TV (zona discriminatoria).\n'
    ' • ≥6500 = saco visible en USG abdominal.\n'
    'Duplicación: ↑ ≥66% c/48 h en embarazo viable temprano.\n'
    'Pico: ~10 SDG (100,000); luego ↓ hasta meseta.',
    'Cualitativa positiva pero clínica de sangrado o dolor → cuantitativa\n'
    'Cuantitativa: subir lento (&lt;53% c/48 h) o caer\n'
    'Cuantitativa ≥1500 sin saco IU en USG TV = ectópico hasta descartar\n'
    'Niveles muy altos &gt;100,000 + USG con racimo de uvas = mola hidatiforme\n'
    'Persistencia post-evacuación de mola = enfermedad trofoblástica gestacional',
    [
        "β-hCG positiva = paciente embarazada hasta demostrar lo contrario; descartar antes de Rx, fármacos teratógenos, cirugía electiva.",
        "Subida menor a 53% c/48 h en embarazo temprano = embarazo no viable o ectópico → vigilar + USG TV.",
        "β-hCG &gt;1500-2000 + USG TV sin saco intrauterino = embarazo ectópico → metotrexate (si estable, &lt;3.5 cm, sin LCF) o quirúrgico.",
        "Caída &gt;50% c/48 h post-evacuación de aborto incompleto = curación; sin caer = retención de restos o trofoblástica.",
        "Mola: hCG &gt;100,000, útero mayor a EG, hiperémesis, USG en panal de abeja o tormenta de nieve.",
        "Hyperémesis gravidica + β-hCG ↑↑↑ = embarazo múltiple o mola.",
        "β-hCG falsa positiva: fármacos heterófilos, neoplasias germinales (testículo, ovario), tumores trofoblásticos no gestacionales.",
        "β-hCG plateau post-mola o no descenso = ETG persistente → metotrexate o quimio.",
    ],
    "TRANSVERSAL en MUJER FÉRTIL: antes de Rx, fármaco teratógeno, anestesia, cirugía electiva. MF/MI/Cx/Psiq: confirmar antes de prescribir. GyO: dx de embarazo, ectópico, aborto, mola, ETG.",
    "pedir β-hCG antes de cualquier intervención de riesgo teratogénico en mujer 12-50 a.",
    "prescribes teratógeno o haces Rx sin descartar embarazo en mujer fértil.",
    "ACOG; FDA Pregnancy Categories; Williams Obstetrics 26ª; UpToDate.",
    "gineco", "hcg", "embarazo", "universal", "mujer_fertil",
)


# ============================================================
# B · ESPECÍFICOS POR ESTACIÓN — 12 cards
# ============================================================

make_card(
    "MEDICINA FAMILIAR", "tip-endo",
    "EBMF1 · HbA1c + glucemia + CTOG 75 g (criterios DM ADA 2025)",
    'Glucemia ayuno: normal &lt;100 · GAA 100-125 · DM ≥126 (en 2 ocasiones)\n'
    'Glucemia random: ≥200 + síntomas clásicos = DM\n'
    'HbA1c: normal &lt;5.7% · prediabetes 5.7-6.4% · DM ≥6.5%\n'
    'CTOG 75 g (2 h): normal &lt;140 · prediabetes 140-199 · DM ≥200\n'
    'Glucosa promedio estimada: HbA1c × 28.7 − 46.7\n'
    'Objetivos en DM: HbA1c &lt;7% (general); &lt;6.5% si seguro; &lt;8% comorbilidad/anciano.',
    'HbA1c ≥6.5% (confirmar)\n'
    'GAA ≥126 (confirmar)\n'
    'CTOG 75 g ≥200\n'
    'Glucemia random ≥200 + síntomas\n'
    'HbA1c 5.7-6.4 o GAA 100-125 = prediabetes',
    [
        "DM se diagnostica con cualquiera de: HbA1c ≥6.5%, GAA ≥126, CTOG 2h ≥200, o glucemia random ≥200 + síntomas. CONFIRMAR en 2 ocasiones SEPARADAS (salvo crisis hiperglucémica).",
        "Prediabetes (5.7-6.4% / GAA 100-125 / CTOG 2h 140-199) = riesgo de progresión 5-10%/año; intervenir con estilo de vida (-7% peso, ejercicio 150 min/sem) + metformina si IMC ≥35 o ≥60 a o DG previa.",
        "HbA1c puede ser falso en: anemia hemolítica (falsamente baja), ERC, hemoglobinopatías, embarazo, transfusión reciente, ferropenia (falsamente alta).",
        "Objetivo HbA1c &lt;7% reduce micro y macrovascular; &lt;6.5% solo si se logra sin hipoglucemia ni polifarmacia; &lt;8% en mayor con multimorbilidad.",
        "ADA 2025: en DM tipo 2 considerar SGLT2/GLP-1 desde el inicio si ECV, IC, ERC, obesidad — beneficio cardiorrenal probado.",
        "Tamizaje ADA 2025: a partir de 35 a en todos; antes si sobrepeso + 1 FR (AHF, DG, raza, sx ovario poliquístico, HTA, dislipidemia).",
    ],
    "MF: tamizaje y control. MI: descompensación (DKA, EHH), comorbilidades CV/renales. Ped: DM1 (autoinmune, presentación con DKA), MODY, DM2 en obesidad infantil. GyO: DG (ver EBGO2).",
    "confirmar el dx con un segundo análisis y verificar la condición del paciente (anemia, hemoglobinopatías).",
    "haces dx de DM con un solo análisis o no confirmas si paciente asintomático.",
    "ADA Standards of Care 2025.",
    "medicina_familiar", "diabetes", "hba1c",
)

make_card(
    "MEDICINA FAMILIAR", "tip-endo",
    "EBMF2 · Perfil lipídico completo + objetivos por riesgo CV",
    'Colesterol total: deseable &lt;200 mg/dL\n'
    'LDL: óptimo &lt;100 · cerca de óptimo 100-129 · límite alto 130-159 · alto 160-189 · muy alto ≥190\n'
    'HDL: bajo &lt;40 H / &lt;50 M · alto ≥60 (factor protector)\n'
    'Triglicéridos: normal &lt;150 · límite alto 150-199 · alto 200-499 · muy alto ≥500\n'
    'No-HDL = CT − HDL · objetivo &lt; LDL + 30\n'
    'ApoB: refleja partículas aterogénicas; objetivo &lt;90 (riesgo alto) / &lt;80 (muy alto)\n'
    'Lp(a): &gt;50 mg/dL = factor de riesgo independiente',
    'LDL ≥190 = hipercolesterolemia familiar\n'
    'LDL ≥160 + 2 FR / ≥130 + 3 FR / ≥100 + ECV o DM\n'
    'TG ≥500 = riesgo de pancreatitis aguda\n'
    'HDL bajo + TG alto + LDL "normal" = dislipidemia aterogénica (sx metabólico)\n'
    'No-HDL más alto que LDL en TG altos',
    [
        "LDL ≥190 = hipercolesterolemia familiar HASTA descartar → tamizaje familiar (heterocigoto 1:250).",
        "ASCVD risk calculator (Pooled Cohort Equation): 40-75 a; ≥7.5% = considerar estatina; ≥20% = estatina alta intensidad.",
        "Prevención secundaria (ECV establecida): estatina alta intensidad + LDL objetivo &lt;55-70 mg/dL; añadir ezetimiba o iPCSK9 si no se alcanza.",
        "DM + ≥40 a o DM + ≥1 FR = estatina moderada/alta intensidad; objetivo LDL &lt;70.",
        "TG ≥500 = riesgo pancreatitis → fibrato (fenofibrato) ± omega-3; controlar DM y alcohol.",
        "HDL bajo aislado no es indicación de fármaco (terapias para subir HDL no han mostrado beneficio CV); enfocar en LDL y estilo de vida.",
        "Estatinas: monitorizar ALT y CK basal; no rutinariamente repetir salvo síntomas (mialgias, hepatopatía).",
        "Inhibidores PCSK9 (alirocumab, evolocumab) reducen LDL 60% adicional; indicados en ECV + LDL no controlado con estatina máxima + ezetimiba.",
    ],
    "MF: tamizaje universal adulto + ASCVD. MI: prevención secundaria post-IAM/EVC, optimizar a LDL &lt;55. GyO: embarazo eleva TG (fisiológico), pero TG &gt;1000 en 3T = riesgo de pancreatitis materno-fetal.",
    "calcular ASCVD risk en adulto 40-75 a y decidir estatina por riesgo no solo por LDL.",
    "tratas dislipidemia sin calcular riesgo CV global o sin descartar causas secundarias (hipotiroidismo, nefrótico, OH, ERC).",
    "ACC/AHA 2018 + 2022 actualización colesterol; ADA 2025; AHA scientific statements.",
    "medicina_familiar", "lipidos",
)

make_card(
    "MEDICINA FAMILIAR", "tip-endo",
    "EBMF3 · Microalbuminuria + relación A/Cr + tamizaje nefropatía",
    'Albúmina orina aleatoria + creatinina:\n'
    ' • Relación A/Cr (mg/g): normal &lt;30 · moderadamente aumentada 30-300 · severamente aumentada &gt;300\n'
    'Albúmina 24 h: normal &lt;30 mg/24 h · A1 &lt;30 · A2 30-300 · A3 &gt;300\n'
    'Tamizaje en DM: anual desde dx en DM2 y a partir de 5 años post-dx en DM1.\n'
    'Tamizaje en HTA: anual.\n'
    'TFG (CKD-EPI sin raza, 2021): mL/min/1.73 m²\n'
    ' • G1 ≥90 · G2 60-89 · G3a 45-59 · G3b 30-44 · G4 15-29 · G5 &lt;15 (diálisis)',
    'A/Cr 30-300 = microalbuminuria (KDIGO A2)\n'
    'A/Cr &gt;300 = macroalbuminuria/proteinuria (KDIGO A3)\n'
    'TFG &lt;60 sostenido ≥3 m = ERC\n'
    'Proteinuria nefrótica &gt;3.5 g/24h (o A/Cr &gt;3500)\n'
    'Hematuria + proteinuria + cilindros hemáticos = sx nefrítico',
    [
        "A/Cr &gt;30 confirma nefropatía DM/HTA → IECA o ARA II + control glucémico y tensional (objetivo &lt;130/80 en DM/ERC).",
        "Persistencia &gt;3 m de A/Cr &gt;30 o TFG &lt;60 = ERC establecida (KDIGO 2024); manejo según etapa G y A.",
        "ERC G3a en adelante = derivar nefrología; G4 = preparar acceso vascular y planear modalidad sustitución (HD, DP, trasplante).",
        "iSGLT2 (canagliflozina, empagliflozina, dapagliflozina) reducen progresión de nefropatía DM en ERC con A/Cr &gt;200; usar incluso con TFG ≥20.",
        "Finerenona (antagonista MR no esteroideo) reduce progresión ERC en DM2 con A/Cr ≥30.",
        "Causas reversibles de A/Cr alta: ITU, ejercicio reciente, fiebre, ICC descompensada — repetir en estado estable.",
        "Proteinuria rango nefrótico + hipoalbuminemia + edema + hipercolesterolemia = sx nefrótico → biopsia renal (membranosa, focal segmentaria, mínimos cambios, amiloidosis).",
    ],
    "MF: tamizaje universal en DM y HTA. MI: ERC, AKI sobre ERC, sx nefrítico/nefrótico (biopsia). Cx: contraste IV nefrotóxico en ERC G3 en adelante → premedicar/alternativas. GyO: tamizaje proteinuria en embarazadas para preeclampsia.",
    "documentar etapa de ERC con G y A (ej. ERC G3a-A2) y derivar a nefrología en G3a o A3.",
    "tratas DM/HTA sin tamizar A/Cr y TFG; no usas iSGLT2/finerenona cuando indicado.",
    "KDIGO 2024 CKD/Diabetes; ADA 2025; UPSTF.",
    "medicina_familiar", "renal", "albuminuria",
)

make_card(
    "MEDICINA INTERNA", "tip-endo",
    "EBMI1 · Función tiroidea (TSH · T4L · T3 · AntiTPO · AntiTg)",
    'TSH: 0.4-4.0 mUI/L (referencia trimestral en embarazo)\n'
    'T4 libre: 0.8-1.8 ng/dL · T3 total: 80-180 ng/dL · T3 libre: 2.3-4.2 pg/mL\n'
    'AntiTPO: &lt;35 UI/mL · AntiTg: &lt;40 UI/mL\n'
    'Tiroglobulina: marcador post-tiroidectomía por ca.\n'
    'Tamizaje TSH: mujeres ≥50 a, postparto, infertilidad, dislipidemia, depresión, AHF tiroides.',
    'TSH ↑ + T4L ↓ → hipotiroidismo primario\n'
    'TSH ↑ + T4L normal → hipotiroidismo subclínico\n'
    'TSH ↓ + T4L ↑ → hipertiroidismo primario\n'
    'TSH ↓ + T4L normal → hipertiroidismo subclínico\n'
    'TSH ↓ + T4L ↓ → hipopituitarismo (raro) o sx eutiroideo enfermo\n'
    'AntiTPO + → tiroiditis autoinmune (Hashimoto)\n'
    'AntiTSI / TSI + → Graves',
    [
        "Hipotiroidismo primario clínico (TSH &gt;10 + T4L ↓) = levotiroxina 1.6 µg/kg/día; control TSH 6-8 sem post-cambio.",
        "Hipotiroidismo subclínico (TSH 4-10): tratar si síntomas, AntiTPO +, infertilidad, depresión, dislipidemia, embarazo o intención.",
        "Hipertiroidismo (Graves 70%): T4L y T3 ↑ + TSH ↓ + bocio difuso + oftalmopatía + TSI + → metimazol + β-bloq; ablación con I-131 o tiroidectomía si grave/recurrente.",
        "Tiroiditis subaguda (de Quervain): dolor cervical + ↑ enzimas + captación baja en gammagrafía → AINE, esteroide si grave.",
        "Crisis tiroidotóxica: fiebre + taquicardia + agitación + IC + abdomen + altera concienc + alteración hepática → metimazol + β-bloq + esteroide + yoduro + UCI.",
        "Coma mixedematoso: hipotermia + bradicardia + hipoTA + estupor + hipoNa + insuficiencia respiratoria → levotiroxina IV + hidrocortisona + soporte UCI.",
        "Embarazo: TSH objetivo &lt;2.5 1T, &lt;3.0 2T-3T; hipotiroidismo materno = riesgo de retraso del DPM hijo → tratar precozmente.",
        "Antipsicóticos / litio pueden alterar TSH y T4L → tamizar antes y cada 6 m.",
    ],
    "MI: hipo/hipertiroidismo, mixedema, crisis tirotóxica. MF: tamizaje y dosificación. Psiq: DDx de depresión/manía. GyO: hipotiroidismo en embarazo (objetivo TSH &lt;2.5). Cx: optimizar antes de cirugía electiva.",
    "siempre interpretar TSH + T4L juntos; no tratar hipotiroidismo subclínico sin criterios.",
    "tratas hipotiroidismo subclínico sin indicación o no consideras embarazo.",
    "ATA Hypothyroidism 2014 + Hyperthyroidism 2016; ATA Thyroid in Pregnancy 2017.",
    "medicina_interna", "tiroides",
)

make_card(
    "MEDICINA INTERNA", "tip-cardio",
    "EBMI2 · Marcadores cardíacos (troponina hs · BNP / NT-proBNP · CK-MB)",
    'Troponina I/T de alta sensibilidad (hs-cTn): &lt;14 ng/L mujer / &lt;22 ng/L hombre (umbrales locales)\n'
    'Algoritmo ESC 0/1h o 0/3h: rule-in / rule-out IAM.\n'
    'BNP &lt;100 pg/mL (excluye IC); 100-400 zona gris; &gt;400 sugerente IC.\n'
    'NT-proBNP &lt;125 (&lt;75 a) o &lt;450 (≥75 a) excluye; &gt;450 / 900 / 1800 según edad sugiere IC.\n'
    'CK-MB: 0-5 ng/mL · pico 12-24 h post-IAM (poco usado ahora).\n'
    'Mioglobina: marcador temprano (2-6 h), poco específico.',
    'Troponina elevada + cambios ECG + clínica = SICA\n'
    'Curva ascendente o descendente (rise/fall) = lesión aguda\n'
    'BNP elevado = IC (descompensada o crónica)\n'
    'Tn elevada SIN dinámica clara = lesión miocárdica no aguda (miocarditis, sepsis, TEP, ERC, insuficiencia respi)\n'
    'CK ↑↑ sin Tn = rabdomiolisis (CK &gt;5000)',
    [
        "Algoritmo ESC 0/1h: tn al ingreso + a 1 h; cambio ≥5 ng/L o tn &gt;52 = IAM; tn &lt;5 + sin cambio + clínica baja = descartar y alta.",
        "Tn elevada CRÓNICA en ERC = lesión miocárdica crónica (microvascular); buscar cambio (rise/fall) para IAM.",
        "BNP/NT-proBNP eleva en: IC, ERC, edad, SCA, TEP, sepsis; ↓ en obesidad.",
        "NT-proBNP &gt;1800 + clínica disnea = alta probabilidad IC.",
        "Tn + BNP + RxTx + ECG = paquete básico para distinguir IC vs neumonía vs EPOC en disnea aguda.",
        "Tn ↑ en sepsis = factor pronóstico de mortalidad (no IAM).",
        "Tn ↑ en TEP = falla VD; pronóstico peor; considerar trombólisis si masivo.",
    ],
    "MI/MF: dolor torácico, disnea aguda, palpitaciones; algoritmo IAM. Cx: pre/postop alto riesgo (Tn pre-op en cirugía mayor ≥65 a). Psiq: ataque de pánico vs SICA (Tn aclara). GyO: cardiomiopatía periparto.",
    "siempre interpretar Tn DINÁMICA (rise/fall) en sospecha de SICA y combinar con clínica + ECG.",
    "registras Tn sola sin contexto clínico o sin segunda muestra.",
    "ESC NSTEMI 2023; ACC/AHA 2023; ESC Heart Failure 2021.",
    "medicina_interna", "marcadores_cardio",
)

make_card(
    "CIRUGÍA", "tip-bioq",
    "EBCx1 · Amilasa + lipasa + Atlanta revisada + Ranson/BISAP (pancreatitis)",
    'Amilasa: 30-110 U/L (poco específica; eleva también en parotiditis, perforación intestinal, EAO).\n'
    'Lipasa: 0-160 U/L (más específica; ≥3× límite alto = pancreatitis).\n'
    'Atlanta revisada 2012: 2/3 criterios para dx — dolor abdominal característico + lipasa/amilasa ≥3× + imagen.\n'
    'Severidad Atlanta: leve (sin falla orgánica), moderada (falla orgánica transitoria &lt;48 h), grave (falla orgánica persistente &gt;48 h).\n'
    'Ranson (al ingreso + 48 h): &gt;3 puntos = grave.\n'
    'BISAP (más simple, 5 puntos en 24 h): BUN &gt;25, alteración mental, SIRS, edad &gt;60, derrame pleural.',
    'Lipasa ≥3× límite alto + clínica = pancreatitis aguda\n'
    'Hemoconcentración (Hto &gt;44 ingreso) = factor pronóstico adverso\n'
    'Hiperglucemia &gt;200, hipocalcemia &lt;8, ↑ BUN, ↑ DHL = severidad\n'
    'Cullen (periumbilical) / Grey-Turner (flancos) = hemorragia retroperitoneal',
    [
        "Pancreatitis biliar (cálculo): USG + PFH colestásicas; colecistectomía en mismo ingreso si leve.",
        "Pancreatitis OH: 2ª causa; cesar consumo + tiamina.",
        "Pancreatitis severa = UCI; reposición agresiva (lactato Ringer 250-500 mL/h primeras 24 h, ajustar por respuesta), control dolor.",
        "Necrosis pancreática &gt;30% por TC con contraste a las 72-96 h; manejo expectante si estéril, drenaje/desbridamiento si infectada.",
        "ATB no profiláctico; sí si infección comprobada o sospecha alta (fiebre persistente + leucocitosis + necrosis).",
        "ERCP precoz (&lt;24 h) solo si colangitis aguda o ictericia persistente con coledocolitiasis.",
        "Pseudoquiste pancreático &gt;6 sem post: drenaje si síntomas o complicación.",
        "Hipertrigliceridemia &gt;1000 mg/dL = causa pancreatitis severa; plasmaféresis o insulina IV.",
    ],
    "Cx: dx + severidad. MI: pancreatitis OH/biliar como descompensación; complicaciones (ARDS, AKI). MF: pancreatitis crónica (DM + insuficiencia exocrina). GyO: pancreatitis en embarazo (litiasis biliar y hipertrigliceridemia 3T).",
    "calcular BISAP a las 24 h y reanimar agresivamente las primeras 24-48 h.",
    "haces dx de pancreatitis con amilasa sola o no clasificas severidad.",
    "Atlanta revisada 2012; IAP/APA guidelines; UpToDate.",
    "cirugia", "pancreatitis",
)

make_card(
    "PEDIATRÍA", "tip-hema",
    "EBPed1 · Tamiz neonatal + BH pediátrica por edad",
    'Tamiz neonatal metabólico ampliado (México, talón, día 3-5):\n'
    ' • Hipotiroidismo congénito (TSH &gt;30), fenilcetonuria, hiperplasia suprarrenal congénita, galactosemia, fibrosis quística, deficiencia biotinidasa.\n'
    'Tamiz auditivo (otoemisiones acústicas o PEATC).\n'
    'BH pediátrica por edad (valores normales aproximados):\n'
    ' • Recién nacido: Hb 14-22 (mayor que adulto), leucos 9-30k, plaquetas 150-450k.\n'
    ' • Lactante 6-12 m: Hb 11-13, leucos 6-15k, neutrófilos 30%, linfocitos 60% (inversión vs adulto).\n'
    ' • Preescolar 2-6 a: Hb 11-13, leucos 5-15k, fórmula se acerca al adulto a los 4-6 a.\n'
    ' • Escolar/adolescente: similar a adulto.',
    'Hb &lt;11 lactante / &lt;11.5 niño = anemia OMS\n'
    'Leucos &lt;5k o &gt;20k = patológico fuera del rango edad\n'
    'Neutropenia &lt;1500 = riesgo infección\n'
    'TSH neonatal &gt;30 = hipotiroidismo congénito\n'
    'Tamiz auditivo: refer = derivar audiología',
    [
        "Hipotiroidismo congénito (1:3,500-4,000): iniciar levotiroxina &lt;14 días post nacimiento previene retraso mental; dosis 10-15 µg/kg/día.",
        "Fenilcetonuria: dieta restrictiva en fenilalanina de por vida; tamizaje + tratamiento previenen retraso mental.",
        "Anemia ferropénica del lactante (más prevalente 9-24 m): Hb &lt;11 + VCM &lt;70 + ferritina &lt;12; tratamiento Fe oral 3-6 mg/kg/día.",
        "Neutropenia &lt;1500 + fiebre = neutropenia febril → BH + HC + LCR (si &lt;3 m) + ATB empírico.",
        "Leucocitosis &gt;30k + blastos = LLA pediátrica (más común neoplasia infantil) → derivar hematología urgente.",
        "Linfocitosis transitoria (tos ferina, EBV) puede llegar a 50k.",
        "Plaquetas &lt;100k en niño: PTI postviral (la causa más común), considerar IVIG si sangrado o &lt;30k.",
        "Reticulocitos elevados en lactante = compensación normal a la anemia fisiológica del lactante (nadir 8-12 sem).",
    ],
    "Ped: tamiz neonatal universal, BH por edad. MF: anemia ferropénica del lactante. MI: neoplasias pediátricas (LLA). GyO: HC vs hipotiroidismo congénito (control TSH materna en embarazo).",
    "interpretar BH pediátrica usando rangos por edad, no del adulto.",
    "aplicas rango adulto en niño (resultaría en sobre-dx anemia o leucocitosis).",
    "AAP Bright Futures 2022; NOM-007-SSA2-2016; OMS anemia infantil.",
    "pediatria", "tamiz_neonatal", "bh_ped",
)

make_card(
    "PSIQUIATRÍA", "tip-bioq",
    "EBPsiq1 · Laboratorios basales antes de psicofármaco",
    'Pre-antipsicótico atípico (clozapina, olanzapina, quetiapina, risperidona):\n'
    ' • BH (línea base de neutros si clozapina), glucosa ayunas, HbA1c, perfil lipídico, perímetro abdominal, peso, IMC.\n'
    ' • Función hepática, renal, electrolitos, prolactina (basal si será risperidona), TSH.\n'
    ' • ECG (QTc) — clave en haloperidol, ziprasidona, citalopram, escitalopram, antipsicóticos.\n'
    ' • β-hCG en mujer fértil.\n'
    'Pre-litio:\n'
    ' • TSH (afecta tiroides), creatinina (afecta riñón), electrolitos, calcio, β-hCG, ECG, BH.\n'
    'Pre-valproato:\n'
    ' • PFH, BH (plaquetas), amilasa/lipasa, β-hCG.\n'
    'Pre-carbamazepina:\n'
    ' • BH (leucos), PFH, Na, HLA-B*1502 en asiáticos (riesgo Stevens-Johnson).',
    'BH: línea base de neutros (clozapina), plaquetas (VPA)\n'
    'Glucosa/HbA1c/lípidos: línea base para sx metabólico\n'
    'ECG QTc &gt;500 = riesgo torsade\n'
    'PFH, creatinina, electrolitos, TSH, β-hCG\n'
    'Tóxicos en orina (descartar SUD comórbido)',
    [
        "Clozapina: BH semanal × 6 meses, después cada 2 sem × 6 m, después mensual; suspender si neutros &lt;1500; nunca readministrar si &lt;1000.",
        "Litio: estrecho margen terapéutico (0.6-1.2 mEq/L); tóxico &gt;1.5; monitorizar c/3-6 m + TSH + Cr; suspender 24 h antes de cirugía electiva.",
        "Valproato: contraindicado en mujer fértil (teratógeno mayor, DTN); si imprescindible, anticoncepción dual + folato 4 mg/día.",
        "Carbamazepina: induce CYP3A4 → ↓ ACO; controlar Na (SIADH); HLA-B*1502 + en asiáticos predispone a Stevens-Johnson.",
        "Antipsicóticos atípicos: vigilar peso (cintura), glucosa, lípidos al inicio, 3 m, 6 m, anual; sx metabólico es la principal causa de morbimortalidad.",
        "ECG QTc &gt;500 o cambio &gt;60 ms: no iniciar o cambiar antipsicótico; corregir K, Mg.",
        "ISRS + tramadol/triptanes/IMAO = sx serotoninérgico (hipertermia, hiperreflexia, clonus, agitación) → urgencia.",
        "Antipsicótico + fiebre + rigidez + AMS + ↑ CK = sx neuroléptico maligno → suspender + bromocriptina/dantroleno + soporte UCI.",
    ],
    "Psiq: antes de iniciar; monitoreo periódico. MF: detección de sx metabólico inducido. MI: complicaciones (hiponatremia, hipotiroidismo por litio). GyO: contraindicaciones en mujer fértil (VPA, litio); ajuste en embarazo.",
    "siempre pedir BH + QS + PFH + TSH + ECG + β-hCG antes de iniciar psicofármaco.",
    "inicias antipsicótico/litio/VPA sin labs basales o no monitorizas QTc.",
    "APA Practice Guidelines; FDA labels; Maudsley 14th ed; UpToDate.",
    "psiquiatria", "psicofarmacos", "labs_basales",
)

make_card(
    "PSIQUIATRÍA", "tip-bioq",
    "EBPsiq2 · Niveles séricos terapéuticos / tóxicos (litio · VPA · CBZ · clozapina)",
    'Litio: terapéutico 0.6-1.2 mEq/L · tóxico ≥1.5 · severo ≥2.5\n'
    ' • Toma muestra 12 h post-dosis (valle); reajustar c/5-7 días.\n'
    'Valproato (ácido valproico): terapéutico 50-100 µg/mL · tóxico &gt;100 · letal &gt;1000\n'
    'Carbamazepina: terapéutico 4-12 µg/mL · tóxico &gt;12\n'
    'Clozapina: terapéutico 350-600 ng/mL · &gt;1000 ng/mL riesgo de toxicidad\n'
    'Fenitoína: terapéutico 10-20 µg/mL · tóxico &gt;20 (libre &gt;2)\n'
    'Lamotrigina: terapéutico 1-15 µg/mL (poco rutinario)\n'
    'Olanzapina: 20-80 ng/mL\n'
    'Risperidona + 9-OH: 20-60 ng/mL',
    'Litio tóxico: tremor grueso, ataxia, vómito, diarrea, confusión, convulsión\n'
    'VPA tóxico: somnolencia, ataxia, hiperamonemia, pancreatitis, hepatotoxicidad\n'
    'CBZ tóxico: ataxia, diplopía, somnolencia, hipoNa, agranulocitosis\n'
    'Clozapina &gt;1000: convulsión, miocarditis, sialorrea masiva\n'
    'Fenitoína &gt;30: nistagmo, ataxia, disartria; &gt;40: alteración consciencia',
    [
        "Litio: factores que ↑ niveles → AINE, IECA, tiazidas, deshidratación, dieta baja en Na, ERC; tóxico → suspender + suero fisiológico + hemodiálisis si &gt;2.5 o sintomático.",
        "VPA hiperamonemia: alteración mental + ↑ amonio sérico (a veces con niveles VPA normales); tratar con L-carnitina + lactulosa.",
        "VPA pancreatitis: idiosincrásica, sin relación dosis; suspender al confirmar.",
        "CBZ hipoNa por SIADH: Na &lt;130 sintomática → suspender y restringir agua.",
        "CBZ agranulocitosis (rara): neutros &lt;500 → suspender + soporte; cribar HLA-B*1502 en asiáticos antes de iniciar.",
        "Clozapina miocarditis: dentro de las primeras 4 semanas → tropoinina + CK + ECG semanal; si Tn ↑ suspender inmediatamente.",
        "Sx serotoninérgico (ISRS + tramadol/triptanes/IMAO): hipertermia + clonus + hiperreflexia + agitación → suspender, ciproheptadina, soporte.",
        "Síndrome neuroléptico maligno: fiebre + rigidez en barra de plomo + AMS + ↑ CK → suspender antipsicótico, bromocriptina/dantroleno, refrigerar, UCI.",
    ],
    "Psiq: monitorizar niveles al inicio (c/5-7 d), cambio de dosis, sospecha de toxicidad. MI: intoxicaciones, sx serotoninérgico, NMS. MF/Cx: comprobar antes de cirugía electiva.",
    "tomar litio en valle (12 h post-dosis); verificar amonio en VPA con alteración mental.",
    "interpretas niveles fuera del tiempo correcto (pico vs valle) o no asocias síntomas a niveles.",
    "Maudsley 14th ed; APA Practice Guidelines; Goodman & Gilman 14th.",
    "psiquiatria", "niveles_sericos",
)

make_card(
    "GINECO-OBSTETRICIA", "tip-gyo",
    "EBGO1 · Perfil prenatal completo",
    'Primer trimestre (8-12 SDG):\n'
    ' • BH (anemia Hb &lt;11 = anémica)\n'
    ' • Grupo sanguíneo y Rh (si Rh− pedir Coombs indirecto)\n'
    ' • Glucosa ayuno (si &gt;92 = DG temprana, ≥126 = DM pre-gestacional)\n'
    ' • EGO + urocultivo (bacteriuria asintomática)\n'
    ' • Serologías: VIH, VDRL/sífilis, HBsAg, AcHbsAg, AcVHC\n'
    ' • Inmunidad: rubéola IgG, varicela IgG, citomegalovirus, toxoplasma (si riesgo), Chagas (zonas endémicas)\n'
    ' • Tiroides (TSH, T4L) si síntomas o AHF\n'
    'Tamizaje aneuploidías 1T (11-14 SDG): TN + PAPP-A + β-hCG libre.\n'
    'Segundo trimestre: USG anatomía + cervicometría (20-24).\n'
    'Tercer trimestre: BH + EGO + USG crecimiento + Streptococcus B (35-37 SDG, hisopado vaginal + rectal).',
    'Hb &lt;11 = anemia gestacional → Fe + folato\n'
    'GS-Rh− + Coombs+ = isoinmunización → vigilancia y Ig anti-D\n'
    'VIH+ → AVR + cesárea programada si CV detectable\n'
    'Sífilis+ → penicilina G + tratar pareja\n'
    'HBsAg+ → Ig específica + vacuna neonato\n'
    'Rubéola IgG− → vacunar postparto (NO en embarazo)\n'
    'Streptococcus B+ → penicilina IV intraparto',
    [
        "Bacteriuria asintomática en embarazo SIEMPRE tratar (10-30% progresan a pielonefritis con riesgo de parto pretérmino).",
        "Sífilis: penicilina G benzatínica 2.4 M UI IM (única en primaria/secundaria; semanal × 3 en latente tardía o desconocida).",
        "Rh− no sensibilizada: Ig anti-D 300 µg IM a las 28 SDG + dentro de 72 h post-parto si RN Rh+.",
        "Rh− con Coombs indirecto +: titulación; ≥1:16 = riesgo EHRN → manejo en 3er nivel con USG Doppler ACM.",
        "Toxoplasma IgM+ + IgG- = primoinfección reciente → espiramicina + amniocentesis (PCR LA).",
        "Streptococcus B+: penicilina G 5 M UI bolo + 2.5 M c/4 h hasta nacimiento; previene sepsis neonatal por SGB.",
        "Tamizaje aneuploidías 1T (combinado: TN + PAPP-A + β-hCG libre) = sensibilidad 85-90% para Down; complementar con NIPT si alto riesgo.",
        "VHC+: NO tratar en embarazo (DAAs no recomendados); tratar postparto; cesárea solo si OI estándar.",
    ],
    "GyO: control prenatal universal; tamizaje DG ver EBGO2. MF: pre-conceptional (folato, vacunas, tabaco, alcohol, OH, dieta). MI: comorbilidad pre-gestacional (HTA, DM, tiroides, autoinmune). Psiq: depresión perinatal (EPDS).",
    "el perfil prenatal completo se solicita en la 1ª consulta + segundo + tercer trimestre con SGB y BH/EGO.",
    "omites alguna serología (VDRL, VIH, HBsAg, rubéola) o no haces SGB en 35-37 SDG.",
    "ACOG; Williams Obstetrics 26ª; NOM-007-SSA2-2016; CDC.",
    "gineco", "embarazo", "prenatal",
)

make_card(
    "GINECO-OBSTETRICIA", "tip-gyo",
    "EBGO2 · Tamizaje diabetes gestacional (O\'Sullivan + CTOG)",
    'Estrategia dos pasos (ACOG):\n'
    ' 1) O\'Sullivan (24-28 SDG): carga 50 g VO, glucemia a 1 h. Anormal: ≥140 (algunos ≥130 para mayor sensibilidad).\n'
    ' 2) CTOG 100 g (Carpenter-Coustan): ayuno + 1h + 2h + 3h. Dx DG con ≥2 valores anormales: ayuno ≥95, 1h ≥180, 2h ≥155, 3h ≥140.\n'
    'Estrategia un paso (IADPSG/ADA):\n'
    ' • CTOG 75 g a 24-28 SDG. Dx DG con CUALQUIERA ≥ ayuno 92 / 1h 180 / 2h 153.\n'
    'Tamizaje precoz en 1er trimestre si: IMC ≥30, AHF DM, DG previa, edad ≥35, HbA1c ≥5.7.\n'
    'DM pre-gestacional: glucemia ayuno ≥126 o HbA1c ≥6.5 antes/al inicio de embarazo.',
    'O\'Sullivan ≥140 → CTOG 100 g\n'
    'CTOG (Carpenter-Coustan) con ≥2 valores anormales = DG\n'
    'CTOG 75 g (IADPSG) con ≥1 anormal = DG\n'
    'Glucemia ayuno ≥126 o HbA1c ≥6.5 = DM pre-gestacional',
    [
        "Manejo DG: nutrición + ejercicio + autovigilancia 4×/día (ayuno + postprandial 1h); insulina si falla en 1-2 semanas.",
        "Metformina es alternativa pero pasa placenta; ACOG y ADA permiten; insulina sigue siendo primera línea.",
        "Objetivos glucémicos DG: ayuno &lt;95, 1h &lt;140, 2h &lt;120.",
        "Macrosomía fetal (&gt;4000-4500 g) → distocia de hombros, cesárea; PFE &gt;p90 considera inducción 39 SDG.",
        "Hipoglucemia neonatal en hijo de madre diabética: glucemia &lt;40 mg/dL primeras 24 h; vigilar y alimentar precozmente.",
        "Postparto: CTOG 75 g a 4-12 semanas postparto (50% riesgo DM2 a 10 años); HbA1c c/1-3 años; estilo de vida.",
        "DM pregestacional: control HbA1c &lt;6.5% periconcepcional reduce malformaciones (cardio, neural, esqueléticas); folato 4 mg.",
        "Cetoacidosis diabética en embarazo puede ocurrir con glucemia &lt;200 (rara fuera de embarazo); pH &lt;7.3, HCO3 &lt;15.",
    ],
    "GyO: tamizaje 24-28 SDG + precoz si riesgo. MF/MI: prediabetes pre-gestacional. Ped: hijo de madre diabética (hipoglucemia, macrosomía). Cx: cesárea por macrosomía.",
    "tamizar SIEMPRE 24-28 SDG; precoz si IMC ≥30, AHF, DG previa, HbA1c ≥5.7.",
    "no tamizas DG en 24-28 SDG o usas criterios obsoletos.",
    "ACOG Practice Bulletin 190; ADA Standards of Care 2025; IADPSG.",
    "gineco", "embarazo", "diabetes_gestacional",
)

make_card(
    "GINECO-OBSTETRICIA", "tip-gyo",
    "EBGO3 · USG obstétrico por trimestre",
    'Primer trimestre (11-14 SDG):\n'
    ' • Translucencia nucal (TN): &lt;3 mm normal.\n'
    ' • Hueso nasal: presente.\n'
    ' • Tamizaje combinado: TN + PAPP-A + β-hCG libre + edad materna → riesgo Down.\n'
    ' • Datación: longitud céfalo-caudal (LCC) más exacta para EG.\n'
    'Segundo trimestre (18-22 SDG):\n'
    ' • USG estructural (anatomía fetal): cardio, SNC, columna, abdomen, extremidades, perfil.\n'
    ' • Marcadores soft: pielectasia, foco hiperecogénico, hueso nasal.\n'
    ' • Cervicometría: longitud cervical (LC); &lt;25 mm = riesgo de parto pretérmino.\n'
    'Tercer trimestre (28-32 SDG):\n'
    ' • PFE (peso fetal estimado) por percentiles.\n'
    ' • Doppler arteria umbilical (AU), cerebral media (ACM), ductus venoso.\n'
    ' • ILA / pozo único máximo: oligohidramnios (ILA &lt;5) / polihidramnios (ILA &gt;25).\n'
    ' • Perfil biofísico (PBF): tono + movimiento + respiración + LA + NST.',
    'TN &gt;3 mm → riesgo cromosomopatía\n'
    'Anomalía estructural detectada → consejo y plan\n'
    'LC &lt;25 mm → cerclaje o progesterona\n'
    'PFE &lt;p10 = RCIU\n'
    'Doppler AU IP &gt;p95, ausente, reverso = sufrimiento fetal\n'
    'ILA &lt;5 = oligohidramnios; &gt;25 = polihidramnios\n'
    'PBF ≤4/10 = compromiso fetal',
    [
        "TN &gt;3 mm aislada en USG 1T = riesgo aneuploidía y cardiopatías; tamizaje combinado o NIPT + ecocardiograma fetal 22 SDG.",
        "Anomalías mayores en USG estructural 2T = consejo genético, considerar amniocentesis (cariotipo, array CGH).",
        "Cervicometría &lt;25 mm a 16-24 SDG + antecedente de parto pretérmino = cerclaje cervical electivo o progesterona vaginal.",
        "RCIU: PFE &lt;p10 + Doppler anormal = vigilancia estrecha; ausencia/reversión flujo diastólico AU = interrupción ≤32-34 SDG.",
        "Oligohidramnios: rotura prematura, RCIU, malformación renal, postérmino, AINE materno; considerar interrupción según SDG y causa.",
        "Polihidramnios: DM materna, atresia esofágica/duodenal, anencefalia, hidrops; estudiar.",
        "PBF: 8-10/10 normal; 6/10 dudoso (repetir 24 h); ≤4/10 = interrumpir embarazo si maduro.",
        "USG TV inicial en embarazo de localización desconocida + β-hCG ≥1500-2000 sin saco IU = ectópico → manejo.",
    ],
    "GyO: control prenatal universal. MF: derivación ante hallazgos. MI: NA. Ped: prepara al neonatólogo si anomalía conocida. Cx: cesárea programada por hallazgos.",
    "verbalizar percentil PFE, ILA, Doppler en cada USG 3T.",
    "no documentas hallazgos cuantitativos (TN, LC, PFE, ILA, Doppler) o no actúas con flujo diastólico reverso.",
    "ISUOG; ACOG; SMFM; Williams Obstetrics 26ª.",
    "gineco", "embarazo", "usg",
)


# ============================================================
# C · CHEAT SHEETS POR ESTACIÓN — 6 cards
# ============================================================

make_cheat(
    "CHEAT SHEET · MF", "cs-mf",
    "Medicina Familiar · Dx más comunes — estudio + parámetro disparador",
    [
        ("DM2 de novo", "HbA1c · glucemia · CTOG", "HbA1c ≥6.5% o GAA ≥126 o CTOG 2h ≥200"),
        ("Prediabetes", "HbA1c · glucemia", "HbA1c 5.7-6.4% o GAA 100-125"),
        ("Hipercolesterolemia familiar", "Perfil lipídico", "LDL ≥190 mg/dL"),
        ("Dislipidemia 1°", "Perfil lipídico + ASCVD", "LDL ≥160 + 2 FR / ≥100 con ECV o DM"),
        ("HTA con nefropatía", "TA + EGO + A/Cr", "TA ≥140/90 + A/Cr ≥30 mg/g"),
        ("Hipotiroidismo primario", "TSH · T4L", "TSH ↑ + T4L ↓; subclínico TSH 4-10"),
        ("Anemia ferropénica adulto", "BH + ferritina + TSAT", "Hb ↓ + VCM &lt;80 + ferritina &lt;30 + TSAT &lt;20%"),
        ("ITU baja no complicada", "EGO + urocultivo", "Leucos &gt;10/HPF + nitritos+ + urocultivo ≥10⁵"),
        ("Sx metabólico", "TA + perímetro + lípidos + glucosa", "3/5 criterios ATP III"),
        ("Sinusitis bacteriana aguda", "Clínica ± RxSPN Waters", "Síntomas ≥10 d o doble enfermedad + nivel hidroaéreo"),
        ("Anemia + sangrado oculto ≥50 a", "BH + SOH/colonoscopia", "Hb ↓ + SOH+ → CCR hasta descartar"),
        ("Bacteriuria asintomática NO embarazada", "Urocultivo", "Urocultivo ≥10⁵ sin síntomas → NO tratar (salvo embarazo, transplante, prequirúrgico)"),
    ],
    [
        "DM2: confirmar con 2 análisis salvo crisis hiperglucémica; iniciar metformina + estilo de vida; SGLT2/GLP-1 si ECV, IC, ERC, obesidad.",
        "Prediabetes: dieta + ejercicio (-7% peso, 150 min/sem); metformina si IMC ≥35, ≥60 a, o DG previa.",
        "Hipercolesterolemia familiar: estatina alta intensidad + tamizar familia; cribar ECV temprana.",
        "Dislipidemia: ASCVD ≥7.5% considerar estatina; ≥20% alta intensidad; ECV establecida LDL objetivo &lt;55-70.",
        "HTA con A/Cr ≥30: IECA o ARA II + objetivo TA &lt;130/80; añadir iSGLT2 si DM con A/Cr &gt;200.",
        "Hipotiroidismo clínico: levotiroxina 1.6 µg/kg/día; subclínico tratar si síntomas, AntiTPO+, infertilidad, embarazo, TSH &gt;10.",
        "Anemia ferropénica: Fe oral 100-200 mg/día + buscar causa (sangrado oculto, dieta, malabsorción, ginecológico).",
        "ITU baja: nitrofurantoína 100 mg c/12 h × 5 d (1ª línea) o fosfomicina 3 g VO dosis única; cefalexina si embarazo.",
        "Sx metabólico: estilo de vida primero; tratar componentes individuales (HTA, DM, dislipidemia).",
        "Sinusitis bacteriana: amoxicilina 1 g c/8 h × 7-10 d o amoxi-clavulánico si reciente uso de ATB o &gt;65 a.",
        "Anemia inexplicada ≥50 a: colonoscopia + endoscopia alta; pensar siempre en neoplasia digestiva.",
        "Bacteriuria asintomática: solo tratar en embarazo, prequirúrgico urológico, transplante; en demás NO sobretratar.",
    ],
    "verbalizar parámetro + criterio + siguiente paso (siempre con ADA, USPSTF o ACC/AHA).",
    "tratas sin criterio confirmatorio o sobreusas ATB en bacteriuria asintomática.",
    "ADA 2025; USPSTF 2024-2025; ACC/AHA 2018 lipidos + 2017 HTA; KDIGO 2024; IDSA UTI 2010.",
    "medicina_familiar", "cheat",
)

make_cheat(
    "CHEAT SHEET · MI", "cs-mi",
    "Medicina Interna · Dx hospitalarios — estudio + parámetro disparador",
    [
        ("IAM / SICA", "Tn hs + ECG", "Tn rise/fall + supraST/depST + dolor torácico"),
        ("IC descompensada", "BNP/NT-proBNP + RxTx + ECG", "BNP &gt;400 + cardiomegalia + congestión + IVY"),
        ("EPOC reagudizada", "GA + RxTx + BH", "Acidosis respiratoria + hiperinflación + leucos ↑"),
        ("Sepsis / shock séptico", "BH + lactato + GA + HC", "qSOFA ≥2 + lactato &gt;2 (shock séptico ≥4) + leucos ↑/↓"),
        ("LRA (KDIGO)", "Cr · TFG · K · GA · sedimento", "Cr ↑×1.5 en 7d o ↑0.3 en 48h"),
        ("Cetoacidosis DM", "GA + glucosa + K + cetonas + AG", "pH &lt;7.3 + HCO3 &lt;18 + AG &gt;12 + glu &gt;250"),
        ("Estado hiperosmolar", "Glucosa + osm + Na", "Glu &gt;600 + osm &gt;320 + sin cetosis"),
        ("Hepatitis aguda viral o tóxica", "PFH + INR + BT + serologías", "AST/ALT &gt;1000 + ↑ BT + INR ↑"),
        ("Hiponatremia (SIADH)", "Na + osm sérica + osm urinaria + Na urinario", "Na &lt;135; osm sérica &lt;275; osm orina &gt;100; Na orina &gt;40"),
        ("Anemia macrocítica", "BH + B12 + folato + TSH", "VCM &gt;100 + B12 &lt;200"),
        ("TEP", "Wells + dímero D + angio-TC", "Wells ≥4 o dímero D ↑ → angio-TC"),
        ("FA con respuesta rápida", "ECG + TSH + ETT", "FA + FC &gt;110 + CHA₂DS₂-VASc ≥2 → anticoagulación"),
    ],
    [
        "IAM: doble antiagregación (AAS + ticagrelor/prasugrel) + heparina + reperfusión: ICP &lt;90 min, fibrinólisis &lt;30 min si no ICP.",
        "IC descompensada: diurético IV (furosemida 40 mg o doble dosis basal); IECA/ARNI; β-bloq cuando euvolémico; restricción sal/líquidos.",
        "EPOC reagudizada: broncodilatador inhalado (SABA + SAMA) + prednisona 40 mg × 5 d + ATB si purulenta (Anthonisen 2-3 criterios).",
        "Sepsis (Surviving Sepsis 2021 bundle 1h): cultivos antes de ATB + lactato + cristaloides 30 mL/kg + ATB amplio espectro + vasopresores si TAM &lt;65 tras volumen.",
        "LRA: KDIGO etapas 1-3; suspender nefrotóxicos (AINE, IECA/ARA si volumen contraído, contraste); restaurar volemia; diálisis si refractaria.",
        "DKA: insulina IV 0.1 U/kg/h + cristaloides + K cuando &lt;5.5 (incluso si normal); HCO3 solo si pH &lt;6.9.",
        "EHH: rehidratación priorizada (50% déficit 12 h, 50% 12 h siguientes); insulina IV cuando glucosa baja a 300; cuidado con corrección rápida de Na.",
        "Hepatitis fulminante (INR &gt;1.5 + encefalopatía): UCI + N-acetilcisteína si paracetamol + valorar trasplante.",
        "Hiponatremia hipotónica euvolémica = SIADH; restricción agua + tolvaptán; corregir &lt;10 mEq/24h (mielinolisis).",
        "Anemia macrocítica: B12 IM 1000 µg/día × 7 + semanal × 4 + mensual; folato 1-5 mg/día.",
        "TEP: anticoagulación inmediata si alta probabilidad; trombólisis si masivo (PA &lt;90) o submasivo con disfunción VD + Tn+.",
        "FA: control de frecuencia (β-bloq, BCC, digoxina); anticoagulación con CHA₂DS₂-VASc ≥2 (H) o ≥3 (M); DOAC preferido sobre warfarina.",
    ],
    "siempre cuantificar criterio (Tn, BNP, GA, AG) y vincular a conducta inmediata.",
    "tratas sin cuantificar o sin descartar TEP/sepsis cuando hay disnea+taquicardia.",
    "ACC/AHA + ESC; Surviving Sepsis 2021; KDIGO 2024; ADA 2025; AASLD 2024.",
    "medicina_interna", "cheat",
)

make_cheat(
    "CHEAT SHEET · CIRUGÍA", "cs-cx",
    "Cirugía General · Dx abdominal/trauma — estudio + parámetro disparador",
    [
        ("Apendicitis aguda", "BH + Alvarado + USG/TC", "Leucos &gt;12k + Alvarado ≥7 + apéndice &gt;6 mm no compresible"),
        ("Colecistitis aguda", "USG + BH + PFH", "Pared vesicular &gt;4 mm + Murphy ecográfico + leucos ↑"),
        ("Coledocolitiasis / colangitis", "USG + PFH + BH", "Colédoco &gt;7 mm + BD ↑ + Charcot (ictericia + fiebre + dolor)"),
        ("Pancreatitis aguda", "Lipasa + Atlanta + BISAP", "Lipasa ≥3× límite alto + 2/3 Atlanta"),
        ("Obstrucción intestinal", "Rx abdomen + TC", "Niveles + dilatación ID &gt;3 cm / colon &gt;6 cm"),
        ("Perforación víscera hueca", "Rx abdomen + TC", "Neumoperitoneo (aire libre subdiafragmático)"),
        ("Hemorragia digestiva alta", "BH + endoscopia urgente", "Hb ↓ + melena/hematemesis + úlcera/varices/Mallory-Weiss"),
        ("AAA roto", "USG + TC + Hb", "Aorta &gt;3 cm + líquido libre + hipotensión + ↓Hb"),
        ("Trauma abdominal contuso", "FAST + Hb + lactato", "Líquido libre + ↓Hb + lactato ↑ + inestabilidad"),
        ("Neumotórax a tensión", "Clínica + RxTx", "Desplazamiento traqueal + ↓ ruidos + timpanismo → descomprimir SIN esperar Rx"),
        ("Hemotórax masivo", "RxTx + tubo torácico", "&gt;1500 mL inicial o &gt;200 mL/h × 4 h"),
        ("Shock hipovolémico clase III-IV", "Lactato + GA + Hb + BE", "Pérdida &gt;30% + lactato &gt;4 + BE &lt;−6"),
    ],
    [
        "Apendicitis: cirugía urgente (laparoscopia preferida); ATB pre-op (cefoxitin o piperazilina/tazobactam).",
        "Colecistitis: TG24 clasifica grados I-III; colecistectomía precoz mismo ingreso si I-II; III en UCI antes.",
        "Colangitis (Tokyo): triada Charcot o pentada Reynolds; ATB amplio espectro + drenaje urgente (CPRE).",
        "Pancreatitis severa = UCI + reposición agresiva (lactato Ringer 250-500 mL/h primeras 24 h); no ATB profiláctico.",
        "Obstrucción mecánica + estrangulación (peritonismo, fiebre, leucos, acidosis) = quirófano.",
        "Perforación: laparotomía urgente + ATB amplio espectro + control del foco.",
        "HD alta: endoscopia &lt;24 h; var ices → octreótido + ligadura + ATB profiláctico SBP; úlcera Forrest Ia-IIb → hemostasia.",
        "AAA roto: reparación endovascular emergente; FAST + TC si estable; protocolo de transfusión masiva.",
        "Trauma + FAST+ + inestable = laparotomía exploradora; FAST+ + estable = TC.",
        "Neumotórax a tensión: descomprimir 2EIC LMC o 4-5 EIC LMA con angiocatéter ≥14G; después tubo torácico.",
        "Hemotórax masivo: tubo torácico 28-32 Fr; toracotomía si &gt;1500 mL inicial.",
        "Shock hipovolémico: transfusión masiva 1:1:1 (plasma:plaquetas:eritrocitos) + control del foco + ácido tranexámico &lt;3 h.",
    ],
    "verbalizar el dx con criterio cuantitativo y plan quirúrgico inmediato.",
    "demoras laparotomía en FAST+ con inestabilidad, o tratas pancreatitis sin reanimar.",
    "ATLS 10ª; TG24; Atlanta revisada; Surviving Sepsis 2021; CRASH-2.",
    "cirugia", "cheat",
)

make_cheat(
    "CHEAT SHEET · PEDIATRÍA", "cs-ped",
    "Pediatría · Dx por edad — estudio + parámetro disparador",
    [
        ("Sepsis neonatal", "BH + PCR + HC + LCR + EGO", "Leucos &lt;5k o &gt;20k + PCR ↑ + plaquetas ↓"),
        ("NAC pediátrica", "RxTx + BH + PCR", "Consolidación lobar + leucos ↑ + PCR ↑"),
        ("Bronquiolitis VSR", "Clínica + saturación", "Hiperinflación + sibilancias + ↓SatO₂; sin consolidación"),
        ("Anemia ferropénica del lactante", "BH + ferritina + TSAT", "Hb &lt;11 + VCM &lt;70 + ferritina &lt;12"),
        ("LLA pediátrica", "BH + frotis", "Pancitopenia o blastos + visceromegalia + adenopatías"),
        ("Crisis febril simple", "Clínica + glucosa + electrolitos", "&lt;15 min, generalizada, 6 m-5 a, sin foco neurológico"),
        ("Hipotiroidismo congénito", "Tamiz neonatal TSH", "TSH neonatal &gt;30 mUI/L"),
        ("GEA con deshidratación", "Electrolitos + GA + BUN", "Acidosis met + hipoK + hipoNa + ↑BUN"),
        ("ITU pediátrica", "EGO + urocultivo", "Leucos+ + nitritos+ + urocultivo ≥10⁵ (vejiga)"),
        ("Estenosis pilórica", "USG abdomen + electrolitos", "Pared píloro &gt;3 mm + longitud &gt;15 mm + alcalosis hipoclorémica"),
        ("Invaginación intestinal", "USG abdomen", "Signo del donut / pseudoriñón + heces en jalea de grosella"),
        ("Maltrato infantil físico", "Rx esquelético + fondo de ojo + BH/PFH", "Fracturas múltiples en distintas etapas; hematoma retiniano (sx del niño sacudido)"),
    ],
    [
        "Sepsis neonatal: ampicilina + gentamicina IV; meningitis añadir cefotaxima; reevaluar a las 36-48 h con cultivos.",
        "NAC pediátrica: amoxicilina alta dosis 90 mg/kg/día × 7-10 d (típica); azitromicina si atípica adolescente.",
        "Bronquiolitis VSR: oxígeno + hidratación + SF nasal; NO broncodilatador ni esteroide rutinario.",
        "Anemia ferropénica lactante: Fe oral 3-6 mg/kg/día × 3-6 meses; mejorar dieta (carne, cereales fortificados, citricos con Fe).",
        "LLA: derivar hematología urgente (médula ósea); tratamiento intensivo multifásico; tasa de curación 85-90%.",
        "Crisis febril simple: no requiere EEG ni neuroimagen; manejo de fiebre (paracetamol/ibuprofeno); educar familia.",
        "Hipotiroidismo congénito: levotiroxina 10-15 µg/kg/día &lt;14 d post nacimiento previene retraso mental.",
        "GEA + deshidratación: SRO si leve-moderada (50-100 mL/kg en 4 h); IV con SF si severa (20 mL/kg bolos).",
        "ITU pediátrica: ATB según urocultivo; cefalexina/cefuroxima 7-10 d en mayor; cefotaxima IV si &lt;2 m o sepsis; USG renal 1ª ITU &lt;2 a.",
        "Estenosis pilórica: pyloromiotomía Ramstedt post-corrección hidroelectrolítica.",
        "Invaginación: reducción hidrostática con enema (USG o fluoroscopia); cirugía si falla o necrosis intestinal.",
        "Maltrato: denuncia legal obligatoria + Rx esquelético en &lt;2 a + valorar fondo de ojo (sx del niño sacudido).",
    ],
    "ajustar dosis y rangos de referencia siempre por edad y peso; no copiar adulto.",
    "usas rangos adulto en niño, o no haces denuncia legal en maltrato.",
    "AAP Bright Futures 2022; NOM-007-SSA2-2016; OMS; Red Book AAP 2024.",
    "pediatria", "cheat",
)

make_cheat(
    "CHEAT SHEET · PSIQUIATRÍA", "cs-psiq",
    "Psiquiatría · Descartar orgánico + monitoreo psicofármaco — estudio + parámetro",
    [
        ("Hipotiroidismo simulando depresión", "TSH · T4L", "TSH &gt;10 + T4L ↓"),
        ("Hipertiroidismo simulando manía/ansiedad", "TSH · T4L · T3", "TSH ↓ + T4L/T3 ↑"),
        ("Anemia (fatiga, depresión)", "BH + ferritina + B12", "Hb ↓ → caracterizar VCM"),
        ("Hiponatremia (confusión, agitación)", "Na sérico + osm", "Na &lt;130; SIADH por ISRS, oxcarbazepina, CBZ"),
        ("Intoxicación alcohólica/abstinencia", "Alcoholemia + GA + glucosa + electrolitos", "Alcoholemia &gt;300 = riesgo coma; CIWA &gt;15 = severa"),
        ("Drogas en orina", "TIRA tóxicos", "Detecta cocaína, opioides, BZD, THC, anfetaminas (positiva)"),
        ("Intoxicación por litio", "Litio sérico (12 h post-dosis)", "&gt;1.5 mEq/L tóxico, &gt;2.5 severa"),
        ("Intoxicación por VPA + hiperamonemia", "VPA sérico + amonio", "VPA &gt;100 µg/mL + amonio ↑ + alteración mental"),
        ("Intoxicación por CBZ", "CBZ sérico", "&gt;12 µg/mL tóxico"),
        ("Agranulocitosis por clozapina", "BH semanal (neutros)", "Neutros &lt;1500 = stop; &lt;1000 nunca reintroducir"),
        ("Síndrome metabólico por antipsicótico", "Glucosa, lípidos, perímetro, peso", "3/5 criterios ATP III"),
        ("Sx neuroléptico maligno", "CK + Tn + leucos + creatinina + amonio", "Fiebre + rigidez + AMS + CK ↑↑↑"),
        ("Sx serotoninérgico", "Clínica + tóxicos", "Hipertermia + hiperreflexia + clonus + agitación (post-ISRS+tramadol/triptanes)"),
        ("Pre-clozapina (descartar miocarditis)", "Tn + CK + ECG primeras 4 sem", "Tn ↑ inexplicada → suspender"),
    ],
    [
        "Hipotiroidismo: levotiroxina ANTES de antidepresivo si TSH &gt;10 + síntomas.",
        "Hipertiroidismo: β-bloq inmediato + metimazol; antipsicótico contraindicado puro hasta controlar.",
        "Anemia: tratar causa antes de antidepresivo (en anemia ferropénica, mejorar Fe puede revertir 'depresión').",
        "Hiponatremia &lt;130 sintomática: suspender psicofármaco causante + corregir &lt;10 mEq/24h (mielinolisis).",
        "Alcoholismo: CIWA + BZD (lorazepam o diazepam) escalonado + tiamina ANTES de glucosa (Wernicke).",
        "Drogas en orina: confirma uso; intoxicación aguda requiere manejo específico (naloxona para opioides, flumazenil para BZD).",
        "Litio tóxico: suspender + suero fisiológico + hemodiálisis si &gt;2.5 o sintomático severo.",
        "VPA hiperamonemia: suspender + L-carnitina + lactulosa; tratar similar a encefalopatía hepática.",
        "CBZ tóxico: suspender + carbón activado si &lt;1 h post ingesta; soporte UCI si severo.",
        "Clozapina agranulocitosis: stop inmediato + neutropenia febril (cefepima + filgrastim si severa).",
        "Sx metabólico por antipsicótico: cambiar a quetiapina/aripiprazol (menor riesgo) + dieta + ejercicio + estatina/metformina.",
        "NMS: suspender antipsicótico + bromocriptina o dantroleno + refrigerar + UCI + hidratar (riesgo IRA por rabdomiolisis).",
        "Sx serotoninérgico: suspender ISRS + ciproheptadina + soporte (BZD si agitación); diferencial con NMS (clonus + hiperreflexia favorecen serotoninérgico).",
        "Miocarditis por clozapina: si Tn ↑ en primeras 4 sem suspender INMEDIATO; ETT + cardio.",
    ],
    "siempre tamizar BH + QS + PFH + TSH + ECG + β-hCG basal antes de iniciar psicofármaco.",
    "tratas síntomas psiquiátricos sin descartar orgánico o no monitorizas niveles séricos.",
    "APA Practice Guidelines; Maudsley 14th ed; UpToDate; ACOG (embarazo).",
    "psiquiatria", "cheat",
)

make_cheat(
    "CHEAT SHEET · GINECO-OBSTETRICIA", "cs-gyo",
    "GyO · Dx embarazo + ginecológicos — estudio + parámetro disparador",
    [
        ("Embarazo confirmado", "β-hCG cuantitativa", "≥5 mUI/mL"),
        ("Embarazo ectópico", "β-hCG + USG TV", "β-hCG &gt;1500-2000 sin saco IU"),
        ("Aborto incompleto", "USG TV + β-hCG", "Restos endometriales &gt;15 mm + ↓ β-hCG"),
        ("Mola hidatiforme", "β-hCG + USG", "β-hCG &gt;100,000 + útero mayor + USG en tormenta de nieve"),
        ("Diabetes gestacional", "CTOG 75 g 24-28 SDG (IADPSG)", "≥92 ayuno o ≥180 1h o ≥153 2h"),
        ("Preeclampsia", "TA + proteinuria + PFH + plaquetas + Cr", "TA ≥140/90 ×2 + proteinuria ≥300 mg/24h o A/Cr ≥0.3"),
        ("Eclampsia / preeclampsia severa", "Clínica + PFH + plaquetas + Cr + ácido úrico", "Convulsiones tónico-clónicas / TA ≥160/110 + síntomas o disfunción orgánica"),
        ("HELLP", "BH + PFH + DHL + frotis", "Plaquetas &lt;100k + AST/ALT ↑ + DHL &gt;600 + esquistocitos"),
        ("Anemia gestacional", "BH", "Hb &lt;11 (1T/3T), &lt;10.5 (2T)"),
        ("Iso-inmunización Rh", "Coombs indirecto + GS-Rh", "Anti-D ↑ titulación"),
        ("Bacteriuria asintomática / ITU en embarazo", "EGO + urocultivo", "Urocultivo ≥10⁵ (siempre tratar)"),
        ("Aneuploidía 1T", "Combinado: TN + PAPP-A + β-hCG libre", "Riesgo &gt;1/270 o TN &gt;3 mm"),
        ("RCIU", "USG 3T: PFE + Doppler + ILA", "PFE &lt;p10 + IP AU &gt;p95 / flujo ausente o reverso"),
        ("Parto pretérmino amenazado", "Cervicometría + fibronectina + clínica", "LC &lt;25 mm + contracciones regulares"),
        ("Sufrimiento fetal anteparto", "NST + PBF", "NST no reactivo + PBF ≤4/10"),
    ],
    [
        "Embarazo confirmado: USG TV para datar y descartar ectópico; iniciar control prenatal.",
        "Ectópico: metotrexate (criterios: estable, β-hCG &lt;5000, masa &lt;3.5 cm, sin LCF); cirugía si roto/inestable o falla MTX.",
        "Aborto incompleto: AMEU + Ig anti-D si Rh−; descartar mola con histopatología.",
        "Mola: evacuación + control β-hCG semanal hasta negativizar + mensual × 6 m; anticoncepción durante seguimiento.",
        "DG: nutrición + ejercicio + autovigilancia 4×/día; insulina si falla en 1-2 sem (metformina alternativa).",
        "Preeclampsia: AAS 100-150 mg desde 12 SDG en embarazo siguiente; tratamiento agudo con labetalol/hidralazina + sulfato Mg neuroprotección.",
        "Eclampsia: sulfato Mg 4-6 g IV bolo + 2 g/h mantenimiento; control crisis + interrupción del embarazo independiente SDG.",
        "HELLP: interrumpir embarazo + sulfato Mg + transfusión plaquetas si &lt;50k para parto/cesárea.",
        "Anemia gestacional: Fe oral 60-120 mg/día + folato 0.4-5 mg; Fe IV si severa o intolerancia oral.",
        "Iso-inmunización Rh: Ig anti-D 300 µg IM a las 28 SDG + dentro de 72 h post-parto si RN Rh+.",
        "Bacteriuria asintomática SIEMPRE tratar en embarazo (cefalexina, fosfomicina, amoxicilina); urocultivo de control.",
        "Aneuploidía: NIPT (alta sensibilidad) o amniocentesis (15-18 SDG) confirmatoria; consejo genético.",
        "RCIU + Doppler ausente o reverso: interrumpir según SDG (≥32-34 SDG + maduración pulmonar).",
        "Parto pretérmino: tocolisis (atosibán o nifedipino 48 h) + corticoide (betametasona 12 mg ×2) + sulfato Mg si &lt;32 SDG (neuroprotección).",
        "Sufrimiento fetal: interrumpir si maduro; vigilar y considerar maduración pulmonar si pretérmino.",
    ],
    "siempre cuantificar (β-hCG, Hb, percentil PFE, IP Doppler) y vincular a plan obstétrico claro.",
    "no cuantificas hallazgos o no aplicas profilaxis (Ig anti-D, AAS preeclampsia, sulfato Mg).",
    "ACOG; Williams Obstetrics 26ª; ISUOG; NOM-007-SSA2-2016; USPSTF; IADPSG.",
    "gineco", "cheat",
)


# ============================================================
# GENERAR .APKG
# ============================================================
if __name__ == "__main__":
    output_path = os.path.join(
        OUTPUT_DIR,
        "Preparacion_Verbalizada_Deck4_Estudios_Basicos.apkg",
    )
    genanki.Package(deck).write_to_file(output_path)
    print(f"✓ Generado: {output_path}")
    print(f"  Total notas: {len(deck.notes)}")
    print(f"  Deck ID: {DECK_ID}")
    print(f"  Deck name: {DECK_NAME}")
