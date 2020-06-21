"""
Escreva uma função que recebe um número inteiro devolva a raiz_quadrada dele, para fazer essa conta use a estratégia de subtrações sucessivas. Suponha que o número informado é positivo e vai levar a uma raiz quadrada exata, ou seja não vai ser um número "quebrado". Para fazer esse cálculo, faça subtrações sucessiva dos números impares do valor pedido, o número de vezes é o valor desejado. Mais informações em: https://www.youtube.com/watch?v=w-tLphmhxkg

O nome da sua função deve ser raiz_quadrada.
"""

def raiz_quadrada(n):
    cont = 0
    sub = 1
    while n != 0:
        n -= sub
        sub += 2
        cont += 1
    return cont