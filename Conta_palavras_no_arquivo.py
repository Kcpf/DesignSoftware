"""
Faça um programa que conta e imprime a quantidade de palavras em um arquivo chamado texto.txt (não contar espaços em branco).

Dica: use .split()
"""

with open("texto.txt", "r") as file:
    print(len(file.read().split()))