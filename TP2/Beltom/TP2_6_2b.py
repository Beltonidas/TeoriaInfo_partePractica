from random import *
# import numpy as np

# vInicial_acum = np.array([0, 1, 1])
vInicial_acum = [0, 1, 1]

#                 S               L               N
prob_acum = [[0, 0.5, 1], [0.25, 0.75, 1], [0.25, 0.75, 1]]

#                           S               L               N
# prob_acum = np.array([[0, 0.5, 1], [0.25, 0.75, 1], [0.25, 0.75, 1]])

epsilon = 0.0001


def converge(act, ant):
    if(abs(ant - act) < 0.001):
        return True
    return False


def first_symbol():
    r = random()
    return r


print(vInicial_acum.shape[0])
