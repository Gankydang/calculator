from math import sqrt
from sys import exit
from fractions import *

def quadratic_solutions(a, b, c):
    try:
        discriminant = Fraction((b**2) - 4 * a * c)
        sqrt_numerator = sqrt(discriminant.numerator)
        sqrt_denominator = sqrt(discriminant.denominator)
        if sqrt_numerator.is_integer() and sqrt_denominator.is_integer():
            sqrt_discriminant = Fraction(int(sqrt_numerator), int(sqrt_denominator))
        else:
            sqrt_discriminant = sqrt(discriminant)
    except:
        exit('THERE IS NO REAL SOLUTION')
    else:
        x1 = (-b + sqrt_discriminant) / (2 * a)
        x2 = (-b - sqrt_discriminant) / (2 * a)
    return {'x1': x1, 'x2': x2}

print('For f(x) = ax^2 + bx + c,\nenter the values of a, b and c')
a = Fraction(input('a: '))
b = Fraction(input('b: '))
c = Fraction(input('c: '))
if a == 0 or b == 0 or c == 0:
    exit('CANNOT BE ZERO')

solutions = quadratic_solutions(a, b, c)
if solutions['x1'] == solutions['x2']:
    print('x =', solutions['x1'])
else:
    print('x =', solutions['x1'], 'or', solutions['x2'])
