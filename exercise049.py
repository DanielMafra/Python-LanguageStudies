num = int(input('Enter a number to see your multiplication table: '))

print('-' * 12)

for c in range(1, 11):
    print('{} x {:2} = {}'.format(num, c, (num*c)))
