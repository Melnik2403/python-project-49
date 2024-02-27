from random import randint
from typing import Tuple

TITLE = 'Answer "yes" if the number is even, otherwise answer "no".'


def brain_even() -> Tuple[str, str]:
    """
    This function generates random number.
    :return: Tuple with question string and correct answer string.
    """
    question = randint(1, 100)
    if question % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return str(question), correct_answer
