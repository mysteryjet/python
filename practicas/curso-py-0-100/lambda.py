# Las funciones lambda son funciones anónimas que sirven para abreviar o resumir una función más
# simple o sencilla de leer.

# la siguiente función ejemplo nos ayudará a diferenciar
"""def sumar(n1, n2):
    return n1 + n2


print(sumar(12,2))"""

# Toda función lambda se puede convertir a una función normal, pero no viceversa.
# esta es la función lambda:
sumar = lambda n1, n2: n1 + n2
print(sumar(2,3))

elevar_cuadrado = lambda num:  num * num
print(elevar_cuadrado(3))
