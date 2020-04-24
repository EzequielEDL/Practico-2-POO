class ViajeroFrecuente: 
    __numViajero = 0
    __dni = 0
    __nombre = ''
    __apellido = ''
    __millasAcum = 0
    def __init__(self, numViajero, dni, nombre, apellido, millasAcum):
        if self.__testing(numViajero, dni, nombre, apellido, millasAcum) :
            self.__numViajero = int(numViajero)
            self.__dni = int(dni)
            self.__nombre = str(nombre)
            self.__apellido = str(apellido)
            self.__millasAcum = int(millasAcum)
        else :
            print('Error al validar tipos de datos')

    def __testing(self, numViajero, dni, nombre, apellido, millasAcum):
        if numViajero.isdecimal() and dni.isdecimal() and nombre.isalpha() and apellido.isalpha() and millasAcum.isdecimal() :
            return True
        else :
            return False

    def cantidadTotaldeMillas(self):
        return self.__millasAcum

    def acumularMillas(self, xMillas):
        if xMillas.isdecimal() :
            millas = int(xMillas)
            if(millas > 0):
                self.__millasAcum = self.__millasAcum + millas
                print('\tMillas Resultado: '+str(self.__millasAcum))
        else :
            print('Error al validar tipos de datos')

    def canjearMillas(self, xMillas):
        if xMillas.isdecimal() :
            millas = int(xMillas)
            if(self.__millasAcum > 0):
                self.__millasAcum = self.__millasAcum - millas
                print('\tMillas Resultado: '+str(self.__millasAcum))
        else :
            print('Error al validar tipos de datos')
