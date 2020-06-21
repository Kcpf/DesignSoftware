"""
Escreva uma função que recebe uma lista de nomes de alunos e devolve uma lista de trios de alunos (cada trio é uma lista com 3 strings). Os trios são formados por 3 alunos em sequência na lista inicial, ou seja, o primeiro trio é formado pelo 
1o, 2o e 3o alunos, o segundo trio, pelo 4o, 5o e 6o, etc. O último grupo pode ser formado por uma ou duas pessoas caso não haja alunos suficientes para fechar um trio.

Exemplo:

Entrada: ['João', 'Maria', 'Tiago', 'Pedro', 'Julia', 'Laura', 'Alice']
Saída: [['João', 'Maria', 'Tiago'], ['Pedro', 'Julia', 'Laura'], ['Alice']]
O nome da sua função deve ser separa_trios.
"""

def separa_trios(l):
    lista = []
    for c in range(len(l)):
        if c % 3 == 0:
            lista.append(l[c:c+3])
    return lista