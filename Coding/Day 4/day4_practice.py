import random
# import day4_mymodule

# random_integer = random.randint(1,10);
# print(random_integer)
# print(day4_mymodule.pi)

# random_float = random.random()
# print(random_float)


random.seed(3)
  
# print a random number between 1 and 1000.
print(random.randint(1, 1000))
  
# if you want to get the same random number again then,
random.seed(3) 
print(random.randint(1, 1000))
  
# If seed function is not used
  
# Gives totally unpredictable responses.
print(random.randint(1, 1000))