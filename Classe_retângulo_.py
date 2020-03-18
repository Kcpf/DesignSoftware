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