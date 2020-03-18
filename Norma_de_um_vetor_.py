import math

def calcula_norma(l):
    lista = []
    for c in l:
        lista.append(c**2)
    return math.sqrt(sum(lista))