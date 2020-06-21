"""
Faça uma função que recebe uma lista de palavras e retorna a palavra mais frequente. Por exemplo, para a lista

['abobora', 'chuchu', 'abobora', 'abobora', 'chuchu’]
sua função deve retornar 'abobora'.

Dica: se você não resolveu o exercício 146. Conta ocorrências de palavras, resolva-o primeiro e utilize-o como função auxiliar para este exercício (cole o código nesta solução).

O nome da sua função deve ser mais_frequente.
"""

def conta_ocorrencias(l):
    dic = {}
    for each in l:
        if each not in dic:
            dic[each] = 0
        dic[each] += 1
    return dic

def mais_frequente(l):
    dic = conta_ocorrencias(l)
    cont = 0
    resultado = ""
    for each in dic:
        if dic[each] > cont:
            resultado = each
            cont = dic[each]
    return resultado
    