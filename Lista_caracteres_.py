"""
Faça uma função que recebe uma senha (string) e devolve uma string do mesmo tamanho da senha formada somente por asteriscos ('*').

O nome da sua função deve ser esconde_senha.
"""

def lista_caracteres(s):
    return list(set(filter(lambda x: x[0], s)))

#def lista_caracteres(s):
#    lista = []
#    for c in s:
#        if c not in lista:
#            lista.append(c)
#    return lista