"""
Faça um programa que pergunta logins para o usuário até que ele digite a palavra 'fim'. Para cada login digitado pelo usuário, o programa deve verificar qual é o próximo login disponível no sistema e adicionar esse novo login em uma lista. Ao final do programa, os login devem ser impressos, um por linha, no console.

Utilize a função do Exercício 168.

Exemplo de interação com o programa:

Usuário digita: fabio
Usuário digita: andre
Usuário digita: fabio
Usuário digita: fabio
Usuário digita: fim
Programa imprime: fabio
Programa imprime: andre
Programa imprime: fabio1
Programa imprime: fabio2
A ordem em que os logins são impressos não importa.
"""

def login_disponivel(login, lista_logins):
    cont = 1
    login_ok = login
    while login_ok in lista_logins:
        login_ok = login
        login_ok += str(cont)
        cont += 1
    return login_ok

inp = input()
lista = []

while inp != "fim":
    login = login_disponivel(inp, lista)
    lista.append(login)
    inp = input()

for each in lista:
    print(each)
