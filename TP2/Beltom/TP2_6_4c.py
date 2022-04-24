from random import *

vInicial_acum = [0, 1, 1]
#                 0               1               2
prob_acum = [[0.25, 0.75, 1], [0.75, 1, 1], [0, 0.5, 1]]

# static data
epsilon = 0.0000000000001
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


def second_symbol(s_ant):
    r = random()
    for i in range(simbolos):
        # print("iterador i --> ", i)
        # print("nuemro random: ", r)
        # print("el simbolo anterior es: ", s_ant)
        #print("la matriz: ", prob_acum[i][s_ant])
        # if (r > 0.5):
        # print("el r tiene valor: ", r)
        # print("fila a operar: ", s_ant)
        if (r <= prob_acum[s_ant][i]):
            return i


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
