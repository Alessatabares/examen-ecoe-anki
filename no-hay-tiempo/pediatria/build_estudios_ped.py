"""No hay tiempo / Pediatria — PILAR EXPLORACION + ESTUDIOS.

A) DISCRIMINADOR: una herramienta separa un grupo por un hallazgo (por herramienta).
B) PANEL/workup: una entidad pide una bateria con rol de cada estudio (por enfermedad).
Enfoque pediatrico: que pido, que NO de rutina, y los signos/scores clasicos del examen.
Guia: AAP, AHA/PALS, GINA, OMS, Nelson, GPC MX.
"""
import os
import genanki

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "output")
os.makedirs(OUTPUT_DIR, exist_ok=True)

MODEL_QA_ID = 1990010903
DECK_ID_D, DECK_ID_P, DECK_ID_M = 1990010021, 1990010022, 1990010023
DECK_NAME_D = "No hay tiempo::Pediatria::Estudios::1 - Discriminadores (herramienta)"
DECK_NAME_P = "No hay tiempo::Pediatria::Estudios::2 - Paneles (por entidad)"
DECK_NAME_M = "No hay tiempo::Pediatria::Estudios::3 - Signos y scores"

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
model_qa = genanki.Model(MODEL_QA_ID, "NHT Ped Estudios QA",
    fields=[{"name": "Front"}, {"name": "Back"}],
    templates=[{"name": "QA", "qfmt": "{{Front}}", "afmt": '{{Front}}<hr id="extra">{{Back}}'}],
    css=CSS_BASE)

deck_d = genanki.Deck(DECK_ID_D, DECK_NAME_D)
deck_p = genanki.Deck(DECK_ID_P, DECK_NAME_P)
deck_m = genanki.Deck(DECK_ID_M, DECK_NAME_M)
BASE_TAGS = ["pediatria", "ecoe", "no_hay_tiempo", "estudios"]


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
add(deck_d, caso("Triangulo de Evaluacion Pediatrica (TEP)"),
    disc("Decidir gravedad/urgencia en segundos, ANTES de tocar al nino.",
         [("<b>Apariencia</b> alterada (tono, mirada, consuelo)", "Disfuncion SNC / metabolico / sepsis"),
          ("<b>Respiracion</b> alterada (ruidos, tiraje, postura)", "Dificultad respiratoria"),
          ("<b>Circulacion</b> alterada (palidez, marmoreo, cianosis)", "Choque"),
          ("Los 3 alterados", "Falla cardiopulmonar")],
         "El TEP es OBSERVACIONAL (sin tocar). Un solo lado alterado ya cambia la prioridad."),
    D + ["tep"])

add(deck_d, caso("Discriminador de EXANTEMAS"),
    disc("Identificar el exantema por morfologia + pródromo.",
         [("<b>Manchas de Koplik</b> + coriza/tos/conjuntivitis", "Sarampion"),
          ("<b>Vesiculas en distintos estadios</b> + prurito", "Varicela"),
          ("<b>Piel en lija + lengua aframbuesada</b>", "Escarlatina"),
          ("Fiebre 3 d que cede y aparece exantema", "Roseola (exantema subito)"),
          ("<b>'Cara abofeteada'</b> + reticular", "Eritema infeccioso"),
          ("<b>Petequias/purpura que NO blanquean</b> + mal estado", "Meningococemia (urgencia)")],
         "Toda fiebre + exantema: BUSCA petequias que no blanquean (presion/diascopia) = meningococemia."),
    D + ["exantemas"])

add(deck_d, caso("Discriminador del ESTRIDOR (via aerea alta)"),
    disc("Separar las causas de estridor y su urgencia.",
         [("<b>Tos perruna + estridor + disfonia</b>, febricula", "Crup (laringotraqueitis)"),
          ("<b>Fiebre alta + babeo + tripode + toxico</b>, sin tos perruna", "Epiglotitis (urgencia)"),
          ("<b>Inicio subito atragantandose</b>, sano previo", "Cuerpo extrano"),
          ("Estridor desde el nacimiento, intermitente", "Laringomalacia")],
         "En epiglotitis NO explores la garganta ni agites al nino (puede cerrar la via aerea)."),
    D + ["estridor"])

