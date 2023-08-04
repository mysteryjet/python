# Las listas son estructuras de datos que nos permiten almacenar distintos valores
# Son equivalentes a los arrays en otros lenguajes de programación
# Son estructuras dinámicas, es decir que pueden cambiar su tamaño añadiendo nuevos elementos, pueden mutar.
# Lo anterior es la principal diferencia con las tuplas

lista1 = ["Oscar", 25, 98.3, True, "Felicidad", 3.14]
print(lista1)
print(lista1[:])  # para imprimir todos los elementos de la lista1
print(lista1[1])  # para imprimir un elemento es una posición en específica
print(lista1[-1])  # para imprimir el último elemento en la lista1
print(lista1[0:3])  # para imprimir solo una porción de la lista1
print(lista1[:2])  # para acceder a los dos primeros elementos de lista1
print(lista1[3:])  # para acceder desde la posición marcada por el tres, hasta el final de la lista

# estructuras dinámicas
lista1.append("Manuel")  # para agregar un elemento a la lista, se agrega al final de ésta
print(lista1)
lista1.insert(4, "México")  # para insertar un elemento, el primer argumento es la posición donde se quiere agregar
# el segundo argumento es el elemento que quiere insertar.
print(lista1)
lista1.extend(["Alejandro", 110, False])  # para extender una lista con otra lista
print(lista1)

# para saber en que posición se encuentra un elemento, se pasa como argumento el elemento que se quiere buscar
print(lista1.index("Felicidad"))

# para remover un elemento de la lista, se pasa como argumento el elemento que se desea quitar de la lista
lista1.remove("Felicidad")
print(lista1)

# para eliminar el último elemento de una lista
lista1.pop()
print(lista1)

# para comprobar si un elemento está en una lista mediante un valor de retorno True o False
print("Manuel" in lista1)
