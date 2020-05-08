class Camion:
    __id = 0
    __nombreConductor = ''
    __patenteCamion = ''
    __marcaCamion = ''
    __tara = 0

    def __init__(self, id, nombreConductor, patenteCamion, marcaCamion, tara):
        if self.__testing(id, nombreConductor, patenteCamion, marcaCamion, tara) :
            self.__id = int(id)
            self.__nombreConductor = str(nombreConductor)
            self.__patenteCamion = str(patenteCamion)
            self.__marcaCamion = str(marcaCamion)
            self.__tara = int(tara)
        else :
            print('<< Error en la verificacion de tipos de datos >>')  

    def __str__(self) :
        return ' {:>02}: {:<10}{:<8}{:<11}{:0000}.kg'.format(self.__id, self.__nombreConductor, self.__patenteCamion, self.__marcaCamion, self.__tara)
        
    def __testing(self, id, nombreConductor, patenteCamion, marcaCamion, tara):
        if id.isdecimal() and nombreConductor.isalpha() and patenteCamion.isalnum() and marcaCamion.isalpha() and tara.isdecimal() :
            return True
        else :
            return False

    def getTara(self):
        return self.__tara
    
    def getId(self):
        return self.__id
    
    def getNombreConductor(self):
        return self.__nombreConductor

    def getPatenteCamion(self):
        return self.__patenteCamion