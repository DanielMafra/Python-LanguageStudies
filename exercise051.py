first = int(input('First value: '))
reason = int(input('Reason: '))
tenth = first + (10 - 1) * reason

for c in range(first, tenth + reason, reason):
    print('{} '.format(c), end='-> ')

print('Finish')
