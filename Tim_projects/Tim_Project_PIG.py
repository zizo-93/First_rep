# Game based on getting as hig of a dice roll score as possible, on your turn you can roll the dice as many times as possible
# but if you get a 1 that will end your turn and only add +1 on your overall score. 
# Game can bet best of five turns, Or first to 50, etc. 

# STEPS: 1. import an random number generator (1-6) 2. Ask player to roll/coninue or roll again --> add score and switch player
#        3. Keep going untill player reaches 50 points. 4. Print the results. 

import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll


while True:
    player = input('How many players are there, please pick between 2-4: ')
    if player.isdigit():
        players = int(player)
        if  2 <= players <= 4:
            break
        else: 
            print('Invalid input, must be between 2-4')

max_score = 10 
player_scores = [0 for _ in range(players)]



def the_game():   
    while max(player_scores) < max_score:
        for player_idx in range(players):
            print(f'\n Player nmber: {player_idx +1 } turn has STARTED' )
            print(f'Your total score is {player_scores[player_idx]}\n')
            current_score = 0

            while True:
                roll_time = input('Do you want to roll? (y/n): ')
                if roll_time.lower() != 'y':
                    break

                value = roll() 
                if value == 1:
                    print(' You got a 1, turn over')
                    current_score = 0
                    break
                else:
                    current_score += value
                    print(f'You rolled a: {value}')

                print(f'Your current score is {current_score}')
                
            player_scores[player_idx] += current_score
            print(f'Your total score is {player_scores[player_idx]}')

the_game()

max_score = max(player_scores)
winning_idx = player_scores.index(max_score)

print(f'Player number {winning_idx + 1} is the winner with the score of {max_score} ')
        

