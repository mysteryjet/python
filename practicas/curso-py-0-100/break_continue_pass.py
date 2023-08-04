# break permite salir de un bucle cuando se cumple una condición

for num in range(1, 6):
    if num == 3:
        break
    print("El número es: {}".format(num))
print("Bucle terminado.")

# Continue: omite una parte del bucle cuando se cumple una condición y continúa con el resto

for numero in range (1, 6):
    if numero == 3:
        continue
    print("El número es: {}".format(numero))
print("Bucle terminado.")

# Pass: permite continuar con una sentencia o función que ya no tiene un bloque de código útil

for numero in range (1, 6):
    if numero <= 3:
        # aqui no pasa nada y el bucle sigue trabajando
        pass
    else:
        print("El siguiente valor es mayor a 3: ")
    print("El número es: {}".format(numero))
print("Bucle terminado.")