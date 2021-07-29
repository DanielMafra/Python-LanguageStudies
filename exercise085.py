num = [[], []]
value = 0

for c in range(1, 8):
    value = int(input(f'Enter the {c} value: '))
    if value % 2 == 0:
        num[0].append(value)
    else:
        num[1].append(value)

print('-=' * 30)
num[0].sort()
num[1].sort()
print(f'Pairs: {num[0]}')
print(f'Odd: {num[1]}')
