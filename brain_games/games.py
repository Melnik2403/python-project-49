from random import randint, choice


def brain_even():
    title = 'Answer "yes" if number is even, otherwise answer "no".'
    question = randint(1, 100)
    if question % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return title, str(question), correct_answer


def brain_calc():
    title = 'What is the result of the expression?'
    num1 = randint(1, 10)
    num2 = randint(2, 5)
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
