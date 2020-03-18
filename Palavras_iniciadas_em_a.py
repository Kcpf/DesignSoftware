lista = []
palavra = input()

while palavra != 'fim':
    lista.append(palavra)
    palavra = input()

for each in lista:
    if each[0] == 'a':
        print(each)