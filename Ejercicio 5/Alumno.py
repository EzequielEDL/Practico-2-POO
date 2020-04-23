class Alumno:
    __nombre = ''
    __anio = 0
    __division = ''
    __inasistencias = 0
    maxInasistencias = 5
    cantClases = 25

    def __init__(self, nombre = '', anio = 0, division = '', inasistencias = 0):
        if self.__testing(nombre, anio, division, inasistencias) : 
            self.__nombre = str(nombre)
            self.__anio = int(anio)
            self.__division = str(division)
            self.__inasistencias = int(inasistencias)
        else :
            print('Error al validar tipos de datos')

    def __testing(self, nombre, anio, division, inasistencias):
        if nombre.title() and anio.isdecimal() and division.isalpha and inasistencias.isdecimal() :
            return True
        else :
            return False

    def getNombre(self):
        return self.__nombre

    def getAnio(self):
        return self.__anio

    def getDivision(self):
        return self.__division

    def getInasistencias(self):
        return self.__inasistencias
        
    @classmethod
    def setMaxInasistencias(cls, xMaxInasistencias):
        if xMaxInasistencias.isdecimal() :
            maxInasistencias = int(xMaxInasistencias)
            cls.maxInasistencias = maxInasistencias
        else :
            print('Error al validar tipos de datos')

    @classmethod
    def getMaxInasistencias(cls):
        return cls.maxInasistencias
