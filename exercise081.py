values = []

while True:
    values.append(int(input('Enter a value: ')))
    ans = str(input('Continue? [Y/N] '))
    if ans in 'Nn':
        break

print('-=' * 30)
print(f'You entered {len(values)} elements.')
values.sort(reverse=True)
print(f'Values in descending order are {values}')

if 5 in values:
    print('The value 5 is part of the list!')
else:
    print('The value 5 was not found in the list!')
