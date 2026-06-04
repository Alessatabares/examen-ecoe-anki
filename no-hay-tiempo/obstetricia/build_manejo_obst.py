"""No hay tiempo / Obstetricia — PILAR MANEJO (ejes + core + menos).

Formato carta de manejo (Back, 3 bloques): VERBALIZO / CONSEJERIA / CIERRE.
Formato carta de eje (Back, 3 bloques): REGLA MADRE / BIFURCACION / TRAMPA.
Guia: GPC mexicanas + ACOG + Williams.
"""
import os
import genanki

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "output")
os.makedirs(OUTPUT_DIR, exist_ok=True)

MODEL_QA_ID = 1990004001
DECK_ID_EJES, DECK_ID_CORE, DECK_ID_MENOS = 1990003001, 1990003002, 1990003003
DECK_NAME_EJES = "No hay tiempo::Obstetricia::1 - Ejes (madre)"
DECK_NAME_CORE = "No hay tiempo::Obstetricia::2 - Manejos trampa (core)"
DECK_NAME_MENOS = "No hay tiempo::Obstetricia::3 - Menos preguntados"

CSS_BASE = """
.card { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  font-size: 19px; text-align: left; color: #1a1a1a; background-color: #fafafa;
  padding: 20px; line-height: 1.55; }
.caso { font-size: 21px; font-weight: 700; color: #1e3a8a; }
#extra { margin-top: 16px; border: none; border-top: 1px solid #d4d4d4; padding-top: 12px; }
.bloque { display: block; margin: 12px 0; padding: 10px 14px; border-radius: 8px; }
.lab { display: block; font-size: 13px; font-weight: 700; letter-spacing: .5px;
  text-transform: uppercase; margin-bottom: 4px; }
.verbalizo { background: #eef2ff; border-left: 4px solid #1e3a8a; }
.consejeria { background: #ecfdf5; border-left: 4px solid #047857; }
.cierre { background: #fff7ed; border-left: 4px solid #b45309; }
.verbalizo .lab { color: #1e3a8a; } .consejeria .lab { color: #047857; } .cierre .lab { color: #b45309; }
.consejeria em { color: #065f46; font-style: italic; }
.regla { background: #eef2ff; border-left: 4px solid #1e3a8a; }
.bif { background: #f5f3ff; border-left: 4px solid #6d28d9; }
.trampa { background: #fef2f2; border-left: 4px solid #b91c1c; }
.regla .lab { color: #1e3a8a; } .bif .lab { color: #6d28d9; } .trampa .lab { color: #b91c1c; }
b { color: #111; }
"""
model_qa = genanki.Model(MODEL_QA_ID, "NHT Obst Manejo QA",
    fields=[{"name": "Front"}, {"name": "Back"}],
    templates=[{"name": "QA", "qfmt": "{{Front}}", "afmt": '{{Front}}<hr id="extra">{{Back}}'}],
    css=CSS_BASE)

deck_ejes = genanki.Deck(DECK_ID_EJES, DECK_NAME_EJES)
deck_core = genanki.Deck(DECK_ID_CORE, DECK_NAME_CORE)
deck_menos = genanki.Deck(DECK_ID_MENOS, DECK_NAME_MENOS)
BASE_TAGS = ["obstetricia", "ecoe", "no_hay_tiempo"]


def add(deck, front, back, tags):
    deck.add_note(genanki.Note(model=model_qa, fields=[front, back], tags=BASE_TAGS + tags))

def caso(t): return f'<span class="caso">{t}</span>'

def manejo(v, c, ci):
    return (f'<span class="bloque verbalizo"><span class="lab">Verbalizo (al sinodal)</span>{v}</span>'
            f'<span class="bloque consejeria"><span class="lab">Consejeria (a la paciente)</span><em>{c}</em></span>'
            f'<span class="bloque cierre"><span class="lab">Cierre (seguridad)</span><em>{ci}</em></span>')

def eje(r, b, t):
    return (f'<span class="bloque regla"><span class="lab">Regla madre</span>{r}</span>'
            f'<span class="bloque bif"><span class="lab">Bifurcacion</span>{b}</span>'
            f'<span class="bloque trampa"><span class="lab">Trampa ECOE</span>{t}</span>')


