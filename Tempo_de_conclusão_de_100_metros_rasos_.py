import math
def calcula_tempo(d):
    dic = {}
    for each in d:
        dic[each] = math.sqrt(200/d[each])
    return dic