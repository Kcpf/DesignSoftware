"""
Considere a seguinte sequência iterativa definida para os números inteiros positivos:
n→n/2 (n é par) 
n→3n+1(n é ímpar)
Usando a regra acima e começando com o número 13, geramos a seguinte sequência:

13→40→20→10→5→16→8→4→2→1

Percebe-se que essa sequência (começando em 13 e terminando em 1) contém 10 termos. Apesar de ainda não ter sido provado (Problema de Collatz), acredita-se que a sequência sempre termina em 1, independentemente do número inicial.

Faça um programa que determina qual número positivo inicial menor que 1000 gera a sequência de Collatz mais longa. Seu programa deve imprimir esse número.

Nota: Uma vez que a sequência começa os números podem passar de 1000.

Adaptado de https://projecteuler.net/problem=14
"""

contMaior = 0
numMaior = 0
for c in range(1000):
    i = c
    cont = 0
    while i > 1:
        if i%2==0:
            i = i/2
        else:
            i = 3*i + 1
        cont += 1
    if cont > contMaior:
        contMaior = cont
        numMaior = c
print(numMaior)