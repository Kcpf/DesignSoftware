"""
Faça uma função que recebe uma lista de números e retorna a string 'crescente', 'decrescente' ou 'nenhum' se ela for, respectivamente, estritamente crescente, estritamente decrescente, ou nenhum dos dois (em algumas partes é crescente e em outras é decrescente). Se a lista tiver menos de dois elementos ela deve retornar obrigatoriamente 'nenhum'.

O nome da sua função deve ser classifica_lista.
"""

def classifica_lista(l):
    if len(l) < 2:
        return "nenhum"
    lista = []
    for e in range(1, len(l)):
        if l[e] > l[e-1]:
            lista.append(1)
        elif l[e] < l[e-1]:
            lista.append(-1)
    
    if 1 in lista and -1 in lista:
        return "nenhum"
    elif 1 in lista:
        return "crescente"
    else:
        return "decrescente"