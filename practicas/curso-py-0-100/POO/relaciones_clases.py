class Pais:
    def __init__(self, nom, pre):
        self.nombre = nom
        self.presidente = pre

    def __str__(self):
        txt = "Pais: {} - Presidente: {}"
        return txt.format(self.nombre, self.presidente)


class Ciudad:
    def __init__(self, nom, hab, pai):
        self.nombre = nom
        self.habitantes = hab
        self.pais = pai

    def __str__(self):
        txt = "Ciudad: {} - Num. Habitantes: {} ({})".format(self.nombre, self.habitantes, self.pais)
        return txt


class Urbanizacion:
    def __init__(self, nom, ciu):
        self.nombre = nom
        self.ciudad = ciu

    def __str__(self):
        txt = "Urbanización: {} ({})".format(self.nombre, self.ciudad)
        return txt


pais1 = Pais("Peru", "Martin Vizcarra")
print(pais1)

ciudad1 = Ciudad("Chiclayo", 150000, pais1.nombre)
print(ciudad1)

urba1 = Urbanizacion("María de los Angeles", ciudad1)
print(urba1)