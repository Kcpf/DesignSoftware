def inverte_dicionario(dic):
    d = {}
    for each in dic:
        if dic[each] not in d:
        	d[dic[each]] = []
        d[dic[each]].append(each)
    return d