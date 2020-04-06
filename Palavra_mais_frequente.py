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
    