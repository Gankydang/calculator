from fractions import Fraction
from sys import exit
from math import *

def f(x, eqn):
    try:
        value = eval(eqn)
        return value
    except:
        return 'not valid'

def gradient(x, eqn):
    h = 10**(-9)
    if f(x, eqn) == 'not valid':
        print('THIS IS NOT A VALID EQUATION OR VALUE OF X')
        exit()
    else:
        return (f(x + h, eqn) - f(x, eqn)) / h
        
def is_prime(number):
    '''returns True if is prime number, False if not'''
    number = int(number)
    if number > 1:
        for i in range(2, int(number / 2) + 1):
            if (number % i) == 0:
                return False
        return True
    return False

def solve_simul_eqn(a, b, c, a2, b2, c2):
    '''returns a list of the values of x and y'''
    b = -b
    new_b = b / a * a2
    new_c = c / a * a2
    y_coeff = new_b + b2
    y = (-new_c + c2) / y_coeff
    x = (y * b + c) / a
    return [x, y]

def add_or_subtract(value):
    '''returns a string of a number with its corresponding sign'''
    if value == 0:
        return 'no const'
    elif value > 0:
        value = '+ ' + str(value)
    else:
        value = str(value)
        value = value[:1] + ' ' + value[1:]
    return value

def complete_the_square(a, b, c):
    '''returns the completed square form of the given equation in a string'''
    if a == 0 or b == 0:
        exit('CANNOT COMPLETE THE SQUARE')

    final_b = Fraction(b, a) / 2
    final_constant = c - a * final_b ** 2

    final_b_with_sign = add_or_subtract(final_b)
    final_constant_with_sign = add_or_subtract(final_constant)

    if final_constant_with_sign == 'no const':
        return f'(x {final_b_with_sign})**2'
    elif a == 1:
        return f'(x {final_b_with_sign})**2 {final_constant_with_sign}'
    else:
        return f'{a}(x {final_b_with_sign})**2 {final_constant_with_sign}'

def quadratic_solutions(a, b, c):
    '''returns a dictionary of the 2 values of x (as integers) from the given equation'''
    try:
        discriminant = Fraction((b**2) - 4 * a * c)
        sqrt_numerator = sqrt(discriminant.numerator)
        sqrt_denominator = sqrt(discriminant.edenominator)
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

def convert_to_surd(unsimplified_root):
    '''returns the surd of an unsimplified_root'''
    smallest_newer_number = last_multiple = 10 ** 10
    number = int(unsimplified_root[:unsimplified_root.index('*')])
    power = Fraction(unsimplified_root[unsimplified_root.index('*') + 2:])
    number **= power.numerator

    for multiple in range(2, int((number / 2)) + 1):
        new_number = number / multiple
        if new_number.is_integer():
            newer_multiple = multiple ** (1 / power.denominator)

            if newer_multiple.is_integer():
                if new_number < smallest_newer_number:
                    smallest_newer_number = new_number
                    last_multiple = newer_multiple

    return f'({int(last_multiple)})({int(smallest_newer_number)})**1/{power.denominator}'
