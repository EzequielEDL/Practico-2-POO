#Ejercicio 5

import csv
from Alumno import Alumno
import os

def option1(lista):
    anio = int(input('Ingresar año: '))
    division = input('Ingresar division: ')
    
    print('\t{:<40} {:<5}'.format('Alumno','Porcentaje'))
    for i in range(0, len(lista)):

        if lista[i].getAnio() == anio and lista[i].getDivision() == division :

            if lista[i].getInasistencias() > Alumno.maxInasistencias :
                print('\t{:<40} {:<5}%'.format(lista[i].getNombre(), (lista[i].getInasistencias()/Alumno.cantClases)*100))

    input()

def option2(lista):
    maxInasistencias = input('-Ingrese cantidad: ')
    Alumno.setMaxInasistencias(maxInasistencias)
    input()

select = {1: option1, 2: option2}

def menu(opc, lista):
    func = select.get(opc, lambda: print("Opcion Incorrecta"))
    func(lista)

def readFile(lista):
    file = open('fileAlumno.csv')
    reader = csv.reader(file, delimiter = ',')

    for fila in reader:
        oneAlumno = Alumno (fila[0], fila[1], fila[2], fila[3])
        lista.append(oneAlumno)
        print('Added {}'.format(str(fila[0])))
        
    file.close()
    input()

if __name__ == "__main__":

    lista = []
    readFile(lista)
    flag = False

    while not flag:
        os.system('cls')
        print('\tMenu - Cantidad total de clases ({})'.format(Alumno.cantClases))
        print('1:Mostrar porcentaje de inasistencias por alumno')
        print('2:Modificar Cantidad maxima de inasistencias ({})'.format(Alumno.getMaxInasistencias()))
        print('3:Salir')
        opc = int(input('\nIngrese Opcion: '))
        if opc != 3 : menu(opc, lista)
        flag = int(opc) == 3