from asyncore import loop
from random import *

listaElementos = ["hola", 3, 5, 7, 2]
probAcumulada = [1/6, 2/6, 3/6, 4/6, 5/6, 6/6]
n = random()


def converge(act, ant):
    if(abs(ant - act) < 00000000000.1):
        return True
    return False


def calc_prob_sum_6():
    exitos = 0
    nTotal = 0
    probAnterior = -1
    probActual = 1
    while(not converge(probActual, probAnterior)):
        x = arrojarDado()
        print(x)
        y = arrojarDado()
        print(y)
        if (x+y == 6):
            exitos+1
        nTotal = nTotal + 1
        print("el n total es:", nTotal)
        probAnterior = probActual
        print("la prob anterior", probAnterior)
        probActual = exitos/nTotal
        print("la prob actual", probActual)
    return probActual


def arrojarDado():
    for i in range(6):
        if n < probAcumulada[i]:
            return i


resul = calc_prob_sum_6()
print(resul)
