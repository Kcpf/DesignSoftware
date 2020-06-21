"""
Escreva um programa que calcule a redução de tempo de vida de um fumante a partir do número de cigarros. Pergunte quantos cigarros ele fuma por dia e há quantos anos fuma. Imprima o tempo de vida perdido em dias. Considere que um cigarro rouba 10 minutos de expectativa de vida.
"""
cigarros = int(input())
anos = float(input())
cig = 365*anos*cigarros
print((cig*10)/1440)