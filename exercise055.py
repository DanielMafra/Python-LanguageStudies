bigg = 0
small = 0

for w in range(1, 6):
    weight = float(input('Weight of {} person: '.format(w)))
    if w == 1:
        bgg = weight
        small = weight
    else:
        if weight > bigg:
            bigg = weight
        if weight < small:
            small = weight

print('The greatest weight read was {}kg.'.format(bigg))
print('The smallest weight read was {}kg.'.format(small))
