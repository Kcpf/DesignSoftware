"""
Faça uma função que recebe uma lista e decide se a lista é estritamente crescente. Em caso positivo a função deve devolver True, em caso negativo, False.

O nome da sua função deve ser eh_crescente.
"""

def eh_crescente(lista):
    for c in range(1, len(lista)):
        if lista[c] <= lista[c-1]:
            return False
    return True