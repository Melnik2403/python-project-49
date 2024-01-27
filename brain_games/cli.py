import prompt
from random import randint, choice


def welcome_user():
    print('Welcome to Brain Games!')
    player_name = prompt.string('May I have your name? ')
    print(f'Hello, {player_name}!')
    return player_name


def tell_result(player_name, last_answer, correct_answer):
    if last_answer == correct_answer:
        print(f'Congratulations, {player_name}!')
    else:
        print(f'"{last_answer}" is wrong answer ;(. Correct answer was {correct_answer}.')
        print(f"Let's try again, {player_name}!")


def ask_question(player_name, round1, round2, round3):
    print(round1[0])
    print('Question: ' + round1[1])
    last_answer = input('Your answer: ')
    if last_answer == round1[2]:
        print('Correct!')
    else:
        return tell_result(player_name, last_answer, round1[2])
    print('Question: ' + round2[1])
    last_answer = input('Your answer: ')
    if last_answer == round2[2]:
        print('Correct!')
    else:
        return tell_result(player_name, last_answer, round2[2])
    print('Question: ' + round3[1])
    last_answer = input('Your answer: ')
    if last_answer == round3[2]:
        print('Correct!')
    else:
        return tell_result(player_name, last_answer, round3[2])
    tell_result(player_name, last_answer, round3[2])


def brain_even():
    title = 'Answer "yes" if answer is even, otherwise answer "no".'
    question = randint(1, 100)
    if question % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return title, str(question), correct_answer


def brain_calc():
    title = 'What is the result of the expression?'
    num1 = randint(15, 30)
    num2 = randint(2, 10)
    operator = choice('+-*')
    question = f'{num1} {operator} {num2}'
    correct_answer = str(eval(question))
    return title, question, correct_answer


def brain_gcd():
    title = 'Find the greatest common divisor of following numbers.'
    num1 = randint(1, 100)
    num2 = randint(1, 100)
    question = f'{num1} {num2}'
    while num1 != 0 and num2 != 0:
        if num1 > num2:
            num1 = num1 % num2
        else:
            num2 = num2 % num1
    correct_answer = str(num1 + num2)
    return title, question, correct_answer


def brain_progression():
    title = 'What number is missing in the progression?'
    step = randint(1, 10)
    progression = [step]
    i = 0
    while i < 9:
        progression.append(progression[i] + step)
        i += 1
    correct_answer = progression[randint(0, len(progression) - 1)]
    question = ''
    for i in progression:
        if i == correct_answer:
            question += '.. '
        else:
            question += str(i) + ' '
    return title, question, str(correct_answer)


def brain_prime():
    title = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    num = randint(2, 100)
    correct_answer = ''
    if num == 2 or num == 3:
        correct_answer = 'yes'
    i = 2
    while i < num - 1:
        if num % i == 0:
            correct_answer = 'no'
            break
        else:
            correct_answer = 'yes'
        i += 1
    return title, str(num), correct_answer
