from random import *
import re
listSobres = [2/5, 1]
def retirarSobre():
    n= random()
    print (n)
    for i in range(2):
        print ("iterador i: ",i)
        if n < listSobres[i]:
            return i

action = retirarSobre()
print (action)

