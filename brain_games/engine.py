import prompt


WRONG_ANSWER = "' is wrong answer ;(. Correct answer was "
TOTAL_ROUND = 3


def run(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.TASK_TEXT)
    current_round = 0
    while current_round < TOTAL_ROUND:
        question, real_answer = game.generate_round()
        print('Question: ' + str(question))
        answer = prompt.string('Your answer:')
        if str(answer) == str(real_answer):
            print('Correct!')
            current_round += 1
        else:
            print("'" + str(answer) + WRONG_ANSWER + str(real_answer) + ".")
            print("Let's try again, " + name + '!')
            return
    print('Congratulations, ' + name + '!')
