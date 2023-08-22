from enum import Enum

class Color(Enum):
    rojo = '#ff0000'
    verde = '#008000'
    azul = '#0000ff'

print(Color.rojo)
print(Color.rojo.value)
print(Color('#008000'))
print(Color['rojo'].value)

lista = [c for c in Color]
print(lista)
lista = list([c for c in Color])
print(lista)
print(len(lista))

for a in lista:
    print(a.value)
