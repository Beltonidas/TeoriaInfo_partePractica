import random as randomLibrary
from random import *
n = random()
print(n)


def Arrojar_dado():
    prob_acum = [1/6, 2/6, 3/6, 4/6, 5/6, 1]
    p = randomLibrary
    for i in range(6):
        if p < prob_acum[i]:
            return i


def converge(ant, act):
    if (abs(ant - act) < 0.00000000001):
        return True
    return False


def Calcular_Prob_Suma6():
    exitos = 0
    N = 0
    prob_ant = -1
    prob_act = 1
    while (not converge(prob_ant, prob_act)):
        x = Arrojar_dado()
        y = Arrojar_dado()
        if(x+y == 6):
            exitos+1
        N+1
        prob_ant = prob_act
        prob_act = exitos / N
    return prob_act