"""
Faça uma função que recebe uma lista e devolve a lista invertida. Observação: a sua solução não pode usar slicing ou alguma outra função pronta do Python.

O nome da sua função deve ser inverte_lista.
"""

def inverte_lista(lista):
    resp = []
    for c in range(len(lista)-1, -1, -1):
        resp.append(lista[c])
    return resp
