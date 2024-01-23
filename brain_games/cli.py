import prompt
from random import randint, choice


def welcome_user():
    print('Welcome to Brain Games!')
    player_name = prompt.string('May I have your name? ')
    print(f'Hello, {player_name}!')
    return player_name


def tell_result(player_name, correct_answer, last_answer):
    if last_answer == correct_answer:
        print(f'Congratulations, {player_name}!')
    else:
        print(f'"{last_answer}" is wrong answer ;(. Correct answer was {correct_answer}.')
        print(f"Let's try again, {player_name}!")


def is_even(player_name):
    print('Answer "yes" if answer is even, otherwise answer "no".')
    last_answer = ''
    correct_answer = ''
    i = 0
    while i < 3:
        num = randint(1, 100)
        if num % 2 == 0:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'
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
    tell_result(player_name, correct_answer, last_answer)


def brain_calc(player_name):
    print('What is the result of the expression?')
    last_answer = ''
    correct_answer = ''
    i = 0
    while i < 3:
        num1 = randint(15, 30)
        num2 = randint(2, 10)
        operator = choice('+-*')
        expression = f'{num1} {operator} {num2}'
        correct_answer = str(eval(str(num1) + operator + str(num2)))
        print(f'Question: ' + str(expression))
        last_answer = input('Your answer: ')
        if last_answer == correct_answer:
            print('Correct!')
            i += 1
        else:
            i = 3
    tell_result(player_name, correct_answer, last_answer)
