"""
Faça uma função que recebe uma lista de números e devolve um dicionário no qual as chaves são os números da lista e os valores são um booleano indicando se aquele número é primo ou não.

O nome da sua função deve ser verifica_primos.
"""

def eh_primo(n):
    if n <= 1:
        return False
    for c in range(2, n):
        if c % 2 != 0 or c == 2:
            print(c)
            if n % c == 0:
                return False
    return True

def verifica_primos(l):
    dic = {}
    for each in l:
        dic[each] = eh_primo(each)
    return dic