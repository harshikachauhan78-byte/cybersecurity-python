import re

def check_password(password):
    score = 0

    # Check length
    if len(password) >= 8:
        score += 1

    # Check uppercase
    if re.search(r"[A-Z]", password):
        score += 1

    # Check lowercase
    if re.search(r"[a-z]", password):
        score += 1

    # Check number
    if re.search(r"[0-9]", password):
        score += 1

    # Check special character
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1

    # Display result
    if score <= 2:
        print("Password Strength: Weak")
    elif score == 3 or score == 4:
        print("Password Strength: Medium")
    else:
        print("Password Strength: Strong")

# Main program
password = input("Enter your password: ")
check_password(password)