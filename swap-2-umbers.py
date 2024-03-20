#Swap 2 numbers.

def swap_numbers_without_temp(a, b):
    a = a + b
    b = a - b
    a = a - b
    return a, b

num1 = 5
num2 = 10
print(f"Before swapping: num1 = {num1}, num2 = {num2}")
num1, num2 = swap_numbers_without_temp(num1, num2)
print(f"After swapping: num1 = {num1}, num2 = {num2}")
