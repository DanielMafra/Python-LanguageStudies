tot18 = totM = totW20 = 0

while True:
    age = int(input('Age: '))
    gender = ' '
    while gender not in 'MF':
        gender = str(input('Gender: [M/F] ')).strip().upper()[0]
    if age >= 18:
        tot18 += 1
    if gender == 'M':
        totM += 1
    if gender == 'F' and age < 20:
        totW20 += 1
    answer = ' '
    while answer not in 'YN':
        answer = str(input('Continue? [Y/N]')).strip().upper()[0]
    if answer == 'N':
        break

print(f'Total people over 18 years old: {tot18}')
print(f'Altogether we have {totM} registered men')
print(f'And we have {totW20} women under the age of 20')
