#Ejercicio 8

from Conjunto import Conjunto
import os

def __dicShowConjuntos(dictConjuntos):
    print('\nConjuntos:\n')
    if len(dictConjuntos) == 0 :
        print('\n<< No hay conjuntos >>')
    else : 
        for k in range(len(dictConjuntos)) :
            print(' {}: {} = {}'.format(k+1, chr(k + 65), dictConjuntos[k]))

def option1(dictConjuntos):
    print('\nCrear Conjuntos')
    opc = input('\n¿Agregar conjunto nuevo? (Y/N): ')
    i = 0

    while opc == 'Y' or opc == 'y' :
        j = 0
        c = Conjunto()
        value = input('\nConjunto {} (0: End)\n {} Valor: '.format(chr(i + 65), j + 1))

        while int(value) != 0 :
            j = j + 1
            c.setValue(value)
            value = input(' {} Valor: '.format(j + 1))

        dictConjuntos.update({i: c})
        i = i + 1
        opc = input('\n¿Agregar conjunto nuevo? (Y/N): ')

    __dicShowConjuntos(dictConjuntos)
    
    input('\n\n<< press any key to continue >>')

def option2(dictConjuntos):
    __dicShowConjuntos(dictConjuntos)

    input('\n\n<< press any key to continue >>')

def option3(dictConjuntos):
    __dicShowConjuntos(dictConjuntos)

    c1 = int(input('\nElegir dos conjuntos: '))
    c2 = int(input(' %s y ' %c1))
    res = dictConjuntos[c1-1] + dictConjuntos[c2-1]
    c3 = Conjunto()
    for i in range(len(res)) : c3.setValue(res[i])

    print('\n {} U {} = {}'.format(chr(65 + int(c1) - 1), chr(65 + int(c2) - 1), c3))

    input('\n\n<< press any key to continue >>')

def option4(dictConjuntos):
    print('\nConjuntos:\n')
    if len(dictConjuntos) == 0 :
        print('\n<< No hay conjuntos >>')
    else : 
        for k in range(len(dictConjuntos)) :
            print(' {}: {} = {}'.format(k+1, chr(k + 65), dictConjuntos[k]))

    c1 = int(input('\nElegir dos conjuntos: '))
    c2 = int(input(' %s y ' %c1))
    res = dictConjuntos[c1-1] - dictConjuntos[c2-1]
    c3 = Conjunto()
    for i in range(len(res)) : c3.setValue(res[i])

    print('\n {} - {} = {}'.format(chr(65 + int(c1) - 1), chr(65 + int(c2) - 1), c3))
    
    input('\n\n<< press any key to continue >>')
    
def option5(dictConjuntos):
    __dicShowConjuntos(dictConjuntos)

    c1 = int(input('\nElegir dos conjuntos: '))
    c2 = int(input(' %s y ' %c1))
    res = dictConjuntos[c1-1] == dictConjuntos[c2-1]
    print('\n {} = {} = {}'.format(chr(65 + int(c1) - 1), chr(65 + int(c2) - 1), res))
    
    input('\n\n<< press any key to continue >>')

select = {1: option1, 2: option2, 3: option3, 4: option4, 5: option5}

def menu(opc, dictConjuntos):
    func = select.get(opc, lambda: print("Opcion Incorrecta"))
    func(dictConjuntos)

if __name__ == "__main__":
    dictConjuntos = {}
    flag = False

    while not flag:
        os.system('cls')
        print('\tOperaciones con conjuntos\n')
        print('1: Crear Conjuntos')
        print('2: Mostrar Conjuntos')
        print('3: Union de dos Conjuntos')
        print('4: Diferencia de dos Conjuntos')
        print('5: Igualdad de dos Conjuntos')
        print('6: Salir')
        opc = int(input('\nIngrese Opcion: '))
        if opc != 6 : menu(opc, dictConjuntos)
        flag = int(opc) == 6