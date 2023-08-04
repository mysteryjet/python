# Una tupla es una estructura de datos propia de python que permite almacenar distintos tipos de valores,
# son inmutables: no cambian una vez inicializadas.

tupla = (1, 2, 3)
print(tupla)

tupla2 = (7, "Oscar", True, 450.1, 16+7j, 15, "Felicidad", False)
print(tupla2)

tupla3 = (9, 3, (4, 5, 6))
print(tupla3)

# para acceder a un elemento de la tupla2 en su segundo elemento:
print(tupla2[1])

# para acceder al último elemento de la tupla2:
print(tupla2[-1])
# para acceder a los elementos de la posición 0 a la 4 de la tupla2:
print(tupla2[0:4])
# para acceder al penúltimo elemento de la tupla2:
print(tupla2[-2])

# para volcar los elementos de una tupla en variables se hace:
a, b, c = tupla
print(a)
print(b)
print(c)

# para crear una tupla en conjunto con otra
tuplaFinal = tupla + tupla3
print(tuplaFinal)

# para saber cuántas veces se repite un elemento, el argumento es el elemento que estamos buscando
print(tuplaFinal.count(3))
# para saber en qué posición se encuentra un elemento, el argumento es el elemento que estamos buscando
print(tuplaFinal.index(3))