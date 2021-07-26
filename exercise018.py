from math import radians, sin, cos, tan

angle = float(input('Enter the angle you want: '))
sine = sin(radians(angle))
cosine = cos(radians(angle))
tangent = tan(radians(angle))

print('The angle of {} has a SINE of {:.2f}.'.format(angle, sine))
print('The angle of {} has a COSINE of {:.2f}.'.format(angle, cosine))
print('The angle of {} has a TANGENT of {:.2f}.'.format(angle, tangent))
