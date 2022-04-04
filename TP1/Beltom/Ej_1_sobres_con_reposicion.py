from random import *
listSobres = [2/5, 1]


def converge(act, ant):
    print("mi valor absoluto es:", abs(ant - act))
    if(abs(ant - act) < 0.001):
        return True
    return False


def calcular_probabilidad():
    exitos = 0
    nTotal = 0
    probAnterior = -1
    probActual = 1
    cantMinima = 10
    while((converge(probActual, probAnterior) == False) or (nTotal < cantMinima)):
        x = retirarSobre()
        print("sobre 1", x)
        y = retirarSobre()
        print("sobre 2", y)
        if ((x == 1) and (y == 1)):
            exitos = exitos + 1
            print("la cantidad de exitos: ", exitos)
        nTotal = nTotal + 1
        probAnterior = probActual
        probActual = exitos/nTotal
        print("la cantidad de exitos sobre el total es: ", exitos, " /", nTotal)
    return probActual


def retirarSobre():
    n = random()
    if (n > 2/5):
        return 1
    else:
        return 0


resul = calcular_probabilidad()
print(resul)
