#!/usr/bin/env python
from random import randint
import prompt
from math import gcd


def random_nod_play():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    x = 0
    while x < 3:
        random_num_one = randint(1, 100)
        randon_num_two = randint(1, 100)
        print('Find the greatest common divisor of given numbers')
        print('Question: ' + str(random_num_one) + ', ' + str(randon_num_two))
        print('Your answer:', end='')
        answer = int(input())
        real_answer = gcd(random_num_one, randon_num_two)
        if answer == real_answer:
            x = x + 1
            print('Correct!')
        else:
            print("'" + str(answer) + "' is wrong answer ;(. Correct answer was '" + str(real_answer) + "'")
            break
    if x == 3:
        print('Congratulations, ' + name + '!')
    else:
        print("Let's try again, " + name + '!' )

def main():
    random_nod_play()

if __name__ == '__main__':
    main()