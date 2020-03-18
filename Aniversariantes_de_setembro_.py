def aniversariantes_de_setembro(d):
    dic = {}
    for each in d:
        if d[each][3:5] == '09':
            dic[each] = d[each]
    return dic