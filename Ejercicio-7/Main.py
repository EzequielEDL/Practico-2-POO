#Ejercicio 7

from FechaHora import FechaHora
from Hora import Hora
import os

if __name__ == '__main__':

    d = int(input("Ingrese Dia: "))
    mes = int(input("Ingrese Mes: "))
    a = int(input("Ingrese Año: "))
    h = int(input("Ingrese Hora: "))
    m = int(input("Ingrese Minutos: "))
    s = int(input("Ingrese Segundos: "))
    f = FechaHora(d,mes,a,h, m, s)
    f.mostrar()
    input()

    h1 = int(input("Ingrese Hora: "))
    m1 = int(input("Ingrese Minutos: "))
    s1 = int(input("Ingrese Segundos: "))
    r = Hora(h1, m1, s1)
    r.mostrar()
    input()

    f2 = f + r
    f2.mostrar()
    input()

    f3 = r + f
    f3.mostrar()
    input()

    f4 = f3 - 1 # Al restar un número entero a un objeto FechaHora se debe restar la cantidad de días indicada por el número entero
    f4.mostrar()
    input()
    
    f4 = 1 + f2 # suma un día a un objeto FechaHora
    f4.mostrar()
    input()