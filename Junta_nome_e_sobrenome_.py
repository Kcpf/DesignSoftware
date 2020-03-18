def junta_nome_sobrenome(nomes, sobrenomes):
    lista = []
    for c in range(len(nomes)):
        lista.append(nomes[c] + " " + sobrenomes[c])
    return lista