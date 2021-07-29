headquarters = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for l in range(0, 3):
    for c in range(0, 3):
        headquarters[l][c] = int(input(f'Enter a value for [{l}, {c}]: '))

print('-=' * 30)

for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{headquarters[l][c]:^5}]', end='')
    print()
