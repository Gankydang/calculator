from math import *
from sys import *

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

print('Let f(x) be a function of x\nEnter the function f(x).')
equation = input('f(x) = ')
print('Enter the value of x')
x = eval(input('x = '))
print(f'Gradient at x = {x} is: {round(gradient(x, equation), 5)}')
