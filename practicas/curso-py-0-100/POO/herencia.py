class Persona():

    def __init__(self, ape_pat, ape_mat, nom):
        self.apellido_paterno = ape_pat
        self.apellido_materno = ape_mat
        self.nombres = nom

    def mostrar_nombre(self):
        txt = "{} {} {}"
        return txt.format(self.apellido_paterno, self.apellido_materno, self.nombres)

    def datos(self):
        print(self.mostrar_nombre())


# se reutiliza el código de la clase Persona, ya que la clase estudiante tienen en común esos atributos
# se usa una función llamada super() para heredar el constructor de la clase padre.
class Estudiante(Persona):

    def __init__(self, ape_pat, ape_mat, nom, pro):
        super().__init__(ape_pat, ape_mat, nom)
        self.profesion = pro

    def datos(self):
        super().datos()
        print("Profesion: {}".format(self.profesion))



# est1 = Estudiante("Leonheart", "Raine", "Squall", "Mercenario")
est1 = Persona("Leonheart", "Raine", "Squall")
# print(est1.mostrar_nombre())
# print(est1.profesion)

# est1.datos()

print(isinstance(est1, Persona))
