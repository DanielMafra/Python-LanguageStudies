num = int(input('Enter an integer: '))

print('''Choose one of the bases for conversion:
[1] convert to BINARY
[2] convert to OCTAL
[3] convert to HEXADECIMAL''')

option = int(input('Your choice: '))

if option == 1:
    print('{} converted to BINARY equals {}'.format(num, bin(num)[2:]))
elif option == 2:
    print('{} converted to OCTAL equals {}'.format(num, oct(num)[2:]))
elif option == 3:
    print('{} converted to HEXADECIMAL equals {}'.format(
        num, hex(num)[2:]))
else:
    print('Invalid option. Try again.')
