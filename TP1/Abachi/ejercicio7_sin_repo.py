import random as randomLibrary
from random import random


def Sacar_primer_sobre():
    prob_acum = [2/5, 1]
    p = random()
    for i in range(len(prob_acum)):
        if p < prob_acum[i]:
            return i


def Sacar_segundo_sobre(primer_sobre):
    prob_acum = [[1/2, 3/4], [1, 1]]
    p = random()
    for i in range(len(prob_acum)):
        if p < prob_acum[i][primer_sobre]:
            return i


def converge(ant, act):
    if (abs(ant - act) < 0.000001):
        return True
    return False


def Sacar_al_menos_1_facil():
    exitos = 0
    n = 0
    prob_ant = -1
    prob_act = 1
    minimo = 0
    while (not converge(prob_ant, prob_act) or minimo < 15):
        x = Sacar_primer_sobre()
        y = Sacar_segundo_sobre(x)
        if(x+y == 6):
            exitos = exitos+1
        n = n+1
        prob_ant = prob_act
        prob_act = exitos / n
        minimo = minimo+1
    return prob_act


prueba = Sacar_al_menos_1_facil()
print(prueba)
