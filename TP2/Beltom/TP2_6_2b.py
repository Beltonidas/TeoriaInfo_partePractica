from random import *
#import numpy as np

# vInicial_acum = np.array([0, 1, 1])
vInicial_acum = [0, 1, 1]

#                 S               L               N
prob_acum = [[0, 0.50000, 1],
             [0.25, 0.75, 1],
             [0.25, 0.75, 1]]

#                           S               L               N
# prob_acum = np.array([[0, 0.5, 1], [0.25, 0.75, 1], [0.25, 0.75, 1]])

# static data
epsilon = 0.00000001
simbolos = 3


def converge(act, ant):
    for i in range(simbolos):
        if(abs(ant[i] - act[i]) < 0.001):
            return True
    return False


def first_symbol():
    r = random()
    print(r)
    if (r <= 0.33):
        return 0
    if (r > 0.33 and r <= 0.66):
        return 1
    return 2

# def first_symbol():
#     r = random()
#     for i in range(simbolos):
#         if (r <= vInicial_acum[i]):
#             return i


def second_symbol(s_ant):
    r = random()
    for i in range(simbolos):
        print("iterador i --> ", i)
        # print("nuemro random: ", r)
        # print("el simbolo anterior es: ", s_ant)
        #print("la matriz: ", prob_acum[i][s_ant])
        if (r > 0.5):
            print("el r tiene valor: ", r)
            print("fila a operar: ", s_ant)
        if (r <= prob_acum[s_ant][i]):
            print(r, " <= ", prob_acum[s_ant][i])
            print("devuelvo el valor de i: ", i)

            return i


# def Calcular_Vector_Estado(iteration):
#     emisiones = [0, 0, 0]  # cantidad de emisiones de cada si
#     Vt = [0, 0, 0]  # Vector de estado actual
#     Vt_ant = [-1, 0, 0]  # Vector de estado anterior
#     mensajes = 0  # cantidad de mensajes emitidos
#     T_MIN = 500
#     s = first_symbol()
#     mensajes = 1
#     emisiones[s] += 1
#     while not converge(Vt, Vt_ant) or (mensajes < T_MIN):
#         s = first_symbol()
#         for i in range(len(iteration)):
#             s = second_symbol(s)
#             print(i)
#         emisiones[s] = emisiones[s]+1
#         mensajes = mensajes+1
#         Vt_ant = Vt
#         Vt = emisiones/mensajes
#     return Vt


def Calcular_Vector_Estacionario():
    emisiones = [0, 0, 0]  # cantidad de emisiones de cada si
    V_est = [0, 0, 0]  # Vector de estado actual
    V_est_ant = [-1, 0, 0]  # Vector de estado anterior
    T_MIN = 100000
    s = first_symbol()
    emisiones[s] = emisiones[s]+1
    # --> [0, 0, 0] -->
    mensajes = 1  # cantidad de mensajes emitidos
    while not converge(V_est, V_est_ant) or (mensajes < T_MIN):
        s = second_symbol(s)
        print("mi segundo simbolo: ", s)
        emisiones[s] += 1
        mensajes += 1
        V_est_ant = V_est
        for i in range(3):
            V_est[i] = emisiones[i]/mensajes
            # print(V_est[i], "entre ", mensajes)
    return V_est


v = Calcular_Vector_Estacionario()
print(v)
