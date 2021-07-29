temp = []
princ = []
mai = men = 0

while True:
    temp.append(str(input('Name: ')))
    temp.append(float(input('Weight: ')))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = str(input('Continue? [Y/N] '))
    if resp in 'Nn':
        break

print('-=' * 30)
print(f'In all, you registered {len(princ)} people')
print(f'The biggest weight was {mai}kg. Name: ', end='')

for p in princ:
    if p[1] == mai:
        print(f'[{p[0]}] ', end='')

print()
print(f'The smallest weight was {men}kg. Name: ', end='')

for p in princ:
    if p[1] == men:
        print(f'[{p[0]}] ', end='')

print()
