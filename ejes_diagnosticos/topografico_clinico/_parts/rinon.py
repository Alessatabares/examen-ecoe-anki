# -*- coding: utf-8 -*-
NAME = "Rinon / Urinario"

EJES = [
  ("Oliguria / anuria", [
    ("Hipotensi&oacute;n + sed + mucosas secas + FeNa &lt;1% + BUN/Cr &gt;20", "AKI prerrenal (por hipoperfusi&oacute;n)"),
    ("Hipovolemia por v&oacute;mitos/diarrea/diur&eacute;ticos + orina concentrada Na &lt;20", "AKI prerrenal"),
    ("Tras hipotensi&oacute;n/sepsis/nefrot&oacute;xico + cilindros granulosos pardos + FeNa &gt;2%", "Necrosis tubular aguda (NTA)"),
    ("Anuria s&uacute;bita + globo vesical + dilataci&oacute;n bilateral en USG", "<b>Obstrucci&oacute;n postrenal (uropat&iacute;a obstructiva)</b>"),
    ("Oliguria + edema + HTA + hematuria con cilindros hem&aacute;ticos", "S&iacute;ndrome nefr&iacute;tico (GN aguda)"),
    ("Var&oacute;n mayor + globo vesical palpable + goteo y chorro d&eacute;bil previos", "Retenci&oacute;n urinaria por HBP"),
    ("Oliguria progresiva en meses + eGFR bajo cr&oacute;nico + ri&ntilde;ones peque&ntilde;os", "Enfermedad renal cr&oacute;nica (ERC)"),
  ]),
  ("Hematuria", [
    ("Microhematuria + cilindros hem&aacute;ticos + hemat&iacute;es dismorficos + proteinuria", "S&iacute;ndrome nefr&iacute;tico (origen glomerular)"),
    ("Macrohematuria + c&oacute;lico lumbar irradiado a genitales + agitaci&oacute;n", "Litiasis ureteral"),
    ("Hematuria + disuria + polaquiuria + dolor suprap&uacute;bico sin fiebre", "Cistitis"),
    ("Macrohematuria indolora + tabaquismo + edad avanzada", "Neoplasia urotelial (descartar)"),
    ("Hematuria + fiebre + lumbalgia + pu&ntilde;o-percusi&oacute;n positiva", "Pielonefritis aguda"),
    ("Hematuria 1-2 d&iacute;as tras infecci&oacute;n respiratoria (sin&iacute;faringitis)", "Nefropat&iacute;a IgA"),
  ]),
  ("Edema", [
    ("Edema gravitacional + proteinuria &gt;3.5 g/d&iacute;a + hipoalbuminemia + hiperlipidemia", "S&iacute;ndrome nefr&oacute;tico"),
    ("Edema periorbitario matutino + HTA + hematuria + oliguria", "S&iacute;ndrome nefr&iacute;tico"),
    ("Edema generalizado + eGFR bajo + albuminuria + anemia + sobrecarga", "ERC con sobrecarga de volumen"),
    ("Edema con espuma en la orina (proteinuria masiva) + trombosis venosa", "S&iacute;ndrome nefr&oacute;tico (estado protromb&oacute;tico)"),
    ("Edema + balance positivo tras reposici&oacute;n excesiva en AKI", "Sobrecarga h&iacute;drica i&aacute;trogena"),
  ]),
  ("Dolor lumbar / c&oacute;lico renal", [
    ("C&oacute;lico s&uacute;bito en flanco irradiado a ingle + paciente inquieto + hematuria", "Litiasis (c&oacute;lico nefr&iacute;tico)"),
    ("Lumbalgia + fiebre alta + escalofr&iacute;os + Giordano positivo + piuria", "<b>Pielonefritis aguda</b>"),
    ("Dolor lumbar + anuria + hidronefrosis bilateral en USG", "<b>Uropat&iacute;a obstructiva</b>"),
    ("Lumbalgia + fiebre + obstrucci&oacute;n (c&aacute;lculo que no progresa)", "<b>Pionefrosis / sepsis urinaria obstructiva (urgencia)</b>"),
    ("Dolor sordo cr&oacute;nico + ri&ntilde;ones poliqu&iacute;sticos palpables + HTA", "Poliquistosis renal (PQRAD)"),
  ]),
  ("S&iacute;ndrome urinario (disuria / polaquiuria)", [
    ("Disuria + polaquiuria + urgencia + dolor suprap&uacute;bico SIN fiebre", "Cistitis (ITU baja)"),
    ("Disuria + fiebre + lumbalgia + Giordano positivo + malestar general", "Pielonefritis (ITU alta)"),
    ("Disuria + secreci&oacute;n uretral + pareja con s&iacute;ntomas", "Uretritis (ITS)"),
    ("Polaquiuria + nicturia + chorro d&eacute;bil + goteo en var&oacute;n mayor", "HBP"),
    ("Disuria + piuria est&eacute;ril (urocultivo negativo de rutina)", "Uretritis por Chlamydia / TB urinaria"),
    ("S&iacute;ntomas urinarios + exantema + eosinofilia + f&aacute;rmaco reciente (AINE/antibi&oacute;tico)", "Nefritis intersticial aguda (NIA)"),
  ]),
]

