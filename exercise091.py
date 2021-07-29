from random import randint
from time import sleep
from operator import itemgetter

game = {'player1': randint(1, 6),
        'player2': randint(1, 6),
        'player3': randint(1, 6),
        'player4': randint(1, 6)}
ranking = list()

print('Raffled values: ')

for k, v in game.items():
    print(f'{k} rolled a {v} on the dice')
    sleep(1)

ranking = sorted(game.items(), key=itemgetter(1), reverse=True)

print('-=' * 30)
print(' == RANKING PLAYERS == ')

for i, v in enumerate(ranking):
    print(f'   {i+1} position: {v[0]} with {v[1]}')
    sleep(1)
