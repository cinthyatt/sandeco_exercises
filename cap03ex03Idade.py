from datetime import date
current_date = date.today().year
birth = int(input('Enter your year of birth: '))
age = current_date - birth

if age < 18:
    print('You are underage.')
elif age > 64:
    print('You are a senior.')
else:
    print('You are an adult.')