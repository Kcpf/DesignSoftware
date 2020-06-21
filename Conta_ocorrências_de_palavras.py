"""
Faça uma função que recebe uma lista de palavras e retorna um dicionário onde as chaves são as palavras, e o valor é a contagem de cada palavra. Por exemplo, se a lista for

['abobora', 'chuchu', 'abobora', 'abobora', 'chuchu']
a função deve retornar {'chuchu': 2, 'abobora': 3}

O nome da sua função deve ser conta_ocorrencias.
"""

def conta_ocorrencias(l):
    dic = {}
    for each in l:
        if each not in dic:
            dic[each] = 0
        dic[each] += 1
    return dic