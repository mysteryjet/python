'''
Programa para Calcular J
en Anualidades Vencidad

A= 40000
N = 18
R =  3000
m = 6
j = 0.2


'''

def equivalencia (n, r, m, j) :
    res = (j / m)
    res += 1
    res = res ** -n
    res -= 1
    res = res / (j / m)
    res = res * r
    res = res * -1

    return res 

a = float(input("A = "))
n = float(input("N = "))
r = float(input("R = "))
m = float(input("m = "))
j = float(input("j = "))
aprox = equivalencia(n, r, m, j)

while True:
    print(aprox)
    j = float(input("j = "))
    aprox = equivalencia(n, r, m, j)



