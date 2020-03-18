def medias_por_inicial(dic):
    d = {}
    for each in dic:
        if each[0] in d:
            d[each[0]] = (d[each[0]]+dic[each])/2
        else:
            d[each[0]] = dic[each]
    return d

print(medias_por_inicial({'Andrew Ayres': 6, 'Fábio Ikeda': 10, 'Fábio Kurauchi': 9, 'Raul Hage': 8}))