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

    def __add__ (self, addFechaHora):
        resul = self.__verificationTime(self.__seg + addFechaHora.getSeg(), self.__min + addFechaHora.getMin(), self.__hor + addFechaHora.getHor())
        return FechaHora(self.__dia, self.__mes, self.__anio, resul[2], resul[1], resul[0])

    def __sub__(self, addFechaHora):
        sub1 = self.__seg - addFechaHora.getSeg()
        sub2 = self.__min - addFechaHora.getMin()
        sub3 = self.__hor - addFechaHora.getHor()
        mulSub1 = int(((sub1 - 60) * -1) / 60)
        mulSub2 = int(((sub2 - 60) * -1) / 60)
        mulSub3 = int(((sub3 - 24) * -1) / 24)

        if sub1 < 0 : sub1 = sub1 + 60 * mulSub1                        #SEG
        if sub1 * mulSub1 + 59 >= 60 : sub2 = sub2 - mulSub1            #MIN
        if sub2 < 0 : sub2 = sub2 + 60 * mulSub2                        #MIN
        if sub2 * mulSub2 + 59 >= 60 : sub3 = sub3 - mulSub2            #HOR
        if sub3 < 0 : sub3 = sub3 + 24 * mulSub3                        #HOR

        resul = self.__verificationTime(sub1, sub2, sub3)
        return FechaHora(self.__dia, self.__mes, self.__anio, resul[2], resul[1], resul[0])

    def __gt__(self, addFechaHora):
        if self.__hor > addFechaHora.getHor() :
            return FechaHora(self.__dia, self.__mes, self.__anio, self.__hor, self.__min, self.__seg)
        else :
            return FechaHora(addFechaHora.getDia(), addFechaHora.getMes(), addFechaHora.getAnio(), addFechaHora.getHor(), addFechaHora.getMin(), addFechaHora.getSeg())

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
