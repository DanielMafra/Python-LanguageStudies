total = totmil = smaller = cont = 0
cheap = ''

while True:
    product = str(input('Name of product: '))
    price = float(input('Price: U$'))
    cont += 1
    total += price
    if price > 1000:
        totmil += 1
    if cont == 1 or price < smaller:
        smaller = price
        cheap = product
    answer = ' '
    while answer not in 'YN':
        answer = str(
            input('Do you want to continue? [Y/N] ')).strip().upper()[0]
    if answer == 'N':
        break

print('{:-^40}'.format(' END OF PROGRAM '))
print(f'The purchase total was U${total:.2f}')
print(f'We have {totmil} products costing over $1000.00')
print(f'The cheapest product was {cheap} which costs U${smaller:.2f}')
