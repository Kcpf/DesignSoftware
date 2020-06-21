"""
Um ângulo crítico de refração é definido quando um feixe de luz que atravessa de um meio de índice de refração maior para um menor é refratado paralelo a superfície. Ângulos de incidência maiores que este, farão a luz refletir internamente de forma total, e não mais refratar.

Faça uma função em Python que recebe os valores de n1, n2 e θ2 e informa se foi uma refração ou reflexão interna, sabendo que o feixe de luz vai do meio 2 para o meio 1. Para isso crie uma função que recebe os valores e retorne verdadeiro caso seja uma reflexão interna total (não inclui o ângulo crítico), ou falso caso seja uma refração. Dica: Um valor de seno maior que 1 (um) indica uma reflexão total interna.

O nome da sua função deve ser reflexao_total_interna.
"""

import math

def reflexao_total_interna(n1, n2, o2):
    if (n2*math.sin(math.radians(o2)))/n1 > 1:
        return True
    return False