add(deck_d, caso("Estratificacion del lactante febril (por edad + biomarcadores)"),
    disc("Definir cuanto estudio y si trato/ingreso segun la edad.",
         [("<b>&le;28 dias</b>", "Estudio completo + LCR + antibiotico + ingreso (siempre)"),
          ("<b>29-60 dias</b>", "Sangre + orina; PL/antibiotico segun PCT/PCR y aspecto"),
          ("<b>&gt;3 meses, buen aspecto, foco claro</b>", "Manejo del foco; menos estudio"),
          ("<b>Cualquier edad con mal aspecto (TEP)</b>", "Estudio + tratamiento agresivo")],
         "La PCT/PCR estratifican, pero el ASPECTO (TEP) manda. La orina del lactante: sondaje/suprapubica, no bolsa."),
    D + ["lactante_febril"])

add(deck_d, caso("Grado de deshidratacion (clinico)"),
    disc("Estimar perdidas para elegir el plan A/B/C.",
         [("Alerta, bebe normal, sin signos", "Sin deshidratacion -> Plan A"),
          ("<b>Sediento/irritable, ojos hundidos, pliegue lento, lagrimas escasas</b>", "Leve-moderada -> Plan B (SRO)"),
          ("<b>Letargico, ojos muy hundidos, pliegue muy lento, no bebe, llenado lento</b>", "Grave -> Plan C (IV)"),
          ("Hipotension / choque", "Choque -> bolos IV YA")],
         "La hipotension es TARDIA en el nino: no esperes a que caiga la TA. Pesa al nino para guiar la reposicion."),
    D + ["deshidratacion"])

add(deck_d, caso("Bilirrubina neonatal (cuando es patologica)"),
    disc("Decidir si la ictericia requiere accion (nomograma por horas).",
         [("Aparece <b>&lt;24 h</b> de vida", "Patologica (hemolisis) -> estudiar"),
          ("Sube muy rapido o pasa el umbral por <b>horas/EG/factores</b>", "Tratar (fototerapia)"),
          ("Aparece 2-3 d, baja, buen estado", "Fisiologica (vigilar)"),
          ("Ictericia <b>prolongada</b> (&gt;2 sem) o colestasis (coluria/acolia)", "Estudiar (atresia/hipotiroidismo)")],
         "Bilirrubina directa alta + acolia/coluria = colestasis (atresia biliar): NO es fisiologica, urge estudiar."),
    D + ["bilirrubina"])

add(deck_d, caso("Puncion lumbar / LCR"),
    disc("Diferenciar meningitis bacteriana de viral y orientar.",
         [("<b>Polimorfonucleares, glucosa BAJA, proteinas altas, turbio</b>", "Bacteriana"),
          ("Linfocitos, glucosa normal, proteinas algo altas, claro", "Viral"),
          ("Tincion de Gram / cultivo / PCR +", "Agente especifico"),
          ("Inestable / signos de hipertension intracraneal", "NO retrases el antibiotico por la PL")],
         "Si el nino esta inestable o hay datos de hipertension intracraneal, da antibiotico YA y difiere la PL."),
    D + ["lcr"])

add(deck_d, caso("Taquipnea y trabajo respiratorio (clinico)"),
    disc("Valorar gravedad respiratoria y separar entidades.",
         [("<b>Taquipnea</b> (OMS: &lt;2 m &ge;60; 2-12 m &ge;50; 1-5 a &ge;40)", "Mejor signo de neumonia"),
          ("Sibilancias 1er episodio en &lt;2 a", "Bronquiolitis"),
          ("Estridor inspiratorio", "Obstruccion alta (crup/epiglotitis)"),
          ("<b>Tiraje, aleteo, quejido, SatO2 baja, apneas</b>", "Dificultad grave -> soporte/ingreso")],
         "Cuenta la FR un minuto completo. Bronquiolitis y crup son CLINICOS: la Rx de torax NO es de rutina."),
    D + ["respiratorio"])


# ===================== PANELES (8) =====================
P = ["panel"]
add(deck_p, caso("Panel de la fiebre sin foco en lactante &lt; 3 meses"),
    panel("<b>BH + PCR/PCT</b>, <b>hemocultivo</b>, <b>EGO + urocultivo</b> (sondaje/suprapubica), valorar "
          "<b>LCR</b> (siempre en &le;28 d) &plusmn; Rx/coprologico segun clinica.",
          "Infeccion bacteriana grave (ITU es la mas frecuente, luego bacteriemia/meningitis); aspecto (TEP).",
          "&le;28 d: estudio completo + antibiotico + ingreso SIEMPRE. La orina por bolsa NO confirma (sondaje)."),
    P + ["fiebre_sin_foco"])

