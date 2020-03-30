def fatorial(x):
    if x == 1:
        return 1
    else:
        return x * fatorial(x-1)

def soma(x, n):
    if n == 1:
        return x
    else:
        return (x**n)/fatorial(n) + soma(x, n-1)

def calcula_euler(x, n):
    return 1 + soma(x, n-1)
  