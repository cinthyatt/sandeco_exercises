import pandas as pd

#Carregar dados de uma arquivo CSV
df = pd.read_csv('notas.csv')
'''print(df.head()) #Exibe as primeiras 5 linhas do DataFrame'''

#Filtrar determinado dado (alunos que tiraram nota de matematica = 5)
notas_matematica = df[df['NotaMatematica'] == 5]
print(notas_matematica)
