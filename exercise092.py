from datetime import datetime

data = dict()
data['name'] = str(input('Name: '))
birth = int(input('Year birth: '))
data['age'] = datetime.now().year - birth
data['ctps'] = int(input('Work card (0 not have): '))

if data['ctps'] != 0:
    data['hiring'] = int(input('Year hiring: '))
    data['salary'] = float(input('Salary: U$'))
    data['retirement'] = data['age'] + \
        ((data['hiring'] + 35) - datetime.now().year)

print('-=' * 30)

for k, v in data.items():
    print(f'  - {k} have a value {v}')
