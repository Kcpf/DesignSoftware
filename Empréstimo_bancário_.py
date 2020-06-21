"""
Escreva um programa para aprovar o empréstimo bancário para compra de uma casa. O programa deve perguntar o valor da casa a comprar, o salário e a quantidade de anos a pagar. O valor da prestação mensal não pode ser superior a 30% do salário. Calcule o valor da prestação como sendo o valor da casa a comprar dividido pelo número de meses a pagar. (Ex. 4.9 livro Nilo Ney)

Seu programa deve imprimir somente 'Empréstimo não aprovado' ou 'Empréstimo aprovado'.
"""

valor = float(input())
salario = float(input())
anos = float(input())

prestacao = valor/(12*anos)
if prestacao > salario*0.3:
    print("Empréstimo não aprovado")
else:
    print('Empréstimo aprovado')