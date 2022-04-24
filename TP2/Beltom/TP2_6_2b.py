from random import *
# import numpy as np

# vInicial_acum = np.array([0, 1, 1])
vInicial_acum = [0, 1, 1]

#                 S               L               N
prob_acum = [[0, 0.5, 1], [0.25, 0.75, 1], [0.25, 0.75, 1]]

#                           S               L               N
# prob_acum = np.array([[0, 0.5, 1], [0.25, 0.75, 1], [0.25, 0.75, 1]])

# static data
epsilon = 0.0001
simbolos = 3


def converge(act, ant):
    for i in range(simbolos):
        if(abs(ant[i] - act[i]) < 0.001):
            return True
    return False


def first_symbol():
    r = random()
    print (r)
    if (r <= 0.33):
        return 0
    if (r > 0.33 and r<= 0.66):
        return 1
    return 2


# def prueba():
#     for i in range(100):
#         aux = first_symbol()
#         print(aux)


# result = prueba()
# print(result)


def second_symbol(s_ant):
    r = random()
    for i in range(simbolos):
        if (r < prob_acum[i, s_ant]):
            return i


def Calcular_Vector_Estado(iteration):
    emisiones = [0, 0, 0]  # cantidad de emisiones de cada si
    Vt = [0, 0, 0]  # Vector de estado actual
    Vt_ant = [-1, 0, 0]  # Vector de estado anterior
    mensajes = 0  # cantidad de mensajes emitidos
    T_MIN = 500

    while not converge(Vt, Vt_ant) or (mensajes < T_MIN):
        s = first_symbol()
        for i in range(len(iteration)):
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
    T_MIN = 500
    s = first_symbol()
    emisiones[s] = emisiones[s]+1
    mensajes = 1  # cantidad de mensajes emitidos
    while not converge(V_est, V_est_ant) or (mensajes < T_MIN):
        s = second_symbol(s)
        emisiones[s] = emisiones[s]+1
        mensajes = mensajes+1
        V_est_ant = V_est
        V_est = emisiones/mensajes

    return V_est

v= Calcular_Vector_Estacionario()
print(v)