"""
Faça uma função que recebe um dicionário no qual as chaves são nomes de pessoas (representados por strings) e os valores são as idades de cada pessoa e retorna um novo dicionário no qual as chaves são faixas etárias e os valores são listas com os nomes das pessoas daquela faixa. Utilize a seguinte classificação:

Faixa etária	Idade
criança	11 anos ou menos
adolescente	Entre 12 e 17 anos
adulto	Entre 18 e 59 anos
idoso	60 anos ou mais
Exemplo:
Para o dicionário {'João': 10, 'Maria': 8, 'Miguel': 20, 'Helena': 67, 'Alice': 50} sua função deve retornar {'criança': ['João', 'Maria'], 'adolescente': [], 'adulto': ['Miguel', 'Alice'], 'idoso': ['Helena']}.

O nome da sua função deve ser agrupa_por_idade.
"""

def agrupa_por_idade(dic):
    faixas_etarias = {"criança": [], "adolescente": [], "adulto": [], "idoso": []}
    for each in dic:
        if dic[each] <= 11:
            faixas_etarias["criança"].append(each)
        elif 11 < dic[each] <= 17:
            faixas_etarias["adolescente"].append(each)
        elif 17 < dic[each] <= 59:
            faixas_etarias["adulto"].append(each)
        else:
            faixas_etarias["idoso"].append(each)
    return faixas_etarias