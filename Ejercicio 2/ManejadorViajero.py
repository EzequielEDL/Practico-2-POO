from ViajeroFrecuente import ViajeroFrecuente
import csv

class ManejadorViajero:
    __nameFile = '0'
    __listFile = []

    def __init__(self, nameFile = '0'):
        if nameFile != '0' :
            self.__nameFile = nameFile
            file = open(self.__nameFile)
            reader = csv.reader(file,delimiter = ',')

            for fila in reader:
                viajero = ViajeroFrecuente(fila[0], fila[1], fila[2], fila[3], fila[4])
                self.__listFile.append(viajero)
                #print(fila)
            file.close()
        else :
            print('\n<< Nombre invalido o archivo inexistente >>')
    
    def __str__(self):
        strQuit = ''
        for i in range(len(self.__listFile)) :
            strQuit = strQuit + '{}\n'.format(self.__listFile[i])

        return strQuit

    def getFileList(self):
        return self.__listFile

    def getElementList(self, pos):
        return self.__listFile[pos]
    