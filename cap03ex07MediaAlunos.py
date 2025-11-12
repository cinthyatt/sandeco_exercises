lista = []
soma = 0
acima = abaixo = 0
for al in range (5):
    nota = int(input(f'Digite a nota do {al+1}º aluno: '))
    lista.append(nota)
    soma += nota

media = soma/5

for nota in lista:
    if nota >= media:
        acima += 1
    elif nota < media:
        abaixo +=1


print(f'A média dos alunos foi {media:.2f}. {acima} alunos ficaram acima da média e {abaixo} alunos ficaram abaixo da média.')