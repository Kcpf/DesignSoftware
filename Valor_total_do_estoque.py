"""
Faça um programa que lê um arquivo chamado estoque.json com o estoque de uma empresa no formato JSON (conforme o exemplo abaixo) e imprime o valor total dos produtos nesse estoque.

Por exemplo, para o JSON abaixo:

{"produtos":[ 
        { "produto": "açúcar", "quantidade": 4, "valor": 3.22},
        { "produto": "arroz", "quantidade": 1, "valor": 10.34},
        { "produto": "feijão", "quantidade": 2, "valor": 9.55}
    ]}
Deve imprimir 42.32, pois é o resultado de: 4*3.22 + 1*10.34 + 2*9.55.
"""

import json

custo = 0

with open("estoque.json", "r") as file:
    conteudo = file.read()
    produtos = json.loads(conteudo)["produtos"]
    for each in produtos:
        quantidade = float(each["quantidade"])
        valor = float(each["valor"])
        custo += quantidade*valor

print(custo)