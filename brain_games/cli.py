import prompt


def welcome_user():
    print('Welcome to the Brain Games!')
    player_name = prompt.string('May I have your name? ')
    print(f'Hello, {player_name}!')
    return player_name


def tell_result(player_name, last_answer, correct_answer):
    if last_answer == correct_answer:
        print(f'Congratulations, {player_name}!')
    else:
        print(f'"{last_answer}" is wrong answer ;(. '
              f'Correct answer was {correct_answer}.')
        print(f"Let's try again, {player_name}!")


def ask_question(player_name, round1, round2, round3):
    print(round1[0])
    print('Question: ' + round1[1])
    last_answer = input('Your answer: ')
    if last_answer == round1[2]:
        print('Correct!')
    else:
        return tell_result(player_name, last_answer, round1[2])
    print('Question: ' + round2[1])
    last_answer = input('Your answer: ')
    if last_answer == round2[2]:
        print('Correct!')
    else:
        return tell_result(player_name, last_answer, round2[2])
    print('Question: ' + round3[1])
    last_answer = input('Your answer: ')
    if last_answer == round3[2]:
        print('Correct!')
    else:
        return tell_result(player_name, last_answer, round3[2])
    tell_result(player_name, last_answer, round3[2])
