from random import *
import numpy as np
from operator import truediv
#                   1               2          3
prob_acum = [[0.5, 1, 1], [1/3, 2/3, 1], [0, 1, 1]]


vInicial_acum = [1/3, 2/3, 1]

epsilon = 0.0001
simbolos = 3
T_MIN = 1000
pasos = 6


def converge(act, ant, pasos, Simbolo):
    for i in range(pasos):
        if(abs(act[Simbolo, i] - ant[Simbolo, i]) > epsilon):
            return False
    return True


def first_symbol():
    r = random()
    for i in range(simbolos):
        if (r <= vInicial_acum[i]):
            return i


def second_symbol(s_ant):
    r = random()
    for i in range(simbolos):
        if (r <= prob_acum[s_ant][i]):
            return i


def Prob_primera_recurrencia():
    # retornos = recurrencia
    retornos = np.zeros((3, pasos))  # retornos a si en n pasos
    # matriz de retornos pero en probabilidades
    frecuenciaActual = np.zeros((3, pasos))  # prob. primera recurrencia actual
    frecIncAnte = np.ones_like(frecuenciaActual)
    frecIncAnte = frecIncAnte*-1  # prob. primera recurrencia anterior
    total_retornos = [0, 0, 0]  # array de total de retornos por simbolo
    ult_ret = [-1, -1, -1]  # array de ultimos retornos
    t_actual = 0
    Simbolo = first_symbol()
    ult_ret[Simbolo] = t_actual
    while (t_actual < T_MIN or not converge(frecuenciaActual, frecIncAnte, pasos, Simbolo)):
        Simbolo = second_symbol(Simbolo)
        t_actual += 1
        frecIncAnte = frecuenciaActual
        if not (ult_ret[Simbolo] == -1):
            pos = t_actual - ult_ret[Simbolo]
            if()
            retornos[Simbolo, pos] += 1
            total_retornos[Simbolo] += 1
        ult_ret[Simbolo] = t_actual
        # : selecciona todas las columnas
        frecuenciaActual[Simbolo, :] = retornos[Simbolo, :] / \
            total_retornos[Simbolo]
    return frecuenciaActual


v = Prob_primera_recurrencia()
print(v)
