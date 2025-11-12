def calcular_hipotenusa(cat1, cat2):

    hipotenusa = (cat1**2 + cat2**2)**(1/2)
    print(f'Para catetos iguais a {cat1} e {cat2}, temos a hipotenusa igual a {hipotenusa}.')

cat1 = int(input('Digite o valor do primeiro cateto: '))
cat2 = int(input('Digite o valor do segundo cateto: '))
calcular_hipotenusa(cat1, cat2)