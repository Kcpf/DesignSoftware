"""
Faça uma função que recebe uma string contendo um e-mail válido e retorne o nome do usuário. Dica: use a função do exercício 62.

O nome da sua função deve ser nome_usuario.
"""

def nome_usuario(s):
    return s[:s.index("@")]