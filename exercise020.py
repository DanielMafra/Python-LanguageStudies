from random import shuffle

n1 = str(input('First student: '))
n2 = str(input('Second student: '))
n3 = str(input('Third student: '))
n4 = str(input('Fourth student: '))
students = [n1, n2, n3, n4]
shuffle(students)

print('The order of presentation will be: {}'.format(students))
