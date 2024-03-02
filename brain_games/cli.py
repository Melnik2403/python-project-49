import prompt
from typing import Callable, Tuple


def welcome_user() -> str:
    """
    This function welcomes user and asks for his name.
    :return: Users name.
    """
    print('Welcome to the Brain Games!')
    player_name = prompt.string('May I have your name? ')
    print(f'Hello, {player_name}!')
    return player_name


def ask_question(player_name: str, title: str,
                 game: Callable[[], Tuple[str, str]]):
    """
    This function plays 3 rounds of some game with user.
    :param player_name: Name of the player.
    :param game: Game function.
    """
    print(title)
    last_answer = ''
    correct_answer = ''
    i = 0
    while i < 3:
        round = game()
        print('Question: ' + round[0])
        last_answer = input('Your answer: ')
        correct_answer = round[1]
        if last_answer == correct_answer:
            print('Correct!')
            i += 1
        else:
            break

    if last_answer == correct_answer:
        print(f'Congratulations, {player_name}!')
    else:
        print(f'"{last_answer}" is wrong answer ;(. '
              f'Correct answer was {correct_answer}.')
        print(f"Let's try again, {player_name}!")
