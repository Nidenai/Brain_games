import prompt


def run(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.TASK_TEXT)
    current_round = 0
    TOTAL_ROUND = 3
    while current_round < TOTAL_ROUND:
        question, real_answer = game.generate()
        print('Question: ' + str(question))
        print('Your answer:', end='')
        answer = input()
        if str(answer) == str(real_answer):
            print('Correct!')
            current_round = current_round + 1
        else:
            print("'" + str(answer) + "' is wrong answer ;(. Correct answer was " + str(real_answer) + ".")
            break
    if current_round == TOTAL_ROUND:
        print('Congratulations, ' + name + '!')
    else:
        print("Let's try again, " + name + '!')