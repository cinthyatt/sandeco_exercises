import string
dic = {
    "que dia é hoje" : "Hoje é dia de ser feliz!", 
    "quantos anos você tem": "Eu tenho quantos anos Deus quiser me dar.",
    "qual sua comida favorita": "Gosto do que tiver na mesa.",
    "qual seu objetivo de vida" : "Ter paz!!"
    }

pergunta = input('Digite sua pergunta: ').strip().lower()

#remove pontuação
for char in string.punctuation:
    pergunta = pergunta.replace(char, "")

#tenta econtrar correspondência
resposta = None
for chave in dic.keys():
    chave_limpa = chave.lower()
    for char in string.punctuation:
        chave_limpa = chave_limpa.replace(char, "")
    if pergunta == chave_limpa:
        resposta = dic[chave]
        break

if resposta:
    print(resposta)
else:
    print('Pergunta não cadastrada.')