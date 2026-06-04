"""No hay tiempo / Obstetricia — PILAR EXPLORACION + ESTUDIOS.

A) DISCRIMINADOR: una herramienta separa un grupo por un hallazgo (por herramienta).
B) PANEL/workup: una enfermedad pide una bateria con rol de cada estudio (por enfermedad).
Guia: GPC mexicanas + ACOG + Williams.
"""
import os
import genanki

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "output")
os.makedirs(OUTPUT_DIR, exist_ok=True)

MODEL_QA_ID = 1990004003
DECK_ID_D, DECK_ID_P, DECK_ID_M = 1990003021, 1990003022, 1990003023
DECK_NAME_D = "No hay tiempo::Obstetricia::Estudios::1 - Discriminadores (herramienta)"
DECK_NAME_P = "No hay tiempo::Obstetricia::Estudios::2 - Paneles (por enfermedad)"
DECK_NAME_M = "No hay tiempo::Obstetricia::Estudios::3 - Menos preguntados"

CSS_BASE = """
.card { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  font-size: 19px; text-align: left; color: #1a1a1a; background-color: #fafafa;
  padding: 20px; line-height: 1.5; }
.caso { font-size: 21px; font-weight: 700; color: #1e3a8a; }
#extra { margin-top: 16px; border: none; border-top: 1px solid #d4d4d4; padding-top: 12px; }
.bloque { display: block; margin: 12px 0; padding: 10px 14px; border-radius: 8px; }
.lab { display: block; font-size: 13px; font-weight: 700; letter-spacing: .5px;
  text-transform: uppercase; margin-bottom: 4px; }
.paraque { background: #eef2ff; border-left: 4px solid #1e3a8a; }
.trampa { background: #fef2f2; border-left: 4px solid #b91c1c; }
.pido { background: #eef2ff; border-left: 4px solid #1e3a8a; }
.descarto { background: #fff7ed; border-left: 4px solid #b45309; }
.clave { background: #ecfdf5; border-left: 4px solid #047857; }
.paraque .lab { color: #1e3a8a; } .trampa .lab { color: #b91c1c; }
.pido .lab { color: #1e3a8a; } .descarto .lab { color: #b45309; } .clave .lab { color: #047857; }
table.disc { border-collapse: collapse; width: 100%; margin: 6px 0 4px 0; font-size: 17px; }
table.disc td { border-bottom: 1px solid #e5e7eb; padding: 7px 8px; vertical-align: top; }
table.disc td.dx { font-weight: 700; color: #065f46; white-space: nowrap; }
b { color: #111; }
"""
model_qa = genanki.Model(MODEL_QA_ID, "NHT Obst Estudios QA",
    fields=[{"name": "Front"}, {"name": "Back"}],
    templates=[{"name": "QA", "qfmt": "{{Front}}", "afmt": '{{Front}}<hr id="extra">{{Back}}'}],
    css=CSS_BASE)

deck_d = genanki.Deck(DECK_ID_D, DECK_NAME_D)
deck_p = genanki.Deck(DECK_ID_P, DECK_NAME_P)
deck_m = genanki.Deck(DECK_ID_M, DECK_NAME_M)
BASE_TAGS = ["obstetricia", "ecoe", "no_hay_tiempo", "estudios"]


def add(deck, front, back, tags):
    deck.add_note(genanki.Note(model=model_qa, fields=[front, back], tags=BASE_TAGS + tags))

def caso(t): return f'<span class="caso">{t}</span>'

def disc(pq, filas, tr):
    rows = "".join(f'<tr><td>{h}</td><td class="dx">{d}</td></tr>' for h, d in filas)
    return (f'<span class="bloque paraque"><span class="lab">Para que lo pido</span>{pq}</span>'
            f'<table class="disc">{rows}</table>'
            f'<span class="bloque trampa"><span class="lab">Trampa</span>{tr}</span>')

