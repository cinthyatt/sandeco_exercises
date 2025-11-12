def maior_numero(x, y, z):
    maior = 0
    if x > y and x > z:
        maior = x
        return maior
    elif z > x and z > y:
        maior = z
        return maior
    elif y > x and y > z:
        maior = y
        return maior
 
    else:
        print('Outra possibilidade')

print(maior_numero(10, 5, 2))
print(maior_numero(10, 0, 2))
print(maior_numero(5, 2, 0))
print(maior_numero(5, 0, 2))
print(maior_numero(0, 2, 5))
print(maior_numero(0, 5, 10))