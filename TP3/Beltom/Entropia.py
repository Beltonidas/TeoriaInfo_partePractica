import math
from operator import truediv

# Estructuras de datos
listPi = [0.6, 0.1, 0.3];
listLog= [0,0,0];

#listPi = [1/22,1/22,18/44, 6/44, 1/11, 1/11, 4/22];
#listLog= [0,0,0, 0,0,0, 0];
#listLong=[]


logbn = 0
entropia = 0
for i in range(len(listPi)):
    logbn= -math.log(listPi[i])/math.log(2)
    listLog[i] = logbn


for i in range(len(listPi)):
    entropia += listPi[i]*listLog[i]

print("El resultado es: ", entropia)

