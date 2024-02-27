from random import randint, choice
from typing import Tuple

TITLE = 'What is the result of the expression?'


def brain_calc() -> Tuple[str, str]:
    """
    This function generates math expression with two random operands
    and ether +, -, or * operator.
    :return: Tuple with question string and correct answer string.
    """
    num1 = randint(5, 10)
    num2 = randint(2, 5)
    operator = choice('+-*')
    question = f'{num1} {operator} {num2}'
    correct_answer = 0
    match operator:
        case '+':
            correct_answer = num1 + num2
        case '-':
            correct_answer = num1 - num2
        case '*':
            correct_answer = num1 * num2
    return question, str(correct_answer)
