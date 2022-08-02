# Hangaman Game
# Step 1 : Create a random word
# Step 2 : Create as many blanks as random word characters
#### BELOW IS REPEATED UNTIL GAME IS OVER
# Step 3 : Get the input letter from user
# Step 4 : Compare the user input with the random word. If user input letter matches, any of the character from random word
#          then replace the letter in the random word. Else, reduce the life
# Step 5 : Count the lives and validate against 0. If life count is more than 0, then go and get the user input. Else, end the game

# import the modules

import random
import os
from day7_hangman_wordlist import word_list
from day7_hangman_art import stages, logo

# printing the hangman logo from day7_hangman_art file.
print(f"{logo[0]}")

# Getting the word list from day7_hangman_wordlist file.
word_list = word_list

#Randomly choose the word from the word list created.
chosen_word = random.choice(word_list)
print(f"The random word is : {chosen_word}")

# Create the list with blanks based on the chosen word length
display = []
for _ in range(1,len(chosen_word)+1):
    display += "_"

# set the lives based on the stages length
lives = len(stages) - 1

# This is for while condition loop.
end_of_game = False

# until game ends, Ask the user to input the letter
while not end_of_game:
    guess = input("Guess a letter : ")
    guess = guess.lower() # convert user input into lower case
    os.system("clear")
    count = 0 # To store how many times the user input letter checked against the random word at a time
    
    for position in range(len(chosen_word)):   
        # Check if the guessed letter is present in the chosen word, else increase the count
        if(chosen_word[position] == guess):
            display[position] = chosen_word[position] # Replace "_" with the guessed letter 
            print(f"{stages[lives]}") # Print the current stage of the game 
        else:
            count += 1 
    
    # Check count matches the random word length. If so, reduce the lives. For example
    # You random word is apple, user entered "k". In the first iteration, k will validate against 
    # all letter in "apple". It doesnt match any of the letter, hence, lives decreased by 1
    if (count == len(chosen_word)): 
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life")
        print(f"{stages[lives]}")
    
    print(display)
    
    # Check "_" is available in display list. If its not available, which means the game is over and user wins.
    if "_" not in display:
        end_of_game = True
        print("You Win!!!")
    
    # Check  lives is less than or equal to 0, which means the game is over and user lose.
    if lives <= 0:
        end_of_game = True
        print("You Lose!!!")        