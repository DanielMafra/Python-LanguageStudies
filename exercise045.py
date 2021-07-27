from random import randint
from time import sleep

items = ('Rock', 'Paper', 'Scissors')
computer = randint(0, 2)

print('''Your options:
[ 0 ] Rock
[ 1 ] Paper
[ 2 ] Scissors''')

player = int(input("What's your move? "))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')

print('-=' * 11)
print('Computer threw {}'.format(items[computer]))
print('You threw {}'.format(items[player]))
print('-=' * 11)

if computer == 0:
    if player == 0:
        print('DRAW')
    elif player == 1:
        print('YOU WON')
    elif player == 2:
        print('COMPUTER WON')
    else:
        print('Invalid Play!')
elif computer == 1:
    if player == 0:
        print('COMPUTER WON')
    elif player == 1:
        print('DRAW')
    elif player == 2:
        print('YOU WON')
    else:
        print('Invalid Play!')
elif computer == 2:
    if player == 0:
        print('YOU WON')
    elif player == 1:
        print('COMPUTER WON')
    elif player == 2:
        print('DRAW')
    else:
        print('Invalid Play!')
