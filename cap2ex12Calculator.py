print('-'*30)
print("MATH OPERATIONS MENU")
print('-'*30)
print("""   Enter A for Addiction
   Enter S for subtraction
   Enter M for multiplication
   Enter D for division""")
print('-'*30)
while True: 
    operation = input('Choose an operation: ').strip().upper()[0]
    print('-'*30)
    n1 = float(input('Enter the first number: '))
    n2 = float(input('Enter the second number: '))
    print('-'*30)
    if operation == 'A':
        print(f'{n1} + {n2} = {n1+n2}')
        break

    elif operation == 'S':
        print(f'{n1} - {n2} = {n1-n2}')
        break

    elif operation == 'M':
        print(f'{n1} x {n2} = {n1*n2}')
        break

    elif operation == 'D':
        print(f'{n1} / {n2} = {n1/n2:.2f}')
        break

    else: 
        operation = input('Invalid operation! ')

