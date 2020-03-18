def eh_primo(n):
    if n == 0 or n==1:
        return False
    for c in range(2, n):
        if c % 2 != 0 or c == 2:
            if n % c == 0:
                return False
    return True

def maior_primo_menor_que(n):
    for c in range(n, 0, -1):
        if eh_primo(c):
            return c
    return -1