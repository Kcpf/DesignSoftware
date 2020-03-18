def conta_bigramas(s):
    dic = {}
    for c in range(0, len(s)):
        if len(s[c:c+2]) == 2:
            if s[c:c+2] not in dic:
            	dic[s[c:c+2]] = 1
            else:
                dic[s[c:c+2]] += 1
            
    return dic

