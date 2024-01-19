import prompt
from random import randint


def welcome_user():
    print('Welcome to Brain Games!')
    player_name = prompt.string('May I have your name? ')
    print(f'Hello, {player_name}!')
    return player_name


def is_even(player_name):
    print('Answer "yes" if answer is even, otherwise answer "no".')
    last_answer = ''
    num = 0
    i = 0
    while i < 3:
        num = randint(1, 100)
        print('Question: ' + str(num))
        last_answer = input('Your answer: ')
        if num % 2 == 0 and last_answer == 'yes':
            print('Correct!')
            i += 1
        elif num % 2 != 0 and last_answer == 'no':
            print('Correct!')
            i += 1
        else:
            i = 4

    if i == 4 and num % 2 == 0:
        print(f'"{last_answer}" is wrong answer ;(. Correct answer was "yes".')
        print(f"Let's try again, {player_name}!")
    elif i == 4 and num % 2 != 0:
        print(f'"{last_answer}" is wrong answer ;(. Correct answer was "no".')
        print(f"Let's try agai, {player_name}!")
    else:
        print(f'Congratulations, {player_name}!')
