from time import sleep


def higher(* num):
    cont = higher = 0
    print('-=' * 30)
    print('Wait...')
    for value in num:
        print(f'{value} ', end='', flush=True)
        sleep(0.3)
        if cont == 0:
            higher = value
        else:
            if value > higher:
                higher = value
        cont += 1
    print(f'Total: {cont} values')
    print(f'Higher value: {higher}')


higher(2, 9, 4, 5, 7, 1)
higher(4, 7, 0)
higher(1, 2)
higher(6)
higher()
