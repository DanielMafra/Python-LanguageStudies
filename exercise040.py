n1 = float(input('First value: '))
n2 = float(input('Second value: '))
n3 = (n1 + n2) / 2

print(
    'Taking {:.1f} and {:.1f}, the student s average is {:.1f}'.format(n1, n2, n3))

if 7 > n3 >= 5:
    print('The student is in recovery.')
elif n3 < 5:
    print('The student is failing.')
elif n3 >= 7:
    print('The student is approved.')
