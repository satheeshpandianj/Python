# TO DO 1 :
# Generate a random number to get the value of first person
# import the random module
import random
# Import the data 
from game import data
from art import logo, vs
import os

# print(random.choice(data))
# Get the data length
#print(len(data))  
def generate_random(data):
    # Generate the random number within the data length
    return random.randint(0,len(data) - 1)
    #print(random_number)

def get_follower_count(name):
    # TO DO 4 :
    # Get the followers count for first person
    first_follower_count = data[name]['follower_count']
    return first_follower_count



# TO DO 6 :
# Compare the followers count and save it in a variable
def compare(first_follower_count,second_follower_count):
    if first_follower_count > second_follower_count:
        return 'A'
    else:
        return 'B'

first_random_number = generate_random(data)

is_game_over = False
score = 0
while not is_game_over:
    os.system('clear')
    print(logo)
    print(f"Your current score : {score}")
    print(f"Compare A: {data[first_random_number]['name']}, A {data[first_random_number]['description']}, from {data[first_random_number]['country']}")
    second_random_number = generate_random(data)
    while first_random_number == second_random_number:
        second_random_number = generate_random(data)
        
    # TO DO 3 :
    # Check if both random numbers are same or not. If it is same, generate a new number for second person
    # print(f"{first_random_number} {second_random_number}") 
    print(vs)
    print(f"Compare B: {data[second_random_number]['name']}, A {data[second_random_number]['description']}, from {data[second_random_number]['country']}")

    first_follower_count = get_follower_count(first_random_number)
    second_follower_count = get_follower_count(second_random_number)
    print(f"{first_follower_count} {second_follower_count}") 
    result = compare(first_follower_count,second_follower_count)
    print(f"result : {result}") 
    # TO DO 7 :
    # Get the user the input and compare against the result stored in TO DO 6
    user_choice = input("Who has more followers? Type 'A' or 'B': ").upper()

    # TO DO 8 :
    # Increase the score varible if it is right and store the second person details as first person now.
        # TO DO 9 :
        # If it is wrong, display the user score and ask if they want to play again.    
    if user_choice == result:
        score += 1
        # print(f"You 're right! Your current score : {score}")
        data[first_random_number]['name'] = data[second_random_number]['name']
        data[first_random_number]['description'] = data[second_random_number]['description']
        data[first_random_number]['country'] = data[second_random_number]['country']
        data[first_random_number]['follower_count'] = data[second_random_number]['follower_count']
        print(f"Compare A: {data[first_random_number]['name']}, A {data[first_random_number]['description']}, from {data[first_random_number]['country']}")   
    else:
        # os.system('clear')
        print(f"Your current score : {score}")
        is_game_over = True


######################## ANOTHER WAY #########################






