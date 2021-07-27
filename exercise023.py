num = int(input('Enter a number: '))
u = num // 1 % 10
t = num // 10 % 10
h = num // 100 % 10
th = num // 1000 % 10

print('Analyzing the number {}...'.format(num))
print('Unit: {}'.format(u))
print('Ten: {}'.format(t))
print('Hundred: {}'.format(h))
print('Thousands: {}'.format(th))
