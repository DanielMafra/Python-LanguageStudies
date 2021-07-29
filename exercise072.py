cont = ('zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten',
        'eleven', 'twelve', 'thirteen', 'fourteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty')

while True:
    num = int(input('Enter a number between 0 and 20: '))
    if 0 <= num <= 20:
        break
    print('Try again. ', end='')

print(f'You entered {cont[num]}')
