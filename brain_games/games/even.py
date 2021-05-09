from random import randint
TEXT_TASK = 'Answer "yes" if the number is even, otherwise answer "no".'

def even():
    question = randint(1, 100)
    if question % 2 == 0:
        real_answer = 'yes'
    else:
        real_answer = 'no'
    return (question, real_answer)


print(even())