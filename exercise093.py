player = dict()
matches = list()
player['name'] = str(input('Name: '))
tot = int(input(f'How many matches did {player["name"]} play? '))

for c in range(0, tot):
    matches.append(int(input(f'   How many goals in the match {c}? ')))

player['goals'] = matches[:]
player['total'] = sum(matches)

print('-=' * 30)
print(player)
print('-=' * 30)

for k, v in player.items():
    print(f'Field {k} has the value {v}')

print('-=' * 30)
print(f'The player {player["name"]} played {len(player["goals"])} matches')

for i, v in enumerate(player['goals']):
    print(f'     => Match {i}, {v} goals')

print(f'Total goals: {player["total"]}')
