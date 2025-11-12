def eh_primo(x):
    if x <= 1:
        return False
    for i in range (2, x):
        if x % i == 0:
            return False
    return True


x = int(input('Digite um numero para saber se ele é primo: '))
print(eh_primo(x))
