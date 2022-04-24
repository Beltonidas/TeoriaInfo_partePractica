from operator import truediv
from random import *
import numpy as np

v0_acu=np.array([1,1,1])
#                           0               1              2
proba_acu = np.array([[0.25, 0.75, 1], [0.75, 1, 1], [0, 0.5, 1]])
epsilon=0.0001

def converge(v_ant, v_act):
    epsilons = np.ones_like(v_act) * epsilon
    absolutes = np.absolute(v_act - v_ant)
    truth_values = np.less_equal(absolutes,epsilons)
    return np.all(truth_values)

def first_symbol():
    r=random()
    for n in range(v0_acu.shape[0]):
        if(r <= v0_acu[n]):
            return n

def next_symbol_given(s_pre):
    r=random()
    for n in range(proba_acu.shape[1]):
        if(r <= proba_acu[s_pre,n]):
            return n

def v_un_emision():
    v=np.zeros(3)
    #esto solo es la parte de la tirada, falta el muestreo y convergencia
    s=next_symbol_given(first_symbol())
    v[s]+=1
    return v

def v_tres_emisiones():
    v = emisiones = np.zeros(3)
    s=first_symbol()
    cant_symb=0
    #esto solo es la parte de las 3 tiradas, falta el muestreo y convergencia
    for n in range(3):
        s=next_symbol_given(s)
        cant_symb+=1
        emisiones[s]+=1
        v[s]=emisiones/cant_symb
    return v

def distr_proba_rep(rep):
    min=1000
    v_act= emisiones = np.zeros(3)
    v_ant= np.ones_like(v_act)
    cant_symb=0
    while(not converge(v_ant,v_act) or cant_symb < min):
        s=first_symbol()
        for n in range(rep):
            s=next_symbol_given(s)
        emisiones[s]+=1
        cant_symb+=1
        v_ant=v_act
        v_act=emisiones/cant_symb
    return v_act

v1=distr_proba_rep(1)
print(v1)
v2=distr_proba_rep(2)
print(v2)
v3=distr_proba_rep(3)
print(v3)