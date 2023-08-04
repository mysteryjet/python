# Diccionarios son estructuras de datos que permiten almacenar distintos valores
# Su principal característica es que los datos se almacenan asociados a una clave única, tenemos una relación
# clave: valor

# Los elementos almacenados están en desorden, el órden es indiferente a la forma de almacenamiento

miDiccionario = {"España": "Madrid", "Perú": "Lima", "Alemania": "Berlín"}
print(miDiccionario["Perú"])  # para acceder al valor de la clave/key de un elemento en el diccionario

# para agregar un elemento al diccionario, en corchetes se agrega la clave/key
miDiccionario["Venezuela"] = "Caracas"
print(miDiccionario)

# para reemplazar el valor de un elemento que ya esté en el diccionario, se usa la sintaxis anterior
miDiccionario["Perú"] = "Limón"
print(miDiccionario)

# para eliminar un valor, asociado a su clave se usa:
del miDiccionario["Perú"]
print(miDiccionario)

dic2 = {"Pérez": "Juan", 25: True, "Sueldo": 150.8}
print(dic2[25])

# se puede usar una tupla para definir las llaves que tendrá el diccionario:
llaves = ("España", "Francia", "Ingraterra")
dicPaises = {llaves[0]: "Madrid", llaves[1]: "París", llaves[2]: "Londres"}
print(dicPaises)
# para meter un diccionario dentro de otro
datosPersonales = {"Apellido": "Garcia", "Annos": {1: 2010, 2: 2011, 3: 2012, 4: 2013, 5: 2014}}
print(datosPersonales)
print(datosPersonales["Annos"][2])  # para poder acceder al valor de la key, tenemos que pasar como argumento
# el diccionario y la key donde se encuentra el elemento que queremos encontrar
# para usar la función get
print(datosPersonales.get("Ape", "Oscar"))
# para conocer las llaves del diccionario se usa:
print(datosPersonales.keys())
# para conocer los valores del diccionario se usa:
print(datosPersonales.values())
# para convertir en lista los valores de un diccionario:
valores = list(datosPersonales.values())
print(valores)
# para convertir en tupla los valores de un diccionario:
valores = tuple(datosPersonales.values())
print(valores)

