import math

Tup = (1, 2, 3, -4, 5)  # Tuple Declaration
Lis = [-1, 2, -3.5, -4, 5]  # List Declaration

print('Absolute value of Positive Number = %.2f' % math.fabs(10))
print('Absolute value of Negative Number = %.2f' % math.fabs(-15))

print('Absolute value of Tuple Item = %.2f' % math.fabs(Tup[3]))
print('Absolute value of List Item = %.2f' % math.fabs(Lis[2]))

print('Absolute value of Multiple Number = %.2f' % math.fabs(10 + 20 - 40))
print('Absolute value of String Number = ', math.fabs('Hello'))
