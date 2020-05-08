class Conjunto:
    __values = []

    def __init__(self, coutValues = 0):
        if str(coutValues).isdecimal() :
            self.__values = [0 for i in range(int(coutValues))]
            
    def __str__(self):
        quit = str(self.__values[0])

        for i in range(1, len(self.__values)):
            quit = quit + ', ' + str(self.__values[i]) 

        return '{}{}{}'.format('{', quit, '}')

    def __add__(self, addConjunto):
        if str(type(addConjunto)) == 'Conjunto.Conjunto' :    
            resValues = []

            for i in self.__values + addConjunto.getValue():
                if i not in resValues:
                    resValues.append(i)
        
            return resValues
        else :
            print('\n<< Falta de conjunto o conjunto invalido >>')

    def __sub__(self, subConjunto):
        if str(type(subConjunto)) == 'Conjunto.Conjunto' :            
            resValues = []

            for i in self.__values:
                if i not in subConjunto.getValue():
                    resValues.append(i)
        
            return resValues
        else :
            print('\n<< Falta de conjunto o conjunto invalido >>')

    def __eq__(self, eqConjunto):
        if str(type(eqConjunto)) == 'Conjunto.Conjunto' :
            resCoutValues = 0

            if len(self.__values) == len(eqConjunto.getValue()) :
                for i in self.__values:
                    if i in eqConjunto.getValue():
                        resCoutValues = resCoutValues + 1

            return resCoutValues == len(self.__values)
        else :
            print('\n<< Falta de conjunto o conjunto invalido >>')

    def setValue(self, value):
        if str(value).isdecimal() :
            self.__values.append(int(value))
        else :
            print('<< Error en la verificacion de tipos de datos >>')        

    def getValue(self):
        return self.__values