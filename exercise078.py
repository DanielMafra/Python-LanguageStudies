listnum = []
higher = 0
smaller = 0

for c in range(0, 5):
    listnum.append(int(input(f'Enter a number for position {c}: ')))
    if c == 0:
        higher = smaller = listnum[c]
    else:
        if listnum[c] > higher:
            higher = listnum[c]
        if listnum[c] < smaller:
            smaller = listnum[c]

print('=-' * 30)
print(f'You entered the values {listnum}')
print(f'The highest value entered was {higher} in positions ', end='')

for i, v in enumerate(listnum):
    if v == higher:
        print(f'{i}... ', end='')

print()
print(f'The lowest value entered was {smaller} in positions ', end='')

for i, v in enumerate(listnum):
    if v == smaller:
        print(f'{i}... ', end='')

print()
