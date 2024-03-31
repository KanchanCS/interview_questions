#Question 1: Find the Largest Number Write a Python function to find the largest number in a list of integers.
#The function should take a list of numbers as input and return the largest number.
# Input: [10, 20, 4, 45, 99]
# Output: 99


def largest_num(numbers):
    max = numbers[0]
    for num in numbers:
        if num > max:
            max = num
    return max

print(largest_num([10, 20, 4,  45, 99]))
    
