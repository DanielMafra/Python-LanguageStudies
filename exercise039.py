from datetime import date

current = date.today().year
birth = int(input('Year of birth: '))
age = current - birth

print('Whoever was born in {} is {} years old in {}.'.format(birth, age, current))

if age == 18:
    print('You have to sign up right away!')
elif age < 18:
    difference = 18 - age
    print('There are still {} years to enlistment.'.format(difference))
    year = current + difference
    print('Your enlistment will be in {}.'.format(year))
elif age > 18:
    difference = age - 18
    print('You should have joined {} years ago.'.format(difference))
    year = current - difference
    print('Your enlistment was in {}.'.format(year))
