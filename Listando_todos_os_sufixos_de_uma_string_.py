"""
Escreva uma função que recebe uma string e devolve uma lista com todos os seus sufixos. Um sufixo é qualquer substring que se encontra no final da string original.

Exemplos:

Para a string 'abcde' sua função deve retornar ['abcde', 'bcde', 'cde', 'de', 'e']
Para a string 'banana' sua função deve retornar ['banana', 'anana', 'nana', 'ana', 'na', 'a']
O nome da sua função deve ser lista_sufixos.
"""
def lista_sufixos(s):
    lista = []
    for c in range(0,len(s)):
        lista.append(s[c:])
    return lista    