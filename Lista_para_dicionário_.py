def monta_dicionario(lista1, lista2):
    dic = {}
    for c in range(len(lista1)):
        dic[lista1[c]] = lista2[c]
    return dic