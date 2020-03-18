def classifica_triangulo(lado1, lado2, lado3):
    if lado1==lado2==lado3:
        return "equilátero"
    elif lado1==lado2 or lado1==lado3 or lado2==lado3:
        return "isósceles"
    else:
        return "escaleno"