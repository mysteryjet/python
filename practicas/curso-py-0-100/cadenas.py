texto = "Bienvenido al curso de Python desde 0"
print(texto)
print(texto.lower())
print(texto.upper())
print(texto.title())

# para buscar una porción de texto se usa la funcion find()
# esta indicará la posición donde comienza dicha porción a buscar
print(texto.find("al"))

# cantidad de ocurrencias de una letra o porción
print(texto.count("e"))

# reemplaza en una cadena un caracter tomando como argumento el caracter original y el segundo por el caracter nuevo
textoFinal = texto.replace("a", "4")
textoFinal = texto.replace("e", "3")
print(textoFinal)

print(texto.isnumeric())  # Arroja True o False, dependiendo si es un número

# arroja un array separando una cadena tomando como argumento el caracter en el que se quiera separar
cadenaSeparada = texto.split(" ")
print(cadenaSeparada)
