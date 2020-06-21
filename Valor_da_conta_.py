"""
Escreva um programa que pergunta para o usuário o valor da conta do restaurante e imprime: "Valor da conta com 10%: R$ X.YZ", onde X.YZ é um número com exatamente duas casas decimais.
"""

valor = float(input())
print("Valor da conta com 10%: R$ {:.2f}".format(valor*1.1))