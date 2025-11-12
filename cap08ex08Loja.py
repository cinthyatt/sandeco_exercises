class Loja:
    def __init__(self):
        self.estoque = {}
        
    def adicionar_produtos(self, produto, quantidade):
        if produto in self.estoque:
            self.estoque[produto] += quantidade
        else: 
            self.estoque[produto] = quantidade
        
    def vender(self, produto, quantidade):
        if produto in self.estoque: 
            if self.estoque[produto] >= quantidade:
                self.estoque[produto] -= quantidade
                print(f'{quantidade} unidade{'s' if quantidade > 1 else ''} de {produto} vendida{'s' if quantidade > 1 else ''} com sucesso.')
                if self.estoque[produto] == 0:
                    del self.estoque[produto]
                    print(f'Produto {produto} esgotado e remmovido do estoque.')
            else:
                print(f'Estoque insuficiente. Há apenas {self.estoque[produto]} unidades de {produto}.')

        else:
            print(f"Produto '{produto}' não encontrado no estoque.")

papelaria = Loja()
papelaria.estoque = {"caderno":20, "caneta":100, "livro":5}
papelaria.adicionar_produtos("folhas", 500)
print(papelaria.estoque)

papelaria.vender("caneta", 50)
print(papelaria.estoque)

papelaria.vender("caneta", 50)
print(papelaria.estoque)

papelaria.vender("pijama", 20)
