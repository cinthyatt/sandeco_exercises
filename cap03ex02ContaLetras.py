word = input('Enter your word: ')
count = 0
countA = 0
for letter in word:
    if letter == 'a':
        count+=1
    elif letter == 'A':
        countA += 1

print(f'There are {count} letters "a" and {countA} letters "A" in the word {word}.')