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
        resValues = []

        for i in self.__values + addConjunto.getValues():
            if i not in resValues:
                resValues.append(i)
    
        return resValues

    def __sub__(self, subConjunto):        
        resValues = []

        for i in self.__values:
            if i not in subConjunto.getValues():
                resValues.append(i)
    
        return resValues

    def __eq__(self, eqConjunto):
        resCoutValues = 0

        if len(self.__values) == len(eqConjunto.getValues()) :
            for i in self.__values:
                if i in eqConjunto.getValues():
                    resCoutValues = resCoutValues + 1

        return resCoutValues == len(self.__values)

    def addValue(self, value):
        if str(value).isdecimal() :
            self.__values.append(int(value))
        else :
            print('Error en la verificacion de tipos de datos')        

    def getValues(self):
        return self.__values