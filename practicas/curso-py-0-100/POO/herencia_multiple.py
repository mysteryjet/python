# La herencia múltiple toma como argumentos los que tenga la primera clase que se le pasa
# como primer parámetro, en este caso, en la ClaseX, se le paro como primer parámetro la ClaseA
# de tal forma, que para instanciar el objeto cX1, se le debe hacer pasando como argumentos los que solicite
# la ClseA, que en este caso eran dos argumentos los que pide.

class ClaseA:
    def __init__(self, par1, par2):
        self.parametro1 = par1
        self.parametro2 = par2


class ClaseB:
    def __init__(self, par3, par4, par5):
        self.parametro3 = par3
        self.parametro4 = par4
        self.parametro5 = par5


class ClaseX(ClaseA, ClaseB):
    pass


cX1 = ClaseX(15, 21)