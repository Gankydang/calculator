from fractions import Fraction

def solve_simul_eqn(a, b, c, a2, b2, c2):
    b = -b
    new_b = b / a * a2
    new_c = c / a * a2
    y_coeff = new_b + b2
    y = (-new_c + c2) / y_coeff
    x = (y * b + c) / a
    return [x, y]

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
