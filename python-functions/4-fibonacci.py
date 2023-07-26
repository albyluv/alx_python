# Write a Python function called fibonacci_sequence that takes a number n as input and returns a list of the first n Fibonacci numbers.

def fibonacci_sequence(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0,1]
    else:
        fib = [0,1]
        for i in range(2,n):
            fib.append(fib[i-1] + fib[i-2])
        return fib