import math

x = 1.553
print(round(x))
print(round(x, 1))
print('Redondea a numero entero superior: ',math.ceil(x))
print('Redondea a número entero hacia abajo: ', math.floor(x))
print('Retorna la parte entera en un número decimal: ', math.trunc(x))

numeros = range(1,6)
print("Suma de elementos de un objeto iterable, en este caso una lista: ", math.fsum(numeros))
print("Como el resultado lo arroja en decimal, lo transformamos a int: ", int(math.fsum(numeros)))

print("Para valores absolutos se usa la función fabs: {}".format(math.fabs(-4)))
print("Para obtener el módulo/residuo de una división se usa la función fmod, pide dos parámetros,")
print("que serían los números a dividir")
print("El módulo de 17/6 es: {}\n".format(math.fmod(17,6)))
print("La función exp devuelve épsilon elevado a algún número que pasemos como parámetro.")
print(math.exp(2)) # e elevado al cuadrado
print("\nLa función para obtener el valor de PI es pi: {}".format(math.pi))
print("\nLa función para obtener el valor de un número elevado a determinada potencia es pow")
print("El resultado de elevar 5 a la 6ta potencia es: {}".format(math.pow(5,6)))
print("\nLa función para obtener la raíz de un número es sqrt")
print("La raíz cuadrada de 16 es: {}".format(math.sqrt(16)))

h = math.hypot(1.5,1.5)
print("\nLa hipotenusa de dos coordenadas dadas que es 1.5 y 1.5 es: ", h)
print("\nPara convertir a radianes se usa la función math.radians")
r = math.radians(45)
print("Valor en radianes de 45: {}".format(r))
print("\nPara calcular el seno se usa la función sin. El seno de 67 es: {}".format(math.sin(67)))

