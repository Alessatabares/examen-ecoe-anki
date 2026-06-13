"""Builder de los decks INTEGRADOR (por hallazgo en la exploracion) - formato Capa 5 de gine.

Front: estacion/maniobra de exploracion + 3 discriminadores clinicos.
Back:  diagnostico + tip ECOE verbalizable.
Lee data_integrador.INTEGRADOR y emite un .apkg por sistema presente.
"""
import os
import sys
import genanki

sys.path.insert(0, os.path.dirname(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _common import MODEL_QA_ID, PADRE, SYSTEMS, deck_id
from data_integrador import INTEGRADOR

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "output")
os.makedirs(OUTPUT_DIR, exist_ok=True)

CSS = """
.card { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  font-size: 19px; text-align: left; color: #1a1a1a; background-color: #fafafa;
  padding: 20px; line-height: 1.55; }
.loc { display: inline-block; padding: 4px 12px; margin-bottom: 14px;
  background: #1e3a8a; color: #fff; border-radius: 6px; font-size: 14px;
  letter-spacing: 0.5px; font-weight: 600; }
ul.disc { margin: 8px 0 18px 0; padding-left: 22px; }
ul.disc li { margin: 6px 0; }
.prompt { color: #2563eb; font-weight: 600; margin-top: 10px; }
.dx { font-size: 22px; font-weight: 700; color: #047857; margin-top: 4px; }
.ecoe { color: #b45309; font-style: italic; margin-top: 12px; display: block; }
#extra { margin-top: 16px; border: none; border-top: 1px solid #d4d4d4; padding-top: 12px; }
"""

model_qa = genanki.Model(
    MODEL_QA_ID, "Estudio Medico QA",
    fields=[{"name": "Front"}, {"name": "Back"}],
    templates=[{"name": "QA", "qfmt": "{{Front}}",
                "afmt": '{{Front}}<hr id="extra">{{Back}}'}],
    css=CSS,
)


def make_note(loc, d1, d2, d3, dx, ecoe, base_tags, guid):
    front = (
        f'<div class="loc">{loc}</div>'
        f'<ul class="disc"><li>{d1}</li><li>{d2}</li><li>{d3}</li></ul>'
        '<div class="prompt">&iquest;Diagn&oacute;stico?</div>'
    )
    back = f'<div class="dx">{dx}</div><span class="ecoe">ECOE: &laquo;{ecoe}&raquo;</span>'
    # GUID estable por posicion (no por contenido): reimportar tras corregir
    # texto ACTUALIZA la carta en su sitio, nunca duplica.
    return genanki.Note(model=model_qa, fields=[front, back], tags=base_tags, guid=guid)


def build():
    total = 0
    for data_name, short, slug, tag, idx in SYSTEMS:
        sysdata = INTEGRADOR.get(data_name)
        if not sysdata:
            continue
        deck = genanki.Deck(deck_id(idx, 2), f"{PADRE}::{short}::Integrador")
        base_tags = ["ejes_diagnosticos", "topografico", "integrador", "ecoe", tag]
        for si, (loc, rows) in enumerate(sysdata["estaciones"]):
            for ri, (d1, d2, d3, dx, ecoe) in enumerate(rows):
                guid = genanki.guid_for(f"topoclin:int:{idx}:{si}:{ri}")
                deck.add_note(make_note(loc, d1, d2, d3, dx, ecoe, base_tags, guid))
        out = os.path.join(OUTPUT_DIR, f"Topografico_{slug}_Integrador.apkg")
        genanki.Package(deck).write_to_file(out)
        print(f"OK: {os.path.basename(out)}  ({len(deck.notes)} notas)")
        total += 1
    print(f"--- {total} decks Integrador generados ---")


if __name__ == "__main__":
    build()
