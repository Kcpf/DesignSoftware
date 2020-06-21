"""
Escreva uma função que recebe um valor de distância, em km, percorrida por um veículo e o tempo gasto, em horas, para percorrer esta distância. 
A função retorna a velocidade média do veículo em km/h.

O nome da sua função deve ser calcula_velocidade_media.
"""


def calcula_velocidade_media(distancia, tempo):
    if distancia == 0 or tempo == 0:
        return 0
    return (distancia/tempo)