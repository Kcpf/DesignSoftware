def inverte_lista(lista):
    resp = []
    for c in range(len(lista)-1, -1, -1):
        resp.append(lista[c])
    return resp
