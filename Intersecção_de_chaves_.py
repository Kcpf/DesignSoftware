def interseccao_chaves(dic1, dic2):
    lista = []
    for c in dic1:
        if c in dic2:
            lista.append(c)
    return lista