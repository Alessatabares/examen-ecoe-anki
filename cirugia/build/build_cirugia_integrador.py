"""Deck INTEGRADOR de Cirugia (Adulto) - agrupadores y clasificaciones.

Reagrupa el contenido de la Capa 1 (Reconocimiento de Patron Quirurgico) en sentido
inverso: de "caso -> entidad" a "categoria paraguas -> subtipos + el parametro que
los separa". Formato Q&A con tablas.

Generado con un workflow multi-agente (agrupacion por dominio quirurgico + verificacion
adversarial de cifras/criterios contra ATLS 10a, Tokyo 2018, Atlanta revisada, Alvarado,
Hinchey, Forrest, Stanford, Surviving Sepsis 2021). 3 tarjetas fueron corregidas en la
verificacion (p.ej. descompresion del neumotorax a tension al 5o EIC linea axilar por
ATLS 10a; qSOFA como alerta y no definicion de sepsis; descartar HDA con endoscopia alta).

Deck: "Cirugia Adulto::Integrador - Clasificaciones"
Fuente: cirugia/build/build_cirugia.py (Capa 1, 40 cloze)
"""
import os
import genanki

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "output")
os.makedirs(OUTPUT_DIR, exist_ok=True)

MODEL_QA_ID = 1607392320          # reusable (ids.json: qa_estandar)
DECK_ID = 1490337261              # nuevo, unico
DECK_NAME = "Cirugia Adulto::Integrador - Clasificaciones"

CSS_BASE = """
.card {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  font-size: 19px; text-align: left; color: #1a1a1a;
  background-color: #fafafa; padding: 20px; line-height: 1.5;
}
#extra { margin-top: 16px; border: none; border-top: 1px solid #d4d4d4; padding-top: 12px; }
.ecoe { color: #b45309; font-style: italic; margin-top: 12px; display: block; }
.disc { color: #6d28d9; display: block; margin-top: 10px; font-weight: 600; }
.redflag { color: #b91c1c; font-weight: 600; display: block; margin-top: 8px; }
.q { font-weight: 600; color: #1d4ed8; }
table { border-collapse: collapse; width: 100%; margin-top: 8px; font-size: 15px; }
th, td { border: 1px solid #cbd5e1; padding: 5px 8px; text-align: left; vertical-align: top; }
th { background: #eef2ff; color: #111; }
td b { color: #b91c1c; }
"""

model_qa = genanki.Model(
    MODEL_QA_ID, "Estudio Medico QA",
    fields=[{"name": "Front"}, {"name": "Back"}],
    templates=[{"name": "QA", "qfmt": '<div class="q">{{Front}}</div>',
                "afmt": '<div class="q">{{Front}}</div><hr id="extra">{{Back}}'}],
    css=CSS_BASE,
)

deck = genanki.Deck(DECK_ID, DECK_NAME)
BASE_TAGS = ["cirugia", "integrador", "ecoe"]

