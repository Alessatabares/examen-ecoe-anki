"""Metadatos compartidos para los decks Topografico -> Clinico.

Cada uno de los 19 sistemas del Eje 01 Topografico genera DOS decks:
  - Eje Clinico  (por sintoma de presentacion)   -> formato Capa 6 de gine
  - Integrador   (por hallazgo en la exploracion) -> formato Capa 5 de gine

Esquema de deck_id: 1300_SS_C
  SS = indice del sistema (01-19)
  C  = 1 (Eje Clinico) | 2 (Integrador)
Rango valido [1<<30, 1<<31); sin colision con los topograficos (1290xxxxxxx).
"""

MODEL_QA_ID = 1607392320  # qa_estandar (reusable, ver ids.json)
PADRE = "Ejes Diagnosticos Adulto::Topografico"

# (nombre_en_data, nombre_corto_para_deck, slug_archivo, tag, idx)
SYSTEMS = [
    ("Pulmon / Respiratorio",        "Pulmon",            "Pulmon",            "pulmon",             1),
    ("Corazon",                      "Corazon",           "Corazon",           "corazon",            2),
    ("Higado / Biliar / Pancreas",   "Higado-Biliar",     "Higado",            "higado",             3),
    ("Intestino",                    "Intestino",         "Intestino",         "intestino",          4),
    ("Rinon / Urinario",             "Rinon-Urinario",    "Rinon",             "rinon",              5),
    ("Cerebro / SNC",                "SNC",               "SNC",               "cerebro",            6),
    ("Ojo",                          "Ojo",               "Ojo",               "ojo",                7),
    ("Oido",                         "Oido",              "Oido",              "oido",               8),
    ("Endocrino / Suprarrenal",      "Endocrino",         "Endocrino",         "endocrino",          9),
    ("Ap. reproductor femenino",     "Reproductor Fem",   "ReproFem",          "repro_fem",         10),
    ("Ap. reproductor masculino",    "Reproductor Masc",  "ReproMasc",         "repro_masc",        11),
    ("Cabeza / Craneofacial",        "Cabeza",            "Cabeza",            "cabeza",            12),
    ("Musculoesqueletico",           "Musculoesqueletico","Musculoesqueletico","musculoesqueletico",13),
    ("Piel",                         "Piel",              "Piel",              "piel",              14),
    ("Sangre / Hematologico",        "Sangre",            "Sangre",            "sangre",            15),
    ("Nariz / Garganta / Cuello",    "ORL / Cuello",      "ORL_Cuello",        "orl_cuello",        16),
    ("Boca / Dental",                "Boca",              "Boca",              "boca",              17),
    ("Vascular periferico",          "Vascular Perif",    "VascularPerif",     "vascular_perif",    18),
    ("Inmune",                       "Inmune",            "Inmune",            "inmune",            19),
]


def deck_id(idx, fmt):
    """fmt: 1 = Eje Clinico, 2 = Integrador."""
    return 1300000000 + idx * 1000 + fmt
