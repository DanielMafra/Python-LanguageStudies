from random import randint

v = 0

while True:
    player = int(input('Enter a value: '))
    computer = randint(0, 10)
    total = player + computer
    typ = ' '
    while typ not in 'PO':
        typ = str(input('Even or odd? [P/O] ')).strip().upper()[0]
    print(
        f'You played {player} and the computer {computer}. Total gave {total}', end='')
    print(' gave pair' if total % 2 == 0 else ' gave odd')
    if typ == 'P':
        if total % 2 == 0:
            print('You won!')
            v += 1
        else:
            print('You lost!')
            break
    elif typ == 'O':
        if total % 2 == 1:
            print('You won!')
            v += 1
        else:
            print('You lost!')
            break
    print("Let's play again...")

print(f'Game over! You won {v} times')
