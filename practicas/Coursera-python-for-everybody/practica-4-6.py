'''
Escriba un programa para solicitar al usuario las horas y la tarifa por hora utilizando la entrada 
para calcular el salario bruto. El pago debe ser la tarifa normal para las horas hasta 40 horas y la tarifa por hora 
para todas las horas trabajadas por encima de las 40 horas y media. 
Ponga la lógica para hacer el cálculo de pago en una función llamada computepay () y use la función para hacer el cálculo. 
La función debería devolver un valor. Utilice 45 horas y una tarifa de 10,50 por hora para probar el programa 
(el pago debe ser 498,75). Debe usar input para leer una cadena y float () para convertir la cadena en un número. 
No se preocupe por los errores al verificar la entrada del usuario a menos que lo desee; 
puede asumir que el usuario escribe los números correctamente. No nombre su variable suma ni use la función sum ().
'''
def computepay(a, b):
    if a > 40.5:
        pay = a * b
        totalpay = (a - 40) * (b * 0.5)
        finaltotalpay = pay + totalpay
        return finaltotalpay
    else:
        pay = a * b
        return pay

hours = input("Enter hours: ")
rate = input("Enter rate:")
h = float(hours)
r = float(rate)

p = computepay(h, r)
print ("Pay", p)