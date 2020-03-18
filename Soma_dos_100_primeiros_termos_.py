def soma(n):
    if n == 0:
        return 1
    else:
        return 1/2**n + soma(n-1)

print(soma(99))