names = input('Enter the names, separeted by commas: ')
names_list = names.split(',')
for name in names_list:
    print(name.strip())