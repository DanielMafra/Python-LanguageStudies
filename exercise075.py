number = (int(input('Enter a number:')),
          int(input('Enter another number:')),
          int(input('Enter one more number:')),
          int(input('Enter the last number:')))

print(f'You entered the values {number}')
print(f'The value 9 appeared {number.count(9)} times')

if 3 in number:
    print(f'The value 3 appeared in the {number.index(3)+1} position')

print('The even values entered were ', end='')

for n in number:
    if n % 2 == 0:
        print(f'{n} ', end='')
