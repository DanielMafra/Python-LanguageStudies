print('=' * 30)
print('{:^30}'.format('BANK CEV'))
print('=' * 30)

value = int(input('What amount do you want to withdraw? U$'))
total = value
ced = 50
totced = 0

while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total of {totced} U${ced} bills')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break

print('=' * 30)
print('Always come back to BANK CEV! Have a nice day!')
