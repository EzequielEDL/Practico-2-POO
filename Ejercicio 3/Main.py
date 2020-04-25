#Ejercicio 3

from Camion import Camion
from Cosecha import Cosecha
import csv
import os

def showLista(listaCamion, listaCosecha):
    os.system('cls')
    print(' {:<4}{:<10}{:<8}{:<11}{:<9}{:<4}{}\n'.format('ID', 'Nombre', 'Patente', 'Marca', 'Tara', 'Dia', 'Kilos'))
    for i in range(len(listaCamion)) :
        print(listaCamion[i],' {:>02}  {:>2}.kg'.format(listaCosecha[i][1], listaCosecha[i][2]))
    
    input('\n\n<< press any key to continue >>')    

def loadCamion():
    file = open('fileCamion.csv')
    reader = csv.reader(file,delimiter = ',')
    listaAux = []

    for row in reader:
        cam = Camion( row[0], row[1], row[2], row[3], row[4])
        listaAux.append(cam)

    file.close()
    return listaAux

def loadCosecha(listaCamion):
    file = open('fileCosecha.csv')
    reader = csv.reader(file, delimiter = ',')
    listaAux = []

    for row in reader :
        i = 0
        while i < len(listaCamion) - 1 and listaCamion[i].getId() != int(row[0]) : i = i + 1
        kilos = int(row[2]) - listaCamion[i].getTara()
        listaAux.append([int(row[0]), int(row[1]), kilos])

    cos = Cosecha(listaAux)
    file.close()
    return cos.getKilos()

def option1(listaCamion, listaCosecha):
    idCam = int(input('\nIngresar numero de identificador de un camion: '))
    i = 0
    j = i

    while i < len(listaCamion) - 1 and listaCamion[i].getId() != idCam :
        i = i + 1
    
    while j < len(listaCosecha) - 1 and listaCosecha[j][0] != idCam :
        j = j + 1

    print('\n Diferencia: {}.kg - {}.kg'.format(listaCosecha[j][2], listaCamion[i].getTara()))

    kilosDescargado = listaCosecha[j][2] - listaCamion[i].getTara()
    print(' Cantidad total de Kilos Descargado: {}.kg'.format(kilosDescargado))

    input('\n\n<< press any key to continue >>')

def option2(listaCamion, listaCosecha):
    numDia = int(input('\nIngresar numero de un dia: '))
    print('\n {:<9}{:<11}{}\n'.format('PATENTE', 'CONDUCTOR', 'CANTIDAD DE KILOS'))
    
    for i in range(len(listaCosecha)):
        if listaCosecha[i][1] == numDia :
            j  = 0
            while j < len(listaCamion) - 1 and listaCamion[j].getId() != listaCosecha[i][0] :
                j = j + 1
        
            print(' {:<9}{:<11}{}'.format(listaCamion[j].getPatenteCamion(), listaCamion[j].getNombreConductor(), listaCosecha[i][2]))

    input('\n\n<< press any key to continue >>')

select = {1: option1, 2: option2}

def menu(opc, listaCamion, listaCosecha):
    func = select.get(opc, lambda: print("Opcion Incorrecta"))
    func(listaCamion, listaCosecha)

if __name__ == "__main__":
    flag = False
    listaCamion = loadCamion()
    listaCosecha = loadCosecha(listaCamion)
    showLista(listaCamion, listaCosecha)

    while not flag:
        os.system('cls')
        print('\tCosecha de Camiones\n')
        print('1: Mostrar kilos cargados de un camion')
        print('2: Mostrar listado de un dia')
        print('3: Salir')
        opc = int(input('\nIngrese Opcion: '))
        if opc != 3 : menu(opc, listaCamion, listaCosecha)
        flag = int(opc) == 3
    