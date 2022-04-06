from operator import truediv
from random import *
prob_acumulada =[2/5, 1]

def converge(ant,act):
    epsilon=0.001
    if(abs(ant-act) < epsilon):
        return True
    return False

def sacarSobre():
    s=random()
    for n in range(2):
        if ( s <= prob_acumulada[n]): # ¿< o <=?
            return n

def calcular_Proba():
    min_experim=200
    exitos=0
    N=0
    prob_ant=-1
    prob_act=0
    while(not converge(prob_ant,prob_act) or N < min_experim):
        f1=sacarSobre()
        f2=sacarSobre()
        # 0 es un sobre dificil, 1 es un sobre facil
        if (f1 != f2): # (f1=0 y f2=1) o (f1=1 y f2=0)
            exitos+=1
        N+=1
        prob_ant=prob_act
        prob_act=exitos/N
    return prob_act

proba=calcular_Proba()
print("proba: " + str(proba))