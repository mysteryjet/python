texto1 = "Hola"
texto2 = "mundo"
print("El saludo concatenado con operador es: " + texto1 + " " + texto2)
print("**********************************")

print("El saludo con comodín es: %s %s" % (texto1, texto2))  # concatenación con comodín
print("**********************************")

saludoFinal = "El saludo con .format: {} {}".format(texto1, texto2) # concatenación con .format
print(saludoFinal)
print("**********************************")

saludoFinal2 = "Saludo de la 4ta forma es: {x} {y}".format(x=texto1, y=texto2)
print(saludoFinal2)
print("**********************************")