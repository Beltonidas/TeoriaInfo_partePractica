from operator import truediv
from random import *
prob_acumulada1 = [2/5, 1]
# fila 1: antes salio un sobre dificil
# fila 2: antes salio un sobre facil
prob_acumulada2 = [[1/4, 1 ] , [2/4, 1]]

def converge(ant,act):
    epsilon=0.001
    if(abs(ant-act) < epsilon):
        return True
    return False

def sacarSobre1():
    s=random()
    for n in range(2):
        if ( s <= prob_acumulada1[n]): # ¿< o <=?
            return n

def sacarSobre2(f1):
    s=random()
    for n in range(2):
        if ( s <= prob_acumulada2[f1][n]):
            return n

def calcular_Proba():
    min_experim=200
    exitos=0
    N=0
    prob_ant=-1
    prob_act=0
    while(not converge(prob_ant,prob_act) or N < min_experim):
        f1=sacarSobre1()
        f2=sacarSobre2(f1)
        # 0 es un sobre dificil, 1 es un sobre facil
        if (f1==1 or f2==1):
            exitos+=1
        N+=1
        prob_ant=prob_act
        prob_act=exitos/N
    return prob_act

proba=calcular_Proba()
print("proba: " + str(proba))
