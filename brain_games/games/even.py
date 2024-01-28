from random import randint


def brain_even():
    title = 'Answer "yes" if the number is even, otherwise answer "no".'
    question = randint(1, 100)
    if question % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return title, str(question), correct_answer
