import csv
from Camion import Camion

class ManejadorCamion:
    __nameFile = ''
    __listFile = []

    def __init__(self, nameFile = '0'):
        if nameFile != '0' :
            self.__nameFile = nameFile
            file = open(self.__nameFile)
            reader = csv.reader(file,delimiter = ',')

            for row in reader:
                cam = Camion( row[0], row[1], row[2], row[3], row[4])
                self.__listFile.append(cam)
                
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

    def getElementList(self, pos = 0):
        return self.__listFile[pos]