answer = 'Y'
sum = quant = average = higher = smaller = 0

while answer in 'Yy':
    num = int(input('Enter a number: '))
    sum += num
    quant += 1
    if quant == 1:
        higher = smaller = num
    else:
        if num > higher:
            higher = num
        if num < smaller:
            smaller = num
    answer = str(input('Do you want to continue? [Y/N] ')).upper().strip()[0]

average = sum / quant

print('You entered {} numbers and the average was {}'.format(quant, average))
print('The highest value was {} and the lowest was {}'.format(higher, smaller))
