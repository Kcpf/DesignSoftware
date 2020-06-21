"""
Faça uma função que recebe um dicionário com os nomes de estados do Brasil, onde cada entrada possui um outro dicionário com os municípios e sua quantidade de habitantes, e retorna o nome do estado mais populoso de todos. Abaixo está um exemplo bem resumido:

brasil = {
    "São Paulo": {"São Paulo": 21571281, "Campinas": 3224443},
    "Minas Gerais": {"Belo Horizonte": 2385639, "Uberlândia": 611903},
}
O nome da sua função deve ser mais_populoso.
"""

def mais_populoso(dic):
    d = {}
    for each in dic:
        d[each] = sum(dic[each].values())
    
    return list({k: v for k, v in sorted(d.items(), key=lambda item: item[1])})[-1]