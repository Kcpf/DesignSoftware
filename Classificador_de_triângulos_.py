"""
Faça uma função que recebe os lados de um triângulo e retorna se ele é equilátero, isósceles ou escaleno. Sua função deve retornar a string "equilátero", "isósceles", ou "escaleno". Assuma que os lados do triângulo são válidos.

O nome da sua função deve ser classifica_triangulo.
"""

def classifica_triangulo(lado1, lado2, lado3):
    if lado1==lado2==lado3:
        return "equilátero"
    elif lado1==lado2 or lado1==lado3 or lado2==lado3:
        return "isósceles"
    else:
        return "escaleno"