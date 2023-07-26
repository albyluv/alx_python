# Write a Python function called is_prime that takes a number as input and returns True if the number is prime, and False otherwise.

def is_prime(number):
    if number <= 1:
        return False
    elif number == 2:
        return True
    else:
        for i in range(2,number):
            if number % i == 0:
                return False
        return True