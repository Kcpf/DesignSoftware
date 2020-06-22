"""
Desenvolva em Python uma classe Foguete. Essa classe deve ser iniciada com a velocidade do foguete em km/h. Supondo agora que o foguete tem uma velocidade constante (desde a partida), crie nessa classe um método atualizar() que recebe como argumento o tempo decorrido em segundos desde a última vez que este método foi invocado, o retorno desse método deve ser a distância total já percorrida pelo foguete, em km.

Exemplos de código usando a classe:

foguete = Foguete(10000)
print(foguete.atualizar(9))
print(foguete.atualizar(18))
Essa execução deveria mostrar na tela os seguintes valores:

25.0
75.0

"""

class Foguete:
    def __init__(self, velocidade):
        self.velocidade = velocidade
        self.distancia = 0
    
    def atualizar(self, tempo_segundos):
        tempo_horas = tempo_segundos/3600
        self.distancia += tempo_horas*self.velocidade
        return self.distancia
        