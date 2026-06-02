#!/usr/bin/env python3
"""
Simulación 3 — Trauma / Cirugía urgente (ATLS 11a ed., 2024)
Deck "Simulaciones::Trauma Cirugía - Repaso 3" (.apkg) + TSV de respaldo.

Uso (venv del repo):  ../../.venv/bin/python build_deck.py

Estructura por entidad: Abordaje (interrogatorio + exploración/verbalización) +
Manejo (dx + tratamiento + criterios de quirófano/referencia + frase ECOE) +
Caso escalonado (estable → respondedor/transitorio → inestable-crítico en una tarjeta).
10 entidades (Base xABCDE + 9 cuadros) × 3 = 30 tarjetas.
"""

import genanki

MODEL_QA_ID = 1607392320  # qa_estandar del repo (reusable)
DECK_ID = 2063900330      # registrado en ids.json
DECK_NAME = "Simulaciones::Trauma Cirugía - Repaso 3"

MODEL = genanki.Model(
    MODEL_QA_ID,
    "Estudio Medico QA",
    fields=[{"name": "Front"}, {"name": "Back"}],
    templates=[{
        "name": "QA",
        "qfmt": "{{Front}}",
        "afmt": '{{Front}}<hr id="extra">{{Back}}',
    }],
    css="""
.card { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
        font-size: 19px; text-align: left; color: #1a1a1a;
        background-color: #fafafa; padding: 20px; line-height: 1.55; }
b { color: #b45309; }
i { color: #2563eb; }
ul { margin: 8px 0 8px 22px; }
li { margin: 7px 0; }
#extra { margin-top: 16px; border: none; border-top: 1px solid #d4d4d4; padding-top: 12px; }
""",
)

DECK = genanki.Deck(DECK_ID, DECK_NAME)

