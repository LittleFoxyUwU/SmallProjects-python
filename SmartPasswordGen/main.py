import random

digits = '23456789'
lowercase_letters = 'abcdefghjkmnpqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKMNPQRSTUVWXYZ'
symbols = '!#$%&*+-=?@^_.'
bad_symbols = 'il1Lo0O'


def create_password(amount, length, have_digits, have_upcase, have_lowercase, have_symbols, have_bad_symbols):
    chars = str()
    if have_digits:
        chars += digits
    if have_upcase:
        chars += uppercase_letters
    if have_lowercase:
        chars += lowercase_letters
    if have_symbols:
        chars += symbols
    if have_bad_symbols:
        chars += bad_symbols

    if len(chars) == 0:
        print('Error: no chars to create password (You didn\'t select any parameters!')
        password_rules_input()
        return

    for _ in range(amount):
        password = str()
        for _ in range(length):
            password += chars[random.randint(0, len(chars) - 1)]
        print(password)

    if input('Want to create more passwords? Input Yes to continue!').lower() in 'yes':
        password_rules_input()
        return
    else:
        print('See you later then!')
        return


def password_rules_input():
    amount = int(input('Enter amount of passwords to generate\n'))
    length = int(input('Enter amount of chars in each password\n'))
    if input('Will your password/s will have digits? input yes to include them, or anything else to exclude!\n').lower() in 'yes':
        have_digits = True
    else:
        have_digits = False

    if input('Will your password/s will have UPPERCASE LETTERS input yes to include them, or anything else to '
             'exclude!\n').lower() in 'yes':
        have_uppercase = True
    else:
        have_uppercase = False

    if input('Will your password/s will have lowercase letters? input yes to include them, or anything else to '
             'exclude!\n').lower() in 'yes':
        have_lowercase = True
    else:
        have_lowercase = False

    if input('Will your password/s will have symbols (!#$%&*+-=?@^_.)? Input yes to include them, or anything else to '
             'exclude!\n').lower() in 'yes':
        have_symbols = True
    else:
        have_symbols = False

    if input('Will your password/s will have bad symbols (il1Lo0O)? Input yes to include them, or anything else to '
             'exclude!\n').lower() in 'yes':
        have_bad_symbols = True
    else:
        have_bad_symbols = False

    print(f'Your password/s atributes:\n'
          f'Amount of passwords = {amount}\n'
          f'Length of each password = {length}\n'
          f'Digits = {have_digits}\n'
          f'Uppercase letters = {have_uppercase}\n'
          f'Lowercase letters = {have_lowercase}\n'
          f'Symbols = {have_symbols}\n'
          f'Bad Symbols = {have_bad_symbols}\n')
    if input('Do you agree with those attributes? Print yes to start generating, or anything else if you want to '
             're-enter them!\n').lower() in 'yes':
        create_password(amount, length, have_digits, have_uppercase, have_lowercase, have_symbols, have_bad_symbols)
        return
    else:
        password_rules_input()
        return


print("*****WELCOME TO PASSWORD GENERATOR")
password_rules_input()
input()