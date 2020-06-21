"""
Escreva uma função que recebe a idade e verifica se a pessoa pode comprar bebida alcóolica no Brasil e/ou nos EUA, onde somente maiores de 21 anos podem comprar bebida alcóolica. Os possíveis resultados da função são: "Liberado EUA e BRASIL", "Liberado BRASIL" e "Não está liberado".

O nome da sua função deve ser verifica_idade.
"""

def verifica_idade(idade):
    if idade >= 21:
        return "Liberado EUA e BRASIL"
    elif idade >= 18:
        return "Liberado BRASIL"
    else:
        return "Não está liberado"