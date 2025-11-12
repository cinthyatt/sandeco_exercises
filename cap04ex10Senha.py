import secrets
import string

def gerar_senha(n: int):
    if n < 4:
        #interrompe a função e avisa caso o comprimento pedido seja menor que 4
        raise ValueError("O tamanho mínimo é 4 para conter todos os tipos de caracteres.")
    #Grupos de caracteres
    letras_maiusculas = string.ascii_uppercase
    letras_minusculas = string.ascii_lowercase
    digitos = string.digits
    especiais = string.punctuation

    #Garante pelo menos um de cada
    senha = [
        secrets.choice(letras_maiusculas), 
        secrets.choice(letras_minusculas), 
        secrets.choice(digitos),
        secrets.choice(especiais)]
    
    #Preenche o restante
    todos = letras_maiusculas + letras_minusculas + digitos + especiais
    senha +=[secrets.choice(todos) for i in range(n-4)]

    #Embaralha pra nao ficar previsivel
    secrets.SystemRandom().shuffle(senha)

    return ''.join(senha)

print(gerar_senha(12))
print(gerar_senha(8))
