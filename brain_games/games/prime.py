from random import randint


def IsPrime(n):
    d = 2
    while d * d <= n and n % d != 0:
        d += 1
    return d * d > n


def generate():
    question = randint(2, 1000)
    required_num = IsPrime(question)
    if required_num is True:
        real_answer = 'yes'
    else:
        real_answer = 'no'
    return (question, real_answer)


TASK_TEXT = 'Answer "yes" if given number is prime. Otherwise answer "no".'
