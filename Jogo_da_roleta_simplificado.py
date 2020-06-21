"""
Faça um programa em Python que implementa o jogo da roleta simplificado, o usuário começa com 100 dinheiros, e o programa fica em loop até que o dinheiro acabe:

O programa mostra a quantidade de dinheiro disponível (obrigatório o uso de print)
O usuário aposta um valor (se o valor for zero o programa para)
Posteriormente o programa pergunta se a aposta é em um número ou paridade (par/ímpar)
Se o usuário digitar a opção 'n' o usuário digita o número de 1 a 36, caso ganhe ele recebe 35 vezes o que apostou. Por exemplo, se ele tinha 
100 e apostou 10 ele passará a ter 100+35⋅10=450, se ganhar, ou 100−10=90, se perder.
Se o usuário digitar a opção 'p' o usuário escolhe se par (opção 'p') ou ímpar (opção 'i'), caso ganhe ele recebe o mesmo que apostou.

Por exemplo, se ele tinha 100 e apostou 10 ele passará a ter 100+10=110, se ganhar, ou 100−10=90, se perder.
Será feito um sorteio de 0 (zero) a 36 (trinta e seis) e na sequência o pagamento das apostas
Utilize a função random.randint.
"""

import random

din = 100
while din != 0:
    print(din)
    valor = float(input())
    if valor == 0:
        break
    
    aposta = input()
    numSorteado = random.randint(0, 36)
    
    if aposta == "n":
        numAposta = int(input())
        if numAposta == numSorteado:
            din += valor*35
        else:
            din -= valor
    else:
        parOuImpar = input()
        if (parOuImpar == 'p' and numSorteado % 2 == 0) or (parOuImpar == "i" and numSorteado % 2 != 0):
            din += valor
        else:
            din -= valor