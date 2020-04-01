import math

# Exercício 1
def calcula_trabalho(f, teta, s):
    return f*math.cos(math.radians(teta))*s

print(calcula_trabalho(10, 180, 20))

# Exercicio 2
resp = input("Está funcionando? ")

if resp == "s":
    print("Sem problemas")
else:
    resp = input("Você sabe corrigir? (n/s) ")

    if resp == "s":
        print("Sem problemas")
    else:
        resp = input("Você precisa corrigir? (n/s) ")
        
        if resp == "s":
            print("Apague tudo e tente novamente")
        else:
            print("Sem problemas")


# Exercicio 3


def verifica_quadrado_perfeito(n):
    m = n

    cont = 1
    while m > 0:
        m -= 2*cont
        cont += 1
    
    if m**2 == n:
        return True
    
    return False

print(verifica_quadrado_perfeito(49))

# Exercicio 4

def equaliza_imagem(l, k):
    l = list(map(lambda x: x*k, l))
    l = list(map(lambda x: 255 if x > 255 else x, l))
    return l

print(equaliza_imagem([10, 12, 100], 2))

# Exercicio 5

import random

soma_gerada = random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)

dinheiro = 10

def fase_dicas(din):
    while True:
        print(din)

        if din <= 0:
            perdeu = True
            return din, perdeu 
        
        resp = input("Você quer uma dica? ")

        if resp == "sim":
            din -= 1

            soma1 = int(input())
            soma2 = int(input())
            soma3 = int(input())
            
            if soma_gerada in [soma1, soma2, soma3]:
                print("Está entre os 3")
            else:
                print("Não está entre os 3")
        else:
            return din, False


def fase_chutes(din, perdeu):
    if perdeu:
        return din, False
    
    while True:
        print(din)

        if din <= 0:
            return din, False

        chute = int(input("Chute um número: "))

        if chute == soma_gerada:
            din += din*5
            return din, True
        
        din -= 1


dinheiro, perdeu = fase_dicas(dinheiro)
dinheiro, ganhou = fase_chutes(dinheiro, perdeu)

if ganhou:
    print(f"Você ganhou o jogo com {dinheiro} dinheiros!")
else:
    print("Você perdeu!")