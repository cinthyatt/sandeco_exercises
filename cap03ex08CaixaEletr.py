
valor = float(input('Digite o valor de saque desejado: R$ '))
ced100 = ced50 = ced20 = ced10 = 0

ced100 = int(valor//100)
valor2 = valor % 100
ced50 = int(valor2//50)
valor3 = valor2%50
ced20 = int(valor3//20)
valor4=valor3%20
ced10 = int(valor4//10)


print(f'Você recebeu {ced100} notas de 100, {ced50} notas de 50, {ced20} notas de 20 e {ced10} notas de 10.')