"""
O valor de π pode ser aproximado a partir da seguinte fórmula: π=√6/1^2+6/2^2+6/3^2+⋯+6/n^2

Faça uma função que recebe o valor de n e retorna o resultado da fórmula acima utilizando os n termos.

O nome da sua função deve ser calcula_pi.
"""

def calcula_pi(n):
    soma = 0
    for number in range(1, n+1):
        soma += 6/(number**2)
        
    return soma**0.5