print('PA generator')
print('-=' * 10)

first = int(input('First term: '))
reason = int(input('Reason for PA: '))
term = first
cont = 1

while cont <= 10:
    print('{} -> '.format(term), end='')
    term += reason
    cont += 1

print('END')
