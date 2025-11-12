class Funcionario:
    def __init__(self, nome, salario, cargo):
        self.nome = nome
        self.salario = salario
        self.cargo = cargo

    def promover(self, novo_cargo):
        self.cargo = novo_cargo
        self.salario = self.salario * 1.20

func1 = Funcionario("Ana", 1800.00, "vendedora")
print(f'Funcionário {func1.nome}, tem o cargo de {func1.cargo} e recebe o salário de R$ {func1.salario:.2f}')
func1.promover("Gerente")

print(f'Funcionário {func1.nome}, tem o cargo de {func1.cargo} e recebe o salário de R$ {func1.salario:.2f}')