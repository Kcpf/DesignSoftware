import math
def calcula_tempo(d):
    dic = {}
    for each in d:
        dic[each] = math.sqrt(200/d[each])
    return dic

d = {}
nome = input()
aceleracao= int(input())

while True:
    d[nome] = aceleracao
    nome = input()
    if nome == "sair":
        break
    aceleracao = int(input())

dic = calcula_tempo(d)
tempMin = 100000000
pessoa = ""
for c in dic:
    if tempMin > dic[c]:
        tempMin = dic[c]
        pessoa = c

print(f'O vencedor é {pessoa} com tempo de conclusão de {dic[pessoa]} s')
