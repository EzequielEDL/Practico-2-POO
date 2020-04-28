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

def loadFile(listaEmail):
    file = open('fileEmail.csv')
    reader = csv.reader(file,delimiter = ',')
    i = 0

    for fila in reader:
        #print(d)
        listaEmail.append(fila[i])
        i+1

    file.close()

def findDom(listaEmail):
    d = input("Ingresar un Dominio: ")
    cont = 0

    for i in range(len(listaEmail)):
        if(re.search(d, listaEmail[i])) is not None:
            cont = cont + 1
        
    if(cont != 0):
        print('La cantidad de direcciones de e-mail con el dominio ' + d + ' son: ' + str(cont))
    else:
        print('No hay ninguna direccion de e-mail con el dominio ' + d)



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
    listaEmail = []
    loadFile(listaEmail)
    findDom(listaEmail)
