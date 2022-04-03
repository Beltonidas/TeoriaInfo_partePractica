from random import random



def Arrojar_dado():
    prob_acum = [1/6, 2/6, 3/6, 4/6, 5/6, 1]
    p = random()
    for i in range(len(prob_acum)):
        if (p < prob_acum[i]): 
            return i+1

def converge (ant, act): 
   if ( abs (ant - act )< 0.0001 ):
        return True
   return False
 
def Calcular_prob_suma6():
    exitos=0
    n=0
    prob_ant=-1
    prob_act=0
    minimo=0
    while (not converge (prob_ant,prob_act) or minimo<15):
        x= Arrojar_dado();
        y= Arrojar_dado();
        if(x+y==6):
            exitos=exitos+1
        n=n+1
        prob_ant=prob_act
        prob_act= exitos/n
        minimo=minimo+1
        print("X: ",x)
        print("Y: ",y)
        print("exito: ",exitos)
        print("N: ",n)
    return prob_act


prueba=Calcular_prob_suma6()

print(prueba)