# ===================== SUBDECK 1 - EJES (7) =====================
E = ["eje"]
add(deck_ejes, caso("EJE 1 — Hemorragia obstetrica: ESTABILIZO antes de diagnosticar"),
    eje("Imagen: la madre primero. El sangrado obstetrico mata por hipovolemia, no por no saber el dx. "
        "<b>ABC + 2 vias gruesas + cristaloides + cruzar/hemoderivados + O2</b>, y en paralelo busco la causa.",
        "<b>1er trimestre:</b> ectopico / aborto / mola.<br><b>3er trimestre:</b> placenta previa / DPPNI.<br>"
        "<b>Posparto:</b> las 4 T (tono, trauma, tejido, trombina).",
        "Nunca te quedes nombrando el dx con la paciente inestable: primero reanimas, luego clasificas."),
    E + ["hemorragia"])

add(deck_ejes, caso("EJE 2 — Sangrado de 3er trimestre: NO TACTO hasta descartar previa"),
    eje("Imagen: las manos quietas. Ante sangrado del 3T, <b>especuloscopia suave y USG</b> ANTES de cualquier "
        "tacto vaginal (un tacto sobre placenta previa desencadena hemorragia masiva).",
        "<b>Indoloro, sangre roja rutilante, utero blando, FCF buena</b> &rarr; placenta previa.<br>"
        "<b>Doloroso, hipertonia, sangre oscura &plusmn; oculta, sufrimiento fetal</b> &rarr; DPPNI.",
        "La primera orden en sangrado del 3T es <b>&laquo;NO tacto vaginal&raquo;</b> + USG. Es lo que puntua el sinodal."),
    E + ["sangrado_3t"])

add(deck_ejes, caso("EJE 3 — Preeclampsia/eclampsia: Mg + antiHTA, pero lo definitivo es INTERRUMPIR"),
    eje("Imagen: tres palancas. <b>Sulfato de Mg</b> (previene/trata convulsion) + <b>antihipertensivo</b> "
        "(protege a la madre) + <b>interrupcion</b> (unico tratamiento curativo: saca la placenta).",
        "<b>Severa &ge;34 sem o eclampsia/HELLP</b> &rarr; interrumpo. <b>&lt;34 sem estable</b> &rarr; "
        "corticoide + Mg neuroproteccion + manejo expectante vigilado.",
        "El Mg <b>no baja la TA</b> (es anticonvulsivante); el antiHTA no previene convulsiones. Son cosas distintas."),
    E + ["preeclampsia"])

add(deck_ejes, caso("EJE 4 — La EDAD GESTACIONAL bifurca casi todo en obstetricia"),
    eje("Imagen: una linea del tiempo con un corte en <b>34</b> y otro en <b>37</b> semanas.",
        "<b>&lt;34 sem:</b> ganar tiempo &rarr; corticoide (madurez pulmonar) + Mg neuroproteccion (&lt;32) + expectante.<br>"
        "<b>34-37:</b> individualizar.<br><b>&ge;37 sem:</b> interrumpir suele ser seguro.",
        "Aplica igual a pretermino, RPM, preeclampsia y previa: cuando dudes la conducta, pregunta <b>&iquest;cuantas semanas?</b>"),
    E + ["edad_gestacional"])

add(deck_ejes, caso("EJE 5 — Farmacos prohibidos vs seguros en embarazo"),
    eje("Imagen: una lista negra que recitas antes de prescribir.",
        "<b>PROHIBIDOS:</b> IECA/ARA-II, warfarina, misoprostol (salvo indicacion obstetrica), tetraciclinas, "
        "isotretinoina, valproato, atenolol, estatinas, vacunas vivas.<br>"
        "<b>SEGUROS:</b> alfa-metildopa/labetalol/hidralazina/nifedipino (HTA), penicilina, heparina, insulina, "
        "folato/hierro, Tdap/influenza.",
        "<b>Nunca IECA/ARA-II</b> en embarazo (oligohidramnios, dano renal fetal). Es la trampa farmacologica clasica."),
    E + ["farmacos"])

add(deck_ejes, caso("EJE 6 — Vigilancia fetal: la categoria del RCTG decide la conducta"),
    eje("Imagen: un semaforo sobre el trazo cardiotocografico.",
        "<b>Categoria I (normal):</b> continuo vigilancia.<br>"
        "<b>Categoria II (indeterminado):</b> <b>reanimacion intrauterina</b> (decubito lateral izq, O2, liquidos, "
        "suspender oxitocina) y revaloro.<br>"
        "<b>Categoria III (anormal):</b> reanimo y <b>preparo interrupcion urgente</b> si no mejora.",
        "Desaceleraciones <b>tardias</b> o <b>variabilidad ausente</b> = hipoxia. Variables = compresion de cordon."),
    E + ["vigilancia_fetal"])

