# Es una de las funciones de orden superior, que está ligada al paradigma de la programación funcional.
# Verifica que los elementos de una lista cumplan una determinanda condición, devolviendo un objeto iterable
# con los elementos que cumplieron esa condición determinada que se indicó.

edades = [12, 11, 24, 36, 8, 6, 10, 43, 58, 14, 50, 7]


def mayor_edad(edad):
    return edad >= 18

# print(filter(mayor_edad, edades))
edades_mayores_edad = list(filter(mayor_edad, edades))
# print(edades_mayores_edad)

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return "{} tiene {} años.".format(self.nombre, self.edad)


personas= [
    Persona("Alberto", 32),
    Persona("Ana", 16),
    Persona("Andy", 27),
    Persona("Jesús", 25),
    Persona("Cecilia", 19),
    Persona("Laura", 30),
]

personas_mayores_edad = list(filter(lambda per: per.edad >= 18, personas))
print(personas_mayores_edad)

for per in personas_mayores_edad:
    print(per)