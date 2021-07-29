from random import randint
from time import sleep

mlist = list()
games = list()
quantity = int(input("How many games do you want me to raffle? \n"))
total = 1

while total <= quantity:
    counter = 0
    while True:
        number = randint(1, 60)
        if number not in mlist:
            mlist.append(number)
            counter += 1
        if counter >= 6:
            break
    mlist.sort()
    games.append(mlist[:])
    mlist.clear()
    total += 1

for i, l in enumerate(games):
    print(f"game {i + 1}: {l}")
    sleep(1)
