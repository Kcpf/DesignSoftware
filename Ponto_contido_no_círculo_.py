"""
Crie uma classe chamada Circulo que tem na construção (no init ) um ponto como centro e um float como raio. Adicione um método contem(self, ponto) que avalia se um ponto está dentro da área do círculo ou não.

Pontos são representados por objetos da classe Ponto, especificada a seguir. Você não precisa implementar a classe Ponto.

class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
"""

import math
class Circulo:
    def __init__(self, p, r):
        self.p = p
        self.r = r
    def contem(self, ponto):
        distancia = math.sqrt((ponto.x - self.p.x)**2 + (ponto.y-self.p.y)**2)
        return distancia <= self.r