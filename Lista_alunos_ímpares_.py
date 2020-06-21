"""
Escreva uma função que recebe uma lista de nomes de alunos e devolve uma lista contendo somente os alunos nos índices ímpares, dividindo a turma em dois.

O nome da sua função deve ser alunos_impares.
"""

def alunos_impares(lista):
    l = []
    for c in range(len(lista)):
        if c % 2 != 0:
        	l.append(lista[c])
    return l
