def numero_no_indice(lista):
    resp = []
    for j, i in enumerate(lista):
        if i == j:
            resp.append(j)
    return resp