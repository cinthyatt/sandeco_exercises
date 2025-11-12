class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def exibir_descricao(self):
        print(f'O carro é da marca {self.marca}, modelo {self.modelo} e foi fabricado no ano {self.ano}.')

c1 = Carro("Fiat", "Argo", 2024)
c2 = Carro("Mercedes", "A200", 2020)
c3 = Carro("Tesla", "Model S", 2025)

c1.exibir_descricao()
c2.exibir_descricao()
c3.exibir_descricao()

