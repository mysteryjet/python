class Cuenta():
    def __init__(self, pro, sal, mon):
        self.__propietario = pro
        self.__saldo = sal
        self.__moneda = mon
    # Estos métodos sirven para leer o modificar propiedades dentro de una clase
    # para este caso, para propiedades encapsuladas que no se modifican ni leen desde afuera de la clase

    # Getters (métodos GET)
    def get_saldo(self):
        return self.__saldo
    def get_propietario(self):
        return self.__propietario
    def get_moneda(self):
        return self.__moneda

    # Setters (métodos SET)
    def set_moneda(self, moneda):
        self.__moneda = moneda


cuenta1 = Cuenta("Squall Leonheart", 1500, "Pesos")
print(cuenta1.get_saldo(), cuenta1.get_moneda())
cuenta1.set_moneda("Dólares")
print(cuenta1.get_saldo(), cuenta1.get_moneda())