add(deck_ejes, caso("EJE 7 — Control prenatal: tamizaje universal por trimestre"),
    eje("Imagen: una agenda con tres casillas. En cada visita 'cosechas' lo que toca tamizar.",
        "<b>1T:</b> grupo y Rh + Coombs, BH, glucosa, EGO/urocultivo, VIH/VDRL/HepB, USG 11-14 (translucencia).<br>"
        "<b>2T:</b> <b>CTOG 24-28 sem (DMG)</b>, USG estructural 18-22, Coombs si Rh-.<br>"
        "<b>3T:</b> <b>cultivo EGB 36-37 sem</b>, BH, vigilancia de TA/proteinuria, posicion fetal.",
        "Rh- &rarr; <b>anti-D a las 28 sem</b> y posparto si RN Rh+. Bacteriuria asintomatica &rarr; <b>siempre tratar</b>."),
    E + ["control_prenatal"])


# ===================== SUBDECK 2 - CORE (18) =====================
C = ["core"]
add(deck_core, caso("Embarazo ectopico estable (sin ruptura)"),
    manejo("<b>Metotrexato IM dosis unica (50 mg/m2)</b> si: estable, <b>beta-hCG &lt;5000</b>, sin LCF, "
           "masa &lt;3.5-4 cm, sin liquido libre y paciente confiable. Seguimiento beta-hCG dias 4 y 7 (debe bajar &ge;15%).",
           "El embarazo se implanto fuera del utero, casi siempre en la trompa, y no puede continuar. Como esta "
           "estable, podemos disolverlo con un medicamento (metotrexato) y evitar cirugia, pero requiere seguimiento estrecho.",
           "Nada de acido folico, alcohol ni relaciones hasta el alta. Si aparece dolor intenso, mareo o desmayo, "
           "acuda de inmediato: puede significar ruptura."),
    C + ["ectopico"])

add(deck_core, caso("Embarazo ectopico roto / inestable"),
    manejo("<b>Cirugia urgente</b>: laparoscopia/laparotomia con <b>salpingectomia</b> (si trompa muy danada) o "
           "salpingostomia. Reanimacion simultanea con cristaloides + hemoderivados.",
           "Es una urgencia: el embarazo fuera del utero se rompio y hay sangrado interno. Necesitamos operar ahora "
           "para detenerlo. Le explico que puede ser necesario retirar la trompa afectada.",
           "Verbalizo: dos vias, cruzo sangre, aviso a quirofano y anestesia. La vida de la paciente es la prioridad."),
    C + ["ectopico"])

add(deck_core, caso("Aborto (amenaza vs incompleto)"),
    manejo("<b>Amenaza</b> (cuello cerrado, embrion vivo): reposo relativo, abstinencia, datos de alarma, USG control; "
           "progesterona si insuficiencia lutea. <b>Incompleto</b>: <b>AMEU</b> si estable (o misoprostol 600-800 mcg "
           "vaginal); hospitalizar si sepsis/sangrado abundante.",
           "Amenaza: hay sangrado pero el embarazo sigue; con reposo y vigilancia muchos continuan. "
           "Incompleto: quedaron restos y conviene vaciar el utero para evitar infeccion y sangrado.",
           "Datos de alarma: sangrado abundante, fiebre, dolor intenso o mal olor. Si es Rh negativa, indico anti-D."),
    C + ["aborto"])

add(deck_core, caso("Mola hidatiforme"),
    manejo("<b>AMEU/legrado por aspiracion</b> para evacuar + estudio histopatologico. <b>Seguimiento con beta-hCG "
           "semanal</b> hasta negativizar, luego mensual. <b>Anticoncepcion eficaz</b> y evitar embarazo 6-12 meses.",
           "Lo que crecio no es un bebe, sino un tejido placentario anormal; por eso la beta-hCG estaba tan alta. "
           "Hay que vaciar el utero y luego vigilar con analisis de sangre para asegurar que todo se resuelve.",
           "El seguimiento es indispensable: una pequena parte evoluciona a enfermedad trofoblastica persistente. "
           "Por eso no debe embarazarse hasta el alta (la beta-hCG es nuestro marcador)."),
    C + ["mola"])

