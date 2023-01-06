from math import sqrt
from time import time

def is_prime(number):
    number = int(number)
    if number == 2:
        return True
    if number > 1:
        number_sqrt = int(sqrt(number))
        for i in range(2, number_sqrt + 1):
            if (number % i) == 0:
                return False
        return True
    else:
        return False

print('Enter the min value(inclusive) and the max value(not inclusive) with a space in between OR')
print('Enter a number to check whether it is a prime number')
numbers = input('> ').split()

start_time = time()

if len(numbers) == 1:
    print(is_prime(numbers[0]))
else:
    prime_numbers = filter(is_prime, range(int(numbers[0]), int(numbers[len(numbers) - 1])))
    yes = map(str, prime_numbers)
    print(' '.join(yes))

end_time = time()
print(f'Time elapsed: {end_time - start_time}')
