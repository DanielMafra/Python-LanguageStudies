from random import randint

numbers = (randint(1, 10), randint(1, 10), randint(
    1, 10), randint(1, 10), randint(1, 10))

print('The numbers drawn were: ', end='')

for n in numbers:
    print(f'{n} ', end='')

print(f'\nThe highest value drawn was: {max(numbers)}')
print(f'The lowest value drawn was: {min(numbers)}')