add(deck_core, caso("Placenta previa con sangrado activo"),
    manejo("<b>Hospitalizo, NO TACTO VAGINAL</b>, USG + especuloscopia. Estabilizo: 2 vias, hemoderivados disponibles. "
           "<b>&lt;34 sem y sangrado controlado:</b> corticoide + expectante. <b>&ge;37 sem o sangrado severo:</b> <b>cesarea</b>.",
           "La placenta esta cubriendo la salida del utero, por eso el sangrado. Es indoloro pero hay que vigilarla. "
           "El nacimiento sera por cesarea, programada si todo esta estable.",
           "Reposo, nada de tactos ni relaciones. Si vuelve a sangrar de forma abundante, acuda de urgencia."),
    C + ["placenta_previa"])

add(deck_core, caso("Desprendimiento de placenta (DPPNI)"),
    manejo("<b>ABC materno + reanimacion</b> (cristaloides + hemoderivados). <b>Interrupcion urgente</b> (cesarea casi "
           "siempre); parto vaginal solo si dilatacion avanzada, feto muerto y madre estable. <b>Vigilar CID</b> y HPP.",
           "La placenta se esta separando antes de tiempo y eso pone en riesgo al bebe y a usted. Por eso hay que "
           "sacarlo cuanto antes, generalmente por cesarea.",
           "Verbalizo vigilancia de coagulopatia: pido plaquetas, fibrinogeno y TP/TTP, y tengo sangre lista."),
    C + ["dppni"])

add(deck_core, caso("Preeclampsia con datos de severidad"),
    manejo("1) <b>Hospitalizo</b> + monitoreo materno-fetal. 2) <b>Sulfato de Mg</b> (neuroproteccion). "
           "3) <b>Antihipertensivo</b>: labetalol, hidralazina o nifedipino (meta &lt;160/110). "
           "4) <b>Interrupcion</b>: &ge;34 sem inmediata; &lt;34 corticoide y evaluar segun estabilidad.",
           "Su presion esta peligrosamente alta y afecta organos. Vamos a controlarla y a prevenir convulsiones con "
           "un medicamento (sulfato de magnesio). El tratamiento que cura es que nazca el bebe, segun las semanas.",
           "Datos de alarma que debe avisar ya: dolor de cabeza intenso, ver lucecitas, dolor en la boca del "
           "estomago. La vigilo de cerca."),
    C + ["preeclampsia"])

add(deck_core, caso("Eclampsia"),
    manejo("1) <b>ABC</b> + decubito lateral izquierdo + O2 + proteccion de via aerea. 2) <b>Sulfato de Mg</b> "
           "(4-6 g IV en 20 min, luego 1-2 g/h). 3) Si persiste: bolo adicional 2 g; refractario &rarr; midazolam/diazepam. "
           "4) <b>Interrupcion</b> una vez estabilizada (no en plena convulsion).",
           "Tuvo una convulsion por la preeclampsia. Lo primero es protegerla y detener las convulsiones con sulfato "
           "de magnesio; cuando este estable, procederemos al nacimiento.",
           "No se interrumpe el embarazo durante la convulsion: primero se estabiliza a la madre."),
    C + ["eclampsia"])

add(deck_core, caso("Sindrome HELLP"),
    manejo("Estabilizo + <b>sulfato de Mg</b> + control de TA + <b>interrupcion del embarazo</b> (tratamiento "
           "definitivo). Manejo de plaquetas/hemoderivados segun sangrado; corticoide si &lt;34 sem para madurez pulmonar.",
           "Es una forma grave de la preeclampsia que afecta higado y plaquetas. Necesitamos estabilizarla y que el "
           "bebe nazca, porque es lo unico que revierte el cuadro.",
           "Vigilo plaquetas, transaminasas y datos de sangrado/CID. Es una urgencia obstetrica."),
    C + ["hellp"])

add(deck_core, caso("Sulfato de Mg: dosis y monitoreo"),
    manejo("<b>Carga 4-6 g IV en 20 min &rarr; mantenimiento 1-2 g/h IV</b> por 24 h posparto. "
           "<b>Vigilo</b>: reflejo patelar (si abolido, suspender), FR &ge;12, diuresis &ge;30 mL/h, niveles si insuf. renal.",
           "Le pondre sulfato de magnesio para prevenir convulsiones. Es normal sentir calor o pesadez; el equipo la "
           "vigilara de cerca mientras lo recibe.",
           "Los tres centinelas: reflejo patelar, respiracion y orina. Si caen, suspendo la infusion."),
    C + ["sulfato_mg"])

