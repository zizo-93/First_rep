
import random 


def conclusion(word_display):
    if '_' not in word_display:
        print('Yeah, guessed the word and survived')
        print(f'The word was {the_word}')

    else:
        print('LOL you died')
        print(f'The word was {the_word}')

def letter_check(the_word, guess, word_display, attempts):
    if guess in the_word:
        for index, letter in enumerate(the_word):
            if letter == guess:
                word_display[index] = guess
                print('Letter was found in word, Nice!')
    else:
        print('Letter does not exist in word, LoL')
        print(f'You have {attempts} left')
        attempts -= 1



words = ['strong', 'weak', 'light', 'heavy']

the_word = random.choice(words)
word_display = ['_' for _ in the_word]
attempts = 8

print('Welcome to Hangman')


def play_game(attempts):  
    while attempts > 0 and '_' in word_display:
        print('\n' + ' '.join(word_display)) 

        guess = input('guess a letter: ').lower()
    
        if guess in the_word:
            for index, letter in enumerate(the_word):
                if letter == guess:
                    word_display[index] = guess
                    print('Letter was found in word, Nice!')
        else:
            print('Letter does not exist in word, LoL')
            print(f'You have {attempts} left')
            attempts -= 1

    conclusion(word_display)



play_game(attempts)



         