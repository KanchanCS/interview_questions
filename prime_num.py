# A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. In other words,
# a prime number is a number that is only divisible by 1 and itself.

# Here are a few examples of prime numbers:

# 2
# 3
# 5
def is_prime(num):
    """Return True if the input number is prim , otherwise return False."""
    # Numbers less than 2
    count = 0
    if num >= 1:
        for i in range(1, num+1):
            if num % i == 0:

                count += 1
    if count == 2:
        return f"{num} is a prime number."
    return f"{num} is not a prime number."        

# Test the function
number = int(input("Enter a number: "))
print(is_prime(number))