def panel(pido, des, clave):
    return (f'<span class="bloque pido"><span class="lab">Pido (bateria + para que)</span>{pido}</span>'
            f'<span class="bloque descarto"><span class="lab">Descarto / vigilo</span>{des}</span>'
            f'<span class="bloque clave"><span class="lab">Clave / criterio</span>{clave}</span>')


# ===================== DISCRIMINADORES (8) =====================
D = ["discriminador"]
add(deck_d, caso("USG del 1er trimestre"),
    disc("Confirmar embarazo intrauterino, viabilidad y descartar ectopico/mola.",
         [("<b>Saco intrauterino + embrion con LCF</b>", "Embarazo viable"),
          ("<b>Utero vacio</b> con beta-hCG &gt;1500-2000 (zona discriminatoria)", "Sospecha de ectopico"),
          ("Masa anexial / anillo tubario, liquido libre", "Ectopico"),
          ("Imagen en <b>copos de nieve / panal</b>, sin embrion, quistes tecaluteinicos", "Mola"),
          ("Saco sin embrion (&gt;25 mm) o embrion sin LCF", "Aborto diferido")],
         "beta-hCG &gt;2000 + utero vacio = ectopico hasta demostrar lo contrario."),
    D + ["usg_1t"])

add(deck_d, caso("USG del 3er trimestre / localizacion placentaria"),
    disc("Ubicar la placenta y buscar hematoma ante sangrado del 3T.",
         [("<b>Placenta cubre orificio cervical interno</b>", "Placenta previa"),
          ("<b>Hematoma retroplacentario</b> (USG normal NO lo excluye)", "DPPNI"),
          ("Placenta con lagunas/perdida de plano + cesarea previa", "Acretismo placentario"),
          ("ILA bajo (oligohidramnios)", "RPM / insuficiencia placentaria")],
         "El USG es poco sensible para DPPNI: es dx <b>clinico</b>; no lo descartes por USG normal."),
    D + ["usg_3t"])

add(deck_d, caso("Cardiotocografia (RCTG) — categorias"),
    disc("Valorar el bienestar fetal por la FCF y su relacion con contracciones.",
         [("FCF 110-160, variabilidad 6-25, sin desaceleraciones patologicas", "Categoria I (normal)"),
          ("Hallazgos intermedios (no I ni III)", "Categoria II (indeterminado)"),
          ("<b>Variabilidad ausente</b> + tardias/variables recurrentes o bradicardia; sinusoidal", "Categoria III (anormal)"),
          ("Desaceleraciones <b>tardias</b>", "Hipoxia / insuf. placentaria"),
          ("Desaceleraciones <b>variables</b>", "Compresion de cordon")],
         "Tempranas = cabeza (benignas); tardias = hipoxia; variables = cordon."),
    D + ["rctg"])

add(deck_d, caso("Doppler fetal (RCIU / vigilancia)"),
    disc("Evaluar la circulacion fetoplacentaria y el grado de compromiso.",
         [("<b>Arteria umbilical:</b> flujo diastolico ausente/reverso", "Insuf. placentaria avanzada"),
          ("<b>ACM:</b> vasodilatacion (indice bajo)", "Redistribucion / 'brain sparing'"),
          ("<b>Ductus venoso:</b> onda a ausente/reversa", "Acidemia (interrupcion)"),
          ("ACM pico sistolico alto", "Anemia fetal (isoinmunizacion)")],
         "El ductus venoso reverso es el marcador mas tardio y grave: indica interrumpir."),
    D + ["doppler"])

add(deck_d, caso("Especuloscopia obstetrica (sospecha de RPM)"),
    disc("Confirmar salida de liquido amniotico ante sospecha de RPM.",
         [("<b>Liquido en fondo de saco</b> + escurre con Valsalva", "RPM (visualizacion directa)"),
          ("<b>Nitrazina</b>: papel vira a azul (pH alcalino)", "Liquido amniotico (vs flujo acido)"),
          ("<b>Cristalografia</b>: patron en <b>hoja de helecho</b>", "Liquido amniotico"),
          ("Liquido <b>fetido/purulento</b>", "Corioamnionitis")],
         "Evita el tacto en RPM pretermino (aumenta infeccion); usa especulo esteril."),
    D + ["rpm"])