add(deck_core, caso("Intoxicacion por sulfato de Mg"),
    manejo("<b>Suspender la infusion</b> + <b>gluconato de calcio 1 g IV (10 mL al 10%) en 10 min</b>. "
           "Soporte ventilatorio si depresion respiratoria.",
           "(situacion de manejo intrahospitalario; se explica al acompanante) Hubo exceso de magnesio; lo revertimos "
           "con calcio intravenoso y vigilamos la respiracion.",
           "Antidoto = <b>gluconato de calcio</b>. Tenlo siempre a la mano cuando uses Mg."),
    C + ["sulfato_mg"])

add(deck_core, caso("Antihipertensivos en embarazo"),
    manejo("<b>Seguros:</b> alfa-metildopa (cronico), labetalol, hidralazina, nifedipino. "
           "<b>EVITAR:</b> IECA, ARA-II, inhibidores de renina, atenolol. Meta de TA 130-150 / 80-100 "
           "(no bajar de mas para no comprometer la perfusion uteroplacentaria).",
           "Le dare un medicamento para la presion que es seguro en el embarazo. Hay otros que no se pueden usar "
           "porque danan al bebe; por eso elegimos con cuidado.",
           "<b>Nunca IECA/ARA-II.</b> Es la trampa farmacologica que mas se pregunta."),
    C + ["hta_embarazo"])

add(deck_core, caso("Diabetes gestacional (DMG)"),
    manejo("1) <b>Dieta + ejercicio</b> y automonitoreo (metas: ayuno &lt;95, 1 h posprandial &lt;140, 2 h &lt;120). "
           "2) <b>Insulina</b> si no se alcanzan metas (1ra eleccion farmacologica) &plusmn; metformina. "
           "Vigilo crecimiento fetal y polihidramnios.",
           "Desarrollo diabetes propia del embarazo. La base es la alimentacion y el ejercicio; muchas se controlan "
           "asi. Si no basta, agregamos insulina, que es segura para el bebe.",
           "Controlar el azucar protege al bebe de crecer demasiado. Tras el parto repetimos la prueba: tiene mayor "
           "riesgo de diabetes a futuro."),
    C + ["dmg"])

add(deck_core, caso("Profilaxis intraparto para Estreptococo grupo B (EGB)"),
    manejo("<b>Penicilina G 5 millones UI IV de inicio, luego 2.5-3 millones c/4 h hasta el parto</b>. "
           "Alternativa ampicilina; alergica: cefazolina o clindamicina/vancomicina segun sensibilidad. "
           "Indicada si cultivo + (36-37 sem), bacteriuria por EGB, hijo previo con EGB o factores de riesgo.",
           "Una bacteria comun (estreptococo) puede pasar al bebe durante el parto. Le pondremos antibiotico en el "
           "trabajo de parto para protegerlo; no requiere tratamiento antes.",
           "El antibiotico es intraparto, cada 4 horas hasta que nazca. Ideal &ge;4 h antes del nacimiento."),
    C + ["egb"])

add(deck_core, caso("Amenaza de parto pretermino (24-34 sem)"),
    manejo("1) <b>Tocolisis 48 h</b>: nifedipino o atosiban. 2) <b>Maduracion pulmonar</b>: betametasona 12 mg IM "
           "c/24 h x2 (o dexametasona 6 mg IM c/12 h x4). 3) <b>Neuroproteccion con sulfato de Mg si &lt;32 sem</b>. "
           "4) Antibiotico para EGB segun cultivo.",
           "Su utero esta contrayendo antes de tiempo. Vamos a frenar las contracciones unas horas para dar tiempo a "
           "unos medicamentos que maduran los pulmones del bebe por si nace pronto.",
           "La tocolisis solo gana 48 h (la ventana del corticoide). No frena el parto indefinidamente."),
    C + ["pretermino"])

add(deck_core, caso("RPM pretermino (<34 sem)"),
    manejo("<b>Manejo expectante hospitalizado</b>: <b>antibiotico</b> (ampicilina + azitromicina/eritromicina 7 d) + "
           "<b>maduracion pulmonar</b> + vigilancia de corioamnionitis. Interrumpo si: corioamnionitis, sufrimiento "
           "fetal o se alcanzan 34 sem.",
           "Se rompio la fuente antes de tiempo. Como el bebe aun es muy prematuro, intentamos prolongar el embarazo "
           "con antibiotico y vigilancia, dandole corticoide para sus pulmones.",
           "Vigilo datos de infeccion: fiebre, dolor uterino, liquido fetido, taquicardia fetal. Si aparecen, se interrumpe."),
    C + ["rpm"])

