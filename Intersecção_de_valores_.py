def interseccao_valores(dic1, dic2):
    l = []
    l1 = list(dic1.values())
    l2 = list(dic2.values())
    for c in l1:
        if c in l2:
            l.append(c)
    return l
         