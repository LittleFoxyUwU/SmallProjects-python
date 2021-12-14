import random


def game():
    print('Starting game...')
    tries = 1
    num = random.randint(0, 100)
    while True:
        player_input = input('Enter your number! \n')
        if not is_valid(player_input):
            print('Your Input is invalid! Try Again!')
            continue

        if int(player_input) == num:
            print(f'You have guessed number after {tries} tries!')
            start_again()
            return
        else:
            print(f'Your number is {less_or_more(player_input, num)} than needed')
            tries += 1


def less_or_more(player_input, num):
    if int(player_input) < num:
        return 'less'
    else:
        return 'more'


def is_valid(num):
    if num.isdigit() and 0 <= int(num) <= 100:
        return True
    else:
        return False


def start_again():
    if input('Would you like to start again? Enter Y, y or yes. \n') in 'Yyes':
        game()
    else:
        print('Thank you for playing!')


print('Welcome to "Guess A Number"!')
game()

