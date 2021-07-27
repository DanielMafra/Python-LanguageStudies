name = str(input('Enter your full name: ')).strip()
n = name.split()

print('Very pleased to meet you!')
print('Your first name is {}.'.format(n[0]))
print('Your last name is {}.'.format(n[len(n) - 1]))