add(deck_p, caso("Panel de la sepsis neonatal"),
    panel("<b>Hemocultivo</b> + BH + PCR/PCT + <b>EGO/urocultivo</b> + valorar <b>PL (LCR)</b>; glucemia. "
          "NO retrasar el antibiotico empirico por completar el estudio.",
          "Precoz (SGB, Listeria, E. coli) vs tardia (nosocomial); meningitis asociada.",
          "Signos inespecificos: ante la duda, cultiva y trata. Empirico precoz = ampicilina + gentamicina."),
    P + ["sepsis_neonatal"])

add(deck_p, caso("Panel de la ITU pediatrica"),
    panel("<b>EGO</b> (esterasa/nitritos) + <b>urocultivo de muestra valida</b> (sondaje/suprapubica si no controla "
          "esfinter); funcion renal si grave. <b>Ecografia renal</b> tras ITU febril; valorar reflujo si recurrente.",
          "Pielonefritis vs cistitis; anomalia de la via urinaria / reflujo; obstruccion.",
          "La bolsa recolectora solo sirve para DESCARTAR (alta tasa de contaminacion). Urocultivo confirma."),
    P + ["itu"])

add(deck_p, caso("Panel de la enfermedad de Kawasaki"),
    panel("Clinica (<b>fiebre &ge;5 d + criterios</b>) + reactantes (PCR/VSG, plaquetas), BH, PFH, EGO; "
          "<b>ECOCARDIOGRAMA</b> (arterias coronarias) al dx y en seguimiento.",
          "Aneurismas coronarios (la complicacion que importa); descartar otras causas de fiebre/exantema.",
          "El ecocardiograma es clave (aneurismas). Hay Kawasaki <b>incompleto</b> (menos criterios + reactantes "
          "altos): no lo pases por alto en el lactante."),
    P + ["kawasaki"])

add(deck_p, caso("Panel de la convulsion febril (cuando NO estudiar)"),
    panel("<b>Simple y buen estado</b>: NO requiere de rutina EEG, TAC ni PL; busco el <b>foco de la fiebre</b> "
          "(clinica, EGO si aplica). <b>PL</b> si datos meningeos, &lt;12 meses con dudas o aspecto toxico.",
          "Meningitis/encefalitis; causas no febriles (descarta si no hay fuente clara).",
          "La febril SIMPLE no necesita neuroimagen ni EEG. Estudia la compleja, la prolongada o el mal aspecto."),
    P + ["convulsion_febril"])

add(deck_p, caso("Panel respiratorio pediatrico (bronquiolitis / crup / neumonia)"),
    panel("<b>Clinico</b> (FR, trabajo, SatO2). <b>Rx de torax</b> solo si: duda dx, gravedad, mala evolucion o "
          "sospecha de complicacion (derrame). Virus respiratorios si cambia el manejo/aislamiento.",
          "Neumonia complicada (derrame/empiema), cuerpo extrano, insuficiencia respiratoria.",
          "Bronquiolitis y crup son CLINICOS: NO Rx ni broncodilatador/antibiotico de rutina. Taquipnea = mejor "
          "signo de neumonia."),
    P + ["respiratorio"])

add(deck_p, caso("Panel del maltrato infantil (estudio dirigido)"),
    panel("Exploracion completa + <b>documentacion objetiva</b> (describir/fotografiar) + <b>serie osea</b> "
          "(&lt;2 a), <b>fondo de ojo</b> (hemorragias retinianas), neuroimagen segun caso; estudio de coagulacion "
          "para descartar diferenciales.",
          "Lesiones en distintos estadios, fracturas especificas, hemorragias retinianas; coagulopatia (dx "
          "diferencial).",
          "Documenta textual y objetivamente (puede ser prueba legal). <b>Notificar es obligacion</b>; prioriza la "
          "seguridad del nino."),
    P + ["maltrato"])

add(deck_p, caso("Panel del recien nacido sano (tamizajes)"),
    panel("<b>Tamiz metabolico (talon)</b>, <b>tamiz auditivo</b>, <b>cardiopatia critica (oximetria pre/"
          "posductal)</b>, exploracion de <b>caderas (Ortolani/Barlow)</b>, reflejo rojo (ojos), peso/PC.",
          "Hipotiroidismo congenito y metabolopatias, sordera, cardiopatia critica, displasia de cadera, "
          "cataratas/retinoblastoma.",
          "Los tamizajes detectan en presintomatico, cuando tratar cambia el pronostico (p.ej. hipotiroidismo "
          "congenito). Verifica que se hayan hecho."),
    P + ["rn_sano"])


