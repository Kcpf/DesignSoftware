"""
Crie um programa que pergunta o nome do mês e imprime o número do mês (use os nomes dos meses com letra minúscula).
"""

lista = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
nome = input()
print(lista.index(nome)+1)