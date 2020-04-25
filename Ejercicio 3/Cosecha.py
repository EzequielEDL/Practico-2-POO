class Cosecha:
    __kilos = []

    def __init__ (self, kilos = [0, 0, 0]):
        if type(kilos) == type(self.__kilos) :
            self.__kilos = kilos
        else :
            print('<< Error en la verificacion de tipos de datos >>')  

    def getKilos(self):
        return self.__kilos