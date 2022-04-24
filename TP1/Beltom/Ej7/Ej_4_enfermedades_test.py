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


# enfermo = 0,005
listEstado_acumulada = [0.005, 1]

lista_uno = [0.05, 1]
lista_2 = [0.04, 1]

# positivo = 0.004455

listTest_acumulada = [0.004455, 1]
cantidadTests = 1000


def converge(act, ant):
    if(abs(ant - act) < 0.000001):
        return True
    return False


def resultadoTestPositivo(x):
    n = random()
    # x == 1 --> esta enfermo
    if (x == 1):
        if (n > 0.05):  # el test dio positivo
            return 0
        else:
            return 1
    else:
        # X == 0 --> esta sano
        if(n <= 0.04):
            return 2  # el test es positivo
        else:
            return 3


def estaEnferma():
    n = random()
    if (n <= 0.005):
        return 1
    else:
        return 0


def calc_prob():
    exitos = 0
    nTotal = 1
    probAnterior = -1
    probActual = 1
    cantMinima = 1000
    while((converge(probActual, probAnterior) == False) or (nTotal < cantMinima)):
        x = estaEnferma()
        y = resultadoTestPositivo(x)
        print("el valor de x es: ", x, " , el valor de y es: ", y)
        if (x == 1 and y == 0):
            exitos = exitos + 1
        if((x == 0 and y == 2) or (x == 1 and y == 0)):
            nTotal = nTotal + 1
        probAnterior = probActual
        probActual = exitos/nTotal
    return probActual


# Con esa entrada "cantMinima" me dio como resultado 0.107

resul = calc_prob()
print(resul)
