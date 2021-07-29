enjoyment = dict()
sumgoals, cod = 0, 0, 0
listgoals, infos = list(), list()

while True:
    enjoyment['nome'] = input("Name player? \n")
    nome_jogador = enjoyment['nome']
    cod += 1
    enjoyment['cod'] = cod
    enjoyment['partidas'] = int(input("Matches played \n"))
    partidas_jogadas = enjoyment['partidas']
    for partida in range(partidas_jogadas):
        gols_partida = int(input(f"Goals {nome_jogador} make {partida+1}? \n"))
        listgoals.append(gols_partida)
        enjoyment['listgoals'] = listgoals.copy()
    enjoyment['sumgoals'] = sum(listgoals)
    infos.append(enjoyment.copy())
    listgoals.clear()
    continuar = input("Continue [S/N] \n")
    continuar = continuar.upper()
    if continuar[0] == "N":
        break

print(f"{'cod':^5} {'nome':^10} {'gols':<25} {'total':<25}")
for jogador in infos:
    print(f"{jogador['cod']!s:^5s} {jogador['nome']!s:^10s} {jogador['listgoals']!s:<25s} {jogador['sumgoals']!s:<25s}")

while True:
    cod_usuario = int(input("Select player (999 para parar) \n"))
    if cod_usuario == 999:
        break
    if cod_usuario > len(infos):
        print("Error, try again!")
    for dictionary in infos:
        if dictionary['cod'] == cod_usuario:
            print(f"About {dictionary['nome'].upper()}:")
            for n, gol in enumerate(dictionary['listgoals']):
                print(f"In game {n+1}, make {gol} goals.")
