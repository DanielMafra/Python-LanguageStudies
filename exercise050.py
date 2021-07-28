sum = 0
cont = 0

for c in range(1, 7):
    num = int(input('Enter the {} value:'.format(c)))
    if num % 2 == 0:
        sum += num
        cont += 1

print('You entered {} even numbers and the sum was {}'.format(cont, sum))
