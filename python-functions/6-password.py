# Write a Python function called validate_password that takes a password as input and performs the following checks:
# 1. The password must be at least 8 characters long.
# 2. The password must not contain any spaces.
# 3. The password must contain at least one uppercase letter.

def validate_password(password):
    if len(password) < 8:
        return False
    elif " " in password:
        return False
    elif password.isalnum() == False:
        return False
    elif password.islower() == True:
        return False
    elif password.isupper() == True:
        return False
    else:
        return True