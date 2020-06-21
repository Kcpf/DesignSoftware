"""
Foi criado um dicionário em Python para cada turma de design de software, o dicionário possui o nome do aluno e sua média final. Esses dicionários foram colocados em uma lista. Faça uma função recebe essa lista e calcule a média dos alunos de todas as turmas.

Por exemplo:

Para a lista alunos = [ {"aluno1": 5, "aluno2": 8}, {"aluno3": 5} ], a função calcula_media(alunos) retorna o valor 6.0

O nome da sua função deve ser calcula_media.
"""

def calcula_media(lista):
    l = []
    for dic in lista:
        for ele in dic:
            l.append(dic[ele])
    if len(l) != 0:
        return sum(l)/len(l)
    return 0