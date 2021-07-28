from datetime import date

current = date.today().year
total1 = 0
total2 = 0

for people in range(1, 8):
    birth = int(input('In what year was {} person born? '.format(people)))
    age = current - birth
    if age >= 21:
        total1 += 1
    else:
        total2 += 1

print('In all, we had {} people of legal age.'.format(total1))
print('And we also had {} underage people.'.format(total2))
