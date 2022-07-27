import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''



user_choice = int(input(f"What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: \n"))
# print(user_choice)
computer_choice = random.randint(0,2)
# print(computer_choice)
if (user_choice >= 3) or (user_choice < 0):
  print(f"You typed an wrong value")
else: 
  images = [rock, paper,scissors]
  print(f"You chose: \n")
  print(images[user_choice])
  print(f"Computer chose: \n")
  print(images[computer_choice])

  if(computer_choice == user_choice):
    print(f"Match draw")
  elif (computer_choice == 0) and (user_choice == 2):
    print(f"You lose!")
  elif (computer_choice == 2) and (user_choice == 0):
    print(f"You win!")
  elif (computer_choice > user_choice):
    print(f"You lose!")
  elif (computer_choice < user_choice):
    print(f"You Win!")

  