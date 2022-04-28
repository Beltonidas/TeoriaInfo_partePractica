from random import *
#               1               2               3
prob_acum = [[0.5, 0.5, 1],
             [0.333, 0.666, 1],
             [0, 1, 1]]
vInicial_acum = [0, 1, 1]

epsilon = 0.0000001
simbolos = 3
T_MIN = 10000


def converge(act, ant):
    for i in range(simbolos):
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


def Prob_primera_recurrencia(simbolos):
    retornos = [0, 0, 0]  # retornos a si en n pasos
    fi_i = [0, 0, 0]  # prob. primera recurrencia actual
    fi_i_ant = [-1, -1, -1]  # prob. primera recurrencia anterior
    t_actual = 0
    ret_total = 0
    ult_ret = 0
    s = simbolos  # parámetro (no es necesario generar Primer_Simbolo)
    while not converge(fi_i, fi_i_ant) or (t_actual < T_MIN):
        s = second_symbol(s)
        t_actual += 1
        if (s == simbolos):   # hay retorno
            n = t_actual - ult_ret
            retornos[n] += 1
            ret_total += 1
            fi_i_ant = fi_i
            fi_i = retornos / ret_total
            ult_ret = t_actual
    return fi_i


v = Prob_primera_recurrencia(simbolos)
print(v)
