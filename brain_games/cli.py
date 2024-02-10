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


def ask_question(player_name, game):
    print(game.__call__()[0])
    last_answer = ''
    correct_answer = ''
    i = 0
    while i < 3:
        round = game.__call__()
        print('Question: ' + round[1])
        last_answer = input('Your answer: ')
        correct_answer = round[2]
        if last_answer == correct_answer:
            print('Correct!')
            i += 1
        else:
            break
    tell_result(player_name, last_answer, correct_answer)
