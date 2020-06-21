"""
Escreva uma função que recebe um número inteiro n e devolve o maior número primo menor ou igual a n. Caso não haja nenhum número primo que se encaixe nessa situação (ex: números negativos), devolva -1. Dica: Escreva uma função auxiliar que devolve True se o número é primo e False caso contrário.

O nome da sua função deve ser maior_primo_menor_que.
"""

def eh_primo(n):
    if n == 0 or n==1:
        return False
    for c in range(2, n):
        if c % 2 != 0 or c == 2:
            if n % c == 0:
                return False
    return True

def maior_primo_menor_que(n):
    for c in range(n, 0, -1):
        if eh_primo(c):
            return c
    return -1