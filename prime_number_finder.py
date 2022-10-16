def is_prime(number):
    number = int(number)
    if number > 1:
        for i in range(2, int(number / 2) + 1):
            if (number % i) == 0:
                return False
        return True
    return False

print('Enter the min value(inclusive) and the max value(not inclusive) with a space in between OR')
print('Enter a number to check whether it is a prime number')
numbers = input().split()

if len(numbers) == 1:
    print(is_prime(numbers[0]))
else:
    prime_numbers = filter(is_prime, range(int(numbers[0]), int(numbers[len(numbers) - 1])))
    yes = map(str, prime_numbers)
    print(' '.join(yes))