add(deck_core, caso("Corioamnionitis"),
    manejo("<b>Antibiotico IV de amplio espectro</b>: ampicilina + gentamicina (anadir clindamicina/metronidazol si "
           "cesarea). <b>Interrupcion del embarazo independiente de la edad gestacional</b>. Antipireticos.",
           "Hay una infeccion dentro del utero que pone en riesgo a usted y al bebe. Iniciamos antibiotico y el bebe "
           "debe nacer pronto, sin importar las semanas, porque esperar es peligroso.",
           "Aqui la edad gestacional NO frena la conducta: antibiotico + interrupcion ya."),
    C + ["corioamnionitis"])

add(deck_core, caso("Isoinmunizacion Rh — profilaxis"),
    manejo("Madre <b>Rh negativa</b> no sensibilizada (Coombs indirecto -): <b>inmunoglobulina anti-D 300 mcg IM a "
           "las 28 sem</b> y <b>dentro de 72 h posparto si el RN es Rh+</b>. Tambien en eventos sensibilizantes "
           "(aborto, ectopico, amniocentesis, trauma, sangrado).",
           "Su sangre es Rh negativa y la del bebe podria ser positiva; su cuerpo podria formar defensas que afecten "
           "a este o a futuros embarazos. Una inyeccion lo previene.",
           "Es preventiva: a las 28 semanas y otra tras el parto si el bebe es Rh+. No sirve si ya esta sensibilizada."),
    C + ["rh"])


# ===================== SUBDECK 3 - MENOS (17) =====================
M = ["menos_preguntado"]
def menos(deck, titulo, v, c, ci, tags):
    add(deck, caso(titulo), manejo(v, c, ci), M + tags)

menos(deck_menos, "RPM a termino (>=37 sem)",
      "<b>Induccion del trabajo de parto</b> si no inicia espontaneamente (algunos inducen de inmediato). "
      "Profilaxis EGB segun cultivo/factores de riesgo.",
      "Se rompio la fuente y el bebe ya esta a termino, asi que lo mejor es que nazca. Si el trabajo de parto no "
      "empieza solo, lo inducimos.", "Evito demorar &gt;24 h por riesgo de infeccion.", ["rpm"])

menos(deck_menos, "Embarazo postermino (>=42 sem)",
      "<b>Vigilancia fetal</b> (RCTG + ILA/perfil biofisico) desde las 41 sem e <b>induccion del parto a las 41 sem</b> "
      "(no esperar a 42 por riesgo de insuficiencia placentaria).",
      "El embarazo paso de la fecha. Para evitar riesgos por una placenta que envejece, vigilamos al bebe e "
      "inducimos el parto.", "Datos de alarma: disminucion de movimientos fetales.", ["postermino"])

menos(deck_menos, "RCIU (restriccion del crecimiento)",
      "Confirmo con biometria &lt;p10 + <b>Doppler</b> (umbilical, ACM, ductus venoso). La conducta y el momento de "
      "<b>interrupcion</b> dependen del deterioro Doppler y la edad gestacional; corticoide si &lt;34 sem.",
      "El bebe esta creciendo menos de lo esperado. Vamos a vigilarlo de cerca con ecografias y Doppler para decidir "
      "el mejor momento para que nazca.", "Control de movimientos fetales y citas estrechas.", ["rciu"])

menos(deck_menos, "Bacteriuria asintomatica / IVU en embarazo",
      "<b>Bacteriuria asintomatica: SIEMPRE tratar</b> (urocultivo) con antibiotico seguro (nitrofurantoina -evitar a "
      "termino-, fosfomicina, cefalexina; <b>no quinolonas</b>). Pielonefritis: hospitalizar + IV. Urocultivo de control.",
      "En el embarazo, una infeccion urinaria aunque no de sintomas hay que tratarla, porque puede subir al rinon o "
      "adelantar el parto.", "Repito urocultivo tras el tratamiento para confirmar curacion.", ["ivu"])

menos(deck_menos, "TORCH en embarazo (enfoque)",
      "Tamizo/trato segun agente: <b>sifilis</b> (penicilina, desensibilizar si alergica), <b>toxoplasma</b> "
      "(espiramicina; pirimetamina-sulfa si fetal), <b>rubeola/CMV/VHS</b> (prevencion y manejo de soporte/antiviral). "
      "Evito vacunas vivas en embarazo.",
      "Hay infecciones que en el embarazo pueden afectar al bebe. Por eso las buscamos y, cuando hay tratamiento, lo "
      "iniciamos pronto; otras se previenen.", "La prevencion (higiene, evitar gato/carne cruda) cuenta tanto como tratar.", ["torch"])