ESTACIONES = [
  ("SIGNOS VITALES / VOLEMIA", [
    ("Hipotensi&oacute;n ortost&aacute;tica + taquicardia + mucosas secas", "Pliegue cut&aacute;neo lento + sed", "Oliguria con orina concentrada", "AKI prerrenal (hipovolemia)", "valoro volemia: la prerrenal mejora con reposici&oacute;n; pido FeNa y BUN/Cr"),
    ("Fiebre + taquicardia + hipotensi&oacute;n", "Lumbalgia + Giordano positivo", "Oliguria", "<b>Sepsis urinaria / pielonefritis</b>", "shock s&eacute;ptico de foco urinario: hemocultivo + antibi&oacute;tico precoz + l&iacute;quidos"),
    ("HTA + edema + ingurgitaci&oacute;n yugular", "Crepitantes bibasales (sobrecarga)", "Oliguria reciente", "AKI/ERC con sobrecarga de volumen", "hipervolemia: restrinjo l&iacute;quidos y Na, valoro di&aacute;lisis si refractario"),
  ]),
  ("PUNO-PERCUSION RENAL (GIORDANO)", [
    ("Pu&ntilde;o-percusi&oacute;n lumbar dolorosa unilateral", "Fiebre alta + escalofr&iacute;os", "Piuria + bacteriuria", "Pielonefritis aguda", "Giordano positivo + fiebre = ITU alta; urocultivo y antibi&oacute;tico, no solo tira"),
    ("Pu&ntilde;o-percusi&oacute;n positiva + dolor c&oacute;lico que no cede", "Paciente inquieto que no halla postura", "Hematuria + fiebre", "<b>C&aacute;lculo obstructivo infectado (urgencia)</b>", "obstrucci&oacute;n + fiebre exige drenaje urgente (cat&eacute;ter doble J / nefrostom&iacute;a)"),
    ("Pu&ntilde;o-percusi&oacute;n negativa", "Disuria + polaquiuria sin fiebre", "Dolor suprap&uacute;bico", "Cistitis (ITU baja)", "Giordano negativo + sin fiebre orienta a vejiga, no a ri&ntilde;&oacute;n"),
  ]),
  ("PALPACION VESICAL (GLOBO)", [
    ("Masa suprap&uacute;bica mate redondeada y dolorosa", "Deseo miccional intenso sin poder orinar", "Var&oacute;n mayor con prostatismo", "Retenci&oacute;n urinaria aguda (HBP)", "globo vesical: sondaje vesical descompresivo; alivia el dolor y protege el ri&ntilde;&oacute;n"),
    ("Globo vesical + anuria + creatinina elevada", "Hidronefrosis bilateral en USG", "Antecedente de obstrucci&oacute;n baja", "<b>AKI postrenal obstructiva</b>", "descomprimo (sonda/nefrostom&iacute;a): la causa postrenal es potencialmente reversible"),
    ("Ausencia de globo + oliguria", "Mucosas secas / hipotensi&oacute;n", "FeNa &lt;1%", "AKI prerrenal", "vejiga vac&iacute;a descarta retenci&oacute;n; el problema es de perfusi&oacute;n, no obstructivo"),
  ]),
  ("EXAMEN DE ORINA / SEDIMENTO (INTERPRETACION)", [
    ("Cilindros granulosos pardos (muddy brown)", "FeNa &gt;2% + Na urinario &gt;40", "Tras isquemia o nefrot&oacute;xico", "Necrosis tubular aguda (NTA)", "cilindros pardos + FeNa alta = da&ntilde;o tubular intr&iacute;nseco, ya no prerrenal"),
    ("Cilindros hem&aacute;ticos + hemat&iacute;es dismorficos", "Proteinuria + HTA + edema", "Oliguria", "S&iacute;ndrome nefr&iacute;tico (glom&eacute;rulo)", "cilindros hem&aacute;ticos = hematuria glomerular; estudio inmunol&oacute;gico y complemento"),
    ("Proteinuria &gt;3.5 g/24h + cuerpos ovales grasos (cruz de Malta)", "Hipoalbuminemia + hiperlipidemia", "Edema con espuma", "S&iacute;ndrome nefr&oacute;tico", "proteinuria masiva define el nefr&oacute;tico; cuantifico con cociente prote&iacute;na/creatinina"),
    ("Leucocituria + nitritos + bacteriuria", "Disuria + polaquiuria", "Urocultivo &gt;100000 UFC", "ITU (cistitis / pielonefritis)", "tira con nitritos + leucocitos apoya ITU; confirmo con urocultivo antes de antibi&oacute;tico"),
    ("Piuria est&eacute;ril + cilindros leucocitarios + eosinofiluria", "Exantema + eosinofilia + f&aacute;rmaco reciente", "Creatinina en ascenso", "Nefritis intersticial aguda (NIA)", "piuria est&eacute;ril + eosin&oacute;filos + f&aacute;rmaco = NIA; retiro el f&aacute;rmaco causal"),
    ("Cristaluria + hematuria + pH orientativo", "C&oacute;lico lumbar irradiado a ingle", "Imagen de c&aacute;lculo en USG/TC", "Litiasis renal", "cristales y hematuria con c&oacute;lico apoyan litiasis; TC sin contraste lo confirma"),
  ]),
  ("EDEMA / BALANCE HIDRICO (KDIGO-ERC)", [
    ("Fovea en miembros inferiores + edema palpebral", "Proteinuria + hipoalbuminemia", "Aumento de peso", "S&iacute;ndrome nefr&oacute;tico", "edema con foveola + proteinuria masiva; pierdo albumina por orina, retengo agua y sal"),
    ("eGFR &lt;60 sostenido &ge;3 meses + albuminuria", "Anemia + hiperfosfatemia + acidosis", "HTA + edema", "ERC (estadios G y A de KDIGO)", "clasifico por eGFR (G1-G5) y albuminuria (A1-A3); no es solo un n&uacute;mero de creatinina"),
    ("Diuresis &lt;0.5 ml/kg/h &ge;6 h o creatinina en ascenso", "Balance h&iacute;drico positivo", "Sobrecarga de volumen", "AKI (criterios KDIGO)", "AKI por diuresis/creatinina; vigilo K+, acidosis y sobrecarga (indicaciones de di&aacute;lisis: AEIOU)"),
    ("Edema refractario + hiperpotasemia + acidosis + ur&eacute;mia", "Pericarditis o encefalopat&iacute;a ur&eacute;mica", "Sobrecarga que no responde a diur&eacute;tico", "<b>Indicaci&oacute;n de di&aacute;lisis urgente</b>", "AEIOU: Acidosis, Electrolitos (K+), Intoxicaci&oacute;n, Overload, Ur&eacute;mia &rarr; di&aacute;lisis"),
  ]),
]
