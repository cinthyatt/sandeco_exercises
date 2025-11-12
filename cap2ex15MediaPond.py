grade1 = float(input('Enter the first grade: '))
w1 = float(input('Enter the weight for the first grade: '))

grade2 = float(input('Enter the second grade: '))
w2 = float(input('Enter the weight for the second grade: '))

grade3 = float(input('Enter the third grade: '))
w3 = float(input('Enter the weight for the third grade: '))
print('-'*30)
print(f'The weighted average is: {((grade1*w1)+(grade2*w2)+(grade3*w3))/(w1+w2+w3):.2f}')