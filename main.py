from generation import generate_password
from security import encrypt, check_password


def start_generate_dialog():
    password = generate_password()
    print('Your password is:', password)

    is_want_encrypt = input('Would you like to encrypt your password? (y/n)')
    if is_want_encrypt.lower() == 'y':
        print('Your encrypted password is: ', encrypt(password))

    print('See you next time!')


def start_check_dialog():
    password = input('Enter your password: ')
    if check_password(password):
        print('Your password under threat!')
    else:
        print('Your password is safe for now')


def main():
    chosen_dialog = input('Would you like to?(generate/check)')
    if chosen_dialog.lower() == 'check':
        start_check_dialog()
    else:
        start_generate_dialog()
    main()


if __name__ == '__main__':
    main()
