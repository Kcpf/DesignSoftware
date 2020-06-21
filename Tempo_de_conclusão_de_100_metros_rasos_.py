"""
Faça uma função que recebe um dicionário de atletas em uma corrida de 100 metros rasos e devolve um dicionário cujas chaves são os nomes dos atletas e os valores são os respectivos tempos de conclusão da prova. As chaves do dicionário de atletas são strings e os valores são a sua aceleração. Dica: assuma movimento retilíneo uniformemente variado com velocidade inicial 0.

O nome da sua função deve ser calcula_tempo.
"""

import math
def calcula_tempo(d):
    dic = {}
    for each in d:
        dic[each] = math.sqrt(200/d[each])
    return dic