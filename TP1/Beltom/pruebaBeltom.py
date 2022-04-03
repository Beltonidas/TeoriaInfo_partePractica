from asyncore import loop
from random import *

listaElementos = ["hola", 3, 5, 7, 2]
probAcumulada = [1/6, 2/6, 3/6, 4/6, 5/6, 6/6]
n = random()


def converge(act, ant):
    if(abs(ant - act) < 0.00000000001):
        return True
    return False


def calc_prob_sum_6():
    exitos = 0
    nTotal = 0
    probAnterior = -1
    probActual = 1
    while(converge(probActual, probAnterior) == False):
        x = arrojarDado()
        print("dado1", x)
        y = arrojarDado()
        print("dado2", y)
        if (x+y == 6):
            exitos = exitos +1
            print ("la cantidad de exitos: ", exitos)
        nTotal = nTotal + 1
        print ("la cantidad de tiradas: ", nTotal)
        print("el n total es:", nTotal)
        probAnterior = probActual
        print("la prob anterior", probAnterior)
        aux = (exitos/nTotal)
        print ("mi aux es..", aux)
        probActual = exitos/nTotal
        print("la prob actual", probActual)
    return probActual

def pruebagit():
    a = 3
    print (a)


def arrojarDado():
    for i in range(6):
        if n < probAcumulada[i]:
            return i
        
resul = calc_prob_sum_6()
print(resul)
