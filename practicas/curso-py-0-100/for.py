# Bucles son estructuras de control que repiten una o varias líneas de código
# Se llaman estructuras de control de flujo porque controlan el flujo del programa, acciones a repetir,
# o veces a repetir datos

for num in range(0, 10, 2):
    print("Valor actual: {}".format(num))

for i in range(1, 11):
    print("{} x {} es: {}".format(i, i, (i * i)))

# muestra la cantidad de letras de cada uno de los nombres en la tupla
for nom in ["Karen", "Oscar", "Héctor", "Leonardo"]:
    print("Cantidad de letras de {} es: {}".format(nom, len(nom)))
