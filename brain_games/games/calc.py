from random import randint
from random import choice


TASK_TEXT = 'What is the result of the expression?'


def calculate(a, b, symbol):
    if symbol == '+':
        return a + b
    if symbol == '-':
        return a - b
    else:
        return a * b



def generate_round():
    num1 = randint(1, 100)
    num2 = randint(1, 100)
    symb = choice(['+', '-', '*'])
    real_answer = calculate(num1, num2, symb)
    question = (f'{num1} {symb} {num2}')
    return question, real_answer
