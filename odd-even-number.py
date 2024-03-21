#Odd-Even Number.
def odd_even(num):
    if num % 2 == 0:
        return "even"
    else:
        return "odd"

# Test the function
number = int(input("Enter a number: "))
result = odd_even(number)
print(f"The number {number} is {result}.")
