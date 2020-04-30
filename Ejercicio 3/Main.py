#Ejercicio 3

from ManejadorCamion import ManejadorCamion
from Cosecha import Cosecha
import csv
import os

def showLista(listCamion, listCosecha):
    os.system('cls')
    print(' {:<4}{:<10}{:<8}{:<11}{:<9}\n'.format('ID', 'Nombre', 'Patente', 'Marca', 'Tara'))
    for i in range(len(listCamion)) :
        print(listCamion[i])
    
    print('\n Dia ', end = '-')

    for i in range(len(listCosecha[i])) : print('-{:>02}-'.format(i + 1), end = '-')
    print('\n')

    for i in range(len(listCosecha)) :
        print(' {:>02}: '.format(i+1), end = ' ')
        for j in range(len(listCosecha[i])) : 
            if j == len(listCosecha[i]) - 1: print('{:>4}'.format(listCosecha[i][j]))
            else: print('{:>4}'.format(listCosecha[i][j]), end = ' ')

    input('\n\n<< press any key to continue >>')    

def option1(listCamion, listCosecha):
    idCam = int(input('\nIngresar numero de identificador de un camion: '))
    acumKilos = 0
    if idCam < len(listCamion) and idCam > 0 :
        for i in range(len(listCosecha[idCam - 1])) :
            acumKilos = acumKilos + listCosecha[idCam - 1][i]
        
        print(' Cantidad total de Kilos Descargado durante {} dias: {}.kg'.format(len(listCosecha[idCam - 1]), acumKilos))
    else:
        print('Identificador Inexistente')

    input('\n\n<< press any key to continue >>')

def option2(listCamion, listCosecha):
    numDia = int(input('\nIngresar numero de un dia: '))
    if numDia < len(listCosecha) and numDia > 0 : 
        print('\n {:<9}{:<11}{}\n'.format('PATENTE', 'CONDUCTOR', 'CANTIDAD DE KILOS'))
        
        for i in range(len(listCosecha)):
            print(' {:<9}{:<11}{:>4}.kg'.format(listCamion[i].getPatenteCamion(), listCamion[i].getNombreConductor(), listCosecha[i][numDia - 1]))
    else:
        print('Dia inexistente')

    input('\n\n<< press any key to continue >>')

select = {1: option1, 2: option2}

def menu(opc, listCamion, listCosecha):
    func = select.get(opc, lambda: print("Opcion Incorrecta"))
    func(listCamion, listCosecha)

if __name__ == "__main__":
    os.system('cls')
    dias = int(input('Cantidad de Dias a evaluar: '))

    flag = False
    manejadorCamion = ManejadorCamion('fileCamion.csv')
    cosecha = Cosecha('fileCosecha.csv', manejadorCamion.getFileList(), len(manejadorCamion.getFileList()), dias )
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
        
