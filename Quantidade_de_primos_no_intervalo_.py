"""
Escreva uma função que recebe dois números a e b e devolve a quantidade de números de primos p tais que a≤p≤b.

O nome da sua função deve ser primos_entre.
"""
def eh_primo(n):
    if n == 0 or n==1:
        return False
    for c in range(2, n):
        if c % 2 != 0 or c == 2:
            if n % c == 0:
                return False
    return True

def primos_entre(a, b):
    num = 0
    for c in range(a, b+1):
        if eh_primo(c):
            num += 1
    return num