"""
Faça uma função que recebe duas listas, uma de nomes e outra com os respectivos sobrenomes, e devolve uma nova lista com os nomes e sobrenomes em uma única string. Coloque exatamente um espaço entre o nome e o sobrenome.

O nome da sua função deve ser junta_nome_sobrenome.
"""

def junta_nome_sobrenome(nomes, sobrenomes):
    lista = []
    for c in range(len(nomes)):
        lista.append(nomes[c] + " " + sobrenomes[c])
    return lista