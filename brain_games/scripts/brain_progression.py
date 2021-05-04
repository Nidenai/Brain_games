#!/usr/bin/env python
from random import randint
import prompt

#создал функцию для создания арифметической прогрессии. Потому что найти ничего подобного не нашел.
def ar_progress(start_number, step, length):
    result = [start_number]
    x = 0
    while x < length:
        start_number = start_number + step
        result.append(start_number)
        x = x + 1
    return result

def progression_play():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    x = 0
    while x < 3:
        first_num = randint(1, 100)
        list_step = randint(1, 100)
        list_lenght = randint(5, 9)
        rand_progress = ar_progress(first_num, list_step, list_lenght)
        random_element = randint(0, len(rand_progress))
        real_answer = rand_progress[random_element]
        list_for_user = rand_progress
        list_for_user.pop(random_element)
        list_for_user.insert(random_element, "..")
        print('What number is missing in the progression?')
        print('Question: ' + ' '.join(map(str, list_for_user)))
        print('Your answer:', end='')
        answer = int(input())
        if answer == real_answer:
            x = x + 1
            print('Correct!')
        else:
            print("'" + str(answer) + "' is wrong answer ;(. Correct answer was '" + str(real_answer) + "'")
            break
    if x == 3:
        print('Congratulations, ' + name + '!')
    else:
        print("Let's try again, " + name + '!')

def main():
    progression_play()

if __name__ == '__main__':
    main()