from fractions import Fraction

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

print('Welcome to simplifying the surd.\nEnter the surd you want to simplify.')
unsimplified_root = input('> ')
print(convert_to_surd(unsimplified_root))