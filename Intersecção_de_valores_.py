"""
Faça uma função que recebe dois dicionários e devolve uma lista contendo os valores que estão presentes em ambos os dicionários.

O nome da sua função deve ser interseccao_valores.
"""

def interseccao_valores(dic1, dic2):
    l = []
    l1 = list(dic1.values())
    l2 = list(dic2.values())
    for c in l1:
        if c in l2:
            l.append(c)
    return l
         