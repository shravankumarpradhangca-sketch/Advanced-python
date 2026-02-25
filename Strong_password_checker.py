# Strong Password Checker System
import re


def is_strong_password(password):
    

    # Check minimum length
    if len(password) < 8:
        return False

    # Check for uppercase letter
    if not re.search(r"[A-Z]", password):
        return False

    # Check for lowercase letter
    if not re.search(r"[a-z]", password):
        return False

    # Check for digit
    if not re.search(r"[0-9]", password):
        return False

    # Check for special character
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False

    return True


    