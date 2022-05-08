from random import *
import numpy as np
#                   1               2          3
prob_acum = [[0.5, 1, 1], [1/3, 2/3, 1], [0, 1, 1]]
vInicial_acum = [1/3, 2/3, 1]

epsilon = 0.00001
simbolos = 3
T_MIN = 100000
pasos = 5


def converge(frecuenciaActual, frecuenciaAnterior):
    matriz_epsilon = np.full_like(frecuenciaActual, epsilon)
    difValorAbsoluto = np.absolute(frecuenciaAnterior-frecuenciaActual)

    # asigno un booleano que me dice si difValorAbsoluto es menor a matriz_epsiolon
    valores_verdad = np.less_equal(difValorAbsoluto, matriz_epsilon)

    # valores_verdad es arreglo de boolean, retorno true si todos son true
    return np.all(valores_verdad)


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
    retornos = np.zeros((3, pasos+1))  # matriz de retornos

    frecuenciaActual = np.zeros_like(retornos)  # matriz de prob
    frecuenciaAnterior = np.ones_like(retornos)  # matriz de prob

    # array total de retornos por simbolo
    total_retornos = np.zeros(3, dtype=np.intc)
    # array de ultimos retornos valor discernible
    ultimo_retorno = np.ones_like(total_retornos)*-1

    t_actual = 0

    Simbolo = first_symbol()
    ultimo_retorno[Simbolo] = t_actual

    while (t_actual < T_MIN or not converge(frecuenciaActual, frecuenciaAnterior)):
        Simbolo = second_symbol(Simbolo)
        t_actual += 1
        frecuenciaAnterior = frecuenciaActual

        if not (ultimo_retorno[Simbolo] == -1):
            pos = t_actual - ultimo_retorno[Simbolo]
            total_retornos[Simbolo] += 1
            if(pos <= pasos):
                retornos[Simbolo, pos] += 1
            # division dentro del if para que no de 0/0
            frecuenciaActual[Simbolo, :] = np.divide(
                retornos[Simbolo, :], total_retornos[Simbolo])

        # si es primera ocurrencia
        ultimo_retorno[Simbolo] = t_actual
    return frecuenciaActual


v = Prob_primera_recurrencia()
np.set_printoptions(precision=4)
print("recurrencia simbolos:\n" + str(v[:, 1:6]))
