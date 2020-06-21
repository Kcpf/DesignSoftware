"""
Existe uma suspeita do laboratório SpuriousCorrelations de que a letra inicial do nome de um aluno influencia em seu desempenho acadêmico. Faça uma função que recebe um dicionário de notas cujas chaves são os nomes dos alunos. A função deve devolver um novo dicionário com as médias das notas dos alunos para cada letra inicial. Exemplo:

Entrada: {'Andrew Ayres': 6, 'Fábio Ikeda': 10, 'Fábio Kurauchi': 9, 'Raul Hage': 8}

Saída: {'A': 6, 'F': 9.5, 'R': 8}

O nome da sua função deve ser medias_por_inicial.
"""

def medias_por_inicial(dic):
    d = {}
    for each in dic:
        if each[0] in d:
            d[each[0]] = (d[each[0]]+dic[each])/2
        else:
            d[each[0]] = dic[each]
    return d

print(medias_por_inicial({'Andrew Ayres': 6, 'Fábio Ikeda': 10, 'Fábio Kurauchi': 9, 'Raul Hage': 8}))