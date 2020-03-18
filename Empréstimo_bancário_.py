valor = float(input())
salario = float(input())
anos = float(input())

prestacao = valor/(12*anos)
if prestacao > salario*0.3:
    print("Empréstimo não aprovado")
else:
    print('Empréstimo aprovado')