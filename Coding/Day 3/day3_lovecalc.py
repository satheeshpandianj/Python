# You are going to write a program that tests the compatibility between two people.
# To work out the love score between two people:
# Take both people's names and check for the number of times the letters in the word TRUE occurs. 
# Then check for the number of times the letters in the word LOVE occurs. 
# Then combine these numbers to make a 2 digit number.
  # For Love Scores less than 10 or greater than 90, the message should be:
  # "Your score is **x**, you go together like coke and mentos."
  # For Love Scores between 40 and 50, the message should be:
  # "Your score is **y**, you are alright together."
  # Otherwise, the message will just be their score. e.g.:
  # "Your score is **z**."
  
  # 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

t_count = name1.lower().count("t") + name2.lower().count("t")
r_count = name1.lower().count("r") + name2.lower().count("r")
u_count = name1.lower().count("u") + name2.lower().count("u")
e_count = name1.lower().count("e") + name2.lower().count("e")

true_total = t_count + r_count + u_count + e_count
# print(true_total)

l_count = name1.lower().count("l") + name2.lower().count("l")
o_count = name1.lower().count("o") + name2.lower().count("o")
v_count = name1.lower().count("v") + name2.lower().count("v")
e_count = name1.lower().count("e") + name2.lower().count("e")
love_total = l_count + o_count + v_count + e_count
# print(love_total)
digit = str(true_total) + str(love_total)
# print(type(digit))
digit = int(digit)
# print((digit))

if digit < 10 or digit > 90:
    print(f"Your score is {digit}, you go together like coke and mentos.")
elif digit > 40 and digit <= 50:
    print(f"Your score is {digit}, you are alright together.")
else:
    print(f"Your score is {digit}.")    
