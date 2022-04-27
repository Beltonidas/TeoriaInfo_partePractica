from operator import truediv
from random import *
import numpy as np

v0_acu = np.array([0, 1, 1])
#                           S               N              L
proba_acu = np.array([[0, 0.5, 1], [0.25, 0.75, 1], [0.25, 0.5, 1]])
epsilon = 0.0001


def converge(v_act, v_pre):
    epsilons = np.ones_like(v_act) * epsilon
    vec_abs = np.absolute(v_pre - v_act)
    truth_vals = np.less_equal(vec_abs, epsilons)
    return np.all(truth_vals)


def first_symbol():
    r = random()
    for n in range(v0_acu.shape[0]):
        if(r <= v0_acu[n]):
            return n


def next_symbol_given(s_pre):
    r = random()
    for n in range(proba_acu.shape[1]):
        if(r <= proba_acu[s_pre, n]):
            return n


def calculate_V():
    # init
    v_act = emisions = np.zeros(3)
    v_pre = np.ones_like(v_act)
    min_it = 1000
    s = first_symbol()
    cant_symb = 1
    emisions[s] += 1
    # iter
    while(not converge(v_act, v_pre) or cant_symb < min_it):
        s = next_symbol_given(s)
        emisions[s] += 1
        cant_symb += 1
        v_pre = v_act
        v_act = emisions/cant_symb
    return v_act


v = calculate_V()
print("resultado analitico: [0.2 0.4 0.4]")
print("resultado muestreo: " + str(v))
