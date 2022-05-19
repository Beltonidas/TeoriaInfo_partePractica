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

#Calculadora codigo Huffman
lista_valores = [(0.5,[0]),(0.3,[1]),(0.1,[2]),(0.1,[3])]
lista_codigos = []

for x in range(len(lista_valores)):
    lista_codigos.append([])

def calcular_codigos(lista_valores_originales):
    def devolverPrimero(elemento):
        return elemento[0]

    while (len(lista_valores_originales)>1):
        lista_valores_originales.sort(key=devolverPrimero)

        elemento1 = lista_valores_originales.pop(0)
        for x in elemento1[1]:
            lista_codigos[x].append(0)

        elemento2 = lista_valores_originales.pop(0)
        for x in elemento2[1]:
            lista_codigos[x].append(1)

        elemento_aux = []
        elemento_aux.append(elemento1[0]+elemento2[0])
        elemento_aux.append(elemento1[1]+elemento2[1])
        lista_valores_originales.append(elemento_aux)
    for x in lista_codigos:
        x.reverse()

calcular_codigos(lista_valores)
print(lista_codigos)