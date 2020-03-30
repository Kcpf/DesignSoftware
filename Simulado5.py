def subtracao_de_listas(lista1, lista2):
    return list(filter(lambda x: x not in lista2, lista1))