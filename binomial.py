import re
from math import factorial
from fractions import Fraction

class Input:
    def __init__(self, a_or_b):
        self.a_or_b = a_or_b
    
    def get_nums(self):
        splitted_list = re.split(r'x\*?\*?\^?', self.a_or_b)

        if len(splitted_list) == 2:
            x_coeff, x_pow = splitted_list
        else:
            x_coeff = splitted_list[0]
            x_pow = 0

        if x_coeff == '-':
            x_coeff = -1
        if x_coeff == '':
            x_coeff = 1
        if x_pow == '':
            x_pow = 1

        x_coeff = Fraction(x_coeff)
        x_pow = Fraction(x_pow)

        return [x_coeff, x_pow]

def ncr(n, r):
    return int(factorial(n) // factorial(n-r) // factorial(r))

def find_x_term(a, b, n, r):
    x_coeffa, x_powa = a
    x_coeffb, x_powb = b

    ttl_coeff = x_coeffa**(n-r) * x_coeffb**r * ncr(n, r)
    ttl_x_pow = x_powa*(n-r) + x_powb*r
    return [ttl_coeff, ttl_x_pow]

print('Welcome to binomial expansion calculator.')
choice = input('Expand or find term? (exp/term)\n> ').strip()

if choice.startswith('e'):
    print('\nFor (a + b)^n, enter the values of a, b, n.')
    a = input('a: ').strip()
    b = input('b: ').strip()
    n = int(input('n: ').strip()) 
    print()

    for_a = Input(a)
    for_b = Input(b)

    a = for_a.get_nums()
    b = for_b.get_nums()

    l = []
    for r in range(0, n+1):
        l.append(find_x_term(a, b, n, r))
    
    first = second = third = x = ''
    for coeff, power in l:
        if coeff < 0:
            first = ' -  '
            second = abs(coeff)
        if coeff > 0:
            first = ' +  '
            second = coeff
        if power == 0:
            x = ''
            third = ''
        if power == 1:
            x = ' x'
            third = ''
        if power > 1:
            x = ' x^'
            third = power
        if l.index([coeff, power]) == 0:
            first = ''
            second = coeff
            x = x.strip()
        if coeff == 1:
            first = ''
            second = ''
        if coeff == -1 and power != 0:
            second = ''
            if l.index([coeff, power]) == 0:
                second = '-'
        print(f'{first}{second}{x}{third}', end=' ')

elif choice.startswith('t'):
    print('\nFor (a + b)^n, enter the values of a, b, n, term.')
    a = input('a: ').strip()
    b = input('b: ').strip()
    n = int(input('n: ').strip()) 
    term = int(input('term: ').strip())
    print()

    for_a = Input(a)
    for_b = Input(b)

    a = for_a.get_nums()
    b = for_b.get_nums()

    coeff, power = find_x_term(a, b, n, term-1)
    if coeff == 1:
        print(f'x^{power}')  
    elif power == 0:
        print(f'{coeff}')
    elif power == 1:
        print(f'{coeff} x')
    elif coeff == -1:
        print(f'-x^{power}')
    else:
        print(f'{coeff} x^{power}')
