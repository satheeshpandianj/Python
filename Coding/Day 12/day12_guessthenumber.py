from art import logo
import random
print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
if level == 'hard':
    attempts = 5
    print("You have 5 attempts remaining to guess the number.")
elif level == 'easy':
    attempts = 10
    print("You have 10 attempts remaining to guess the number.")
else:
    attempts = 0
    print("Wrong input")
    

is_game_over = False


def compare(random_number,guess_number):
    if(random_number > guess_number):
        print(f"Too low")
        return False
    elif(guess_number > random_number):
        print(f"Too high")
        return False
    else:
        print(f"You got it!. The answer was {random_number}")
        return True


# Generate the random number  
random_number = random.randint(1, 100)  
print(f"random number generated : {random_number}")  

while not is_game_over:
    guess = int(input("Make a guess: "))
    result = compare(random_number,guess)
    if result:
       is_game_over = True 
    else:
        attempts -= 1
    
    if attempts == 0:
        print(f"Sorry you lose the game. The answer was {random_number}")  
        is_game_over = True    
        
    




