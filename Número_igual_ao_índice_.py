"""
Faça uma função que recebe uma lista de números e devolve uma lista com os números que são iguais ao índice no qual eles se encontram. Exemplos:

[1, 3, 2, 4] deve retornar [2]
[0, 10, 2, 30, 4] deve retornar [0, 2,4]
[5, 4, 3, 2, 1] deve retornar uma lista vazia

O nome da sua função deve ser numero_no_indice.
"""

def numero_no_indice(lista):
    resp = []
    for j, i in enumerate(lista):
        if i == j:
            resp.append(j)
    return resp