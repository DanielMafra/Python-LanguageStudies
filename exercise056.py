sumage = 0
averageage = 0
bageman = 0
nameold = ''
totalwoman = 0

for p in range(1, 5):
    print('----- {} PEOPLE -----'.format(p))
    name = str(input('Name: ')).strip()
    age = int(input('Age: '))
    gender = str(input('Gender [M/F]: ')).strip()
    sumage += age
    if p == 1 and gender in 'Mm':
        bageman = age
        nameold = name
    if gender in 'Mm' and age > bageman:
        bageman = age
        nameold = name
    if gender in 'Ff' and age < 20:
        totalwoman += 1

averageage = sumage / 4

print('The average age of the group is {} years.'.format(averageage))
print('The oldest man is {} years old and his name is {}.'.format(bageman, nameold))
print('Altogether there are {} women under 20 years old.'.format(totalwoman))
