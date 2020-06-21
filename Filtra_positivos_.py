"""
Faça uma função que recebe uma lista de números reais e retorna uma nova lista contendo apenas os números estritamente positivos da lista original.

O nome da sua função deve ser filtra_positivos.
"""

def filtra_positivos(l):
    return list(filter(lambda x: x > 0, l))