
password = input("Enter your password: ")

# Check for all the required conditions
has_upper = any(char.isupper() for char in password)
has_lower = any(char.islower() for char in password)
has_digit = any(char.isdigit() for char in password)
is_long_enough = len(password) >= 8

# Final decision
if has_upper and has_lower and has_digit and is_long_enough:
    print("Password is strong")
else:
    print("Password is weak")
