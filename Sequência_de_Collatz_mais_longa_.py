contMaior = 0
numMaior = 0
for c in range(1000):
    i = c
    cont = 0
    while i > 1:
        if i%2==0:
            i = i/2
        else:
            i = 3*i + 1
        cont += 1
    if cont > contMaior:
        contMaior = cont
        numMaior = c
print(numMaior)