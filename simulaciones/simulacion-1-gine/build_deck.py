#!/usr/bin/env python3
"""
Simulación 1 — Ginecología (ITS / EIP)
Genera el deck de Anki "Simulaciones::Gine - Repaso 1" (.apkg) y un TSV de respaldo.

Uso:
    pip install genanki
    python build_deck.py
Produce:
    simulacion-1-gine.apkg   -> importar con doble clic en Anki
    simulacion-1-gine.tsv    -> importar manual (Archivo > Importar), separador TAB

Estructura por entidad (6): 3 tarjetas de núcleo (interrogatorio / exploración /
manejo) + 3 casos de la MISMA enfermedad escalando (leve, moderado, difícil) = 36.
La exploración describe cómo se hace y qué verbalizar en la ECOE.
"""

import genanki

# Reusa el note type Q&A estándar del repo (ver ids.json -> models.qa_estandar)
# para que las tarjetas compartan tipo de nota en Anki con las demás capas Q&A.
MODEL_QA_ID = 1607392320
DECK_ID = 2059400110  # registrado en ids.json
DECK_NAME = "Simulaciones::Gine - Repaso 1"

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
li { margin: 5px 0; }
#extra { margin-top: 16px; border: none; border-top: 1px solid #d4d4d4; padding-top: 12px; }
""",
)

DECK = genanki.Deck(DECK_ID, DECK_NAME)

# (Front, Back, [tags])
CARDS = [
    # ===================== 1. HERPES GENITAL =====================
    ("<b>Herpes genital — Interrogatorio dirigido.</b> ¿Qué pregunto y qué orienta cada cosa?",
     "<ul>"
     "<li><b>Pareja nueva/múltiple, uso de condón</b> → riesgo de ITS.</li>"
     "<li><b>¿Duele? ¿ardor/ampollas?</b> → herpes duele (vs úlcera indolora = sífilis).</li>"
     "<li><b>Disuria</b> → afección uretral/vulvar.</li>"
     "<li><b>Fiebre, malestar, mialgias</b> → primer episodio (más sistémico).</li>"
     "<li><b>Episodios previos / pródromo (hormigueo)</b> → recurrencia por latencia ganglionar.</li>"
     "<li><b>Embarazo</b> → riesgo de herpes neonatal.</li></ul>",
     ["Simulacion1::Gine::Herpes", "Interrogatorio"]),

    ("<b>Herpes — Exploración dirigida.</b> ¿Cómo la hago y qué verbalizo?",
     "<i>Verbalizo:</i> «Con su consentimiento y guantes, inspecciono vulva, periné y región perianal con buena luz.»"
     "<ul>"
     "<li>Busco <b>vesículas agrupadas sobre base eritematosa</b> y/o <b>úlceras pequeñas múltiples, dolorosas</b>.</li>"
     "<li>Palpo regiones inguinales: <b>adenopatías dolorosas</b>.</li>"
     "<li>Especuloscopía si sospecho lesión vaginal/cervical.</li>"
     "<li><b>Toma:</b> hisopo de la base de una vesícula destechada para <b>PCR</b> (prueba de elección).</li></ul>"
     "<i>Verbalizo hallazgo:</i> «Vesículas agrupadas dolorosas + adenopatía → herpes genital.»",
     ["Simulacion1::Gine::Herpes", "Exploracion"]),

    ("<b>Herpes — Manejo:</b> Dx + tratamiento + consejería.",
     "<b>Dx:</b> herpes genital (VHS). <b>Dif:</b> sífilis (úlcera indolora), chancroide (úlcera sucia dolorosa), candidiasis irritativa."
     "<ul>"
     "<li><b>Primer episodio:</b> aciclovir 400 mg VO c/8 h 7–10 días (alt. valaciclovir).</li>"
     "<li><b>Recurrente:</b> aciclovir 800 mg VO c/12 h 5 días.</li>"
     "<li>Supresión diaria si recurrencias frecuentes.</li></ul>"
     "<b>Consejería:</b> queda latente en ganglios → recurre; evitar sexo en brotes; condón (reduce, no elimina); avisar parejas.",
     ["Simulacion1::Gine::Herpes", "Manejo"]),

    ("<b>HERPES — Caso LEVE.</b> Mujer 22 a, primera relación con pareja nueva hace 6 días; «ampollitas que arden» en vulva, sin fiebre. EF: 3 vesículas agrupadas en labio menor, sin adenopatías. ¿Dx y conducta?",
     "<b>Primer episodio leve de herpes genital.</b> PCR de vesícula. Aciclovir 400 mg c/8 h 7–10 d. Consejería + condón + avisar pareja.",
     ["Simulacion1::Gine::Herpes", "Caso", "Leve"]),

    ("<b>HERPES — Caso MODERADO.</b> Mujer 25 a, fiebre 38.5°, malestar, disuria intensa con retención parcial; múltiples úlceras dolorosas en vulva y adenopatías inguinales dolorosas. ¿Dx y conducta?",
     "<b>Primer episodio florido (sistémico).</b> PCR. Aciclovir 400 mg c/8 h 7–10 d (valorar IV si no tolera). Analgesia, hidratación, cuidado local; <b>sondaje si retención urinaria</b>. Consejería.",
     ["Simulacion1::Gine::Herpes", "Caso", "Moderado"]),

    ("<b>HERPES — Caso DIFÍCIL.</b> Embarazada de 38 SDG con primer brote de vesículas dolorosas en vulva. ¿Riesgo y conducta?",
     "<b>Herpes primario cerca del término = alto riesgo de herpes neonatal.</b> Aciclovir + <b>cesárea si hay lesiones activas o pródromo al inicio del trabajo de parto</b>. Profilaxis con aciclovir desde la semana 36 en pacientes con antecedente.",
     ["Simulacion1::Gine::Herpes", "Caso", "Dificil"]),

    # ===================== 2. SÍFILIS PRIMARIA =====================
    ("<b>Sífilis primaria — Interrogatorio dirigido.</b> ¿Qué pregunto y qué orienta?",
     "<ul>"
     "<li><b>¿La úlcera duele?</b> → <b>indolora</b> orienta a sífilis.</li>"
     "<li>Pareja nueva, condón, ITS previas.</li>"
     "<li><b>Embarazo</b> → riesgo de sífilis congénita.</li>"
     "<li>Síntomas sistémicos / <b>rash palmoplantar</b> → ¿ya secundaria?</li>"
     "<li>Tiempo desde el contacto sexual.</li></ul>",
     ["Simulacion1::Gine::Sifilis", "Interrogatorio"]),

    ("<b>Sífilis — Exploración dirigida.</b> ¿Cómo y qué verbalizo?",
     "<i>Verbalizo:</i> «Inspecciono genitales externos; reviso también boca/ano según la práctica sexual.»"
     "<ul>"
     "<li>Busco el <b>chancro: úlcera única, indolora, bordes indurados, base limpia no purulenta</b>.</li>"
     "<li>Compruebo con presión suave que <b>NO duele</b> (dato clave).</li>"
     "<li>Palpo inguinal: <b>adenopatías firmes, móviles, no dolorosas</b>.</li>"
     "<li><b>Estudios:</b> VDRL/RPR (tamizaje no treponémico) + confirmar con prueba treponémica (FTA-ABS/TPHA).</li></ul>",
     ["Simulacion1::Gine::Sifilis", "Exploracion"]),

    ("<b>Sífilis — Manejo:</b> Dx + tratamiento + consejería.",
     "<b>Dx:</b> sífilis primaria. <b>Dif:</b> chancroide (dolorosa, sucia), herpes (vesículas)."
     "<ul>"
     "<li><b>Penicilina G benzatínica 2.4 millones UI IM dosis única.</b></li>"
     "<li>Alergia: doxiciclina 100 mg c/12 h 14 d. <b>En embarazo: desensibilizar y dar penicilina</b> (obligatoria).</li></ul>"
     "<b>Consejería:</b> curable; avisar/tratar parejas; no sexo hasta completar y reevaluar; seguimiento por títulos serológicos.",
     ["Simulacion1::Gine::Sifilis", "Manejo"]),

    ("<b>SÍFILIS — Caso LEVE.</b> Mujer 28 a, «llaga» en vulva que NO duele, notada hace 1 semana; pareja nueva. EF: úlcera única indurada, base limpia; ganglio inguinal firme no doloroso. ¿Dx y conducta?",
     "<b>Sífilis primaria.</b> RPR + prueba treponémica. <b>Penicilina benzatínica 2.4M UI IM dosis única.</b> Avisar y tratar pareja; no sexo hasta reevaluar.",
     ["Simulacion1::Gine::Sifilis", "Caso", "Leve"]),

    ("<b>SÍFILIS — Caso MODERADO.</b> Embarazada de 16 SDG con chancro vulvar indoloro; RPR positivo. ¿Dx y conducta?",
     "<b>Sífilis primaria en embarazo</b> (riesgo de sífilis congénita). <b>Penicilina benzatínica IM</b>; en embarazo es la única opción válida (desensibilizar si es alérgica). Seguimiento de títulos; tratar pareja.",
     ["Simulacion1::Gine::Sifilis", "Caso", "Moderado"]),

    ("<b>SÍFILIS — Caso DIFÍCIL.</b> Mujer con antecedente de úlcera genital indolora hace 6 semanas (ya resuelta) que ahora consulta por rash en palmas y plantas + malestar. ¿Dx y conducta?",
     "<b>Sífilis secundaria</b> (la primaria pasó desapercibida). RPR + treponémica. <b>Penicilina benzatínica 2.4M UI IM</b> (si duración &gt;1 año o indeterminada → 3 dosis semanales). Consejería + parejas.",
     ["Simulacion1::Gine::Sifilis", "Caso", "Dificil"]),

    # ===================== 3. CHANCROIDE =====================
    ("<b>Chancroide — Interrogatorio dirigido.</b> ¿Qué pregunto y qué orienta?",
     "<ul>"
     "<li><b>¿Úlcera dolorosa?</b> → chancroide (dolor a diferencia de sífilis).</li>"
     "<li>Pareja reciente, condón.</li>"
     "<li>Secreción de la úlcera.</li>"
     "<li><b>Ganglio inguinal doloroso que crece/supura</b> (bubón).</li>"
     "<li>Viaje o zona endémica.</li></ul>",
     ["Simulacion1::Gine::Chancroide", "Interrogatorio"]),

    ("<b>Chancroide — Exploración dirigida.</b> ¿Cómo y qué verbalizo?",
     "<i>Verbalizo:</i> «Con guantes y buena luz inspecciono la lesión genital.»"
     "<ul>"
     "<li>Busco <b>úlcera dolorosa, bordes irregulares/socavados, base sucia purulenta, blanda</b>; puede ser múltiple.</li>"
     "<li>Palpo inguinal: <b>bubón doloroso unilateral</b>, que puede fluctuar/fistulizar.</li>"
     "<li>Tomo muestras para <b>excluir sífilis y herpes</b> (RPR, PCR VHS): el dx es clínico de exclusión.</li></ul>",
     ["Simulacion1::Gine::Chancroide", "Exploracion"]),

    ("<b>Chancroide — Manejo:</b> Dx + tratamiento + consejería.",
     "<b>Dx:</b> chancroide (<i>Haemophilus ducreyi</i>). <b>Dif:</b> sífilis (indolora), herpes (vesículas)."
     "<ul>"
     "<li><b>Azitromicina 1 g VO dosis única</b> O <b>ceftriaxona 250 mg IM dosis única</b> (alt. ciprofloxacino/eritromicina).</li>"
     "<li><b>Bubón fluctuante: aspiración con aguja</b> (NO incisión y drenaje → fistuliza).</li></ul>"
     "<b>Consejería:</b> se cura; no sexo hasta sanar; evaluar/tratar parejas.",
     ["Simulacion1::Gine::Chancroide", "Manejo"]),

    ("<b>CHANCROIDE — Caso LEVE.</b> Mujer 24 a, úlcera genital DOLOROSA única hace 5 días, base con pus, pareja reciente. ¿Dx y conducta?",
     "<b>Chancroide.</b> Azitromicina 1 g VO única (o ceftriaxona 250 mg IM). Tratar pareja, condón, no sexo hasta sanar.",
     ["Simulacion1::Gine::Chancroide", "Caso", "Leve"]),

    ("<b>CHANCROIDE — Caso MODERADO.</b> Lo mismo + ganglio inguinal doloroso y aumentado de tamaño (bubón), aún no fluctuante. ¿Dx y conducta?",
     "<b>Chancroide con linfadenopatía/bubón.</b> Mismo antibiótico (azitromicina 1 g o ceftriaxona 250 IM) + vigilar el bubón.",
     ["Simulacion1::Gine::Chancroide", "Caso", "Moderado"]),

    ("<b>CHANCROIDE — Caso DIFÍCIL.</b> Úlcera dolorosa + <b>bubón inguinal fluctuante</b> a punto de fistulizar; además la úlcera confunde con herpes. ¿Dx y conducta?",
     "<b>Chancroide con bubón fluctuante.</b> Antibiótico + <b>ASPIRACIÓN con aguja</b> (no incisión, fistuliza). Tomar RPR y PCR VHS para descartar coinfección/úlcera mixta.",
     ["Simulacion1::Gine::Chancroide", "Caso", "Dificil"]),

    # ===================== 4. VPH / CONDILOMA =====================
    ("<b>VPH / condiloma — Interrogatorio dirigido.</b> ¿Qué pregunto y qué orienta?",
     "<ul>"
     "<li>Verrugas: tiempo de evolución y crecimiento.</li>"
     "<li>¿Dolor/secreción/sangrado? (suelen <b>no</b> doler).</li>"
     "<li>Parejas, condón.</li>"
     "<li><b>Vacuna VPH</b> y último <b>Papanicolaou</b>.</li>"
     "<li>Inmunosupresión → crecen más.</li></ul>",
     ["Simulacion1::Gine::VPH", "Interrogatorio"]),

    ("<b>VPH / condiloma — Exploración dirigida.</b> ¿Cómo y qué verbalizo?",
     "<i>Verbalizo:</i> «Inspecciono vulva, periné y región perianal; hago especuloscopía para vagina y cérvix.»"
     "<ul>"
     "<li>Busco <b>verrugas exofíticas, blandas, aspecto en coliflor, no dolorosas</b>.</li>"
     "<li>El ácido acético puede blanquear lesiones (acetoblanqueo), opcional.</li>"
     "<li><i>Verbalizo:</i> dx <b>clínico</b>; el test de VPH cervical mide riesgo oncogénico, <b>no se toma de la verruga</b>.</li></ul>",
     ["Simulacion1::Gine::VPH", "Exploracion"]),

    ("<b>VPH / condiloma — Manejo:</b> Dx + tratamiento + consejería.",
     "<b>Dx:</b> condiloma acuminado (VPH 6/11). <b>Dif:</b> molusco (umbilicadas), condiloma lata de sífilis 2ª (planos húmedos), herpes."
     "<ul>"
     "<li><b>Aplica la paciente:</b> podofilotoxina, imiquimod.</li>"
     "<li><b>Aplica el médico:</b> crioterapia, ácido tricloroacético, podofilina; resección si son grandes.</li></ul>"
     "<b>Consejería:</b> puede recurrir; condón reduce no elimina; vacuna previene otros tipos; mantener Papanicolaou al día.",
     ["Simulacion1::Gine::VPH", "Manejo"]),

    ("<b>VPH — Caso LEVE.</b> Mujer 23 a, «verruguitas» no dolorosas en horquilla vulvar hace 1 mes. EF: pocas lesiones en coliflor. ¿Dx y conducta?",
     "<b>Condiloma acuminado (VPH 6/11).</b> Crioterapia o imiquimod/podofilotoxina. Consejería + vacuna + Papanicolaou al día.",
     ["Simulacion1::Gine::VPH", "Caso", "Leve"]),

    ("<b>VPH — Caso MODERADO.</b> Múltiples condilomas vulvares y perianales, recurrentes pese a tratamiento previo. ¿Dx y conducta?",
     "<b>Condilomatosis extensa/recurrente.</b> Combinar (crioterapia + imiquimod), valorar resección; revisar adherencia, <b>descartar inmunosupresión</b>, Papanicolaou.",
     ["Simulacion1::Gine::VPH", "Caso", "Moderado"]),

    ("<b>VPH — Caso DIFÍCIL.</b> Embarazada con condilomas vulvares grandes que crecen rápido + Papanicolaou con lesión intraepitelial. ¿Dx y conducta?",
     "<b>Condilomas en embarazo</b> (crecen por inmunomodulación). <b>NO usar podofilina ni imiquimod</b> (contraindicados); usar <b>crioterapia o ácido tricloroacético</b>. Cesárea solo si obstruyen el canal. Lesión cervical → colposcopía/seguimiento posparto.",
     ["Simulacion1::Gine::VPH", "Caso", "Dificil"]),

    # ===================== 5. MOLUSCO CONTAGIOSO =====================
    ("<b>Molusco contagioso — Interrogatorio dirigido.</b> ¿Qué pregunto y qué orienta?",
     "<ul>"
     "<li>Contacto piel con piel; toallas/objetos compartidos.</li>"
     "<li>Niños o contactos con lesiones.</li>"
     "<li><b>Rascado</b> → autoinoculación.</li>"
     "<li>Si es genital → transmisión sexual.</li>"
     "<li><b>Inmunosupresión (VIH)</b> → extenso/atípico.</li></ul>",
     ["Simulacion1::Gine::Molusco", "Interrogatorio"]),

    ("<b>Molusco — Exploración dirigida.</b> ¿Cómo y qué verbalizo?",
     "<i>Verbalizo:</i> «Inspecciono piel y genitales con buena luz.»"
     "<ul>"
     "<li>Busco <b>pápulas perladas, pequeñas (2–5 mm), umbilicadas</b> (depresión central), no dolorosas.</li>"
     "<li>La expresión libera <b>material caseoso central</b> (confirma el dx clínico).</li>"
     "<li><i>Verbalizo:</i> dx clínico; si es extenso/atípico, pensar en inmunosupresión.</li></ul>",
     ["Simulacion1::Gine::Molusco", "Exploracion"]),

    ("<b>Molusco — Manejo:</b> Dx + tratamiento + consejería.",
     "<b>Dx:</b> molusco contagioso (poxvirus). <b>Dif:</b> VPH (coliflor), herpes (vesículas dolorosas)."
     "<ul>"
     "<li><b>Leve/autolimitado:</b> observación (resuelve solo en meses).</li>"
     "<li><b>Pocas lesiones:</b> curetaje/crioterapia; tópicos (KOH, cantaridina).</li></ul>"
     "<b>Consejería:</b> autolimitado; evitar rascarse y compartir toallas; contagia por contacto.",
     ["Simulacion1::Gine::Molusco", "Manejo"]),

    ("<b>MOLUSCO — Caso LEVE.</b> Mujer 20 a, pocas pápulas perladas umbilicadas en pubis, no duelen. ¿Dx y conducta?",
     "<b>Molusco contagioso.</b> Observación o curetaje. Evitar rascado y compartir toallas.",
     ["Simulacion1::Gine::Molusco", "Caso", "Leve"]),

    ("<b>MOLUSCO — Caso MODERADO.</b> Lesiones múltiples diseminadas en pubis y muslos por rascado. ¿Dx y conducta?",
     "<b>Molusco autoinoculado.</b> Curetaje/crioterapia de las lesiones + evitar rascado; tratar pareja si es genital.",
     ["Simulacion1::Gine::Molusco", "Caso", "Moderado"]),

    ("<b>MOLUSCO — Caso DIFÍCIL.</b> Molusco genital MUY extenso, lesiones grandes (&gt;1 cm), recurrentes. ¿Dx y conducta?",
     "<b>Sospechar inmunosupresión (VIH):</b> solicitar prueba de VIH. Tratar lesiones + manejar la causa de base.",
     ["Simulacion1::Gine::Molusco", "Caso", "Dificil"]),

    # ===================== 6. EIP =====================
    ("<b>EIP — Interrogatorio dirigido.</b> ¿Qué pregunto y qué orienta?",
     "<ul>"
     "<li>Dolor pélvico (inicio, lado), fiebre, flujo, <b>dispareunia</b>, sangrado postcoital.</li>"
     "<li>Pareja nueva, condón, ITS previas.</li>"
     "<li><b>FUM y posibilidad de embarazo</b> → descartar ectópico.</li>"
     "<li>Náusea/vómito; <b>dolor súbito unilateral</b> → torsión/ectópico.</li></ul>",
     ["Simulacion1::Gine::EIP", "Interrogatorio"]),

    ("<b>EIP — Exploración dirigida.</b> ¿Cómo y qué verbalizo?",
     "<i>Verbalizo:</i> «Exploro abdomen buscando dolor/irritación; luego, con su consentimiento, hago especuloscopía y tacto bimanual.»"
     "<ul>"
     "<li><b>Abdomen:</b> dolor en hipogastrio; signos peritoneales si es grave.</li>"
     "<li><b>Especuloscopía:</b> cervicitis, flujo mucopurulento.</li>"
     "<li><b>Bimanual:</b> busco <b>dolor a la movilización cervical</b>, dolor uterino y dolor anexial (criterios mínimos); <b>masa anexial = absceso</b>.</li>"
     "<li>Verbalizo cada maniobra y su hallazgo.</li></ul>",
     ["Simulacion1::Gine::EIP", "Exploracion"]),

    ("<b>EIP — Manejo:</b> Dx + estudios + tratamiento.",
     "<b>Dx:</b> dolor pélvico + contexto ITS + dolor a la movilización cervical/uterino/anexial. <b>Dif:</b> ectópico, torsión, apendicitis, tricomoniasis/vaginosis/candidiasis."
     "<ul>"
     "<li><b>Estudios:</b> prueba de embarazo SIEMPRE, NAAT gonorrea/clamidia, exudado, BH/PCR/VSG, USG TV si duda/complicación.</li>"
     "<li><b>Ambulatorio:</b> ceftriaxona 500 mg IM única + doxiciclina 100 mg VO c/12 h 14 d + metronidazol 500 mg VO c/12 h 14 d.</li>"
     "<li><b>No retrasar el antibiótico empírico</b> esperando resultados.</li></ul>",
     ["Simulacion1::Gine::EIP", "Manejo"]),

    ("<b>EIP — Caso LEVE.</b> Mujer 23 a, dolor pélvico bajo 3 días, flujo, dispareunia, pareja nueva sin condón; afebril, estable. Bimanual: dolor a la movilización cervical. Embarazo negativo. ¿Dx y conducta?",
     "<b>EIP leve, manejo ambulatorio:</b> ceftriaxona 500 mg IM única + doxiciclina 14 d + metronidazol 14 d. Tratar pareja; reevaluar en 48–72 h.",
     ["Simulacion1::Gine::EIP", "Caso", "Leve"]),

    ("<b>EIP — Caso MODERADO.</b> Lo mismo + fiebre 38.5°, náusea, dolor anexial bilateral, no tolera la vía oral. ¿Dx y conducta?",
     "<b>EIP que requiere hospitalización:</b> antibiótico IV (cefoxitina/ceftriaxona + doxiciclina ± metronidazol), hidratación; pasar a VO al mejorar.",
     ["Simulacion1::Gine::EIP", "Caso", "Moderado"]),

    ("<b>EIP — Caso DIFÍCIL.</b> Mujer con EIP previa: ahora fiebre persistente, dolor intenso, <b>masa anexial palpable</b>, mal estado general; o bien dolor súbito unilateral con vómito. ¿Dx y conducta?",
     "Diferenciar:<ul>"
     "<li><b>Absceso tubo-ovárico</b> → hospitalizar, antibiótico IV ± drenaje/cirugía.</li>"
     "<li><b>Torsión ovárica</b> → USG Doppler, <b>cirugía urgente</b>.</li>"
     "<li>Siempre <b>descartar embarazo ectópico</b> (prueba de embarazo + USG TV).</li></ul>",
     ["Simulacion1::Gine::EIP", "Caso", "Dificil"]),
]


def main():
    for front, back, tags in CARDS:
        DECK.add_note(genanki.Note(model=MODEL, fields=[front, back], tags=tags))
    genanki.Package(DECK).write_to_file("simulacion-1-gine.apkg")

    # TSV de respaldo (separador TAB). El HTML se mantiene; activar "permitir HTML" al importar.
    with open("simulacion-1-gine.tsv", "w", encoding="utf-8") as f:
        for front, back, tags in CARDS:
            f.write(f"{front}\t{back}\t{' '.join(tags)}\n")

    print(f"Listo: {len(CARDS)} tarjetas -> simulacion-1-gine.apkg + .tsv")


if __name__ == "__main__":
    main()
