def primeiras_ocorrencias(s):
    dic = {}
    for each in s:
        if each not in dic:
            dic[each] = s.index(each)
    return dic