import random as randomLibrary
from random import *
n = random()
print(n)


def Sacar_sobre():
    prob_acum = [2/5, 3/5, 1]
    p = randomLibrary
    for i in range(2):
        if p < prob_acum[i]:
            return i


def converge(ant, act):
    if (abs(ant - act) < 0.00000000001):
        return True
    return False


def Sacar_al_menos_1_facil():
    exitos = 0
    N = 0
    prob_ant = -1
    prob_act = 1
    while (not converge(prob_ant, prob_act)):
        x = Sacar_sobre()
        y = Sacar_sobre()
        if(x+y == 6):
            exitos+1
        N+1
        prob_ant = prob_act
        prob_act = exitos / N
    return prob_act
