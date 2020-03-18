def calcula_fibonacci(n):
    if n == 1:
        return [1]
    lista = [1,1]
    for c in range(2, n):
        lista.append(lista[c-1] + lista[c-2])
    return lista