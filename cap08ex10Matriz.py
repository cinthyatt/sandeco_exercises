
class Matriz:
    def __init__(self):
        self.matriz = []
        self.transposta = []

    def transpor(self):
        self.transposta = []
        for i in range(len(self.matriz[0])):
            nova_linha = []
            for j in range(len(self.matriz)):
                nova_linha.append(self.matriz[j][i])
            self.transposta.append(nova_linha)
        return self.transposta
    
    def eh_quadrada(self):
        n_linhas = len(self.matriz)
        if n_linhas == 0:
            return False
        for linha in self.matriz:
            if len(linha) != n_linhas:
                return False
        return True


    def determinante(self):
        #só funciona para matriz quadrada
        if not self.eh_quadrada():
            print('Não é possível calcular o determinante pois a matriz não é quadrada.')
            return None
    
        n = len(self.matriz)
        if n==1:
            return self.matriz[0][0]
        if n==2:
            return self.matriz[0][0]*self.matriz[1][1] - self.matriz[0][1]*self.matriz[1][0]
        det = 0
        for c in range(n):
            # Cria a submatriz removendo a primeira linha e a coluna c
            submatriz = [linha[:c] + linha[c+1:] for linha in self.matriz[1:]]
            # Recursivamente calcula o determinante da submatriz
            temp = Matriz()
            temp.matriz = submatriz
            det += ((-1)**c) * self.matriz[0][c] * temp.determinante()
        return det




matriz1 = Matriz()
matriz1.matriz = [[1, 5, 9], [7, 5, 3], [8, 2, 6]]
print(matriz1.transpor())
print(matriz1.determinante())