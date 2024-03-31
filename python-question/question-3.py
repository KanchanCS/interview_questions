# Question 3: Fibonacci Series Write a Python function to generate the Fibonacci series up
# to a specified number of terms. The Fibonacci sequence is calculated by adding the previous two terms.

# Example:

# Input: 7
# Output: 0, 1, 1, 2, 3, 5, 8


def fibonacci_series(n):
    fib_series = [0, 1]
    for i in range(2, n):
        next_fib = fib_series[-1] + fib_series[-2]
        fib_series.append(next_fib)
    
    return fib_series

nums = 7
print("Input:", nums)
print("Output:", fibonacci_series(nums))
