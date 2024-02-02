from random import randint, choice


def brain_calc():
    title = 'What is the result of the expression?'
    num1 = randint(1, 5)
    num2 = randint(1, 5)
    operator = choice('+-*')
    question = f'{num1} {operator} {num2}'
    correct_answer = str(eval(question))
    return title, question, correct_answer
