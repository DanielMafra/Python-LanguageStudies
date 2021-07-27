from datetime import date

current = date.today().year
birth = int(input('Year of birth: '))
age = current - birth

print('The athlete is {} years old.'.format(age))

if age <= 9:
    print('Classification: little')
elif age <= 14:
    print('Classification: child')
elif age <= 19:
    print('Classification: junior')
elif age <= 25:
    print('Classification: senior')
else:
    print('Classification: master')
