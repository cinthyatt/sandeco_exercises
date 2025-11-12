phrase = input('Enter your phrase: ').strip()

characters = len(phrase)
charactersns = len(phrase.replace(' ', ''))
words = len(phrase.split())

upper = 0
for letter in phrase:
    if letter.isupper():
        upper += 1

print(f'The phrase has a total of {characters} characters, {charactersns} characters without spaces, {words} words, and {upper} captalized letters.')
