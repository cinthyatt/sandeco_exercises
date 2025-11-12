class Agenda:
    def __init__(self):
        self.compromissos = {}

    def adicionar(self, data, descricao):
        if data in self.compromissos: 
            self.compromissos[data].append(descricao)
            print(f'Novo compromisso adicionado à data {data}.')
        else:
            self.compromissos[data] = [descricao]
            print(f'Compromisso {descricao} adicionado à data {data}.')

    def remover(self, data, descricao):
        if data in self.compromissos:
            if descricao in self.compromissos[data]:
                self.compromissos[data].remove(descricao)
                print(f"Compromisso '{descricao}' removido da agenda.")
                if not self.compromissos[data]:
                    del self.compromissos[data]
            else:
                print('Esse compromisso não foi encontrado nessa data.')
        else: 
            print('Não existem compromissos registrados nessa data.')

    def exibir(self, data):
        if data in self.compromissos:
            print(f"No dia {data} você tem agendado:")
            for i, compromisso in enumerate(self.compromissos[data]):
                print(f"     {i+1}. {compromisso}")
        else: 
            print('Nessa data não há compromissos registrados.')


agenda = Agenda()
agenda.adicionar("02/11", "Consulta Médica")
print(agenda.compromissos)

agenda.adicionar("02/11", "Reunião com Artur")
print(agenda.compromissos)

agenda.exibir("02/11")
agenda.remover("02/11", "Consulta Médica")

agenda.exibir("03/11")

agenda.adicionar("03/11", "Consulta Médica")
agenda.exibir("03/11")