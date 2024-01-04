from manager.generation import generate_password as generate_pass
from manager.security import encrypt_data, check_password_usage


def generate_password() -> None:
    password = generate_pass()
    print('Your password is:', password)

    is_want_encrypt = input('Would you like to encrypt your password? (y/n)')
    if is_want_encrypt.lower() == 'y':
        print('Your encrypted password is: ', encrypt_data(password))

    print('See you next time!')


def ask_password() -> None:
    password = input('Enter your password: ')
    if check_password_usage(password):
        print('Your password under threat!')
    else:
        print('Your password is safe for now')


def main() -> None:
    chosen_dialog = input('Would you like to?(generate/check)')
    if chosen_dialog.lower() == 'check':
        ask_password()
    else:
        generate_password()
    main()


if __name__ == '__main__':
    main()
