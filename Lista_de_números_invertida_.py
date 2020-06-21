"""
Crie um programa que pede ao usuário que digite números inteiros positivos e armazene-os em uma lista, até que o usuário digite um número negativo ou zero. Em seguida, imprima os números digitados na ordem reversa.
"""

num = int(input())
lista = []

while num > 0:
    lista.append(num)
    num = int(input()) 

print(lista[::-1])