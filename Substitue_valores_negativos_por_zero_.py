def zera_negativos(lista):
    for j, each in enumerate(lista):
        if each < 0:
            lista[j] = 0
    return lista