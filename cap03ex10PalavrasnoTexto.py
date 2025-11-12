with open("cap03ex10Texto.txt", "rt", encoding="utf-8") as file:
    texto = file.read()
words = texto.split()

freq = {}
for word in words:
    word = word.lower().strip(".,!?:;()[]\"'")
    freq[word] = freq.get(word, 0) +1

#conta as palavras e coloca em ordem de frequencia
for word, count in sorted(freq.items(), key=lambda x: x[1], reverse=True):
    print(f'{word}:{count}')