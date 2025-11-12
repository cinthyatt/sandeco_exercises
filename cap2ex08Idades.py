age1 = int(input('Enter the first age: '))
age2 = int(input('Enter the second age: '))

if age1 > age2:
    print('The first age value is greater / The first person is older.')
elif age1 < age2:
    print('The first age value is less than the second / The second person is older / The first person is younger.')

else:
    print('The two age values are equal / Both people have the same age.')