class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo
        valor = 0

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f"Depósito de {valor} realizado com sucesso!")
        else:
            print("Valor de depósito inválido.") 
    
    def sacar(self, valor):
        if valor > self.__saldo:
            print("Saldo insuficiente")
        else:
            self.__saldo -= valor
            print(f'Saque de R$ {valor:.2f} realizado com sucesso.')

    #precisa desse Método getter para acessar o saldo    
    def obter_saldo(self):
        return self.__saldo

conta1 = ContaBancaria("Ana", 500)

conta1.depositar(10)
print(f'Novo saldo: {conta1.obter_saldo()}')
conta1.depositar(-60)
print(conta1.obter_saldo())
conta1.sacar(500)
print(conta1.obter_saldo())
conta1.sacar(10000)
print(conta1.obter_saldo())

pass