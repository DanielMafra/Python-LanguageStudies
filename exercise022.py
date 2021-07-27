name = str(input('Enter your full name: ')).strip()
separate = name.split()

print('Analyzing your name...')
print('Your name in uppercase is {}'.format(name.upper()))
print('Your name in lowercase is {}'.format(name.lower()))
print('Your name has a total of {} letters'.format(len(name) - name.count(' ')))
print('Your first name is {} and it has {} letters'.format(
    separate[0], len(separate[0])))
