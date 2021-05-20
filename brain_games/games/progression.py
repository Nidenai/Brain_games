from random import randint


# создал функцию для создания прогрессии
def ar_progress(start_number, step, length):
    result = [start_number]
    x = 0
    while x < length:
        start_number = start_number + step
        result.append(start_number)
        x = x + 1
    return result


def generate():
    first_num = randint(1, 100)
    list_step = randint(1, 100)
    list_lenght = randint(5, 9)
    rand_progress = ar_progress(first_num, list_step, list_lenght)
    random_element = randint(0, (len(rand_progress) - 1))
    real_answer = rand_progress[random_element]
    list_middle = rand_progress
    list_middle.pop(random_element)
    list_middle.insert(random_element, "..")
    question = ' '.join(map(str, list_middle))
    return (question, real_answer)


TASK_TEXT = 'What number is missing in the progression?'
