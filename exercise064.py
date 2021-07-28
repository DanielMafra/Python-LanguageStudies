num = cont = sum = 0
num = int(input('Enter a number [999 to stop]: '))

while num != 999:
    sum += num
    cont += 1
    num = int(input('Enter a number [999 to stop]:'))

print('You entered {} numbers and the sum between them was {}'.format(cont, sum))
