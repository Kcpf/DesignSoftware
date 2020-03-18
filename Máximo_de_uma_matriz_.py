def encontra_maximo(matriz):
    maximo = abs(matriz[0][0])
    for c in matriz:
        for i in c:
            if abs(i) > maximo:
                maximo = abs(i)
    return maximo
