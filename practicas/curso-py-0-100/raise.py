# raise: sirve para lanzar de forma intencional excepciones en python.

def evaluar_notas(nota):
    if nota < 0:
        # raise ZeroDivisionError("Este mensaje es personalizado de la excepción.")
        raise ValueError("Valor incorrecto...")
    elif nota >= 16:
        print("Excelente")
    elif nota >= 11:
        print("Aprobado")
    else:
        print("Reprobado")


evaluar_notas(-2)

print("Este es el fin de mi programa.")