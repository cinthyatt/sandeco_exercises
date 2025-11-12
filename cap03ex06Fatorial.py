num = int(input('Enter the number: '))
count = num
fat = 1
print(f'{num}! = ', end='')
while count >0:
    print(f'{count}', end='')
    fat *= (count)
    count -= 1
    
    print(' x ' if count > 0 else ' = ', end='' )
print(fat)