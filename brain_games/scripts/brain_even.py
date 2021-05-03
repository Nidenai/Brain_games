#!/usr/bin/env python
from random import randint
import prompt


def random_play():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    x = 0
    while x < 3:
        random_num = randint(1, 100)
        print("Question:" + str(random_num))
        print('Your answer:', end='')
        answer = input()
        if answer == 'yes' and (random_num % 2) == 0:
            x = x + 1
            print("Correct!")
        elif answer == 'yes' and (random_num % 2) == 1:
            print("'" + answer + "' is wrong answer ;(. Correct answer was 'no'.")
            break
        elif answer == 'no' and (random_num % 2) == 1:
            x = x + 1
            print("Correct!")
        else:
            print("'" + answer + "' is wrong answer ;(. Correct answer was 'yes'.")
            break
    if x == 3:
        print('Congratulations, ' + name + '!')
    else:
        print("Let's try again, " + name + '!' )

def main():
    random_play()

if __name__ == '__main__':
    main()