from random import randint

#создал функцию для создания арифметической прогрессии. Потому что найти ничего подобного не нашел.
def ar_progress(start_number, step, length):
    result = [start_number]
    x = 0
    while x < length:
        start_number = start_number + step
        result.append(start_number)
        x = x + 1
    return result

def function():
    first_num = randint(1, 100)
    list_step = randint(1, 100)
    list_lenght = randint(5, 9)
    rand_progress = ar_progress(first_num, list_step, list_lenght)
    random_element = randint(0, (len(rand_progress)-1))
    real_answer = rand_progress[random_element]
    question = rand_progress
    question.pop(random_element)
    question.insert(random_element, "..")
    return (question, real_answer)

TASK_TEXT = 'What number is missing in the progression?'