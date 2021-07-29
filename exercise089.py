record = list()

while True:
    name = str(input('Name: '))
    n1 = float(input('Note 1: '))
    n2 = float(input('Note 2: '))
    average = (n1 + n2) / 2
    record.append([name, [n1, n2], average])
    ans = str(input('Continue? [Y/N] '))
    if ans in 'Nn':
        break

print('-=' * 30)
print(f'{"No.":<4}{"NAME":<10}{"AVERAGE":>8}')
print('-' * 26)

for i, a in enumerate(record):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')

while True:
    print('-' * 35)
    opt = int(input('Show notes from which student? (999 to exit): '))
    if opt == 999:
        print('FINISH...')
        break
    if opt <= len(record) - 1:
        print(f'Notes from {record[opt][0]} is {record[opt][1]}')

print('<<< BYE >>>')
