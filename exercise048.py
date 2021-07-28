sum = 0
cont = 0

for c in range(1, 501, 2):
    if c % 3 == 0:
        cont += 1
        sum += c

print('The sum of all {} requested values is {}.'.format(cont, sum))