CARDS = CARDS = [
  {
    "front": "Trauma torácico que mata en minutos: cómo se diferencian las 4 entidades de descompensación inmediata",
    "back": "<table><tr><th>Entidad</th><th>Hallazgo discriminador</th><th>Diagnóstico</th><th>Tratamiento</th></tr><tr><td><b>Neumotórax a tensión</b></td><td>Desviación traqueal CONTRAlateral + ingurgitación yugular + hipersonoridad + ausencia de murmullo unilateral</td><td>CLÍNICO (no esperar Rx)</td><td>Descompresión con aguja 5º EIC línea axilar anterior/media (ATLS 10ª; alternativa 2º EIC línea medioclavicular) -&gt; toracostomía</td></tr><tr><td><b>Tamponade cardiaco</b></td><td>Tríada de Beck: hipotensión + ingurgitación yugular + ruidos cardiacos apagados</td><td>FAST subxifoideo</td><td>Pericardiocentesis / cirugía</td></tr><tr><td><b>Hemotórax masivo</b></td><td>Salida inicial por sonda &gt;1500 mL o &gt;200 mL/h por 2-4 h</td><td>Sonda pleural + Rx</td><td>Toracotomía</td></tr><tr><td><b>Tórax inestable (flail chest)</b></td><td>Segmento torácico con movimiento PARADÓJICO; lo que mata es la contusión pulmonar asociada</td><td>Clínico + imagen</td><td>Analgesia + soporte ventilatorio (tratar la contusión)</td></tr></table><span class=\"disc\">Discriminador: yugulares ingurgitadas + hipersonoridad/ausencia de murmullo = neumotórax a tensión; yugulares ingurgitadas + ruidos apagados (tórax silente bilateral) = tamponade; sangre cuantificada por sonda = hemotórax masivo; movimiento paradójico de la pared = flail chest.</span><span class=\"redflag\">El neumotórax a tensión y el tamponade son diagnósticos CLÍNICOS: descomprimir/FAST sin esperar radiografía.</span><span class=\"ecoe\">ECOE: \"Politraumatizado con disnea súbita, hipotensión e ingurgitación yugular; ¿qué hallazgo te orienta y cuál es la conducta inmediata?\"</span>",
    "tags": [
      "agrupador",
      "trauma",
      "torax"
    ]
  },
  {
    "front": "Trauma abdominal y pélvico: qué entidad sospechar y a dónde llevar al paciente según estabilidad",
    "back": "<table><tr><th>Escenario</th><th>Parámetro discriminador</th><th>Entidad / lesión</th><th>Conducta</th></tr><tr><td><b>Penetrante + INESTABLE</b></td><td>Inestabilidad hemodinámica</td><td>Lesión visceral con sangrado</td><td>Laparotomía exploradora (NO TAC)</td></tr><tr><td><b>Penetrante + ESTABLE</b></td><td>Hemodinámicamente estable</td><td>Por caracterizar</td><td>TAC triple contraste</td></tr><tr><td><b>Objeto clavado</b></td><td>Objeto penetrante empalado in situ</td><td>Tapón temporal del vaso/víscera</td><td>NO retirar; se retira solo en quirófano</td></tr><tr><td><b>Cerrado + Kehr</b></td><td>Dolor referido a hombro IZQUIERDO (signo de Kehr)</td><td>Lesión esplénica con hemoperitoneo</td><td>Manejo según estabilidad (FAST/TAC vs quirófano)</td></tr><tr><td><b>Alta energía + dolor pélvico</b></td><td>Inestabilidad + apertura del anillo pélvico</td><td>Fractura pélvica inestable con sangrado retroperitoneal</td><td>Faja pélvica (binder)</td></tr></table><span class=\"disc\">Discriminador clave: la ESTABILIDAD HEMODINÁMICA decide el destino en el penetrante (inestable = quirófano directo; estable = TAC). El signo de Kehr (hombro izquierdo) apunta al bazo; la apertura del anillo pélvico apunta al sangrado retroperitoneal.</span><span class=\"redflag\">NUNCA retirar un objeto empalado fuera de quirófano: actúa como tapón hemostático.</span><span class=\"ecoe\">ECOE: \"Herida por arma blanca en abdomen con PAS 80 y FC 130: ¿pides TAC o laparotomía?\" Respuesta: laparotomía (inestable).</span>",
    "tags": [
      "agrupador",
      "trauma",
      "abdomen",
      "pelvis"
    ]
  },
  {
    "front": "Hemorragia digestiva alta (HDA): cómo se diferencian las causas y su manejo",
    "back": "<table><tr><th>Entidad</th><th>Pista clave</th><th>Sangrado</th><th>Manejo</th></tr><tr><td><b>Úlcera péptica</b></td><td>AINE / H. pylori; más frecuente duodenal</td><td>Hematemesis (sangre fresca o posos de café) + melena</td><td>IBP IV + endoscopia &lt;24h; Forrest clasifica riesgo de resangrado</td></tr><tr><td><b>Várices esofágicas</b></td><td>Estigmas de hepatopatía crónica</td><td>Hematemesis abundante</td><td>Octreótido + ligadura + ATB profiláctico</td></tr></table><span class=\"disc\">Discriminador: estigmas de hepatopatía crónica apuntan a várices; antecedente de AINE/H. pylori apunta a úlcera. La hematemesis abundante en hepatópata = várices.</span><span class=\"ecoe\">ECOE: \"Varón con ascitis y arañas vasculares vomita gran cantidad de sangre roja\" -> várices: octreótido + ligadura + profilaxis ATB.\"</span>",
    "tags": [
      "agrupador",
      "hemorragia",
      "hda"
    ]
  },
  {
    "front": "Sangrado masivo intraabdominal con inestabilidad: ectópico roto vs AAA roto",
    "back": "<table><tr><th>Entidad</th><th>Perfil</th><th>Clínica clave</th><th>Conducta si inestable</th></tr><tr><td><b>Embarazo ectópico roto</b></td><td>Mujer fértil + amenorrea</td><td>Dolor abdominal bajo súbito + inestabilidad + líquido libre en FAST</td><td>Quirófano (estable + masa anexial sin líquido libre = no roto -> metotrexato posible)</td></tr><tr><td><b>AAA roto</b></td><td>Varón &gt;60a fumador</td><td>Tríada: dolor abdominal/lumbar súbito + masa pulsátil + hipotensión</td><td>Quirófano sin TAC (mortalidad &gt;80%)</td></tr></table><span class=\"disc\">Discriminador: edad/sexo y antecedente. Mujer fértil con amenorrea -> ectópico; varón mayor fumador con masa pulsátil -> AAA.</span><span class=\"redflag\">Si inestable: NO se pierde tiempo en TAC, va directo a quirófano.</span><span class=\"ecoe\">ECOE: \"Varón 70a fumador, dolor lumbar súbito, masa abdominal pulsátil e hipotensión\" -> AAA roto a quirófano.\"</span>",
    "tags": [
      "agrupador",
      "hemorragia",
      "abdomen_agudo"
    ]
  },
  {
    "front": "Hemorragia digestiva baja (HDB) en el anciano: divertículo vs angiodisplasia",
    "back": "<table><tr><th>Entidad</th><th>Frecuencia</th><th>Pista</th><th>Sangrado</th></tr><tr><td><b>Diverticulosis</b></td><td>1a causa de HDB</td><td>&gt;60 años con diverticulosis conocida</td><td>Hematoquezia (indolora, autolimitada)</td></tr><tr><td><b>Angiodisplasia colónica</b></td><td>2a causa</td><td>Lesiones vasculares colónicas</td><td>Hematoquezia recurrente</td></tr></table><span class=\"disc\">Discriminador: ambas dan hematoquezia en el anciano; ante hematoquezia abundante siempre descartar una HDA brusca (10-15% se presentan así) con endoscopia alta (EGD), NO con lavado por SNG (baja sensibilidad: aspirado claro no excluye sangrado postpilórico). Un cociente BUN/creatinina &gt;30 apoya origen alto.</span><span class=\"ecoe\">ECOE: \"Paciente 72a con diverticulosis y sangre roja rectal abundante\" -&gt; sospecha HDB por divertículo; estabilizar y descartar HDA con endoscopia alta antes de etiquetar como HDB.</span>",
    "tags": [
      "agrupador",
      "hemorragia",
      "hdb"
    ]
  },
  {
    "front": "Choque hipovolémico (ATLS) y reanimación: cómo se clasifica y cuál es la meta",
    "back": "<table><tr><th>Parámetro</th><th>Clase III</th><th>Clase IV</th></tr><tr><td><b>Pérdida</b></td><td>30-40% (1500-2000 mL)</td><td>&gt;40%</td></tr><tr><td><b>FC</b></td><td>&gt;120</td><td>Muy elevada</td></tr><tr><td><b>PA</b></td><td>Disminuida</td><td>Hipotensión severa</td></tr><tr><td><b>Estado mental / diuresis</b></td><td>Confuso</td><td>Letargia, anuria</td></tr><tr><td><b>Manejo</b></td><td>Cristaloides + hemoderivados</td><td>Hemoderivados (transfusión masiva)</td></tr></table><span class=\"disc\">Discriminador clase III vs IV: la pérdida del 40% es el corte; clase IV añade anuria y letargia. La confusión aparece desde clase III.</span><span class=\"redflag\">Reanimación hipotensiva permisiva en hemorragia traumática: meta PAS 80-90 mmHg (o pulso radial palpable) hasta control quirúrgico. Excepción TCE: PAS &gt;=110. Hemoderivados 1:1:1.</span><span class=\"ecoe\">ECOE: \"Politraumatizado FC 130, confuso, PA baja\" -> choque clase III, cristaloides + hemoderivados con meta de PAS permisiva 80-90.\"</span>",
    "tags": [
      "agrupador",
      "hemorragia",
      "choque"
    ]
  },
  {
    "front": "Abdomen agudo del cuadrante superior derecho / vía biliar: cómo se diferencian (cólico, colecistitis, colangitis)",
    "back": "<table><tr><th>Entidad</th><th>Fiebre/leucocitosis</th><th>Hallazgo clave</th><th>Conducta</th></tr><tr><td><b>Cólico biliar</b></td><td>NO (afebril, sin leucocitosis)</td><td>Dolor HCD postprandial graso &lt;6 h, autolimitado</td><td>Manejo del dolor; colecistectomía programada</td></tr><tr><td><b>Colecistitis aguda</b></td><td>SÍ</td><td>Murphy positivo + dolor HCD persistente</td><td>Colecistectomía laparoscópica &lt;72 h + ATB</td></tr><tr><td><b>Colangitis aguda</b></td><td>SÍ (con escalofríos)</td><td>Tríada de Charcot: fiebre + ictericia + dolor HCD</td><td>ATB + CPRE</td></tr><tr><td><b>Colangitis grave (Tokyo III)</b></td><td>SÍ</td><td>Péntada de Reynolds: Charcot + hipotensión + alteración mental</td><td>UCI + CPRE &lt;24 h</td></tr></table><span class=\"disc\">Discriminador: la FIEBRE/leucocitosis separa cólico (ausente) de colecistitis; la ICTERICIA + Charcot añade afectación de la vía biliar (colangitis); la HIPOTENSIÓN + confusión (Reynolds) marca el grado más grave.</span><span class=\"redflag\">Red flag: hipotensión + alteración mental en un paciente con Charcot = sepsis biliar (Tokyo III), CPRE urgente.</span><span class=\"ecoe\">ECOE: \"Mujer con dolor en HCD tras comida grasa, fiebre 38.5 y Murphy positivo\" -> colecistitis aguda; si además ictericia y escalofríos -> colangitis.</span>",
    "tags": [
      "agrupador",
      "abdomen_agudo",
      "via_biliar"
    ]
  },
  {
    "front": "Abdomen agudo con peritonitis o irritación peritoneal: cómo se diferencian (apendicitis, perforación péptica, diverticulitis, pancreatitis)",
    "back": "<table><tr><th>Entidad</th><th>Localización dolor</th><th>Dato discriminador</th><th>Score/manejo</th></tr><tr><td><b>Apendicitis aguda</b></td><td>Periumbilical que migra a FID en 12-24 h</td><td>Anorexia + febrícula</td><td>Alvarado; apendicectomía</td></tr><tr><td><b>Apendicitis perforada</b></td><td>FID -&gt; defensa generalizada</td><td>&gt;48-72 h + fiebre alta + leucocitosis + taquicardia</td><td>Quirófano + ATB</td></tr><tr><td><b>Perforación de úlcera péptica</b></td><td>Súbito en puñalada, epigastrio</td><td>Abdomen en tabla + aire libre subdiafragmático en Rx</td><td>Parche de Graham</td></tr><tr><td><b>Diverticulitis aguda</b></td><td>Fosa ilíaca izquierda, &gt;50 a</td><td>Fiebre + cambio del hábito intestinal</td><td>Hinchey I-IV guía manejo</td></tr><tr><td><b>Pancreatitis aguda</b></td><td>Epigástrico en cinturón irradiado a espalda</td><td>Vómito + lipasa &gt;3x normal</td><td>Atlanta revisada (litiasis/alcohol)</td></tr></table><span class=\"disc\">Discriminador: la MIGRACIÓN periumbilical-&gt;FID = apendicitis; aire libre + abdomen en tabla = perforación péptica; FIL en mayor de 50 a = diverticulitis; LIPASA &gt;3x + dolor en cinturón = pancreatitis.</span><span class=\"redflag\">Red flag: defensa generalizada / abdomen en tabla = peritonitis difusa -> quirófano.</span><span class=\"ecoe\">ECOE: \"Dolor que empezó en el ombligo y ahora se localiza en fosa ilíaca derecha, no quiere comer\" -> apendicitis aguda.</span>",
    "tags": [
      "agrupador",
      "abdomen_agudo",
      "peritonitis"
    ]
  },
  {
    "front": "Abdomen agudo isquémico u obstructivo grave: cómo se diferencian (isquemia mesentérica vs vólvulo de sigmoides)",
    "back": "<table><tr><th>Entidad</th><th>Paciente típico</th><th>Dato discriminador</th><th>Rx / manejo</th></tr><tr><td><b>Isquemia mesentérica aguda</b></td><td>FA / cardiopatía embólica</td><td>Dolor DESPROPORCIONADO a hallazgos + acidosis metabólica + lactato elevado</td><td>TAC angiográfico + laparotomía</td></tr><tr><td><b>Vólvulo de sigmoides</b></td><td>Adulto mayor (cecal en joven)</td><td>Distensión asimétrica masiva + dolor cólico</td><td>Rx asa en grano de café / U invertida</td></tr></table><span class=\"disc\">Discriminador: el DOLOR DESPROPORCIONADO a la exploración + lactato/acidosis + fuente embólica (FA) apunta a isquemia mesentérica; la DISTENSIÓN asimétrica masiva con imagen en grano de café señala vólvulo de sigmoides.</span><span class=\"redflag\">Red flag: lactato elevado + dolor que no concuerda con un abdomen casi normal a la palpación = isquemia mesentérica, no demorar el TAC angiográfico.</span><span class=\"ecoe\">ECOE: \"Paciente con fibrilación auricular y dolor abdominal intenso pero abdomen blando a la palpación\" -> isquemia mesentérica aguda.</span>",
    "tags": [
      "agrupador",
      "abdomen_agudo",
      "isquemia_obstruccion"
    ]
  },
  {
    "front": "Obstrucción intestinal: cómo se diferencian los grandes tipos (alta vs baja, mecánica vs paralítica)",
    "back": "<table><tr><th>Tipo</th><th>Vómito</th><th>Distensión</th><th>RHA</th><th>Rx</th><th>Causa típica</th></tr><tr><td><b>SOI alta (adherencias)</b></td><td>Bilioso, precoz</td><td>Leve</td><td>Metálicos/aumentados</td><td>Niveles altos, gas distal escaso</td><td>Adherencias (causa #1), cirugía previa</td></tr><tr><td><b>SOI baja completa</b></td><td>Tardío, fecaloide</td><td>Marcada</td><td>Metálicos/aumentados</td><td>Niveles hidroaéreos SIN gas distal</td><td>Mecánica distal (mayor riesgo estrangulación)</td></tr><tr><td><b>Íleo paralítico</b></td><td>Variable</td><td>Difusa</td><td>AUSENTES</td><td>Gas difuso intestino/colon, sin transición</td><td>Postop, sepsis, electrolitos, opioides</td></tr></table><span class=\"disc\">Discriminador: RHA metálicos/aumentados = mecánica; RHA AUSENTES = íleo paralítico. Dentro de la mecánica, vómito bilioso precoz + distensión leve = alta; vómito fecaloide tardío + distensión marcada = baja.</span><span class=\"redflag\">SOI baja completa = mayor riesgo de estrangulación.</span><span class=\"ecoe\">ECOE: \"Vómito bilioso, dolor cólico, distensión leve y cirugía abdominal previa\" -> SOI alta por adherencias (SNG, hidratación, Gastrografin).</span>",
    "tags": [
      "agrupador",
      "obstruccion",
      "cirugia"
    ]
  },
  {
    "front": "Hernia con dolor: cómo distinguir reductible vs incarcerada vs estrangulada",
    "back": "<table><tr><th>Estado</th><th>Reductibilidad</th><th>Dolor</th><th>Obstrucción</th><th>Signos de isquemia/sepsis</th><th>Conducta</th></tr><tr><td><b>Hernia reductible</b></td><td>Reduce</td><td>Leve/ausente</td><td>No</td><td>No</td><td>Programable</td></tr><tr><td><b>Hernia incarcerada</b></td><td>Irreductible</td><td>Sí</td><td>Sí</td><td>No</td><td>Reducción/cirugía</td></tr><tr><td><b>Hernia estrangulada</b></td><td>Irreductible</td><td>Intenso</td><td>Sí</td><td>SÍ: cambio de coloración, fiebre, sepsis</td><td>Quirófano urgente</td></tr></table><span class=\"disc\">Discriminador: masa irreductible + dolor + obstrucción SIN datos de isquemia = incarcerada; si se añade cambio de coloración / fiebre / sepsis = estrangulada (isquemia).</span><span class=\"redflag\">Estrangulada = isquemia -> quirófano sin demora.</span><span class=\"ecoe\">ECOE: \"Hernia con masa irreductible, dolorosa, que cambia de color y con fiebre\" -> hernia estrangulada.</span>",
    "tags": [
      "agrupador",
      "obstruccion",
      "hernia"
    ]
  },
  {
    "front": "Vólvulo y obstrucción en asa cerrada: cómo se reconocen y por qué urgen",
    "back": "<table><tr><th>Entidad</th><th>Paciente/contexto</th><th>Rx característica</th><th>Riesgo</th><th>Manejo inicial</th></tr><tr><td><b>Vólvulo de sigmoides</b></td><td>Adulto mayor encamado, estreñimiento crónico, distensión súbita</td><td>Asa dilatada en grano de café</td><td>Asa cerrada -> isquemia/perforación</td><td>Descompresión endoscópica</td></tr><tr><td><b>Obstrucción en asa cerrada</b> (vólvulo, hernia estrangulada, banda)</td><td>Punto fijo proximal y distal ocluido</td><td>Asa dilatada aislada</td><td>Mayor riesgo de isquemia y perforación; cirugía más urgente</td><td>Cirugía urgente</td></tr></table><span class=\"disc\">Discriminador clave: el asa cerrada (vólvulo, hernia estrangulada, banda) tiene MAYOR riesgo de isquemia/perforación que la obstrucción simple -> cirugía más urgente.</span><span class=\"redflag\">Datos de isquemia: lactato elevado, taquicardia, dolor desproporcionado, defensa.</span><span class=\"ecoe\">ECOE: \"Anciano encamado, estreñido, con distensión súbita y asa en grano de café en la Rx\" -> vólvulo de sigmoides (descompresión endoscópica).</span>",
    "tags": [
      "agrupador",
      "obstruccion",
      "volvulo"
    ]
  },
  {
    "front": "Infección quirúrgica de partes blandas/intraabdominal: ¿cómo se diferencian las entidades por presentación y manejo?",
    "back": "<table><tr><th>Entidad</th><th>Clave diagnóstica / temporalidad</th><th>Manejo</th></tr><tr><td><b>Peritonitis secundaria</b></td><td>Abdomen en tabla + dolor a cualquier movimiento + sepsis (perforación de víscera hueca)</td><td>Control quirúrgico del foco</td></tr><tr><td><b>Absceso intraabdominal</b></td><td>Fiebre persistente + leucocitosis + dolor focal en postoperatorio 5-10 días</td><td>TAC con contraste; drenaje percutáneo</td></tr><tr><td><b>Fascitis necrotizante</b></td><td>Dolor DESPROPORCIONADO a hallazgos cutáneos + edema + crepitación + bullas/equimosis + toxicidad</td><td>Emergencia quirúrgica: desbridamiento + ATB amplio</td></tr><tr><td><b>Gangrena gaseosa / polimicrobiana</b></td><td>Diabético + lesión en pie + olor fétido + crepitación + Rx aire en subcutáneo</td><td>Desbridamiento; valorar amputación</td></tr></table><span class=\"disc\">Discriminador: el dolor desproporcionado a la lesión cutánea visible + crepitación apunta a infección necrotizante de partes blandas (quirófano YA), mientras que fiebre + dolor focal a los 5-10 días postop apunta a absceso (drenaje).</span><span class=\"redflag\">Crepitación, bullas, equimosis o aire en tejidos = necrosis tisular: NO retrasar el desbridamiento por imagen.</span><span class=\"ecoe\">ECOE: \"Paciente postoperado de hace 7 días con fiebre persistente, leucocitosis y dolor focal: ¿siguiente paso?\" -> TAC con contraste y drenaje percutáneo del absceso.</span>",
    "tags": [
      "agrupador",
      "infeccion_quirurgica",
      "partes_blandas"
    ]
  },
  {
    "front": "Definiciones de sepsis quirúrgica: ¿qué parámetro separa infección, sepsis y shock séptico?",
    "back": "<table><tr><th>Entidad</th><th>Criterio discriminador</th><th>Acción</th></tr><tr><td><b>Infección</b></td><td>Foco infeccioso SIN disfunción orgánica (SOFA sin aumento &gt;=2)</td><td>Antibiótico dirigido + control del foco; vigilar deterioro</td></tr><tr><td><b>Sepsis quirúrgica</b></td><td>Infección + disfunción orgánica = aumento agudo de SOFA &gt;=2 (qSOFA &gt;=2 -FR &gt;=22, PAS &lt;=100, alteración mental- es solo alerta a pie de cama, NO define sepsis)</td><td>Bundle hora-1 Surviving Sepsis 2021</td></tr><tr><td><b>Shock séptico</b></td><td>Sepsis + necesidad de vasopresor para PAM &gt;=65 + lactato &gt;2 PESE a resucitación</td><td>Vasopresores + control del foco</td></tr></table><span class=\"disc\">Discriminador: lo que separa infección de sepsis es la disfunción orgánica (SOFA &gt;=2), no el qSOFA; qSOFA &gt;=2 es solo una señal de alerta que obliga a evaluar SOFA y lactato. Lo que distingue el shock séptico es la dependencia de vasopresores (PAM &gt;=65) MÁS lactato &gt;2 a pesar de reanimación con líquidos adecuada.</span><span class=\"redflag\">qSOFA &gt;=2 al pie de cama (taquipnea + hipotensión + confusión) = alta sospecha de sepsis: buscar foco, medir lactato y activar bundle hora-1 sin demora. OJO: la SSC 2021 recomienda en contra de usar qSOFA como ÚNICA herramienta de cribado (baja sensibilidad).</span><span class=\"ecoe\">ECOE: \"Postoperado con foco infeccioso, FR 24, PAS 95 y desorientado; ¿clasificación y conducta?\" -&gt; qSOFA 3 -&gt; sospecha de sepsis; confirmar disfunción orgánica (SOFA, lactato) y activar bundle hora-1 Surviving Sepsis.</span>",
    "tags": [
      "agrupador",
      "infeccion_quirurgica",
      "sepsis"
    ]
  },
  {
    "front": "Dolor catastrófico súbito en el adulto (cabeza, tórax, testículo): cómo se diferencian las 3 urgencias 'especiales'",
    "back": "<table><tr><th>Entidad</th><th>Dolor / inicio</th><th>Signo discriminador clave</th><th>Dx / Conducta</th></tr><tr><td><b>Hemorragia subaracnoidea (HSA)</b></td><td>Cefalea en trueno, \"la peor de la vida\", instantánea</td><td>Meningismo + fotofobia</td><td>TAC simple urgente; si negativa y alta sospecha &rarr; PL con xantocromía</td></tr><tr><td><b>Disección aórtica</b></td><td>Torácico desgarrante irradiado a la espalda</td><td>Diferencia de pulsos/PA entre ambos brazos + mediastino ensanchado</td><td>Tipo A (ascendente) &rarr; quirófano; Tipo B &rarr; médico con esmolol</td></tr><tr><td><b>Torsión testicular</b></td><td>Testicular súbito intenso + náusea (adolescente/joven)</td><td>Ausencia de reflejo cremastérico + Prehn negativo</td><td>Ventana &lt;6 h &rarr; cirugía urgente + orquidopexia bilateral</td></tr></table><span class=\"disc\">Discriminador: el LOCALIZADOR anatómico del dolor + su signo acompañante (meningismo vs asimetría de pulsos vs cremastérico abolido) define la entidad.</span><span class=\"redflag\">Las 3 son tiempo-dependientes: HSA puede resangrar, disección A se rompe al pericardio, la torsión pierde el teste a las 6 h.</span><span class=\"ecoe\">ECOE: \"Varón joven con dolor escrotal súbito y náusea; el teste asciende y no hay reflejo cremastérico\" &rarr; torsión testicular, NO esperes ecografía si la clínica es clara.</span>",
    "tags": [
      "agrupador",
      "especiales",
      "urgencias"
    ]
  },
  {
    "front": "Torsión testicular vs epididimitis: parámetros que las separan",
    "back": "<table><tr><th>Parámetro</th><th><b>Torsión testicular</b></th><th><b>Epididimitis</b></th></tr><tr><td>Inicio del dolor</td><td>Súbito, intenso</td><td>Gradual</td></tr><tr><td>Signo de Prehn (elevar teste)</td><td>Negativo (no alivia)</td><td>Positivo (alivia)</td></tr><tr><td>Reflejo cremastérico</td><td>Ausente</td><td>Presente</td></tr><tr><td>Fiebre</td><td>Ausente (náusea sí)</td><td>Presente (febril)</td></tr><tr><td>Conducta</td><td>Cirugía urgente &lt;6 h + orquidopexia bilateral</td><td>Manejo médico (antibiótico)</td></tr></table><span class=\"disc\">Discriminador: Prehn NEGATIVO + cremastérico AUSENTE + inicio súbito = torsión. La epididimitis es gradual, febril, Prehn positivo.</span><span class=\"ecoe\">ECOE: \"Adolescente con dolor escrotal brusco; elevar el teste no alivia\" &rarr; torsión; \"varón adulto con dolor gradual y fiebre que alivia al elevar el teste\" &rarr; epididimitis.</span>",
    "tags": [
      "discriminador_rapido",
      "especiales",
      "urologia"
    ]
  },
  {
    "front": "Disección aórtica: cómo el tipo de Stanford cambia el destino del paciente",
    "back": "<table><tr><th>Tipo Stanford</th><th>Segmento afectado</th><th>Tratamiento</th></tr><tr><td><b>Tipo A</b></td><td>Aorta ascendente</td><td>Quirófano (urgente)</td></tr><tr><td><b>Tipo B</b></td><td>Aorta descendente (no ascendente)</td><td>Manejo médico con esmolol (control de FC/PA)</td></tr></table><span class=\"disc\">Discriminador: si afecta la aorta ASCENDENTE (tipo A) &rarr; cirugía; si NO la afecta (tipo B) &rarr; médico.</span><span class=\"redflag\">Cuadro clínico: dolor torácico DESGARRANTE irradiado a la espalda + diferencia de pulsos/PA entre brazos + mediastino ensanchado en Rx.</span><span class=\"ecoe\">ECOE: \"Dolor torácico que se irradia a la espalda con PA distinta en cada brazo y mediastino ancho\" &rarr; disección aórtica; clasifica Stanford para decidir quirófano (A) vs esmolol (B).</span>",
    "tags": [
      "agrupador",
      "especiales",
      "vascular"
    ]
  }
]

for c in CARDS:
    deck.add_note(genanki.Note(model=model_qa, fields=[c["front"], c["back"]],
                               tags=BASE_TAGS + c["tags"]))

out = os.path.join(OUTPUT_DIR, "Cirugia_Adulto_Integrador.apkg")
genanki.Package([deck]).write_to_file(out)
print(f"OK -> {out}")
print(f"TOTAL notas: {len(deck.notes)}")
