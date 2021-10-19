encontrado = False
print("Antes", encontrado)
for valor in [9, 41, 12, 3, 74, 15]:
    if valor == 3: 
        encontrado = True
    print (encontrado, valor)
print("Después", encontrado)