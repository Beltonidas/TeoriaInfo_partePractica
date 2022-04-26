from random import *
#import numpy as np

# vInicial_acum = np.array([0, 1, 1])
vInicial_acum = [0, 1, 1]

#                 S               L               N
prob_acum = [[0, 0.5, 1],
<<<<<<< HEAD
             [0.25, 0.75, 1],
=======
            [0.25, 0.75, 1],
>>>>>>> 58605c8f46b52197980352c13dee5c8bc2f3af36
             [0.25, 0.75, 1]]

#                           S               L               N
# prob_acum = np.array([[0, 0.5, 1], [0.25, 0.75, 1], [0.25, 0.75, 1]])

# static data
epsilon = 0.000001
simbolos = 3


def converge(act, ant):
    vTrue= [False,False,False]
    print (vTrue)
    for i in range(simbolos):
        if(abs(act[i] - ant[i]) < epsilon):
            vTrue[i]= True
    
    for i in range(len(vTrue)):
        if(vTrue[i]== False):
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



def Calcular_Vector_Estacionario():
    emisiones = [0, 0, 0]  # cantidad de emisiones de cada si
    V_est = [0, 0, 0]  # Vector de estado actual
    V_est_ant = [-1, 0, 0]  # Vector de estado anterior
    T_MIN = 1000
    s = first_symbol()
    emisiones[s] = emisiones[s]+1
    # --> [0, 0, 0] -->
    mensajes = 1  # cantidad de mensajes emitidos
    while (not converge(V_est, V_est_ant)or mensajes < T_MIN):
        s = second_symbol(s)
<<<<<<< HEAD
        # print("mi segundo simbolo: ", s)
=======
>>>>>>> 58605c8f46b52197980352c13dee5c8bc2f3af36
        emisiones[s] += 1
        mensajes += 1
        V_est_ant = V_est
        for i in range(3):
            V_est[i] = emisiones[i]/mensajes
            # print(V_est[i], "entre ", mensajes)
    return V_est


v = Calcular_Vector_Estacionario()
print(v)
