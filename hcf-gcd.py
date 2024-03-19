
#Here's a Python program to find the Highest Common Factor (HCF) or Greatest Common Divisor 
# (GCD) of two numbers using the Euclidean algorithm:

def hcf_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Test the function
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

result = hcf_gcd(num1, num2)
print("The HCF/GCD of", num1, "and", num2, "is", result)
