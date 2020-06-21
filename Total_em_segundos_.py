"""
Escreva um programa que pergunte, em sequência, uma quantidade de dias, horas, minutos e segundos para o usuário. Depois calcule o total em segundos e imprima.
"""

dias = float(input())
horas = float(input())
minutos = float(input())
segundos = float(input())

print(dias*86400+horas*3600+minutos*60+segundos)