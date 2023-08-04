# AND Equivalente a "Y si además..."
# OR "o sino..."
# NOT -> negación

distancia = 400
numeroHermanos = 3
salarioPadres = 3500
tieneBeneficio = False

if (distancia > 1000 and numeroHermanos > 2) or salarioPadres < 2000:
    tieneBeneficio = True

print(not tieneBeneficio)

if (5 > 3) or (8 < 6):
    print("verdad")
else:
    print("Es mentira...")