menos(deck_menos, "Induccion del trabajo de parto",
      "Valoro <b>indice de Bishop</b>. <b>Cuello desfavorable (&lt;6):</b> maduracion con prostaglandinas (misoprostol/"
      "dinoprostona) o sonda Foley. <b>Favorable:</b> <b>oxitocina</b> + amniotomia. Monitoreo continuo de FCF.",
      "Vamos a iniciar el trabajo de parto con medicamentos. Primero preparamos el cuello si esta cerrado y luego "
      "estimulamos las contracciones, vigilando al bebe todo el tiempo.",
      "Misoprostol contraindicado con cesarea previa (riesgo de ruptura uterina).", ["induccion"])

menos(deck_menos, "Trabajo de parto verdadero vs falso",
      "<b>Verdadero:</b> contracciones regulares que aumentan + <b>cambios cervicales (borramiento/dilatacion)</b>. "
      "<b>Falso (Braxton-Hicks):</b> irregulares, sin cambio cervical, ceden con reposo. Ingreso en fase activa.",
      "Estas contracciones aun no modifican el cuello, asi que es un trabajo de parto falso; puede irse a casa y "
      "volver si se hacen regulares e intensas.",
      "Datos de regreso: contracciones c/5 min por 1 h, ruptura de fuente o sangrado.", ["trabajo_parto"])

menos(deck_menos, "Suplementacion en el embarazo",
      "<b>Acido folico 400 mcg/dia</b> (preconcepcional; <b>4-5 mg si antecedente de DTN</b>, diabetes o anticonvulsivos). "
      "<b>Hierro</b> profilactico/segun anemia. Calcio si dieta baja (reduce preeclampsia). Yodo segun zona.",
      "El acido folico desde antes del embarazo previene defectos del tubo neural del bebe; el hierro previene anemia. "
      "Se los indico de rutina.", "El folato funciona en las primeras semanas: idealmente desde antes de embarazarse.", ["suplementos"])

menos(deck_menos, "Vacunas en el embarazo (consejeria)",
      "<b>Recomendadas:</b> <b>Tdap</b> (27-36 sem, cada embarazo, protege de tos ferina), <b>influenza inactivada</b> "
      "(cualquier trimestre), COVID. <b>Contraindicadas: vacunas VIVAS</b> (SRP, varicela, fiebre amarilla salvo riesgo alto).",
      "Hay vacunas que la protegen a usted y al bebe, como la de tos ferina y la de influenza. Otras, las de virus "
      "vivos, se posponen para despues del parto.", "La Tdap se repite en cada embarazo aunque ya la tenga.", ["vacunas"])

menos(deck_menos, "Anticoncepcion posparto (consejeria)",
      "Lactancia: <b>solo progestina</b> (minipildora, implante, DIU-LNG) o DIU de cobre; <b>evitar estrogenos las "
      "primeras 6 semanas</b> (riesgo trombotico) y mientras la lactancia se establece. MELA si criterios estrictos.",
      "Despues del parto conviene un metodo compatible con la lactancia. Los de solo progestina y el DIU son ideales; "
      "los que llevan estrogeno se posponen unas semanas.",
      "El DIU puede colocarse posparto inmediato o a las 6 semanas. La lactancia sola no es metodo confiable.", ["anticoncepcion"])

menos(deck_menos, "HTA gestacional (sin proteinuria ni severidad)",
      "TA &ge;140/90 despues de las 20 sem <b>sin proteinuria ni datos de severidad</b>. Vigilancia estrecha "
      "(puede progresar a preeclampsia), antihipertensivo si persiste, interrupcion hacia las 37-39 sem.",
      "Subio la presion en el embarazo pero por ahora sin afectar otros organos. La vigilamos de cerca porque puede "
      "evolucionar, y planeamos el nacimiento cerca del termino.",
      "Diferencia con preeclampsia: aqui NO hay proteinuria ni datos de severidad. Puede convertirse: reviso en cada cita.", ["hta_gestacional"])

