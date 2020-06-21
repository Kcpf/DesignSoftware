"""
Faça uma função que varre uma lista de inteiros e troca os elementos negativos por zero. Sua função recebe uma lista como argumento e deve retornar a lista com os valores substituídos.

O nome da sua função deve ser zera_negativos.
"""

def zera_negativos(lista):
    for j, each in enumerate(lista):
        if each < 0:
            lista[j] = 0
    return lista