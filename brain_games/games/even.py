from random import randint


def even():
    question = randint(1, 100)
    if question % 2 == 0:
        real_answer = 'yes'
    else:
        real_answer = 'no'
    task_text = 'Answer "yes" if the number is even, otherwise answer "no".'
    return (task_text, question, real_answer)


print(even())