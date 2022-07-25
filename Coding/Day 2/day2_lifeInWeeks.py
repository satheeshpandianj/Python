# Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.

# It will take your current age as the input and output a message with our time left in this format:

# You have x days, y weeks, and z months left.

# Where x, y and z are replaced with the actual calculated numbers.

# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
remaining_years = 90 - int(age)
number_of_days = remaining_years * 365
number_of_weeks = remaining_years * 52
number_of_months = remaining_years * 12

print(f"You have {number_of_days} days, {number_of_weeks} weeks, and {number_of_months} months left")

