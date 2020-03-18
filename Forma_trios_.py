def separa_trios(l):
    lista = []
    for c in range(len(l)):
        if c % 3 == 0:
            lista.append(l[c:c+3])
    return lista