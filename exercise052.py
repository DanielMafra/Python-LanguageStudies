num = int(input('Enter a value: '))
total = 0

for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end='')
        total += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')

print('\n\033[mNumber {} has been split {} times'.format(num, total))

if total == 2:
    print("And that's why it's a prime number.")
else:
    print("And that's why it's not a prime number.")
