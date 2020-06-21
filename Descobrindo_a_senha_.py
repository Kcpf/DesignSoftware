"""
Escreva um programa que pergunta uma palavra para o usuário até que ele acerte a senha ("desisto"). Quando o usuário acertar a senha, imprima "Você acertou a senha!".
"""

palavra = input()

while palavra != "desisto":
    palavra = input()

print("Você acertou a senha!")