import math

# Estructuras de datos
listPi = [0.4, 0.12, 0.25, 0.08, 0.15];
listLog= [0,0,0,0,0];
logbn = 0
entropia = 0
for i in range(len(listPi)):
    logbn= -math.log(listPi[i])/math.log(2)
    listLog[i] = logbn


for i in range(len(listPi)):
    entropia += listPi[i]*listLog[i]

print("El resultado es: ", entropia)

