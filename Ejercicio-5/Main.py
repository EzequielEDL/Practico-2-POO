#Ejercicio 5

from ManejadorAlumno import ManejadorAlumno
import os

def option1(manejadorAlumno):
    anio = int(input('Ingresar año: '))
    division = input('Ingresar division: ')
    manejadorAlumno.getListPorce(anio, division)
    
    input('\n\n<< press any key to continue >>')

def option2(manejadorAlumno):
    maxInasistencias = input('-Ingrese cantidad: ')
    manejadorAlumno.getElementList().setMaxInasistencias(maxInasistencias)
    
    input('\n\n<< press any key to continue >>')

select = {1: option1, 2: option2}

def menu(opc, manejadorAlumno):
    func = select.get(opc, lambda: print("Opcion Incorrecta"))
    func(manejadorAlumno)

if __name__ == "__main__":

    manejadorAlumno = []
    manejadorAlumno = ManejadorAlumno('fileAlumno.csv')
    print(manejadorAlumno)
    input()
    flag = False

    while not flag:
        os.system('cls')
        print('\tMenu - Cantidad total de clases ({})'.format(manejadorAlumno.getElementList().cantClases))
        print('1:Mostrar porcentaje de inasistencias por alumno')
        print('2:Modificar Cantidad maxima de inasistencias ({})'.format(manejadorAlumno.getElementList().getMaxInasistencias()))
        print('3:Salir')
        opc = int(input('\nIngrese Opcion: '))
        if opc != 3 : menu(opc, manejadorAlumno)
        flag = int(opc) == 3
