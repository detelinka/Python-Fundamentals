def is_valid_password(password: str) -> None:
    is_valid = True

    # 1. Length check
    if not (6 <= len(password) <= 10):
        print("Password must be between 6 and 10 characters")
        is_valid = False

    # 2. Letters & digits only
    if not password.isalnum():
        print("Password must consist only of letters and digits")
        is_valid = False

    # 3. At least 2 digits
    digit_count = sum(1 for ch in password if ch.isdigit())
    if digit_count < 2:
        print("Password must have at least 2 digits")
        is_valid = False

    # 4. If all checks passed
    if is_valid:
        print("Password is valid")


# Example usage:
pwd = input()
is_valid_password(pwd)