# ===================== SIGNOS Y SCORES (18) =====================
M = ["signo_score"]
simple = [
    ("Triangulo de Evaluacion Pediatrica (TEP)", "Apariencia + Respiracion + Circulacion (observacional) -> decide gravedad/urgencia antes de tocar.", "tep"),
    ("APGAR", "Evalua al RN al 1 y 5 min (FC, respiracion, tono, irritabilidad, color); orienta, NO dirige la reanimacion (esa la guia la FC/respiracion).", "rcp_neonatal"),
    ("Manchas de Koplik", "Enantema patognomonico (puntos blancos en mucosa oral) que precede al exantema del <b>sarampion</b>.", "sarampion"),
    ("Lengua aframbuesada + piel en lija", "Signos de <b>escarlatina</b> (estreptococo); + lineas de Pastia y palidez peribucal.", "escarlatina"),
    ("Criterios de Kawasaki", "Fiebre &ge;5 d + 4/5 (conjuntivitis, labios/lengua, exantema, manos/pies, adenopatia); riesgo = aneurisma coronario.", "kawasaki"),
    ("Centor / McIsaac", "Probabilidad de faringitis estreptococica (fiebre, exudado, adenopatias, ausencia de tos, edad) -> prueba/antibiotico.", "faringitis"),
    ("Escala de Westley (crup)", "Gradua la gravedad del <b>crup</b> (estridor, tiraje, entrada de aire, cianosis, conciencia) -> decide adrenalina.", "crup"),
    ("Taquipnea por edad (OMS)", "&lt;2 m &ge;60; 2-12 m &ge;50; 1-5 a &ge;40 rpm; mejor signo de <b>neumonia</b>.", "neumonia"),
    ("Signos de deshidratacion", "Ojos hundidos, lagrimas, mucosas, <b>signo del pliegue</b>, llenado capilar, estado de alerta, diuresis -> grado y plan A/B/C.", "deshidratacion"),
    ("Planes A / B / C (OMS)", "A: sin deshidratacion (casa); B: leve-moderada (SRO oral); C: grave/choque (IV).", "gea"),
    ("Fontanela abombada", "Signo de <b>meningitis</b>/hipertension intracraneal en el lactante (mas util que Kernig/Brudzinski a esa edad).", "meningitis"),
    ("Kernig / Brudzinski", "Signos meningeos en el nino mayor; POCO fiables en el lactante.", "meningitis"),
    ("Petequias/purpura que no blanquean", "Diascopia/presion: si NO desaparecen + mal estado = <b>meningococemia</b> (antibiotico YA).", "meningitis"),
    ("Ortolani / Barlow", "Maniobras de cadera del RN para <b>displasia del desarrollo (DDC)</b>; tamizaje + USG/Rx segun edad.", "ddc"),
    ("Tos en accesos + gallo + vomito postusivo", "Patron de <b>tos ferina</b>; en &lt;6 meses puede ser apnea sin tos clasica.", "tos_ferina"),
    ("Vomito en proyectil no bilioso (3-6 sem) + oliva", "<b>Estenosis pilorica</b>; alcalosis metabolica hipocloremica. Vomito BILIOSO = obstruccion (urgencia).", "pilorica"),
    ("Heces en jalea de grosella + masa en salchicha", "<b>Invaginacion</b> intestinal (dolor colico + decaimiento); la triada completa es tardia.", "invaginacion"),
    ("Ritmos de paro (PALS)", "Desfibrilables = FV/TV sin pulso; no desfibrilables = asistolia/AESP (los mas frecuentes en el nino). Causa = hipoxica.", "pals"),
]
for titulo, texto, tag in simple:
    add(deck_m, caso(titulo),
        f'<span class="bloque paraque"><span class="lab">Que es / como se lee</span>{texto}</span>',
        M + [tag])


def build():
    for d, f in [(deck_d, "Estudios_01_Discriminadores.apkg"), (deck_p, "Estudios_02_Paneles.apkg"),
                 (deck_m, "Estudios_03_Signos_scores.apkg")]:
        genanki.Package(d).write_to_file(os.path.join(OUTPUT_DIR, f))
        print(f"  -> {f} ({len(d.notes)} notas)")
    genanki.Package([deck_d, deck_p, deck_m]).write_to_file(
        os.path.join(OUTPUT_DIR, "No_Hay_Tiempo_Ped_Estudios_TODOS.apkg"))
    print(f"  -> TODOS ({sum(len(d.notes) for d in [deck_d, deck_p, deck_m])} notas)")


if __name__ == "__main__":
    build()
