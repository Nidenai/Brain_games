#!/usr/bin/env python
from random import randint
import prompt


def IsPrime(n):
    d = 2
    while d * d <= n and n % d != 0:
        d += 1
    return d * d > n


def prime_game():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    x = 0
    while x < 3:
        print('Answer "yes" if given number is prime. Otherwise answer "no".')
        middle_num = randint(2, 1000)
        print('Question: ' + str(middle_num))
        print('Your answer:', end='')
        required_num = IsPrime(middle_num)
        answer = input()
        if answer == 'yes' and (required_num == True):
            print('Correct!')
            x = x + 1
        elif answer == 'no' and (required_num == False):
            print('Correct!')
            x = x + 1
        elif answer != 'no' and (required_num == False):
            print("'" + str(answer) + "' is wrong answer ;(. Correct answer was 'no'.")
            break
        elif answer != 'yes' and (required_num == True):
            print("'" + str(answer) + "' is wrong answer ;(. Correct answer was 'yes'.")
            break
    if x == 3:
        print('Congratulations, ' + name + '!')
    else:
        print("Let's try again, " + name + '!')


def main():
    prime_game()

if __name__ == '__main__':
    main()