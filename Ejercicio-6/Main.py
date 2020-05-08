#Ejercicio 6

from FechaHora import FechaHora
import os

def option1():
    h = int(input("\nHora 1\nIngrese Hora: "))
    m = int(input("Ingrese Minutos: "))
    s = int(input("Ingrese Segundos: "))
    f1 = FechaHora()
    f1.ponerEnHora(h, m, s)

    h = int(input("\nHora 2\nIngrese Hora: "))
    m = int(input("Ingrese Minutos: "))
    s = int(input("Ingrese Segundos: "))
    f2 = FechaHora()
    f2.ponerEnHora(h, m, s)

    print('\nHora 1: ', end = '   ')
    f1.mostrar()
    print('Hora 2: ', end = '   ')
    f2.mostrar()
    f3 = f1 + f2
    print("\nResultado: ", end = '')
    f3.mostrar()
    input()

def option2():
    h = int(input("\nHora 1\nIngrese Hora: "))
    m = int(input("Ingrese Minutos: "))
    s = int(input("Ingrese Segundos: "))
    f1 = FechaHora()
    f1.ponerEnHora(h, m, s)

    h = int(input("\nHora 2\nIngrese Hora: "))
    m = int(input("Ingrese Minutos: "))
    s = int(input("Ingrese Segundos: "))
    f2 = FechaHora()
    f2.ponerEnHora(h, m, s)

    print('\nHora 1: ', end = '   ')
    f1.mostrar()
    print('Hora 2: ', end = '   ')
    f2.mostrar()
    f3 = f1 - f2
    print("\nResultado: ", end = '')
    f3.mostrar()
    input()

def option3():
    h = int(input("\nHora 1\nIngrese Hora: "))
    m = int(input("Ingrese Minutos: "))
    s = int(input("Ingrese Segundos: "))
    f1 = FechaHora()
    f1.ponerEnHora(h, m, s)

    h = int(input("\nHora 2\nIngrese Hora: "))
    m = int(input("Ingrese Minutos: "))
    s = int(input("Ingrese Segundos: "))
    f2 = FechaHora()
    f2.ponerEnHora(h, m, s)

    print('\nHora 1: ', end = '   ')
    f1.mostrar()
    print('Hora 2: ', end = '   ')
    f2.mostrar()
    f3 = f1 > f2
    print("\nResultado f1 > f2 : {}".format(f3))
    input()

select = {1: option1, 2: option2, 3: option3}

def menu(opc):
    func = select.get(opc, lambda: print("Opcion Incorrecta"))
    func()

if __name__ == "__main__":
    flag = False

    while not flag:
        os.system('cls')
        print('1:Sumar hora')
        print('2:Restar hora')
        print('3:Hora mayor')
        print('4:Salir')
        opc = int(input('\nIngrese Opcion: '))
        if opc != 4 : menu(opc)
        flag = int(opc) == 4
