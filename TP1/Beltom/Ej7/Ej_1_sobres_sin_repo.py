# importacion de librerias
from random import *

# Estructuras del ejercicio
# para la primera retirada usamos este vector
listSobres = [2/5, 1]

# si sacamos un sobre Facil nos queda el siguiente resulatdo
listSobresPostFacil = [2/4, 1]

# si sacamos un sobre Complejo nos queda el siguiente resulatdo
listSobresPostComplex = [1/4, 1]


def converge(act, ant):
    print("mi valor absoluto es:", abs(ant - act))
    if(abs(ant - act) < 0.001):
        return True
    return False


def retirarPrimerSobre():
    n = random()
    if (n > 2/5):
        return 1
    else:
        return 0


def retirarSegundoSobre(sobreAnterior):
    n = random()
    if (sobreAnterior == 1):
        if(n <= 2/4):
            return 0
        else:
            return 1
    else:
        if(n <= 1/4):
            return 0
        else:
            return 1


def calcular_probabilidad():
    exitos = 0
    nTotal = 0
    probAnterior = -1
    probActual = 1
    cantMinima = 20
    while((converge(probActual, probAnterior) == False) or (nTotal < cantMinima)):
        x = retirarPrimerSobre()
        print("sobre 1", x)
        y = retirarSegundoSobre(x)
        print("sobre 2", y)
        if ((x == 1) and (y == 1)):
            exitos = exitos + 1
            print("la cantidad de exitos: ", exitos)
        nTotal = nTotal + 1
        probAnterior = probActual
        probActual = exitos/nTotal
        print("la cantidad de exitos sobre el total es: ", exitos, " /", nTotal)
    return probActual


resul = calcular_probabilidad()
print(resul)
