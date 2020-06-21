"""
Faça um programa que lê os nomes e o valor da aceleração de atletas digitados pelo usuário até que o nome digitado seja 'sair' (nesse caso o usuário digita 'sair' no nome e o programa não deve perguntar a aceleração). O programa deve então usar a função do exercício 77 (repita a função na sua solução) para imprimir o nome do vencedor e o seu tempo de conclusão no formato: 'O vencedor é NOME com tempo de conclusão de TEMPO s' onde NOME é o nome do vencedor e TEMPO é o seu tempo de conclusão.
"""
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
