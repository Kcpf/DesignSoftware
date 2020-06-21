"""
Faça uma função que recebe 4 números, 
x1, x2, y1, y2, e devolve a distância entre os pontos 

O nome da sua função deve ser distancia_euclidiana.
"""

import math
def distancia_euclidiana(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)