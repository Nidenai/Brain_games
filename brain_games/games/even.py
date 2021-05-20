from random import randint


TASK_TEXT = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate():
    question = randint(1, 100)
    if question % 2 == 0:
        real_answer = 'yes'
    else:
        real_answer = 'no'
    return (question, real_answer)
