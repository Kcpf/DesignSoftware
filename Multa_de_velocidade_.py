velocidade = float(input())
if velocidade > 80:
    print("você ultrapassou a velocidade")
    print("{:.2f}".format((velocidade - 80)*5))
else:
    print('Não foi multado')
