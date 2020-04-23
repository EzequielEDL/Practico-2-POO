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

    def Mostrar(self):
        return print('{:02d}/{:02d}/{:4d} - {:02d}:{:02d}:{:02d}'.format(self.__dia, self.__mes, self.__anio, self.__hor, self.__min, self.__seg))

    def PonerEnHora(self, hor = 0, min = 0, seg = 0):
        if hor > 0: self.__hor = hor
        if min > 0: self.__min = min
        if seg > 0: self.__seg = seg

    def AdelantarHora(self, hor = 0, min = 0, seg = 0):
        seg = seg + self.__seg
        min = min + self.__min
        hor = hor + self.__hor

        #segundos
        if seg >= 0 :
            if seg >= 60 :
                self.__seg = seg - (int(seg/60)*60)
                min = min + int(seg/60)
            else : self.__seg = seg
        #minutos
        if min >= 0 :
            if min >= 60 :
                self.__min = min - (int(min/60)*60)
                hor = hor + int(min/60)
            else : self.__min = min
        #horas
        if hor >= 0 :
            if hor >= 24 :
                self.__hor = hor - (int(hor/24)*24)
                self.__dia = self.__dia + int(hor/24)
            else : self.__hor = hor

        #calendario
        diasMes = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
        
        #num = diasMes[12]+diasMes[1] + diasMes[2] + diasMes[3] + diasMes[4] + diasMes[5] + diasMes[6] + diasMes[7] + diasMes[8] + diasMes[9] + diasMes[10] + diasMes[11]
        #print('dias del anio: ',num)

        #anio bisiesto
        if (self.__anio % 4 == 0) and ((self.__anio % 100 != 0) or (self.__anio % 400 == 0)) : diasMes[2] = 29

        #dia/mes/anio
        while self.__dia > diasMes[self.__mes] : 
            self.__dia = self.__dia - diasMes[self.__mes]
            #print('mes',self.__mes,'','dias',diasMes[self.__mes],'','dias restantes',self.__dia)
            if self.__mes != 12 :
                self.__mes = self.__mes + 1
            else :
                self.__mes = 1
                self.__anio = self.__anio + 1
        
