print("--Cursos--")
print("Matemática - Biología - Lenguaje - Ciencias")

curso = input("Ingrese el curso deseado: ").title()

if curso in ("Matematicas", "Biologia", "Lenguaje", "Ciencias"):
    print("Curso {} seleccionado.".format(curso))
else:
    print("No existe ese curso...")

