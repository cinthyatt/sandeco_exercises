from random import randint

comp = randint(1, 100)

cont = 0

while True:
    palpite = int(input('Advinhe o número: '))
    if comp > palpite:
        print('Maior!')
        cont += 1
    elif comp < palpite:
        print('Menor')
        cont += 1
    else: 
        print('Acertou! Parabéns!')
        break
    if cont == 7:
        print('Você já tentou 7 vezes e não conseguiu acertar... Mais sorte da próxima vez')
        print(f'O número era: {comp}')
        break