"""
Jordan
"""

MIN_LENGTH = 2


def main():
    password = get_password()
    convert_password_to_asterisk(password)


def convert_password_to_asterisk(password):
    for char in password:
        print('*', end="")


def get_password():
    password = input('Enter password: ')
    while not is_valid_password(password):
        print('Invalid password,try again')
        password = input('Enter password')
    return password


def is_valid_password(password):
    if len(password) < MIN_LENGTH:
        return False
    return True


main()
