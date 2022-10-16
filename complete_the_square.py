from fractions import Fraction
from sys import exit

def add_or_subtract(value):
    if value == 0:
        return 'no const'
    elif value > 0:
        value = '+ ' + str(value)
    else:
        value = str(value)
        value = value[:1] + ' ' + value[1:]
    return value

def complete_the_square(a, b, c):
    if a == 0 or b == 0:
        exit('CANNOT COMPLETE THE SQUARE')

    final_b = Fraction(b, a) / 2
    final_constant = c - a * final_b ** 2

    final_b_with_sign = add_or_subtract(final_b)
    final_constant_with_sign = add_or_subtract(final_constant)

    if final_constant_with_sign == 'no const':
        return f'(x {final_b_with_sign})^2'
    elif a == 1:
        return f'(x {final_b_with_sign})^2 {final_constant_with_sign}'
    else:
        return f'{a}(x {final_b_with_sign})^2 {final_constant_with_sign}'


print('For f(x) = ax^2 + bx + c,\nenter the values of a, b and c')
a = Fraction(input('a: '))
b = Fraction(input('b: '))
c = Fraction(input('c: '))

print('After completing the square: ' + complete_the_square(a, b, c))
