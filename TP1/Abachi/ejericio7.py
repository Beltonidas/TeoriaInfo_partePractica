from pickle import TRUE
from random import random


def Sacar_sobre():
    prob_acum = [2/5, 1]
    p = random()
    for i in range (len(prob_acum)):
        if p < prob_acum[i]: 
            return i
         

def converge (ant, act): 
   if ( abs (ant - act )< 0.0000000001 ):
        return True
   return False
 
def Calcular_prob_al_menos1_facil():
    exitos=0
    n=0
    prob_ant=-1
    prob_act=0
    minimo=0
    while (not converge (prob_ant,prob_act) or minimo<2):
        x= Sacar_sobre()
        y= Sacar_sobre()
        if(x>2/5 and x<=1 ) or (y>=0 and y<2/5 ): 
           exitos=exitos+1
        n=n+1
        prob_ant=prob_act
        prob_act= exitos/n
        minimo=minimo+1
        print("proba actual: ",prob_act)
    return prob_act

prueba= Calcular_prob_al_menos1_facil()
print(prueba)