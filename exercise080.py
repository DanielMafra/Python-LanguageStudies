mlist = []

for c in range(0, 5):
    n = int(input('Enter a value: '))
    if c == 0 or n > mlist[-1]:
        mlist.append(n)
        print('Added to end of list...')
    else:
        pos = 0
        while pos < len(mlist):
            if n <= mlist[pos]:
                mlist.insert(pos, n)
                print(f'Added at position {pos} of the list')
                break
            pos += 1

print('-=' * 30)
print(f'The values entered in order were {mlist}')
