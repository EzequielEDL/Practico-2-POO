class Email:
    __idCuenta = ''
    __dominio = ''
    __tipoDominio = ''
    __clave = ''

    def __init__(self, idCuenta = '', dominio = '', tipoDominio = '', clave = ''):
        if self.__testing(idCuenta, dominio, tipoDominio, clave) :
            self.__idCuenta = str(idCuenta)
            self.__dominio = str(dominio)
            self.__tipoDominio = str(tipoDominio)
            self.__clave = str(clave)
        else :
            print('Error al validar tipos de datos')

    def __testing(self, idCuenta, dominio, tipoDominio, clave):
        if idCuenta.isidentifier() and dominio.isalpha() and tipoDominio.isalpha and clave.isalnum() :
            return True
        else :
            return False

    def retornaEmail(self):
        return self.__idCuenta + '@' + self.__dominio + '.' + self.__tipoDominio

    def getDominio(self):
        return self.__dominio

    def crearCuenta(self, email, clave):
        s2 = email.split('@')
        s3 = s2[1].split('.')

        if s2[0].isidentifier() and s3[0].isalpha() and s3[1].isalpha and clave.isalnum() :
            self.__idCuenta = str(s2[0])
            self.__dominio = str(s3[0])
            self.__tipoDominio = str(s3[1])
            self.__clave = str(clave)
        else :
            print('Error al validar tipos de datos')

    def getClave(self):
        return self.__clave

    def setClave(self, clave):
        if clave.isalnum() :
            self.__clave = clave
        else :
            print('Error al validar tipos de datos')