def estritamente_crescente(lista):
    resp = [0]
    for c in lista:
        if c > resp[-1:][0]: #Verifica último elemento da lista resp
            resp.append(c)
    return resp[1:]
