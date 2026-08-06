import random
import time



OPERATORS = ['+', '-', '*']
MIN_OPERAND = 3
MAX_OPERAND = 12
TOTAL_PROBLEMS = 5


def generate_problem():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)

    expr = str(left) + ' ' + operator + ' ' + str(right)
    answer = eval(expr)

    return expr, answer


wrong = 0
input('Press enter to start!')
print('---------------------')

start_time = round(time.time())

def the_game():
    for i in range(TOTAL_PROBLEMS):
        expr, answer = generate_problem()
        while True:
            guess = input('Problem #' + str(i + 1) + ': ' + expr + '= ')
            if guess == str(answer):
                break
            wrong += 1

the_game()

end_time = round(time.time())
total_time = end_time - start_time

print('Nice work!')
print(f'You got {wrong} wrong answers and your time was {total_time} seconds!')



    

