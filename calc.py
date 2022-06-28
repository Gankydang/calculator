from my_math import *

def calculator():
    answer = input('What would you like to calculate: ').lower().strip()

    if answer == 'simultaneous equations' or answer == 'simul eqn':
        print('First equation: Ax + By = C')
        a = Fraction(input('A: '))
        b = Fraction(input('B: '))
        c = Fraction(input('C: '))
        print('Second equation: Dx + Ey = F')
        d = Fraction(input('D: '))
        e = Fraction(input('E: '))
        f = Fraction(input('F: '))

        x, y = solve_simul_eqn(a, b, c, d, e, f)
        print()
        print(f'x = {x}')
        print(f'y = {y}')

    elif answer == 'complete the square' or answer == 'complete square' or answer == 'complete sq':
        print('For f(x) = ax**2 + bx + c,\nenter the values of a, b and c')
        a = Fraction(input('a: '))
        b = Fraction(input('b: '))
        c = Fraction(input('c: '))

        print('After completing the square: ' + complete_the_square(a, b, c))

    elif answer == 'quadratic equation' or answer == 'quadratic':
        print('For f(x) = ax**2 + bx + c,\nenter the values of a, b and c')
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

    elif answer == 'prime number' or answer == 'prime':
        print('Enter the min value (inclusive) and the max value (not inclusive) with a space in between OR')
        print('Enter a number to check whether it is a prime number')
        numbers = input().split()

        if len(numbers) == 1:
            print(is_prime(numbers[0]))
        else:
            prime_numbers = filter(is_prime, range(int(numbers[0]), int(numbers[len(numbers) - 1])))
            yes = map(str, prime_numbers)
            print(' '.join(yes))

    elif answer == 'gradient':
        print('Let f(x) be a function of x\nEnter the function f(x).')
        equation = input('f(x) = ')
        print('Enter the value of x')
        x = eval(input('x = '))
        print(f'Gradient at x = {x} is: {round(gradient(x, equation), 5)}')

    elif answer == 'arithmetic':
        print(eval(input('> ')))

    elif answer == 'surd':
        unsimplified_root = input('> ')
        print(convert_to_surd(unsimplified_root))

    elif answer == 'help':
        print('key:\nsimultaneous equations\ncomplete the square\nquadratic equation\nprime number\ngradient\narithmetic')
        print('surd')
        calculator()
    else:
        print('Unable to calculate')
        calculator()
print('Welcome to the greatest calculator in the world')
calculator()
