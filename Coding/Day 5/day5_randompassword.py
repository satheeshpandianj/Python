import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Easy way to generate the random password letters+symbols+numbers
# password = "" # creating a empty string  variable to store password


# for char in range (1,nr_letters+1): # Looping through from 1 to number of letters required
#   random_charecter = random.choice(letters) # selecting random charecters from the list
#   # print(random_charecter) 
#   password += random_charecter # Adding the random charecters to the password variable
  
# for symbol in range (1,nr_symbols+1):  # Looping through from 1 to number of symbols required
#   random_symbol = random.choice(symbols) # selecting random symbols from the list
#   # print(random_symbol)
#   password += random_symbol # Adding the random symbol to the password variable
  
# for number in range (1,nr_numbers+1): # Looping through from 1 to number of numbers required
#   random_number = random.choice(numbers) # selecting random number from the list
#   # print(random_number)
#   password += random_number # Adding the random number to the password variable
  
# print(password)

#Easy way to generate the random password letters+symbols+numbers
# password = "" # creating a empty string  variable to store password
# for char in range (1,nr_letters + 1): # Looping through from 1 to number of letters required
#   rand_num = random.randint(1,len(letters)) # generating the random number within 1 to length of letters list
#   # print(rand_num)
#   # print(letters[rand_num - 1]) # selecting the letter based on the randomly generated number
#   password += letters[rand_num - 1] # Adding the random letter to the password variable
  
# for symbol in range (1,nr_symbols + 1):  # Looping through from 1 to number of symbols required
#   random_symbol = random.randint(1,len(symbols))  # selecting the symbol based on the randomly generated number
#   # print(random_symbol)
#   password += symbols[random_symbol - 1] # Adding the random symbol to the password variable
  
# for number in range (1,nr_numbers + 1):  # Looping through from 1 to number of numbers required
#   random_number = random.randint(1,len(numbers))  # selecting the number based on the randomly generated number
#   # print(random_number)
#   password += numbers[random_number - 1] # Adding the random number to the password variable
  
# print(password)

# Hard way to generate the random password (mixed of letters,symbols and numbers)

password_list = [] # creating a empty list variable to store password
for char in range (1,nr_letters+1): # Looping through from 1 to number of letters required
  random_charecter = random.choice(letters) # selecting the letter randomly from the letters list
  password_list.append(random_charecter) # Adding the random letter to the password list
  
for symbol in range (1,nr_symbols+1): # Looping through from 1 to number of symobls required
  random_symbol = random.choice(symbols) # selecting the symbol randomly from the symbols list
  # print(random_symbol)
  password_list.append(random_symbol) # Adding the random symbols to the password list
  
for number in range (1,nr_numbers+1): # Looping through from 1 to number of numbers required
  random_number = random.choice(numbers) # selecting the number randomly from the numbers list
  # print(random_number)
  password_list.append(random_number) # Adding the random number to the password list
  
print(f"Before reshuffling : {password_list}") # Print the list stored in password list

random.shuffle(password_list) # Shuffle the password list

print(f"After reshuffling : {password_list}")  # Print the shuffled list stored in password list

password = "" # create a empty string to store the password
for char in password_list: # Looping through password list
  password += char # Add each charecter to the password
print(password) # print the randomly generated password