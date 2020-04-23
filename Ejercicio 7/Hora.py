class Hora:
    __hor = 0
    __min = 0
    __seg = 0

    def __init__(self, hor = 0, min = 0, seg = 0):
        self.__hor = int(hor)
        self.__min = int(min)
        self.__seg = int(seg)

    def mostrar(self):
        return print('{:02d}:{:02d}:{:02d}'.format(self.__hor, self.__min, self.__seg))

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

    def getHor(self):
        return self.__hor
    
    def getMin(self):
        return self.__min

    def getSeg(self):
        return self.__seg