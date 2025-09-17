#Password Strength Checker: Input: string → check length ≥ 8, contains a digit, contains uppercase.
password = input("Enter a password: ")
has_upper = any(c.isupper() for c in password)
has_digit = any(c.isdigit() for c in password)
if len(password) >= 8 and has_upper and has_digit:
    print("Strong Password")
else:
    print("Weak Password")
    if not len(password) >= 8:
        print("- Password must be at least 8 characters long")
    if not has_digit:
        print("- Password must contain at least one digit")
    if not has_upper:
        print("- Password must contain at least one uppercase letter")