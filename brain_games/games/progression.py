from random import randint
from typing import Tuple

TITLE = 'What number is missing in the progression?'


def brain_progression() -> Tuple[str, str]:
    """
    This function generates random progression of 10 numbers,
    one of the numbers in hidden.
    :return: Tuple with question string and correct answer string.
    """
    step = randint(1, 10)
    progression = list(range(step, step * 10, step))
    correct_answer = progression[randint(0, len(progression) - 1)]
    progression[progression.index(correct_answer)] = '..'
    question = ' '.join(map(str, progression))
    return str(question), str(correct_answer)
