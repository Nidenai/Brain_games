from random import randint
from math import gcd


def generate():
    random_num_one = randint(1, 100)
    randon_num_two = randint(1, 100)
    question = str(random_num_one) + ' ' + str(randon_num_two)
    real_answer = gcd(random_num_one, randon_num_two)
    return (question,real_answer)


TASK_TEXT = 'Find the greatest common divisor of given numbers'
