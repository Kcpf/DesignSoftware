"""
Escreva uma função que recebe um vetor de dimensão arbitrária representado por uma lista e devolve a sua norma. Caso seja necessário, pesquise por norma ou módulo de um vetor no Google ;)

O nome da sua função deve ser calcula_norma.
"""

import math

def calcula_norma(l):
    lista = []
    for c in l:
        lista.append(c**2)
    return math.sqrt(sum(lista))