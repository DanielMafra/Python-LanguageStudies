from random import choice

n1 = str(input('First student: '))
n2 = str(input('Second student: '))
n3 = str(input('Third student: '))
n4 = str(input('Fourth student: '))
students = [n1, n2, n3, n4]
chosen = choice(students)

print('The chosen student was {}.'.format(chosen))
