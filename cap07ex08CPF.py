try:
    cpf = input('Digite seu CPF: ')
    cpf = cpf.replace('.', '')
    cpf = cpf.replace('-', '')

    if len(cpf) != 11 or not cpf.isdigit():
        raise ValueError(f'CPF inválido. O CPF deve conter exatamente 11 dígitos. Você digitou {cpf}')
    else:
        print('CPF registrado com sucesso!')

except ValueError as erro:
    print(erro)