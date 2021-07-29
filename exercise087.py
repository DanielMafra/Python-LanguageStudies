headquarters = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = mai = scol = 0

for l in range(0, 3):
    for c in range(0, 3):
        headquarters[l][c] = int(input(f'Enter a value for [{l}, {c}]: '))

print('-=' * 30)

for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{headquarters[l][c]:^5}]', end='')
        if headquarters[l][c] % 2 == 0:
            spar += headquarters[l][c]
    print()

print('-=' * 30)
print(f'Sum pairs: {spar}')

for l in range(0, 3):
    scol += headquarters[l][2]

print(f'Sum third column: {scol}')

for c in range(0, 3):
    if c == 0:
        mai = headquarters[1][c]
    elif headquarters[1][c] > mai:
        mai = headquarters[1][c]

print(f'Highest value second row: {mai}')
