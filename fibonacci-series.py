# Python Program for Fibonacci numbers using Recursion 

def fib(num):
    if num <=1:
        return num
    else:
        return fib(num-1) +fib(num-2)
    
num = 4
print(fib(num))    
        

