"""
Escreva uma função que recebe uma string e devolve uma lista com todos os seus bigramas. Um bigrama é qualquer sequência de dois caracteres. Ex: para a string 'babador' a sua função deve devolver a lista ['ba', 'ab', 'ad', 'do', 'or']. Note que cada bigrama deve aparecer somente uma vez na lista.

Curiosidade: bigramas são usados em sistemas de entrada de texto (teclados) para predizer a próxima letra mais provável.

O nome da sua função deve ser acha_bigramas.
"""

def acha_bigramas(s):
    lista = []
    for c in range(0, len(s)):
        if s[c:c+2] not in lista:
            if len(s[c:c+2]) == 2:
                lista.append(s[c:c+2])
    return lista