sumage = 0
averageage = 0
bageman = 0
nameold = ''
totalwoman = 0

for p in range(1, 5):
    print('----- {} PESSOA -----'.format(p))
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

print('A média de idade do grupo é de {} anos.'.format(averageage))
print('O homem mais velho tem {} anos e se chama {}.'.format(bageman, nameold))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(totalwoman))
