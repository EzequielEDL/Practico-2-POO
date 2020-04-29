class FechaHora:
    __dia = 0
    __mes = 0
    __anio = 0
    __hor = 0
    __min = 0
    __seg = 0

    def __init__(self, dia = 1, mes = 1, anio = 2020, hor = 0, min = 0, seg = 0):
        self.__dia = int(dia)
        self.__mes = int(mes)
        self.__anio = int(anio)
        self.__hor = int(hor)
        self.__min = int(min)
        self.__seg = int(seg)

    def __verificationTime(self, seg, min, hor):
        totalMin = 0
        totalSeg = 0
        totalHor = 0

        if seg >= 60 :
            min = min + int(seg / 60) 
            totalSeg = seg - (int(seg / 60) * 60)
        else : totalSeg = seg

        if min >= 60 :
            hor = hor + int(min / 60)
            totalMin = min - (int(min / 60) * 60)
        else : totalMin = min

        if hor >= 24 :
            totalHor = hor - (int(hor / 24) * 24)
        else : totalHor = hor

        time = [totalSeg, totalMin, totalHor]
        return time
    
    def __verificationDate(self, dia):
        #calendario
        diasMes = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
        #anio bisiesto
        if (self.__anio % 4 == 0) and ((self.__anio % 100 != 0) or (self.__anio % 400 == 0)) : diasMes[2] = 29
        mes = self.__mes
        anio = self.__anio

        #dia/mes/anio

        if dia == 0 :
            mes = mes - 1
            if mes == 0 :
                mes = 12
                anio = anio -1
            dia = diasMes[mes]
        else : 
            while dia > diasMes[mes] : 
                dia = dia - diasMes[mes]
                #print('mes',self.__mes,'','dias',diasMes[self.__mes],'','dias restantes',self.__dia)
                if mes != 12 :
                    mes = mes + 1
                else :
                    mes = 1
                    anio = anio + 1

        date = [dia, mes, anio]
        return date

    def __add__ (self, argument):
        resul = self.__verificationTime(self.__seg + argument.getSeg(), self.__min + argument.getMin(), self.__hor + argument.getHor())
        return FechaHora(self.__dia, self.__mes, self.__anio, resul[2], resul[1], resul[0])

    def __radd__ (self, argument):
        if str(argument).isdecimal() :
            resul = self.__verificationDate(self.__dia + argument)
            return FechaHora(resul[0], resul[1], resul[2], self.__hor, self.__min, self.__seg)
        else :
            resul = self.__verificationTime(self.__seg + argument.getSeg(), self.__min + argument.getMin(), self.__hor + argument.getHor())
            return FechaHora(self.__dia, self.__mes, self.__anio, resul[2], resul[1], resul[0])
    
    def __sub__(self, argument):
        resul = self.__verificationDate(self.__dia - argument)
        return FechaHora(resul[0], resul[1], resul[2], self.__hor, self.__min, self.__seg)

    def mostrar(self):
        return print('{:02d}/{:02d}/{:4d} - {:02d}:{:02d}:{:02d}'.format(self.__dia, self.__mes, self.__anio, self.__hor, self.__min, self.__seg))

    def ponerEnHora(self, hor = 0, min = 0, seg = 0):
        if hor > 0: self.__hor = hor
        if min > 0: self.__min = min
        if seg > 0: self.__seg = seg

    def getHor(self):
        return self.__hor
    
    def getMin(self):
        return self.__min

    def getSeg(self):
        return self.__seg
    
    def getDia(self):
        return self.__dia

    def getMes(self):
        return self.__mes
    
    def getAnio(self):
        return self.__anio
