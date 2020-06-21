"""
Faça uma função que recebe uma string e retorna um dicionário com o número de ocorrências de cada bigrama (par de caracteres) dessa string. Exemplo:

Entrada: 'banana nanica'

Saída: {'ba': 1, 'an': 3, 'na': 3, 'a ': 1, ' n': 1, 'ni': 1, 'ic': 1, 'ca': 1}

O nome da sua função deve ser conta_bigramas.
"""

def conta_bigramas(s):
    dic = {}
    for c in range(0, len(s)):
        if len(s[c:c+2]) == 2:
            if s[c:c+2] not in dic:
            	dic[s[c:c+2]] = 1
            else:
                dic[s[c:c+2]] += 1
            
    return dic

