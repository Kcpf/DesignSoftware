import math
class Circulo:
    def __init__(self, p, r):
        self.p = p
        self.r = r
    def contem(self, ponto):
        distancia = math.sqrt((ponto.x - self.p.x)**2 + (ponto.y-self.p.y)**2)
        return distancia <= self.r