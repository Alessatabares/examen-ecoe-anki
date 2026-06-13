"""Builder de los decks EJE CLINICO (por sintoma) - formato Capa 6 de gine.

Front: eje sintomatico + lista numerada de presentaciones.
Back:  la misma lista con el dx mas probable de cada presentacion.
Lee data_eje_clinico.EJE_CLINICO y emite un .apkg por sistema presente.
"""
import os
import sys
import genanki

sys.path.insert(0, os.path.dirname(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _common import MODEL_QA_ID, PADRE, SYSTEMS, deck_id
from data_eje_clinico import EJE_CLINICO

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "output")
os.makedirs(OUTPUT_DIR, exist_ok=True)

CSS = """
.card { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  font-size: 18px; text-align: left; color: #1a1a1a; background-color: #fafafa;
  padding: 20px; line-height: 1.55; }
.eje { display: inline-block; padding: 5px 14px; margin-bottom: 14px;
  background: #7c2d12; color: #fff; border-radius: 6px; font-size: 13px;
  letter-spacing: 0.8px; font-weight: 700; text-transform: uppercase; }
.prompt { color: #2563eb; font-weight: 600; margin: 8px 0 12px 0; }
ol.pres { margin: 4px 0 0 0; padding-left: 28px; }
ol.pres li { margin: 8px 0; }
ol.dx { margin: 4px 0 0 0; padding-left: 28px; }
ol.dx li { margin: 8px 0; font-weight: 700; color: #047857; }
#extra { margin-top: 16px; border: none; border-top: 1px solid #d4d4d4; padding-top: 12px; }
"""

model_qa = genanki.Model(
    MODEL_QA_ID, "Estudio Medico QA",
    fields=[{"name": "Front"}, {"name": "Back"}],
    templates=[{"name": "QA", "qfmt": "{{Front}}",
                "afmt": '{{Front}}<hr id="extra">{{Back}}'}],
    css=CSS,
)


def make_note(eje, items, base_tags, guid):
    front = (
        f'<div class="eje">EJE: {eje}</div>'
        '<div class="prompt">&iquest;Dx m&aacute;s probable seg&uacute;n presentaci&oacute;n?</div>'
        '<ol class="pres">' + "".join(f"<li>{p}</li>" for p, _ in items) + "</ol>"
    )
    back = '<ol class="dx">' + "".join(f"<li>{d}</li>" for _, d in items) + "</ol>"
    # GUID estable por posicion (no por contenido): reimportar tras corregir
    # texto ACTUALIZA la carta en su sitio, nunca duplica.
    return genanki.Note(model=model_qa, fields=[front, back], tags=base_tags, guid=guid)


def build():
    total = 0
    for data_name, short, slug, tag, idx in SYSTEMS:
        sysdata = EJE_CLINICO.get(data_name)
        if not sysdata:
            continue
        deck = genanki.Deck(deck_id(idx, 1), f"{PADRE}::{short}::Eje Clinico")
        base_tags = ["ejes_diagnosticos", "topografico", "eje_clinico", "ecoe", tag]
        for ei, (eje, items) in enumerate(sysdata["ejes"]):
            guid = genanki.guid_for(f"topoclin:ec:{idx}:{ei}")
            deck.add_note(make_note(eje, items, base_tags, guid))
        out = os.path.join(OUTPUT_DIR, f"Topografico_{slug}_EjeClinico.apkg")
        genanki.Package(deck).write_to_file(out)
        print(f"OK: {os.path.basename(out)}  ({len(deck.notes)} notas)")
        total += 1
    print(f"--- {total} decks Eje Clinico generados ---")


if __name__ == "__main__":
    build()
