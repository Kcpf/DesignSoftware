num = int(input())
lista = []

while num > 0:
    lista.append(num)
    num = int(input()) 

print(lista[::-1])