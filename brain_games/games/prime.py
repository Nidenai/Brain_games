from random import randint

TASK_TEXT = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def prime_check(n):
    if n < 2:
        return False
    d = 2
    while d * d <= n and n % d != 0:
        d += 1
    return d * d > n


def generate_round():
    question = randint(0, 1000)
    required_num = prime_check(question)
    if required_num is True:
        real_answer = 'yes'
    else:
        real_answer = 'no'
    return question, real_answer
