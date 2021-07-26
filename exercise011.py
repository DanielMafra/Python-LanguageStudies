width = float(input('Wall width: '))
height = float(input('Wall height: '))
area = width * height
paint = area / 2

print('Its wall has a dimension of {}x{} and its area is {}m².'.format(
    width, height, area))
print('To paint this wall, you will need {}l of paint.'.format(paint))
