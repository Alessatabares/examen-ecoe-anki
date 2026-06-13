# -*- coding: utf-8 -*-
NAME = "Boca / Dental"

EJES = [
    ("Dolor / tumefacci&oacute;n dental", [
        ("Dolor pulsatil + tumefacci&oacute;n focal de la enc&iacute;a + diente con caries", "Absceso dentario"),
        ("Dolor a la percusi&oacute;n del diente + fluctuaci&oacute;n + fiebre", "Absceso dentario"),
        ("Enc&iacute;as rojas que sangran al cepillado + sin p&eacute;rdida de hueso", "Gingivitis"),
        ("Sangrado gingival + retracci&oacute;n + movilidad dental (p&eacute;rdida de soporte)", "Periodontitis"),
        ("Tumefacci&oacute;n que progresa al piso de boca + dificultad para tragar", "<b>Angina de Ludwig</b>"),
    ]),
    ("Lesi&oacute;n en mucosa oral", [
        ("&Uacute;lcera peque&ntilde;a dolorosa con halo rojo + recurrente + se cura sola", "Aftas"),
        ("Placas blancas que S&Iacute; se desprenden al raspado + dejan base eritematosa", "Candidiasis oral"),
        ("Placa blanca que NO se desprende al raspado + indolora", "Leucoplasia (sospecha de Ca)"),
        ("Placa/&uacute;lcera que no cura en &gt;2 semanas + fumador/alcohol + induraci&oacute;n", "<b>Ca oral</b>"),
        ("Placa eritematosa o mixta que no se desprende + bordes irregulares", "Eritroplasia (sospecha de Ca)"),
    ]),
    ("Tumefacci&oacute;n submandibular / piso de boca", [
        ("Celulitis dura submandibular bilateral + lengua elevada + fiebre", "<b>Angina de Ludwig</b>"),
        ("Foco dental molar inferior + tumefacci&oacute;n del piso de boca", "<b>Angina de Ludwig</b>"),
        ("Estridor + voz apagada + babeo + no traga saliva", "<b>Angina de Ludwig (v&iacute;a a&eacute;rea)</b>"),
        ("Tumefacci&oacute;n focal gingival sin afectar piso de boca", "Absceso dentario"),
    ]),
]

ESTACIONES = [
    ("INSPECCION DE MUCOSA ORAL", [
        ("Placa blanca que se RASPA y desprende", "Base eritematosa al retirarla", "Inmunodeprimido / pr&oacute;tesis", "Candidiasis oral", "antif&uacute;ngico t&oacute;pico"),
        ("Placa blanca que NO se desprende al raspar", "Indolora + fumador", "Persiste en el tiempo", "Leucoplasia (sospecha de Ca)", "biopsia: derivo"),
        ("&Uacute;lcera que no cura en &gt;2 semanas", "Bordes indurados + sangra", "Tabaco + alcohol", "<b>Ca oral</b>", "biopsia urgente: derivo"),
        ("&Uacute;lcera peque&ntilde;a con halo rojo", "Muy dolorosa + recurrente", "Cura sola en d&iacute;as", "Aftas", "sintom&aacute;tico"),
    ]),
    ("PALPACION DEL PISO DE BOCA / SUBMANDIBULAR", [
        ("Induraci&oacute;n le&ntilde;osa submandibular bilateral", "Lengua elevada + babeo", "Fiebre + foco dental molar", "<b>Angina de Ludwig</b>", "v&iacute;a a&eacute;rea + ingreso urgente"),
        ("Estridor / voz apagada al explorar", "No traga la saliva", "Trismo", "<b>Angina de Ludwig (v&iacute;a a&eacute;rea)</b>", "aseguro v&iacute;a a&eacute;rea YA"),
        ("Tumefacci&oacute;n indurada del suelo de la boca", "Adenopat&iacute;a fija p&eacute;trea", "Tabaco + alcohol", "<b>Ca oral</b>", "derivo + biopsia"),
    ]),
    ("EXPLORACION DENTAL / GINGIVAL", [
        ("Diente con caries + dolor a la percusi&oacute;n", "Tumefacci&oacute;n gingival fluctuante", "Fiebre", "Absceso dentario", "drenaje + antibi&oacute;tico"),
        ("Enc&iacute;as rojas que sangran al sondaje", "Sin movilidad ni p&eacute;rdida &oacute;sea", "Placa bacteriana", "Gingivitis", "higiene: reversible"),
        ("Retracci&oacute;n gingival + bolsas profundas", "Movilidad dental + p&eacute;rdida de soporte", "Sangrado", "Periodontitis", "derivo a periodoncia"),
    ]),
]
