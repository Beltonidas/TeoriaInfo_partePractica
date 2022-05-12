from random import *
import numpy as np
prob_acum = [[0.5, 1, 1], [1/3, 2/3, 1], [0, 1, 1]]
vInicial_acum = [1/3, 2/3, 1]
epsilon = 0.00000001
simbolos = 3


def converge(act, ant):
    for i in range(simbolos):
        if(abs(act[i] - ant[i]) > epsilon):
            return False
    return True


def primer_simbolo():
    r = random()
    for i in range(simbolos):
        if (r < vInicial_acum[i]):
            return i


def segundo_simbolo(s_ant):
    r = random()
    for i in range(simbolos):
        if (r < prob_acum[s_ant][i]):
            return i


def Calcular_Vector_Estacionario():
    emisiones = [0, 0, 0]  # cantidad de emisiones de cada si
    V_actual = np.zeros(3)  # Vector de estado actual
    V_anterior = np.ones_like(V_actual)  # Vector de estado anterior
    S_MIN = 1000000
    s = primer_simbolo()
    emisiones[s] = emisiones[s]+1
    cant_simb = 1  # cantidad de simbolos emitidos
    while not converge(V_actual, V_anterior) or (cant_simb < S_MIN):
        s = segundo_simbolo(s)
        emisiones[s] += 1
        cant_simb += 1
        V_anterior = V_actual
        for i in range(len(V_actual)):
            V_actual[i] = emisiones[i]/cant_simb
    return V_actual


v = Calcular_Vector_Estacionario()
print(v)
