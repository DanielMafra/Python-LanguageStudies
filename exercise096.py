def area(width, height):
    a = width * height
    print(f'Area {width}x{height} is {a}m²')


print('Control land')
print('-' * 20)
l = float(input('Width: '))
c = float(input('Height: '))
area(l, c)
