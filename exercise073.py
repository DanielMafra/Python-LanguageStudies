teams = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense', 'Atlético', 'Botafogo',
         'Atlético-PR', 'Bahia', 'São Paulo', 'Fluminense', 'Sport Recife', 'EC Vitória', 'Coritiba', 'Avaí', 'Ponte Preta', 'Atlético-GO')

print('-=' * 15)
print(f'List of Brasileirão teams: {teams}')
print('-=' * 15)
print(f'The first 5 are: {teams[0:5]}')
print('-=' * 15)
print(f'The last 4 are: {teams[-4:]}')
print('-=' * 15)
print(f'Teams in alphabetical order: {sorted(teams)}')
print('-=' * 15)
print(f'Chapecoense is in {teams.index("Chapecoense")+1} position')
