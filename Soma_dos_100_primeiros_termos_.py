"""
Some os 100 primeiros termos da expressão abaixo usando while e imprima o resultado:

1+1/2+1/2^2+1/2^3+⋯+1/2^99
"""

def soma(n):
    if n == 0:
        return 1
    else:
        return 1/2**n + soma(n-1)

print(soma(99))