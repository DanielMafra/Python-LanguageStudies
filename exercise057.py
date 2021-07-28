gender = str(input('Enter your gender: [M/F] ')).strip().upper()[0]

while gender not in 'MmFf':
    gender = str(
        input('Invalid, enter your gender again: [M/F] ')).strip().upper()[0]

print('Gender {} successfully registered'.format(gender))