add(deck_d, caso("Maniobras de Leopold + tacto obstetrico"),
    disc("Determinar situacion/presentacion fetal y progreso del parto.",
         [("Polo <b>duro y peloteable en fondo</b> uterino", "Presentacion pelvica"),
          ("Cuello con <b>borramiento + dilatacion progresivos</b>", "Trabajo de parto verdadero"),
          ("Bishop &ge;6-8 (cuello blando, anterior, dilatado)", "Cuello favorable para induccion"),
          ("Cordon palpable / late por delante de la presentacion", "Prolapso de cordon (urgencia)")],
         "No tactar en placenta previa ni en RPM pretermino."),
    D + ["tacto"])

add(deck_d, caso("Toma de TA + exploracion en preeclampsia"),
    disc("Estratificar la severidad del trastorno hipertensivo.",
         [("TA <b>&ge;140/90</b> tras 20 sem (2 tomas)", "Hipertension del embarazo"),
          ("TA <b>&ge;160/110</b>", "Criterio de severidad"),
          ("<b>Hiperreflexia / clonus</b>", "Irritabilidad neurologica (riesgo eclampsia)"),
          ("Edema de cara/manos de inicio rapido", "Apoya preeclampsia (no es criterio aislado)")],
         "El edema solo NO hace dx; la proteinuria o el dano de organo si."),
    D + ["preeclampsia"])

add(deck_d, caso("Medicion de altura uterina"),
    disc("Tamizar crecimiento fetal y volumen de liquido segun semanas.",
         [("Altura (cm) &asymp; semanas (entre 20-34)", "Crecimiento acorde"),
          ("Altura <b>&lt; semanas</b> (&gt;3 cm)", "RCIU / oligohidramnios -> USG"),
          ("Altura <b>&gt; semanas</b>", "Macrosomia / polihidramnios / multiple -> USG")],
         "Es tamizaje grueso: toda discordancia se confirma con USG/biometria."),
    D + ["altura_uterina"])


# ===================== PANELES (8) =====================
P = ["panel"]
add(deck_p, caso("Panel del control prenatal por trimestre"),
    panel("<b>1T:</b> grupo y Rh + Coombs, BH, glucosa, EGO + <b>urocultivo</b>, VIH/VDRL/HepB(/HepC), USG 11-14. "
          "<b>2T:</b> <b>CTOG 24-28</b>, USG estructural 18-22. <b>3T:</b> <b>cultivo EGB 36-37</b>, BH, TA/proteinuria.",
          "En cada visita: TA, peso, altura uterina, FCF, movimientos fetales y proteinuria en tira.",
          "Rh- &rarr; anti-D 28 sem + posparto. Urocultivo+ aunque asintomatica &rarr; tratar."),
    P + ["control_prenatal"])

add(deck_p, caso("Panel de preeclampsia / severidad"),
    panel("<b>Proteinuria</b> (tira / relacion proteina-creatinina / 24 h), <b>plaquetas</b>, "
          "<b>transaminasas (AST/ALT)</b>, <b>creatinina</b>, LDH, acido urico, BH con frotis. Vigilancia fetal "
          "(RCTG, USG/Doppler, ILA).",
          "Datos de severidad: TA &ge;160/110, plaquetas &lt;100k, Cr &gt;1.1, transaminasas 2x, edema pulmonar, sintomas neuro/visuales, epigastralgia.",
          "Proteinuria NO es obligatoria si ya hay dano de organo: eso ya define preeclampsia."),
    P + ["preeclampsia"])

