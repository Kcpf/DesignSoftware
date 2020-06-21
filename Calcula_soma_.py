"""
Escreva um programa que pergunta números para o usuário e, depois que o usuário digita o número 0 (zero), imprime a soma.
"""

inp = float(input())
num = inp

while inp != 0:
    inp = float(input())
    num += inp

print(num)