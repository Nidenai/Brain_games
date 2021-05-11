#!/usr/bin/env python
import prompt



def run(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    print(game.TASK_TEXT)
    x = 0
    while x < 3:
        question, real_answer = game.function()
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