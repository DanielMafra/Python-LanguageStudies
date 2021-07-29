numbers = list()

while True:
    n = int(input('Enter a value: '))
    if n not in numbers:
        numbers.append(n)
        print('Successfully added value...')
    else:
        print("Duplicate value! I won't add...")
    a = str(input('Continue? [Y/N] '))
    if a in 'Nn':
        break

print('-=' * 30)
numbers.sort()
print(f'You entered the values {numbers}')
