"""
Jordan
"""

MIN_LENGTH = 2


def main():
    password = input('Enter password')
    while not is_valid_password(password):
        print('Invalid password,try again')
        password = input('Enter password')
    for char in password:
        print('*', end="")


def is_valid_password(password):
    if len(password) < MIN_LENGTH:
        return False
    return True


main()
