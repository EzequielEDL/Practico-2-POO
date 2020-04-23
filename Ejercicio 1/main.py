#Ejercicio 1

from Email import Email
import csv
import re

def modAccount(oneEmail):
    print('¿Modificar Contraseña? (Y/N)')
    if(input() == 'Y'):
        if(input('Ingrese Contraseña actual: ') == oneEmail.getClave()):
            oneEmail.setClave(input('Valido\nIngrese Nueva Contraseña: '))
        else:
            print('Invalido')

def readFile():
    d = input("Ingresar un Dominio: ")
    file = open('fileEmail.csv')
    reader = csv.reader(file,delimiter = ',')
    cont = 0
    i = 0

    for fila in reader:
        #print(d)
        print(fila[i])
        if(re.search(d, fila[i])) is not None:
            cont = cont + 1
        i+1

    if(cont != 0):
        print('La cantidad de direcciones de e-mail con el dominio ' + d + ' son: ' + str(cont))
    else:
        print('No hay ninguna direccion de e-mail con el dominio ' + d)

    file.close()

if __name__ == '__main__':
    n, e, c = input('Nombre: '), input('Cuenta de Correo: '), input('Contraseña: ')
    oneEmail = Email()
    oneEmail.crearCuenta(e,c)
    print('Estimado ' + n + ' te enviaremos tus mensajes a la dirección ' + oneEmail.retornaEmail() + '.')

    #Modificar atributo de objeto de Email
    modAccount(oneEmail)

    #Instancia de la clase Email
    otherEmail = Email('josetoro','hotmail','com','1234')
    print('Instancia de ' + otherEmail.retornaEmail())

    #Lectura de archivo con atributos de Email
    readFile()
