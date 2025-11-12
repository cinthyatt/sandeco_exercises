class Aluno:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota

    def aprovado(self):
        if self.nota >= 7:
            return True
        else:
            return False
        
aluno = Aluno("Alice", 8)
aluno2 = Aluno("Joao", 3)

print(aluno.aprovado())
print(aluno2.aprovado())