menos(deck_menos, "Amenaza de aborto",
      "<b>Reposo relativo</b>, abstinencia sexual, evitar esfuerzos. <b>Progesterona</b> si insuficiencia lutea o "
      "aborto recurrente. USG de control en 1-2 semanas. Anti-D si Rh negativa.",
      "Tiene sangrado pero el embarazo continua y el bebe esta vivo. Con reposo y cuidados, muchos embarazos siguen "
      "adelante.", "Datos de alarma: sangrado abundante, dolor intenso, expulsion de tejido o fiebre.", ["aborto"])

menos(deck_menos, "Maduracion pulmonar fetal (corticoide)",
      "<b>Betametasona 12 mg IM c/24 h x2</b> (o dexametasona 6 mg IM c/12 h x4) entre <b>24 y 34 sem</b> con riesgo "
      "de parto en 7 dias. Reduce SDR, hemorragia intraventricular y enterocolitis.",
      "Le pondre unas inyecciones que ayudan a madurar los pulmones del bebe por si nace antes de tiempo; mejoran "
      "mucho su respiracion al nacer.", "Maximo beneficio si nace entre 24 h y 7 dias despues de la primera dosis.", ["corticoide"])

menos(deck_menos, "Neuroproteccion fetal con Mg (<32 sem)",
      "<b>Sulfato de Mg</b> a la madre cuando hay parto pretermino inminente <b>&lt;32 sem</b>: reduce el riesgo de "
      "<b>paralisis cerebral</b> en el prematuro. Mismo monitoreo que en preeclampsia.",
      "Ademas de frenar y madurar, le doy magnesio para proteger el cerebro del bebe muy prematuro.",
      "Doble uso del Mg: anticonvulsivante en preeclampsia y neuroprotector en pretermino &lt;32 sem.", ["neuroproteccion"])

menos(deck_menos, "Tocolisis (para frenar contracciones)",
      "<b>Nifedipino</b> o <b>atosiban</b> (1ra eleccion); indometacina &lt;32 sem (cierre del ductus si &gt;32). "
      "Solo <b>48 h</b> para ganar la ventana del corticoide. <b>Contraindicada</b> si corioamnionitis, sufrimiento "
      "fetal, DPPNI o muerte fetal.",
      "Vamos a frenar las contracciones unas horas, no para evitar el parto siempre, sino para ganar tiempo y "
      "proteger al bebe con los otros medicamentos.",
      "No tocolizar si hay infeccion o sufrimiento fetal: ahi el bebe debe salir.", ["tocolisis"])

menos(deck_menos, "Sufrimiento fetal agudo (reanimacion intrauterina)",
      "<b>Reanimacion intrauterina</b>: decubito lateral izquierdo, O2, bolo de cristaloides, <b>suspender oxitocina</b>, "
      "corregir hipotension (efedrina), descartar prolapso de cordon (tacto). Si no mejora &rarr; <b>interrupcion urgente</b>.",
      "El bebe muestra signos de estres. Hacemos maniobras para mejorar su oxigenacion de inmediato; si no responde, "
      "procedemos al nacimiento urgente.", "El orden importa: reanimo primero, y si no mejora, cesarea.", ["sufrimiento_fetal"])

menos(deck_menos, "Interpretacion del RCTG (categorias)",
      "<b>Cat I:</b> FCF 110-160, variabilidad normal, sin desaceleraciones tardias/variables. <b>Cat II:</b> "
      "indeterminado. <b>Cat III:</b> variabilidad ausente + tardias/variables recurrentes o bradicardia, o sinusoidal. "
      "Desaceleraciones: tempranas (cabeza), variables (cordon), <b>tardias (hipoxia)</b>.",
      "Este registro vigila los latidos del bebe con las contracciones; me dice si esta tranquilo o si necesita ayuda.",
      "La tardia y la variabilidad ausente son las que asustan (hipoxia).", ["rctg"])


def build():
    for d, f in [(deck_ejes, "Manejo_01_Ejes.apkg"), (deck_core, "Manejo_02_Core.apkg"),
                 (deck_menos, "Manejo_03_Menos.apkg")]:
        genanki.Package(d).write_to_file(os.path.join(OUTPUT_DIR, f))
        print(f"  -> {f} ({len(d.notes)} notas)")
    genanki.Package([deck_ejes, deck_core, deck_menos]).write_to_file(
        os.path.join(OUTPUT_DIR, "No_Hay_Tiempo_Obst_Manejo_TODOS.apkg"))
    print(f"  -> TODOS ({sum(len(d.notes) for d in [deck_ejes, deck_core, deck_menos])} notas)")


if __name__ == "__main__":
    build()
