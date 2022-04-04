import random as randomLibrary
from random import *
n = random()
print(n)


def Sacar_primer_sobre():
    prob_acum = [2/5, 1]
    p = random()
    for i in range(len(prob_acum)):
        if p < prob_acum[i]:
            return i


def Sacar_segundo_sobre(primer_sobre):
    prob_acum = [1/2, 3/4], [1, 1]
    p = random()
    for i in range(0, 1):
        if p < prob_acum[i][primer_sobre]:
            return i


def converge(ant, act):
    if (abs(ant - act) < 0.0001):
        return True
    return False


def Sacar_al_menos_1_facil():
    exitos = 0
    N = 0
    prob_ant = -1
    prob_act = 1
    while (not converge(prob_ant, prob_act)):
        x = Sacar_primer_sobre()
        y = 0
        if(x+y == 6):
            exitos+1
        N+1
        prob_ant = prob_act
        prob_act = exitos / N
    return prob_act
