class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def calcular_area(self):
        area = self.largura * self.altura
        return f'A área do retângulo de {self.largura}m X {self.altura}m é {area}m.'

r1 = Retangulo(5, 3)
r2 = Retangulo(3, 7)

print(r1.calcular_area())
print(r2.calcular_area())
