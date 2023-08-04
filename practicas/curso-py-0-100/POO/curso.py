class Curso():
    """
    nombre = "Matemática"
    creditos = 5
    profesion = "Ingeniería Civil"
    """
    # Estado inicial del objeto
    def __init__(self, nom, cre, pro):
        self.nombre = nom
        self.creditos = cre
        self.profesion = pro
        self.__imparticion = "Presencial"  # Propiedad encapsulada
# El encapsulamiento en POO es esconder/encapsular, una propiedad o función dentro de una clase, aqui
# se hará con una propiedad dentro de la clase

    def mostrar_datos(self):
        dat = "Nombre del curso: {} / Créditos: {} / Modo de impartición: {}"
        print(dat.format(self.nombre, self.creditos, self.__imparticion))
        docente_asignado = self.__verificar_docente()
        if docente_asignado:
            print("Existe docente asignado.")
        else:
            print("Es necesario asignar un docente.")

# Aquí se encapsulara esta función para que no se pueda llamar, únicamente mediante la función mostrar_datos
    def __verificar_docente(self):
        print("Verificando si existe docente asignado...")
        if self.__imparticion == "Presencial":
            return True
        else:
            return False

# Esta función va a llamarse cuando intentamos imprimir el objeto o instancia sin indicar atributo
# Es una función que retorna en formato de texto los datos de una instancia de una clase
    def __str__(self):
        texto = "Nombre: {} - Créditos: {}"
        return texto.format(self.nombre, self.creditos)


curso1 = Curso("Matemática", 5, "Ingeniería Civil")
print(curso1.nombre)
curso1.mostrar_datos()

curso2 = Curso("Lenguaje", 16, "Literatura")
print(curso2.nombre, curso2.creditos, curso2.profesion)

print(curso1)
