from random import randint
from random import choice

def generate():
    random_num_one = randint(1, 100)
    randon_num_two = randint(1, 100)
    play_sum = str(random_num_one) + ' + ' + str(randon_num_two)
    real_sum = random_num_one + randon_num_two
    play_min = str(random_num_one) + ' - ' + str(randon_num_two)
    real_min = random_num_one - randon_num_two
    play_mult = str(random_num_one) + ' * ' + str(randon_num_two)
    real_mult = random_num_one * randon_num_two
    question = choice([play_sum, play_min, play_mult])
    if question[2] == '+' or question[3] == '+':
        real_answer = real_sum
    elif question[2] == '-' or question[3] == '-':
        real_answer = real_min
    else:
        real_answer = real_mult
    return(question, real_answer)

TASK_TEXT = 'What is the result of the expression?'