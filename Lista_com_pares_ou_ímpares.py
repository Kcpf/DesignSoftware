"""
Faça uma função que recebe uma lista de números e retorna a string 'ímpar', 'par' ou 'misturado' se ela tiver, respectivamente, só números ímpares, só números pares, ou números dos dois tipos. Se a lista for vazia ela deve retornar misturado.

O nome da sua função deve ser verifica_lista.
"""

def verifica_lista(num):
    lista = []
    for each in num:
        if each % 2 == 0:
            lista.append(0)
        else:
            lista.append(1)
    if sum(lista) == 0 and len(lista)!= 0:
        return "par"
    elif sum(lista) == len(lista) and len(lista)!= 0:
        return 'ímpar'
    else:
        return "misturado"