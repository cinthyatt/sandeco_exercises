nome = input('Digite seu nome completo: ')

print(nome.upper())
print(nome.lower())
nome_formatado=" ".join([parte.capitalize() for parte in nome.split()])
print(nome_formatado)

'''nome2 = nome.split( )
for n in nome2:
    print(n.capitalize())'''
