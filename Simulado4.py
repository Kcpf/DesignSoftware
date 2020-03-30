import random

din = 100
while din != 0:
    print(din)
    valor = float(input())
    if valor == 0:
        break
    
    aposta = input()
    numSorteado = random.randint(0, 36)
    
    if aposta == "n":
        numAposta = int(input())
        if numAposta == numSorteado:
            din += valor*35
        else:
            din -= valor
    else:
        parOuImpar = input()
        if (parOuImpar == 'p' and numSorteado % 2 == 0) or (parOuImpar == "i" and numSorteado % 2 != 0):
            din += valor
        else:
            din -= valor