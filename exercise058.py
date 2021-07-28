from random import randint

computer = randint(0, 10)
correct = False
attempts = 0

print("I'm your computer... I just thought of a number between 0 and 10.")
print('Can you guess which one it was? ')

while not correct:
    player = int(input("What's your guess? "))
    attempts += 1
    if player == computer:
        correct = True
    else:
        if player < computer:
            print('More... Try one more time.')
        elif player > computer:
            print('Less... Try one more time.')

print('You got it right with {} attempts. Congratulations!'.format(attempts))
