n1 = int(input('First value: '))
n2 = int(input('Second value: '))
option = 0

while option != 5:
    print('''
    [ 1 ] add
    [ 2 ] multiply
    [ 3 ] greater
    [ 4 ] new numbers
    [ 5 ] exit the program
    ''')
    option = int(input(">>>>> What's your option? "))
    if option == 1:
        sum = n1 + n2
        print('The sum between {} + {} is {}'.format(n1, n2, sum))
    elif option == 2:
        sum = n1 * n2
        print('The result of {} x {} is {}'.format(n1, n2, sum))
    elif option == 3:
        if n1 > n2:
            higher = n1
        else:
            higher = n2
        print('Between {} and {} the highest value is {}'.format(n1, n2, higher))
    elif option == 4:
        print('Enter the numbers again: ')
        n1 = int(input('First value: '))
        n2 = int(input('Second value: '))
    elif option == 5:
        print('Finishing...')
    else:
        print('Invalid option. Try again. ')
    print('=-=' * 10)

print('End of program! Check back often!')
