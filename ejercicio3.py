"""

Un programa que compruebe si una variable este vacia, y si esta vacia rellenarla con texto
en minusculas y mostralo en mayusculas.

"""

texto = ""

if len(texto.strip()) <= 0:
    texto = "Hola soy un texto en minusculas"
    print(texto.upper())
    
else:
    print(f"La variable tiene contenido {texto}")    