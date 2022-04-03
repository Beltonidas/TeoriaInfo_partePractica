from pickle import TRUE
from random import random



def Sacar_sobre():
    prob_acum = [2/5,3/5, 1]
    p = random()
    for i in range(6):
        if (p < prob_acum[i]): 
            return i

def converge (ant, act): 
   if ( abs (ant - act )< 0.0000000001 ):
        return True
   return False
 
def Calcular_prob_suma6(prob_act):
    exitos=0
    N=2
    prob_ant=-1
    prob_act=0
    minimo=0
    while (not converge (prob_ant,prob_act) or minimo>2):
        x= Arrojar_dado();
        y= Arrojar_dado();
        if(x+y==6):
            exitos+1
        N+1
        prob_ant=prob_act
        prob_act= exitos/N
    return prob_act
