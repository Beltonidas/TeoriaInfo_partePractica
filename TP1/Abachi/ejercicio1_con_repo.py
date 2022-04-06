
from random import random


def Sacar_sobre():
    prob_acum = [2/5, 1]
    p = random()
    for i in range(len(prob_acum)):
        if p < prob_acum[i]:
            return i


def converge(ant, act):
    if (abs(ant - act) < 0.0001):
        return True
    return False


def Al_menos1_facil():  # probabilidad de sacar al menos un parcial facil
    exitos = 0
    n = 0
    prob_ant = -1
    prob_act = 0
    minimo = 0
    while (not converge(prob_ant, prob_act) or minimo < 20):
        x = Sacar_sobre()
        y = Sacar_sobre()
        if(x == 1) or (y == 1):
            exitos = exitos+1
        n = n+1
        prob_ant = prob_act
        prob_act = exitos/n
        minimo = minimo+1
        print("proba actual: ", prob_act)
    return prob_act


def dos_faciles():  # probabilidad de sacar dos parciales faciles
    exitos = 0
    n = 0
    prob_ant = -1
    prob_act = 0
    minimo = 0
    while (not converge(prob_ant, prob_act) or minimo < 20):
        x = Sacar_sobre()
        y = Sacar_sobre()
        if(x == 1) and (y == 1):
            exitos = exitos+1
        n = n+1
        prob_ant = prob_act
        prob_act = exitos/n
        minimo = minimo+1
        print("proba actual: ", prob_act)
    return prob_act


def segundo_facil_dado_dificil():  # probabilidad de sacar el segundo facil dado uno dificil
    exitos = 0
    n = 0
    prob_ant = -1
    prob_act = 0
    minimo = 0
    while (not converge(prob_ant, prob_act) or minimo < 20):
        x = Sacar_sobre()
        if(x == 0):
            y = Sacar_sobre()
            if(y == 1):
                exitos = exitos+1
        n = n+1
        prob_ant = prob_act
        prob_act = exitos/n
        minimo = minimo+1
        print("proba actual: ", prob_act)
    return prob_act


prueba = dos_faciles()
print(prueba)
