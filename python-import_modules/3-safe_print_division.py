# Write a function that divides 2 integers and prints the result.

def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
        return None
    finally:
        print("Inside result: {}".format(result))
    return result