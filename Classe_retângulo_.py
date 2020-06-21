"""
Crie uma classe Retangulo, com um construtor (__init__) que recebe dois pontos e os armazena como atributos:

Ponto do canto inferior esquerdo
Ponto do canto superior direito
Cada ponto é um objeto do tipo Ponto, como definido à seguir:

class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
Assuma que a classe Ponto já está definida, você só precisa implementar a classe Retangulo.

Sua classe Retangulo deve possuir dois métodos sem argumentos adicionais (lembre-se que métodos sempre recebem self):

calcula_perimetro(self): calcula o perímetro do retângulo;
calcula_area(self): calcula a área do retângulo.
"""

class Retangulo:
    def __init__(self, ci, cs):
        self.ci = ci
        self.cs = cs
    
    def calcula_perimetro(self):
        altura = self.cs.y - self.ci.y
        largura = self.cs.x - self.ci.x
        return 2*altura + 2*largura
    
    def calcula_area(self):
        altura = self.cs.y - self.ci.y
        largura = self.cs.x - self.ci.x
        return altura*largura