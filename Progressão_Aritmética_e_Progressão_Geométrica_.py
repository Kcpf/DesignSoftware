"""
Escreva uma função que recebe uma lista de números e devolve "PA", se ela for uma progressão aritmética, "PG", se for uma progressão geométrica, e "NA" se não for nenhuma das duas. Caso a sequência seja tanto uma PA quanto uma PG, devolva "AG".

O nome da sua função deve ser verifica_progressao.
"""

def verifica_progressao(l):
    listaq = []
    listar = []
    q = 0
    r = 0
    for c in range(1, len(l)):
        if c == 1:
            if l[c-1] == 0:
                q = 0
            else:
                q = l[c]/l[c-1]
            r = l[c] - l[c-1]
        else:
            if l[c]/l[c-1] == q:
                listaq.append(True)
            else:
                listaq.append(False)
            if l[c]-l[c-1] == r:
                listar.append(True)
            else:
                listar.append(False)
    if False in listaq and False in listar:
        return "NA"
    elif False in listaq and True in listar:
        return "PA"
    elif True in listaq and False in listar:
        return "PG"
    return "AG"