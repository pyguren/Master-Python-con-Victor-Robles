"""
Crear un script que tenga 4 variables, una lista, un string, un entero, un booleano y que imprima
un mensaje segun el tipo de dato de cada variable, usar funciones
"""

from pickle import TRUE

def traducirTipo(tipo):
    result = None
    
    if tipo == list:
        result = "Lista"
    elif tipo == str:
        result = "Sting"
    elif tipo == int:
        result = "Numero entero"
    elif tipo == bool:
        result = "Booleano"
        
    return result
    
    
def comprobarTipado(dato, tipo):
    test = isinstance(dato, tipo)
    result = ""
    
    if test:
        result = print(f"Este dato es del tipo {traducirTipo(dato)}")
    
    else:
        result = None
    
    return result



mi_lista = ["Hola mundo", 77]
titulo = "master en python"
numero = 100
verdadero = True


print(comprobarTipado(mi_lista, list))
print(comprobarTipado(titulo, str))
print(comprobarTipado(numero, int))
print(comprobarTipado(verdadero, bool))
