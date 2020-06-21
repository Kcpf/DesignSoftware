"""
Faça uma função que recebe um dicionário cujas chaves são nomes de pessoas e os valores são as respectivas datas de nascimento no formato 'dd/mm/aaaa', onde dd são dois caracteres representando o dia, mm são dois caracteres representando o mês e aaaa são quatro caracteres representando o ano. A função deve devolver um novo dicionário contendo somente os dados (nome e data de nascimento) dos aniversariantes de setembro.

O nome da sua função deve ser aniversariantes_de_setembro.
"""

def aniversariantes_de_setembro(d):
    dic = {}
    for each in d:
        if d[each][3:5] == '09':
            dic[each] = d[each]
    return dic