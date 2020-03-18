def soma_impares(lista):
    soma = 0
    for c in lista:
        if c%2!=0:
            soma += c
    return soma