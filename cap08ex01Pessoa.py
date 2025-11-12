class Pessoa:
    def __init__(self, nome, idade):
        self.nome =  nome
        self.idade = idade

    def exibir_informacoes(self):
        print(f'A pessoa se chama {self.nome} e tem {self.idade} anos.')

pessoa = Pessoa("Maria", 30)

pessoa.exibir_informacoes()

    