add(deck_p, caso("Panel del sindrome HELLP"),
    panel("<b>Hemolisis</b>: <b>LDH alta</b>, bilirrubina, <b>esquistocitos</b> en frotis, haptoglobina baja. "
          "<b>EL</b>: AST/ALT elevadas. <b>LP</b>: <b>plaquetas &lt;100,000</b>.",
          "Vigilo CID (fibrinogeno, TP/TTP), hematoma/ruptura hepatica, lesion renal aguda.",
          "HELLP = Hemolisis + Enzimas hepaticas + Plaquetas bajas, sobre preeclampsia."),
    P + ["hellp"])

add(deck_p, caso("Panel de diabetes gestacional"),
    panel("Tamiz <b>O'Sullivan 50 g (1 h)</b>: &ge;140 &rarr; confirmatoria. <b>CTOG 75 g (un paso) 24-28 sem</b>: "
          "ayuno &ge;92, 1 h &ge;180, 2 h &ge;153 (un valor basta). Alternativa 100 g 3 h (dos valores).",
          "Si factores de riesgo: tamizar tambien en 1T (descartar diabetes pregestacional con HbA1c/glucosa).",
          "Tras el parto: <b>CTOG 75 g a las 6-12 semanas</b> para reclasificar (riesgo de DM2)."),
    P + ["dmg"])

add(deck_p, caso("Panel del sangrado del 1er trimestre"),
    panel("<b>beta-hCG cuantitativa seriada</b> (cada 48 h: debe duplicar), <b>USG transvaginal</b>, "
          "grupo y <b>Rh</b>, BH. (Progesterona si dudas de viabilidad.)",
          "Ectopico (no duplica + utero vacio), aborto (cae), mola (muy alta + copos de nieve).",
          "beta-hCG sola no localiza: se interpreta <b>junto al USG</b> y la zona discriminatoria."),
    P + ["sangrado_1t"])

add(deck_p, caso("Panel TORCH (serologias)"),
    panel("<b>IgG/IgM</b> por agente segun sospecha/tamizaje: <b>T</b>oxoplasma, <b>O</b>tros (sifilis-VDRL, VIH, HepB, "
          "varicela, parvovirus, Zika), <b>R</b>ubeola, <b>C</b>MV, <b>H</b>erpes. Avidez de IgG para datar la infeccion.",
          "IgM+ / seroconversion = infeccion reciente (mayor riesgo fetal); IgG+ aislada = inmunidad previa.",
          "Solo sifilis, VIH y HepB se tamizan a TODAS; el resto segun riesgo/clinica."),
    P + ["torch"])

add(deck_p, caso("Panel de Estreptococo grupo B (EGB)"),
    panel("<b>Cultivo recto-vaginal a las 36-37 sem</b> a todas. Indica profilaxis intraparto si +.",
          "Tambien indican profilaxis (sin cultivo): bacteriuria por EGB en este embarazo, hijo previo con EGB, "
          "o factores de riesgo intraparto (fiebre, RPM &gt;18 h, &lt;37 sem) si estado desconocido.",
          "El cultivo dirige; la profilaxis es <b>intraparto</b>, no anteparto."),
    P + ["egb"])

add(deck_p, caso("Panel de isoinmunizacion Rh"),
    panel("<b>Grupo y Rh</b> maternos, <b>Coombs indirecto</b> (anticuerpos), Rh paterno. Si sensibilizada: titulos "
          "seriados + <b>Doppler de ACM</b> (pico sistolico) para anemia fetal.",
          "Coombs indirecto - &rarr; candidata a profilaxis anti-D. Coombs + &rarr; ya sensibilizada (vigilar feto).",
          "ACM con pico sistolico alto = anemia fetal &rarr; valorar transfusion intrauterina."),
    P + ["rh"])


