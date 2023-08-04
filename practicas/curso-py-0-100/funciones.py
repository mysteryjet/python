# función es un conjunto de instrucciones que realizan un proceso
# Su principal ventaja es que nos ayudan a evitar código que se repite

def saludar():
    print("Hola")
    return "Mundo"


print(saludar())


def evaluar_sueldo_min(sueldo):
    if sueldo >= 850:
        print("Cumples con el sueldo.")
    else:
        print("Ganas menos que el sueldo mínimo.")


evaluar_sueldo_min(200)
