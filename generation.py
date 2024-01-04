from string import ascii_letters, digits, punctuation
from random import choice
from security import check_password


def generate_password(length=6, chars=ascii_letters + digits + punctuation) -> str:
    while True:
        password = ''.join(choice(chars) for _ in range(length))
        if check_password(password):
            return password
    