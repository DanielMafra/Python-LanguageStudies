a = int(input('First value: '))
b = int(input('Second value: '))
c = int(input('Third value: '))

smaller = a
larger = a

if b < a and b < c:
    smaller = b

if c < a and c < b:
    smaller = c

if b > a and b > c:
    larger = b

if c > a and c > b:
    larger = c

print('The lowest value entered was {}'.format(smaller))
print('The highest value entered was {}'.format(larger))
