# factorial de un número es el producto de todos los numeros positivos enteros
# comprendidos entre 1 y un determinado número
# Factorial de 5:  1 * 2 * 3 * 4 * 5 = 120

numero = int(input("Ingrese un número: "))
factorial = 1
for n in range(1, numero+1):
    factorial = factorial * n

print("El factorial de {} es {}.".format(numero, factorial))
