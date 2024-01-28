from random import randint


def brain_progression():
    title = 'What number is missing in the progression?'
    step = randint(1, 10)
    progression = [step]
    i = 0
    while i < 9:
        progression.append(progression[i] + step)
        i += 1
    correct_answer = progression[randint(0, len(progression) - 1)]
    question = ''
    for i in progression:
        if i == correct_answer:
            question += '.. '
        else:
            question += str(i) + ' '
    return title, question, str(correct_answer)
