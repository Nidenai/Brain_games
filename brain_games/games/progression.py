from random import randint


TASK_TEXT = 'What number is missing in the progression?'


# создал функцию для создания прогрессии
def get_progression(start_number, step, length):
    result = [start_number]
    x = 0
    while x < length:
        start_number = start_number + step
        result.append(start_number)
        x = x + 1
    return result


def generate_round():
    first_num = randint(1, 100)
    step = randint(1, 100)
    lenght = randint(5, 9)
    progression = get_progression(first_num, step, lenght)
    index = randint(0, lenght)
    real_answer = progression[index]
    progression[index] = '..'
    question = ' '.join(map(str, progression))
    return question, real_answer

