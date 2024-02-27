from random import randint
from typing import Tuple

TITLE = 'Find the greatest common divisor of given numbers.'


def brain_gcd() -> Tuple[str, str]:
    """
    This function generates two random numbers.
    :return: Tuple with question string and correct answer string.
    """
    num1 = randint(1, 100)
    num2 = randint(1, 100)
    question = f'{num1} {num2}'
    while num1 != 0 and num2 != 0:
        if num1 > num2:
            num1 = num1 % num2
        else:
            num2 = num2 % num1
    correct_answer = str(num1 + num2)
    return question, correct_answer
