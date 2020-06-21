"""
Faça uma função que recebe dois dicionários e devolve uma lista contendo as chaves que estão presentes em ambos os dicionários.

O nome da sua função deve ser interseccao_chaves.
"""

def interseccao_chaves(dic1, dic2):
    lista = []
    for c in dic1:
        if c in dic2:
            lista.append(c)
    return lista