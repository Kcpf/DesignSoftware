"""
Sua empresa possui filiais em diversas regiões da cidade e você precisa fazer uma análise simples dos gastos com infraestrutura em cada bairro. Os gastos com infraestrutura nos últimos 12 meses para cada bairro estão disponíveis em um dicionário como o apresentado a seguir (atenção, este é somente um exemplo):

{
    'Bairro 1': [1234.45, 5123.32, 6134.35, 8567.98, 5472.28, 9715.38, 1380.15, 2569.42, 8459.24, 8351.25, 4082.19, 1750.16],
    'Bairro 2': [236.62, 845.52, 475.72, 846.22, 735.34, 846.26, 48.97, 624.37, 375.46, 4568.76, 73.32, 475.74],
    'Bairro 3': [51234.45, 5123.32, 61334.35, 8567.98, 5472.28, 9715.38, 1380.15, 2569.42, 8459.24, 82351.25, 4082.19, 1750.16],
}
Nesse dicionário, as chaves são os nomes dos bairros e os valores são listas com exatamente 12 números, representando o gasto com infraestrutura em cada mês para o respectivo bairro.

Faça uma função que recebe um dicionário de gastos com infraestrutura e devolve o nome do bairro com maior gasto com infraestrutura nos últimos 6 meses. Utilize a função desenvolvida no Exercício 166.

O nome da sua função deve ser bairro_mais_custoso.
"""

def total_do_semestre_por_bairro(dic):
    d = {}
    for each in dic:
         d[each] = sum(dic[each][-6:])
    return d

def bairro_mais_custoso(dic):
    dic = total_do_semestre_por_bairro(dic)
    return list({k: v for k, v in sorted(dic.items(), key=lambda item: item[1])})[-1]