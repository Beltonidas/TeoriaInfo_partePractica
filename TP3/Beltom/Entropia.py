import math
from operator import truediv

# Estructuras de datos
listPi = [0.385, 0.154, 0.128, 0.154, 0.179];
listLog= [0,0,0,0,0];
listLong=[]


logbn = 0
entropia = 0
for i in range(len(listPi)):
    logbn= -math.log(listPi[i])/math.log(2)
    listLog[i] = logbn


for i in range(len(listPi)):
    entropia += listPi[i]*listLog[i]

print("El resultado es: ", entropia)

