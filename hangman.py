

print('***** Welcome to Hangman *****')

# import section
import random
from words import words   #file is availabe in the folder and impor words means to import the variable
import string

# function which make a valid word in game
def get_valid_word(words):
    word = random.choice(words)
    while '-' in word and ' ' in word: #we add ----- on word
        word = random.choice(words)

    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letter = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()   #letter we will guess

    live = 5
    # get the user input
    while len(word_letter) > 0 or live == 0:
        if len(used_letters) > 0:
            print('You have used these letters: ', ' '.join(used_letters))

        print(f'Lives: {live}')
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))


        user_letter = input('Enter your letter you guess: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letter:
                word_letter.remove(user_letter)

        elif user_letter in used_letters:
            print('You have already used this letter.Please try again.')

        else:
            print('Invalid character.Try again')

        live = live - 1
        if live == 0:
            print('Your lives has been finished.BETTER LOCK NEXT TIME!')
            break

if __name__ == '__main__':
    hangman()