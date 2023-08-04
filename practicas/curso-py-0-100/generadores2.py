# cuando indicamos un * adelante del parámetro de una función, se indica que se va a recibir un
# número indeterminado de parámetros, y se reciben en forma de tupla

"""
def devuelve_lenguajes(*lenguajes):
    for leng in lenguajes:
        yield leng
"""
def devuelve_lenguajes(*lenguajes):
    for leng in lenguajes:
        yield from leng

lenguajesObtenidos = devuelve_lenguajes("Python", "Java", "PHP", "Ruby", "JavaScript")

print(next(lenguajesObtenidos))
print(next(lenguajesObtenidos))