print('Gerador de PA')
print('-=' * 10)

first = int(input('First term: '))
reason = int(input('Reason for PA: '))
term = first
cont = 1
total = 0
more = 10

while more != 0:
    total += more
    while cont <= total:
        print('{} -> '.format(term), end='')
        term += reason
        cont += 1
    print('BREAK')
    more = int(input('How many more terms do you want to show? '))

print('Progression finished with {} terms shown.'.format(total))
