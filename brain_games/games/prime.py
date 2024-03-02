from random import randint
from typing import Tuple

TITLE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def brain_prime() -> Tuple[str, str]:
    """
    This function generates random number.
    :return: Tuple with question string and correct answer string.
    """
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
    return str(num), correct_answer
