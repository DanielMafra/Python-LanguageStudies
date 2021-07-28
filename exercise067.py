while True:
    n = int(input('Want to see the multiplication table of what value? '))
    print('-' * 30)
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} x {c} = {n*c}')
    print('-' * 30)

print('Times tables program ended. Check back often!')
