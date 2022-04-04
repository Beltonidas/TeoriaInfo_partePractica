# #A partir de un estudio estadístico en una población se ha determinado que la probabilidad de que
# una persona posea cierta enfermedad es 0,005. Se ha comprobado además que si una persona
# posee la enfermedad, la probabilidad de que el examen médico dé resultado positivo es del 95%.
# Por otro lado, si alguien que no posee la enfermedad se somete al examen, la probabilidad de que
# éste dé negativo es del 96%.
# a) si alguien obtiene un resultado negativo en el examen, cuál es la probabilidad de que esté sana?
# b) si una persona obtiene un resultado positivo, ¿cuál es la probabilidad de que realmente esté
# enferma?

from random import *
n = random()
print(n)

# ctrl + k + c comentas
# ctrl + k + u descomentas

listEstado_acumulada = [0.005, 0.995]
listTest_acumulada = [0.004455, 1]
cantidadTests = 1000
