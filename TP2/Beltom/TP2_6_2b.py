from random import *
# import numpy as np

# vInicial_acum = np.array([0, 1, 1])
vInicial_acum = [0, 1, 1]

#                 S               L               N
prob_acum = [[0, 0.5, 1], [0.25, 0.75, 1], [0.25, 0.75, 1]]

#                           S               L               N
# prob_acum = np.array([[0, 0.5, 1], [0.25, 0.75, 1], [0.25, 0.75, 1]])

epsilon = 0.0001


def Emitir_Simbolo():
    r = random()
    for i in range(len(simbolos)):
        if (r < Vacum[i]):
            return i


def converge(act, ant):
    if(abs(ant - act) < 0.001):
        return True
    return False


def first_symbol():
    r = random()
    for i in range(len(simbolos)):
        if (r < V0acum[i]):
            return i


def second_symbol(s_ant):
    r = random()
    for i in range(len(simbolos)):
        if (r < Macum[i, s_ant]):
            return i


def Calcular_Vector_Estado(iteration):
    emisiones = [0, 0, 0]  # cantidad de emisiones de cada si
    Vt = [0, 0, 0]  # Vector de estado actual
    Vt_ant = [-1, 0, 0]  # Vector de estado anterior
    mensajes = 0  # cantidad de mensajes emitidos

    T_MIN = 500

    while not converge(Vt, Vt_ant) or (mensajes < T_MIN):
        s = first_symbol()

        for i in range(len(interation)):
            s = second_symbol(s)
            print(i)
        emisiones[s] = emisiones[s]+1
        mensajes = mensajes+1
        Vt_ant = Vt
        Vt = emisiones/mensajes

    return Vt


def Calcular_Vector_Estacionario():
    emisiones = [0, 0, 0]  # cantidad de emisiones de cada si
    V_est = [0, 0, 0]  # Vector de estado actual
    V_est_ant = [-1, 0, 0]  # Vector de estado anterior
    mensajes = 0  # cantidad de mensajes emitidos
    T_MIN = 500
    while not converge(V_est, V_est_ant) or (mensajes < T_MIN):
        s = first_symbol()
        for i in range(len(t)):
            s = second_symbol(s)
        emisiones[s] = emisiones[s]+1
        mensajes = mensajes+1
        V_est_ant = V_est
        V_est = emisiones/mensajes

    return V_est


print(vInicial_acum.shape[0])

resultado = Calcular_Vector_Estacionario()
print(resultado)
