from random import *
#                   0               1          2
prob_acum = [[0.5, 1, 1], [1/3, 2/3, 1], [0, 1, 1]]


vInicial_acum = [0, 1, 1]

epsilon = 0.0001
simbolos = 3
T_MIN = 1000
pasos = 500


def converge(act, ant):
    for i in range(pasos):
        if(abs(act[i] - ant[i]) > epsilon):
            return False
    return True


def first_symbol():
    r = random()
    for i in range(simbolos):
        if (r <= vInicial_acum[i]):
            return i


def second_symbol(s_ant):
    r = random()
    for i in range(simbolos):
        if (r <= prob_acum[s_ant][i]):
            return i


def Prob_primera_recurrencia(simbolo):
    pasos = 500
    T_MIN = 1000
    retornos = []  # retornos a si en n pasos
    frecuenciaInicial = []  # prob. primera recurrencia actual
    frecIncAnte = []  # prob. primera recurrencia anterior
    for _ in range(pasos):
        frecuenciaInicial.append(0)
        frecIncAnte.append(-1)
        retornos.append(0)
    t_actual = 0
    ret_total = 0
    ult_ret = 0
    # parámetro (no es necesario generar Primer_Simbolo)
    nuevoSimbolo = simbolo
    while (t_actual < T_MIN or not converge(frecuenciaInicial, frecIncAnte)):
        nuevoSimbolo = second_symbol(nuevoSimbolo)
        t_actual += 1
        frecIncAnte = frecuenciaInicial
        if (nuevoSimbolo == simbolo):   # hay retorno
            pos = t_actual - ult_ret
            retornos[pos] += 1
            ret_total += 1
            ult_ret = t_actual
            for i in range(pasos):
                frecuenciaInicial[i] = retornos[i]/ret_total
            
    return frecuenciaInicial


v = Prob_primera_recurrencia(2)
print(v)
