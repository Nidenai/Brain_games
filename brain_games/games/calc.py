from random import choice, randint

TASK_TEXT = 'What is the result of the expression?'


def calculate(num1, num2, symbol):
    if symbol == '+':
        return num1 + num2
    elif symbol == '-':
        return num1 - num2
    return num1 * num2


def generate_round():
    num1 = randint(1, 100)
    num2 = randint(1, 100)
    symb = choice(['+', '-', '*'])
    real_answer = calculate(num1, num2, symb)
    question = f'{num1} {symb} {num2}'
    return question, real_answer
