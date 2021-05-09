from random import randint


def even():
    question = randint(1, 100)
    if question % 2 == 0:
        real_answer = 'yes'
    else:
        real_answer = 'no'
    return (question, real_answer)


