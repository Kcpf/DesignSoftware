def acha_bigramas(s):
    lista = []
    for c in range(0, len(s)):
        if s[c:c+2] not in lista:
            if len(s[c:c+2]) == 2:
                lista.append(s[c:c+2])
    return lista