# Excepción: es un error en tiempo de ejecución (durante la ejecución de un programa)

num1 = 20
num2 = 2

# print("La división de {} entre {} es: ".format(num1, num2, (num1 / num2)))
try:
    resultado = num1 / num2
except ZeroDivisionError:
    print("No se puede dividir entre 0..")
finally:
    print("Yo siempre aparezco.")

print("Aquí termina mi programa.")
