#Ejercicio 2

from ManejadorViajero import ManejadorViajero
import os

def option1(manejadorViajero, num):
    print('\tCantidad total de Millas: {}'.format(manejadorViajero.getElementList(num-1).cantidadTotaldeMillas()))
    
    input('\n\n<< press any key to continue >>')

def option2(manejadorViajero, num):
    mil = input('\tCantidad de millas: ')
    manejadorViajero.getElementList(num-1).acumularMillas(mil)
    
    input('\n\n<< press any key to continue >>')

def option3(manejadorViajero, num):
    mil = input('\tCantidad de millas: ')
    manejadorViajero.getElementList(num-1).canjearMillas(mil)
    
    input('\n\n<< press any key to continue >>')

select = {1: option1, 2: option2, 3: option3}

def menu(opc, manejadorViajero, num):
    func = select.get(opc, lambda: print("Opcion Incorrecta"))
    func(manejadorViajero, num)

if __name__ == '__main__':

    flag = False
    manejadorViajero = ManejadorViajero('fileViajero.csv')
    print(manejadorViajero)
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
            if((num <= len(manejadorViajero.getFileList())) and (num > 0)):
                menu(opc, manejadorViajero, num)
        else : flag = True
            
    


