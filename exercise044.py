print('{:=^40}'.format(' GUANABARA STORE '))

price = float(input('Purchase price: U$'))

print('''PAYMENT METHODS
[ 1 ] cash/check
[ 2 ] card cash
[ 3 ] 2x on the card
[ 4 ] 3x or more on the card''')

option = int(input('What is the option? '))

if option == 1:
    total = price - (price * 10 / 100)
elif option == 2:
    total = price - (price * 5 / 100)
elif option == 3:
    total = price
    portion = total / 2
    print(
        'Your purchase will be paid in 2 installments of U${:.2f} without interest'.format(portion))
elif option == 4:
    total = price + (price * 20 / 100)
    totalPortions = int(input('How many installments? '))
    portion = total / totalPortions
    print('Your purchase will be paid in {} installments of U${:.2f} with interest'.format(
        totalPortions, portion))
else:
    total = price
    print('Invalid payment option. Try again!')

print('Your U${:.2f} purchase will cost U${:.2f} at the end.'.format(
    price, total))
