from math import hypot

ol = float(input('Length of opposite leg: '))
al = float(input('Length of adjacent leg: '))
hy = hypot(ol, al)

print('The hypotenuse will measure {:.2f}'.format(hy))
