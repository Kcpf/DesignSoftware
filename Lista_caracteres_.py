def lista_caracteres(s):
    return list(set(filter(lambda x: x[0], s)))

#def lista_caracteres(s):
#    lista = []
#    for c in s:
#        if c not in lista:
#            lista.append(c)
#    return lista