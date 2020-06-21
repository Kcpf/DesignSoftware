"""
Escreva uma função que recebe um número e verifica se é ou não um número primo. Para fazer essa verificação, calcule o resto da divisão do número por 2 e depois por todos os números ímpares até o número recebido. Se o resto de uma dessas divisões for igual a zero, o número não é primo. Observe que 0 e 1 não são primos e que 2 é o único número primo que é par (adaptado do Ex. 5.23 livro do Nilo Ney).

Sua função deve retornar True ou False.

Observação: este exercício vai te ajudar nos exercícios 32, 33, 34, 51 e 75 ;)

O nome da sua função deve ser eh_primo.
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