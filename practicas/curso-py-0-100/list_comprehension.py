import math

numeros = [1, 4, 9, 16, 25]

# esto es una list comprehension
# la lista interna es asignada a la variable cuando todos los elementos han
# sido procesados:
raices = [int(math.sqrt(x) )for x in numeros]



# la list comprehension ayuda a entender la sintaxis anterior:

"""for n in numeros:
    raices.append(int(math.sqrt(n)))
    print(n)"""

print(raices)

v = [b if (b > 10) else '*' for b in numeros]
print(v)

l = [c.upper() for c in 'Manuel']
print(l)
print([c.upper() for c in 'Manuel'])

a = [l if l in 'aeiou' else 'X' for l in 'murcielago']
print(a)



