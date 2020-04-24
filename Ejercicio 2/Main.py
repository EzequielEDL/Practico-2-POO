#Ejercicio 2

from ViajeroFrecuente import ViajeroFrecuente
import csv
import os

def option1(lista, num):
    print('\tCantidad total de Millas: ' + str(lista[num-1].cantidadTotaldeMillas()))
    
    input('\n\n<< press any key to continue >>')

def option2(lista, num):
    mil = input('\tCantidad de millas: ')
    lista[num-1].acumularMillas(mil)
    
    input('\n\n<< press any key to continue >>')

def option3(lista, num):
    mil = input('\tCantidad de millas: ')
    lista[num-1].canjearMillas(mil)
    
    input('\n\n<< press any key to continue >>')

select = {1: option1, 2: option2, 3: option3}

def menu(opc, lista, num):
    func = select.get(opc, lambda: print("Opcion Incorrecta"))
    func(lista, num)

def loadFile(lista):
    file = open('fileViajero.csv')
    reader = csv.reader(file,delimiter = ',')

    for fila in reader:
        viajero = ViajeroFrecuente(fila[0], fila[1], fila[2], fila[3], fila[4])
        lista.append(viajero)
        #print(fila)
    file.close()

def listaMemoria(lista):
    print('\tAlmacenamiento en Memoria')
    for i in range(0,len(lista)):
        print(' {}'.format(lista[i]))

if __name__ == '__main__':
    lista = []
    loadFile(lista)    
    flag = False

    os.system('cls')
    listaMemoria(lista)
    input('\n\n<< press any key to continue >>')

    while not flag:
        os.system('cls')
        print('1:Consultar cantidad de Millas')
        print('2:Acumular Millas')
        print('3:Canjear Millas')    
        print('4:Salir')
        opc = int(input('\nIngrese Opcion: '))
        if opc != 4 :
            num = int(input("Numero de Viajero frecuente: "))
            if((num <= len(lista)) and (num > 0)):
                menu(opc, lista, num)
        else : flag = True
            
    


