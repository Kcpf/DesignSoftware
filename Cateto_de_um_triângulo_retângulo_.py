"""

Faça uma função que recebe a medida de um dos catetos e da hipotenusa de um triângulo retângulo e devolve o valor do outro cateto.

O nome da sua função deve ser encontra_cateto.

"""
import math
def encontra_cateto(cat, hip):
    return math.sqrt(hip**2 - cat**2)