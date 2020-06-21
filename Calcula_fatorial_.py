"""
Escreva uma função que recebe um número n e devolve o valor de n! =1⋅2⋅3⋅⋯⋅n.

O nome da sua função deve ser fatorial.
"""

def fatorial(n):
    if n == 1:
        return 1
    else:
        return n*fatorial(n-1)