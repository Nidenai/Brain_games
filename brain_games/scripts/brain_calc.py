from random import randint
from random import choice
import prompt


def random_calc_play():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    x = 0
    while x < 3:
        random_num_one = randint(1, 100)
        randon_num_two = randint(1, 100)
        play_sum = str(random_num_one) + ' + ' + str(randon_num_two)
        real_sum = random_num_one + randon_num_two
        play_min = str(random_num_one) + ' - ' + str(randon_num_two)
        real_min = random_num_one - randon_num_two
        play_mult = str(random_num_one) + ' * ' + str(randon_num_two)
        real_mult = random_num_one * randon_num_two
        random_game = choice([play_sum, play_min, play_mult])
        print('What is the result of the expression?')
        print('Question: ' + random_game)
        print('Your answer:', end='')
        answer = int(input())
        if random_game[2] == '+' or random_game[3] == '+':
            real_answer = real_sum
        elif random_game[2] == '-' or random_game[3] == '-':
            real_answer = real_min
        else:
            real_answer = real_mult
        print(real_answer)

        if real_answer == answer:
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
    random_calc_play()

if __name__ == '__main__':
    main()