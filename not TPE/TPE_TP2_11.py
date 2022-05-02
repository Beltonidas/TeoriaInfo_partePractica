from random import *
import numpy as np

#inicializacion
v0_acu=np.array([0,1,1])
proba_acu = np.array([[1/2, 1, 1], [1/3, 2/3, 1], [0, 1, 1]])
epsilon = 0.0001

def converge(act, ant):
    epsilons = np.full_like(act, epsilon)
    absolutos = np.absolute(ant-act)
    valores_verdad = np.less_equal(absolutos, epsilons)
    #valores_verdad es arreglo de boolean, retorno true si todos son true
    return np.all(valores_verdad)

def primer_simbolo():
    r=random()
    nro_simbolos = v0_acu.shape[0]
    for n in range(nro_simbolos):
        if(r <= v0_acu[n]):
            return n

def sig_dado_ant(s_ant):
    r=random()
    nro_simbolos = proba_acu.shape[1]
    for n in range(nro_simbolos):
        valor = proba_acu[s_ant,n]
        if(r <= valor):
            return n

def calcular_V():
    #inicializacion
    v_act = np.zeros(3)
    emisiones = np.zeros_like(v_act)
    v_ant = np.ones_like(v_act)
    min = 1000
    s=primer_simbolo()
    cant_simb = 1
    emisiones[s] += 1
    #iteracion
    while(not converge(v_act,v_ant) or cant_simb<min):
        v_ant = v_act
        s=sig_dado_ant(s)
        emisiones[s] += 1
        cant_simb += 1
        v_act = emisiones/cant_simb
    return v_act

def calcular_1er_recurrencia():
    #inicializacion
    min = 10000
    n_Pasos = 5
    t_actual = 0
    total_retornos = np.zeros(3, dtype=np.intc) #ver si puedo generalizarlo
    retornos = np.zeros((3, n_Pasos+1)) #sumo 1 porque no voy a usar el cero
    f_act = np.zeros_like(retornos)
    f_ant = np.ones_like(retornos)
    ult_ret = np.zeros_like(total_retornos)
    #al aparecer un numero, puede que sea su primer ocurrencia, en vez de una recurrencia
    hubo_1er_ocurrencia = np.full(3,False)
    s=primer_simbolo()
    hubo_1er_ocurrencia[s] = True
    #iteracion
    while(not converge(f_act,f_ant) or t_actual < min):
        t_actual += 1
        f_ant = f_act
        s = sig_dado_ant(s)

        #Puede que sea la primer ocurrencia de "s", en vez de una recurrencia
        if(not hubo_1er_ocurrencia[s]):
            hubo_1er_ocurrencia[s] = True
        else:
            total_retornos[s] += 1
            tiempo_ret = t_actual - ult_ret[s]
            if(tiempo_ret <= 5):
                retornos[s,tiempo_ret] += 1
            #la notación f[s,:] significa "de la fila s, todas las columnas"
            f_act[s,:] = retornos[s,:]/total_retornos[s]
        ult_ret[s] = t_actual
    return f_act

#calculos
v = calcular_V()
rec = calcular_1er_recurrencia()

#obtengo las condicionadas a partir de las acumuladas
proba_cond = np.zeros(3)
proba_cond[0] = v[0]*proba_acu[0,0]
for n in range(1,proba_acu.shape[1]):
    #quito la acumulada anterior, para quedarme con la proba condicionada sin acumular
    prob_cond_n = proba_acu[n,n] - proba_acu[n,n-1]
    proba_cond[n] = v[n]*prob_cond_n

np.set_printoptions(precision=3)
print("v*:\n" + str(v))
print("proba condicionada:\n" + str(proba_cond))
print("recurrencia en n pasos:\n" + str(rec[:,1:6]))
