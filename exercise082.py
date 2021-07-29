num = list()
pairs = list()
odd = list()

while True:
    num.append(int(input('Enter a value: ')))
    ans = str(input('Continue? [Y/N] '))
    if ans in 'Nn':
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        pairs.append(v)
    elif v % 2 == 1:
        odd.append(v)

print('-=' * 30)
print(f'The full list is {num}')
print(f'The list of pairs is {pairs}')
print(f'The odd list is {odd}')
