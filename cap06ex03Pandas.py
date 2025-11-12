import pandas as pd

df = pd.read_csv('notas.csv')

#Mostra quantos valores ausentes tem em cada coluna
print('Valores nulos por coluna:')
print(df.isnull().sum())

'''#Remove linhas inteiras que contenham pelo menos um valor ausente
df_limpo = df.dropna()
#Para remover as colunas com valores ausentes:
df_limpo = df.dropna(axis=1)

#se quiser modificar a tabela original tirando essas linhas
df.dropna(inplace=True)'''

#Substituir valores nulos 
df.fillna(0, inplace=True) #Substitui NaN por 0

'''#Cria uma nova coluna "Média"
df['Média'] = df[['NotaMatematica', 'NotaPortugues', 'NotaGeografia', 'NotaHistoria']].mean(axis=1)
print(df)

#salva o resultado em outro csv
df.to_csv('notas_com_medias.csv', index=False)'''

'''#Média apenas das duas primeiras notas
df['Média Mat-Port'] = df[['NotaMatematica', 'NotaPortugues']].mean(axis=1)
'''
#insert(posição, nome_coluna, valores)
#Colocar a coluna "Média Mat-Port"  depois da nota de portugues
df.insert(3, 'Média Mat-Port', df[['NotaMatematica', 'NotaPortugues']].mean(axis=1))

df.to_csv('notas_med_matport.csv', index=False)
print(df.head())