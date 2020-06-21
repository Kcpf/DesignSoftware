"""
Escreva uma função que recebe uma matriz de tamanho 3×3 e devolve o maior valor absoluto dentre todos os seus elementos. A matriz é representada por uma lista de listas. Exemplo: a lista [[1, 2, 3], [4, 5, 6], [7, 8, 9]] representa a matriz

Curiosidade: o maior valor absoluto encontrado em uma matriz é conhecido como a norma infinito dessa matriz.

O nome da sua função deve ser encontra_maximo.
"""

def encontra_maximo(matriz):
    maximo = abs(matriz[0][0])
    for c in matriz:
        for i in c:
            if abs(i) > maximo:
                maximo = abs(i)
    return maximo
