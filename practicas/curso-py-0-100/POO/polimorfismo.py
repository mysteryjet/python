# polimorfismo (poli = muchas, morfos = formas)

class Estudiante:
    def describir(self):
        print("Soy un buen estudiante.")


class Docente:
    def describir(self):
        print("Soy un buen maestro.")


class Trabajador:
    def describir(self):
        print("Soy un buen trabajador.")


def describir_persona(persona):
    persona.describir()


doc1 = Trabajador()
describir_persona(doc1)

