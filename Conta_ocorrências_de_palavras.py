def conta_ocorrencias(l):
    dic = {}
    for each in l:
        if each not in dic:
            dic[each] = 0
        dic[each] += 1
    return dic