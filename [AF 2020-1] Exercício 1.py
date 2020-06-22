"""
Faça um programa que lê um arquivo chamado criptografado.txt e imprime o seu conteúdo descriptografado utilizando a lógica a seguir:

Todas as ocorrências da letra 's' devem ser substituídas pela letra 'z';
Todas as ocorrências da letra 'a' devem ser substituídas pela letra 'e';
Todas as ocorrências da letra 'r' devem ser substituídas pela letra 'b';
Todas as ocorrências da letra 'b' devem ser substituídas pela letra 'r';
Todas as ocorrências da letra 'e' devem ser substituídas pela letra 'a';
Todas as ocorrências da letra 'z' devem ser substituídas pela letra 's'.

Por exemplo, se o conteúdo do arquivo criptografado.txt for:

    milho da pipoce qua neo pezze palo fogo continue e zab milho da pipoce, pebe zampba.
    ezzim econtaca com e ganta.
    ez gbendaz tbenzfobmecoaz econtacam quendo pezzemoz palo fogo.
    quam neo pezze palo fogo fice do mazmo jaito, e vide intaibe.
    buram elvaz
As seguintes linhas devem ser impressas (usar um print por linha):

    milho de pipoca que nao passa pelo fogo continua a ser milho de pipoca, para sempre.
    assim acontece com a gente.
    as grandes transformacoes acontecem quando passamos pelo fogo.
    quem nao passa pelo fogo fica do mesmo jeito, a vida inteira.
    rubem alves

O texto contém apenas letras minúsculas.

"""

with open("criptografado.txt", "r") as file:
    conteudo = file.read().split("\n") # Aqui é uma quebra de linha
    for frase in conteudo:
        frase_descripto = ""
        for letra in frase:
            if letra == "s":
                frase_descripto += "z"
            elif letra == "a":
                frase_descripto += "e"
            elif letra == "r":
                frase_descripto += "b"
            elif letra == "b":
                frase_descripto += "r"
            elif letra == "e":
                frase_descripto += "a"
            elif letra == "z":
                frase_descripto += "s"
            else:
                frase_descripto += letra
        print(frase_descripto)