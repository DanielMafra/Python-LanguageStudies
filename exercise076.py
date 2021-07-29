listing = ('Pencil', 1.75,
           'Rubber', 2,
           'Journal', 15.90,
           'Case', 25,
           'Protractor', 4.20,
           'Compass', 9.99,
           'Schoolbag', 120.32,
           'Pens', 22.30,
           'Book', 34.90)

print('-' * 40)
print(f'{"PRICE LISTING":^40}')
print('-' * 40)

for pos in range(0, len(listing)):
    if pos % 2 == 0:
        print(f'{listing[pos]:.<30}', end='')
    else:
        print(f'U${listing[pos]:>7.2f}')

print('-' * 40)
