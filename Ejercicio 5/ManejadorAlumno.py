import csv
from Alumno import Alumno

class ManejadorAlumno:
    __nameFile = ''
    __listFile = []

    def __init__(self, nameFile = '0'):
        if nameFile != '0' :
            self.__nameFile = nameFile
            file = open('fileAlumno.csv')
            reader = csv.reader(file, delimiter = ',')

            for fila in reader:
                oneAlumno = Alumno (fila[0], fila[1], fila[2], fila[3])
                self.__listFile.append(oneAlumno)
                #print('Added {}'.format(str(fila[0])))
            file.close()
        else :
            print('\n<< Nombre invalido o archivo inexistente >>')

    def __str__(self):
        strQuit = ''
        for i in range(len(self.__listFile)) :
            strQuit = strQuit + '{}\n'.format(self.__listFile[i])

        return strQuit

    def getListPorce(self, anio, division):
        i = 0
        while i < len(self.__listFile):
            if self.__listFile[i].getAnio() == anio and self.__listFile[i].getDivision() == division :
                if self.__listFile[i].getInasistencias() > Alumno.maxInasistencias :
                    print('\t{:<40} {:<5}%'.format(self.__listFile[i].getNombre(), (self.__listFile[i].getInasistencias()/Alumno.cantClases)*100))
            i = i + 1
    
    def getFileList(self):
        return self.__listFile

    def getElementList(self, pos = 0):
        return self.__listFile[pos]
        