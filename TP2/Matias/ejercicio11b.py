from random import *
import numpy as np
#                   1               2          3
prob_acum = [[0.5, 1, 1], [1/3, 2/3, 1], [0, 1, 1]]


vInicial_acum = [1/3, 2/3, 1]

epsilon = 0.0001
simbolos = 3
T_MIN = 1000
pasos = 500


def converge(act, ant):
    for i in range(pasos):
        if(abs(act[i] - ant[i]) > epsilon):
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
    pasos = 5
    T_MIN = 1000
    retornos = np.zeros((3,pasos)) # retornos a si en n pasos
    frecRetornos = np.zeros((3,pasos)) # matriz de retornos pero en probabilidades
    frecuenciaActual = []  # prob. primera recurrencia actual
    frecIncAnte = []  # prob. primera recurrencia anterior
    total_retornos = [] # array de total de retornos por simbolo
    ult_ret = [] # array de ultimos retornos
    
    for _ in range(pasos):#inicializamos arrays
        frecuenciaActual.append(0)
        frecIncAnte.append(-1)
        total_retornos.append(0)
        ult_ret.append(0)

    t_actual = 0    
    primerSimbolo = first_symbol()
    ult_ret[primerSimbolo] = t_actual

    while (t_actual < T_MIN or not converge(frecuenciaActual, frecIncAnte)):
        NuevoSimbolo = second_symbol(primerSimbolo)
        t_actual += 1
        frecIncAnte = frecuenciaActual
        pos = t_actual - ult_ret[NuevoSimbolo]
        if not (pos == -1):
            retornos[NuevoSimbolo,pos] += 1
            total_retornos[NuevoSimbolo] += 1
        ult_ret[NuevoSimbolo] = t_actual
        # : selecciona todas las columnas
        frecRetornos[NuevoSimbolo,:] = retornos[NuevoSimbolo,:]/total_retornos[NuevoSimbolo]
    return frecRetornos

v = Prob_primera_recurrencia()
print(v)
