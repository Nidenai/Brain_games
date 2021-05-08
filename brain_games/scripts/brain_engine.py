#!/usr/bin/env python
import prompt



def brain_play(function):
    (task_text, question, real_answer) = function
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    x = 0
    while x < 3:
        print(task_text)
        print('Question: ' + str(question))
        print('Your answer:', end='')
        answer = input()
        if str(answer) == str(real_answer):
            print('Correct!')
            x = x + 1
        else:
            print("'" + str(answer) + "' is wrong answer ;(. Correct answer was " + str(real_answer) + ".")
            break
    if x == 3:
        print('Congratulations, ' + name + '!')
    else:
        print("Let's try again, " + name + '!')