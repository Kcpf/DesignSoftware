"""
Faça uma função que recebe duas listas com informações de uma nota fiscal e devolve o preço total da nota. A nota fiscal é representada pelas duas listas, uma com preços de produtos e outra com a respectiva quantidade de itens comprados daquele produto.

O nome da sua função deve ser calcula_total_da_nota.
"""

def calcula_total_da_nota(inf1, inf2):
    total = 0
    for c in range(len(inf1)):
        total += inf1[c]*inf2[c]
    return total