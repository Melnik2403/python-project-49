from random import randint


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
