import csv

class Cosecha:
    __listFile = []

    def __init__ (self, nameFile = '0', listCamion = []):
        if nameFile != '0' and type(self.__listFile) == type(listCamion):
            self.__nameFile = nameFile
            file = open(nameFile)
            reader = csv.reader(file, delimiter = ',')

            for row in reader :
                i = 0
                while i < len(listCamion) - 1 and listCamion[i].getId() != int(row[0]) :
                    i = i + 1
                kilos = int(row[2]) - listCamion[i].getTara()
                self.__listFile.append([int(row[0]), int(row[1]), kilos])

            file.close()
        else :
            print('\n<< Nombre invalido o archivo inexistente >>')
        
    def getFileList(self):
        return self.__listFile

    def getElementList(self, pos = 0):
        return self.__listFile[pos]
