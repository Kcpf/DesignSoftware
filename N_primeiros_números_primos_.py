"""
Escreva uma função que recebe um número n e retorna uma lista com os n primeiros números primos em ordem crescente (adaptado do Ex. 5.24 do livro do Nilo Ney).

O nome da sua função deve ser lista_primos.
"""
def eh_primo(n):
    if n == 0 or n==1:
        return False
    for c in range(2, n):
        if c % 2 != 0 or c == 2:
            if n % c == 0:
                return False
    return True

def lista_primos(n):
    cont = 0
    lista = []
    i = 2
    while cont < n:
        if eh_primo(i):
            lista.append(i)
            cont += 1
        i += 1
    return lista