# ===================== MENOS (17) =====================
M = ["menos_preguntado"]
simple = [
    ("Perfil biofisico fetal", "5 componentes (RCTG, movimientos, tono, respiracion, <b>ILA</b>); &le;4/10 = compromiso &rarr; valorar interrupcion.", "vigilancia_fetal"),
    ("Indice de liquido amniotico (ILA)", "<b>&lt;5 cm = oligohidramnios</b> (insuf. placentaria/RPM); <b>&gt;24 cm = polihidramnios</b> (DMG/atresias).", "liquido"),
    ("Fibronectina fetal / cervicometria", "Cervix &lt;25 mm o fibronectina+ &rarr; mayor riesgo de parto pretermino; su <b>negatividad</b> tranquiliza (alto VPN).", "pretermino"),
    ("Test de nitrazina vs cristalografia", "Nitrazina (pH) tiene falsos+ (sangre, semen); <b>helecho</b> (cristalografia) es mas especifico para RPM.", "rpm"),
    ("Zona discriminatoria de beta-hCG", "Con beta-hCG <b>&gt;1500-2000</b> deberia verse saco intrauterino; si no, sospecha de ectopico.", "ectopico"),
    ("Translucencia nucal + bioquimica (1T)", "USG 11-14 sem + PAPP-A/beta-hCG libre: <b>cribado de aneuploidias</b> (riesgo de T21/T18).", "cribado"),
    ("USG estructural (18-22 sem)", "Anatomia fetal detallada: <b>malformaciones</b>, marcadores, placenta y liquido.", "cribado"),
    ("ADN fetal libre (cffDNA / NIPT)", "Cribado prenatal no invasivo de trisomias con alta sensibilidad; <b>no es diagnostico</b> (confirmar con invasivo).", "cribado"),
    ("Amniocentesis / biopsia de vellosidades", "<b>Diagnostico</b> (cariotipo) tras cribado positivo; pequeno riesgo de perdida. Evento sensibilizante &rarr; anti-D si Rh-.", "cribado"),
    ("Test de Kleihauer-Betke", "Cuantifica <b>hemorragia fetomaterna</b> (trauma, DPPNI) para ajustar dosis de anti-D.", "rh"),
    ("Acidos biliares (colestasis)", "Elevados en prurito del 3T sin exantema = <b>colestasis intrahepatica</b>; correlacionan con riesgo fetal.", "colestasis"),
    ("Frotis con esquistocitos", "Hematies fragmentados = <b>hemolisis microangiopatica</b> (HELLP/microangiopatia).", "hellp"),
    ("Punopercusion (Giordano)", "Positiva + fiebre en embarazada con disuria = <b>pielonefritis</b> &rarr; hospitalizar + IV.", "ivu"),
    ("Gasometria de cordon al nacer", "pH bajo + base exceso negativo = <b>acidemia/asfixia</b> perinatal.", "sufrimiento_fetal"),
    ("Escala de Edimburgo", "Tamizaje de <b>depresion perinatal</b> a las 2-6 sem posparto y en visitas; deriva si ideacion suicida.", "salud_mental"),
    ("Maduracion pulmonar: ventana", "El corticoide da maximo beneficio si el parto ocurre entre <b>24 h y 7 dias</b> de la 1a dosis (24-34 sem).", "corticoide"),
    ("Glucemia capilar (automonitoreo DMG)", "Metas: ayuno &lt;95, 1 h posprandial &lt;140, 2 h &lt;120; guia el ajuste de insulina.", "dmg"),
]
for titulo, texto, tag in simple:
    add(deck_m, caso(titulo),
        f'<span class="bloque paraque"><span class="lab">Para que / como se lee</span>{texto}</span>',
        M + [tag])


def build():
    for d, f in [(deck_d, "Estudios_01_Discriminadores.apkg"), (deck_p, "Estudios_02_Paneles.apkg"),
                 (deck_m, "Estudios_03_Menos.apkg")]:
        genanki.Package(d).write_to_file(os.path.join(OUTPUT_DIR, f))
        print(f"  -> {f} ({len(d.notes)} notas)")
    genanki.Package([deck_d, deck_p, deck_m]).write_to_file(
        os.path.join(OUTPUT_DIR, "No_Hay_Tiempo_Obst_Estudios_TODOS.apkg"))
    print(f"  -> TODOS ({sum(len(d.notes) for d in [deck_d, deck_p, deck_m])} notas)")


if __name__ == "__main__":
    build()
