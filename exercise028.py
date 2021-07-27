from random import randint
from time import sleep

computer = randint(0, 5)

print('-=-' * 20)
print('I will think of a number between 0 and 5. Try to guess...')
print('-=-' * 20)
player = int(input('What number did I think of? '))
print('Processing...')
sleep(2)

if player == computer:
    print('CONGRATULATIONS! You managed to beat me!')
else:
    print('WON! I thought of number {} and not {}'.format(computer, player))
