from operator import truediv
from random import *
prob_acu_enfermo = [0.005, 1]
# fila 1: antes dio enfermo, proba de que de positivo
# fila 2: antes dio sano, proba de que de positivo
prob_acu_test = [[0.95, 1] , [0.04, 1]]

def converge(ant,act):
    epsilon=0.00001
    if(abs(ant-act) < epsilon):
        return True
    return False

def enfermedad():
    s=random()
    for n in range(2):
        if ( s <= prob_acu_enfermo[n]): # ¿< o <=?
            return n

def testear(f1):
    s=random()
    for n in range(2):
        if ( s <= prob_acu_test[f1][n]):
            return n

def calcular_Proba():
    min_experim=20000
    exitos=0
    N=0
    prob_ant=-1
    prob_act=0
    while(not converge(prob_ant,prob_act) or (N < min_experim)):
        f1=enfermedad()
        f2=testear(f1)
        #f1= 0 es enfermo
        #f2= 0 es positivo
        if (f1==0 and f2==0):
            exitos+=1
        if (f2==0):
            N+=1
            prob_ant=prob_act
            prob_act=exitos/N
    return prob_act

proba=calcular_Proba()
print("proba analitica: 0.1066")
print("proba muestreo: " + str(proba))
