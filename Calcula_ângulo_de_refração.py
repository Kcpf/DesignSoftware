"""
A lei de Snell-Descartes define que a relação entre o ângulo de incidência e o ângulo de refração de um raio de luz atravessando de um meio para o outro é inversamente proporcional a razão dos índices de refração dos meios, que é dado pela seguinte fórmula:

n1n2=sen(θ2)sen(θ1)

Faça uma função que recebe os valores de n1, n2 e θ1 e retorna o valor do θ2. Os valores passados de n1, n2 são adimensionais, já os valores de θ1 e θ2 deverão ser recebidos e retornados em graus.

O nome da sua função deve ser snell_descartes.
"""

import math
def snell_descartes(n1, n2, teta1):
    return math.degrees(math.asin((n1*math.sin(math.radians(teta1)))/n2))