# A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. In other words, a prime number is a number that is only divisible by 1 and itself.

# Here are a few examples of prime numbers:

# 2
# 3
# 5

def is_prime(num):
    if num <= 1:
        return False
    elif num <= 3:
        return True
    elif num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

# Test the function
number = int(input("Enter a number: "))
if is_prime(number):
    print(number, "is a prime number.")
else:
    print(number, "is not a prime number.")
