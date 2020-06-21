"""
Faça uma função que recebe um número inteiro n e devolve uma lista contendo os n primeiros números da sequência de Fibonacci. 
O n-ésimo número da sequência de Fibonacci, definido como Fn, é dado por:

Fn=Fn−1+Fn−2 

Com valores iniciais: F1=1 e F2=1.

Ou seja, a sequência de Fibonacci é:

1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,1597,2584,…

O nome da sua função deve ser calcula_fibonacci.
"""

def calcula_fibonacci(n):
    if n == 1:
        return [1]
    lista = [1,1]
    for c in range(2, n):
        lista.append(lista[c-1] + lista[c-2])
    return lista