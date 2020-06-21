"""
Se pode usar uma série para calcular o valor do e (número de Euler ou Neperiano). Basicamente a ideia é somar uma sequência de número, e conforme se avança na sequência, se chega mais perto do valor desejado. A série de Taylor para calcular 
e x é:
e^x=1+x+x^2/2!+x^3/3!+x^4/4!+x^5/5!+...

Faça uma função em Python que calcula o resultado do e x para uma série de tamanho n. Você pode supor que as entradas para x e n serão enviadas nesta ordem e sempre serão números positivos.

O nome da sua função deve ser calcula_euler.

"""

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
  