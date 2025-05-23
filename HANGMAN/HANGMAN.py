import numpy as np
from STAGES import *
from WORD_LIST import *
from COLORS import *
from FUNCTIONS import *

# USE NUMPY RANDOM CHOICE FUNCTION TO CHOOSE A RANDOM WORD
selected_word = np.random.choice(words).upper()

# CONSTANTS
player_lives = 6
game_over = False
correct_letters = []
word_bank = []

title()
print(rgb(f"YOUR SELECTED WORD IS [{len(selected_word)}] LETTERS LONG!\nGOOD LUCK!\n", PEACH))
print(rgb("#"*44, GOLD))

while not game_over:
    # ASK THE USER TO GUESS A LETTER - USE INPUT()
    print(rgb(f"\nREMAINING LIVES: {player_lives}", RED))
    guess = input(rgb("GUESS A LETTER ==> ", WHITE)).upper()
    print(rgb("-"*44, PEACH))

    if guess in word_bank:
        print(rgb(f"GUESS AGAIN. {guess} HAS ALREADY BEEN USED.\n", WHITE))

    elif guess in selected_word:
        print(rgb("YOU HAVE A GUESSED A LETTER IN THE WORD!\nNICE JOB! 🤩", WHITE))
        correct_letters.append(guess)

    else:
        print(rgb(f"YOU HAVE GUESSED A LETTER NOT IN THE WORD.\nLOSE A LIFE! 🥲", WHITE))
        player_lives -= 1

    if guess not in word_bank:
        word_bank.append(guess)

    display = ''.join([x if x in correct_letters else '_' for x in selected_word])      

    print(rgb(STAGES[player_lives], PEACH))
    print(rgb(f"WORD: {display} \nWORD BANK: {word_bank}", WHITE))
    print(rgb("#"*44, GOLD))

    if player_lives == 0:
        game_over = True
        print(rgb(f"\nYOU WERE UNSUCCESSFUL IN GUESSING THE WORD {selected_word}!\nYOU LOSE! :)", WHITE))

    if "_" not in display:
        game_over = True
        print(rgb("\nYOU HAVE SUCCESSFULLY GUESSED THE WORD!\nYOU WIN! :)", WHITE))
