"""
Escreva uma função que recebe um número representando um ano e devolve True se um ano é bissexto e False caso contrário.

O nome da sua função deve ser eh_bissexto.
"""

import calendar
def eh_bissexto(ano):
    return calendar.isleap(ano)