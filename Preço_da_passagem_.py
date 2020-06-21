"""
Escreva um programa que pergunta a distância que um passageiro deseja percorrer em km. Seu programa deve imprimir o preço da passagem, cobrando R$0.50 por km para viagens de até 200km e R$0.45 por quilômetro extra para viagens mais longas. (Adaptado do ex. 4.6 livro Nilo Ney).

O resultado deve ser impresso com exatamente duas casas decimais.
"""

distancia = float(input())
if distancia <= 200:
    print("{:.2f}".format(distancia*0.5))
else:
    print("{:.2f}".format(100 + (distancia-200)*0.45))
