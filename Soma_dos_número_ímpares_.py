"""
Faça uma função que recebe uma lista de números e devolve a soma dos números ímpares contidos nela.

O nome da sua função deve ser soma_impares.
"""

def soma_impares(lista):
    soma = 0
    for c in lista:
        if c%2!=0:
            soma += c
    return soma

def soma_impares2(lista):
    return sum(list(filter(lambda x: x % 2 != 0, lista)))