# (Front, Back, [tags])
CARDS = [
    # ===================== Base — Politraumatizado / xABCDE =====================
    ('<b>BASE — Politraumatizado (xABCDE):</b> ¿qué interrogo y cómo verbalizo la evaluación primaria?',
     '<b>Interrogatorio breve (AMPLIA / "qué pasó"):</b> <ul><li>¿<b>Qué pasó y cuándo</b>? <b>mecanismo</b> (energía, velocidad, caída, arma) → predice el patrón lesional.</li><li><b>Dolor principal</b>, <b>alergias</b>, <b>medicamentos</b> (anticoagulantes), <b>antecedentes</b>, <b>última comida</b> (riesgo anestésico) y <b>embarazo</b> si es mujer fértil.</li></ul><br><b>Exploración — evaluación primaria.</b> <i>Verbalizo:</i> «<b>x:</b> primero <b>control de hemorragia exanguinante</b> (presión directa, torniquete o agente hemostático). <b>A:</b> ¿habla?, vía aérea permeable <b>con control cervical</b>. <b>B:</b> evalúo tórax, saturación y ruidos respiratorios. <b>C:</b> pulso, TA, piel, llenado capilar y control de hemorragia. <b>D:</b> Glasgow, pupilas y glucosa. <b>E:</b> expongo completo, busco lesiones ocultas y prevengo hipotermia.»<ul><li>ATLS 11 antepone la <b>x</b> (hemorragia exanguinante) a la A: el sangrado masivo se controla <b>antes</b> que la vía aérea.</li><li>Adjuntos a la primaria (sobre todo en C): <b>eFAST + Rx tórax + Rx pelvis</b> a pie de cama.</li></ul>',
     ['Simulacion3::Trauma-Cirugia::Base-xABCDE', 'Abordaje']),

    ('<b>BASE — Politraumatizado:</b> material, accesos y reanimación de control de daños',
     '<b>Material base:</b> monitor, <b>oxígeno</b>, <b>2 vías periféricas cortas y gruesas 16G/18G</b> (si no se logra acceso rápido → <b>vía intraósea</b>), grupo/Rh y pruebas cruzadas, BH, coagulación, gasometría/lactato.<br><b>Reanimación de control de daños (ATLS 11):</b><ul><li><b>Hipotensión permisiva</b> y <b>minimizar cristaloides</b>: el <b>Ringer lactato tibio</b> es solo <b>fluido puente</b> hasta tener sangre.</li><li>En shock hemorrágico, la reanimación de elección es <b>hemoderivados precoces</b>: <b>transfusión masiva 1:1:1</b> (eritrocitos:plasma:plaquetas) o <b>sangre total O negativo</b> de bajo título.</li><li><b>Ácido tranexámico (TXA) 1 g IV en &lt;3 h</b> + infusión de 1 g (2 g si TCE).</li><li>Cuando haya TEG/ROTEM o laboratorio → transición a terapia guiada por objetivos.</li></ul><i>ECOE:</i> «Activo el protocolo de transfusión masiva 1:1:1 y uso el cristaloide solo como puente.»',
     ['Simulacion3::Trauma-Cirugia::Base-xABCDE', 'Manejo']),

    ('<b>BASE — Politraumatizado:</b> principio integrador (frase final global)',
     '<i>ECOE (cierre global):</i> «Paciente politraumatizado: realizo <b>xABCDE</b>, identifico la <b>amenaza vital dominante</b> y la <b>trato de inmediato sin esperar estudios si el diagnóstico es clínico</b>, coloco <b>accesos gruesos</b>, reanimo con <b>cristaloides tibios como puente y hemoderivados si hay shock</b>, solicito <b>eFAST/Rx dirigidas</b> y <b>activo cirugía/trauma</b> para el control definitivo.»<br><br><b>Regla de oro:</b> los diagnósticos clínicos (neumotórax a tensión, taponamiento, hemorragia exanguinante) <b>se tratan antes de la imagen</b>; el inestable <b>no va al TAC</b>, va a quirófano o a la intervención salvadora.',
     ['Simulacion3::Trauma-Cirugia::Base-xABCDE', 'Principio']),

    # ===================== 1. Objeto penetrante encajado (impalado) =====================
    ('<b>Objeto penetrante encajado (impalado) — Abordaje:</b> ¿qué pregunto, cómo exploro y qué verbalizo?',
     '<b>Interrogatorio.</b> <ul><li><b>Mecanismo, tipo y tamaño del objeto, tiempo</b> → predice trayecto y estructuras en riesgo.</li><li>Dolor, sangrado, alergias, medicamentos (anticoagulantes), última comida, embarazo.</li></ul><br><b>Exploración.</b> <i>Verbalizo:</i> «Aplico el <b>xABCDE</b>; <b>NO movilizo el objeto</b>. Busco sangrado externo y lo controlo, exploro el abdomen, palpo <b>pulsos distales</b> al sitio, evalúo perfusión y déficit neurológico, y rastreo <b>otras heridas y el orificio de salida</b>.» <ul><li><b>No retiro ni movilizo el objeto:</b> puede estar tamponando el sangrado.</li><li>Valoro estabilidad hemodinámica, signos de peritonitis y compromiso vascular/neurológico distal.</li></ul>',
     ['Simulacion3::Trauma-Cirugia::ObjetoEncajado', 'Abordaje']),

    ('<b>Objeto penetrante encajado (impalado) — Manejo:</b> Dx + conducta + criterios de quirófano',
     '<b>Clave: NO retirar.</b> «Objeto in situ: no lo retiro porque puede estar tamponando el sangrado; lo <b>estabilizo con gasas voluminosas y vendaje</b>.»<br><b>Soporte:</b> 2 vías gruesas, cristaloide tibio como puente, <b>sangre si shock</b>, <b>analgesia (fentanilo 25–50 mcg IV titulado)</b>.<br><b>Estudios:</b> si <b>estable</b> → <b>TAC con contraste</b>; si <b>inestable / peritonitis</b> → <b>quirófano</b>.<br><b>El impalamiento es por sí mismo indicación de quirófano:</b> la <b>retirada definitiva la hace el cirujano en quirófano</b>, en entorno controlado.<br><i>ECOE:</i> «Objeto impalado: lo estabilizo, no lo retiro, y traslado a quirófano para extracción controlada.»',
     ['Simulacion3::Trauma-Cirugia::ObjetoEncajado', 'Manejo']),

    ('<b>OBJETO PENETRANTE ENCAJADO — Caso escalonado.</b> ¿Conducta en estable → dudoso → inestable?',
     '<ul><li><b>Estable:</b> Varón de 30 años con cuchillo encajado en flanco, consciente, TA y FC normales, sin peritonitis. → <b>estabilizar el objeto</b> con gasas voluminosas, analgesia, 2 vías, y <b>TAC con contraste</b> para planear la extracción quirúrgica.</li><li><b>Dudoso/transitorio:</b> Mismo paciente con barra metálica en abdomen, taquicárdico que mejora con líquidos pero con dolor abdominal creciente. → <b>no demorar</b>: respondedor transitorio + dolor abdominal → <b>quirófano</b>; mantener objeto in situ y activar reserva de sangre.</li><li><b>Inestable:</b> Mujer con objeto torácico/abdominal impalado, hipotensa, diaforética y con abdomen rígido. → <b>quirófano inmediato</b> con <b>transfusión masiva 1:1:1</b>; nunca retirar el objeto fuera del quirófano.</li></ul>',
     ['Simulacion3::Trauma-Cirugia::ObjetoEncajado', 'Caso']),

    # ===================== 2. Trauma penetrante inestable =====================
    ('<b>Trauma penetrante inestable — Abordaje:</b> ¿qué pregunto, cómo exploro y qué verbalizo?',
     '<b>Interrogatorio (breve, no demorar):</b> arma (blanca/fuego), número de heridas, tiempo, sangrado en el lugar, dolor; AMPLIA si el tiempo lo permite.<br><b>Exploración.</b> <i>Verbalizo:</i> «<b>xABCDE rápido</b> con <b>control de hemorragia</b>; cuento orificios de entrada/salida; busco <b>abdomen rígido/peritonitis</b> y <b>evisceración</b>; valoro pulsos y perfusión; hago <b>eFAST</b> (pericárdica + abdominal).» <ul><li><b>Dx sindromático:</b> trauma penetrante con <b>shock hemorrágico</b>.</li><li>«Paciente hipotenso, taquicárdico y diaforético: <b>shock hemorrágico hasta demostrar lo contrario</b>.»</li><li><b>FAST positivo</b> apoya quirófano; un <b>FAST negativo NO excluye</b> lesión y no debe retrasar la cirugía.</li></ul>',
     ['Simulacion3::Trauma-Cirugia::PenetranteInestable', 'Abordaje']),

    ('<b>Trauma penetrante inestable — Manejo:</b> Dx + conducta + criterios de quirófano',
     '<b>Dx:</b> trauma penetrante con shock hemorrágico.<br><b>Conducta:</b> <b>NO TAC</b>. <b>Quirófano</b> + <b>activar transfusión masiva 1:1:1</b> (o sangre total), cristaloide solo como puente, TXA.<br><b>Criterios de laparotomía/quirófano inmediato:</b><ul><li><b>Inestabilidad hemodinámica</b> (por sí sola ya indica quirófano).</li><li><b>Peritonitis.</b></li><li><b>Evisceración.</b></li><li><b>Impalamiento.</b></li><li><b>eFAST positivo</b> / sangrado activo.</li></ul><i>ECOE:</i> «Penetrante inestable: no pierdo tiempo en TAC; activo transfusión masiva y lo llevo a quirófano.»',
     ['Simulacion3::Trauma-Cirugia::PenetranteInestable', 'Manejo']),

    ('<b>TRAUMA PENETRANTE — Caso escalonado.</b> ¿Conducta en estable → respondedor → inestable?',
     '<ul><li><b>Estable:</b> Herida por arma blanca en abdomen anterior, paciente consciente, hemodinámicamente estable, abdomen sin peritonitis. → reanimación, observación seriada y <b>TAC con contraste</b> (puede ser candidato a manejo selectivo no operatorio).</li><li><b>Respondedor transitorio:</b> Herida abdominal con TA 90/60 y FC 120 que mejora con líquidos pero vuelve a caer. → respondedor transitorio = <b>sangrado activo</b> → <b>quirófano</b> y transfusión 1:1:1.</li><li><b>Inestable:</b> Herida por arma de fuego toracoabdominal, hipotenso, diaforético, abdomen rígido / eFAST positivo. → <b>quirófano inmediato sin TAC</b>, transfusión masiva. Recuerda: FAST negativo no lo descarta.</li></ul>',
     ['Simulacion3::Trauma-Cirugia::PenetranteInestable', 'Caso']),

    # ===================== 3. Trauma cerrado / politrauma =====================
    ('<b>Trauma cerrado / politrauma — Abordaje:</b> ¿qué pregunto, cómo exploro y qué verbalizo?',
     '<b>Interrogatorio (cinemática):</b> <ul><li><b>Choque y velocidad</b>, uso de <b>cinturón</b>, <b>expulsión</b> del vehículo, <b>pérdida de conciencia</b>, deformidad del habitáculo, muertos en la escena → marcadores de alta energía.</li><li>Dolor en <b>tórax / abdomen / pelvis</b>; AMPLIA.</li></ul><br><b>Exploración.</b> <i>Verbalizo:</i> «<b>xABCDE</b>; exploro <b>tórax, abdomen, pelvis, huesos largos y dorso</b> (rodando al paciente en bloque); <b>busco fuentes ocultas de sangrado</b>.» <ul><li>«Busco fuentes ocultas de sangrado: <b>tórax, abdomen, pelvis y huesos largos</b>» (los 5 sitios del shock hemorrágico, + "el suelo").</li><li>Adjuntos de la primaria: <b>eFAST + Rx tórax + Rx pelvis</b>.</li></ul>',
     ['Simulacion3::Trauma-Cirugia::CerradoPolitrauma', 'Abordaje']),

    ('<b>Trauma cerrado / politrauma — Manejo:</b> Dx + conducta + cuándo a quirófano vs TAC',
     '<b>Conducta:</b> <b>xABCDE</b>, oxígeno si SatO2 baja, <b>2 vías gruesas</b>, <b>cristaloide tibio como puente</b> y <b>transfusión 1:1:1 si no responde</b>, TXA.<br><b>Estudios de la evaluación primaria:</b> <b>eFAST + Rx tórax + Rx pelvis</b> a pie de cama.<br><b>Decisión:</b><ul><li><b>Estable</b> → <b>TAC</b> (body-TAC) para mapear lesiones.</li><li><b>Inestable</b> que no responde + <b>eFAST positivo</b> → <b>quirófano</b>, no TAC.</li></ul><i>ECOE:</i> «Reanimo, identifico el foco de sangrado dominante y decido TAC si estable o quirófano si inestable.»',
     ['Simulacion3::Trauma-Cirugia::CerradoPolitrauma', 'Manejo']),

    ('<b>TRAUMA CERRADO / POLITRAUMA — Caso escalonado.</b> ¿Conducta en estable → respondedor → inestable?',
     '<ul><li><b>Estable:</b> Colisión a baja velocidad, con cinturón, consciente, vitales normales, dolor abdominal leve. → reanimación, monitorización y <b>TAC</b> dirigido; observación seriada.</li><li><b>Respondedor transitorio:</b> Atropello con dolor abdominal y pélvico, TA 95/60, FC 118 que mejora parcialmente con líquidos. → <b>eFAST + Rx pelvis/tórax</b>; si FAST+ o sangrado persistente → <b>quirófano/angioembolización</b> + transfusión.</li><li><b>Inestable:</b> Expulsado del vehículo, hipotenso, taquicárdico, eFAST positivo. → <b>quirófano inmediato</b> con transfusión masiva 1:1:1; no demorar en TAC.</li></ul>',
     ['Simulacion3::Trauma-Cirugia::CerradoPolitrauma', 'Caso']),

    # ===================== 4. Lesión esplénica / signo de Kehr =====================
    ('<b>Lesión esplénica / signo de Kehr — Abordaje:</b> ¿qué pregunto, cómo exploro y qué verbalizo?',
     '<b>Interrogatorio.</b> <ul><li>Mecanismo (trauma cerrado en <b>hipocondrio/flanco izquierdo</b>, costillas bajas izquierdas), dolor abdominal y <b>dolor referido al hombro izquierdo</b>.</li><li>AMPLIA; síntomas de hipovolemia (mareo, sed).</li></ul><br><b>Exploración.</b> <i>Verbalizo:</i> «Exploro el abdomen buscando dolor y defensa en <b>hipocondrio izquierdo</b>, signos de <b>peritonitis</b> e hipovolemia; hago <b>eFAST con ventana periesplénica</b> (esplenorrenal).» <ul><li><b>Clave:</b> trauma + dolor en hipocondrio izquierdo + <b>dolor en hombro izquierdo</b>.</li><li>«<b>Signo de Kehr:</b> sospecho irritación diafragmática por <b>hemoperitoneo</b> secundario a lesión esplénica» (dolor referido por el nervio frénico).</li></ul>',
     ['Simulacion3::Trauma-Cirugia::LesionEsplenica', 'Abordaje']),

    ('<b>Lesión esplénica — Manejo:</b> Dx + manejo operatorio vs no operatorio (NOM) + frase ECOE',
     '<b>Estudios:</b> <b>eFAST</b>. Si <b>estable</b> → <b>TAC con contraste</b> (gradúa la lesión). Si <b>inestable + FAST positivo</b> → <b>laparotomía</b>.<br><b>Soporte:</b> 2 vías, RL tibio como puente, <b>transfusión masiva si shock</b>, cirugía urgente si inestable.<br><b>Manejo no operatorio (NOM):</b> reservado a <b>hemodinámicamente estables, sin peritonitis</b>, con <b>capacidad de vigilancia seriada y quirófano disponible</b>; puede complementarse con <b>angioembolización</b> en lesiones de alto grado con blush/pseudoaneurisma.<br><i>ECOE:</i> «Lesión esplénica: si está estable, TAC y manejo no operatorio vigilado; si está inestable con FAST+, laparotomía.»',
     ['Simulacion3::Trauma-Cirugia::LesionEsplenica', 'Manejo']),

    ('<b>LESIÓN ESPLÉNICA — Caso escalonado.</b> ¿Conducta en estable → alto grado → inestable?',
     '<ul><li><b>Estable:</b> Joven tras caída de bici con dolor en hipocondrio izquierdo y Kehr, vitales normales. → <b>TAC con contraste</b>; lesión de bajo grado → <b>NOM</b> con vigilancia (Hto seriado, exploraciones) en sitio con quirófano disponible.</li><li><b>Alto grado/estable:</b> Lesión esplénica grado alto con <b>blush</b> arterial en TAC pero paciente estable. → <b>NOM + angioembolización</b>; vigilancia estrecha.</li><li><b>Inestable:</b> Trauma de flanco izquierdo, hipotenso, FAST positivo con líquido libre. → <b>laparotomía urgente</b> (esplenectomía/reparación) + transfusión masiva 1:1:1.</li></ul>',
     ['Simulacion3::Trauma-Cirugia::LesionEsplenica', 'Caso']),

    # ===================== 5. Neumotórax a tensión =====================
    ('<b>Neumotórax a tensión — Abordaje:</b> ¿qué busco, cómo exploro y qué verbalizo?',
     '<b>Reconocimiento (clínico, no esperar Rx):</b> <ul><li><b>Disnea intensa, SatO2 baja, hipotensión</b> (shock obstructivo).</li><li><b>Ausencia de murmullo vesicular unilateral</b> + <b>hiperresonancia</b> a la percusión.</li><li><b>Ingurgitación yugular</b>; <b>desviación traqueal</b> (signo tardío).</li></ul><br><b>Exploración.</b> <i>Verbalizo:</i> «Inspecciono el trabajo respiratorio y la simetría torácica, <b>ausculto y percuto ambos hemitórax</b>, valoro tráquea y yugulares, y mido SatO2/TA. <b>No espero la radiografía</b>: es un diagnóstico clínico.» <ul><li>«<b>Neumotórax a tensión es diagnóstico clínico; no espero radiografía.</b>»</li></ul>',
     ['Simulacion3::Trauma-Cirugia::NeumotoraxTension', 'Abordaje']),

    ('<b>Neumotórax a tensión — Manejo:</b> descompresión inmediata + tubo definitivo',
     '<b>Manejo (no demorar):</b><ul><li><b>Oxígeno con reservorio 15 L/min</b> si respira.</li><li><b>Descompresión inmediata con aguja:</b> <b>5º espacio intercostal, línea axilar anterior/media</b>, sobre el <b>borde superior de la costilla</b> (catéter ≥8 cm). Alternativa aceptable: 2º EIC línea medioclavicular (en <b>pediatría</b> se conserva el 2º EIC LMC).</li><li>Luego <b>tubo de tórax definitivo</b> (triángulo de seguridad, 4º–5º EIC anterior a la línea axilar media).</li><li><b>Rx de control</b> después.</li></ul>La aguja es solo <b>medida temporal</b> hasta el tubo.<br><i>ECOE:</i> «Neumotórax a tensión: descomprimo de inmediato y luego coloco tubo de tórax; la radiografía es de control.»',
     ['Simulacion3::Trauma-Cirugia::NeumotoraxTension', 'Manejo']),

    ('<b>NEUMOTÓRAX A TENSIÓN — Caso escalonado.</b> ¿Conducta en simple → a tensión → paro inminente?',
     '<ul><li><b>Neumotórax simple (estable):</b> Trauma torácico, disnea leve, SatO2 94%, murmullo algo disminuido, <b>sin</b> hipotensión ni desviación traqueal. → oxígeno, <b>Rx/TAC</b> y <b>tubo de tórax</b> programado; vigilar.</li><li><b>A tensión:</b> Disnea grave, SatO2 85%, TA 80/50, hemitórax silente e hiperresonante, yugulares ingurgitadas. → <b>descompresión con aguja inmediata</b> (5º EIC LAA/LAM) <b>sin esperar Rx</b> + reservorio 15 L/min, luego tubo.</li><li><b>Paro inminente:</b> Cianótico, casi sin pulso tras descompresión con aguja. → <b>tubo de tórax urgente</b> (o toracostomía con dedo) y reanimación; reevaluar otras causas de shock obstructivo (taponamiento).</li></ul>',
     ['Simulacion3::Trauma-Cirugia::NeumotoraxTension', 'Caso']),

    # ===================== 6. Taponamiento cardíaco =====================
    ('<b>Taponamiento cardíaco — Abordaje:</b> tríada de Beck, exploración y verbalización',
     '<b>Reconocimiento:</b> <b>tríada de Beck</b> = <b>hipotensión + ingurgitación yugular + ruidos cardíacos apagados</b> (shock obstructivo). Suele faltar: es <b>poco sensible y tardía</b>.<br><b>Exploración.</b> <i>Verbalizo:</i> «Ausculto los focos cardíacos: <b>aórtico (2º EIC derecho)</b>, <b>pulmonar (2º EIC izquierdo)</b>, <b>tricuspídeo (borde esternal inferior)</b> y <b>mitral (5º EIC línea medioclavicular)</b>; valoro yugulares y TA, y descarto neumotórax a tensión como causa de shock obstructivo.» <ul><li>«Paciente con <b>shock obstructivo</b> por probable <b>taponamiento cardíaco</b>.»</li><li><b>Estudio de elección:</b> <b>eFAST ventana subxifoidea</b> → líquido pericárdico.</li></ul>',
     ['Simulacion3::Trauma-Cirugia::Taponamiento', 'Abordaje']),

    ('<b>Taponamiento cardíaco — Manejo:</b> puente + tratamiento definitivo',
     '<b>Soporte (puente):</b> 2 vías, <b>líquidos/hemoderivados</b> para mantener precarga mientras se resuelve.<br><b>Tratamiento DEFINITIVO = cirugía:</b> <b>ventana pericárdica / toracotomía o esternotomía</b> con reparación. En trauma, es la intervención principal.<br><b>Pericardiocentesis guiada por USG:</b> solo <b>medida temporizadora/puente</b> si hay deterioro y <b>no hay cirujano/quirófano de inmediato</b>; tiene <b>falsos negativos</b> (sangre coagulada) y no sustituye a la cirugía.<br><i>ECOE:</i> «Taponamiento traumático: estabilizo con volumen y activo cirugía; la pericardiocentesis es solo puente si no hay quirófano disponible.»',
     ['Simulacion3::Trauma-Cirugia::Taponamiento', 'Manejo']),

    ('<b>TAPONAMIENTO CARDÍACO — Caso escalonado.</b> ¿Conducta en sospecha estable → deterioro → paro?',
     '<ul><li><b>Sospecha/estable:</b> Herida precordial, TA en límite bajo, eFAST subxifoideo con derrame pericárdico pequeño. → <b>volumen</b> como puente, <b>activar cirugía</b> (ventana pericárdica/quirófano) y monitorización estrecha.</li><li><b>Deterioro:</b> Tríada de Beck franca, hipotensión que no responde a líquidos, derrame en aumento. → <b>quirófano urgente</b>; si no hay cirujano disponible de inmediato → <b>pericardiocentesis guiada por USG como puente</b>.</li><li><b>Paro / actividad eléctrica sin pulso:</b> Trauma penetrante torácico con PEA reciente. → <b>toracotomía de reanimación</b> con pericardiotomía; transfusión masiva.</li></ul>',
     ['Simulacion3::Trauma-Cirugia::Taponamiento', 'Caso']),

    # ===================== 7. Hemotórax masivo =====================
    ('<b>Hemotórax masivo — Abordaje:</b> ¿qué busco, cómo exploro y qué verbalizo?',
     '<b>Reconocimiento:</b> <b>disnea + shock</b> + <b>ausencia de murmullo vesicular unilateral</b> + <b>matidez</b> a la percusión.<br><b>Exploración.</b> <i>Verbalizo:</i> «Valoro trabajo respiratorio, SatO2 y TA; <b>ausculto y percuto</b> ambos hemitórax buscando <b>matidez y silencio auscultatorio</b>; hago <b>eFAST/Rx tórax</b>, pero <b>si está inestable no retraso el drenaje</b>.» <ul><li>«<b>Matidez a la percusión y ausencia de murmullo vesicular</b> sugieren sangre en la cavidad pleural.»</li><li>Diferencia del neumotórax a tensión: aquí hay <b>matidez</b> (no hiperresonancia).</li></ul>',
     ['Simulacion3::Trauma-Cirugia::HemotoraxMasivo', 'Abordaje']),

    ('<b>Hemotórax masivo — Manejo:</b> drenaje + reanimación + umbral de toracotomía',
     '<b>Manejo:</b><ul><li><b>Oxígeno reservorio 15 L/min</b>; <b>2 vías 16G/18G</b>.</li><li><b>Transfusión masiva 1:1:1</b> si shock (reanimación simultánea al drenaje).</li><li><b>Tubo de tórax</b> (4º–5º EIC, línea axilar media/anterior).</li></ul><b>Definición:</b> hemotórax masivo = <b>&gt;1500 mL inmediatos</b> (o ≥1/3 de la volemia).<br><b>Toracotomía si:</b> <b>drenaje inicial &gt;1500 mL</b>, o <b>sangrado persistente &gt;200 mL/h durante 2–4 h</b>, o necesidad continua de transfusión (también guía el estado hemodinámico).<br><i>ECOE:</i> «Hemotórax masivo: coloco tubo de tórax y reanimo con sangre; si drena &gt;1500 mL o sigue sangrando, toracotomía.»',
     ['Simulacion3::Trauma-Cirugia::HemotoraxMasivo', 'Manejo']),

    ('<b>HEMOTÓRAX MASIVO — Caso escalonado.</b> ¿Conducta en moderado → masivo → sangrado persistente?',
     '<ul><li><b>Moderado/estable:</b> Trauma torácico con matidez basal, SatO2 93%, TA normal; Rx con hemotórax moderado. → <b>tubo de tórax</b> y vigilancia del débito; oxígeno.</li><li><b>Masivo:</b> Disnea, shock, hemitórax mate y silente; al colocar el tubo drena <b>1800 mL de sangre</b>. → <b>transfusión masiva 1:1:1</b> + <b>toracotomía</b> (&gt;1500 mL inmediatos).</li><li><b>Sangrado persistente:</b> Drenaje inicial de 1000 mL pero continúa con <b>250 mL/h</b> durante horas e inestabilidad. → <b>toracotomía</b> por sangrado persistente / necesidad continua de transfusión.</li></ul>',
     ['Simulacion3::Trauma-Cirugia::HemotoraxMasivo', 'Caso']),

    # ===================== 8. Tórax inestable / flail chest =====================
    ('<b>Tórax inestable / flail chest — Abordaje:</b> ¿qué busco, cómo exploro y qué verbalizo?',
     '<b>Dx:</b> trauma cerrado + <b>movimiento paradójico</b> de la pared torácica (≥2 costillas fracturadas en ≥2 puntos).<br><b>Exploración.</b> <i>Verbalizo:</i> «Observo la pared torácica en cada respiración buscando el <b>segmento que se hunde en la inspiración</b> (movimiento paradójico), palpo crepitación y dolor, <b>ausculto</b>, mido SatO2 y vigilo signos de <b>contusión pulmonar</b> subyacente.» <ul><li>«<b>Movimiento paradójico</b> de la pared compatible con <b>tórax inestable</b> por fracturas costales múltiples.»</li><li>La verdadera amenaza es la <b>contusión pulmonar</b> subyacente.</li></ul>',
     ['Simulacion3::Trauma-Cirugia::FlailChest', 'Abordaje']),

    ('<b>Tórax inestable / flail chest — Manejo:</b> analgesia, soporte y vigilancia',
     '<b>Manejo (pilares):</b><ul><li><b>Oxígeno reservorio 15 L/min</b> si hipoxemia.</li><li><b>Analgesia agresiva</b> (clave): <b>fentanilo 25–50 mcg IV titulado</b>; en casos graves, analgesia regional/epidural.</li><li><b>Fisioterapia respiratoria y movilización</b>.</li><li><b>Rx/TAC</b> si estable.</li><li><b>Monitorizar contusión pulmonar:</b> SatO2, FR, trabajo respiratorio, gasometría; reanimación hídrica juiciosa.</li><li><b>Intubación/ventilación solo si hay falla respiratoria</b> (no de rutina).</li></ul>El control del dolor, la fisioterapia respiratoria y la movilización son los pilares del trauma torácico cerrado.<br><i>ECOE:</i> «Tórax inestable: analgesia agresiva, fisioterapia y vigilancia de contusión pulmonar; intubo solo si falla la respiración.»',
     ['Simulacion3::Trauma-Cirugia::FlailChest', 'Manejo']),

    ('<b>TÓRAX INESTABLE / FLAIL CHEST — Caso escalonado.</b> ¿Conducta en leve → moderado → falla respiratoria?',
     '<ul><li><b>Leve:</b> Fracturas costales múltiples con segmento paradójico pequeño, SatO2 95%, buen esfuerzo. → <b>analgesia</b> (fentanilo titulado) + <b>fisioterapia respiratoria</b> + vigilancia; Rx/TAC.</li><li><b>Moderado:</b> Movimiento paradójico evidente, dolor que limita la respiración, SatO2 90%, signos de <b>contusión pulmonar</b>. → optimizar analgesia (regional/epidural), oxígeno, vigilancia estrecha de gasometría y trabajo respiratorio.</li><li><b>Falla respiratoria:</b> Hipoxemia refractaria, fatiga, hipercapnia pese a soporte. → <b>intubación y ventilación</b>; valorar manejo en UCI ± fijación costal quirúrgica (SSRF) en casos seleccionados.</li></ul>',
     ['Simulacion3::Trauma-Cirugia::FlailChest', 'Caso']),

    # ===================== 9. Fractura pélvica inestable =====================
    ('<b>Fractura pélvica inestable — Abordaje:</b> ¿qué pregunto, cómo exploro y qué verbalizo?',
     '<b>Interrogatorio:</b> trauma de <b>alta energía</b> (atropello, caída de altura, moto), <b>dolor pélvico</b>, incapacidad para bipedestar; AMPLIA; sangre en meato/recto/vagina.<br><b>Exploración.</b> <i>Verbalizo:</i> «Hago <b>una sola compresión suave</b> del anillo pélvico para valorar dolor/inestabilidad y <b>no la repito</b> (evito desplazar coágulos / movilizar el anillo); inspecciono periné, busco sangre en meato/recto/vagina, y hago <b>eFAST + Rx AP de pelvis</b>.» <ul><li>«Sospecho <b>fractura pélvica inestable</b> con <b>hemorragia retroperitoneal</b>.»</li><li>Trauma alta energía + dolor pélvico + hipotensión = sangrado pélvico hasta demostrar lo contrario.</li></ul>',
     ['Simulacion3::Trauma-Cirugia::FracturaPelvica', 'Abordaje']),

    ('<b>Fractura pélvica inestable — Manejo:</b> binder, reanimación y control hemorrágico',
     '<b>Manejo:</b><ul><li><b>Binder pélvico a nivel de los TROCÁNTERES MAYORES</b> (no en la cintura/crestas: colocarlo alto puede abrir el anillo) con compresión controlada.</li><li><b>2 vías gruesas</b>; <b>RL tibio como puente</b>, <b>transfusión masiva 1:1:1 o sangre total si hipotenso</b>, TXA.</li><li><b>eFAST + Rx AP de pelvis</b>.</li><li>Si persiste el sangrado → <b>trauma/ortopedia + angioembolización o fijación externa</b> (± packing preperitoneal/REBOA según recursos).</li></ul><i>ECOE:</i> «Fractura pélvica inestable: coloco binder en trocánteres mayores, transfundo 1:1:1 y, si sigue sangrando, angioembolización o fijación externa.»',
     ['Simulacion3::Trauma-Cirugia::FracturaPelvica', 'Manejo']),

    ('<b>FRACTURA PÉLVICA INESTABLE — Caso escalonado.</b> ¿Conducta en estable → respondedor → inestable?',
     '<ul><li><b>Estable:</b> Caída con dolor pélvico, vitales normales, Rx con fractura sin gran desplazamiento. → analgesia, <b>TAC</b> para caracterizar, manejo ortopédico; vigilancia.</li><li><b>Respondedor transitorio:</b> Atropello con dolor pélvico, TA 90/60 que mejora con líquidos pero recae; Rx con fractura inestable. → <b>binder en trocánteres mayores</b>, transfusión 1:1:1 y <b>angioembolización/fijación externa</b>.</li><li><b>Inestable:</b> Alta energía, hipotensión que no responde, anillo pélvico abierto. → <b>binder + transfusión masiva</b> y control hemorrágico urgente (angioembolización/fijación externa ± packing preperitoneal/REBOA). Descartar otras fuentes con eFAST.</li></ul>',
     ['Simulacion3::Trauma-Cirugia::FracturaPelvica', 'Caso']),
]


def main():
    for front, back, tags in CARDS:
        DECK.add_note(genanki.Note(model=MODEL, fields=[front, back], tags=tags))
    genanki.Package(DECK).write_to_file("simulacion-3-trauma-cirugia.apkg")
    with open("simulacion-3-trauma-cirugia.tsv", "w", encoding="utf-8") as f:
        for front, back, tags in CARDS:
            f.write(f"{front}\t{back}\t{' '.join(tags)}\n")
    print(f"Listo: {len(CARDS)} tarjetas -> simulacion-3-trauma-cirugia.apkg + .tsv")


if __name__ == "__main__":
    main()
