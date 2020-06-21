"""
Faça uma função que recebe uma string composta somente por letras minúsculas e a devolve removendo as vogais.

O nome da sua função deve ser remove_vogais.
"""

def remove_vogais(s):
    string = ""
    vogais = ["a", "e", "i", "o", "u"]
    for c in s:
        if c not in vogais:
            string += c
    return string