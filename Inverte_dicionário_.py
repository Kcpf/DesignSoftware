"""
Escreva uma função que recebe um dicionário cujas chaves são nomes de pessoas (strings) e os valores são suas respectivas idades (números inteiros). A função deve devolver um novo dicionário cujas chaves são idades e os valores são listas de strings com os nomes das pessoas que têm aquela idade. Exemplo:

Entrada: {'Ana': 19, 'Bruno': 18, 'João': 19}

Saída: {18: ['Bruno'], 19: ['Ana', 'João']}

O nome da sua função deve ser inverte_dicionario.
"""

def inverte_dicionario(dic):
    d = {}
    for each in dic:
        if dic[each] not in d:
        	d[dic[each]] = []
        d[dic[each]].append(each)
    return d