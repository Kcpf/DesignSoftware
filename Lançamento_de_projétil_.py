"""
Faça uma função que calcule a distância alcançada por um projétil lançado com velocidade v em um ângulo θ, de uma altura y0. A distância é dada pela fórmula: d=v22g(1+√1+2gy0v2(sin(θ))2)sin(2θ)Use g=9.8.

O nome da sua função deve ser calcula_distancia_do_projetil.
"""

import math

g= 9.8

def calcula_distancia_do_projetil(v, teta, y):
    return ((v**2)/(2*g))*(1 + math.sqrt(1 + ((2*g*y)/((v**2)*(math.sin(teta)**2)))))*math.sin(2*teta)