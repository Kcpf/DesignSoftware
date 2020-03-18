def calcula_total_da_nota(inf1, inf2):
    total = 0
    for c in range(len(inf1)):
        total += inf1[c]*inf2[c]
    return total