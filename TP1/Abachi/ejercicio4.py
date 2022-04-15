from random import random

Prob_Negativo = 0.005*0.05+0.995*0.96
Prob_Positivo = 0.995*0.04+0.005*0.95


def Enfermo_o_Sano():
    prob_acum = [0.005, 1]
    p = random()
    for i in range(len(prob_acum)):
        if p < prob_acum[i]:  # si es 0 esta enfermo, si es 1 esta sano
            return i


def Resultado_Test(Estado_Salud):
    if(Estado_Salud == 0):
        prob_acum = [0.05, 1]  # si es 0 es -, si es 1 es +
    else:
        prob_acum = [0.96, 1]  # si es 0 es -, si es 1 es +
    p = random()
    for i in range(len(prob_acum)):
        if p < prob_acum[i]:
            return i


def converge(ant, act):
    if (abs(ant - act) < 0.000001):
        return True
    return False


def Enfermo_dado_positivo():
    exitos = 0
    n = 1
    prob_ant = -1
    prob_act = 1
    minimo = 0
    while (not converge(prob_ant, prob_act) or minimo < 15):
        x = Enfermo_o_Sano()
        print("Enfermo/Sano", x)
        y = Resultado_Test(x)
        print("Es +/-", y)
        if((x == 0 and y == 1)):
            exitos = exitos+1
        if((x == 0 and y == 2) or (x == 1 and y == 0)):
            n = n+1
        prob_ant = prob_act
        prob_act = exitos / n
        minimo = minimo+1
    return prob_act/Prob_Positivo


def Sano_dado_negativo():
    exitos = 0
    n = 0
    prob_ant = -1
    prob_act = 1
    minimo = 0
    while (not converge(prob_ant, prob_act) or minimo < 15):
        x = Enfermo_o_Sano()
        print("Enfermo/Sano", x)
        y = Resultado_Test(x)
        print("Es +/-", y)
        if((x == 1 and y == 0)):
            exitos = exitos+1
        n = n+1
        prob_ant = prob_act
        prob_act = exitos / n
        minimo = minimo+1
    return prob_act


prueba = Enfermo_dado_positivo()
print(prueba)
