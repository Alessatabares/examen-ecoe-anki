#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Guion ECOE (mínimo) — Crisis hipertensiva (URGENCIA) + síndrome metabólico + DM2 + hígado graso.
4 tarjetas. Eje: distinguir urgencia de emergencia (daño AGUDO a órgano blanco) + manejo integral.
Guion verbalizado completo en scripts/guion-hta-sindrome-metabolico.md.
"""
import os
import genanki

MODEL_ID = 1607392319  # cloze_estandar
DECK_ID = 1990012014
OUT = os.path.join(os.path.dirname(__file__), "output")

model = genanki.Model(
    MODEL_ID, "Estudio Médico Cloze",
    fields=[{"name": "Text"}, {"name": "Extra"}],
    templates=[{"name": "Cloze", "qfmt": "{{cloze:Text}}",
                "afmt": '{{cloze:Text}}<hr id="extra">{{Extra}}'}],
    css="""
    .card {
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      font-size: 19px; text-align: left; color: #1a1a1a;
      background-color: #fafafa; padding: 20px; line-height: 1.5;
    }
    .cloze { font-weight: 600; color: #2563eb; }
    #extra { margin-top: 16px; border: none; border-top: 1px solid #d4d4d4; }
    """,
    model_type=genanki.Model.CLOZE,
)
TAGS = ["ecoe", "guion", "medicina-interna", "hipertension", "diabetes", "sindrome-metabolico", "higado-graso"]
deck = genanki.Deck(DECK_ID, "Guiones ECOE::Crisis HTA + sindrome metabolico + DM2 + higado graso")


def note(text, extra=""):
    deck.add_note(genanki.Note(model=model, fields=[text.strip(), extra.strip()], tags=TAGS))


note(
    "❤️ [Interrogatorio + exploración] Ante crisis HTA, lo PRIMERO es buscar daño AGUDO a órgano blanco: "
    "{{c1::neuro (cefalea intensa, déficit, confusión, convulsión), tórax (dolor, disnea/edema agudo pulmonar), "
    "dolor desgarrante a la espalda (disección), visión, oliguria}}. Antecedentes metabólicos: "
    "{{c2::peso, glucosa, alcohol, adherencia al antihipertensivo, tabaco, familiares}}. Exploración: "
    "{{c3::TA en ambos brazos, IMC y perímetro abdominal, fondo de ojo, cardiopulmonar, abdomen (hepatomegalia), "
    "edema, neuro}}.",
    "Caso: 52 a, TA 208/118, cefalea leve, SIN dolor torácico/déficit/disnea. IMC 33, perímetro 108.",
)
note(
    "❤️ [Dx — la distinción que reprueba si fallas] Crisis HTA = TA ≥180/120. "
    "{{c1::URGENCIA = SIN daño agudo a órgano blanco → tratamiento oral, gradual}}; "
    "{{c2::EMERGENCIA = CON daño agudo (encefalopatía, EVC, IAM, edema agudo pulmonar, disección, LRA, eclampsia) "
    "→ IV en monitorización, bajar solo 10–20% la 1ª hora}}. "
    "Dx coexistentes: {{c3::síndrome metabólico, DM2 de novo, hígado graso (MASLD)}}.",
    "🗣️ «La HVI y la microalbuminuria son daño CRÓNICO, no agudo → es urgencia, no emergencia.» "
    "Sx metabólico = ≥3 de: perímetro ♂≥90/♀≥80, TG≥150, HDL ♂&lt;40/♀&lt;50, TA≥130/85, glucosa≥100.",
)
note(
    "❤️ [Estudios + interpretación] Daño a órgano blanco: {{c1::ECG (HVI/isquemia), creatinina/TFG, "
    "EGO (proteinuria/albuminuria), fondo de ojo; troponina/Rx solo si dolor torácico o disnea}}. "
    "Metabólico: {{c2::glucosa ayuno + HbA1c, perfil de lípidos}}. "
    "Hígado: {{c3::AST/ALT/FA/GGT + USG; ALT>AST = MASLD, AST/ALT>2 = alcohólico (De Ritis)}}.",
    "Caso: HbA1c 8.2% (DM2), TG 240/HDL 34, ALT 78 > AST 55, USG hígado graso, EGO microalbuminuria, "
    "ECG HVI sin isquemia → confirma urgencia (daño crónico, no agudo).",
)
note(
    "❤️ [Plan integral + errores críticos] TA: {{c1::urgencia → oral, bajar gradual en horas-días "
    "(NO bruscamente, NO nifedipino sublingual); IECA/ARA II en diabético con albuminuria}}. "
    "Crónico: {{c2::metformina (meta HbA1c <7%), TA <130/80, estatina, pérdida de peso 7–10%, abstinencia de alcohol}}. "
    "NO: {{c3::bajar TA brusca, no distinguir urgencia/emergencia, no buscar daño a órgano blanco, "
    "ignorar alcohol y los demás componentes}}.",
    "Considerar SGLT2i/GLP-1 por beneficio cardiorrenal. Tamizar: fondo de ojo, albuminuria, pies, ECG. "
    "MASLD: el tratamiento es metabólico (no hay pastilla mágica).",
)

os.makedirs(OUT, exist_ok=True)
out_path = os.path.join(OUT, "Guiones_ECOE_HTA_Sindrome_Metabolico.apkg")
genanki.Package([deck]).write_to_file(out_path)
print(f"OK -> {out_path}")
print(f"  Crisis HTA + sx metabólico: {len(deck.notes)} notas (deck {DECK_ID})")
