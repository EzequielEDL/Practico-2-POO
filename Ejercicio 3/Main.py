#Ejercicio 3

from ManejadorCamion import ManejadorCamion
from Cosecha import Cosecha
import csv
import os

def showLista(listCamion, listCosecha):
    os.system('cls')
    print(' {:<4}{:<10}{:<8}{:<11}{:<9}{:<4}{}\n'.format('ID', 'Nombre', 'Patente', 'Marca', 'Tara', 'Dia', 'Kilos'))
    for i in range(len(listCamion)) :
        print(listCamion[i],' {:>02}  {:>2}.kg'.format(listCosecha[i][1], listCosecha[i][2]))
    
    input('\n\n<< press any key to continue >>')    

def option1(listCamion, listCosecha):
    idCam = int(input('\nIngresar numero de identificador de un camion: '))
    i = 0
    j = i

    while i < len(listCamion) - 1 and listCamion[i].getId() != idCam :
        i = i + 1
    
    while j < len(listCosecha) - 1 and listCosecha[j][0] != idCam :
        j = j + 1

    print('\n Diferencia: {}.kg - {}.kg'.format(listCosecha[j][2] + listCamion[i].getTara(), listCamion[i].getTara()))
    print(' Cantidad total de Kilos Descargado: {}.kg'.format(listCosecha[j][2]))

    input('\n\n<< press any key to continue >>')

def option2(listCamion, listCosecha):
    numDia = int(input('\nIngresar numero de un dia: '))
    print('\n {:<9}{:<11}{}\n'.format('PATENTE', 'CONDUCTOR', 'CANTIDAD DE KILOS'))
    
    for i in range(len(listCosecha)):
        if listCosecha[i][1] == numDia :
            j  = 0
            while j < len(listCamion) - 1 and listCamion[j].getId() != listCosecha[i][0] :
                j = j + 1
        
            print(' {:<9}{:<11}{}'.format(listCamion[j].getPatenteCamion(), listCamion[j].getNombreConductor(), listCosecha[i][2]))

    input('\n\n<< press any key to continue >>')

select = {1: option1, 2: option2}

def menu(opc, listCamion, listCosecha):
    func = select.get(opc, lambda: print("Opcion Incorrecta"))
    func(listCamion, listCosecha)

if __name__ == "__main__":
    flag = False
    manejadorCamion = ManejadorCamion('fileCamion.csv')
    cosecha = Cosecha('fileCosecha.csv', manejadorCamion.getFileList())
    showLista(manejadorCamion.getFileList(), cosecha.getFileList())

    while not flag:
        os.system('cls')
        print('\tCosecha de Camiones\n')
        print('1: Mostrar kilos descargados de un camion')
        print('2: Mostrar listado de un dia')
        print('3: Salir')
        opc = int(input('\nIngrese Opcion: '))
        if opc != 3 : menu(opc, manejadorCamion.getFileList(), cosecha.getFileList())
        flag = int(opc) == 3
    
