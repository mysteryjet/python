# generadores: permiten extraer valores de una función y almacenarlos de uno en uno
# en objetos iterables (objetos que se pueden recorrer) sin la necesidad de almacenar todos a la vez en la memoria ram
# son más eficientes que las funciones tradicionales
# muy útiles con listas de valores infinitos
# entre llamada y llamada, el objeto iterable entra en un estado de pausa (suspensión)
"""
def genera_multiplos(limite):
    numero = 1
    listaNumeros=[]

    while numero <= limite:
        listaNumeros.append(numero * 7)
        numero = numero + 1
    return listaNumeros
"""


def genera_multiplos(limite):
    numero = 1

    while numero <= limite:
        yield numero * 7
        numero = numero + 1


obtiene_Multiplos = genera_multiplos(10)

"""print(obtiene_Multiplos)
for n in obtiene_Multiplos:
    print(n)
"""

# next(): retorna el siguiente elemento de un objeto iterable
print(next(obtiene_Multiplos))
print("Acá hay 300 líneas de código")
print(next(obtiene_Multiplos))
print("Acá hay 1000 líneas de código")
print(next(obtiene_Multiplos))