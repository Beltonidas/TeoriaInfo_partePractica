from random import random



def Arrojar_dado():
    prob_acum = {1/6, 2/6, 3/6, 4/6, 5/6, 1}
    p = random()
    X = 6
    for i in range(6):
        if (p < prob_acum[i]): 
            return i
